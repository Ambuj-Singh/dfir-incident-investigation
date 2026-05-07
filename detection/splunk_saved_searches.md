# Saved Searches / Example Alerts

1. High frequency outbound TLS beaconing
   - Saved search: `index=proxy dest_ip=203.0.113.55 | bin _time span=1m | stats count by src_ip | where count > 6`

2. Run key creation (Windows Event Tracking)
   - Saved search: `index=wineventlog EventCode=13 CommandLine=*Run\\SysHelper* | table _time, host, user, CommandLine`
