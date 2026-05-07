# Splunk / SIEM Query Examples

## Detect registry run key persistence
```splunk
index=wineventlog EventCode=13 OR EventCode=12
| where CommandLine like "%Run\\SysHelper%" OR Image like "%svc.exe%"
| table _time, host, user, CommandLine, Image
```

## Detect suspicious outbound TLS beacons (high frequency)
```splunk
index=proxy (dest_ip=203.0.113.55 OR dest_domain="malware-serve.example.com")
| bin _time span=5m
| stats count by _time, src_ip, dest_ip, dest_port
| where count > 10
```
