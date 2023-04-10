res=$(curl -x POST \
--header "accept: application/json" \
--header "content-type: application/json;charset=utf-8" \
--header "Authorization: eyJhbGciOiJIUzI1NiJ9.eyJhY2NvdW50Ijoib2N0b2Jlci5rdW9AaHAuY29tIiwiaWF0IjoxNjgxMTA3MjExLCJleHAiOjE2ODExOTM2MTEsInZlciI6Mjc5fQ.5Wq1EvRjZ-iJjcxTMmaC5IaxP5ONczx_hpQ2ZG7jg9c" \
-d "{\"planId\": \"6433a9139e388c001a7d7159\"}" \
--proxy http://web-proxy.jp.hpicorp.net:8080 \
https://vcosmos-qa.hpcloud.hp.com/api/v2/jobsByPlan?planId=6433a9139e388c001a7d7159)
