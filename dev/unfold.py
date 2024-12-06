from datetime import datetime

from dev.console import COLOR
from dev.layer_comps import unfold_portraits, unfold_mantles
from dev.project import CopyResult


def _display_result(desc: str, result: dict[str, dict[str, CopyResult]]):
    result_keys = sorted(result.keys())
    for result_key in result_keys:
        columns = result[result_key]
        line = f"{desc}: \"{COLOR.GREEN}{result_key}{COLOR.RESET}\""
        for key, status in columns.items():
            line += f"\t\t{key.upper()} [{status.console()}]"
        print(line)


_display_result("Portrait", unfold_portraits())
print("\n----------\n")
_display_result("Mantle", unfold_mantles())
print("\n----------\n")
print(f"Completed unwrap at {datetime.now().isoformat()}")
