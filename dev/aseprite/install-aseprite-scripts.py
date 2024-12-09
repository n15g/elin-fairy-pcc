import glob
import os
from datetime import datetime
from pathlib import Path

from dev.console import COLOR
from dev.project import Project

src_dir = Project.aseprite_dir
dst_dir = os.path.join(Path.home(), "AppData", "Roaming", "Aseprite", "scripts")

lua_files = glob.glob(os.path.join(src_dir, "*.lua"))

for json_file in lua_files:
    name = os.path.basename(json_file)

    txt_file = os.path.join(dst_dir, name)

    result = Project.copy(json_file, txt_file)
    print(f"Script: \"{COLOR.GREEN}{name}{COLOR.RESET}\" [{result.console()}]")

print("\n----------\n")
print(f"Completed copy at {datetime.now().isoformat()}")
