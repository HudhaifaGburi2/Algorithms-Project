"""
Quick Sort animation states.
R7 compliant: Converts algorithm steps to animation-ready states.
No rendering logic - only state preparation.
"""
from typing import List, Dict, Any
from dataclasses import dataclass
from .logic import QuickSortStep, QuickSortStepType


@dataclass
class QuickSortAnimationState:
    """
    Animation-ready state for Quick Sort visualization.
    Contains color mappings and position information.
    """
    array_values: List[int]
    element_colors: Dict[int, str]  # index -> color name
    pivot_index: int
    active_range: tuple
    pointer_positions: Dict[str, int]  # pointer_name -> index
    depth: int
    action_type: str
    swap_pair: tuple = None
    
    def get_highlighted_indices(self) -> List[int]:
        """Get indices that should be highlighted."""
        return list(self.element_colors.keys())


class QuickSortStateConverter:
    """
    Converts QuickSortStep objects to animation states.
    """
    
    # Color semantic names (actual colors resolved in visualization)
    COLOR_UNPROCESSED = "unprocessed"
    COLOR_PIVOT = "pivot"
    COLOR_COMPARING = "comparing"
    COLOR_SORTED = "sorted"
    COLOR_SWAPPING = "swapping"
    
    @classmethod
    def convert_step(cls, step: QuickSortStep) -> QuickSortAnimationState:
        """Convert a single algorithm step to animation state."""
        colors = {}
        pointers = {}
        swap_pair = None
        
        low, high = step.subarray_range
        
        # Mark elements outside active range as sorted or unprocessed
        for i in range(len(step.array_state)):
            if low <= i <= high:
                colors[i] = cls.COLOR_UNPROCESSED
            # Elements before range might be sorted
        
        # Apply step-specific coloring
        if step.step_type == QuickSortStepType.SELECT_PIVOT:
            colors[step.pivot_index] = cls.COLOR_PIVOT
            
        elif step.step_type == QuickSortStepType.COMPARE:
            colors[step.pivot_index] = cls.COLOR_PIVOT
            j_idx = step.compare_indices[0]
            colors[j_idx] = cls.COLOR_COMPARING
            pointers["i"] = step.i_pointer
            pointers["j"] = step.j_pointer
            
        elif step.step_type == QuickSortStepType.SWAP:
            colors[step.pivot_index] = cls.COLOR_PIVOT
            i_idx, j_idx = step.swap_indices
            colors[i_idx] = cls.COLOR_SWAPPING
            colors[j_idx] = cls.COLOR_SWAPPING
            swap_pair = step.swap_indices
            pointers["i"] = step.i_pointer
            pointers["j"] = step.j_pointer
            
        elif step.step_type == QuickSortStepType.PARTITION_COMPLETE:
            colors[step.pivot_index] = cls.COLOR_SORTED
            
        elif step.step_type == QuickSortStepType.SUBARRAY_SORTED:
            idx = step.subarray_range[0]
            colors[idx] = cls.COLOR_SORTED
        
        return QuickSortAnimationState(
            array_values=step.array_state,
            element_colors=colors,
            pivot_index=step.pivot_index,
            active_range=step.subarray_range,
            pointer_positions=pointers,
            depth=step.depth,
            action_type=step.step_type.value,
            swap_pair=swap_pair
        )
    
    @classmethod
    def convert_all_steps(cls, steps: List[QuickSortStep]) -> List[QuickSortAnimationState]:
        """Convert all algorithm steps to animation states."""
        return [cls.convert_step(step) for step in steps]


def get_predefined_quick_sort_states(array: List[int]) -> List[QuickSortAnimationState]:
    """
    Get predefined animation states for Quick Sort.
    R3 compliant: Deterministic output.
    """
    from .logic import quick_sort_with_steps
    
    steps = quick_sort_with_steps(array)
    return QuickSortStateConverter.convert_all_steps(steps)
