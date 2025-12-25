"""Test configuration to import the scrap modules."""

import sys
from pathlib import Path


SCRAP_DIR = Path(__file__).resolve().parents[1] / "scrap"
sys.path.insert(0, str(SCRAP_DIR))
