cd ETU && \
export HUGGING_FACE_HUB_TOKEN="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" && \
echo "🔑 토큰 설정 완료" && \
echo "📥 cyber-forget-corpus 다운로드 중..." && \
huggingface-cli download cais/wmdp-corpora cyber-forget-corpus --local-dir ./datasets/cyber-forget && \
echo "📥 cyber-retain-corpus 다운로드 중..." && \
huggingface-cli download cais/wmdp-corpora cyber-retain-corpus --local-dir ./datasets/cyber-retain && \
echo "📥 bio-forget-corpus 다운로드 중..." && \
huggingface-cli download cais/wmdp-bio-forget-corpus --local-dir ./datasets/bio-forget && \
echo "📥 bio-retain-corpus 다운로드 중..." && \
huggingface-cli download cais/wmdp-corpora bio-retain-corpus --local-dir ./datasets/bio-retain && \
echo "📥 wikitext 다운로드 중..." && \
huggingface-cli download wikitext wikitext-2-raw-v1 --local-dir ./datasets/wikitext && \
echo "✅ 모든 데이터셋 다운로드 완료!"
