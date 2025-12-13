"""
Graph visualization components for BFS.
"""
from manim import *
import sys
sys.path.insert(0, '/home/hg/Desktop/algorthims/Chapter6_BreadthFirstSearch')

from config.colors import (
    NODE_DEFAULT, NODE_ACTIVE, NODE_QUEUED, NODE_VISITED, NODE_TARGET,
    EDGE_DEFAULT, EDGE_ACTIVE, EDGE_PATH, TEXT_PRIMARY
)
from config.fonts import NODE_LABEL_SIZE, DEGREE_LABEL_SIZE


class GraphNodeView(VGroup):
    """Single node in graph."""
    
    def __init__(self, label, radius=0.4, color=NODE_DEFAULT):
        super().__init__()
        self.label_text = label
        self.node_color = color
        self.state = "default"
        
        # Circle
        self.circle = Circle(
            radius=radius,
            fill_color=color, fill_opacity=0.9,
            stroke_color=TEXT_PRIMARY, stroke_width=3
        )
        
        # Label
        self.label = Text(label, font_size=NODE_LABEL_SIZE, color=TEXT_PRIMARY)
        self.label.move_to(self.circle.get_center())
        
        self.add(self.circle, self.label)
    
    def set_state(self, state):
        """Change node state: default, queued, active, visited, target."""
        self.state = state
        colors = {
            "default": NODE_DEFAULT,
            "queued": NODE_QUEUED,
            "active": NODE_ACTIVE,
            "visited": NODE_VISITED,
            "target": NODE_TARGET
        }
        self.circle.set_fill(colors.get(state, NODE_DEFAULT))
    
    def get_state_animation(self, state, run_time=0.4):
        """Return animation for state change."""
        colors = {
            "default": NODE_DEFAULT,
            "queued": NODE_QUEUED,
            "active": NODE_ACTIVE,
            "visited": NODE_VISITED,
            "target": NODE_TARGET
        }
        return self.circle.animate.set_fill(colors.get(state, NODE_DEFAULT))


class GraphEdgeView(VGroup):
    """Edge between nodes."""
    
    def __init__(self, start_node, end_node, directed=True, color=EDGE_DEFAULT):
        super().__init__()
        self.start_node = start_node
        self.end_node = end_node
        self.directed = directed
        self.edge_color = color
        
        if directed:
            self.line = Arrow(
                start_node.get_center(),
                end_node.get_center(),
                color=color, stroke_width=3,
                buff=0.45, max_tip_length_to_length_ratio=0.15
            )
        else:
            self.line = Line(
                start_node.get_center(),
                end_node.get_center(),
                color=color, stroke_width=3
            ).set_opacity(0.6)
        
        self.add(self.line)
    
    def set_active(self):
        self.line.set_color(EDGE_ACTIVE)
        self.line.set_stroke(width=5)
    
    def set_path(self):
        self.line.set_color(EDGE_PATH)
        self.line.set_stroke(width=6)


class QueueCardView(VGroup):
    """Card in the search queue."""
    
    def __init__(self, label, width=1.2, height=0.5, color=None):
        super().__init__()
        from config.colors import QUEUE_COLOR
        color = color or QUEUE_COLOR
        
        self.rect = RoundedRectangle(
            width=width, height=height, corner_radius=0.1,
            fill_color=color, fill_opacity=0.9,
            stroke_color=TEXT_PRIMARY, stroke_width=2
        )
        
        self.label = Text(label, font_size=NODE_LABEL_SIZE, color=TEXT_PRIMARY)
        self.label.move_to(self.rect.get_center())
        
        self.add(self.rect, self.label)


class QueueView(VGroup):
    """Visual queue for BFS."""
    
    def __init__(self, position=None):
        super().__init__()
        self.cards = []
        self.position = position or RIGHT * 4 + UP * 1
        
        # Queue container
        self.container_label = Text("Queue", font_size=NODE_LABEL_SIZE, color=TEXT_PRIMARY)
        self.container_label.move_to(self.position + UP * 1)
        self.add(self.container_label)
        
        # Front/Back labels
        self.front_label = Text("Front", font_size=DEGREE_LABEL_SIZE, color=TEXT_PRIMARY)
        self.back_label = Text("Back", font_size=DEGREE_LABEL_SIZE, color=TEXT_PRIMARY)
    
    def enqueue(self, label):
        """Add card to back of queue."""
        card = QueueCardView(label)
        
        # Position at back
        if self.cards:
            card.next_to(self.cards[-1], DOWN, buff=0.1)
        else:
            card.move_to(self.position)
        
        self.cards.append(card)
        self.add(card)
        return card
    
    def dequeue(self):
        """Remove card from front."""
        if self.cards:
            card = self.cards.pop(0)
            self.remove(card)
            # Shift remaining cards up
            for i, c in enumerate(self.cards):
                if i == 0:
                    c.move_to(self.position)
                else:
                    c.next_to(self.cards[i-1], DOWN, buff=0.1)
            return card
        return None
