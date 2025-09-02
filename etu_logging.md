mkdir -p ./datasets/cyber-forget ./datasets/cyber-retain ./datasets/bio-forget ./datasets/bio-retain ./datasets/wikitext

export HUGGING_FACE_HUB_TOKEN="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"

huggingface-cli download cais/wmdp-corpora cyber-forget-corpus --repo-type dataset --local-dir ./datasets/cyber-forget

huggingface-cli download cais/wmdp-corpora cyber-retain-corpus --repo-type dataset --local-dir ./datasets/cyber-retain

huggingface-cli download cais/wmdp-bio-forget-corpus --repo-type dataset --local-dir ./datasets/bio-forget

huggingface-cli download cais/wmdp-corpora bio-retain-corpus --repo-type dataset --local-dir ./datasets/bio-retain

huggingface-cli download wikitext wikitext-2-raw-v1 --repo-type dataset --local-dir ./datasets/wikitext


(LLM_EvalPipeline_test) aiuser3@ai-smartlaw:~/ETU$ huggingface-cli download cais/wmdp-corpora cyber-forget-corpus --repo-type dataset --local-dir ./datasets/cyber-forget
⚠️  Warning: 'huggingface-cli download' is deprecated. Use 'hf download' instead.
Traceback (most recent call last):
  File "/data/aiuser3/LLM_EvalPipeline_test/.venv/lib/python3.12/site-packages/huggingface_hub/utils/_http.py", line 409, in hf_raise_for_status
    response.raise_for_status()
  File "/data/aiuser3/LLM_EvalPipeline_test/.venv/lib/python3.12/site-packages/requests/models.py", line 1026, in raise_for_status
    raise HTTPError(http_error_msg, response=self)
requests.exceptions.HTTPError: 404 Client Error: Not Found for url: https://huggingface.co/datasets/cais/wmdp-corpora/resolve/main/cyber-forget-corpus

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
  File "/data/aiuser3/LLM_EvalPipeline_test/.venv/lib/python3.12/site-packages/huggingface_hub/file_download.py", line 1230, in _hf_hub_download_to_local_dir
    (url_to_download, etag, commit_hash, expected_size, xet_file_data, head_call_error) = _get_metadata_or_catch_error(
                                                                                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
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
  File "/data/aiuser3/LLM_EvalPipeline_test/.venv/lib/python3.12/site-packages/huggingface_hub/utils/_http.py", line 420, in hf_raise_for_status
    raise _format(EntryNotFoundError, message, response) from e
huggingface_hub.errors.EntryNotFoundError: 404 Client Error. (Request ID: Root=1-68b669dd-3fad8ebc613b16914e163497;dea467df-3ea8-4ea7-9d5a-a04347a85359)

Entry Not Found for url: https://huggingface.co/datasets/cais/wmdp-corpora/resolve/main/cyber-forget-corpus.
(LLM_EvalPipeline_test) aiuser3@ai-smartlaw:~/ETU$ 
