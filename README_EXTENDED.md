## Investigation Workflow

1. Triage incoming alert: identify affected host and initial indicator(s).
2. Collect EDR, Sysmon, and network telemetry for the time window.
3. Acquire volatile memory image and disk image if evidence thresholds are met.
4. Perform static and dynamic analysis on recovered binaries.
5. Map findings to ATT&CK, document IoCs, and create detections.

## Tools Used
- Sysinternals (Procmon, Autoruns)
- Volatility / Rekall for memory analysis
- YARA for pattern detection
- Splunk / Elastic / SIEM for log analysis
- Wireshark / Pyshark for network analysis

## Skills Demonstrated
- Endpoint and network forensics
- Malware triage and reverse-engineering basics
- SIEM detection development (Splunk/Sigma)
- Incident response coordination and remediation planning

## Future Improvements
- Expand detection coverage to include anomaly-based ML models.
- Hardened build and baseline verification for endpoints.
