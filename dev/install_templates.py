import glob
import os
from datetime import datetime
from pathlib import Path

from dev.console import COLOR
from dev.project import Project

# Install the character templates into the User's AppData folder.
# Renames the .json files to .txt

src_dir = Project.template_dir
dst_dir = os.path.join(Path.home(), "AppData", "LocalLow", "Lafrontier", "Elin", "User", "PCC")

json_files = glob.glob(os.path.join(src_dir, "*.json"))

for json_file in json_files:
    name = os.path.basename(os.path.splitext(json_file)[0])

    txt_file = os.path.join(dst_dir, name + ".txt")

    result = Project.copy(json_file, txt_file)
    print(f"Template: \"{COLOR.GREEN}{name}{COLOR.RESET}\" [{result.console()}]")

print("\n----------\n")
print(f"Completed copy at {datetime.now().isoformat()}")
