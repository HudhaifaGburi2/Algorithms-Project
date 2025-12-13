"""
Partition visualization for Quicksort.
"""
from manim import *
import sys
sys.path.insert(0, '/home/hg/Desktop/algorthims/Chapter4_DivideConquerQuicksort')

from config.colors import (
    PIVOT, LESS_THAN, GREATER_THAN, UNPROCESSED, 
    TEXT_PRIMARY, BASE_CASE
)
from config.fonts import LABEL_SIZE, SMALL_SIZE, TINY_SIZE


class ArrayCellView(VGroup):
    """Single array cell for quicksort visualization."""
    
    def __init__(self, value, color=UNPROCESSED, width=0.7, height=0.6, show_index=False, index=0):
        super().__init__()
        self.value = value
        self.cell_color = color
        
        self.rect = Rectangle(
            width=width, height=height,
            fill_color=color, fill_opacity=0.85,
            stroke_color=TEXT_PRIMARY, stroke_width=2
        )
        
        self.label = Text(str(value), font_size=int(LABEL_SIZE * 0.9), color=TEXT_PRIMARY)
        self.label.move_to(self.rect.get_center())
        
        self.add(self.rect, self.label)
        
        if show_index:
            self.idx_label = Text(str(index), font_size=TINY_SIZE, color=TEXT_PRIMARY)
            self.idx_label.next_to(self.rect, DOWN, buff=0.08)
            self.add(self.idx_label)
    
    def set_color(self, color):
        self.cell_color = color
        self.rect.set_fill(color)


class QuicksortArrayView(VGroup):
    """Array visualization for quicksort with partition coloring."""
    
    def __init__(self, values, color=UNPROCESSED, cell_width=0.7, spacing=0.08, show_indices=False):
        super().__init__()
        self.values = list(values)
        self.cells = []
        
        for i, val in enumerate(values):
            cell = ArrayCellView(val, color, cell_width, show_index=show_indices, index=i)
            self.cells.append(cell)
            self.add(cell)
        
        self.arrange(RIGHT, buff=spacing)
    
    def get_cell(self, index):
        return self.cells[index]
    
    def color_pivot(self, index):
        """Color element as pivot."""
        return self.cells[index].rect.animate.set_fill(PIVOT)
    
    def color_less_than(self, indices):
        """Color elements as less than pivot."""
        return [self.cells[i].rect.animate.set_fill(LESS_THAN) for i in indices]
    
    def color_greater_than(self, indices):
        """Color elements as greater than pivot."""
        return [self.cells[i].rect.animate.set_fill(GREATER_THAN) for i in indices]
    
    def color_base_case(self):
        """Color entire array as base case."""
        return [cell.rect.animate.set_fill(BASE_CASE) for cell in self.cells]
