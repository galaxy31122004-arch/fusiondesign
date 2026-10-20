# Bambu Studio preset preparation

[prepare_presets.py](prepare_presets.py) resolves the installed Bambu Studio profile inheritance for P2S 0.4 mm, Bambu PETG HF and 0.20 mm Standard. It writes temporary machine, process and filament JSON files to the run directory selected by `FUSIONDESIGN_RUN_DIR`, or `projects/box-hybrid-lora/runs/<yyyymmdd>-preset-check/presets/` by default. Override the source directory with `BAMBU_STUDIO_PROFILE_ROOT` when Bambu Studio is installed elsewhere.

The script does not slice or send a print job. Verify effective G-code values after slicing, including `printer_model`, `nozzle_diameter`, `filament_type`, `curr_bed_type`, bed temperature and warnings. The current print status and slicer results are documented in [Box HybridLora results](../../projects/box-hybrid-lora/notes/results.md).

Bambu CLI writes `result.json` and G-code into `--outputdir`; always set it to a named `runs/<yyyymmdd>-<mục-đích>/` directory. Copy the effective values, warnings and source file names to `notes/results.md` before cleaning the run. The mesh checker JSON is also transient; record its geometry findings in `notes/results.md`. No script in this folder sends a print command.

## Optional mesh check

[check_mesh.py](check_mesh.py) calls MeshRight's read-only `check --json` command on Fusion mesh exports. It records watertightness, disconnected pieces, dimensions and geometry issues; it deliberately omits MeshRight's score and solid-PLA weight because neither proves P2S printability. Bambu Studio still decides support/brim/profile and must preview the slice. The script never repairs or overwrites a mesh.

Install [MeshRight](https://github.com/Huzy85/MeshRight) separately and pass its executable with `--meshright` if it is not on `PATH` ([source and CLI](https://github.com/Huzy85/MeshRight/blob/main/src/meshright/cli.py), read 2026-10-20; RSCH-20261020-0005). It is an early-alpha GPL-3.0 tool, so the repo invokes its CLI without copying its source or making it a mandatory dependency. On this machine Python 3.14 could not install the full package because `pymcubes` required C++ Build Tools; an isolated check-only environment under the ignored `runs/` directory was used to verify the adapter.

```powershell
py -3 scripts/printing/check_mesh.py --meshright path/to/meshright.exe --output projects/<id>/runs/mesh-check.json path/to/body.3mf path/to/lid.3mf
```
