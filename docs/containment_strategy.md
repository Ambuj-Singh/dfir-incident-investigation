# Containment Strategy

Immediate actions:
- Isolate compromised host from network and disable accounts used for lateral movement.
- Block outbound connections to identified C2 IPs and domains at perimeter controls.

Forensic actions:
- Acquire memory dump and forensic image of suspected host(s) prior to reimaging.
- Collect relevant logs and preserve chain-of-custody documentation.
