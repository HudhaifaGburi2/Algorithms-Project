"""
Memory cell visualization component for arrays.
"""
from manim import *
import sys
sys.path.insert(0, '/home/hg/Desktop/algorthims/Chapter2_ArraysLinkedListsSelectionSort')

from config.colors import MEMORY_BOX, TEXT_PRIMARY, UNPROCESSED
from config.fonts import LABEL_SIZE, TINY_SIZE


class MemoryCellView(VGroup):
    """
    Visual representation of a memory cell (array element).
    Shows contiguous memory layout.
    """
    
    def __init__(
        self,
        value,
        index: int = 0,
        color: str = UNPROCESSED,
        width: float = 0.8,
        height: float = 0.6,
        show_address: bool = False,
        show_index: bool = True
    ):
        super().__init__()
        self.value = value
        self.index = index
        self.cell_color = color
        
        # Main cell box
        self.box = Rectangle(
            width=width,
            height=height,
            fill_color=color,
            fill_opacity=0.85,
            stroke_color=TEXT_PRIMARY,
            stroke_width=2
        )
        
        # Value label
        self.label = Text(str(value), font_size=int(LABEL_SIZE * 0.9), color=TEXT_PRIMARY)
        self.label.move_to(self.box.get_center())
        
        self.add(self.box, self.label)
        
        # Index label below
        if show_index:
            self.idx_label = Text(str(index), font_size=TINY_SIZE, color=TEXT_PRIMARY)
            self.idx_label.next_to(self.box, DOWN, buff=0.1)
            self.add(self.idx_label)
        
        # Memory address (optional)
        if show_address:
            addr = f"0x{1000 + index * 4:04X}"
            self.addr_label = Text(addr, font_size=TINY_SIZE - 2, color=TEXT_PRIMARY)
            self.addr_label.next_to(self.box, UP, buff=0.08)
            self.add(self.addr_label)
    
    def set_color(self, color):
        """Change cell color."""
        self.cell_color = color
        self.box.set_fill(color)
    
    def get_color_animation(self, color, run_time=0.5):
        """Return animation for color change."""
        return self.box.animate.set_fill(color)


class ArrayView(VGroup):
    """
    Visual representation of an array in memory.
    Shows contiguous memory cells.
    """
    
    def __init__(
        self,
        values: list,
        color: str = UNPROCESSED,
        cell_width: float = 0.8,
        cell_height: float = 0.6,
        spacing: float = 0.0,
        show_indices: bool = True,
        show_addresses: bool = False
    ):
        super().__init__()
        self.values = values
        self.cells = []
        
        for i, val in enumerate(values):
            cell = MemoryCellView(
                value=val,
                index=i,
                color=color,
                width=cell_width,
                height=cell_height,
                show_index=show_indices,
                show_address=show_addresses
            )
            self.cells.append(cell)
            self.add(cell)
        
        self.arrange(RIGHT, buff=spacing)
    
    def get_cell(self, index: int) -> MemoryCellView:
        """Get cell at index."""
        return self.cells[index]
    
    def highlight_cell(self, index: int, color: str):
        """Return animation to highlight a cell."""
        return self.cells[index].get_color_animation(color)
    
    def swap_values(self, i: int, j: int):
        """Swap values at indices i and j (updates internal state)."""
        self.values[i], self.values[j] = self.values[j], self.values[i]
