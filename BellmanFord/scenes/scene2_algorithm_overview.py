#!/usr/bin/env python3
"""Scene 2: Algorithm Overview - Core Concept"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from manim import *
from config.colors import *
from config.fonts import *
from config.animation_constants import *


class Scene2_AlgorithmOverview(Scene):
    """Algorithm Overview (75s)"""
    
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        self._run_scene()
    
    def _node(self, label, pos=ORIGIN, color=NODE_DEFAULT, radius=0.45):
        grp = VGroup()
        circle = Circle(radius=radius, fill_color=color, fill_opacity=0.9,
                       stroke_color=TEXT_PRIMARY, stroke_width=3)
        circle.move_to(pos)
        lbl = Text(str(label), font_size=NODE_LABEL_SIZE, color=TEXT_PRIMARY)
        lbl.move_to(circle.get_center())
        grp.add(circle, lbl)
        grp.circle = circle
        return grp
    
    def _edge(self, n1, n2, weight, is_negative=False):
        grp = VGroup()
        color = EDGE_NEGATIVE if is_negative else EDGE_POSITIVE
        arrow = Arrow(n1.get_center(), n2.get_center(), color=color,
                     stroke_width=4, buff=0.5, max_tip_length_to_length_ratio=0.1)
        mid = (n1.get_center() + n2.get_center()) / 2
        badge_color = WARNING_RED if is_negative else EDGE_POSITIVE
        badge_bg = Circle(radius=0.22, fill_color=BACKGROUND_COLOR, fill_opacity=0.95,
                         stroke_color=badge_color, stroke_width=2)
        badge_bg.move_to(mid)
        badge_text = Text(str(weight), font_size=WEIGHT_LABEL_SIZE, 
                         color=WARNING_RED if is_negative else TEXT_PRIMARY)
        badge_text.move_to(mid)
        grp.add(arrow, badge_bg, badge_text)
        grp.arrow = arrow
        grp.is_negative = is_negative
        return grp
    
    def _run_scene(self):
        # Title
        title = Text("Bellman-Ford: The Core Idea", font_size=HEADING_SIZE, color=TEXT_PRIMARY)
        title.move_to(UP * TITLE_Y)
        self.play(Write(title), run_time=NORMAL)
        
        # Core concept - THE key insight
        core = Text("Relax ALL edges, V-1 times", font_size=SUBTITLE_SIZE, 
                   color=TEXT_ACCENT, weight=BOLD)
        core.move_to(UP * 2)
        self.play(Write(core), run_time=SLOW)
        self.wait(PAUSE)
        
        # Simple 4-node graph demonstration
        n0 = self._node("0", LEFT * 3, NODE_SOURCE, 0.4)
        n1 = self._node("1", LEFT * 0.5 + UP * 1, NODE_DEFAULT, 0.4)
        n2 = self._node("2", LEFT * 0.5 + DOWN * 1, NODE_DEFAULT, 0.4)
        n3 = self._node("3", RIGHT * 2, NODE_DEFAULT, 0.4)
        
        nodes = [n0, n1, n2, n3]
        self.play(LaggedStart(*[FadeIn(n) for n in nodes], lag_ratio=0.1), run_time=NORMAL)
        
        # Edges with one negative
        edges = [
            self._edge(n0, n1, 4),
            self._edge(n0, n2, 2),
            self._edge(n1, n2, -1, is_negative=True),
            self._edge(n1, n3, 2),
            self._edge(n2, n3, 3),
        ]
        
        for e in edges:
            self.play(GrowArrow(e.arrow), FadeIn(VGroup(e[1], e[2])), run_time=INSTANT)
        
        # V-1 explanation
        v_text = Text("V = 4 vertices → 3 iterations needed", font_size=LABEL_SIZE, 
                     color=TEXT_SECONDARY)
        v_text.move_to(DOWN * 2)
        self.play(Write(v_text), run_time=NORMAL)
        
        # All edges pulse to show "ALL edges"
        self.play(
            *[e.arrow.animate.set_stroke(width=6, color=ITERATION_BG) for e in edges],
            run_time=NORMAL
        )
        self.play(
            *[e.arrow.animate.set_stroke(width=4, color=EDGE_POSITIVE if not e.is_negative else EDGE_NEGATIVE) for e in edges],
            run_time=NORMAL
        )
        
        compare = Text("Process ALL edges each iteration (not just neighbors)", 
                      font_size=SMALL_SIZE, color=TEXT_ACCENT)
        compare.move_to(DOWN * 2.7)
        self.play(Write(compare), run_time=NORMAL)
        self.wait(PAUSE)
        
        # Clear for relaxation explanation
        self.play(
            FadeOut(v_text), FadeOut(compare),
            *[FadeOut(n) for n in nodes],
            *[FadeOut(e) for e in edges],
            run_time=FAST
        )
        
        # Relaxation explained
        relax_title = Text("Edge Relaxation", font_size=HEADING_SIZE, color=TEXT_PRIMARY)
        relax_title.move_to(UP * 1.5)
        self.play(Write(relax_title), run_time=NORMAL)
        
        # Visual edge u -> v
        u_node = self._node("u", LEFT * 2, NODE_UPDATED, 0.5)
        v_node = self._node("v", RIGHT * 2, NODE_DEFAULT, 0.5)
        uv_edge = self._edge(u_node, v_node, "w")
        
        self.play(FadeIn(u_node), FadeIn(v_node), run_time=FAST)
        self.play(GrowArrow(uv_edge.arrow), FadeIn(VGroup(uv_edge[1], uv_edge[2])), run_time=FAST)
        
        # Condition and update
        condition = Text("If distance[v] > distance[u] + w:", font_size=LABEL_SIZE, 
                        color=TEXT_SECONDARY)
        condition.move_to(DOWN * 0.5)
        
        update = Text("    distance[v] = distance[u] + w  ✓", font_size=LABEL_SIZE, 
                     color=SUCCESS_GREEN)
        update.move_to(DOWN * 1.1)
        
        self.play(Write(condition), run_time=NORMAL)
        self.play(Write(update), run_time=NORMAL)
        self.wait(PAUSE)
        
        # Clear and show V-1 reasoning
        self.play(
            FadeOut(relax_title), FadeOut(condition), FadeOut(update),
            FadeOut(u_node), FadeOut(v_node), FadeOut(uv_edge),
            run_time=FAST
        )
        
        why_title = Text("Why V-1 iterations?", font_size=HEADING_SIZE, color=TEXT_PRIMARY)
        why_title.move_to(UP * 1.5)
        self.play(Write(why_title), run_time=NORMAL)
        
        # Path with 5 nodes showing V-1 edges
        path_nodes = VGroup()
        for i in range(5):
            n = self._node(str(i), LEFT * 3 + RIGHT * 1.5 * i + DOWN * 0.5, NODE_DEFAULT, 0.3)
            path_nodes.add(n)
        path_nodes[0].circle.set_fill(NODE_SOURCE)
        
        self.play(LaggedStart(*[FadeIn(n) for n in path_nodes], lag_ratio=0.1), run_time=NORMAL)
        
        # Connect with arrows
        path_edges = []
        for i in range(4):
            e = Arrow(path_nodes[i].get_center(), path_nodes[i+1].get_center(),
                     color=EDGE_POSITIVE, stroke_width=3, buff=0.35)
            path_edges.append(e)
        
        self.play(*[GrowArrow(e) for e in path_edges], run_time=NORMAL)
        
        explanation = Text("Longest simple path: V-1 edges (no repeated vertices)", 
                          font_size=SMALL_SIZE, color=TEXT_SECONDARY)
        explanation.move_to(DOWN * 2)
        
        count_text = Text("5 vertices → 4 edges max → 4 iterations guarantee correctness", 
                         font_size=SMALL_SIZE, color=TEXT_ACCENT)
        count_text.move_to(DOWN * 2.6)
        
        self.play(Write(explanation), run_time=NORMAL)
        self.play(Write(count_text), run_time=NORMAL)
        self.wait(LONG_PAUSE)
