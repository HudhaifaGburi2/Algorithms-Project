"""
Quick Sort algorithm implementation.
R7 compliant: Pure Python, no Manim imports.
R3 compliant: Deterministic, outputs step-by-step states.
"""
from typing import List, Tuple
from dataclasses import dataclass
from enum import Enum


class QuickSortStepType(Enum):
    """Types of steps in Quick Sort."""
    SELECT_PIVOT = "select_pivot"
    COMPARE = "compare"
    SWAP = "swap"
    PARTITION_COMPLETE = "partition_complete"
    RECURSE_LEFT = "recurse_left"
    RECURSE_RIGHT = "recurse_right"
    SUBARRAY_SORTED = "subarray_sorted"


@dataclass
class QuickSortStep:
    """
    Represents a single step in Quick Sort execution.
    Contains all information needed for visualization.
    """
    step_type: QuickSortStepType
    array_state: List[int]
    pivot_index: int = -1
    compare_indices: Tuple[int, int] = (-1, -1)
    swap_indices: Tuple[int, int] = (-1, -1)
    subarray_range: Tuple[int, int] = (-1, -1)
    i_pointer: int = -1
    j_pointer: int = -1
    depth: int = 0
    description: str = ""


def quick_sort_with_steps(arr: List[int]) -> List[QuickSortStep]:
    """
    Execute Quick Sort and record all steps.
    R3: Deterministic execution.
    
    Args:
        arr: Input array to sort
        
    Returns:
        List of QuickSortStep objects representing each step
    """
    steps = []
    array = arr.copy()
    
    def partition(low: int, high: int, depth: int) -> int:
        """Lomuto partition scheme."""
        pivot = array[high]
        pivot_idx = high
        
        # Record pivot selection
        steps.append(QuickSortStep(
            step_type=QuickSortStepType.SELECT_PIVOT,
            array_state=array.copy(),
            pivot_index=pivot_idx,
            subarray_range=(low, high),
            depth=depth,
            description=f"Select pivot: {pivot}"
        ))
        
        i = low - 1
        
        for j in range(low, high):
            # Record comparison
            steps.append(QuickSortStep(
                step_type=QuickSortStepType.COMPARE,
                array_state=array.copy(),
                pivot_index=pivot_idx,
                compare_indices=(j, pivot_idx),
                subarray_range=(low, high),
                i_pointer=i,
                j_pointer=j,
                depth=depth,
                description=f"Compare {array[j]} with pivot {pivot}"
            ))
            
            if array[j] <= pivot:
                i += 1
                if i != j:
                    # Record swap
                    steps.append(QuickSortStep(
                        step_type=QuickSortStepType.SWAP,
                        array_state=array.copy(),
                        pivot_index=pivot_idx,
                        swap_indices=(i, j),
                        subarray_range=(low, high),
                        i_pointer=i,
                        j_pointer=j,
                        depth=depth,
                        description=f"Swap {array[i]} and {array[j]}"
                    ))
                    array[i], array[j] = array[j], array[i]
        
        # Place pivot in correct position
        if i + 1 != high:
            steps.append(QuickSortStep(
                step_type=QuickSortStepType.SWAP,
                array_state=array.copy(),
                pivot_index=pivot_idx,
                swap_indices=(i + 1, high),
                subarray_range=(low, high),
                depth=depth,
                description=f"Place pivot {pivot} at position {i + 1}"
            ))
            array[i + 1], array[high] = array[high], array[i + 1]
        
        # Record partition complete
        steps.append(QuickSortStep(
            step_type=QuickSortStepType.PARTITION_COMPLETE,
            array_state=array.copy(),
            pivot_index=i + 1,
            subarray_range=(low, high),
            depth=depth,
            description=f"Pivot {array[i + 1]} in final position"
        ))
        
        return i + 1
    
    def quicksort(low: int, high: int, depth: int):
        """Recursive Quick Sort."""
        if low < high:
            pivot_pos = partition(low, high, depth)
            
            # Record left recursion
            if low < pivot_pos - 1:
                steps.append(QuickSortStep(
                    step_type=QuickSortStepType.RECURSE_LEFT,
                    array_state=array.copy(),
                    pivot_index=pivot_pos,
                    subarray_range=(low, pivot_pos - 1),
                    depth=depth + 1,
                    description=f"Recurse left: [{low}, {pivot_pos - 1}]"
                ))
                quicksort(low, pivot_pos - 1, depth + 1)
            elif low == pivot_pos - 1:
                steps.append(QuickSortStep(
                    step_type=QuickSortStepType.SUBARRAY_SORTED,
                    array_state=array.copy(),
                    subarray_range=(low, low),
                    depth=depth + 1,
                    description=f"Single element sorted: {array[low]}"
                ))
            
            # Record right recursion
            if pivot_pos + 1 < high:
                steps.append(QuickSortStep(
                    step_type=QuickSortStepType.RECURSE_RIGHT,
                    array_state=array.copy(),
                    pivot_index=pivot_pos,
                    subarray_range=(pivot_pos + 1, high),
                    depth=depth + 1,
                    description=f"Recurse right: [{pivot_pos + 1}, {high}]"
                ))
                quicksort(pivot_pos + 1, high, depth + 1)
            elif pivot_pos + 1 == high:
                steps.append(QuickSortStep(
                    step_type=QuickSortStepType.SUBARRAY_SORTED,
                    array_state=array.copy(),
                    subarray_range=(high, high),
                    depth=depth + 1,
                    description=f"Single element sorted: {array[high]}"
                ))
    
    quicksort(0, len(array) - 1, 0)
    
    return steps


def get_quick_sort_complexity_info() -> dict:
    """Return complexity information for Quick Sort."""
    return {
        "best_time": "O(n log n)",
        "average_time": "O(n log n)",
        "worst_time": "O(n²)",
        "space": "O(log n)",
        "stable": False,
        "in_place": True
    }
