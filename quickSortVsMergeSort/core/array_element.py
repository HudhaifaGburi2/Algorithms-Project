"""
ArrayElement: Reusable visual component for array bars.
R10 compliant: Reusable component, no copy-paste.
R6 compliant: No hard-coded coordinates.
"""
from manim import (
    VGroup, Rectangle, Text, 
    UP, DOWN, ORIGIN,
    FadeIn, FadeOut, Transform
)
from config.colors import UNPROCESSED, TEXT_PRIMARY
from config.animation_constants import BAR_WIDTH, BAR_HEIGHT_SCALE, MAX_BAR_HEIGHT
from config.fonts import LABEL_SIZE


class ArrayElementView(VGroup):
    """
    Visual representation of a single array element as a bar.
    Color encodes semantic state (R4 compliant).
    """
    
    def __init__(
        self,
        value: int,
        color: str = UNPROCESSED,
        show_label: bool = True,
        width: float = BAR_WIDTH,
        height_scale: float = BAR_HEIGHT_SCALE,
        max_height: float = MAX_BAR_HEIGHT,
        **kwargs
    ):
        super().__init__(**kwargs)
        self.value = value
        self.element_color = color
        
        # Calculate bar height based on value
        self.bar_height = min(value * height_scale, max_height)
        
        # Create bar rectangle
        self.bar = Rectangle(
            width=width,
            height=self.bar_height,
            fill_color=color,
            fill_opacity=0.9,
            stroke_color=color,
            stroke_width=2
        )
        
        # Create value label
        self.label = Text(
            str(value),
            font_size=LABEL_SIZE,
            color=TEXT_PRIMARY
        )
        self.label.next_to(self.bar, UP, buff=0.1)
        
        self.add(self.bar)
        if show_label:
            self.add(self.label)
    
    def set_semantic_color(self, color: str, animate: bool = False):
        """
        Change color to reflect semantic state.
        R4: Color encodes meaning.
        """
        self.element_color = color
        if animate:
            return self.bar.animate.set_fill(color).set_stroke(color)
        else:
            self.bar.set_fill(color)
            self.bar.set_stroke(color)
            return self
    
    def get_color_animation(self, color: str):
        """Return animation for color change."""
        return self.bar.animate.set_fill(color).set_stroke(color)
    
    def get_value(self) -> int:
        """Return the numeric value."""
        return self.value
    
    def copy_with_value(self, new_value: int = None):
        """Create a copy with optionally different value."""
        return ArrayElementView(
            value=new_value if new_value is not None else self.value,
            color=self.element_color,
            show_label=self.label in self.submobjects
        )


class ArrayGroupView(VGroup):
    """
    Visual representation of an array as a group of bars.
    R6 compliant: Uses relative positioning.
    R10 compliant: Reusable component.
    """
    
    def __init__(
        self,
        values: list,
        color: str = UNPROCESSED,
        spacing: float = 0.15,
        show_labels: bool = True,
        **kwargs
    ):
        super().__init__(**kwargs)
        self.values = values
        self.spacing = spacing
        self.elements = []
        
        # Create elements
        for value in values:
            element = ArrayElementView(
                value=value,
                color=color,
                show_label=show_labels
            )
            self.elements.append(element)
            self.add(element)
        
        # Arrange horizontally with spacing (R6: relative positioning)
        self.arrange(RIGHT, buff=spacing)
    
    def get_element(self, index: int) -> ArrayElementView:
        """Get element at index."""
        return self.elements[index]
    
    def get_elements_range(self, start: int, end: int) -> list:
        """Get elements in range [start, end)."""
        return self.elements[start:end]
    
    def set_range_color(self, start: int, end: int, color: str):
        """Set color for a range of elements."""
        animations = []
        for i in range(start, end):
            animations.append(self.elements[i].get_color_animation(color))
        return animations
    
    def highlight_element(self, index: int, color: str):
        """Highlight single element."""
        return self.elements[index].get_color_animation(color)
    
    def get_subarray_group(self, start: int, end: int) -> VGroup:
        """Get a VGroup of elements in range."""
        return VGroup(*self.elements[start:end])


# Import RIGHT for arrange
from manim import RIGHT
