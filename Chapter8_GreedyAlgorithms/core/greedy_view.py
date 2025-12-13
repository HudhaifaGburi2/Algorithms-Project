"""
Greedy algorithm visualization components.
"""
from manim import *
import sys
sys.path.insert(0, '/home/hg/Desktop/algorthims/Chapter8_GreedyAlgorithms')

from config.colors import (
    GREEDY_CHOICE, SELECTED_ITEM, REJECTED_ITEM, AVAILABLE_ITEM,
    TEXT_PRIMARY, BACKGROUND_COLOR, STATE_COVERED, STATE_UNCOVERED
)
from config.fonts import LABEL_SIZE, SMALL_SIZE, TINY_SIZE, VALUE_SIZE


class TimelineBlockView(VGroup):
    """Class block on a schedule timeline."""
    
    def __init__(self, name, start_hour, end_hour, color=AVAILABLE_ITEM, 
                 timeline_start=9, timeline_width=10):
        super().__init__()
        self.name = name
        self.start_hour = start_hour
        self.end_hour = end_hour
        
        # Calculate position and width
        hour_width = timeline_width / 3  # 9am to 12pm = 3 hours
        x_start = (start_hour - timeline_start) * hour_width - timeline_width / 2
        block_width = (end_hour - start_hour) * hour_width
        
        # Block rectangle
        self.block = Rectangle(
            width=block_width, height=0.6,
            fill_color=color, fill_opacity=0.8,
            stroke_color=TEXT_PRIMARY, stroke_width=2
        )
        self.block.move_to(RIGHT * (x_start + block_width / 2))
        
        # Name label
        self.label = Text(name, font_size=TINY_SIZE, color=TEXT_PRIMARY)
        self.label.move_to(self.block.get_center())
        
        # End time badge
        end_time = f"{end_hour}:00" if end_hour < 12 else "12:00"
        self.end_label = Text(end_time, font_size=12, color=TEXT_PRIMARY)
        self.end_label.next_to(self.block, RIGHT, buff=0.1)
        
        self.add(self.block, self.label, self.end_label)
    
    def select(self):
        self.block.set_fill(SELECTED_ITEM)
    
    def reject(self):
        self.block.set_fill(REJECTED_ITEM)
        self.block.set_opacity(0.4)


class KnapsackItemView(VGroup):
    """Item for knapsack problem."""
    
    def __init__(self, name, value, weight, color=AVAILABLE_ITEM):
        super().__init__()
        self.item_name = name
        self.value = value
        self.weight = weight
        
        # Container
        self.box = RoundedRectangle(
            width=2.2, height=1.2, corner_radius=0.1,
            fill_color=color, fill_opacity=0.8,
            stroke_color=TEXT_PRIMARY, stroke_width=2
        )
        
        # Name
        self.name_text = Text(name, font_size=SMALL_SIZE, color=TEXT_PRIMARY)
        self.name_text.move_to(self.box.get_center() + UP * 0.3)
        
        # Value and weight
        self.value_text = Text(f"${value}", font_size=TINY_SIZE, color=GREEDY_CHOICE)
        self.weight_text = Text(f"{weight} lbs", font_size=TINY_SIZE, color=TEXT_PRIMARY)
        self.value_text.move_to(self.box.get_center() + DOWN * 0.15 + LEFT * 0.4)
        self.weight_text.move_to(self.box.get_center() + DOWN * 0.15 + RIGHT * 0.4)
        
        self.add(self.box, self.name_text, self.value_text, self.weight_text)
    
    def select(self):
        self.box.set_fill(SELECTED_ITEM)
    
    def reject(self):
        self.box.set_fill(REJECTED_ITEM)
        self.box.set_opacity(0.5)


class CapacityGaugeView(VGroup):
    """Visual gauge for knapsack capacity."""
    
    def __init__(self, capacity, width=4.0, height=0.4):
        super().__init__()
        self.capacity = capacity
        self.used = 0
        self.gauge_width = width
        
        # Background
        self.bg = Rectangle(
            width=width, height=height,
            fill_color="#1E293B", fill_opacity=1,
            stroke_color=TEXT_PRIMARY, stroke_width=2
        )
        
        # Fill bar
        self.fill_bar = Rectangle(
            width=0.01, height=height - 0.1,
            fill_color=SELECTED_ITEM, fill_opacity=0.9,
            stroke_width=0
        )
        self.fill_bar.align_to(self.bg, LEFT)
        self.fill_bar.shift(RIGHT * 0.05)
        
        # Label
        self.label = Text(f"0/{capacity} lbs", font_size=TINY_SIZE, color=TEXT_PRIMARY)
        self.label.next_to(self.bg, RIGHT, buff=0.2)
        
        self.add(self.bg, self.fill_bar, self.label)
    
    def set_used(self, used):
        self.used = used
        fill_width = (used / self.capacity) * (self.gauge_width - 0.1)
        self.fill_bar.stretch_to_fit_width(max(0.01, fill_width))
        self.fill_bar.align_to(self.bg, LEFT)
        self.fill_bar.shift(RIGHT * 0.05)


class StateNodeView(VGroup):
    """State node for set covering map."""
    
    def __init__(self, name, position, radius=0.3):
        super().__init__()
        self.state_name = name
        self.covered = False
        
        self.circle = Circle(
            radius=radius,
            fill_color=STATE_UNCOVERED, fill_opacity=0.8,
            stroke_color=TEXT_PRIMARY, stroke_width=2
        )
        self.circle.move_to(position)
        
        self.label = Text(name, font_size=12, color=TEXT_PRIMARY)
        self.label.move_to(position)
        
        self.add(self.circle, self.label)
    
    def cover(self):
        self.covered = True
        self.circle.set_fill(STATE_COVERED)


class StationCoverageView(VGroup):
    """Radio station with coverage area."""
    
    def __init__(self, name, position, radius=1.5, color=None):
        super().__init__()
        from config.colors import STATION_COLOR
        color = color or STATION_COLOR
        
        # Coverage circle
        self.coverage = Circle(
            radius=radius,
            fill_color=color, fill_opacity=0.15,
            stroke_color=color, stroke_width=2
        )
        self.coverage.move_to(position)
        
        # Station marker
        self.marker = Circle(
            radius=0.15,
            fill_color=color, fill_opacity=0.9,
            stroke_width=0
        )
        self.marker.move_to(position)
        
        # Label
        self.label = Text(name, font_size=TINY_SIZE, color=color)
        self.label.next_to(self.marker, UP, buff=0.1)
        
        self.add(self.coverage, self.marker, self.label)
    
    def select(self):
        self.coverage.set_fill(opacity=0.3)
        self.coverage.set_stroke(width=4)
