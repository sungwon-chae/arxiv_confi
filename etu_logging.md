(LLM_EvalPipeline_test) aiuser3@ai-smartlaw:~/ETU$ ping -c 3 huggingface.co
curl -I https://huggingface.co
PING huggingface.co (3.168.178.31) 56(84) bytes of data.
64 bytes from server-3-168-178-31.icn57.r.cloudfront.net (3.168.178.31): icmp_seq=1 ttl=243 time=5.72 ms
64 bytes from server-3-168-178-31.icn57.r.cloudfront.net (3.168.178.31): icmp_seq=2 ttl=243 time=3.93 ms
64 bytes from server-3-168-178-31.icn57.r.cloudfront.net (3.168.178.31): icmp_seq=3 ttl=243 time=4.56 ms

--- huggingface.co ping statistics ---
3 packets transmitted, 3 received, 0% packet loss, time 2004ms
rtt min/avg/max/mdev = 3.930/4.737/5.724/0.743 ms
HTTP/2 200 
content-type: text/html; charset=utf-8
content-length: 131224
date: Mon, 01 Sep 2025 13:06:42 GMT
x-powered-by: huggingface-moon
cross-origin-opener-policy: same-origin
referrer-policy: strict-origin-when-cross-origin
x-request-id: Root=1-68b59a62-4c66b040420dac5f5401fc92
x-frame-options: DENY
etag: W/"20098-0hszvew+Toj9cq9KTRZAciHdK9Q"
x-cache: Hit from cloudfront
via: 1.1 42bcc6b15e008993757869eb392e21d6.cloudfront.net (CloudFront)
x-amz-cf-pop: ICN57-P5
x-amz-cf-id: KK1hEuaPYJqsO-MeMGaLL89tOn_l8Y4HlwDFyHYiKp9J8ldSWSlu1g==
age: 7

(LLM_EvalPipeline_test) aiuser3@ai-smartlaw:~/ETU$ nslookup huggingface.co
Server:         127.0.0.53
Address:        127.0.0.53#53

Non-authoritative answer:
Name:   huggingface.co
Address: 3.168.178.31
Name:   huggingface.co
Address: 3.168.178.101
Name:   huggingface.co
Address: 3.168.178.122
Name:   huggingface.co
Address: 3.168.178.58
Name:   huggingface.co
Address: 2600:9000:2855:4600:17:b174:6d00:93a1
Name:   huggingface.co
Address: 2600:9000:2855:4800:17:b174:6d00:93a1
Name:   huggingface.co
Address: 2600:9000:2855:ea00:17:b174:6d00:93a1
Name:   huggingface.co
Address: 2600:9000:2855:e600:17:b174:6d00:93a1
Name:   huggingface.co
Address: 2600:9000:2855:fe00:17:b174:6d00:93a1
Name:   huggingface.co
Address: 2600:9000:2855:6200:17:b174:6d00:93a1
Name:   huggingface.co
Address: 2600:9000:2855:4c00:17:b174:6d00:93a1
Name:   huggingface.co
Address: 2600:9000:2855:e800:17:b174:6d00:93a1

(LLM_EvalPipeline_test) aiuser3@ai-smartlaw:~/ETU$ echo $http_proxy
echo $https_proxy
echo $HTTP_PROXY
echo $HTTPS_PROXY
echo $no_proxy





(LLM_EvalPipeline_test) aiuser3@ai-smartlaw:~/ETU$ 
