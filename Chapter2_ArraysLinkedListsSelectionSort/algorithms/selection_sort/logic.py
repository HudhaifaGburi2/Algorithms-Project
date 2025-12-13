"""
Pure selection sort algorithm implementation.
No Manim imports - outputs step-by-step states.
"""
from typing import List
from dataclasses import dataclass


@dataclass
class SelectionSortState:
    """Represents one step in selection sort."""
    array: List[int]           # Current array state
    sorted_boundary: int       # Index where sorted portion ends
    current_index: int         # Current position being scanned
    min_index: int             # Index of current minimum
    comparing_index: int       # Index being compared to minimum
    phase: str                 # "scanning", "found_min", "swapping", "done"
    comparisons: int           # Total comparisons so far
    swaps: int                 # Total swaps so far


def selection_sort_steps(arr: List[int]) -> List[SelectionSortState]:
    """
    Generate step-by-step states for selection sort.
    
    Args:
        arr: List of integers to sort
        
    Returns:
        List of SelectionSortState objects representing each step
    """
    states = []
    array = arr.copy()
    n = len(array)
    comparisons = 0
    swaps = 0
    
    for i in range(n - 1):
        min_idx = i
        
        # Initial state for this pass
        states.append(SelectionSortState(
            array=array.copy(),
            sorted_boundary=i,
            current_index=i,
            min_index=min_idx,
            comparing_index=i,
            phase="scanning",
            comparisons=comparisons,
            swaps=swaps
        ))
        
        # Find minimum in unsorted portion
        for j in range(i + 1, n):
            comparisons += 1
            
            # Comparing state
            states.append(SelectionSortState(
                array=array.copy(),
                sorted_boundary=i,
                current_index=i,
                min_index=min_idx,
                comparing_index=j,
                phase="scanning",
                comparisons=comparisons,
                swaps=swaps
            ))
            
            if array[j] < array[min_idx]:
                min_idx = j
                # Found new minimum
                states.append(SelectionSortState(
                    array=array.copy(),
                    sorted_boundary=i,
                    current_index=i,
                    min_index=min_idx,
                    comparing_index=j,
                    phase="found_min",
                    comparisons=comparisons,
                    swaps=swaps
                ))
        
        # Swap if needed
        if min_idx != i:
            array[i], array[min_idx] = array[min_idx], array[i]
            swaps += 1
            
            states.append(SelectionSortState(
                array=array.copy(),
                sorted_boundary=i + 1,
                current_index=i,
                min_index=min_idx,
                comparing_index=-1,
                phase="swapping",
                comparisons=comparisons,
                swaps=swaps
            ))
    
    # Final sorted state
    states.append(SelectionSortState(
        array=array.copy(),
        sorted_boundary=n,
        current_index=-1,
        min_index=-1,
        comparing_index=-1,
        phase="done",
        comparisons=comparisons,
        swaps=swaps
    ))
    
    return states


def selection_sort_complexity(n: int) -> dict:
    """Return complexity information for selection sort."""
    return {
        "comparisons": n * (n - 1) // 2,  # Always n(n-1)/2 comparisons
        "swaps_best": 0,                   # Already sorted
        "swaps_worst": n - 1,              # One swap per pass
        "time_complexity": "O(n²)",
        "space_complexity": "O(1)"
    }
