# DFIR Handbook — Chapter-wise Guide (Project Companion)

This chapter-wise handbook explains the concepts, techniques, and tools used throughout the `dfir-incident-investigation` repository. It is written for practitioners moving from triage to full incident response and detection engineering.

---

## Chapter 1 — Incident Overview & Threat Modeling

Purpose: define scope, assets, and attacker goals.

- Threat modeling: identify crown-jewel assets (finance data, credentials), attack surface (email, remote access), and capabilities required (phishing, remote execution, C2).
- Adversary TTP mapping: use MITRE ATT&CK to map probable techniques (e.g., T1566 Phishing, T1204 User Execution, T1071 C2).

Exercise: create an assets-prioritization matrix for your environment.

---

## Chapter 2 — Email & Phishing Analysis

Topics:
- Email header analysis: `Received` chain, SPF/DKIM/DMARC validation.
- Attachment triage: static inspection of Office macros, extracting VBA code.

Key commands/tools:
- `ripmime` / `munpack` to extract attachments
- `oletools` (oledump, olevba) to inspect macros

Example: run `olevba Invoice_0422.docm` to extract and deobfuscate VBA macro strings.

Deliverable: indicator list (malicious URLs, file names, email addresses) and safe copy of the artifact for sandboxing.

---

## Chapter 3 — Host Triage & Windows Forensics

Topics:
- Acquiring volatile data (memory) and non-volatile artifacts (registry, event logs).
- Key Windows artifacts: Run keys, Scheduled Tasks, Services, Prefetch, LNK files, MFT.

Commands/tools:
- `win32dd` or `DumpIt` for memory acquisition; `FTK Imager` for disk images.
- Windows Event logs: export EVTX and search for EventIDs (e.g., 4688 process creation, Sysmon EventIDs).
- Registry: use `reg.exe` or `RegRipper` to extract run keys.

Example detection:
- Search for `regsvr32` or suspicious `CommandLine` in process creation logs (Sysmon EventID 1).

---

## Chapter 4 — Malware Triage & Static Analysis

Topics:
- Binary identification, unpacking, string analysis, import table review, PE header checks.
- Quick triage steps: file type, entropy, string searches for C2 domains, embedded URIs.

Tools/commands:
- `file`, `strings`, `pefile` (Python), `rabin2`/`radare2`, `Ghidra`/`IDA Pro` for deeper reversing.
- YARA: write rules to detect strings or structural patterns.

Example YARA use:
```bash
yara -r detection/yara_rules/sample_yara.yar evidence/malware_metadata/svc.exe
```

Deliverable: a malware triage memo with hashes, suspicious strings, and recommended next steps (dynamic analysis sandboxing, memory dumps for network IOCs).

---

## Chapter 5 — Memory Forensics

Topics:
- When to capture memory, memory capture best practices, parsing memory with Volatility/Volatility3 and Rekall.
- Extracting process memory, network sockets, injected DLLs, and command history.

Commands/examples (Volatility 3):
```bash
vol -f memory.raw windows.pslist
vol -f memory.raw windows.netconnscan
vol -f memory.raw windows.malfind
```

Key outputs: suspicious process lists, in-memory strings, open network connections that may reveal in-memory-only C2 payloads.

---

## Chapter 6 — Network Forensics (Wireshark, Pyshark, TShark)

Topics:
- Capturing traffic policy, filtering, decrypting TLS where possible (via server keys or SSLKEYLOGFILE), identifying beaconing patterns.

Wireshark basics:
- Display filters: `http`, `tcp.port==443 && ip.addr==203.0.113.55`, `tls.handshake.type==1`.
- Follow streams: right-click TCP stream -> Follow -> TCP Stream.

Command-line (tshark) examples:
```bash
tshark -r capture.pcap -Y "ip.addr==203.0.113.55 && tcp.port==443" -T fields -e _ws.col.Time -e ip.src -e ip.dst -e tcp.len
```

Beacon detection approach:
- Aggregate connections by `src_ip` -> `dest_ip` with time-binning; look for periodicity (e.g., every 300s).

---

## Chapter 7 — Persistence Mechanisms & Windows Registry

Topics:
- Common persistence: Run keys (T1547), Services, Scheduled Tasks, WMI, DLL search order hijacks.
- Hunting for anomalies: uncommon services, base64-encoded service binaries, Run keys pointing to odd paths.

Detection hints:
- Monitor creation/modification of Registry Run keys; correlate with process creation events.

