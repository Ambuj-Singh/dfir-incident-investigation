#!/usr/bin/env python3
"""Convert DOCX to PDF using docx2pdf (Windows COM or LibreOffice backend).

This script attempts conversion and prints clear error messages if it fails.
"""
import sys
from pathlib import Path


def main():
    src = Path('docs/dfir_handbook_chapters.docx')
    dst = Path('docs/dfir_handbook_chapters.pdf')
    if not src.exists():
        print('Source DOCX not found:', src)
        sys.exit(1)
    try:
        from docx2pdf import convert
    except Exception as e:
        print('docx2pdf not installed or failed to import:', e)
        sys.exit(2)
    try:
        convert(str(src), str(dst))
        print('Wrote', dst)
    except Exception as e:
        print('Conversion failed:', e)
        sys.exit(3)


if __name__ == '__main__':
    main()
