#!/usr/bin/env python3
"""Scene 4: Negative Cycle Detection"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from manim import *
from config.colors import *
from config.fonts import *
from config.animation_constants import *


class Scene4_NegativeCycle(Scene):
    """Negative Cycle Detection (120s)"""
    
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
        title = Text("Negative Cycle Detection", font_size=HEADING_SIZE, color=TEXT_PRIMARY)
        title.move_to(UP * TITLE_Y)
        self.play(Write(title), run_time=NORMAL)
        
        warning = Text("⚠️ When negative cycles exist...", font_size=BODY_SIZE, 
                      color=WARNING_ORANGE)
        warning.move_to(UP * 2)
        self.play(Write(warning), run_time=NORMAL)
        self.wait(PAUSE)
        self.play(FadeOut(warning), run_time=FAST)
        
        # Cycle graph: A → B → C → A
        a_node = self._node("A", LEFT * 2, NODE_SOURCE, 0.5)
        b_node = self._node("B", RIGHT * 2 + UP * 1.5, NODE_DEFAULT, 0.5)
        c_node = self._node("C", RIGHT * 2 + DOWN * 1.5, NODE_DEFAULT, 0.5)
        
        cycle_nodes = [a_node, b_node, c_node]
        self.play(LaggedStart(*[FadeIn(n) for n in cycle_nodes], lag_ratio=0.1), run_time=NORMAL)
        
        # Edges creating negative cycle
        e_ab = self._edge(a_node, b_node, 2)
        e_bc = self._edge(b_node, c_node, 3)
        e_ca = self._edge(c_node, a_node, -8, is_negative=True)
        
        cycle_edges = [e_ab, e_bc, e_ca]
        for e in cycle_edges:
            self.play(GrowArrow(e.arrow), FadeIn(VGroup(e[1], e[2])), run_time=FAST)
        
        # Show cycle sum
        cycle_sum = Text("Cycle sum: 2 + 3 + (-8) = -3", font_size=LABEL_SIZE, color=WARNING_RED)
        cycle_sum.move_to(DOWN * 2.5)
        self.play(Write(cycle_sum), run_time=NORMAL)
        
        meaning = Text("Negative cycle = Can always find shorter path!", 
                      font_size=SMALL_SIZE, color=WARNING_RED)
        meaning.move_to(DOWN * 3)
        self.play(Write(meaning), run_time=NORMAL)
        self.wait(PAUSE)
        self.play(FadeOut(cycle_sum), FadeOut(meaning), run_time=FAST)
        
        # Distance labels
        distances = {"A": 0, "B": float('inf'), "C": float('inf')}
        dist_labels = {}
        
        for node, name in [(a_node, "A"), (b_node, "B"), (c_node, "C")]:
            d = distances[name]
            d_str = "0" if d == 0 else "∞"
            lbl = Text(d_str, font_size=DISTANCE_SIZE, 
                      color=DIST_INFINITY if d == float('inf') else DIST_FINITE)
            lbl.next_to(node, DOWN, buff=0.3)
            dist_labels[name] = lbl
            self.play(FadeIn(lbl), run_time=INSTANT)
        
        # Iteration 1
        iter_label = Text("Iteration 1", font_size=LABEL_SIZE, color=TEXT_ACCENT)
        iter_label.move_to(UP * 2.5)
        self.play(Write(iter_label), run_time=FAST)
        
        # A→B: 0+2=2
        self.play(e_ab.arrow.animate.set_color(EDGE_CURRENT), run_time=FAST)
        distances["B"] = 2
        new_b = Text("2", font_size=DISTANCE_SIZE, color=DIST_IMPROVING)
        new_b.next_to(b_node, DOWN, buff=0.3)
        self.play(Transform(dist_labels["B"], new_b), run_time=FAST)
        self.play(e_ab.arrow.animate.set_color(EDGE_POSITIVE), run_time=FAST)
        
        # B→C: 2+3=5
        self.play(e_bc.arrow.animate.set_color(EDGE_CURRENT), run_time=FAST)
        distances["C"] = 5
        new_c = Text("5", font_size=DISTANCE_SIZE, color=DIST_IMPROVING)
        new_c.next_to(c_node, DOWN, buff=0.3)
        self.play(Transform(dist_labels["C"], new_c), run_time=FAST)
        self.play(e_bc.arrow.animate.set_color(EDGE_POSITIVE), run_time=FAST)
        
        # C→A: 5+(-8)=-3
        self.play(e_ca.arrow.animate.set_color(EDGE_CURRENT), run_time=FAST)
        distances["A"] = -3
        new_a = Text("-3", font_size=DISTANCE_SIZE, color=WARNING_RED)
        new_a.next_to(a_node, DOWN, buff=0.3)
        self.play(Transform(dist_labels["A"], new_a), run_time=FAST)
        self.play(e_ca.arrow.animate.set_color(EDGE_NEGATIVE), run_time=FAST)
        
        self.wait(PAUSE)
        
        # Iteration 2
        new_iter = Text("Iteration 2", font_size=LABEL_SIZE, color=TEXT_ACCENT)
        new_iter.move_to(UP * 2.5)
        self.play(Transform(iter_label, new_iter), run_time=FAST)
        
        # A→B: -3+2=-1
        self.play(e_ab.arrow.animate.set_color(EDGE_CURRENT), run_time=FAST)
        distances["B"] = -1
        new_b2 = Text("-1", font_size=DISTANCE_SIZE, color=WARNING_RED)
        new_b2.next_to(b_node, DOWN, buff=0.3)
        self.play(Transform(dist_labels["B"], new_b2), run_time=FAST)
        
        # B→C: -1+3=2
        self.play(e_bc.arrow.animate.set_color(EDGE_CURRENT), run_time=FAST)
        distances["C"] = 2
        new_c2 = Text("2", font_size=DISTANCE_SIZE, color=WARNING_ORANGE)
        new_c2.next_to(c_node, DOWN, buff=0.3)
        self.play(Transform(dist_labels["C"], new_c2), run_time=FAST)
        
        # C→A: 2+(-8)=-6
        self.play(e_ca.arrow.animate.set_color(EDGE_CURRENT), run_time=FAST)
        distances["A"] = -6
        new_a2 = Text("-6", font_size=DISTANCE_SIZE, color=WARNING_RED)
        new_a2.next_to(a_node, DOWN, buff=0.3)
        self.play(Transform(dist_labels["A"], new_a2), run_time=FAST)
        
        decreasing = Text("Distances keep decreasing!", font_size=BODY_SIZE, color=WARNING_RED)
        decreasing.move_to(DOWN * 2.5)
        self.play(Write(decreasing), run_time=NORMAL)
        self.wait(PAUSE)
        
        # Detection phase
        detect_iter = Text("Iteration 3 (DETECTION)", font_size=LABEL_SIZE, color=WARNING_RED)
        detect_iter.move_to(UP * 2.5)
        self.play(Transform(iter_label, detect_iter), FadeOut(decreasing), run_time=FAST)
        
        self.play(e_ab.arrow.animate.set_color(EDGE_CURRENT), run_time=FAST)
        
        # ALARM!
        alarm_text = Text("⚠️ NEGATIVE CYCLE DETECTED!", font_size=WARNING_SIZE, 
                         color=WARNING_RED, weight=BOLD)
        alarm_text.move_to(DOWN * 2.5)
        
        self.play(
            Write(alarm_text),
            *[e.arrow.animate.set_color(CYCLE_GLOW).set_stroke(width=8) for e in cycle_edges],
            run_time=NORMAL
        )
        
        # Pulsing effect
        for _ in range(3):
            self.play(
                *[e.arrow.animate.set_stroke(width=10) for e in cycle_edges],
                run_time=0.2
            )
            self.play(
                *[e.arrow.animate.set_stroke(width=6) for e in cycle_edges],
                run_time=0.2
            )
        
        explain = Text("If Vth iteration improves any distance → Negative cycle exists", 
                      font_size=SMALL_SIZE, color=TEXT_SECONDARY)
        explain.move_to(DOWN * 3.3)
        self.play(Write(explain), run_time=NORMAL)
        self.wait(LONG_PAUSE)
