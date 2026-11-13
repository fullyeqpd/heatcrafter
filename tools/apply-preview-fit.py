#!/usr/bin/env python3
"""Compatibility entry point: responsive layouts supersede phone/tablet zoom."""
from pathlib import Path
import runpy
runpy.run_path(str(Path(__file__).with_name('apply-responsive.py')),run_name='__main__')
