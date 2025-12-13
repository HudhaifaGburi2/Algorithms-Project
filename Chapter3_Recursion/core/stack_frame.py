"""
Stack frame visualization component for call stack.
"""
from manim import *
import sys
sys.path.insert(0, '/home/hg/Desktop/algorthims/Chapter3_Recursion')

from config.colors import STACK_FRAME, TEXT_PRIMARY, STACK_ACTIVE
from config.fonts import SMALL_SIZE, TINY_SIZE


class StackFrameView(VGroup):
    """
    Visual representation of a stack frame.
    Shows function name and local variables.
    """
    
    def __init__(
        self,
        func_name: str,
        params: dict = None,
        color: str = STACK_FRAME,
        width: float = 3.0,
        height: float = 0.7
    ):
        super().__init__()
        self.func_name = func_name
        self.params = params or {}
        self.frame_color = color
        
        # Main frame box
        self.box = Rectangle(
            width=width,
            height=height,
            fill_color=color,
            fill_opacity=0.85,
            stroke_color=TEXT_PRIMARY,
            stroke_width=2
        )
        
        # Function name
        self.name_label = Text(func_name, font_size=SMALL_SIZE, color=TEXT_PRIMARY)
        self.name_label.move_to(self.box.get_center())
        
        # Parameters (if any)
        if params:
            param_str = ", ".join([f"{k}={v}" for k, v in params.items()])
            self.param_label = Text(param_str, font_size=TINY_SIZE, color=TEXT_PRIMARY)
            self.param_label.next_to(self.name_label, DOWN, buff=0.05)
            self.name_label.shift(UP * 0.1)
            self.add(self.param_label)
        
        self.add(self.box, self.name_label)
    
    def set_active(self, active: bool = True):
        """Highlight as active frame."""
        color = STACK_ACTIVE if active else self.frame_color
        self.box.set_fill(color)
    
    def get_activation_animation(self, run_time=0.5):
        """Return animation for activating this frame."""
        return self.box.animate.set_fill(STACK_ACTIVE)
    
    def get_deactivation_animation(self, run_time=0.5):
        """Return animation for deactivating this frame."""
        return self.box.animate.set_fill(self.frame_color)


class CallStackView(VGroup):
    """
    Visual representation of the call stack.
    Manages multiple stack frames.
    """
    
    def __init__(
        self,
        base_position: np.ndarray = None,
        frame_width: float = 3.0,
        frame_height: float = 0.7,
        spacing: float = 0.1
    ):
        super().__init__()
        self.frames = []
        self.base_position = base_position if base_position is not None else DOWN * 2.5
        self.frame_width = frame_width
        self.frame_height = frame_height
        self.spacing = spacing
        
        # Stack base indicator
        self.base_line = Line(
            self.base_position + LEFT * (frame_width / 2 + 0.2),
            self.base_position + RIGHT * (frame_width / 2 + 0.2),
            color=TEXT_PRIMARY,
            stroke_width=3
        )
        self.add(self.base_line)
    
    def push_frame(self, func_name: str, params: dict = None, color: str = STACK_FRAME):
        """Create and position a new frame on top of stack."""
        frame = StackFrameView(
            func_name=func_name,
            params=params,
            color=color,
            width=self.frame_width,
            height=self.frame_height
        )
        
        # Position on top of existing frames
        y_offset = len(self.frames) * (self.frame_height + self.spacing)
        frame.move_to(self.base_position + UP * (self.frame_height / 2 + y_offset + 0.1))
        
        self.frames.append(frame)
        self.add(frame)
        return frame
    
    def pop_frame(self):
        """Remove and return the top frame."""
        if self.frames:
            frame = self.frames.pop()
            self.remove(frame)
            return frame
        return None
    
    def get_top_frame(self):
        """Get the topmost frame without removing it."""
        return self.frames[-1] if self.frames else None
    
    def get_frame_count(self):
        """Return number of frames on stack."""
        return len(self.frames)
