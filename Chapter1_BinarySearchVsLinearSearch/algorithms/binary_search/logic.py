"""
Pure binary search algorithm implementation.
No Manim imports - outputs step-by-step states.
"""
from typing import List, Tuple, Optional
from dataclasses import dataclass
import math


@dataclass
class BinarySearchState:
    """Represents one step in binary search."""
    low: int
    mid: int
    high: int
    target: int
    mid_value: int
    comparison: str  # "less", "greater", "equal"
    found: bool
    comparisons: int
    status: str  # "searching", "found", "not_found"


def binary_search_steps(arr: List[int], target: int) -> List[BinarySearchState]:
    """
    Generate step-by-step states for binary search.
    Assumes array is sorted.
    
    Args:
        arr: Sorted list of integers to search
        target: Value to find
        
    Returns:
        List of BinarySearchState objects representing each step
    """
    states = []
    low = 0
    high = len(arr) - 1
    comparisons = 0
    
    while low <= high:
        mid = (low + high) // 2
        mid_value = arr[mid]
        comparisons += 1
        
        if mid_value == target:
            states.append(BinarySearchState(
                low=low,
                mid=mid,
                high=high,
                target=target,
                mid_value=mid_value,
                comparison="equal",
                found=True,
                comparisons=comparisons,
                status="found"
            ))
            return states
        elif mid_value < target:
            states.append(BinarySearchState(
                low=low,
                mid=mid,
                high=high,
                target=target,
                mid_value=mid_value,
                comparison="less",
                found=False,
                comparisons=comparisons,
                status="searching"
            ))
            low = mid + 1
        else:
            states.append(BinarySearchState(
                low=low,
                mid=mid,
                high=high,
                target=target,
                mid_value=mid_value,
                comparison="greater",
                found=False,
                comparisons=comparisons,
                status="searching"
            ))
            high = mid - 1
    
    # Target not found
    states.append(BinarySearchState(
        low=low,
        mid=-1,
        high=high,
        target=target,
        mid_value=-1,
        comparison="none",
        found=False,
        comparisons=comparisons,
        status="not_found"
    ))
    
    return states


def binary_search_max_steps(n: int) -> int:
    """Return maximum number of steps for binary search."""
    if n <= 0:
        return 0
    return math.ceil(math.log2(n)) + 1


def binary_search_steps_for_size(n: int) -> int:
    """Return number of steps needed for array of size n."""
    return math.ceil(math.log2(n + 1))
