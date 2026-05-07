#!/usr/bin/env python3
"""ioc_parser.py

Lightweight parser to extract IoCs from `analysis/iocs.md` into structured JSON.
Designed to help automate ingestion into detection platforms during an investigation.
"""
import re
import json
from pathlib import Path


def parse_iocs(md_path: Path) -> dict:
    text = md_path.read_text(encoding="utf-8")
    ips = re.findall(r"\b(?:\d{1,3}\.){3}\d{1,3}\b", text)
    domains = re.findall(r"\b[\w.-]+\.(?:com|net|org|local|cloud)\b", text)
    hashes = re.findall(r"\b[a-fA-F0-9]{32,64}\b", text)
    return {"ips": sorted(set(ips)), "domains": sorted(set(domains)), "hashes": sorted(set(hashes))}


def main():
    md = Path("analysis/iocs.md")
    if not md.exists():
        print("analysis/iocs.md not found")
        return
    iocs = parse_iocs(md)
    out = Path("analysis/iocs_parsed.json")
    out.write_text(json.dumps(iocs, indent=2))
    print(f"Wrote parsed IoCs to {out}")


if __name__ == "__main__":
    main()
