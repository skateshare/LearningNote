curl -o actions-runner-linux-x64-2.293.1.tar.gz -L -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IlREYjU0V0Q5S1ZiLW5FZzM4VFdlQ2V0b1hqTSJ9.eyJuYW1laWQiOiJkZGRkZGRkZC1kZGRkLWRkZGQtZGRkZC1kZGRkZGRkZGRkZGQiLCJzY3AiOiJBY3Rpb25zUnVudGltZS5QYWNrYWdlRG93bmxvYWQiLCJJZGVudGl0eVR5cGVDbGFpbSI6IlN5c3RlbTpTZXJ2aWNlSWRlbnRpdHkiLCJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9zaWQiOiJERERERERERC1ERERELUREREQtRERERC1EREREREREREREREQiLCJodHRwOi8vc2NoZW1hcy5taWNyb3NvZnQuY29tL3dzLzIwMDgvMDYvaWRlbnRpdHkvY2xhaW1zL3ByaW1hcnlzaWQiOiJkZGRkZGRkZC1kZGRkLWRkZGQtZGRkZC1kZGRkZGRkZGRkZGQiLCJhdWkiOiJjNjZhYmRkYy02YWQ2LTRiOTctYWRlNC1iN2U0ZjE5NzYxNDEiLCJzaWQiOiI1MzRiNTZmZS1kMWIzLTRmNGQtYWNkZC03YzYwZTcyNjU5ZDUiLCJpc3MiOiJnaXRodWIuYXpjLmV4dC5ocC5jb20iLCJhdWQiOiJnaXRodWIuYXpjLmV4dC5ocC5jb20vX3NlcnZpY2VzL3ZzdG9rZW4iLCJuYmYiOjE2Nzk5NzQyMTIsImV4cCI6MTY3OTk3ODQxMn0.todVm9T1VwCZVGGLMdcixiV5rq_OhHYNxYyJMcMEOhuMVxVOFjTn68YjiObniLd0s_Ca22gnIrDZwF9-m5J43Rqxz7BFgX51kUQSnSNBS_nz1Ps_bDs44qdj6vwXcLv7YPeafsrZyvr66NpPGuf8ah-YThb_icvNQYwcbI1JTaojHiLpBQr8E3q5ku1QnmQcoyLiPdwVR2r1UUlQOrgE0yp1SumUiqadUP4W8J4ajRRHG1ghct_fHsRXHYU0g3kWIWqrPyLhnYm4KhCQWUptqMTbYlI-KZB8CjQcagWwDcaZJxrnQeIwrr81mpXE8-lGE2ZIEk7CmQQjRgTHRhnUHhuO9e2bnuPTnVbohFQaNiInQZyy4-7s1MmGntSf4wBvg5m8E935TSAIIP6HYrooI4QLkcD_WZkYV2yzFKI4saoTOXxzbBUOemYeuAVFbS7fvRb22sh0TgAW7MRgLrpgzOnyaxjkHeGJvYb7CAfHvrec07jG0AzkQeETLUfB5eAAz8AkTzhXzWfK7JcYygKEZQVjqvDO7LxCeZhxQddxd-b6yeXCFAA2J-gMDCUiDVV-A9YDP_5plHQOkDR_6M9ze3vqLlRpUCDOioSJurKj2Ehl1s-CG18Wjdn1Mci1S3MKVxfXEHPl0IBhGBRtAFR-gctLcd8-fzyu5g-sUIGjgBs' https://github.azc.ext.hp.com/_services/pipelines/_apis/distributedtask/packagedownload/agent/linux-x64/2.293.1


tar xzf ./actions-runner-linux-x64-2.293.1.tar.gz

./config.sh --url https://github.azc.ext.hp.com/BPSVCommonService/QA-Stage-Daily-Smoking-Test --token AAAHYN4GJIIYR2BOHRA7XTDEEJX2Y


./run.sh
