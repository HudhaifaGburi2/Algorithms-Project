#!/usr/bin/env python3
"""Scene 3: Step-by-Step Example - Main Demonstration"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from manim import *
from config.colors import *
from config.fonts import *
from config.animation_constants import *


class Scene3_StepByStep(Scene):
    """Step-by-Step Example (240s) - Main demonstration"""
    
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
        weight_str = str(weight)
        badge_text = Text(weight_str, font_size=WEIGHT_LABEL_SIZE, 
                         color=WARNING_RED if is_negative else TEXT_PRIMARY)
        badge_text.move_to(mid)
        grp.add(arrow, badge_bg, badge_text)
        grp.arrow = arrow
        grp.weight = weight
        grp.is_negative = is_negative
        return grp
    
    def _iteration_counter(self, current, total):
        grp = VGroup()
        bg = RoundedRectangle(width=4, height=0.9, corner_radius=0.15,
                             fill_color=ITERATION_BG, fill_opacity=1,
                             stroke_color=TEXT_PRIMARY, stroke_width=2)
        bg.move_to(UP * 3)
        text = Text(f"ITERATION {current}/{total}", font_size=ITERATION_SIZE,
                   color=ITERATION_TEXT, weight=BOLD)
        text.move_to(bg.get_center())
        grp.add(bg, text)
        return grp
    
    def _calc_box(self, old_dist, edge_weight, new_dist, comparison, success):
        grp = VGroup()
        bg = RoundedRectangle(width=5, height=1.2, corner_radius=0.1,
                             fill_color="#FFFFFF", fill_opacity=0.95,
                             stroke_color=ITERATION_BG, stroke_width=3)
        old_str = "∞" if old_dist == float('inf') else str(old_dist)
        if edge_weight >= 0:
            calc_str = f"{old_str} + {edge_weight} = {new_dist}"
        else:
            calc_str = f"{old_str} + ({edge_weight}) = {new_dist}"
        comp_str = "∞" if comparison == float('inf') else str(comparison)
        if success:
            result = f" < {comp_str} ✓"
            result_color = CALC_SUCCESS
        else:
            result = f" ≥ {comp_str} ✗"
            result_color = CALC_FAIL
        calc_text = Text(calc_str, font_size=CALC_SIZE, color="#1F2937")
        result_text = Text(result, font_size=CALC_SIZE, color=result_color, weight=BOLD)
        full_text = VGroup(calc_text, result_text).arrange(RIGHT, buff=0.1)
        full_text.move_to(bg.get_center())
        grp.add(bg, full_text)
        return grp
    
    def _run_scene(self):
        title = Text("Step-by-Step Example", font_size=HEADING_SIZE, color=TEXT_PRIMARY)
        title.move_to(UP * TITLE_Y)
        self.play(Write(title), run_time=NORMAL)
        self.play(title.animate.scale(0.7).move_to(UP * 3.5), run_time=FAST)
        
        # Graph with 5 vertices
        positions = {
            0: LEFT * 4 + UP * 0.5,
            1: LEFT * 1.5 + UP * 1.5,
            2: LEFT * 1.5 + DOWN * 1,
            3: RIGHT * 1.5 + DOWN * 0.5,
            4: RIGHT * 1.5 + UP * 1.5,
        }
        
        nodes = {}
        for v, pos in positions.items():
            color = NODE_SOURCE if v == 0 else NODE_DEFAULT
            nodes[v] = self._node(str(v), pos, color, 0.4)
        
        self.play(LaggedStart(*[FadeIn(n) for n in nodes.values()], lag_ratio=0.08), 
                 run_time=NORMAL)
        
        # Edges with mixed weights
        edges_data = [
            (0, 1, 6, False),
            (0, 2, 7, False),
            (1, 2, 5, False),
            (1, 3, -4, True),
            (1, 4, 8, False),
            (2, 4, -3, True),
            (3, 2, 9, False),
            (4, 3, 2, False),
        ]
        
        edges = {}
        for u, v, w, neg in edges_data:
            e = self._edge(nodes[u], nodes[v], w, neg)
            edges[(u, v)] = e
        
        for e in edges.values():
            self.play(GrowArrow(e.arrow), run_time=INSTANT)
            self.play(FadeIn(VGroup(e[1], e[2])), run_time=INSTANT)
        
        self.wait(PAUSE)
        
        # Distance table
        distances = {0: 0, 1: float('inf'), 2: float('inf'), 3: float('inf'), 4: float('inf')}
        
        dist_header = Text("DISTANCES", font_size=SMALL_SIZE, color=TEXT_ACCENT, weight=BOLD)
        dist_header.move_to(RIGHT * TABLE_X + UP * 2.5)
        self.play(FadeIn(dist_header), run_time=FAST)
        
        dist_labels = {}
        y = 2.0
        for v in range(5):
            d = distances[v]
            d_str = "∞" if d == float('inf') else str(d)
            d_color = DIST_INFINITY if d == float('inf') else DIST_FINITE
            
            v_text = Text(str(v) + ":", font_size=TINY_SIZE, color=TEXT_PRIMARY)
            v_text.move_to(RIGHT * (TABLE_X - 0.5) + UP * y)
            
            d_text = Text(d_str, font_size=DISTANCE_SIZE, color=d_color, weight=BOLD)
            d_text.move_to(RIGHT * (TABLE_X + 0.5) + UP * y)
            
            self.play(FadeIn(v_text), FadeIn(d_text), run_time=INSTANT)
            dist_labels[v] = d_text
            y -= 0.55
        
        src_label = Text("Source: 0", font_size=SMALL_SIZE, color=NODE_SOURCE)
        src_label.move_to(LEFT * 4 + DOWN * 2.5)
        self.play(Write(src_label), run_time=FAST)
        
        V = 5
        num_iterations = V - 1
        
        iter_counter = self._iteration_counter(1, num_iterations)
        self.play(FadeIn(iter_counter), run_time=ITERATION_TRANSITION)
        
        # Process iterations
        for iteration in range(1, num_iterations + 1):
            if iteration > 1:
                new_counter = self._iteration_counter(iteration, num_iterations)
                self.play(Transform(iter_counter, new_counter), run_time=ITERATION_TRANSITION)
            
            self.wait(0.3)
            speed = RELAXATION_TIME if iteration == 1 else FAST
            
            for (u, v), edge in edges.items():
                original_color = EDGE_NEGATIVE if edge.is_negative else EDGE_POSITIVE
                self.play(edge.arrow.animate.set_color(EDGE_CURRENT).set_stroke(width=6),
                         run_time=EDGE_GLOW_TIME if iteration == 1 else INSTANT)
                
                dist_u = distances[u]
                dist_v = distances[v]
                weight = edge.weight
                
                if dist_u != float('inf'):
                    new_dist = dist_u + weight
                    
                    if new_dist < dist_v:
                        if iteration == 1:
                            calc = self._calc_box(dist_u, weight, new_dist, dist_v, True)
                            calc.move_to(DOWN * 2.8)
                            self.play(FadeIn(calc), run_time=FAST)
                            self.wait(0.3)
                            self.play(FadeOut(calc), run_time=FAST)
                        
                        distances[v] = new_dist
                        
                        new_dist_text = Text(str(new_dist), font_size=DISTANCE_SIZE, 
                                            color=DIST_IMPROVING, weight=BOLD)
                        new_dist_text.move_to(dist_labels[v].get_center())
                        
                        self.play(
                            dist_labels[v].animate.set_color(WARNING_RED),
                            nodes[v].circle.animate.set_fill(NODE_UPDATED),
                            edge.arrow.animate.set_color(EDGE_RELAXED),
                            run_time=speed
                        )
                        self.play(
                            Transform(dist_labels[v], new_dist_text),
                            run_time=DISTANCE_UPDATE_TIME
                        )
                        self.play(
                            nodes[v].circle.animate.set_fill(NODE_DEFAULT if v != 0 else NODE_SOURCE),
                            run_time=FAST
                        )
                    else:
                        self.play(edge.arrow.animate.set_color(EDGE_NO_CHANGE), run_time=INSTANT)
                else:
                    self.play(edge.arrow.animate.set_color(EDGE_NO_CHANGE), run_time=INSTANT)
                
                self.play(
                    edge.arrow.animate.set_color(original_color).set_stroke(width=4),
                    run_time=INSTANT
                )
            
            self.wait(0.3)
        
        # Detection check
        detect_counter = VGroup()
        detect_bg = RoundedRectangle(width=4, height=0.9, corner_radius=0.15,
                                    fill_color=WARNING_ORANGE, fill_opacity=1,
                                    stroke_color=TEXT_PRIMARY, stroke_width=2)
        detect_bg.move_to(UP * 3)
        detect_text = Text("CYCLE CHECK", font_size=ITERATION_SIZE,
                          color=ITERATION_TEXT, weight=BOLD)
        detect_text.move_to(detect_bg.get_center())
        detect_counter.add(detect_bg, detect_text)
        
        self.play(Transform(iter_counter, detect_counter), run_time=ITERATION_TRANSITION)
        
        detect_label = Text("Checking for negative cycles...", font_size=SMALL_SIZE, 
                           color=WARNING_ORANGE)
        detect_label.move_to(DOWN * 2.5)
        self.play(Write(detect_label), run_time=NORMAL)
        
        for (u, v), edge in edges.items():
            self.play(edge.arrow.animate.set_color(EDGE_CURRENT), run_time=INSTANT)
            self.play(edge.arrow.animate.set_color(EDGE_NO_CHANGE), run_time=INSTANT)
        
        success_text = Text("✓ No updates = No negative cycle!", font_size=BODY_SIZE, 
                           color=SUCCESS_GREEN)
        success_text.move_to(DOWN * 3)
        self.play(FadeOut(detect_label), Write(success_text), run_time=NORMAL)
        
        # Final result
        final_box = VGroup()
        final_bg = RoundedRectangle(width=3.5, height=2.2, corner_radius=0.15,
                                   fill_color=SUCCESS_GREEN, fill_opacity=0.2,
                                   stroke_color=SUCCESS_GREEN, stroke_width=2)
        final_bg.move_to(RIGHT * 4.5 + DOWN * 0.5)
        final_title = Text("SHORTEST PATHS", font_size=SMALL_SIZE, color=SUCCESS_GREEN, weight=BOLD)
        final_title.move_to(final_bg.get_center() + UP * 0.7)
        final_box.add(final_bg, final_title)
        
        self.play(FadeIn(final_box), run_time=NORMAL)
        self.wait(LONG_PAUSE)
