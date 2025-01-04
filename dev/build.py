import os
import shutil
from datetime import datetime

from dev.console import COLOR
from dev.project import Project
import glob

def tree_copy(pathspec: str, new_ext: str | None = None):
    files = glob.glob(pathspec, recursive=True)
    for file in files:
        rel_path = os.path.relpath(file, Project.root)

        dst_folder = os.path.join(Project.build_dir, os.path.dirname(rel_path))
        os.makedirs(dst_folder, exist_ok=True)

        src_path = os.path.join(Project.root, rel_path)
        if new_ext is not None:
            dst_path = os.path.join(Project.build_dir, os.path.splitext(rel_path)[0] + new_ext)
        else:
            dst_path = os.path.join(Project.build_dir, rel_path)

        shutil.copy(src_path, dst_path)
        print(f"{COLOR.GREEN}[{rel_path}]{COLOR.RESET}")

build_dir = Project.build_dir

if os.path.exists(build_dir):
    print(f"{COLOR.YELLOW}Cleaning existing build...{COLOR.RESET}")
    shutil.rmtree(build_dir)
os.makedirs(build_dir, exist_ok=True)


root_files = ["LICENSE", "package.xml", "preview.jpg", "README.md"]
for root_file in root_files:
    shutil.copy(os.path.join(Project.root, root_file), build_dir)
    print(f"{COLOR.GREEN}[{root_file}]{COLOR.RESET}")


tree_copy(os.path.join(Project.actor_dir, "**", "*.png"))
tree_copy(os.path.join(Project.portrait_dir, "**", "*.png"))
tree_copy(os.path.join(Project.template_dir, "**", "*.json"), ".txt")

print()
print(f"Completed build at {datetime.now().isoformat()}")
