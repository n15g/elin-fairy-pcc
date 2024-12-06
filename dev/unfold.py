from dev.console import COLOR
from dev.layer_comps import unfold_portraits, unfold_mantles
from dev.project import CopyResult


def _display_result(desc: str, result: dict[str, dict[str, CopyResult]]):
    result_keys = sorted(result.keys())
    for result_key in result_keys:
        columns = result[result_key]
        line = f"{desc}: \"{COLOR.GREEN}{result_key}{COLOR.RESET}\""
        for key, status in columns.items():
            line += f"\t\t{key.upper()} [{_display_status(status)}]"
        print(line)


def _display_status(cr: CopyResult):
    match cr:
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


_display_result("Portrait", unfold_portraits())
print("\n----------\n")
_display_result("Mantle", unfold_mantles())
