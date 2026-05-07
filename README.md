# DFIR Incident Investigation — Enterprise Simulation

Project: dfir-incident-investigation

This repository is a professional-quality DFIR portfolio project simulating a realistic enterprise security incident involving phishing, malware execution, persistence, command-and-control (C2) behavior, and potential data exfiltration. The content, findings, and artifacts are synthetic and intended for demonstrative and hiring/recruiting purposes.

## Project Overview

- Attack vector: targeted phishing email containing a weaponized attachment and a malicious macro.
- Malware: downloader -> second-stage payload with persistence and C2 beaconing.
- Data exfiltration: simulated exfil to cloud storage via encrypted channel.

See `docs/attack_flow.md` for the complete attack narrative and `analysis/` for reconstructed artifacts.

## Quick start

1. Create Python virtual environment and install dependencies:

```bash
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
pip install -r requirements.txt
```

2. Run utilities in `scripts/` to parse IoCs and process sample logs.

## Structure

Top-level layout mirrors industry incident packages and contains evidence, analysis, detection rules, and reproducible investigator notes.
