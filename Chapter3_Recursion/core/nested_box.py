"""
Nested box visualization for recursion metaphor.
"""
from manim import *
import sys
sys.path.insert(0, '/home/hg/Desktop/algorthims/Chapter3_Recursion')

from config.colors import BOX_OUTER, BOX_INNER, KEY_FOUND, TEXT_PRIMARY
from config.fonts import LABEL_SIZE, SMALL_SIZE


class NestedBoxView(VGroup):
    """
    Visual representation of nested boxes (recursion metaphor).
    """
    
    def __init__(
        self,
        size: float = 1.2,
        color: str = BOX_OUTER,
        label: str = "",
        has_key: bool = False
    ):
        super().__init__()
        self.box_size = size
        self.box_color = color
        self.has_key = has_key
        
        # Main box
        self.box = RoundedRectangle(
            width=size,
            height=size,
            corner_radius=0.1,
            fill_color=color,
            fill_opacity=0.7,
            stroke_color=TEXT_PRIMARY,
            stroke_width=2
        )
        
        self.add(self.box)
        
        # Label
        if label:
            self.label = Text(label, font_size=SMALL_SIZE, color=TEXT_PRIMARY)
            self.label.move_to(self.box.get_center())
            self.add(self.label)
        
        # Key indicator
        if has_key:
            self.key = Text("🔑", font_size=int(LABEL_SIZE * 0.8))
            self.key.move_to(self.box.get_center())
            self.add(self.key)
    
    def set_color(self, color):
        """Change box color."""
        self.box_color = color
        self.box.set_fill(color)
        self.box.set_stroke(color)
    
    def highlight(self, color):
        """Return animation to highlight box."""
        return self.box.animate.set_fill(color).set_stroke(color)


class BoxSearchView(VGroup):
    """
    Visual representation of nested boxes for search metaphor.
    Grandma's attic boxes containing more boxes or a key.
    """
    
    def __init__(self, depth: int = 3):
        super().__init__()
        self.boxes = []
        self.depth = depth
        
        # Create nested boxes visually
        sizes = [2.5, 1.8, 1.2, 0.8, 0.5]
        colors = [BOX_OUTER, BOX_INNER, "#818CF8", "#A78BFA", KEY_FOUND]
        
        for i in range(min(depth, len(sizes))):
            has_key = (i == depth - 1)
            box = NestedBoxView(
                size=sizes[i],
                color=colors[i],
                has_key=has_key
            )
            self.boxes.append(box)
            self.add(box)
