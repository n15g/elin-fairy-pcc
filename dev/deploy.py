import os
import shutil
import sys
from datetime import datetime

from dev.console import COLOR
from dev.project import Project

build_dir = Project.build_dir
deploy_dir = (len(sys.argv) > 1 and sys.argv[1]) or os.path.join("D:/", "Steam", "steamapps", "common", "Elin", "Package", "Mod_Fairy_PCC")

if not os.path.exists(build_dir):
    print(f"{COLOR.RED}Nothing built...{COLOR.RESET}")
    exit(1)

shutil.copytree(build_dir, deploy_dir, dirs_exist_ok=True)

print()
print(f"Completed deploy at {datetime.now().isoformat()}")
