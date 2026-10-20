"""Read-only MeshRight geometry check for Fusion mesh exports."""

import argparse
import json
import subprocess
import sys
from pathlib import Path


def check(executable, path):
    result = subprocess.run(
        [executable, "check", str(path), "--json"],
        capture_output=True, text=True, timeout=180, check=False,
    )
    if result.returncode not in (0, 1):
        raise RuntimeError(result.stderr.strip() or
                           f"MeshRight exited with code {result.returncode}")
    data = json.loads(result.stdout)
    stats = data["stats"]
    issues = [{"code": issue["code"], "severity": issue["severity"],
               "title": issue["title"], "count": issue["count"]}
              for issue in data["issues"]]
    return {
        "file": str(path),
        "geometry_status": "fail" if not data["printable"] else
                           ("warning" if issues else "pass"),
        "watertight": stats["watertight"],
        "pieces": stats["pieces"],
        "size_mm": stats["size_mm"],
        "triangles": stats["triangles"],
        "issues": issues,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("meshes", nargs="+", type=Path)
    parser.add_argument("--meshright", default="meshright",
                        help="MeshRight CLI executable; optional dependency")
    parser.add_argument("--output", type=Path, help="write a JSON report")
    args = parser.parse_args()

    report = {"checker": "MeshRight check --json", "scope": "mesh geometry only",
              "not_checked": ["support", "brim", "material", "slicer profile",
                              "functional fit", "water resistance"], "meshes": []}
    try:
        for path in args.meshes:
            if not path.is_file():
                raise FileNotFoundError(path)
            report["meshes"].append(check(args.meshright, path))
    except (FileNotFoundError, OSError, RuntimeError, ValueError,
            json.JSONDecodeError, subprocess.TimeoutExpired) as exc:
        print(f"Mesh check could not finish: {exc}", file=sys.stderr)
        return 2

    output = json.dumps(report, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(output, encoding="utf-8")
    else:
        print(output, end="")
    return 1 if any(item["geometry_status"] == "fail" for item in report["meshes"]) else 0


if __name__ == "__main__":
    sys.exit(main())
