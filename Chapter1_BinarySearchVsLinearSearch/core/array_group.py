"""
Reusable array group visualization component.
"""
from manim import *
import sys
sys.path.insert(0, '/home/hg/Desktop/algorthims/Chapter1_BinarySearchVsLinearSearch')

from config.colors import UNPROCESSED
from core.array_element import ArrayElementView


class ArrayGroupView(VGroup):
    """
    Visual representation of an array of elements.
    Supports both box and bar display modes.
    """
    
    def __init__(
        self,
        values: list,
        color: str = UNPROCESSED,
        scale: float = 1.0,
        spacing: float = 0.15,
        show_indices: bool = False,
        mode: str = "box"
    ):
        super().__init__()
        self.values = values
        self.elements = []
        
        for i, val in enumerate(values):
            elem = ArrayElementView(
                value=val,
                index=i,
                color=color,
                scale=scale,
                show_index=show_indices,
                mode=mode
            )
            self.elements.append(elem)
            self.add(elem)
        
        self.arrange(RIGHT, buff=spacing * scale)
    
    def get_element(self, index: int) -> ArrayElementView:
        """Get element at index."""
        return self.elements[index]
    
    def highlight_range(self, start: int, end: int, color: str):
        """Return animations to highlight a range of elements."""
        anims = []
        for i in range(start, end + 1):
            anims.append(self.elements[i].get_color_animation(color))
        return AnimationGroup(*anims)
    
    def dim_range(self, start: int, end: int, opacity: float = 0.3):
        """Return animations to dim a range of elements."""
        anims = []
        for i in range(start, end + 1):
            anims.append(self.elements[i].animate.set_opacity(opacity))
        return AnimationGroup(*anims)
