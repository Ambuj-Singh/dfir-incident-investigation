# Final Investigative Report

## Overview
This final report consolidates the technical analysis, timeline, indicators of compromise (IoCs), and recommended remediation steps.

## Summary of Findings
- Phishing email delivered to `alice.smith@corp.example.com` containing `Invoice_0422.docm` (macro)
- Execution of `Invoice_0422.docm` spawned `regsvr32` abusing a crafted DLL loader.
- Downloader fetched `http://malware-serve.example[.]com/payload.bin` and installed as `C:\ProgramData\syshelper\svc.exe`.
- Persistence achieved via Registry Run key: `HKLM\Software\Microsoft\Windows\CurrentVersion\Run\SysHelper`.
- C2 beacons to `203.0.113.55:443` with custom TLS; lateral movement evidence on internal host `10.10.12.4`.

Complete technical annexes are available in `analysis/` and `evidence/`.
