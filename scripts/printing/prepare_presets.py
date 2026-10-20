"""Resolve installed Bambu Studio preset inheritance for a CLI test slice."""

import json
import os
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def profile_root():
    configured = os.environ.get("BAMBU_STUDIO_PROFILE_ROOT")
    if configured:
        candidates = [Path(configured)]
    else:
        candidates = [
            Path(os.environ.get("APPDATA", "")) / "BambuStudio" / "system" / "BBL",
            Path(r"D:\Application\Bambu Studio\resources\profiles\BBL"),
        ]
    for candidate in candidates:
        if (candidate / "machine" / "Bambu Lab P2S 0.4 nozzle.json").is_file():
            return candidate
    raise FileNotFoundError("Bambu Studio P2S profiles not found; set BAMBU_STUDIO_PROFILE_ROOT")


PRESETS = profile_root()
OUTPUT = ROOT / "projects" / "box-hybrid-lora" / "runs" / "resolved_presets"
SELECTED = {
    "machine": "Bambu Lab P2S 0.4 nozzle",
    "process": "0.20mm Standard @BBL P2S",
    "filament": "Bambu PETG HF @BBL P2S 0.4 nozzle",
}


def resolve(kind, name, seen=None):
    seen = seen or set()
    if name in seen:
        raise ValueError(f"Circular preset dependency: {name}")
    path = PRESETS / kind / f"{name}.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    inherited = data.get("inherits")
    result = resolve(kind, inherited, seen | {name}) if inherited else {}
    for included in data.get("include", []):
        result.update(resolve(kind, included, seen | {name}))
    result.update({key: value for key, value in data.items()
                   if key not in ("inherits", "include")})
    return result


def main():
    OUTPUT.mkdir(parents=True, exist_ok=True)
    print(f"Source: {PRESETS}")
    for kind, name in SELECTED.items():
        resolved = resolve(kind, name)
        if kind == "process":
            resolved["curr_bed_type"] = "Textured PEI Plate"
        target = OUTPUT / f"{kind}.json"
        target.write_text(json.dumps(resolved, ensure_ascii=False, indent=2) + "\n",
                          encoding="utf-8")
        print(f"{target}: {len(resolved)} settings")


if __name__ == "__main__":
    main()
