"""
Pointer visualization components for search algorithms.
"""
from manim import *
import sys
sys.path.insert(0, '/home/hg/Desktop/algorthims/Chapter1_BinarySearchVsLinearSearch')

from config.colors import LOW_POINTER, MID_POINTER, HIGH_POINTER, TEXT_PRIMARY
from config.fonts import SMALL_SIZE


class PointerView(VGroup):
    """
    Visual pointer/arrow for indicating position in array.
    """
    
    def __init__(
        self,
        label: str = "",
        color: str = MID_POINTER,
        direction: str = "up",  # "up" or "down"
        scale: float = 1.0
    ):
        super().__init__()
        self.pointer_color = color
        
        # Create arrow
        if direction == "up":
            arrow = Triangle(fill_color=color, fill_opacity=1, stroke_width=0)
            arrow.scale(0.15 * scale)
            arrow.rotate(PI)
        else:
            arrow = Triangle(fill_color=color, fill_opacity=1, stroke_width=0)
            arrow.scale(0.15 * scale)
        
        self.arrow = arrow
        self.add(arrow)
        
        # Create label
        if label:
            lbl = Text(label, font_size=int(SMALL_SIZE * scale), color=color)
            if direction == "up":
                lbl.next_to(arrow, DOWN, buff=0.1 * scale)
            else:
                lbl.next_to(arrow, UP, buff=0.1 * scale)
            self.label = lbl
            self.add(lbl)
    
    def point_to(self, mobject, direction=UP, buff=0.3):
        """Position pointer relative to a mobject."""
        if direction == UP:
            self.next_to(mobject, DOWN, buff=buff)
        else:
            self.next_to(mobject, UP, buff=buff)
        return self


class SearchPointerGroup(VGroup):
    """
    Group of pointers for binary search (low, mid, high).
    """
    
    def __init__(self, scale: float = 1.0):
        super().__init__()
        
        self.low = PointerView("low", LOW_POINTER, "up", scale)
        self.mid = PointerView("mid", MID_POINTER, "up", scale)
        self.high = PointerView("high", HIGH_POINTER, "up", scale)
        
        self.add(self.low, self.mid, self.high)
    
    def position_pointers(self, array_group, low_idx, mid_idx, high_idx, buff=0.4):
        """Position all three pointers below array elements."""
        self.low.next_to(array_group.get_element(low_idx), DOWN, buff=buff)
        self.mid.next_to(array_group.get_element(mid_idx), DOWN, buff=buff + 0.4)
        self.high.next_to(array_group.get_element(high_idx), DOWN, buff=buff)
        return self
