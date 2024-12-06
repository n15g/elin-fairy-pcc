import os
import glob
import re

from dev.project import Project, CopyResult


# Photoshop's layer comps are really useful for outputting linked sprites, but don't let you modify the
# output filename meaningfully. This script unfolds the output layers to match Elin's format.

# Portraits:
# c_<base>_base.png -> c_<base>.png
# c_<base>_overlay.png -> c_<base>-overlay.png

# Mantles:
# pcc_mantle_<base>_base.png -> pcc_mantle_<base>.png
# pcc_mantle_<base>_back.png -> pcc_mantlebk_<base>.png

def unfold_portraits() -> dict[str, dict[str, CopyResult]]:
    portrait_dir = Project.portrait_dir
    portrait_files = _get_files(portrait_dir, "c_*")
    bases = {_get_portrait_base(path) for path in portrait_files}

    portraits = {}
    for base in bases:
        portrait = {}
        psd_path = os.path.join(portrait_dir, f"c_{base}.psd")
        base_path = os.path.join(portrait_dir, f"c_{base}.png")
        base_layer_path = os.path.join(portrait_dir, f"c_{base}_base.png")
        overlay_path = os.path.join(portrait_dir, f"c_{base}-overlay.png")
        overlay_layer_path = os.path.join(portrait_dir, f"c_{base}_overlay.png")

        portrait['psd'] = CopyResult.UNMODIFIED if os.path.exists(psd_path) else CopyResult.MISSING
        portrait['base'] = _rename(base_layer_path, base_path)
        portrait['overlay'] = _rename(overlay_layer_path, overlay_path)
        portraits[base] = portrait

    return portraits


def _get_portrait_base(path: str) -> str:
    basename = os.path.splitext(os.path.basename(path))[0]
    basename = re.sub(r'^c_', '', basename)
    basename = re.sub(r'(_base|_overlay|-overlay)$', '', basename)
    return basename


def unfold_mantles() -> dict[str, dict[str, CopyResult]]:
    mantle_dir = Project.actor_female_dir
    mantle_files = _get_files(mantle_dir, "pcc_mantle*")
    bases = {_get_mantle_base(path) for path in mantle_files}

    mantles = {}
    for base in bases:
        mantle = {}
        psd_path = os.path.join(mantle_dir, f"pcc_mantle_{base}.psd")
        base_path = os.path.join(mantle_dir, f"pcc_mantle_{base}.png")
        base_layer_path = os.path.join(mantle_dir, f"pcc_mantle_{base}_base.png")
        back_path = os.path.join(mantle_dir, f"pcc_mantlebk_{base}.png")
        back_layer_path = os.path.join(mantle_dir, f"pcc_mantle_{base}_back.png")

        mantle['psd'] = CopyResult.UNMODIFIED if os.path.exists(psd_path) else CopyResult.MISSING
        mantle['base'] = _rename(base_layer_path, base_path)
        mantle['overlay'] = _rename(back_layer_path, back_path)
        mantles[base] = mantle

    return mantles


def _get_mantle_base(path: str) -> str:
    basename = os.path.splitext(os.path.basename(path))[0]
    basename = re.sub(r'^(pcc_mantle_|pcc_mantlebk_)', '', basename)
    basename = re.sub(r'(_base|_back)$', '', basename)
    return basename


def _get_files(_path: str, _glob: str) -> list[str]:
    files = glob.glob(os.path.join(_path, f"{_glob}.png"), recursive=True)
    files += glob.glob(os.path.join(_path, f"{_glob}.psd"), recursive=True)
    return files


def _rename(src: str, dst: str) -> CopyResult:
    if os.path.exists(src):
        existed = os.path.exists(dst)
        os.replace(src, dst)
        return CopyResult.UPDATED if existed else CopyResult.CREATED
    else:
        return CopyResult.UNMODIFIED if os.path.exists(dst) else CopyResult.MISSING
