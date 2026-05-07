# MITRE ATT&CK Mapping

The following techniques were observed or are strongly suspected during the incident.

- Initial Access: Phishing (T1566)
- User Execution: Malicious Office Macro (T1204.002)
- Command and Scripting Interpreter: Regsvr32 (T1218)
- Persistence: Registry Run Keys/Startup Folder (T1547.001)
- Exfiltration: Exfiltration Over C2 Channel / Exfiltration to Cloud Storage (T1041 / T1020)
- Command-and-Control: Application Layer Protocol (HTTP/S) (T1071.001)

Each finding in `analysis/findings.md` references these technique IDs where applicable.
