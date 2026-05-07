# Attack Flow

High-level sequence of the simulated attack:

1. Phishing email with `Invoice_0422.docm` delivered to user.
2. User enables macros; loader executed via `regsvr32` to bypass execution policy (T1218).
3. Downloader retrieves second-stage payload from `malware-serve.example.com` (T1105).
4. Malware establishes persistence and begins periodic C2 beacons to `203.0.113.55` (T1547, T1071.001).
5. Attacker performs discovery and stages files for exfiltration; uses cloud storage endpoint to exfiltrate (T1020).