---

## Chapter 8 — Command-and-Control & Exfiltration

Topics:
- C2 channels (HTTP/S, DNS, custom protocols), typical C2 behaviours (beacons, long polling, piggybacking on legitimate services).
- Exfiltration patterns: unusual POSTs to cloud storage, large encrypted uploads, uncommon User-Agent strings.

SIEM example (Splunk):
```splunk
index=proxy dest_ip=203.0.113.55 | bin _time span=5m | stats count by _time, src_ip | where count > 6
```

---

## Chapter 9 — Detection Engineering (Sigma, Splunk, YARA)

Topics:
- Translating findings into detection content: YARA for binaries, Sigma for SIEM-agnostic rules, Splunk SPL saved searches.
- Rule lifecycle: write -> test on historical data -> calibrate thresholds -> promote to production.

Sigma example structure:
- `title`, `id`, `description`, `logsource`, `detection` (selection + condition), `level`.

Practical: convert `detection/sigma_rules/sample_suspicious_outbound.yml` into a Splunk saved search and test against `evidence/logs` extracts.

---

## Chapter 10 — Timeline Reconstruction & Correlation

Topics:
- Building a canonical timeline: normalize timestamps to UTC, reconcile clock skew, combine host, network, and cloud logs.
- Tools: `plaso`, `log2timeline`, custom pandas scripts for correlation.

Deliverable: an evidentiary timeline that supports the incident narrative and remediation decisions.

---

## Chapter 11 — Containment, Eradication & Recovery

Topics:
- Containment options: isolation, blocking IOCs at perimeter, temporary credential resets.
- Eradication: remove artifacts, validate absence of persistence, scoping for lateral movement.
- Recovery: rebuild, harden, and monitor restored systems.

Checklist: preserve images, rotate credentials, deploy updated detection, run hunting queries.

---

## Chapter 12 — Reporting, Communication & Legal Considerations

Topics:
- Executive summary writing, technical annexes, chain-of-custody documentation, coordination with legal/compliance.
- Evidence handling: hash all artifacts, preserve originals offline, track collection metadata.

Template: use files in `incident_report/` to structure final deliverables.

---

## Chapter 13 — Case Study: Phishing -> Downloader -> C2 (This Project)

Walkthrough: step-by-step replay of the repository's scenario linking artifacts to the MITRE mapping in `analysis/mitre_mapping.md`.

Key links:
- `analysis/iocs.md` (IoCs)
- `analysis/timeline.md` (chronology)
- `detection/splunk_queries.md` and `detection/sigma_rules/` (detections)

---

## Chapter 14 — Tools Appendix (Quick Reference)

- Wireshark / TShark: capture and analyze PCAPs. Useful filters: `ip.addr==X`, `http.request`, `tls.handshake.type==1`.
- Volatility / Rekall: memory analysis, `pslist`, `malfind`, `netscan`.
- YARA: pattern-based binary detection. `yara -r rules.yar sample.exe`.
- Sigma: write SIEM-agnostic rule, test and convert into SIEM native query.
- Splunk: SPL basics — `index=... | stats count by ... | where count>n`.
- Python/pandas: timeline normalization and correlation scripts.

---

## Chapter 15 — Exercises & Labs

1. Extract and analyze VBA macro from `Invoice_0422.docm` using `olevba`.
2. Compute hashes of `svc.exe` using `scripts/hash_checker.py` and cross-check with `analysis/iocs.md`.
3. Use `tshark` to extract TLS sessions with `203.0.113.55` and search for periodicity.
4. Write a Sigma rule to detect new Run key creations and test against sample logs.

---

## Chapter 16 — Further Reading & Resources

- MITRE ATT&CK: https://attack.mitre.org
- Volatility Framework: https://www.volatilityfoundation.org
- Wireshark documentation: https://www.wireshark.org/docs/
- YARA: https://virustotal.github.io/yara/
- Sigma rules repo: https://github.com/SigmaHQ/sigma

---

## How to Download / Convert to Word/PDF

If you want a `.docx` or `.pdf` for recruiters, use `pandoc` (requires installation):

```bash
pandoc docs/dfir_handbook_chapters.md -o dfir_handbook_chapters.docx
pandoc docs/dfir_handbook_chapters.md -o dfir_handbook_chapters.pdf
```

You can also open the Markdown directly in code editors for download.

---

If you want, I can also generate a polished `.docx` (converted via `pandoc`) and place it in `docs/` — shall I do that now? 
