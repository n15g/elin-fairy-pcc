import glob
import os
from datetime import datetime
from pathlib import Path

from dev.console import COLOR
from dev.project import Project

src_dir = Project.aseprite_dir

# Scripts
script_dir = os.path.join(Path.home(), "AppData", "Roaming", "Aseprite", "scripts")
lua_files = glob.glob(os.path.join(src_dir, "*.lua"))
for json_file in lua_files:
    name = os.path.basename(json_file)

    dst_file = os.path.join(script_dir, name)

    result = Project.copy(json_file, dst_file)
    print(f"Script: \"{COLOR.GREEN}{name}{COLOR.RESET}\" [{result.console()}]")

# Palettes
palette_dir = os.path.join(Path.home(), "AppData", "Roaming", "Aseprite", "palettes")
palette_files = glob.glob(os.path.join(src_dir, "*.pal"))
for palette_file in palette_files:
    name = os.path.basename(palette_file)

    dst_file = os.path.join(palette_dir, name)

    result = Project.copy(palette_file, dst_file)
    print(f"Palette: \"{COLOR.GREEN}{name}{COLOR.RESET}\" [{result.console()}]")

print("\n----------\n")
print(f"Completed copy at {datetime.now().isoformat()}")
