#!/usr/bin/env python3
"""hash_checker.py

Small utility to compute file hashes (MD5, SHA1, SHA256) and compare
against a provided IoC list (simple JSON or text file).

Usage: python scripts/hash_checker.py /path/to/file
"""
import sys
import hashlib
from pathlib import Path


def compute_hashes(path: Path) -> dict:
    """Compute MD5, SHA1, SHA256 for the given file."""
    h_md5 = hashlib.md5()
    h_sha1 = hashlib.sha1()
    h_sha256 = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h_md5.update(chunk)
            h_sha1.update(chunk)
            h_sha256.update(chunk)
    return {"md5": h_md5.hexdigest(), "sha1": h_sha1.hexdigest(), "sha256": h_sha256.hexdigest()}


def main():
    if len(sys.argv) < 2:
        print("Usage: python hash_checker.py <file>")
        sys.exit(2)
    p = Path(sys.argv[1])
    if not p.exists():
        print(f"File not found: {p}")
        sys.exit(1)
    hashes = compute_hashes(p)
    print(f"Hashes for {p}:\nMD5: {hashes['md5']}\nSHA1: {hashes['sha1']}\nSHA256: {hashes['sha256']}")


if __name__ == "__main__":
    main()
