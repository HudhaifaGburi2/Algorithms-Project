"""
Reusable array element visualization component.
"""
from manim import *
import sys
sys.path.insert(0, '/home/hg/Desktop/algorthims/Chapter1_BinarySearchVsLinearSearch')

from config.colors import UNPROCESSED, TEXT_PRIMARY
from config.fonts import LABEL_SIZE


class ArrayElementView(VGroup):
    """
    Visual representation of a single array element.
    Can display as bar or box with value label.
    """
    
    def __init__(
        self,
        value: int,
        index: int = 0,
        color: str = UNPROCESSED,
        scale: float = 1.0,
        show_index: bool = False,
        mode: str = "box"  # "box" or "bar"
    ):
        super().__init__()
        self.value = value
        self.index = index
        self.element_color = color
        
        if mode == "box":
            self._create_box(value, color, scale, show_index)
        else:
            self._create_bar(value, color, scale, show_index)
    
    def _create_box(self, value, color, scale, show_index):
        """Create box-style element."""
        box = RoundedRectangle(
            width=0.8 * scale,
            height=0.8 * scale,
            corner_radius=0.08 * scale,
            fill_color=color,
            fill_opacity=0.9,
            stroke_color=color,
            stroke_width=2
        )
        
        label = Text(str(value), font_size=int(LABEL_SIZE * scale), color=TEXT_PRIMARY)
        label.move_to(box.get_center())
        
        self.box = box
        self.label = label
        self.add(box, label)
        
        if show_index:
            idx_label = Text(str(self.index), font_size=int(14 * scale), color=TEXT_PRIMARY)
            idx_label.next_to(box, DOWN, buff=0.1 * scale)
            self.idx_label = idx_label
            self.add(idx_label)
    
    def _create_bar(self, value, color, scale, show_index):
        """Create bar-style element (height proportional to value)."""
        bar = RoundedRectangle(
            width=0.6 * scale,
            height=value * 0.3 * scale,
            corner_radius=0.05 * scale,
            fill_color=color,
            fill_opacity=0.9,
            stroke_color=color,
            stroke_width=2
        )
        
        label = Text(str(value), font_size=int(16 * scale), color=TEXT_PRIMARY)
        label.move_to(bar.get_center())
        
        self.box = bar
        self.label = label
        self.add(bar, label)
        
        if show_index:
            idx_label = Text(str(self.index), font_size=int(14 * scale), color=TEXT_PRIMARY)
            idx_label.next_to(bar, DOWN, buff=0.1 * scale)
            self.idx_label = idx_label
            self.add(idx_label)
    
    def set_color(self, color):
        """Change element color."""
        self.element_color = color
        self.box.set_fill(color)
        self.box.set_stroke(color)
    
    def get_color_animation(self, color, run_time=0.5):
        """Return animation for color change."""
        return AnimationGroup(
            self.box.animate.set_fill(color).set_stroke(color),
            run_time=run_time
        )
