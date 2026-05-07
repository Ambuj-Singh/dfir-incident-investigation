# Executive Summary

On 2026-04-22, a targeted phishing campaign successfully delivered a macro-enabled document to multiple employees in the Finance and HR business units. One user executed the document which led to a downloader establishing persistence and a command-and-control channel. The attacker subsequently enumerated local files and performed simulated exfiltration of a subset of sensitive documents.

Key impact:
- Initial compromise via phishing (ATT&CK: T1566)
- Malware execution and persistence (ATT&CK: T1059, T1547)
- C2 over HTTPS (ATT&CK: T1071.001)
- Potential data staging/exfiltration (ATT&CK: T1020)

Recommended priority actions are contained in `incident_report/remediation_plan.md`.
