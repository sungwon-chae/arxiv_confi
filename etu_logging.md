# 외부 인터넷 연결 확인
ping -c 3 huggingface.co
curl -I https://huggingface.co

# DNS 확인
nslookup huggingface.co

# 환경 변수 확인
echo $http_proxy
echo $https_proxy
echo $HTTP_PROXY
echo $HTTPS_PROXY
echo $no_proxy
