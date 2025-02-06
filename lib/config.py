import os
from pathlib import Path

import toml


class Config:
    _cfg = {}

    root = None
    version = None
    package_name = None
    src_dir = None
    build_dir = None
    package_build_dir = None
    dist_dir = None
    install_dir = None
    install_template_dir = None

    def __init__(self):
        self.root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        self._cfg = toml.load(os.path.join(self.root, "pyproject.toml"))

        self.version = self.get("project.version")
        self.package_name = self.get("tool.elin.package-name") or "My_Mod"

        self.src_dir = os.path.join(self.root, "src")
        self.build_dir = os.path.join(self.root, "build")
        self.package_build_dir = os.path.join(self.build_dir, self.package_name)

        self.dist_dir = os.path.join(self.root, "dist")

        self.install_dir = os.path.join(
            os.path.abspath("D:\\Steam\\steamapps\\common\\Elin\\Package")
        )
        self.install_template_dir = os.path.abspath(
            self.get("tool.elin.install-template-dir") or
            os.path.join(Path.home(), "AppData\\LocalLow\\Lafrontier\\Elin\\User\\PCC")
        )

    def get(self, key: str):
        path = key.split(".")
        return self._safe_dict(self._cfg, *path)

    def to_dict(self):
        return self._cfg

    @staticmethod
    def _safe_dict(_dict: dict[str, any], *kwargs: str) -> any or None:
        if _dict is None:
            return None
        try:
            entry = _dict.get(kwargs[0])

            if len(kwargs) > 1:
                return Config._safe_dict(entry, *kwargs[1:])
            else:
                return entry
        except KeyError:
            return None
