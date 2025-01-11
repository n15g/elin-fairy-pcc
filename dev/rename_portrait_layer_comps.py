import os
from datetime import datetime

from dev.console import COLOR
from dev.project import CopyResult, Project
import glob

def _rename(src: str, dst: str) -> CopyResult:
    if os.path.exists(src):
        existed = os.path.exists(dst)
        os.replace(src, dst)
        return CopyResult.UPDATED if existed else CopyResult.CREATED
    else:
        return CopyResult.UNMODIFIED if os.path.exists(dst) else CopyResult.MISSING

files = glob.glob(os.path.join(Project.portrait_dir, "*.png"))
for file in files:
    if file.endswith("_base.png"):
        result = _rename(file, file.replace("_base.png", ".png"))
        print(f"\"{COLOR.GREEN}{file}{COLOR.RESET}\"\t\t [{result.console()}]")

    if file.endswith("_overlay.png"):
        result = _rename(file, file.replace("_overlay.png", "-overlay.png"))
        print(f"\"{COLOR.GREEN}{file}{COLOR.RESET}\"\t\t [{result.console()}]")

print()
print(f"{COLOR.GREEN}Completed rename at {COLOR.CYAN}{datetime.now().isoformat()}{COLOR.RESET}")
