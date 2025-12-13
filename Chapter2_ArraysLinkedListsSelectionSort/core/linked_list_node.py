"""
Linked list node visualization component.
"""
from manim import *
import sys
sys.path.insert(0, '/home/hg/Desktop/algorthims/Chapter2_ArraysLinkedListsSelectionSort')

from config.colors import LINKED_LIST_COLOR, POINTER_COLOR, TEXT_PRIMARY, MEMORY_BOX
from config.fonts import LABEL_SIZE, TINY_SIZE


class LinkedListNodeView(VGroup):
    """
    Visual representation of a linked list node.
    Contains value section and pointer section.
    """
    
    def __init__(
        self,
        value,
        index: int = 0,
        color: str = LINKED_LIST_COLOR,
        width: float = 1.2,
        height: float = 0.6,
        show_address: bool = False
    ):
        super().__init__()
        self.value = value
        self.index = index
        self.node_color = color
        
        # Value section (left part of node)
        value_width = width * 0.65
        self.value_box = Rectangle(
            width=value_width,
            height=height,
            fill_color=color,
            fill_opacity=0.85,
            stroke_color=TEXT_PRIMARY,
            stroke_width=2
        )
        
        # Pointer section (right part of node)
        ptr_width = width * 0.35
        self.ptr_box = Rectangle(
            width=ptr_width,
            height=height,
            fill_color=MEMORY_BOX,
            fill_opacity=0.7,
            stroke_color=TEXT_PRIMARY,
            stroke_width=2
        )
        self.ptr_box.next_to(self.value_box, RIGHT, buff=0)
        
        # Value label
        self.label = Text(str(value), font_size=int(LABEL_SIZE * 0.85), color=TEXT_PRIMARY)
        self.label.move_to(self.value_box.get_center())
        
        # Pointer dot
        self.ptr_dot = Dot(color=POINTER_COLOR, radius=0.08)
        self.ptr_dot.move_to(self.ptr_box.get_center())
        
        self.add(self.value_box, self.ptr_box, self.label, self.ptr_dot)
        
        # Memory address (optional)
        if show_address:
            # Scattered addresses (non-contiguous)
            addr = f"0x{1000 + index * 100 + (index % 3) * 50:04X}"
            self.addr_label = Text(addr, font_size=TINY_SIZE - 2, color=TEXT_PRIMARY)
            self.addr_label.next_to(self.value_box, UP, buff=0.08)
            self.add(self.addr_label)
    
    def set_color(self, color):
        """Change node color."""
        self.node_color = color
        self.value_box.set_fill(color)
    
    def get_color_animation(self, color, run_time=0.5):
        """Return animation for color change."""
        return self.value_box.animate.set_fill(color)
    
    def get_ptr_position(self):
        """Get position for outgoing pointer arrow."""
        return self.ptr_box.get_right()
    
    def get_input_position(self):
        """Get position for incoming pointer arrow."""
        return self.value_box.get_left()


class LinkedListView(VGroup):
    """
    Visual representation of a linked list.
    Shows nodes with pointer arrows between them.
    """
    
    def __init__(
        self,
        values: list,
        color: str = LINKED_LIST_COLOR,
        node_width: float = 1.2,
        node_height: float = 0.6,
        spacing: float = 0.8,
        show_addresses: bool = False,
        scattered: bool = False
    ):
        super().__init__()
        self.values = values
        self.nodes = []
        self.arrows = []
        
        # Create nodes
        for i, val in enumerate(values):
            node = LinkedListNodeView(
                value=val,
                index=i,
                color=color,
                width=node_width,
                height=node_height,
                show_address=show_addresses
            )
            self.nodes.append(node)
            self.add(node)
        
        # Arrange nodes
        if scattered:
            # Scattered layout to show non-contiguous memory
            positions = [
                ORIGIN,
                RIGHT * 2.5 + UP * 0.3,
                RIGHT * 5 + DOWN * 0.2,
                RIGHT * 7.5 + UP * 0.4,
                RIGHT * 10 + DOWN * 0.1,
            ]
            for i, node in enumerate(self.nodes):
                if i < len(positions):
                    node.move_to(positions[i])
        else:
            # Linear arrangement
            for i, node in enumerate(self.nodes):
                if i > 0:
                    node.next_to(self.nodes[i-1], RIGHT, buff=spacing)
        
        # Create arrows between nodes
        for i in range(len(self.nodes) - 1):
            arrow = Arrow(
                start=self.nodes[i].get_ptr_position(),
                end=self.nodes[i+1].get_input_position(),
                color=POINTER_COLOR,
                buff=0.1,
                stroke_width=3,
                max_tip_length_to_length_ratio=0.2
            )
            self.arrows.append(arrow)
            self.add(arrow)
        
        # NULL terminator
        if self.nodes:
            null_text = Text("NULL", font_size=TINY_SIZE, color=TEXT_PRIMARY)
            null_text.next_to(self.nodes[-1].ptr_box, RIGHT, buff=0.3)
            self.null_label = null_text
            self.add(null_text)
    
    def get_node(self, index: int) -> LinkedListNodeView:
        """Get node at index."""
        return self.nodes[index]
    
    def highlight_node(self, index: int, color: str):
        """Return animation to highlight a node."""
        return self.nodes[index].get_color_animation(color)
