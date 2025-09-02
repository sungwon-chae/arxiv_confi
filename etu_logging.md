#!/usr/bin/env bash
set -euo pipefail

# 0) 저장 폴더
mkdir -p ./datasets/cyber-forget ./datasets/cyber-retain ./datasets/bio-forget ./datasets/bio-retain ./datasets/wikitext

# 1) 토큰 (환경변수로만 사용; 로그인 과정 없이도 인식됨)
export HUGGING_FACE_HUB_TOKEN="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"
: "${HUGGING_FACE_HUB_TOKEN:?HUGGING_FACE_HUB_TOKEN is required}"

# 2) 다운로드 커맨드 결정: hf(신규) 우선, 없으면 huggingface-cli(구버전)
if command -v hf >/dev/null 2>&1; then
  DL_CMD=("hf" "download")
else
  echo "⚠️  'hf'가 없어 'huggingface-cli'를 사용합니다. (권장: pip install -U huggingface_hub)"
  DL_CMD=("huggingface-cli" "download")
fi

# 헬퍼 함수
dl_dataset () {
  # $1: repo_id, $2: local_dir, $3+: extra args (예: --include "subdir/**")
  "${DL_CMD[@]}" "$1" --repo-type dataset --local-dir "$2" "${@:3}"
}

# 3) 개별 다운로드
# - wmdp-corpora 레포에서 특정 서브폴더만 선택
dl_dataset "cais/wmdp-corpora"            "./datasets/cyber-forget" --include "cyber-forget-corpus/**"
dl_dataset "cais/wmdp-corpora"            "./datasets/cyber-retain" --include "cyber-retain-corpus/**"
dl_dataset "cais/wmdp-bio-forget-corpus"  "./datasets/bio-forget"
dl_dataset "cais/wmdp-corpora"            "./datasets/bio-retain"  --include "bio-retain-corpus/**"

# - Salesforce/wikitext에서 wikitext-2-raw-v1만 선택
dl_dataset "Salesforce/wikitext"          "./datasets/wikitext"    --include "wikitext-2-raw-v1/**"

echo "✅ All datasets downloaded successfully."
