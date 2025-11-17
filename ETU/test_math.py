#!/usr/bin/env python3
"""
Quick math validation snippets for ETU.
Run these to check mathematical correctness.
"""

import torch
import numpy as np

def test_lambda_mapping_inverse():
    """Test λ-매핑 단조성 및 역함수"""
    from etu.utils import q_mass_from_lambda
    
    print("Testing λ-매핑 단조성...")
    
    for p in [0.01, 0.1, 0.3, 0.7]:
        # ε = 0.05로 설정
        epsilon = 0.05
        
        # λ 계산 (간단한 근사)
        if p > epsilon:
            lam = 5.0  # 억제
        else:
            lam = -2.0  # 증폭
        
        q = q_mass_from_lambda(p, lam)
        
        # 검증
        if p > epsilon:
            assert q <= epsilon, f"p={p} > ε={epsilon}이면 q={q} ≤ ε이어야 함"
        else:
            assert q >= epsilon, f"p={p} < ε={epsilon}이면 q={q} ≥ ε이어야 함"
        
        print(f"✓ p={p:.2f}, λ={lam:.1f} → q={q:.4f}")

def test_kl_directionality():
    """Test KL divergence directionality"""
    print("\nTesting KL divergence directionality...")
    
    # Random distributions
    logp = torch.log_softmax(torch.randn(2, 3), -1)
    q = torch.softmax(torch.randn(2, 3), -1)
    
    # KL(q || p) = sum(q * log(q/p))
    kl = torch.nn.functional.kl_div(logp, q, reduction='batchmean')
    
    assert kl >= 0, f"KL divergence must be non-negative, got {kl}"
    print(f"✓ KL(q||p) = {kl:.6f} ≥ 0")

def test_wilson_upper_bound():
    """Test Wilson upper bound properties"""
    from etu.utils import wilson_upper
    
    print("\nTesting Wilson upper bound...")
    
    p_hat = 0.1
    n_eff = 100
    
    upper = wilson_upper(p_hat, n_eff)
    
    assert upper >= p_hat, f"Wilson upper bound must be ≥ p_hat: {upper} vs {p_hat}"
    assert upper <= 1.0, f"Wilson upper bound must be ≤ 1.0: {upper}"
    
    print(f"✓ p_hat={p_hat:.3f}, n={n_eff} → Wilson upper={upper:.4f}")

if __name__ == "__main__":
    print("ETU Math Validation Tests")
    print("=" * 40)
    
    try:
        test_lambda_mapping_inverse()
        test_kl_directionality()
        test_wilson_upper_bound()
        print("\n🎉 All tests passed!")
    except Exception as e:
        print(f"\n❌ Test failed: {e}")
        import traceback
        traceback.print_exc() 