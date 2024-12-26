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


portraits_result = unfold_portraits()
mantles_result = unfold_mantles()

_display_result("Portrait", portraits_result)
print("\n----------\n")

# Moved to Aseprite
# _display_result("Mantle", mantles_result)
# print("\n----------\n")
print(f"Completed unwrap at {datetime.now().isoformat()}")
