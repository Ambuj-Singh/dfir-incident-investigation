# Findings

1. Email-based initial access.
   - Email headers show external sender with display name impersonating accounting.
   - Attachment contained obfuscated macro that executed `regsvr32`.

2. Malware persistence and execution.
   - Binary `svc.exe` placed in `C:\\ProgramData\\syshelper`.
   - Registry run key created for persistence (T1547.001).

3. C2 communications and unusual TLS.
   - Periodic beacons to `203.0.113.55:443` with long-lived TCP sessions.
   - TLS fingerprint differs from mainstream libraries — indicator of custom/shell TLS.

4. Evidence of data staging.
   - Compression of documents and attempted upload to cloud storage endpoint.

Impact: Confidential business documents and credentials potentially exposed. Recommend the remediation steps in `incident_report/remediation_plan.md`.
