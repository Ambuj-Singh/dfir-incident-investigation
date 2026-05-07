# Remediation Plan

Priority remediation actions (immediate -> long-term):

1. Containment
   - Isolate compromised endpoints (CORP-WS-23) from the network.
   - Reset credentials for accounts with suspicious activity; enforce MFA.

2. Eradication
   - Remove malicious binaries: `C:\ProgramData\syshelper\svc.exe`.
   - Remove persistence artifacts: `HKLM\\Software\\Microsoft\\Windows\\CurrentVersion\\Run\\SysHelper`.

3. Recovery
   - Reimage affected hosts when root cause cannot be fully validated.
   - Restore files from known-good backups and rotate keys.

4. Lessons and improvements
   - Tighten email filtering and block known malicious domains/IP addresses.
   - Expand endpoint telemetry and implement application whitelisting for high-risk assets.

See `detection/` for SIEM detections to implement.
