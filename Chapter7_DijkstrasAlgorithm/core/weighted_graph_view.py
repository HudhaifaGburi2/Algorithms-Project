"""
Weighted graph visualization components for Dijkstra's algorithm.
"""
from manim import *
import sys
sys.path.insert(0, '/home/hg/Desktop/algorthims/Chapter7_DijkstrasAlgorithm')

from config.colors import (
    NODE_DEFAULT, NODE_PROCESSING, NODE_PROCESSED, NODE_CHEAPEST,
    NODE_START, NODE_FINISH, EDGE_DEFAULT, EDGE_PATH, TEXT_PRIMARY,
    COST_TABLE, PARENT_TABLE, PROCESSED_SET
)
from config.fonts import NODE_LABEL_SIZE, WEIGHT_LABEL_SIZE, TINY_SIZE


class WeightedNodeView(VGroup):
    """Node with cost badge for Dijkstra visualization."""
    
    def __init__(self, label, radius=0.45, color=NODE_DEFAULT, is_start=False, is_finish=False):
        super().__init__()
        self.label_text = label
        self.state = "default"
        
        # Determine initial color
        if is_start:
            color = NODE_START
        elif is_finish:
            color = NODE_FINISH
        
        # Circle
        self.circle = Circle(
            radius=radius,
            fill_color=color, fill_opacity=0.9,
            stroke_color=TEXT_PRIMARY, stroke_width=4
        )
        
        # Label
        self.label = Text(label, font_size=NODE_LABEL_SIZE, color=TEXT_PRIMARY)
        self.label.move_to(self.circle.get_center())
        
        self.add(self.circle, self.label)
    
    def set_state(self, state):
        """Change node state."""
        self.state = state
        colors = {
            "default": NODE_DEFAULT,
            "cheapest": NODE_CHEAPEST,
            "processing": NODE_PROCESSING,
            "processed": NODE_PROCESSED,
            "start": NODE_START,
            "finish": NODE_FINISH
        }
        self.circle.set_fill(colors.get(state, NODE_DEFAULT))


class WeightedEdgeView(VGroup):
    """Edge with weight label for weighted graphs."""
    
    def __init__(self, start_node, end_node, weight, color=EDGE_DEFAULT, directed=True):
        super().__init__()
        self.weight = weight
        self.directed = directed
        
        # Calculate direction
        start = start_node.get_center()
        end = end_node.get_center()
        
        if directed:
            self.line = Arrow(
                start, end, color=color, stroke_width=4,
                buff=0.5, max_tip_length_to_length_ratio=0.1
            )
        else:
            self.line = Line(start, end, color=color, stroke_width=4)
        
        # Weight badge
        mid = (start + end) / 2
        self.weight_badge = VGroup()
        
        badge_bg = Circle(radius=0.2, fill_color=BACKGROUND_COLOR, fill_opacity=0.9,
                         stroke_color=color, stroke_width=2)
        badge_text = Text(str(weight), font_size=WEIGHT_LABEL_SIZE, color=TEXT_PRIMARY)
        badge_text.move_to(badge_bg.get_center())
        
        self.weight_badge.add(badge_bg, badge_text)
        self.weight_badge.move_to(mid)
        
        self.add(self.line, self.weight_badge)


class CostTableView(VGroup):
    """Cost tracking table for Dijkstra."""
    
    def __init__(self, nodes, position=None):
        super().__init__()
        self.nodes = nodes
        self.cost_texts = {}
        
        # Header
        header = Text("COSTS", font_size=TINY_SIZE, color=COST_TABLE, weight=BOLD)
        self.add(header)
        
        # Rows
        self.rows = VGroup()
        for i, node in enumerate(nodes):
            row = VGroup()
            name = Text(node, font_size=TINY_SIZE, color=TEXT_PRIMARY)
            cost = Text("∞", font_size=TINY_SIZE, color=TEXT_PRIMARY)
            name.move_to(LEFT * 0.8)
            cost.move_to(RIGHT * 0.5)
            row.add(name, cost)
            self.cost_texts[node] = cost
            self.rows.add(row)
        
        self.rows.arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        self.rows.next_to(header, DOWN, buff=0.3)
        self.add(self.rows)
        
        if position:
            self.move_to(position)
    
    def update_cost(self, node, cost):
        """Update cost display for a node."""
        if node in self.cost_texts:
            if cost == float('inf'):
                self.cost_texts[node].become(
                    Text("∞", font_size=TINY_SIZE, color=TEXT_PRIMARY)
                    .move_to(self.cost_texts[node].get_center())
                )
            else:
                self.cost_texts[node].become(
                    Text(str(cost), font_size=TINY_SIZE, color=COST_TABLE)
                    .move_to(self.cost_texts[node].get_center())
                )


class ParentTableView(VGroup):
    """Parent tracking table for path reconstruction."""
    
    def __init__(self, nodes, position=None):
        super().__init__()
        self.nodes = nodes
        self.parent_texts = {}
        
        # Header
        header = Text("PARENTS", font_size=TINY_SIZE, color=PARENT_TABLE, weight=BOLD)
        self.add(header)
        
        # Rows
        self.rows = VGroup()
        for node in nodes:
            row = VGroup()
            name = Text(node, font_size=TINY_SIZE, color=TEXT_PRIMARY)
            parent = Text("—", font_size=TINY_SIZE, color=TEXT_PRIMARY)
            name.move_to(LEFT * 0.8)
            parent.move_to(RIGHT * 0.5)
            row.add(name, parent)
            self.parent_texts[node] = parent
            self.rows.add(row)
        
        self.rows.arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        self.rows.next_to(header, DOWN, buff=0.3)
        self.add(self.rows)
        
        if position:
            self.move_to(position)


class ProcessedSetView(VGroup):
    """Processed nodes display."""
    
    def __init__(self, position=None):
        super().__init__()
        self.chips = []
        
        # Header
        header = Text("PROCESSED", font_size=TINY_SIZE, color=PROCESSED_SET, weight=BOLD)
        self.add(header)
        
        self.chip_container = VGroup()
        self.chip_container.next_to(header, DOWN, buff=0.3)
        self.add(self.chip_container)
        
        if position:
            self.move_to(position)
    
    def add_node(self, node_name):
        """Add a processed node chip."""
        chip = VGroup()
        bg = RoundedRectangle(width=0.8, height=0.35, corner_radius=0.1,
                             fill_color=PROCESSED_SET, fill_opacity=0.9,
                             stroke_width=0)
        label = Text(f"✓{node_name}", font_size=12, color=TEXT_PRIMARY)
        label.move_to(bg.get_center())
        chip.add(bg, label)
        
        if self.chips:
            chip.next_to(self.chips[-1], RIGHT, buff=0.1)
        else:
            chip.next_to(self.submobjects[0], DOWN, buff=0.3)
        
        self.chips.append(chip)
        self.chip_container.add(chip)
        return chip


# Import background color
from config.colors import BACKGROUND_COLOR
