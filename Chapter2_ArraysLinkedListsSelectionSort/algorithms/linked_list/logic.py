"""
Linked list operations - complexity analysis.
No Manim imports.
"""
from dataclasses import dataclass


@dataclass 
class LinkedListOperation:
    """Represents a linked list operation with its complexity."""
    name: str
    time_complexity: str
    description: str


# Linked list operation complexities
LINKED_LIST_OPERATIONS = {
    "read": LinkedListOperation(
        name="Read (by index)",
        time_complexity="O(n)",
        description="Must traverse from head to index"
    ),
    "read_head": LinkedListOperation(
        name="Read (head)",
        time_complexity="O(1)",
        description="Direct access to first element"
    ),
    "insert_start": LinkedListOperation(
        name="Insert (at start)",
        time_complexity="O(1)",
        description="Update head pointer - instant"
    ),
    "insert_end": LinkedListOperation(
        name="Insert (at end)",
        time_complexity="O(n)",
        description="Traverse to end, then insert"
    ),
    "insert_middle": LinkedListOperation(
        name="Insert (middle)",
        time_complexity="O(n)",
        description="Traverse to position, then O(1) insert"
    ),
    "delete_start": LinkedListOperation(
        name="Delete (at start)",
        time_complexity="O(1)",
        description="Update head pointer - instant"
    ),
    "delete_end": LinkedListOperation(
        name="Delete (at end)",
        time_complexity="O(n)",
        description="Traverse to end"
    ),
    "delete_middle": LinkedListOperation(
        name="Delete (middle)",
        time_complexity="O(n)",
        description="Traverse to position, then O(1) delete"
    ),
    "search": LinkedListOperation(
        name="Search",
        time_complexity="O(n)",
        description="Linear search through nodes"
    ),
}


def get_linked_list_complexity_table():
    """Return complexity table for linked list operations."""
    return [
        ("Read", "O(n)", "Slow - must traverse"),
        ("Insert (start)", "O(1)", "Fast - update head"),
        ("Insert (end/mid)", "O(n)", "Traverse first"),
        ("Delete (start)", "O(1)", "Fast - update head"),
        ("Delete (end/mid)", "O(n)", "Traverse first"),
    ]


def get_comparison_table():
    """Return comparison table: Array vs Linked List."""
    return [
        ("Operation", "Array", "Linked List"),
        ("Read", "O(1) Fast", "O(n) Slow"),
        ("Insert (start)", "O(n) Slow", "O(1) Fast"),
        ("Insert (end)", "O(1) Fast", "O(n) Slow"),
        ("Delete (start)", "O(n) Slow", "O(1) Fast"),
        ("Memory", "Contiguous", "Scattered"),
    ]
