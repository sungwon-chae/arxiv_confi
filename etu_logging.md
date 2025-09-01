
def get_data(forget_corpora, retain_corpora, min_len=50, max_len=2000, batch_size=4):
    """
    Flexible loader for WMDP + WikiText + local files:
    - "bio:forget", "cyber:forget"
    - "bio:retain", "cyber:retain"
    - "wikitext"
    - local file paths
    """
    from datasets import load_dataset
    import os

    def normalize_text(rec):
        if 'text' in rec and isinstance(rec['text'], str):
            return rec['text']
        parts = []
        for k in ['question', 'prompt', 'instruction']:
            if k in rec and isinstance(rec[k], str):
                parts.append(rec[k])
        if 'choices' in rec and isinstance(rec['choices'], (list, tuple)):
            parts.append("Choices: " + " | ".join(map(str, rec['choices'])))
        for k in ['context', 'passage', 'body', 'response', 'completion']:
            if k in rec and isinstance(rec[k], str):
                parts.append(rec[k])
        return " ".join(parts) if parts else str(rec)

    def load_local_file(file_path):
        """로컬 파일에서 텍스트 로드"""
        data = []
        try:
            if os.path.isfile(file_path):
                with open(file_path, 'r', encoding='utf-8') as f:
                    text = f.read().strip()
                    if min_len < len(text) <= max_len:
                        data.append(text)
                    else:
                        # 긴 텍스트를 청크로 분할
                        words = text.split()
                        current_chunk = []
                        for word in words:
                            current_chunk.append(word)
                            chunk_text = " ".join(current_chunk)
                            if min_len < len(chunk_text) <= max_len:
                                data.append(chunk_text)
                                current_chunk = []
                        # 마지막 청크 처리
                        if current_chunk:
                            chunk_text = " ".join(current_chunk)
                            if min_len < len(chunk_text) <= max_len:
                                data.append(chunk_text)
            return data
        except Exception as e:
            print(f"Warning: Failed to load local file {file_path}: {e}")
            return []

    def load_wmdp(domain, role):
        data = []
        # 1) 전용 데이터셋 시도 (예: cais/wmdp-bio-forget-corpus)
        try:
            ds = load_dataset(f"cais/wmdp-{domain}-{role}-corpus", split="train", cache_dir="./data_cache")
            for rec in ds:
                txt = normalize_text(rec)
                if min_len < len(txt) <= max_len:
                    data.append(txt)
            return data
        except Exception:
            pass
        # 2) 통합 데이터셋 시도 (cais/wmdp-corpora config=bio/cyber)
        try:
            ds = load_dataset("cais/wmdp-corpora", domain, split="train", cache_dir="./data_cache")
            role_key = None
            for k in ['role', 'split', 'subset', 'category', 'part']:
                if k in ds.features:
                    role_key = k; break
            if role_key:
                ds = ds.filter(lambda x: str(x.get(role_key, "")).lower() == role)
            for rec in ds:
                txt = normalize_text(rec)
                if min_len < len(txt) <= max_len:
                    data.append(txt)
            return data
        except Exception:
            return []

    def load_corpus(spec):
        spec = spec.strip()
        # 로컬 파일 경로 확인
        if os.path.exists(spec):
            return load_local_file(spec)
        
        spec_lower = spec.lower()
        if spec_lower == "wikitext":
            raw = load_dataset("wikitext", "wikitext-2-raw-v1", split="test", cache_dir="./data_cache")
            return [str(x['text']) for x in raw if len(x['text']) > min_len]
        if ":" in spec_lower:
            dom, role = spec_lower.split(":")
            return load_wmdp(dom, role)
        return []

    def to_batches(data):
        return [data[i:i+batch_size] for i in range(0, len(data), batch_size)]

    return (
        [to_batches(load_corpus(c)) for c in forget_corpora],
        [to_batches(load_corpus(c)) for c in retain_corpora],
    )
