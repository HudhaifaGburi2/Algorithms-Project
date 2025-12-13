"""
Hash table visualization components.
"""
from manim import *
import sys
sys.path.insert(0, '/home/hg/Desktop/algorthims/Chapter5_HashTables')

from config.colors import (
    CELL_EMPTY, CELL_FILLED, CELL_HIGHLIGHT, TEXT_PRIMARY,
    KEY_COLOR, VALUE_COLOR, LINKED_LIST, HASH_FUNCTION
)
from config.fonts import LABEL_SIZE, SMALL_SIZE, TINY_SIZE


class HashCellView(VGroup):
    """Single cell in hash table array."""
    
    def __init__(self, index, width=0.8, height=0.6, color=CELL_EMPTY):
        super().__init__()
        self.index = index
        self.cell_color = color
        self.key = None
        self.value = None
        self.chain = []  # For collision handling
        
        # Cell rectangle
        self.rect = Rectangle(
            width=width, height=height,
            fill_color=color, fill_opacity=0.85,
            stroke_color=TEXT_PRIMARY, stroke_width=2
        )
        
        # Index label
        self.idx_label = Text(str(index), font_size=TINY_SIZE, color=TEXT_PRIMARY)
        self.idx_label.next_to(self.rect, UP, buff=0.08)
        
        self.add(self.rect, self.idx_label)
        
        # Content labels (hidden initially)
        self.content_label = None
    
    def set_content(self, key, value):
        """Set key-value content."""
        self.key = key
        self.value = value
        self.rect.set_fill(CELL_FILLED)
        
        if self.content_label:
            self.remove(self.content_label)
        
        self.content_label = Text(
            f"{key}:{value}", 
            font_size=TINY_SIZE, 
            color=TEXT_PRIMARY
        )
        self.content_label.move_to(self.rect.get_center())
        self.add(self.content_label)
    
    def highlight(self, color):
        """Return animation to highlight cell."""
        return self.rect.animate.set_fill(color)


class HashTableView(VGroup):
    """Complete hash table visualization."""
    
    def __init__(self, slots=10, cell_width=0.8, cell_height=0.6, spacing=0.1):
        super().__init__()
        self.slots = slots
        self.cells = []
        
        for i in range(slots):
            cell = HashCellView(i, cell_width, cell_height)
            self.cells.append(cell)
            self.add(cell)
        
        self.arrange(RIGHT, buff=spacing)
    
    def get_cell(self, index):
        return self.cells[index % self.slots]
    
    def insert(self, key, value, index):
        """Insert key-value at index."""
        cell = self.cells[index % self.slots]
        cell.set_content(key, value)


class HashFunctionView(VGroup):
    """Visual hash function box."""
    
    def __init__(self, width=2.0, height=1.2):
        super().__init__()
        
        # Main box
        self.box = RoundedRectangle(
            width=width, height=height,
            corner_radius=0.15,
            fill_color=HASH_FUNCTION, fill_opacity=0.7,
            stroke_color=TEXT_PRIMARY, stroke_width=2
        )
        
        # Label
        self.label = Text("hash()", font_size=SMALL_SIZE, color=TEXT_PRIMARY)
        self.label.move_to(self.box.get_center())
        
        # Input/output indicators
        self.input_dot = Dot(color=KEY_COLOR, radius=0.08)
        self.input_dot.next_to(self.box, UP, buff=0.15)
        
        self.output_dot = Dot(color=VALUE_COLOR, radius=0.08)
        self.output_dot.next_to(self.box, DOWN, buff=0.15)
        
        self.add(self.box, self.label, self.input_dot, self.output_dot)
    
    def pulse(self):
        """Return pulsing animation."""
        return self.box.animate.scale(1.1).set_fill(opacity=0.9)


class LinkedListNodeView(VGroup):
    """Node for collision chain."""
    
    def __init__(self, key, value, width=1.0, height=0.5):
        super().__init__()
        
        self.rect = Rectangle(
            width=width, height=height,
            fill_color=LINKED_LIST, fill_opacity=0.85,
            stroke_color=TEXT_PRIMARY, stroke_width=2
        )
        
        self.label = Text(
            f"{key}:{value}",
            font_size=TINY_SIZE,
            color=TEXT_PRIMARY
        )
        self.label.move_to(self.rect.get_center())
        
        self.add(self.rect, self.label)
