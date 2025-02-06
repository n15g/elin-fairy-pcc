import filecmp
import glob
import os
import shutil
from enum import Enum

import chevron

from lib.config import Config
from lib.console import COLOR

config = Config()


class CopyResult(Enum):
    UNMODIFIED = 0
    CREATED = 1
    UPDATED = 2
    MISSING = 3

    def print(self) -> str:
        match self:
            case CopyResult.UNMODIFIED:
                return f"{COLOR.WHITE}✔{COLOR.RESET}"
            case CopyResult.CREATED:
                return f"{COLOR.GREEN}C{COLOR.RESET}"
            case CopyResult.UPDATED:
                return f"{COLOR.CYAN}U{COLOR.RESET}"
            case CopyResult.MISSING:
                return f"{COLOR.WHITE}?{COLOR.RESET}"
            case _:
                return f"{COLOR.YELLOW}?{COLOR.RESET}"


def mkdir(path: str) -> None:
    if not os.path.exists(path):
        os.makedirs(path, exist_ok=True)
        print(f"[{COLOR.GREEN}C{COLOR.RESET}] {path}")


def rmdir(path: str) -> None:
    if os.path.exists(path):
        print(f"[{COLOR.WHITE}D{COLOR.RESET}] {path}")
        shutil.rmtree(path)


def copy_file(src: str, dst: str) -> None:
    dst_path = os.path.join(dst, os.path.basename(src)) if os.path.isdir(dst) else dst

    if not os.path.exists(src):
        print(f"[{CopyResult.MISSING.print()}] {dst_path}")
        return

    exists = os.path.exists(dst_path)
    if exists and filecmp.cmp(src, dst_path):
        print(f"[{CopyResult.UNMODIFIED.print()}] {dst_path}")
        return

    shutil.copy(src, dst_path)
    print(f"[{(CopyResult.UPDATED if exists else CopyResult.CREATED).print()}] {dst_path}")


def rename_file(src: str, dst: str) -> None:
    if os.path.exists(src):
        existed = os.path.exists(dst)
        os.replace(src, dst)
        print(f"[{CopyResult.UPDATED.print() if existed else CopyResult.CREATED.print()}] {dst}")
    else:
        print(f"[{CopyResult.UNMODIFIED.print() if os.path.exists(dst) else CopyResult.MISSING.print()}] {dst}")


def copy_template(src: str, dst: str) -> None:
    dst_path = os.path.join(dst, os.path.basename(src)) if os.path.isdir(dst) else dst

    if not os.path.exists(src):
        print(f"[{CopyResult.MISSING.print()}] {dst_path}")
        return

    with open(src, 'r') as src_file:
        exists = os.path.exists(dst_path)

        existing_content = None
        if exists:
            with open(dst_path, 'r') as dst_file:
                existing_content = dst_file.read()

        content = chevron.render(src_file, config.to_dict())
        if content == existing_content:
            print(f"[{CopyResult.UNMODIFIED.print()}] {dst_path}")
            return

        with open(dst_path, 'w') as dst_file:
            dst_file.write(content)
            print(f"[{(CopyResult.UPDATED if exists else CopyResult.CREATED).print()}] {dst_path}")


def glob_copy(src: str, _glob: str, dst: str, new_ext: str | None = None) -> None:
    files = glob.glob(os.path.join(config.root, src, _glob), recursive=True)
    for file in files:
        rel_path = os.path.relpath(file, src)

        dst_folder = os.path.join(dst, os.path.dirname(rel_path))
        os.makedirs(dst_folder, exist_ok=True)

        src_path = os.path.join(src, rel_path)
        if new_ext is not None:
            dst_path = os.path.join(dst, os.path.splitext(rel_path)[0] + new_ext)
        else:
            dst_path = os.path.join(dst, rel_path)

        copy_file(src_path, dst_path)


def mkarchive(src: str, dst: str) -> None:
    print(dst, "zip", src)
    shutil.make_archive(dst, "zip", src)
    print(f"[{COLOR.GREEN}C{COLOR.RESET}] {dst}.zip")


def rename_layer_comps(tgt_dir: str) -> None:
    files = glob.glob(os.path.join(tgt_dir, "*.png"))
    for file in files:
        if file.endswith("_base.png"):
            rename_file(file, file.replace("_base.png", ".png"))

        if file.endswith("_overlay.png"):
            rename_file(file, file.replace("_overlay.png", "-overlay.png"))
