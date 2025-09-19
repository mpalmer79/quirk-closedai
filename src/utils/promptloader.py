from pathlib import Path
from typing import Optional


BASE = Path(__file__).resolve().parents[2] # repo root
CONFIG = BASE / "config"


class Prompts:
def __init__(self):
self.meta = self._read(CONFIG / "meta_prompt.md")
self.system = self._read(CONFIG / "system_prompt.md")
self.subprompts = {}
subdir = CONFIG / "prompts"
if subdir.exists():
for p in subdir.glob("*.md"):
self.subprompts[p.stem.lower()] = self._read(p)


def _read(self, path: Path) -> str:
return path.read_text(encoding="utf-8") if path.exists() else ""


def compose(self, department: Optional[str] = None) -> str:
parts = [self.meta, "\n---\n", self.system]
if department:
dep = self.subprompts.get(department.lower())
if dep:
parts.extend(["\n---\n", dep])
return "".join(parts).strip()
