
Invoke-WebRequest -Headers @{ 'Authorization' = 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IlREYjU0V0Q5S1ZiLW5FZzM4VFdlQ2V0b1hqTSJ9.eyJuYW1laWQiOiJkZGRkZGRkZC1kZGRkLWRkZGQtZGRkZC1kZGRkZGRkZGRkZGQiLCJzY3AiOiJBY3Rpb25zUnVudGltZS5QYWNrYWdlRG93bmxvYWQiLCJJZGVudGl0eVR5cGVDbGFpbSI6IlN5c3RlbTpTZXJ2aWNlSWRlbnRpdHkiLCJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9zaWQiOiJERERERERERC1ERERELUREREQtRERERC1EREREREREREREREQiLCJodHRwOi8vc2NoZW1hcy5taWNyb3NvZnQuY29tL3dzLzIwMDgvMDYvaWRlbnRpdHkvY2xhaW1zL3ByaW1hcnlzaWQiOiJkZGRkZGRkZC1kZGRkLWRkZGQtZGRkZC1kZGRkZGRkZGRkZGQiLCJhdWkiOiIxN2E3OWRmZS04MGQwLTQ3ZmQtYTdiNC1jOWVmNTJjMGNhYjgiLCJzaWQiOiIxM2RiNTRhOS0xM2E3LTQ4YWMtYTFmNS1lZGUzODYxNTE5YWIiLCJpc3MiOiJnaXRodWIuYXpjLmV4dC5ocC5jb20iLCJhdWQiOiJnaXRodWIuYXpjLmV4dC5ocC5jb20vX3NlcnZpY2VzL3ZzdG9rZW4iLCJuYmYiOjE2Nzk4OTc1ODAsImV4cCI6MTY3OTkwMTc4MH0.NvgeFtogT9PJkl8Mql-RTJ7l-3hiiprQVj0AvsdNdwwdP7k5SKDHbR_sR3b7EiEqc8Lsm5h1ISqjY8MkGl3qy19YNvCNw1KmFZB37hrnh0t2jY1WZHnKgANM0c3wvRLLgzGvuVvuFUrP6Vcbu4Kc5OHYbVCIb0l7v7XbDFgjRSe4NZNTxuH6bK0mockLwf8EfUwLGf_83ssVeDbL35h9wApnVl6PC5ar3mcgEqMJPtsVED7w3nc-46exAFHGNsOQU30aMg-knMTaLDyKfW_4xoAIp_CZ8bZ5WobmugSkeK1Ft-c0LXjh-uz53KEFOQyRaUcPzssqzfPYuvYS37hi_bgkFWJfY--OeztcdlX5Ubnbsv8XH1SuxpCwmAOaDZkX8zmfTz4Vi9sLJcEK4WNPmPNUDajwarjgW_Ttu25Ag-Xj-670bzkNU0Xik3J1ELlzYsicETCdSvibp5Tfn9EgEJiyReTZ8qj9h-3ADFr1yGmm_ZoC_iUchN0cYzl5xIvbfkgSD9S6irjpsO77vTaL2LFXF5ekoapLgT2tV5048i7nhdTi0AHl49SozkU7Nl8nMoLOgVKuVkHeqLj3WgIAqgvu5SGJvLmpqJxsb7qGCESzghYxnbPmjHON0P47RTdHDeUAcnXRjLhe199ZQLtO0KTwR88rAIib_jNDDtzL1VY' } -Uri https://github.azc.ext.hp.com/_services/pipelines/_apis/distributedtask/packagedownload/agent/win-x64/2.293.1 -OutFile actions-runner-win-x64-2.293.1.zip


if((Get-FileHash -Path actions-runner-win-x64-2.293.1.zip -Algorithm SHA256).Hash.ToUpper() -ne 'c940816cbaafa7992e18c88bc1d00ce7578cfacfa19671ccea682ad323229153'.ToUpper()){ throw 'Computed checksum did not match' }

Add-Type -AssemblyName System.IO.Compression.FileSystem ; [System.IO.Compression.ZipFile]::ExtractToDirectory("$PWD/actions-runner-win-x64-2.293.1.zip", "$PWD")



./config.cmd --url https://github.azc.ext.hp.com/BPSVCommonService/QA-Stage-Daily-Smoking-Test --token AAAHYNYP4L4RPEDIHC6GFGDEEFCFG
