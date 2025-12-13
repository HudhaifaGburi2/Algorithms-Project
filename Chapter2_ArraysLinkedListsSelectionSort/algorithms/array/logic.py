"""
Array operations - complexity analysis.
No Manim imports.
"""
from dataclasses import dataclass


@dataclass
class ArrayOperation:
    """Represents an array operation with its complexity."""
    name: str
    time_complexity: str
    description: str


# Array operation complexities
ARRAY_OPERATIONS = {
    "read": ArrayOperation(
        name="Read (by index)",
        time_complexity="O(1)",
        description="Direct access via index - instant"
    ),
    "insert_end": ArrayOperation(
        name="Insert (at end)",
        time_complexity="O(1)",
        description="Append to end - instant if space available"
    ),
    "insert_start": ArrayOperation(
        name="Insert (at start)",
        time_complexity="O(n)",
        description="Shift all elements right"
    ),
    "insert_middle": ArrayOperation(
        name="Insert (middle)",
        time_complexity="O(n)",
        description="Shift elements after insertion point"
    ),
    "delete_end": ArrayOperation(
        name="Delete (at end)",
        time_complexity="O(1)",
        description="Remove last element - instant"
    ),
    "delete_start": ArrayOperation(
        name="Delete (at start)",
        time_complexity="O(n)",
        description="Shift all elements left"
    ),
    "delete_middle": ArrayOperation(
        name="Delete (middle)",
        time_complexity="O(n)",
        description="Shift elements to fill gap"
    ),
    "search": ArrayOperation(
        name="Search (unsorted)",
        time_complexity="O(n)",
        description="Linear search through all elements"
    ),
    "search_sorted": ArrayOperation(
        name="Search (sorted)",
        time_complexity="O(log n)",
        description="Binary search"
    ),
}


def get_array_complexity_table():
    """Return complexity table for array operations."""
    return [
        ("Read", "O(1)", "Fast - direct index access"),
        ("Insert (end)", "O(1)", "Fast"),
        ("Insert (start/mid)", "O(n)", "Slow - must shift elements"),
        ("Delete (end)", "O(1)", "Fast"),
        ("Delete (start/mid)", "O(n)", "Slow - must shift elements"),
    ]
