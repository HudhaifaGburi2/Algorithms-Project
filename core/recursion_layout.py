"""
Recursion tree layout for visualizing divide-and-conquer.
R5 compliant: Recursion shown spatially, not textually.
R6 compliant: Relative positioning only.
"""
from manim import (
    VGroup, Line, DashedLine,
    UP, DOWN, LEFT, RIGHT, ORIGIN,
    Create, FadeIn, FadeOut
)
from config.colors import TEXT_SECONDARY, UNPROCESSED
from config.animation_constants import (
    RECURSION_VERTICAL_SPACING,
    RECURSION_HORIZONTAL_SPACING,
    SCALE_RECURSION_DEPTH
)


class RecursionNodeView(VGroup):
    """
    A node in the recursion tree containing an array visualization.
    Vertical position = recursion depth (R5 compliant).
    """
    
    def __init__(
        self,
        array_view: VGroup,
        depth: int = 0,
        **kwargs
    ):
        super().__init__(**kwargs)
        self.array_view = array_view
        self.depth = depth
        self.children = []
        self.parent = None
        self.connection_lines = VGroup()
        
        # Scale based on depth
        scale_factor = SCALE_RECURSION_DEPTH ** depth
        array_view.scale(scale_factor)
        
        self.add(array_view)
        self.add(self.connection_lines)
    
    def add_child(self, child_node, position: str = "left"):
        """
        Add a child node and create connection line.
        R6: Positioning is relative to parent.
        """
        child_node.parent = self
        child_node.depth = self.depth + 1
        self.children.append(child_node)
        
        # Position child below parent (R5: vertical = depth)
        vertical_offset = DOWN * RECURSION_VERTICAL_SPACING
        
        if position == "left":
            horizontal_offset = LEFT * RECURSION_HORIZONTAL_SPACING * (2 ** (3 - self.depth))
        else:
            horizontal_offset = RIGHT * RECURSION_HORIZONTAL_SPACING * (2 ** (3 - self.depth))
        
        child_node.next_to(self.array_view, DOWN, buff=RECURSION_VERTICAL_SPACING)
        child_node.shift(horizontal_offset)
        
        # Create connection line
        line = Line(
            self.array_view.get_bottom(),
            child_node.array_view.get_top(),
            color=TEXT_SECONDARY,
            stroke_width=2
        )
        self.connection_lines.add(line)
        
        return child_node
    
    def get_connection_animation(self):
        """Get animation for drawing connection lines."""
        return [Create(line) for line in self.connection_lines]


class RecursionTreeView(VGroup):
    """
    Complete recursion tree visualization.
    R5: Recursion depth shown spatially via vertical position.
    """
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.root = None
        self.all_nodes = []
        self.all_lines = VGroup()
    
    def set_root(self, node: RecursionNodeView):
        """Set the root node of the tree."""
        self.root = node
        self.all_nodes.append(node)
        self.add(node)
        return self
    
    def add_level(self, parent_node: RecursionNodeView, left_view: VGroup, right_view: VGroup):
        """
        Add a level to the tree with left and right children.
        Returns tuple of (left_node, right_node).
        """
        left_node = RecursionNodeView(
            left_view,
            depth=parent_node.depth + 1
        )
        right_node = RecursionNodeView(
            right_view,
            depth=parent_node.depth + 1
        )
        
        parent_node.add_child(left_node, "left")
        parent_node.add_child(right_node, "right")
        
        self.all_nodes.extend([left_node, right_node])
        self.add(left_node, right_node)
        self.all_lines.add(*parent_node.connection_lines)
        
        return left_node, right_node
    
    def get_nodes_at_depth(self, depth: int) -> list:
        """Get all nodes at a specific depth."""
        return [node for node in self.all_nodes if node.depth == depth]
    
    def get_max_depth(self) -> int:
        """Get maximum depth of the tree."""
        return max(node.depth for node in self.all_nodes) if self.all_nodes else 0


class MergeContainerView(VGroup):
    """
    Container for merge operation visualization.
    Shows temporary storage during merge (R4: Purple color).
    """
    
    def __init__(
        self,
        width: float,
        height: float,
        color: str = UNPROCESSED,
        **kwargs
    ):
        super().__init__(**kwargs)
        from manim import Rectangle, RoundedRectangle
        
        self.container = RoundedRectangle(
            width=width,
            height=height,
            corner_radius=0.1,
            fill_color=color,
            fill_opacity=0.1,
            stroke_color=color,
            stroke_width=2
        )
        self.add(self.container)
        self.elements = VGroup()
        self.add(self.elements)
    
    def add_element(self, element: VGroup, index: int = None):
        """Add element to container."""
        self.elements.add(element)
        # Arrange elements inside container
        self.elements.arrange(RIGHT, buff=0.1)
        self.elements.move_to(self.container.get_center())
        return self
