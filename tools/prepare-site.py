#!/usr/bin/env python3
"""Run after overlaying Pencil exports; preserve the site's implementation layer."""
from pathlib import Path
import runpy
HERE=Path(__file__).resolve().parent
for script in ('build-sister-page.py','apply-footer-partner-links.py','apply-responsive.py'):
    runpy.run_path(str(HERE/script),run_name='__main__')
