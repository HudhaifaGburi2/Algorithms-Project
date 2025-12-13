"""
Pure Quicksort algorithm implementation.
No Manim imports - outputs step-by-step states.
"""
from typing import List, Tuple
from dataclasses import dataclass


@dataclass
class QuicksortState:
    """Represents one step in quicksort."""
    array: List[int]
    left: int
    right: int
    pivot_idx: int
    pivot_value: int
    less_than: List[int]       # Indices of elements < pivot
    greater_than: List[int]    # Indices of elements > pivot
    phase: str                 # "select_pivot", "partition", "recurse_left", "recurse_right", "done"
    depth: int
    is_base_case: bool


def quicksort_steps(arr: List[int]) -> List[QuicksortState]:
    """
    Generate step-by-step states for quicksort.
    Uses last element as pivot for simplicity.
    """
    states = []
    
    def _quicksort(array, left, right, depth):
        if left >= right:
            # Base case
            states.append(QuicksortState(
                array=array.copy(),
                left=left,
                right=right,
                pivot_idx=-1,
                pivot_value=-1,
                less_than=[],
                greater_than=[],
                phase="base_case",
                depth=depth,
                is_base_case=True
            ))
            return
        
        # Select pivot (last element)
        pivot_idx = right
        pivot_value = array[pivot_idx]
        
        states.append(QuicksortState(
            array=array.copy(),
            left=left,
            right=right,
            pivot_idx=pivot_idx,
            pivot_value=pivot_value,
            less_than=[],
            greater_than=[],
            phase="select_pivot",
            depth=depth,
            is_base_case=False
        ))
        
        # Partition
        less_than = []
        greater_than = []
        
        for i in range(left, right):
            if array[i] < pivot_value:
                less_than.append(i)
            else:
                greater_than.append(i)
        
        states.append(QuicksortState(
            array=array.copy(),
            left=left,
            right=right,
            pivot_idx=pivot_idx,
            pivot_value=pivot_value,
            less_than=less_than,
            greater_than=greater_than,
            phase="partition",
            depth=depth,
            is_base_case=False
        ))
        
        # Perform actual partition (Lomuto scheme)
        i = left - 1
        for j in range(left, right):
            if array[j] < pivot_value:
                i += 1
                array[i], array[j] = array[j], array[i]
        
        # Place pivot in correct position
        array[i + 1], array[right] = array[right], array[i + 1]
        pivot_final_idx = i + 1
        
        # Recurse on left partition
        _quicksort(array, left, pivot_final_idx - 1, depth + 1)
        
        # Recurse on right partition
        _quicksort(array, pivot_final_idx + 1, right, depth + 1)
    
    array = arr.copy()
    _quicksort(array, 0, len(array) - 1, 0)
    
    # Final sorted state
    states.append(QuicksortState(
        array=array,
        left=0,
        right=len(array) - 1,
        pivot_idx=-1,
        pivot_value=-1,
        less_than=[],
        greater_than=[],
        phase="done",
        depth=0,
        is_base_case=False
    ))
    
    return states


def partition_demo(arr: List[int], pivot_idx: int) -> Tuple[List[int], List[int], int]:
    """
    Demonstrate partitioning around a pivot.
    Returns (less_than_elements, greater_than_elements, pivot).
    """
    pivot = arr[pivot_idx]
    less_than = [x for i, x in enumerate(arr) if x < pivot and i != pivot_idx]
    greater_than = [x for i, x in enumerate(arr) if x >= pivot and i != pivot_idx]
    return less_than, greater_than, pivot


def quicksort_depth_analysis(n: int, case: str = "average") -> dict:
    """
    Return depth and complexity information.
    """
    import math
    
    if case == "best" or case == "average":
        depth = math.ceil(math.log2(n)) if n > 0 else 0
        time = "O(n log n)"
    else:  # worst
        depth = n - 1
        time = "O(n²)"
    
    return {
        "depth": depth,
        "time_complexity": time,
        "space_complexity": "O(log n)",  # stack space
        "case": case
    }


# Pre-computed examples for animation
BEST_CASE_EXAMPLE = [4, 2, 6, 1, 3, 5, 7]  # Balanced partitions
WORST_CASE_EXAMPLE = [1, 2, 3, 4, 5, 6, 7]  # Already sorted - worst for last-element pivot
DEMO_ARRAY = [10, 5, 2, 3]  # Small example from prompt
