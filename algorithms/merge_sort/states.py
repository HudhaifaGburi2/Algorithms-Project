"""
Merge Sort animation states.
R7 compliant: Converts algorithm steps to animation-ready states.
No rendering logic - only state preparation.
"""
from typing import List, Dict, Any, Optional
from dataclasses import dataclass
from .logic import MergeSortStep, MergeSortStepType


@dataclass
class MergeSortAnimationState:
    """
    Animation-ready state for Merge Sort visualization.
    Contains color mappings and position information.
    """
    array_values: List[int]
    element_colors: Dict[int, str]  # index -> color name
    left_subarray: Optional[List[int]]
    right_subarray: Optional[List[int]]
    merged_result: Optional[List[int]]
    active_range: tuple
    depth: int
    action_type: str
    compare_values: tuple = None
    selected_value: int = None
    temp_storage_active: bool = False
    
    def get_highlighted_indices(self) -> List[int]:
        """Get indices that should be highlighted."""
        return list(self.element_colors.keys())


class MergeSortStateConverter:
    """
    Converts MergeSortStep objects to animation states.
    """
    
    # Color semantic names (actual colors resolved in visualization)
    COLOR_UNPROCESSED = "unprocessed"
    COLOR_COMPARING = "comparing"
    COLOR_SORTED = "sorted"
    COLOR_TEMP_STORAGE = "temp_storage"
    COLOR_SELECTED = "selected"
    COLOR_LEFT_SUBARRAY = "left_subarray"
    COLOR_RIGHT_SUBARRAY = "right_subarray"
    
    @classmethod
    def convert_step(cls, step: MergeSortStep) -> MergeSortAnimationState:
        """Convert a single algorithm step to animation state."""
        colors = {}
        temp_active = False
        
        low, high = step.subarray_range
        
        # Apply step-specific coloring
        if step.step_type == MergeSortStepType.SPLIT:
            # Color left and right subarrays differently
            left_low, left_high = step.left_range
            right_low, right_high = step.right_range
            
            for i in range(left_low, left_high + 1):
                colors[i] = cls.COLOR_LEFT_SUBARRAY
            for i in range(right_low, right_high + 1):
                colors[i] = cls.COLOR_RIGHT_SUBARRAY
                
        elif step.step_type == MergeSortStepType.SINGLE_ELEMENT:
            colors[step.subarray_range[0]] = cls.COLOR_SORTED
            
        elif step.step_type == MergeSortStepType.COMPARE:
            temp_active = True
            # Elements being compared
            
        elif step.step_type in [MergeSortStepType.SELECT_LEFT, MergeSortStepType.SELECT_RIGHT]:
            temp_active = True
            
        elif step.step_type == MergeSortStepType.COPY_REMAINING:
            temp_active = True
            
        elif step.step_type == MergeSortStepType.MERGE_COMPLETE:
            for i in range(low, high + 1):
                colors[i] = cls.COLOR_SORTED
        
        return MergeSortAnimationState(
            array_values=step.array_state,
            element_colors=colors,
            left_subarray=step.left_subarray,
            right_subarray=step.right_subarray,
            merged_result=step.merged_result,
            active_range=step.subarray_range,
            depth=step.depth,
            action_type=step.step_type.value,
            compare_values=step.compare_values,
            selected_value=step.selected_value,
            temp_storage_active=temp_active
        )
    
    @classmethod
    def convert_all_steps(cls, steps: List[MergeSortStep]) -> List[MergeSortAnimationState]:
        """Convert all algorithm steps to animation states."""
        return [cls.convert_step(step) for step in steps]


def get_predefined_merge_sort_states(array: List[int]) -> List[MergeSortAnimationState]:
    """
    Get predefined animation states for Merge Sort.
    R3 compliant: Deterministic output.
    """
    from .logic import merge_sort_with_steps
    
    steps = merge_sort_with_steps(array)
    return MergeSortStateConverter.convert_all_steps(steps)
