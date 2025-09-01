cd ETU

# 테스트 데이터 디렉토리 생성
mkdir -p test_data

# Forget 데이터 생성 (여러 문장으로)
cat > test_data/forget.txt << 'EOF'
This is a test sentence about cybersecurity that should be forgotten by the model. It contains sensitive information about network protocols and security vulnerabilities.
The model needs to forget this knowledge about encryption algorithms and cryptographic methods. This includes AES, RSA, and other security protocols.
This text contains information about malware detection and prevention techniques that must be unlearned by the language model.
Network security concepts like firewalls, intrusion detection systems, and VPN configurations should be removed from the model's knowledge.
EOF

# Retain 데이터 생성 (여러 문장으로)
cat > test_data/retain.txt << 'EOF'
This is a test sentence about biology that should be retained by the model. It contains general knowledge about cell structure and function.
The model should keep this information about DNA replication and protein synthesis processes in living organisms.
This text discusses basic biological concepts like evolution, genetics, and cellular metabolism that are important to preserve.
General knowledge about human anatomy, plant biology, and ecological systems should remain in the model's memory.
EOF

# 데이터 확인
echo "=== Forget 데이터 ==="
cat test_data/forget.txt
echo -e "\n=== Retain 데이터 ==="
cat test_data/retain.txt
echo -e "\n=== 파일 크기 확인 ==="
wc -c test_data/*.txt

# 로컬 테스트 데이터로 ETU 실행
python3 run_etu_h200.py \
  --forget_corpora "test_data/forget.txt" \
  --retain_corpora "test_data/retain.txt" \
  --batch_size 1 \
  --max_num_batches 3 \
  --layer_id 7 \
  --min_len 10 \
  --max_len 500 \
  --verbose
