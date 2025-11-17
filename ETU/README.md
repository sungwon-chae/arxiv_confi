# ETU: Exponential-Tilted Unlearning

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.0+-red.svg)](https://pytorch.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

**ETU (Exponential-Tilted Unlearning)** is a state-of-the-art machine unlearning framework for large language models, providing theoretical guarantees and practical efficiency through exponential-tilted distributions and adaptive λ control.

## 🚀 **Quick Overview**

**ETU** formulates unlearning as a KL I-projection with mass constraint, yielding:
- **Closed-form solution**: Direct ε-λ mapping for precise control
- **Provable guarantees**: π_θ'(S) ≤ ε + √(δ/2) under bounded training error
- **No critics needed**: Works without preference pairs or reference models
- **Parameter-efficient**: Compatible with LoRA and other PEFT methods
- **Memory efficient**: Direct tensor slicing without boolean masks

### **One-Line Usage**
```bash
python -m etu.unlearn --forget_corpora "cais/wmdp-corpora:cyber-forget-corpus" --retain_corpora "cais/wmdp-corpora:bio-retain-corpus" --epsilon 0.05 --use_lora --frozen_on_cpu
```

---

## 📋 **Table of Contents**

- [Installation](#installation)
- [Quick Start](#quick-start)
- [Advanced Usage](#advanced-usage)
- [Experiments](#experiments)
- [API Reference](#api-reference)
- [Contributing](#contributing)
- [Citation](#citation)

## 🛠️ **Installation**

### Prerequisites
- Python 3.9+
- PyTorch 2.0+
- CUDA-compatible GPU (recommended)

### Install Dependencies
```bash
git clone https://github.com/sungwon-chae/ETU.git
cd ETU
pip install -r requirements.txt
```

## 🚀 **Quick Start**

### Basic Unlearning
```bash
python -m etu.unlearn \
  --forget_corpora "cais/wmdp-corpora:cyber-forget-corpus" \
  --retain_corpora "cais/wmdp-corpora:bio-retain-corpus" \
  --epsilon 0.05 \
  --use_lora \
  --frozen_on_cpu \
  --verbose
```

### Quick Debug Mode
```bash
python -m etu.unlearn \
  --forget_corpora wikitext \
  --retain_corpora wikitext \
  --epsilon 0.1 \
  --max_num_batches 10 \
  --frozen_on_cpu \
  --log_every 5
```

## 🔬 **Advanced Usage**

### PMI-based V_S Refinement
```bash
python -m etu.unlearn \
  --forget_corpora "cais/wmdp-corpora:cyber-forget-corpus" \
  --retain_corpora "cais/wmdp-corpora:bio-retain-corpus" \
  --use_pmi_vs \
  --pmi_top_k 2000 \
  --pmi_min_count 20 \
  --pmi_smoothing 1.0 \
  --epsilon 0.05 \
  --use_lora \
  --frozen_on_cpu
```

### Preference Learning Integration
```bash
# NPO (Neural Preference Optimization)
python -m etu.unlearn \
  --forget_corpora "cais/wmdp-corpora:cyber-forget-corpus" \
  --retain_corpora "cais/wmdp-corpora:bio-retain-corpus" \
  --preference_weight 0.1 \
  --pref_format npo \
  --pref_every 5 \
  --pref_margin 0.0 \
  --epsilon 0.05 \
  --use_lora \
  --frozen_on_cpu

# DPO (Direct Preference Optimization)
python -m etu.unlearn \
  --forget_corpora "cais/wmdp-corpora:cyber-forget-corpus" \
  --retain_corpora "cais/wmdp-corpora:bio-retain-corpus" \
  --preference_weight 0.1 \
  --pref_format dpo \
  --pref_beta 0.1 \
  --pref_every 5 \
  --epsilon 0.05 \
  --use_lora \
  --frozen_on_cpu
```

## 📊 **Experiments**

### Paper Reproduction
```bash
# Run complete paper experiments
./run_paper_experiments.sh

# Hyperparameter sweep
./run_hyperparameter_sweep.sh
```

### Performance Optimization
```bash
# LoRA rank comparison
for rank in 64 128 256 512; do
  python -m etu.unlearn \
    --forget_corpora "cais/wmdp-corpora:cyber-forget-corpus" \
    --retain_corpora "cais/wmdp-corpora:bio-retain-corpus" \
    --epsilon 0.05 \
    --use_lora \
    --lora_r $rank \
    --frozen_on_cpu \
    --max_num_batches 40
done
```

## 🔧 **Configuration Options**

### Core Parameters
- `--epsilon`: Target suppression threshold (default: 0.05)
- `--lambda_max`: Maximum λ value (default: 12.0)
- `--lambda_update_freq`: λ update frequency (default: 25)
- `--lambda_eta`: λ update step size (default: 0.25)

### V_S Configuration
- `--use_pmi_vs`: Enable PMI-based refinement (default: True)
- `--pmi_top_k`: Top-K tokens by PMI (default: 2000)
- `--pmi_min_count`: Minimum frequency for PMI (default: 20)
- `--vocab_top_k`: Top-K tokens by frequency (default: None)

### LoRA Integration
- `--use_lora`: Enable LoRA (default: False)
- `--lora_r`: LoRA rank (default: 256)
- `--lora_alpha`: LoRA scaling factor (default: 512)
- `--lora_dropout`: LoRA dropout rate (default: 0.1)

### Performance Options
- `--frozen_on_cpu`: Keep frozen model on CPU (default: False)
- `--batch_size`: Training batch size (default: 4)
- `--max_num_batches`: Maximum batches per epoch (default: 80)
- `--log_every`: Log frequency for non-verbose mode (default: 50)
- `--deterministic`: Enable deterministic algorithms (may impact performance)

## 📈 **Results & Evaluation**

### Output Files
- `V_S.ids.json`: Forbidden token set for reproducibility
- `args.json`: Complete experiment configuration
- `metrics.json`: Training metrics and final results
- `suppression_report.json`: Detailed suppression analysis with Wilson bounds

### Key Metrics
- **πθ(S)**: Current probability mass on forbidden set
- **λ**: Current exponential tilting parameter
- **KL divergence**: Distance to target distribution
- **Wilson upper bound**: Statistical confidence interval
- **Target achieved**: Whether ε threshold is met

## 🧪 **Testing & Validation**

### Mathematical Validation
```bash
python test_math.py
```

### Import Testing
```bash
python -c "
from etu.unlearn import run_etu, get_args
from etu.utils import load_model, get_data
print('✅ All imports successful')
"
```

## 📚 **API Reference**

### Core Functions
- `run_etu()`: Main ETU training function
- `get_args()`: Command-line argument parser
- `load_model()`: Model and tokenizer loader
- `get_data()`: Dataset loader for WMDP and WikiText

### Utility Functions
- `build_forbidden_token_ids()`: V_S construction
- `build_forbidden_token_ids_pmi()`: PMI-based V_S refinement
- `wilson_upper()`: Wilson confidence interval
- `create_suppression_report()`: Evaluation report generator

## 🤝 **Contributing**

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details.

### Development Setup
```bash
git clone https://github.com/sungwon-chae/ETU.git
cd ETU
pip install -r requirements.txt
pip install -e .
```

### Code Style
- Follow PEP 8 guidelines
- Use type hints where appropriate
- Add docstrings for all functions
- Include tests for new features

## 📖 **Citation**

If you use ETU in your research, please cite:

```bibtex
@article{etu2026,
  title={ETU: Exponential-Tilted Unlearning for Large Language Models},
  author={Chae, ...},
  journal={iclr2026},
  year={2026}
}
```

## 📄 **License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 **Acknowledgments**

- Built on top of [Hugging Face Transformers](https://github.com/huggingface/transformers)
- LoRA integration with [PEFT](https://github.com/huggingface/peft)
- Dataset support from [Hugging Face Datasets](https://github.com/huggingface/datasets)

## 📞 **Contact**

- **Author**: Sungwon Chae
- **Email**: csw0815@snu.ac.kr
- **GitHub**: [@sungwon-chae](https://github.com/sungwon-chae)
- **Institution**: Seoul National University

---

## 🔬 **Detailed Technical Documentation**

### Theory

ETU formulates unlearning as the KL I-projection of the base model π_base onto the convex set defined by the mass constraint:

```
min_q KL(q(·|x) || π_base(·|x))  s.t.  Σ_{y∈S} q(y|x) ≤ ε
```

The solution takes the exponential-tilted form:

```
q_λ(y|x) = π_base(y|x) * exp(-λ * 1{y∈S}) / Z(λ)
```

where λ is computed via the closed-form mapping:

```
λ = logit(p_S) - logit(ε)
```

**Theoretical Guarantee**: π_learn(S) ≤ ε + √(δ/2) under bounded training error δ.

### Critical Implementation Details

#### 1. Proper S (Forbidden Set) Handling
- **V_S construction**: Builds forbidden token set from forget data with frequency filtering
- **Token-level approximation**: Uses token frequencies to approximate sequence-level S
- **Configurable size**: `--vocab_top_k` to limit V_S size for stability
- **Empty V_S protection**: Runtime checks prevent training with empty forbidden sets

#### 2. Correct p_S Estimation
- **Mass-based**: Computes Σ_{y∈V_S} π_base(y|x) over positions and batches
- **Base model only**: Uses frozen π_base, not updated model
- **Numerically stable**: Proper clipping and normalization
- **Confidence intervals**: 95% CI reporting for statistical significance

#### 3. Adaptive λ Control
- **Real-time adjustment**: Updates λ based on current π_θ(S) vs target ε
- **Pinsker margin**: Uses ε + √(δ/2) as adjustment threshold
- **EMA smoothing**: Exponential moving average reduces noise
- **Configurable frequency**: `--lambda_update_freq` controls update rate

#### 4. Memory and Performance Optimizations
- **Direct slicing**: No boolean masks, efficient tensor operations
- **Mixed precision**: AMP support for bf16/fp16 training
- **Gradient clipping**: Stable training with norm clipping
- **Learning rate scheduling**: Linear warmup with linear decay for better convergence

#### 5. Amplification Mode

ETU supports amplification mode where λ < 0 to increase probability mass on S:
- **Use case**: Amplification useful for expanding model capabilities on specific topics
- **Control**: λ updates also allow negative values when `--allow_negative_lambda` is set
- **Example**: When ε > p_S, λ becomes negative to amplify π_θ(S) above ε

#### 6. Retain-Free Operation

ETU can operate without retain data, focusing purely on suppression:
- **Core mechanism**: ETU's objective function controls S mass relative to base distribution π_base
- **Retain purpose**: Language/domain utility monitoring + weak regularization
- **Suppression guarantee**: π_θ(S) ≤ ε + √(δ/2) holds regardless of retain data
- **Usage**: Set `--retain_corpora ""` and `--retain_weight 0` for suppression-only experiments

#### 7. Preference-Based Refinement

ETU supports optional preference-based refinement for fine-grained control:
- **NPO (default)**: Hinge loss encouraging retain > forget logprobs
- **DPO (optional)**: Logistic loss with reference model (frozen) for stronger ranking signals
- **Integration**: Combines global suppression (λ-tilt) with local preference (pos↑, neg↓)
- **Safety**: Only active when retain data is available and `--preference_weight > 0`
- **Performance**: Controlled frequency with `--pref_every` to balance speed and effectiveness

#### 8. Retain Data Management

ETU provides flexible retain data handling:
- **Split alignment**: forget와 retain split 수를 맞춰야 함 (예: bio:forget,cyber:forget + wikitext,wikitext)
- **Broadcast mode**: `--retain_broadcast`로 단일 retain corpus를 모든 forget split에 재사용
- **Automatic fallback**: retain 데이터가 없으면 자동으로 retain loss 생략하고 ETU 단독으로 동작

#### 9. Quality Control Checklist

##### **빠른 품질 체크리스트**
- **V_S 크기 로그**: |V_S|/V가 5~15% 정도면 보통 안정적. 50%↑ 경고 뜨면 `--pmi_top_k` 줄이기
- **retain 없이 ETU만**: `--retain_weight 0` 이거나 retain 비어 있으면 자동으로 retain-loss 스킵됨
- **λ 로깅**: [λ-update]에서 EMA πθ(S)가 ε 아래로 안정되면 OK
- **최종 산출물**: V_S.ids.json, args.json, metrics.json 저장 확인
- **Target achieved**: create_suppression_report()에서 ✓ 나오는지 체크

##### **추가 미세 팁**
- **sample_size**: `estimate_p_S_over_VS(..., sample_size=512)`는 무거움. 개발/디버그 때는 128, 실험 고정본에서 512
- **LoRA 없이**: `--use_lora` 제거 + `--layer_ids`로 좁혀(중간 3~4개 레이어) 안정성과 속도 잡기
- **DPO**: `reference_model=frozen`을 넘기는 게 수렴이 잘 됨 (자기참조 self-DPO는 가끔 흔들림)

### Theoretical Guarantees

ETU provides principled guarantees:
- **Suppression**: π_θ(S) ≤ ε + √(δ/2) where δ is KL(π_θ || q_λ) estimated from evaluation
- **Control**: Wilson upper bounds provide conservative confidence intervals
- **Audit**: Comprehensive reporting with both point estimates and statistical bounds
- **δ measurement**: δ는 KL(πθ‖qλ)을 평가 시 측정하며, 리포트에서 Wilson 상한과 함께 보고한다

### Advanced Configuration

#### Wilson Upper Bound Control
- `--wilson_max_n 2048`: Wilson 상한에서 사용할 n_eff 상한 (기본값: 2048)

#### V_S Filtering Parameters
- `--vs_freq_rate 0.01`: V_S 빈도 컷 비율 (기본값: 1%)
- `--vs_abs_cap 20000`: V_S 빈도 절대 상한 (기본값: 20,000)

#### Held-out Mini Evaluation
- **Concept**: λ 업데이트 시 작은 held-out 데이터(4-8 배치)로 π_θ(S)와 δ를 재측정하여 배치 편향 완화
- **Benefits**: 더 정확한 Pinsker 마진 계산, 안정적인 λ 제어

#### Experimental Features
- `--span_masking`: BPE 연속 조각 스팬 단위 V_S 확장 (실험적, 현재는 flag만 노출/비활성)
- `--span_ngram_max 3`: 스팬 마스킹의 최대 n-gram 크기

#### Activation Analysis (Optional)
- **ERASER-inspired**: Activation extraction functions for analysis/debugging
- **Note**: ETU's core mechanism relies on probability mass estimation over V_S, not activation-based unlearning
- **Purpose**: Useful for understanding model behavior and computing layer statistics
- **Usage**: Available in `utils.py` but not used in core ETU training
- **Flag**: `--analyze_activations` to enable activation analysis (disabled by default)
- **Use cases**: Layer selection validation, stability monitoring, LoRA debugging, ablation studies
- **Performance**: Only use when needed - hooks add overhead and memory usage

#### Activation Analysis Usage
```bash
# Enable activation analysis for debugging
python run_etu_lora.py \
    --model_name_or_path HuggingFaceH4/zephyr-7b-beta \
    --forget_corpora bio-forget-corpus,cyber-forget-corpus \
    --retain_corpora wikitext,wikitext \
    --epsilon 0.05 --use_lora \
    --analyze_activations --verbose
```

#### Parameter Selection
- `--name_keywords q_proj,k_proj,v_proj,o_proj`: 파라미터 이름 키워드 (기본값: attention projections)
- `--param_ids`: 파라미터 인덱스 (name_keywords와 함께 사용하지 말 것)
- `--module_str`: 모듈 경로 템플릿 (다양한 아키텍처 지원)

### PEFT Integration

LoRA/DoRA 등 PEFT로의 확장 가능:
- 파라미터 선택 계층을 LoRA 어댑터로 대체
- `--name_keywords`를 LoRA 파라미터 이름으로 설정
- 예: `--name_keywords lora_A,lora_B` (LoRA), `--name_keywords dora_A,dora_B` (DoRA)

### Comprehensive Evaluation
- **Suppression metrics**: π_θ(S) measurement with confidence intervals
- **Utility preservation**: Perplexity on retain data
- **Trade-off analysis**: Suppression vs utility ratios
- **Automated reporting**: JSON output with all metrics

### Algorithm

1. **Build V_S**: Collect forbidden token set from forget data with frequency filtering
2. **Estimate p_S**: Compute π_base(S) over V_S using frozen model (512 samples)
3. **Compute λ**: Use closed-form mapping from ε and p_S
4. **Create tilted distribution**: Apply exponential tilting with direct slicing
5. **Train**: Minimize KL divergence to tilted distribution with AMP
6. **Adapt λ**: Periodically adjust based on EMA of current suppression
7. **Evaluate**: Measure suppression and utility preservation
8. **Optional refinement**: Add NPO/DPO preference-based pairwise loss

### Performance Optimizations

#### Memory Efficiency
- **Direct tensor slicing**: `tilted_logits[..., V_S] -= lambda_val` instead of boolean masks
- **Gradient checkpointing**: Compatible with large models
- **Mixed precision**: Automatic mixed precision (AMP) support

#### Training Stability
- **Gradient clipping**: Norm clipping at 1.0
- **Learning rate scheduling**: Linear warmup with linear decay
- **EMA smoothing**: 20-step moving average for λ updates
- **Confidence intervals**: Statistical significance reporting

#### Numerical Stability
- **Proper clamping**: Min/max bounds on probabilities
- **Log-space operations**: Stable log-softmax computations
- **Error handling**: Graceful handling of edge cases

### Evaluation and Monitoring

#### Key Metrics
- `π_θ(S)`: Current mass on forbidden set with 95% CI
- `E[q_λ(S)]`: Expected mass from theoretical λ
- `KL(π_θ || q_λ)`: Training error bound (KL divergence from updated model to tilted distribution)
- `λ`: Current tilting parameter
- `Perplexity`: Utility preservation on retain data

#### Automated Reporting
```json
{
  "training_success": true,
  "training_duration_seconds": 120.5,
  "epsilon": 0.05,
  "V_S_size": 3247,
  "report": {
    "base_p_S": 0.1234,
    "updated_p_S": 0.0432,
    "suppression_ratio": 0.35,
    "perplexity_ratio": 1.12,
    "target_achieved": true
  }
}
```

### Comparison with Other Methods

| Method | Global Mass Control | Closed-form Solution | Critic/Pairs Needed | Adaptive Control | Memory Efficient |
|--------|-------------------|---------------------|-------------------|------------------|------------------|
| GA | ❌ | ❌ | ❌ | ❌ | ❌ |
| NPO | ❌ | ❌ | ✅ | ❌ | ❌ |
| RMU | ❌ | ❌ | ❌ | ❌ | ❌ |
| **ETU** | **✅** | **✅** | **❌** | **✅** | **✅** |

### Troubleshooting

#### Common Issues

1. **Empty V_S**: Check forget data or reduce filtering
   ```bash
   --vocab_top_k 10000  # Increase token limit
   ```

2. **Unstable training**: Reduce λ_max and increase update frequency
   ```bash
   --lambda_max 8.0 --lambda_update_freq 50
   ```

3. **Poor suppression**: Increase lambda_eta and check V_S size
   ```bash
   --lambda_eta 0.5 --vocab_top_k 2000
   ```

4. **Utility degradation**: Increase retain_weight
   ```bash
   --retain_weight 2.0
   ```

#### Performance Tips

- Use `--verbose` for detailed monitoring
- Start with conservative `--epsilon` (0.05-0.1)
- Monitor perplexity ratio (should stay < 1.5)
- Check confidence intervals for statistical significance

## 🚀 **H200 GPU 환경 최적화**

### **💎 H200 GPU 특화 기능**

ETU는 NVIDIA H200 GPU 환경에 최적화되어 있습니다:

#### **자동 환경 감지**
- **H200 감지**: 자동으로 H200 GPU 환경을 감지하고 최적화된 설정 적용
- **동적 설정**: GPU 환경에 따라 batch_size, LoRA rank, frozen_on_cpu 자동 조정
- **성능 최적화**: 143GB VRAM을 활용한 대용량 배치 처리

#### **H200 최적화된 기본값**
```bash
# H200 환경에서 자동 적용되는 설정
--batch_size 8              # 일반 GPU: 4
--lora_r 512               # 일반 GPU: 256
--lora_alpha 1024          # 일반 GPU: 512
--max_num_batches 100      # 일반 GPU: 80
--frozen_on_cpu false      # 일반 GPU: true
```

### **🎯 H200 전용 실행 스크립트**

#### **A. 기본 실행 (자동 최적화)**
```bash
# H200 환경 자동 감지 및 최적화
python run_etu_h200.py

# 또는 기존 방식 (자동 최적화)
python run_etu.py
```

#### **B. 고급 실행 (수동 제어)**
```bash
# 단일 GPU 사용
python run_etu_h200.py --gpu_id 0

# 멀티 GPU 사용
python run_etu_h200.py --multi_gpu

# 커스텀 설정
python run_etu_h200.py --batch_size 16 --lora_r 1024
```

### **📊 H200 환경 모니터링**

#### **실시간 GPU 모니터링**
```bash
# H200 전용 모니터링
python monitor_h200.py

# 커스텀 간격
python monitor_h200.py --interval 3 --log custom_monitor.log
```

#### **GPU 상태 확인**
```bash
# 기본 GPU 정보
nvidia-smi

# 상세 모니터링
nvidia-smi dmon -s pucvmet -d 1

# H200 전용 정보
nvidia-smi --query-gpu=name,memory.total,memory.used,utilization.gpu --format=csv
```

### **🔥 H200 성능 최적화 팁**

#### **1. 메모리 활용 최적화**
```bash
# H200의 143GB VRAM 활용
--batch_size 8          # 큰 배치 크기
--frozen_on_cpu false   # frozen 모델도 GPU에
--max_num_batches 100   # 더 많은 배치 처리
```

#### **2. LoRA 성능 최적화**
```bash
# H200 최적 LoRA 설정
--lora_r 512           # 높은 rank (메모리 여유)
--lora_alpha 1024      # 높은 alpha
--use_lora true        # LoRA 활성화
```

#### **3. 멀티 GPU 활용**
```bash
# GPU 0,1 사용
export CUDA_VISIBLE_DEVICES=0,1

# 병렬 처리
python run_etu_h200.py --multi_gpu
```

### **📈 H200 vs 일반 GPU 성능 비교**

| 설정 | H200 (143GB) | 일반 GPU (24GB) | 성능 향상 |
|------|---------------|-----------------|-----------|
| **batch_size** | 8 | 4 | 2x |
| **lora_r** | 512 | 256 | 2x |
| **max_batches** | 100 | 80 | 1.25x |
| **frozen_on_cpu** | false | true | 1.5x |
| **총 성능 향상** | - | - | **3-4x** |

### **🔧 H200 환경 문제 해결**

#### **일반적인 문제**
```bash
# 1. CUDA out of memory (H200에서는 드물음)
# 해결: --batch_size 줄이기 (16 → 8)

# 2. GPU 감지 실패
# 해결: nvidia-smi 확인, CUDA_VISIBLE_DEVICES 설정

# 3. 메모리 사용량 높음
# 해결: --frozen_on_cpu true (필요시)
```

#### **H200 특화 문제**
```bash
# 1. 과도한 메모리 사용
# 해결: --batch_size 16 이상 사용 시 주의

# 2. LoRA rank 높음
# 해결: --lora_r 1024 이상 시 안정성 확인

# 3. 멀티 GPU 동기화
# 해결: 단일 GPU로 시작 후 점진적 확장
```
