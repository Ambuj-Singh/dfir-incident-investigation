#!/usr/bin/env python3
"""log_parser.py

Simple log parser to extract suspicious events (e.g., Run keys, regsvr32 execution,
and outbound connections) from a Sysmon-style log export (CSV/TSV).

This is a starter utility to demonstrate automation used during triage.
"""
import csv
from pathlib import Path
import sys


def parse_sysmon_csv(path: Path):
    suspicious = []
    with path.open() as fh:
        reader = csv.DictReader(fh)
        for row in reader:
            cmd = row.get('CommandLine', '') or row.get('Message', '')
            image = row.get('Image', '')
            if 'regsvr32' in cmd.lower() or 'svc.exe' in image.lower() or 'Run\\SysHelper' in cmd:
                suspicious.append({'Time': row.get('TimeCreated', row.get('_time')), 'Host': row.get('Computer', row.get('Host')), 'Image': image, 'CommandLine': cmd})
    return suspicious


def main():
    if len(sys.argv) < 2:
        print('Usage: python log_parser.py <sysmon.csv>')
        sys.exit(2)
    p = Path(sys.argv[1])
    if not p.exists():
        print(f'File not found: {p}')
        sys.exit(1)
    items = parse_sysmon_csv(p)
    for i in items:
        print(i)


if __name__ == '__main__':
    main()
