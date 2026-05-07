# Investigator Notes

Primary analyst: [REDACTED]
Date: 2026-05-06

This file captures quick notes, hypotheses, and triage pointers used during the investigation.

- Initial detection: high volume of failed authentication attempts followed by successful lateral RDP from host `CORP-WS-23`.
- Observed suspicious outbound connections to `203.0.113.55` over TCP/443 with unusual TLS fingerprints.
- Candidate indicators collected in `analysis/iocs.md`.

See `analysis/timeline.md` for a detailed chronological reconstruction.
