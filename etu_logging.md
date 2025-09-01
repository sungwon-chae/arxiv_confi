(LLM_EvalPipeline_test) aiuser3@ai-smartlaw:~/ETU$ python -c "
import os
from datasets import load_dataset

# 토큰 설정
token = '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'

try:
    # bio-forget 데이터셋 로드
    ds = load_dataset('cais/wmdp-bio-forget-corpus', 
                     split='train', 
                     token=token,
                     cache_dir='./data_cache')
    print(f'✅ Success! Loaded {len(ds)} rows')
    print(f'Features: {ds.features}')
    if len(ds) > 0:
        print(f'First row preview: {str(ds[0])[:200]}...')
except Exception as e:
    print(f'❌ Error: {e}')
    import traceback
    traceback.print_exc()
"
Downloading readme: 100%|████████████████████████████████████████████| 1.16k/1.16k [00:00<00:00, 10.2MB/s]
HF google storage unreachable. Downloading and preparing it from source
Downloading data: 100%|████████████████████████████████████████████████| 204M/204M [00:11<00:00, 17.3MB/s]
Downloading data: 100%|████████████████████████████████████████████████| 178M/178M [00:14<00:00, 12.7MB/s]
❌ Error: Couldn't find file at https://huggingface.co/datasets/cais/wmdp-bio-forget-corpus/resolve/5a786ed1041e56fef2d4ed26c1239f12b73a68eb/./data_cache/downloads/0e4e464321ebd459c9627cd96fac70061da719731c916c0f105dacbb428964c6
Traceback (most recent call last):
  File "<string>", line 10, in <module>
  File "/data/aiuser3/LLM_EvalPipeline_test/.venv/lib/python3.12/site-packages/datasets/load.py", line 2545, in load_dataset
    builder_instance.download_and_prepare(
  File "/data/aiuser3/LLM_EvalPipeline_test/.venv/lib/python3.12/site-packages/datasets/builder.py", line 1003, in download_and_prepare
    self._download_and_prepare(
  File "/data/aiuser3/LLM_EvalPipeline_test/.venv/lib/python3.12/site-packages/datasets/builder.py", line 1076, in _download_and_prepare
    split_generators = self._split_generators(dl_manager, **split_generators_kwargs)
                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/data/aiuser3/LLM_EvalPipeline_test/.venv/lib/python3.12/site-packages/datasets/packaged_modules/parquet/parquet.py", line 43, in _split_generators
    data_files = dl_manager.download_and_extract(self.config.data_files)
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/data/aiuser3/LLM_EvalPipeline_test/.venv/lib/python3.12/site-packages/datasets/download/download_manager.py", line 566, in download_and_extract
    return self.extract(self.download(url_or_urls))
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/data/aiuser3/LLM_EvalPipeline_test/.venv/lib/python3.12/site-packages/datasets/download/download_manager.py", line 539, in extract
    extracted_paths = map_nested(
                      ^^^^^^^^^^^
  File "/data/aiuser3/LLM_EvalPipeline_test/.venv/lib/python3.12/site-packages/datasets/utils/py_utils.py", line 467, in map_nested
    _single_map_nested((function, obj, types, None, True, None))
  File "/data/aiuser3/LLM_EvalPipeline_test/.venv/lib/python3.12/site-packages/datasets/utils/py_utils.py", line 387, in _single_map_nested
    mapped = [_single_map_nested((function, v, types, None, True, None)) for v in pbar]
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/data/aiuser3/LLM_EvalPipeline_test/.venv/lib/python3.12/site-packages/datasets/utils/py_utils.py", line 370, in _single_map_nested
    return function(data_struct)
           ^^^^^^^^^^^^^^^^^^^^^
  File "/data/aiuser3/LLM_EvalPipeline_test/.venv/lib/python3.12/site-packages/datasets/download/download_manager.py", line 451, in _download
    out = cached_path(url_or_filename, download_config=download_config)
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/data/aiuser3/LLM_EvalPipeline_test/.venv/lib/python3.12/site-packages/datasets/utils/file_utils.py", line 188, in cached_path
    output_path = get_from_cache(
                  ^^^^^^^^^^^^^^^
  File "/data/aiuser3/LLM_EvalPipeline_test/.venv/lib/python3.12/site-packages/datasets/utils/file_utils.py", line 570, in get_from_cache
    raise FileNotFoundError(f"Couldn't find file at {url}")
FileNotFoundError: Couldn't find file at https://huggingface.co/datasets/cais/wmdp-bio-forget-corpus/resolve/5a786ed1041e56fef2d4ed26c1239f12b73a68eb/./data_cache/downloads/0e4e464321ebd459c9627cd96fac70061da719731c916c0f105dacbb428964c6
(LLM_EvalPipeline_test) aiuser3@ai-smartlaw:~/ETU$ 
