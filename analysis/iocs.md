# Indicators of Compromise (IoCs)

## Domains and URLs
- malware-serve.example[.]com  -> http://malware-serve.example.com/payload.bin
- storage.example-cloud[.]com -> used for simulated exfil

## IP addresses
- 203.0.113.55 (C2 server)
- 198.51.100.12 (malicious drop host)

## File paths and filenames
- C:\\ProgramData\\syshelper\\svc.exe
- Invoice_0422.docm (malicious macro)

## Hashes
- svc.exe (SHA256): c2f3e5a6b0a4d3e1c9f7b6d5e4a3b2c1d0e9f8a7b6c5d4e3f2a1b0c9d8e7f6a
- Invoice_0422.docm (MD5): d41d8cd98f00b204e9800998ecf8427e

## Registry
- HKLM\\Software\\Microsoft\\Windows\\CurrentVersion\\Run\\SysHelper -> C:\\ProgramData\\syshelper\\svc.exe

> Note: Hashes and indicators are synthetic examples for portfolio demonstration only.
