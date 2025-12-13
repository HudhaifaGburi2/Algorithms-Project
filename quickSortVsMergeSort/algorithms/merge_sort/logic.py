"""
Merge Sort algorithm implementation.
R7 compliant: Pure Python, no Manim imports.
R3 compliant: Deterministic, outputs step-by-step states.
"""
from typing import List, Tuple
from dataclasses import dataclass
from enum import Enum


class MergeSortStepType(Enum):
    """Types of steps in Merge Sort."""
    SPLIT = "split"
    SINGLE_ELEMENT = "single_element"
    COMPARE = "compare"
    SELECT_LEFT = "select_left"
    SELECT_RIGHT = "select_right"
    MERGE_COMPLETE = "merge_complete"
    COPY_REMAINING = "copy_remaining"


@dataclass
class MergeSortStep:
    """
    Represents a single step in Merge Sort execution.
    Contains all information needed for visualization.
    """
    step_type: MergeSortStepType
    array_state: List[int]
    left_subarray: List[int] = None
    right_subarray: List[int] = None
    merged_result: List[int] = None
    compare_values: Tuple[int, int] = None
    selected_value: int = None
    subarray_range: Tuple[int, int] = (-1, -1)
    left_range: Tuple[int, int] = (-1, -1)
    right_range: Tuple[int, int] = (-1, -1)
    depth: int = 0
    merge_index: int = -1
    description: str = ""


def merge_sort_with_steps(arr: List[int]) -> List[MergeSortStep]:
    """
    Execute Merge Sort and record all steps.
    R3: Deterministic execution.
    
    Args:
        arr: Input array to sort
        
    Returns:
        List of MergeSortStep objects representing each step
    """
    steps = []
    array = arr.copy()
    
    def merge_sort(arr_slice: List[int], start_idx: int, depth: int) -> List[int]:
        """Recursive Merge Sort with step recording."""
        n = len(arr_slice)
        
        if n <= 1:
            if n == 1:
                steps.append(MergeSortStep(
                    step_type=MergeSortStepType.SINGLE_ELEMENT,
                    array_state=array.copy(),
                    left_subarray=arr_slice.copy(),
                    subarray_range=(start_idx, start_idx),
                    depth=depth,
                    description=f"Single element: {arr_slice[0]}"
                ))
            return arr_slice
        
        mid = n // 2
        
        # Record split
        steps.append(MergeSortStep(
            step_type=MergeSortStepType.SPLIT,
            array_state=array.copy(),
            left_subarray=arr_slice[:mid],
            right_subarray=arr_slice[mid:],
            subarray_range=(start_idx, start_idx + n - 1),
            left_range=(start_idx, start_idx + mid - 1),
            right_range=(start_idx + mid, start_idx + n - 1),
            depth=depth,
            description=f"Split into {arr_slice[:mid]} and {arr_slice[mid:]}"
        ))
        
        # Recursively sort
        left = merge_sort(arr_slice[:mid], start_idx, depth + 1)
        right = merge_sort(arr_slice[mid:], start_idx + mid, depth + 1)
        
        # Merge
        return merge(left, right, start_idx, depth)
    
    def merge(left: List[int], right: List[int], start_idx: int, depth: int) -> List[int]:
        """Merge two sorted arrays with step recording."""
        result = []
        i = j = 0
        merge_idx = 0
        
        while i < len(left) and j < len(right):
            # Record comparison
            steps.append(MergeSortStep(
                step_type=MergeSortStepType.COMPARE,
                array_state=array.copy(),
                left_subarray=left.copy(),
                right_subarray=right.copy(),
                merged_result=result.copy(),
                compare_values=(left[i], right[j]),
                subarray_range=(start_idx, start_idx + len(left) + len(right) - 1),
                depth=depth,
                merge_index=merge_idx,
                description=f"Compare {left[i]} and {right[j]}"
            ))
            
            if left[i] <= right[j]:
                # Record selection from left
                steps.append(MergeSortStep(
                    step_type=MergeSortStepType.SELECT_LEFT,
                    array_state=array.copy(),
                    left_subarray=left.copy(),
                    right_subarray=right.copy(),
                    merged_result=result.copy() + [left[i]],
                    selected_value=left[i],
                    subarray_range=(start_idx, start_idx + len(left) + len(right) - 1),
                    depth=depth,
                    merge_index=merge_idx,
                    description=f"Select {left[i]} from left"
                ))
                result.append(left[i])
                i += 1
            else:
                # Record selection from right
                steps.append(MergeSortStep(
                    step_type=MergeSortStepType.SELECT_RIGHT,
                    array_state=array.copy(),
                    left_subarray=left.copy(),
                    right_subarray=right.copy(),
                    merged_result=result.copy() + [right[j]],
                    selected_value=right[j],
                    subarray_range=(start_idx, start_idx + len(left) + len(right) - 1),
                    depth=depth,
                    merge_index=merge_idx,
                    description=f"Select {right[j]} from right"
                ))
                result.append(right[j])
                j += 1
            
            merge_idx += 1
        
        # Copy remaining elements
        remaining = left[i:] + right[j:]
        if remaining:
            steps.append(MergeSortStep(
                step_type=MergeSortStepType.COPY_REMAINING,
                array_state=array.copy(),
                left_subarray=left.copy(),
                right_subarray=right.copy(),
                merged_result=result.copy() + remaining,
                subarray_range=(start_idx, start_idx + len(left) + len(right) - 1),
                depth=depth,
                description=f"Copy remaining: {remaining}"
            ))
        
        result.extend(remaining)
        
        # Update main array
        for k, val in enumerate(result):
            array[start_idx + k] = val
        
        # Record merge complete
        steps.append(MergeSortStep(
            step_type=MergeSortStepType.MERGE_COMPLETE,
            array_state=array.copy(),
            merged_result=result.copy(),
            subarray_range=(start_idx, start_idx + len(result) - 1),
            depth=depth,
            description=f"Merged: {result}"
        ))
        
        return result
    
    merge_sort(array, 0, 0)
    
    return steps


def get_merge_sort_complexity_info() -> dict:
    """Return complexity information for Merge Sort."""
    return {
        "best_time": "O(n log n)",
        "average_time": "O(n log n)",
        "worst_time": "O(n log n)",
        "space": "O(n)",
        "stable": True,
        "in_place": False
    }
