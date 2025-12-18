#!/usr/bin/env python3
"""Scene 9: Time Complexity Analysis"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from manim import *
from config.colors import *
from config.fonts import *
from config.animation_constants import *


class Scene9_Complexity(Scene):
    """Time Complexity Analysis (45s)"""
    
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        self._run_scene()
    
    def _run_scene(self):
        title = Text("Time Complexity", font_size=HEADING_SIZE, color=TEXT_PRIMARY)
        title.move_to(UP * TITLE_Y)
        self.play(Write(title), run_time=NORMAL)
        
        # Breakdown
        outer = Text("Outer loop: V-1 iterations", font_size=LABEL_SIZE, color=TEXT_ACCENT)
        outer_o = Text("→ O(V)", font_size=LABEL_SIZE, color=SUCCESS_GREEN)
        outer_o.next_to(outer, RIGHT, buff=0.3)
        outer_grp = VGroup(outer, outer_o)
        outer_grp.move_to(UP * 1.5)
        
        inner = Text("Inner loop: Process all E edges", font_size=LABEL_SIZE, color=TEXT_ACCENT)
        inner_o = Text("→ O(E)", font_size=LABEL_SIZE, color=SUCCESS_GREEN)
        inner_o.next_to(inner, RIGHT, buff=0.3)
        inner_grp = VGroup(inner, inner_o)
        inner_grp.move_to(UP * 0.8)
        
        total = Text("Total: O(V × E) = O(VE)", font_size=BODY_SIZE, color=SUCCESS_GREEN, weight=BOLD)
        total.move_to(UP * 0)
        
        self.play(Write(outer_grp), run_time=NORMAL)
        self.play(Write(inner_grp), run_time=NORMAL)
        self.play(Write(total), run_time=NORMAL)
        self.wait(PAUSE)
        
        # Comparison visualization
        compare_title = Text("Comparison", font_size=LABEL_SIZE, color=TEXT_PRIMARY)
        compare_title.move_to(DOWN * 1)
        self.play(Write(compare_title), run_time=FAST)
        
        # Simple visual comparison
        dijk_bar = VGroup()
        dijk_rect = Rectangle(width=2, height=0.5, fill_color=DIJKSTRA_COLOR, 
                             fill_opacity=0.8, stroke_width=0)
        dijk_rect.move_to(LEFT * 1.5 + DOWN * 1.8)
        dijk_label = Text("Dijkstra: O(E log V)", font_size=TINY_SIZE, color=TEXT_PRIMARY)
        dijk_label.next_to(dijk_rect, RIGHT, buff=0.3)
        dijk_bar.add(dijk_rect, dijk_label)
        
        bf_bar = VGroup()
        bf_rect = Rectangle(width=4, height=0.5, fill_color=BELLMAN_COLOR, 
                           fill_opacity=0.8, stroke_width=0)
        bf_rect.move_to(DOWN * 2.5)
        bf_rect.align_to(dijk_rect, LEFT)
        bf_label = Text("Bellman-Ford: O(VE)", font_size=TINY_SIZE, color=TEXT_PRIMARY)
        bf_label.next_to(bf_rect, RIGHT, buff=0.3)
        bf_bar.add(bf_rect, bf_label)
        
        self.play(FadeIn(dijk_bar), run_time=FAST)
        self.play(FadeIn(bf_bar), run_time=FAST)
        self.wait(PAUSE)
        
        # Trade-off message
        tradeoff = Text("Trade-off: Slower, but handles negative weights", 
                       font_size=BODY_SIZE, color=TEXT_ACCENT)
        tradeoff.move_to(DOWN * 3.3)
        self.play(Write(tradeoff), run_time=NORMAL)
        self.wait(LONG_PAUSE)
