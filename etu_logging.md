mkdir -p ./datasets/cyber-forget ./datasets/cyber-retain ./datasets/bio-forget ./datasets/bio-retain ./datasets/wikitext

export HUGGING_FACE_HUB_TOKEN="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"

huggingface-cli download cais/wmdp-corpora cyber-forget-corpus --repo-type dataset --local-dir ./datasets/cyber-forget

huggingface-cli download cais/wmdp-corpora cyber-retain-corpus --repo-type dataset --local-dir ./datasets/cyber-retain

huggingface-cli download cais/wmdp-bio-forget-corpus --repo-type dataset --local-dir ./datasets/bio-forget

huggingface-cli download cais/wmdp-corpora bio-retain-corpus --repo-type dataset --local-dir ./datasets/bio-retain

huggingface-cli download wikitext wikitext-2-raw-v1 --repo-type dataset --local-dir ./datasets/wikitext
