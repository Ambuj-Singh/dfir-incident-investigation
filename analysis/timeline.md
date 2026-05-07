# Attack Timeline Reconstruction

2026-04-22 08:12 UTC — Phishing email delivered to `alice.smith@corp.example.com` (T1566)

2026-04-22 08:28 UTC — `Invoice_0422.docm` opened; macro executed `regsvr32` with remote DLL (T1204.002)

2026-04-22 08:33 UTC — Downloader fetched payload from `http://malware-serve.example[.]com/payload.bin` (T1105)

2026-04-22 08:36 UTC — Payload written to `C:\ProgramData\syshelper\svc.exe` and a Run key created for persistence (T1547.001)

2026-04-22 09:15 UTC — Outbound TLS connections to `203.0.113.55:443` observed, periodic beacons every 300s (T1071.001)

2026-04-23 03:20 UTC — Enumeration activity and staging of `C:\Users\Alice\Documents\CompDocs.zip` detected; partial exfil attempt via HTTPS POST to `storage.example-cloud[.]com` (T1020)

Investigation notes: timestamps reconstructed from `evidence/logs/sysmon.log` and proxy logs.
