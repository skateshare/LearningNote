curl -o actions-runner-linux-x64-2.293.1.tar.gz -L -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IlREYjU0V0Q5S1ZiLW5FZzM4VFdlQ2V0b1hqTSJ9.eyJuYW1laWQiOiJkZGRkZGRkZC1kZGRkLWRkZGQtZGRkZC1kZGRkZGRkZGRkZGQiLCJzY3AiOiJBY3Rpb25zUnVudGltZS5QYWNrYWdlRG93bmxvYWQiLCJJZGVudGl0eVR5cGVDbGFpbSI6IlN5c3RlbTpTZXJ2aWNlSWRlbnRpdHkiLCJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9zaWQiOiJERERERERERC1ERERELUREREQtRERERC1EREREREREREREREQiLCJodHRwOi8vc2NoZW1hcy5taWNyb3NvZnQuY29tL3dzLzIwMDgvMDYvaWRlbnRpdHkvY2xhaW1zL3ByaW1hcnlzaWQiOiJkZGRkZGRkZC1kZGRkLWRkZGQtZGRkZC1kZGRkZGRkZGRkZGQiLCJhdWkiOiJlOGNjOWYwZS0yOGY4LTRhNWQtOGI2OS04M2YyMWVmNjg1MzYiLCJzaWQiOiI5MzEwOWU1Yi1iNjFlLTQ5NmQtOGZhYy0xMGRiZjhmMjE3NzYiLCJpc3MiOiJnaXRodWIuYXpjLmV4dC5ocC5jb20iLCJhdWQiOiJnaXRodWIuYXpjLmV4dC5ocC5jb20vX3NlcnZpY2VzL3ZzdG9rZW4iLCJuYmYiOjE2ODA3NjY1MzYsImV4cCI6MTY4MDc3MDczNn0.O5wxwDoruDwkJI0tGjgckdQDjbMRPZqotEirolm7Yi6TUbPD6nW2lYgmvSqtxgjIGMp0xD296kvkrUKQaSj_3aYpQwaTv_UsvWGbKLHwlImS6IfFM4QegrscdO4-DGpnZzcmbf8HYbxtHrEDDQS6WbiCLQ57-RJyl82321xk4uTuH4KUOpL8zkMEVo0ZxJmqpdzJA2yimPR_53DIgLcddiW2yOwoEXcNul0AJXPDj-N75DcL-bWdZfJW_KV9sT_qBLkTsT3mjgTsTlt4IovsDlO_n4fFhD7mvzRRH5Y-QuvcizGaDsTM6amy20ETelUBdU9zWsylVW9qcZfOijnzlG_xtaFllnR7m4RIUWdE0QV8W_Fox9sRKaNg3scqIdLK538RTcKx5WWetDt_llQHe6WpWWLc16aISVnVQ5dRnJAs4WTCLW31DqDsXVf7tJCgsNmC_RILp1PrquawAWxQ7T_M7WSloRHhJ26gimIxJ2hqhomQ1rpCpNoeMKF8yN9ABr-6wPJekcSKEj7o1h7WBkXqtZXGg8Z5zHTNArRcg6Dt0uQDmEEC4y2BEZDnO_v8fXoULmwb17PGBVfBvYy1hc-f7Ij_IRXXGKgTDNfw1qXRD6sIy390mwBAxquRSNyBHjxEsSKboC2zRH9Ie5i1InGJc8WJ6wWBbxkLVe4V1Ck' https://github.azc.ext.hp.com/_services/pipelines/_apis/distributedtask/packagedownload/agent/linux-x64/2.293.1

tar xzf ./actions-runner-linux-x64-2.293.1.tar.gz


./config.sh --url https://github.azc.ext.hp.com/BPSVCommonService/QA-Stage-Daily-Smoking-Test --token AAAHYNZDUXLYZNCHJL2AVILEF2DK6
