# Investigator Notes (analysis folder)

- Evidence sources: Endpoint Sysmon, Windows Event Logs, Proxy logs, Network PCAP.
- Chain of custody: collected images and network captures stored offline; checksums logged in `evidence/malware_metadata/`.
- Priorities: preserve memory dump of `CORP-WS-23` and capture full `svc.exe` binary for static analysis.
