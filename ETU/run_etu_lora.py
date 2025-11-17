#!/usr/bin/env python3
"""
ETU with LoRA Integration - Production Ready Script
Enhanced for closed network environments with robust error handling.
"""

import os
import sys
import torch
import numpy as np
from etu.unlearn import run_etu, get_args
from etu.utils import load_model, get_data

def main():
    """Main execution function with enhanced error handling."""
    
    # Set up environment
    print("=== ETU with LoRA Integration ===")
    print(f"PyTorch version: {torch.__version__}")
    print(f"CUDA available: {torch.cuda.is_available()}")
    if torch.cuda.is_available():
        print(f"CUDA device: {torch.cuda.get_device_name()}")
    
    # Parse arguments
    try:
        args = get_args()
        print(f"Arguments parsed successfully")
    except Exception as e:
        print(f"Error parsing arguments: {e}")
        return 1
    
    # Set random seeds for reproducibility
    SEED = args.seed
    torch.manual_seed(SEED)
    torch.cuda.manual_seed(SEED)
    torch.cuda.manual_seed_all(SEED)
    np.random.seed(SEED)
    
    # Load models with error handling
    try:
        print("Loading frozen model...")
        frozen_model, tokenizer = load_model(args.model_name_or_path, train=False)
        print("Loading updated model...")
        updated_model, tokenizer = load_model(args.model_name_or_path, train=True)
        print("Models loaded successfully")
    except Exception as e:
        print(f"Error loading models: {e}")
        print("Please check if the model path is correct and accessible")
        return 1
    
    # Load data with error handling
    try:
        print("Loading datasets...")
        forget_data_list, retain_data_list = get_data(
            args.forget_corpora,
            args.retain_corpora,
            args.min_len,
            args.max_len,
            args.batch_size,
        )
        print("Datasets loaded successfully")
    except Exception as e:
        print(f"Error loading datasets: {e}")
        print("Please check if the datasets are available locally")
        return 1
    
    # Run ETU with error handling
    try:
        print("Starting ETU training...")
        run_etu(
            updated_model,
            frozen_model,
            tokenizer,
            forget_data_list,
            retain_data_list,
            args,
        )
        print("ETU training completed successfully")
        return 0
    except Exception as e:
        print(f"Error during ETU training: {e}")
        import traceback
        traceback.print_exc()
        return 1

if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code) 