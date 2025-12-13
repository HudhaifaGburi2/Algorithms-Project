"""
Recursion tree visualization for divide & conquer.
"""
from manim import *
import sys
sys.path.insert(0, '/home/hg/Desktop/algorthims/Chapter4_DivideConquerQuicksort')

from config.colors import STACK_FRAME, STACK_ACTIVE, TEXT_PRIMARY, PIVOT
from config.fonts import SMALL_SIZE, TINY_SIZE


class TreeNodeView(VGroup):
    """Single node in recursion tree."""
    
    def __init__(self, label, color=STACK_FRAME, radius=0.4):
        super().__init__()
        self.node_color = color
        
        self.circle = Circle(
            radius=radius,
            fill_color=color, fill_opacity=0.85,
            stroke_color=TEXT_PRIMARY, stroke_width=2
        )
        
        self.label = Text(label, font_size=TINY_SIZE, color=TEXT_PRIMARY)
        self.label.move_to(self.circle.get_center())
        
        self.add(self.circle, self.label)
    
    def set_active(self, active=True):
        color = STACK_ACTIVE if active else self.node_color
        self.circle.set_fill(color)


class CallStackView(VGroup):
    """Visual call stack for recursion."""
    
    def __init__(self, base_pos=None, frame_width=2.5, frame_height=0.55):
        super().__init__()
        self.frames = []
        self.base_pos = base_pos if base_pos is not None else RIGHT * 4.5 + DOWN * 2.5
        self.frame_width = frame_width
        self.frame_height = frame_height
        
        # Base line
        self.base_line = Line(
            self.base_pos + LEFT * (frame_width / 2 + 0.2),
            self.base_pos + RIGHT * (frame_width / 2 + 0.2),
            color=TEXT_PRIMARY, stroke_width=2
        )
        self.add(self.base_line)
    
    def create_frame(self, label, color=STACK_FRAME):
        """Create a new stack frame."""
        frame = VGroup()
        
        rect = Rectangle(
            width=self.frame_width, height=self.frame_height,
            fill_color=color, fill_opacity=0.85,
            stroke_color=TEXT_PRIMARY, stroke_width=2
        )
        
        text = Text(label, font_size=TINY_SIZE, color=TEXT_PRIMARY)
        text.move_to(rect.get_center())
        
        frame.add(rect, text)
        frame.rect = rect
        
        # Position
        y_offset = len(self.frames) * (self.frame_height + 0.08)
        frame.move_to(self.base_pos + UP * (self.frame_height / 2 + y_offset + 0.1))
        
        self.frames.append(frame)
        self.add(frame)
        return frame
    
    def pop_frame(self):
        """Remove top frame."""
        if self.frames:
            frame = self.frames.pop()
            self.remove(frame)
            return frame
        return None
