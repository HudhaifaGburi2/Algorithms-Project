"""
Pointer visual components for indicating positions in arrays.
R6 compliant: Relative positioning only.
R10 compliant: Reusable components.
"""
from manim import (
    VGroup, Arrow, Triangle, Text,
    UP, DOWN, LEFT, RIGHT, ORIGIN,
    MoveToTarget, Create, FadeIn, FadeOut
)
from config.colors import TEXT_PRIMARY, ACTIVE_COMPARISON, PIVOT
from config.fonts import SMALL_SIZE
from config.animation_constants import DURATION_FAST


class PointerView(VGroup):
    """
    Arrow pointer indicating a position in the array.
    """
    
    def __init__(
        self,
        label: str = "",
        color: str = TEXT_PRIMARY,
        direction: str = "up",
        **kwargs
    ):
        super().__init__(**kwargs)
        self.pointer_color = color
        
        # Create triangle pointer
        self.triangle = Triangle(
            fill_color=color,
            fill_opacity=1.0,
            stroke_width=0
        )
        self.triangle.scale(0.2)
        
        # Rotate based on direction
        if direction == "up":
            self.triangle.rotate(-PI / 2)
        elif direction == "down":
            self.triangle.rotate(PI / 2)
        
        self.add(self.triangle)
        
        # Add label if provided
        if label:
            self.label = Text(
                label,
                font_size=SMALL_SIZE,
                color=color
            )
            if direction == "up":
                self.label.next_to(self.triangle, DOWN, buff=0.1)
            else:
                self.label.next_to(self.triangle, UP, buff=0.1)
            self.add(self.label)
    
    def point_to(self, mobject, direction=DOWN, buff=0.3):
        """Position pointer relative to a mobject."""
        self.next_to(mobject, direction, buff=buff)
        return self
    
    def get_move_animation(self, target_mobject, direction=DOWN, buff=0.3):
        """Get animation to move pointer to target."""
        self.generate_target()
        self.target.next_to(target_mobject, direction, buff=buff)
        return MoveToTarget(self, run_time=DURATION_FAST)


class DualPointerView(VGroup):
    """
    Two pointers for showing comparisons (i and j pointers).
    """
    
    def __init__(
        self,
        left_label: str = "i",
        right_label: str = "j",
        left_color: str = ACTIVE_COMPARISON,
        right_color: str = PIVOT,
        **kwargs
    ):
        super().__init__(**kwargs)
        
        self.left_pointer = PointerView(
            label=left_label,
            color=left_color,
            direction="up"
        )
        self.right_pointer = PointerView(
            label=right_label,
            color=right_color,
            direction="up"
        )
        
        self.add(self.left_pointer, self.right_pointer)
    
    def position_at(self, left_mobject, right_mobject, direction=DOWN, buff=0.3):
        """Position both pointers."""
        self.left_pointer.point_to(left_mobject, direction, buff)
        self.right_pointer.point_to(right_mobject, direction, buff)
        return self
    
    def get_left_move(self, target, direction=DOWN, buff=0.3):
        """Get animation to move left pointer."""
        return self.left_pointer.get_move_animation(target, direction, buff)
    
    def get_right_move(self, target, direction=DOWN, buff=0.3):
        """Get animation to move right pointer."""
        return self.right_pointer.get_move_animation(target, direction, buff)


class PivotMarkerView(VGroup):
    """
    Special marker for pivot element in Quick Sort.
    """
    
    def __init__(self, color: str = PIVOT, **kwargs):
        super().__init__(**kwargs)
        
        self.marker = Text(
            "pivot",
            font_size=SMALL_SIZE,
            color=color
        )
        self.add(self.marker)
    
    def attach_to(self, element, direction=UP, buff=0.4):
        """Attach marker to an element."""
        self.next_to(element, direction, buff=buff)
        return self


# Import PI for rotation
from manim import PI
