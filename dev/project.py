import os
from enum import Enum


class Project:
    root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    portrait_dir = os.path.join(root, "Portrait")
    actor_dir = os.path.join(root, "Actor")
    actor_female_dir = os.path.join(actor_dir, "PCC", "female")


class CopyResult(Enum):
    UNMODIFIED = 0
    CREATED = 1
    UPDATED = 2
    MISSING = 3
