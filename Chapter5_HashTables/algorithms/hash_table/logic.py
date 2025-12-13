"""
Pure hash table operations.
No Manim imports.
"""
from typing import Any, Optional, List, Tuple
from dataclasses import dataclass


@dataclass
class HashOperation:
    """Represents a hash table operation."""
    operation: str        # "insert", "lookup", "delete", "collision"
    key: str
    value: Any
    hash_value: int
    index: int
    found: bool
    collision: bool


def simple_hash(key: str, table_size: int = 10) -> int:
    """
    Simple hash function for demonstration.
    Sums ASCII values and mods by table size.
    """
    return sum(ord(c) for c in key.lower()) % table_size


def first_letter_hash(key: str, table_size: int = 26) -> int:
    """Hash based on first letter (for collision demo)."""
    if not key:
        return 0
    return (ord(key[0].lower()) - ord('a')) % table_size


class SimpleHashTable:
    """Hash table implementation for animation states."""
    
    def __init__(self, size: int = 10):
        self.size = size
        self.table = [None] * size
        self.chains = [[] for _ in range(size)]  # For chaining
        self.count = 0
        self.operations = []  # Track operations for animation
    
    def hash(self, key: str) -> int:
        """Compute hash value."""
        return simple_hash(key, self.size)
    
    def insert(self, key: str, value: Any) -> HashOperation:
        """Insert key-value pair."""
        h = self.hash(key)
        idx = h
        collision = self.table[idx] is not None
        
        if collision:
            # Add to chain
            self.chains[idx].append((key, value))
        else:
            self.table[idx] = (key, value)
        
        self.count += 1
        
        op = HashOperation(
            operation="insert",
            key=key,
            value=value,
            hash_value=h,
            index=idx,
            found=True,
            collision=collision
        )
        self.operations.append(op)
        return op
    
    def lookup(self, key: str) -> HashOperation:
        """Look up a key."""
        h = self.hash(key)
        idx = h
        found = False
        value = None
        
        if self.table[idx] is not None:
            stored_key, stored_value = self.table[idx]
            if stored_key == key:
                found = True
                value = stored_value
        
        if not found:
            # Check chain
            for k, v in self.chains[idx]:
                if k == key:
                    found = True
                    value = v
                    break
        
        op = HashOperation(
            operation="lookup",
            key=key,
            value=value,
            hash_value=h,
            index=idx,
            found=found,
            collision=len(self.chains[idx]) > 0
        )
        self.operations.append(op)
        return op
    
    def load_factor(self) -> float:
        """Calculate current load factor."""
        return self.count / self.size
    
    def get_distribution(self) -> List[int]:
        """Get distribution of items per slot."""
        dist = []
        for i in range(self.size):
            count = 0
            if self.table[i] is not None:
                count = 1
            count += len(self.chains[i])
            dist.append(count)
        return dist


# Demo data
GROCERY_ITEMS = [
    ("apple", 0.67),
    ("milk", 1.49),
    ("avocado", 1.49),
    ("banana", 0.59),
    ("bread", 2.99),
]

PHONE_BOOK = [
    ("jenny", "867-5309"),
    ("emergency", "911"),
    ("pizza", "555-1234"),
]

VOTERS = ["tom", "mike", "sarah", "tom"]  # Tom tries twice

# Complexity info
HASH_TABLE_COMPLEXITY = {
    "search_avg": "O(1)",
    "search_worst": "O(n)",
    "insert_avg": "O(1)",
    "insert_worst": "O(n)",
    "delete_avg": "O(1)",
    "delete_worst": "O(n)",
}
