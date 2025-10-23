aiuser3@ai-smartlaw:~/LegalAI-DataPipeline$ source /data/aiuser3/LegalAI-DataPipeline/.venv/bin/activate
(.venv) aiuser3@ai-smartlaw:~/LegalAI-DataPipeline$ CUDA_VISIBLE_DEVICES=6,7 python -m vllm.entrypoints.openai.api_server --model /data/models/Qwen3-Next-80B-A3B-Instruct --host 0.0.0.0 --port 8000 --tensor-parallel-size 2
INFO 10-23 15:10:08 [__init__.py:216] Automatically detected platform cuda.
(APIServer pid=1804347) INFO 10-23 15:10:10 [api_server.py:1896] vLLM API server version 0.10.2
(APIServer pid=1804347) INFO 10-23 15:10:10 [utils.py:328] non-default args: {'host': '0.0.0.0', 'model': '/data/models/Qwen3-Next-80B-A3B-Instruct', 'tensor_parallel_size': 2}
(APIServer pid=1804347) INFO 10-23 15:10:19 [__init__.py:742] Resolved architecture: Qwen3NextForCausalLM
(APIServer pid=1804347) `torch_dtype` is deprecated! Use `dtype` instead!
(APIServer pid=1804347) INFO 10-23 15:10:19 [__init__.py:1815] Using max model len 262144
(APIServer pid=1804347) INFO 10-23 15:10:20 [scheduler.py:222] Chunked prefill is enabled with max_num_batched_tokens=8192.
(APIServer pid=1804347) INFO 10-23 15:10:20 [config.py:310] Hybrid or mamba-based model detected: disabling prefix caching since it is not yet supported.
(APIServer pid=1804347) INFO 10-23 15:10:20 [config.py:321] Hybrid or mamba-based model detected: setting cudagraph mode to FULL_AND_PIECEWISE in order to optimize performance.
(APIServer pid=1804347) INFO 10-23 15:10:22 [config.py:390] Setting attention block size to 544 tokens to ensure that attention page size is >= mamba page size.
(APIServer pid=1804347) INFO 10-23 15:10:22 [config.py:411] Padding mamba page size by 1.49% to ensure that mamba page size and attention page size are exactly equal.
INFO 10-23 15:10:28 [__init__.py:216] Automatically detected platform cuda.
(EngineCore_DP0 pid=1805889) INFO 10-23 15:10:29 [core.py:654] Waiting for init message from front-end.
(EngineCore_DP0 pid=1805889) INFO 10-23 15:10:29 [core.py:76] Initializing a V1 LLM engine (v0.10.2) with config: model='/data/models/Qwen3-Next-80B-A3B-Instruct', speculative_config=None, tokenizer='/data/models/Qwen3-Next-80B-A3B-Instruct', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=262144, download_dir=None, load_format=auto, tensor_parallel_size=2, pipeline_parallel_size=1, data_parallel_size=1, disable_custom_all_reduce=False, quantization=None, enforce_eager=False, kv_cache_dtype=auto, device_config=cuda, decoding_config=DecodingConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_backend=''), observability_config=ObservabilityConfig(show_hidden_metrics_for_version=None, otlp_traces_endpoint=None, collect_detailed_traces=None), seed=0, served_model_name=/data/models/Qwen3-Next-80B-A3B-Instruct, enable_prefix_caching=False, chunked_prefill_enabled=True, use_async_output_proc=True, pooler_config=None, compilation_config={"level":3,"debug_dump_path":"","cache_dir":"","backend":"","custom_ops":[],"splitting_ops":["vllm.unified_attention","vllm.unified_attention_with_output","vllm.mamba_mixer2","vllm.mamba_mixer","vllm.short_conv","vllm.linear_attention","vllm.plamo2_mamba_mixer","vllm.gdn_attention"],"use_inductor":true,"compile_sizes":[],"inductor_compile_config":{"enable_auto_functionalized_v2":false},"inductor_passes":{},"cudagraph_mode":[2,1],"use_cudagraph":true,"cudagraph_num_of_warmups":1,"cudagraph_capture_sizes":[512,504,496,488,480,472,464,456,448,440,432,424,416,408,400,392,384,376,368,360,352,344,336,328,320,312,304,296,288,280,272,264,256,248,240,232,224,216,208,200,192,184,176,168,160,152,144,136,128,120,112,104,96,88,80,72,64,56,48,40,32,24,16,8,4,2,1],"cudagraph_copy_inputs":false,"full_cuda_graph":false,"pass_config":{},"max_capture_size":512,"local_cache_dir":null}
(EngineCore_DP0 pid=1805889) WARNING 10-23 15:10:29 [multiproc_worker_utils.py:273] Reducing Torch parallelism from 96 threads to 1 to avoid unnecessary CPU contention. Set OMP_NUM_THREADS in the external environment to tune this value as needed.
(EngineCore_DP0 pid=1805889) INFO 10-23 15:10:29 [shm_broadcast.py:289] vLLM message queue communication handle: Handle(local_reader_ranks=[0, 1], buffer_handle=(2, 16777216, 10, 'psm_5a94800c'), local_subscribe_addr='ipc:///tmp/df6d1e71-ce6e-416e-a655-6b468681f743', remote_subscribe_addr=None, remote_addr_ipv6=False)
INFO 10-23 15:10:35 [__init__.py:216] Automatically detected platform cuda.
INFO 10-23 15:10:35 [__init__.py:216] Automatically detected platform cuda.
INFO 10-23 15:10:39 [shm_broadcast.py:289] vLLM message queue communication handle: Handle(local_reader_ranks=[0], buffer_handle=(1, 10485760, 10, 'psm_9d634a56'), local_subscribe_addr='ipc:///tmp/8897b573-6155-461a-bf2c-ecdc6fedab65', remote_subscribe_addr=None, remote_addr_ipv6=False)
INFO 10-23 15:10:39 [shm_broadcast.py:289] vLLM message queue communication handle: Handle(local_reader_ranks=[0], buffer_handle=(1, 10485760, 10, 'psm_dffe6c59'), local_subscribe_addr='ipc:///tmp/60daa42f-4f09-4b54-b9d2-8c4afbd9883f', remote_subscribe_addr=None, remote_addr_ipv6=False)
[W1023 15:10:40.851982880 ProcessGroupNCCL.cpp:981] Warning: TORCH_NCCL_AVOID_RECORD_STREAMS is the default now, this environment variable is thus deprecated. (function operator())
[W1023 15:10:40.859315774 ProcessGroupNCCL.cpp:981] Warning: TORCH_NCCL_AVOID_RECORD_STREAMS is the default now, this environment variable is thus deprecated. (function operator())
[Gloo] Rank 0 is connected to 1 peer ranks. Expected number of connected peer ranks is : 1
[Gloo] Rank 1 is connected to 1 peer ranks. Expected number of connected peer ranks is : 1
[Gloo] Rank 0 is connected to 1 peer ranks. Expected number of connected peer ranks is : 1
[Gloo] Rank 1 is connected to 1 peer ranks. Expected number of connected peer ranks is : 1
INFO 10-23 15:10:40 [__init__.py:1433] Found nccl from library libnccl.so.2
INFO 10-23 15:10:40 [__init__.py:1433] Found nccl from library libnccl.so.2
INFO 10-23 15:10:40 [pynccl.py:70] vLLM is using nccl==2.27.3
INFO 10-23 15:10:40 [pynccl.py:70] vLLM is using nccl==2.27.3
INFO 10-23 15:10:41 [custom_all_reduce.py:35] Skipping P2P check and trusting the driver's P2P report.
INFO 10-23 15:10:41 [custom_all_reduce.py:35] Skipping P2P check and trusting the driver's P2P report.
INFO 10-23 15:10:41 [shm_broadcast.py:289] vLLM message queue communication handle: Handle(local_reader_ranks=[1], buffer_handle=(1, 4194304, 6, 'psm_3d83dfd9'), local_subscribe_addr='ipc:///tmp/9e2a7928-1d75-4517-98cb-01df843b60fa', remote_subscribe_addr=None, remote_addr_ipv6=False)
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 0 peer ranks. Expected number of connected peer ranks is : 0
[Gloo] Rank 0 is connected to 1 peer ranks. Expected number of connected peer ranks is : 1
[Gloo] Rank 1 is connected to 1 peer ranks. Expected number of connected peer ranks is : 1
INFO 10-23 15:10:41 [parallel_state.py:1165] rank 1 in world size 2 is assigned as DP rank 0, PP rank 0, TP rank 1, EP rank 1
INFO 10-23 15:10:41 [parallel_state.py:1165] rank 0 in world size 2 is assigned as DP rank 0, PP rank 0, TP rank 0, EP rank 0
WARNING 10-23 15:10:41 [topk_topp_sampler.py:69] FlashInfer is not available. Falling back to the PyTorch-native implementation of top-p & top-k sampling. For the best performance, please install FlashInfer.
WARNING 10-23 15:10:41 [topk_topp_sampler.py:69] FlashInfer is not available. Falling back to the PyTorch-native implementation of top-p & top-k sampling. For the best performance, please install FlashInfer.
(Worker_TP1 pid=1806414) INFO 10-23 15:10:41 [gpu_model_runner.py:2338] Starting to load model /data/models/Qwen3-Next-80B-A3B-Instruct...
(Worker_TP0 pid=1806413) INFO 10-23 15:10:42 [gpu_model_runner.py:2338] Starting to load model /data/models/Qwen3-Next-80B-A3B-Instruct...
(Worker_TP1 pid=1806414) INFO 10-23 15:10:42 [gpu_model_runner.py:2370] Loading model from scratch...
(Worker_TP1 pid=1806414) `torch_dtype` is deprecated! Use `dtype` instead!
(Worker_TP0 pid=1806413) INFO 10-23 15:10:42 [gpu_model_runner.py:2370] Loading model from scratch...
(Worker_TP0 pid=1806413) `torch_dtype` is deprecated! Use `dtype` instead!
(Worker_TP0 pid=1806413) INFO 10-23 15:10:42 [cuda.py:362] Using Flash Attention backend on V1 engine.
(Worker_TP1 pid=1806414) INFO 10-23 15:10:42 [cuda.py:362] Using Flash Attention backend on V1 engine.
Loading safetensors checkpoint shards:   0% Completed | 0/41 [00:00<?, ?it/s]
Loading safetensors checkpoint shards:   2% Completed | 1/41 [00:05<03:52,  5.81s/it]
Loading safetensors checkpoint shards:   5% Completed | 2/41 [00:10<03:18,  5.10s/it]
Loading safetensors checkpoint shards:   7% Completed | 3/41 [00:14<03:01,  4.79s/it]
Loading safetensors checkpoint shards:  10% Completed | 4/41 [00:19<02:52,  4.67s/it]
Loading safetensors checkpoint shards:  12% Completed | 5/41 [00:25<03:09,  5.26s/it]
Loading safetensors checkpoint shards:  15% Completed | 6/41 [00:31<03:09,  5.40s/it]
Loading safetensors checkpoint shards:  17% Completed | 7/41 [00:36<02:57,  5.22s/it]
Loading safetensors checkpoint shards:  20% Completed | 8/41 [00:41<02:52,  5.22s/it]
Loading safetensors checkpoint shards:  22% Completed | 9/41 [00:46<02:46,  5.20s/it]
Loading safetensors checkpoint shards:  24% Completed | 10/41 [00:51<02:38,  5.11s/it]
Loading safetensors checkpoint shards:  27% Completed | 11/41 [00:56<02:34,  5.16s/it]
Loading safetensors checkpoint shards:  29% Completed | 12/41 [01:01<02:29,  5.15s/it]
Loading safetensors checkpoint shards:  32% Completed | 13/41 [01:08<02:34,  5.50s/it]
Loading safetensors checkpoint shards:  34% Completed | 14/41 [01:14<02:35,  5.77s/it]
Loading safetensors checkpoint shards:  37% Completed | 15/41 [01:19<02:20,  5.39s/it]
Loading safetensors checkpoint shards:  39% Completed | 16/41 [01:25<02:21,  5.65s/it]
Loading safetensors checkpoint shards:  41% Completed | 17/41 [01:31<02:22,  5.96s/it]
Loading safetensors checkpoint shards:  44% Completed | 18/41 [01:38<02:19,  6.06s/it]
Loading safetensors checkpoint shards:  46% Completed | 19/41 [01:44<02:11,  5.98s/it]
Loading safetensors checkpoint shards:  49% Completed | 20/41 [01:49<02:04,  5.95s/it]
Loading safetensors checkpoint shards:  51% Completed | 21/41 [01:55<01:57,  5.90s/it]
Loading safetensors checkpoint shards:  54% Completed | 22/41 [02:00<01:43,  5.47s/it]
Loading safetensors checkpoint shards:  56% Completed | 23/41 [02:06<01:42,  5.70s/it]
Loading safetensors checkpoint shards:  59% Completed | 24/41 [02:10<01:27,  5.13s/it]
Loading safetensors checkpoint shards:  61% Completed | 25/41 [02:16<01:26,  5.39s/it]
Loading safetensors checkpoint shards:  63% Completed | 26/41 [02:21<01:18,  5.24s/it]
Loading safetensors checkpoint shards:  66% Completed | 27/41 [02:26<01:14,  5.33s/it]
Loading safetensors checkpoint shards:  68% Completed | 28/41 [02:31<01:08,  5.24s/it]
Loading safetensors checkpoint shards:  71% Completed | 29/41 [02:37<01:03,  5.32s/it]
Loading safetensors checkpoint shards:  73% Completed | 30/41 [02:41<00:56,  5.11s/it]
Loading safetensors checkpoint shards:  76% Completed | 31/41 [02:47<00:51,  5.15s/it]
Loading safetensors checkpoint shards:  78% Completed | 32/41 [02:51<00:45,  5.05s/it]
Loading safetensors checkpoint shards:  80% Completed | 33/41 [02:56<00:40,  5.06s/it]
Loading safetensors checkpoint shards:  83% Completed | 34/41 [03:01<00:34,  4.92s/it]
Loading safetensors checkpoint shards:  85% Completed | 35/41 [03:07<00:31,  5.21s/it]
Loading safetensors checkpoint shards:  88% Completed | 36/41 [03:11<00:24,  4.99s/it]
Loading safetensors checkpoint shards:  90% Completed | 37/41 [03:17<00:21,  5.30s/it]
Loading safetensors checkpoint shards:  93% Completed | 38/41 [03:24<00:16,  5.54s/it]
Loading safetensors checkpoint shards:  95% Completed | 39/41 [03:29<00:11,  5.54s/it]
Loading safetensors checkpoint shards: 100% Completed | 41/41 [03:35<00:00,  4.33s/it]
Loading safetensors checkpoint shards: 100% Completed | 41/41 [03:35<00:00,  5.25s/it]
(Worker_TP0 pid=1806413) 
(Worker_TP0 pid=1806413) INFO 10-23 15:14:18 [default_loader.py:268] Loading weights took 215.46 seconds
(Worker_TP1 pid=1806414) INFO 10-23 15:14:18 [default_loader.py:268] Loading weights took 215.47 seconds
(Worker_TP1 pid=1806414) INFO 10-23 15:14:18 [gpu_model_runner.py:2392] Model loading took 74.2812 GiB and 215.969277 seconds
(Worker_TP0 pid=1806413) INFO 10-23 15:14:18 [gpu_model_runner.py:2392] Model loading took 74.2812 GiB and 215.831224 seconds
(Worker_TP0 pid=1806413) INFO 10-23 15:14:25 [backends.py:539] Using cache directory: /data/aiuser3/.cache/vllm/torch_compile_cache/76921bbd65/rank_0_0/backbone for vLLM's torch.compile
(Worker_TP1 pid=1806414) INFO 10-23 15:14:25 [backends.py:539] Using cache directory: /data/aiuser3/.cache/vllm/torch_compile_cache/76921bbd65/rank_1_0/backbone for vLLM's torch.compile
(Worker_TP0 pid=1806413) INFO 10-23 15:14:25 [backends.py:550] Dynamo bytecode transform time: 6.75 s
(Worker_TP1 pid=1806414) INFO 10-23 15:14:25 [backends.py:550] Dynamo bytecode transform time: 6.75 s
(Worker_TP1 pid=1806414) INFO 10-23 15:14:28 [backends.py:161] Directly load the compiled graph(s) for dynamic shape from the cache, took 2.517 s
(Worker_TP0 pid=1806413) INFO 10-23 15:14:28 [backends.py:161] Directly load the compiled graph(s) for dynamic shape from the cache, took 2.521 s
(Worker_TP0 pid=1806413) INFO 10-23 15:14:29 [fused_moe.py:720] Using configuration from /data/aiuser3/LegalAI-DataPipeline/.venv/lib/python3.12/site-packages/vllm/model_executor/layers/fused_moe/configs/E=512,N=256,device_name=NVIDIA_H200.json for MoE layer.
(Worker_TP1 pid=1806414) INFO 10-23 15:14:29 [fused_moe.py:720] Using configuration from /data/aiuser3/LegalAI-DataPipeline/.venv/lib/python3.12/site-packages/vllm/model_executor/layers/fused_moe/configs/E=512,N=256,device_name=NVIDIA_H200.json for MoE layer.
(Worker_TP0 pid=1806413) INFO 10-23 15:14:29 [monitor.py:34] torch.compile takes 6.75 s in total
(Worker_TP1 pid=1806414) INFO 10-23 15:14:29 [monitor.py:34] torch.compile takes 6.75 s in total
(Worker_TP1 pid=1806414) INFO 10-23 15:14:30 [gpu_worker.py:298] Available KV cache memory: 44.59 GiB
(Worker_TP0 pid=1806413) INFO 10-23 15:14:30 [gpu_worker.py:298] Available KV cache memory: 44.59 GiB
(EngineCore_DP0 pid=1805889) INFO 10-23 15:14:30 [kv_cache_utils.py:1028] GPU KV cache size: 973,760 tokens
(EngineCore_DP0 pid=1805889) INFO 10-23 15:14:30 [kv_cache_utils.py:1032] Maximum concurrency for 262,144 tokens per request: 14.77x
(EngineCore_DP0 pid=1805889) INFO 10-23 15:14:30 [kv_cache_utils.py:1028] GPU KV cache size: 973,760 tokens
(EngineCore_DP0 pid=1805889) INFO 10-23 15:14:30 [kv_cache_utils.py:1032] Maximum concurrency for 262,144 tokens per request: 14.77x
Capturing CUDA graphs (mixed prefill-decode, PIECEWISE): 100%|██████████████████████████████████████████████████████████| 67/67 [00:06<00:00, 10.53it/s]
Capturing CUDA graphs (decode, FULL): 100%|█████████████████████████████████████████████████████████████████████████████| 67/67 [00:17<00:00,  3.77it/s]
(Worker_TP0 pid=1806413) INFO 10-23 15:14:55 [custom_all_reduce.py:203] Registering 10586 cuda graph addresses
(Worker_TP1 pid=1806414) INFO 10-23 15:14:55 [custom_all_reduce.py:203] Registering 10586 cuda graph addresses
(Worker_TP1 pid=1806414) INFO 10-23 15:14:56 [gpu_model_runner.py:3118] Graph capturing finished in 25 secs, took 2.37 GiB
(Worker_TP1 pid=1806414) INFO 10-23 15:14:56 [gpu_worker.py:391] Free memory on device (139.21/139.81 GiB) on startup. Desired GPU memory utilization is (0.9, 125.83 GiB). Actual usage is 74.28 GiB for weight, 5.58 GiB for peak activation, 1.38 GiB for non-torch memory, and 2.37 GiB for CUDAGraph memory. Replace gpu_memory_utilization config with `--kv-cache-memory=45175492096` to fit into requested memory, or `--kv-cache-memory=59540753920` to fully utilize gpu memory. Current kv cache memory in use is 47878721024 bytes.
(Worker_TP0 pid=1806413) INFO 10-23 15:14:56 [gpu_model_runner.py:3118] Graph capturing finished in 25 secs, took 2.37 GiB
(Worker_TP0 pid=1806413) INFO 10-23 15:14:56 [gpu_worker.py:391] Free memory on device (139.21/139.81 GiB) on startup. Desired GPU memory utilization is (0.9, 125.83 GiB). Actual usage is 74.28 GiB for weight, 5.58 GiB for peak activation, 1.38 GiB for non-torch memory, and 2.37 GiB for CUDAGraph memory. Replace gpu_memory_utilization config with `--kv-cache-memory=45175492096` to fit into requested memory, or `--kv-cache-memory=59540753920` to fully utilize gpu memory. Current kv cache memory in use is 47878721024 bytes.
(EngineCore_DP0 pid=1805889) INFO 10-23 15:14:56 [core.py:218] init engine (profile, create kv cache, warmup model) took 37.74 seconds
(APIServer pid=1804347) INFO 10-23 15:14:56 [loggers.py:142] Engine 000: vllm cache_config_info with initialization after num_gpu_blocks is: 7162
(APIServer pid=1804347) INFO 10-23 15:14:56 [async_llm.py:180] Torch profiler disabled. AsyncLLM CPU traces will not be collected.
(APIServer pid=1804347) INFO 10-23 15:14:57 [api_server.py:1692] Supported_tasks: ['generate']
(APIServer pid=1804347) WARNING 10-23 15:14:57 [__init__.py:1695] Default sampling parameters have been overridden by the model's Hugging Face generation config recommended from the model creator. If this is not intended, please relaunch vLLM instance with `--generation-config vllm`.
(APIServer pid=1804347) INFO 10-23 15:14:57 [serving_responses.py:130] Using default chat sampling params from model: {'temperature': 0.7, 'top_k': 20, 'top_p': 0.8}
(APIServer pid=1804347) INFO 10-23 15:14:57 [serving_chat.py:137] Using default chat sampling params from model: {'temperature': 0.7, 'top_k': 20, 'top_p': 0.8}
(APIServer pid=1804347) INFO 10-23 15:14:57 [serving_completion.py:76] Using default completion sampling params from model: {'temperature': 0.7, 'top_k': 20, 'top_p': 0.8}
(APIServer pid=1804347) INFO 10-23 15:14:57 [api_server.py:1971] Starting vLLM API server 0 on http://0.0.0.0:8000
(APIServer pid=1804347) INFO 10-23 15:14:57 [launcher.py:36] Available routes are:
(APIServer pid=1804347) INFO 10-23 15:14:57 [launcher.py:44] Route: /openapi.json, Methods: GET, HEAD
(APIServer pid=1804347) INFO 10-23 15:14:57 [launcher.py:44] Route: /docs, Methods: GET, HEAD
(APIServer pid=1804347) INFO 10-23 15:14:57 [launcher.py:44] Route: /docs/oauth2-redirect, Methods: GET, HEAD
(APIServer pid=1804347) INFO 10-23 15:14:57 [launcher.py:44] Route: /redoc, Methods: GET, HEAD
(APIServer pid=1804347) INFO 10-23 15:14:57 [launcher.py:44] Route: /health, Methods: GET
(APIServer pid=1804347) INFO 10-23 15:14:57 [launcher.py:44] Route: /load, Methods: GET
(APIServer pid=1804347) INFO 10-23 15:14:57 [launcher.py:44] Route: /ping, Methods: POST
(APIServer pid=1804347) INFO 10-23 15:14:57 [launcher.py:44] Route: /ping, Methods: GET
(APIServer pid=1804347) INFO 10-23 15:14:57 [launcher.py:44] Route: /tokenize, Methods: POST
(APIServer pid=1804347) INFO 10-23 15:14:57 [launcher.py:44] Route: /detokenize, Methods: POST
(APIServer pid=1804347) INFO 10-23 15:14:57 [launcher.py:44] Route: /v1/models, Methods: GET
(APIServer pid=1804347) INFO 10-23 15:14:57 [launcher.py:44] Route: /version, Methods: GET
(APIServer pid=1804347) INFO 10-23 15:14:57 [launcher.py:44] Route: /v1/responses, Methods: POST
(APIServer pid=1804347) INFO 10-23 15:14:57 [launcher.py:44] Route: /v1/responses/{response_id}, Methods: GET
(APIServer pid=1804347) INFO 10-23 15:14:57 [launcher.py:44] Route: /v1/responses/{response_id}/cancel, Methods: POST
(APIServer pid=1804347) INFO 10-23 15:14:57 [launcher.py:44] Route: /v1/chat/completions, Methods: POST
(APIServer pid=1804347) INFO 10-23 15:14:57 [launcher.py:44] Route: /v1/completions, Methods: POST
(APIServer pid=1804347) INFO 10-23 15:14:57 [launcher.py:44] Route: /v1/embeddings, Methods: POST
(APIServer pid=1804347) INFO 10-23 15:14:57 [launcher.py:44] Route: /pooling, Methods: POST
(APIServer pid=1804347) INFO 10-23 15:14:57 [launcher.py:44] Route: /classify, Methods: POST
(APIServer pid=1804347) INFO 10-23 15:14:57 [launcher.py:44] Route: /score, Methods: POST
(APIServer pid=1804347) INFO 10-23 15:14:57 [launcher.py:44] Route: /v1/score, Methods: POST
(APIServer pid=1804347) INFO 10-23 15:14:57 [launcher.py:44] Route: /v1/audio/transcriptions, Methods: POST
(APIServer pid=1804347) INFO 10-23 15:14:57 [launcher.py:44] Route: /v1/audio/translations, Methods: POST
(APIServer pid=1804347) INFO 10-23 15:14:57 [launcher.py:44] Route: /rerank, Methods: POST
(APIServer pid=1804347) INFO 10-23 15:14:57 [launcher.py:44] Route: /v1/rerank, Methods: POST
(APIServer pid=1804347) INFO 10-23 15:14:57 [launcher.py:44] Route: /v2/rerank, Methods: POST
(APIServer pid=1804347) INFO 10-23 15:14:57 [launcher.py:44] Route: /scale_elastic_ep, Methods: POST
(APIServer pid=1804347) INFO 10-23 15:14:57 [launcher.py:44] Route: /is_scaling_elastic_ep, Methods: POST
(APIServer pid=1804347) INFO 10-23 15:14:57 [launcher.py:44] Route: /invocations, Methods: POST
(APIServer pid=1804347) INFO 10-23 15:14:57 [launcher.py:44] Route: /metrics, Methods: GET
(APIServer pid=1804347) INFO:     Started server process [1804347]
(APIServer pid=1804347) INFO:     Waiting for application startup.
(APIServer pid=1804347) INFO:     Application startup complete.
