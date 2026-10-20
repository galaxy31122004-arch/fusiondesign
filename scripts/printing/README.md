# Bambu Studio preset preparation

[prepare_presets.py](prepare_presets.py) resolves the installed Bambu Studio profile inheritance for P2S 0.4 mm, Bambu PETG HF and 0.20 mm Standard. It writes temporary machine, process and filament JSON files to `projects/box-hybrid-lora/runs/resolved_presets/`. Override the source directory with `BAMBU_STUDIO_PROFILE_ROOT` when Bambu Studio is installed elsewhere.

The script does not slice or send a print job. Verify effective G-code values after slicing, including `printer_model`, `nozzle_diameter`, `filament_type`, `curr_bed_type`, bed temperature and warnings. The print packages and their measured slicer results are documented in [print/sliced](../../projects/box-hybrid-lora/print/sliced/README.md).
