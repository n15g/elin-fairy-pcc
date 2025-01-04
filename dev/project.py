import filecmp
import os
import shutil
from enum import Enum
from dev.console import COLOR


class CopyResult(Enum):
    UNMODIFIED = 0
    CREATED = 1
    UPDATED = 2
    MISSING = 3

    def console(self):
        match self:
            case CopyResult.UNMODIFIED:
                return f"{COLOR.WHITE}✔{COLOR.RESET}"
            case CopyResult.CREATED:
                return f"{COLOR.GREEN}C{COLOR.RESET}"
            case CopyResult.UPDATED:
                return f"{COLOR.CYAN}U{COLOR.RESET}"
            case CopyResult.MISSING:
                return f"{COLOR.RED}X{COLOR.RESET}"
            case _:
                return f"{COLOR.YELLOW}?{COLOR.RESET}"


class Project:
    root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    portrait_dir = os.path.join(root, "Portrait")
    build_dir = os.path.join(root, "build")
    actor_dir = os.path.join(root, "Actor")
    actor_female_dir = os.path.join(actor_dir, "PCC", "female")
    template_dir = os.path.join(root, "Template")
    aseprite_dir = os.path.join(root, "dev", "aseprite")

    @staticmethod
    def copy(src: str, dst: str) -> CopyResult:
        if not os.path.exists(src):
            return CopyResult.MISSING

        exists = os.path.exists(dst)
        if exists and filecmp.cmp(src, dst):
            return CopyResult.UNMODIFIED

        shutil.copy(src, dst)
        return CopyResult.UPDATED if exists else CopyResult.CREATED
