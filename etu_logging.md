# 1. 테스트 데이터 생성
mkdir -p test_data
echo "forget this information" > test_data/forget.txt
echo "retain this knowledge" > test_data/retain.txt

# 2. 작은 설정으로 실행
python run_etu_h200.py \
  --forget_corpora "test_data/forget.txt" \
  --retain_corpora "test_data/retain.txt" \
  --batch_size 1 \
  --max_num_batches 5 \
  --layer_id 7 \
  --verbose
