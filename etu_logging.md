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

(LLM_EvalPipeline_test) aiuser3@ai-smartlaw:~/ETU$ huggingface-cli download cais/wmdp-corpora cyber-forget-corpus --local-dir ./datasets/cyber-forget
⚠️  Warning: 'huggingface-cli download' is deprecated. Use 'hf download' instead.
Traceback (most recent call last):
  File "/data/aiuser3/LLM_EvalPipeline_test/.venv/lib/python3.12/site-packages/huggingface_hub/utils/_http.py", line 409, in hf_raise_for_status
    response.raise_for_status()
  File "/data/aiuser3/LLM_EvalPipeline_test/.venv/lib/python3.12/site-packages/requests/models.py", line 1026, in raise_for_status
    raise HTTPError(http_error_msg, response=self)
requests.exceptions.HTTPError: 404 Client Error: Not Found for url: https://huggingface.co/cais/wmdp-corpora/resolve/main/cyber-forget-corpus

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/data/aiuser3/LLM_EvalPipeline_test/.venv/bin/huggingface-cli", line 10, in <module>
    sys.exit(main())
             ^^^^^^
  File "/data/aiuser3/LLM_EvalPipeline_test/.venv/lib/python3.12/site-packages/huggingface_hub/commands/huggingface_cli.py", line 61, in main
    service.run()
  File "/data/aiuser3/LLM_EvalPipeline_test/.venv/lib/python3.12/site-packages/huggingface_hub/commands/download.py", line 157, in run
    print(self._download())  # Print path to downloaded files
          ^^^^^^^^^^^^^^^^
  File "/data/aiuser3/LLM_EvalPipeline_test/.venv/lib/python3.12/site-packages/huggingface_hub/commands/download.py", line 170, in _download
    return hf_hub_download(
           ^^^^^^^^^^^^^^^^
  File "/data/aiuser3/LLM_EvalPipeline_test/.venv/lib/python3.12/site-packages/huggingface_hub/utils/_validators.py", line 114, in _inner_fn
    return fn(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^
  File "/data/aiuser3/LLM_EvalPipeline_test/.venv/lib/python3.12/site-packages/huggingface_hub/file_download.py", line 988, in hf_hub_download
    return _hf_hub_download_to_local_dir(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/data/aiuser3/LLM_EvalPipeline_test/.venv/lib/python3.12/site-packages/huggingface_hub/file_download.py", line 1251, in _hf_hub_download_to_local_dir
    _raise_on_head_call_error(head_call_error, force_download, local_files_only)
  File "/data/aiuser3/LLM_EvalPipeline_test/.venv/lib/python3.12/site-packages/huggingface_hub/file_download.py", line 1656, in _raise_on_head_call_error
    raise head_call_error
  File "/data/aiuser3/LLM_EvalPipeline_test/.venv/lib/python3.12/site-packages/huggingface_hub/file_download.py", line 1544, in _get_metadata_or_catch_error
    metadata = get_hf_file_metadata(
               ^^^^^^^^^^^^^^^^^^^^^
  File "/data/aiuser3/LLM_EvalPipeline_test/.venv/lib/python3.12/site-packages/huggingface_hub/utils/_validators.py", line 114, in _inner_fn
    return fn(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^
  File "/data/aiuser3/LLM_EvalPipeline_test/.venv/lib/python3.12/site-packages/huggingface_hub/file_download.py", line 1461, in get_hf_file_metadata
    r = _request_wrapper(
        ^^^^^^^^^^^^^^^^^
  File "/data/aiuser3/LLM_EvalPipeline_test/.venv/lib/python3.12/site-packages/huggingface_hub/file_download.py", line 286, in _request_wrapper
    response = _request_wrapper(
               ^^^^^^^^^^^^^^^^^
  File "/data/aiuser3/LLM_EvalPipeline_test/.venv/lib/python3.12/site-packages/huggingface_hub/file_download.py", line 310, in _request_wrapper
    hf_raise_for_status(response)
  File "/data/aiuser3/LLM_EvalPipeline_test/.venv/lib/python3.12/site-packages/huggingface_hub/utils/_http.py", line 459, in hf_raise_for_status
    raise _format(RepositoryNotFoundError, message, response) from e
huggingface_hub.errors.RepositoryNotFoundError: 404 Client Error. (Request ID: Root=1-68b6684b-3f6637e0088b1be0366ddc15;3a26dc59-0b2c-40ef-b993-39062eee52f1)

Repository Not Found for url: https://huggingface.co/cais/wmdp-corpora/resolve/main/cyber-forget-corpus.
Please make sure you specified the correct `repo_id` and `repo_type`.
If you are trying to access a private or gated repo, make sure you are authenticated. For more details, see https://huggingface.co/docs/huggingface_hub/authentication
