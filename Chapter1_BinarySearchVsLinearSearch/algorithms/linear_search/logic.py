"""
Pure linear search algorithm implementation.
No Manim imports - outputs step-by-step states.
"""
from typing import List, Tuple, Optional
from dataclasses import dataclass


@dataclass
class LinearSearchState:
    """Represents one step in linear search."""
    current_index: int
    target: int
    found: bool
    comparisons: int
    status: str  # "searching", "found", "not_found"


def linear_search_steps(arr: List[int], target: int) -> List[LinearSearchState]:
    """
    Generate step-by-step states for linear search.
    
    Args:
        arr: List of integers to search
        target: Value to find
        
    Returns:
        List of LinearSearchState objects representing each step
    """
    states = []
    comparisons = 0
    
    for i in range(len(arr)):
        comparisons += 1
        
        if arr[i] == target:
            states.append(LinearSearchState(
                current_index=i,
                target=target,
                found=True,
                comparisons=comparisons,
                status="found"
            ))
            return states
        else:
            states.append(LinearSearchState(
                current_index=i,
                target=target,
                found=False,
                comparisons=comparisons,
                status="searching"
            ))
    
    # Target not found
    states.append(LinearSearchState(
        current_index=-1,
        target=target,
        found=False,
        comparisons=comparisons,
        status="not_found"
    ))
    
    return states


def linear_search_worst_case_steps(n: int) -> int:
    """Return number of steps for worst case (element at end or not found)."""
    return n


def linear_search_average_steps(n: int) -> float:
    """Return average number of steps."""
    return n / 2
