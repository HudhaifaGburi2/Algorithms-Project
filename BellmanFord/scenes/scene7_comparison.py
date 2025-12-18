#!/usr/bin/env python3
"""Scene 7: Bellman-Ford vs Dijkstra's Comparison"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from manim import *
from config.colors import *
from config.fonts import *
from config.animation_constants import *


class Scene7_Comparison(Scene):
    """Bellman-Ford vs Dijkstra's (75s)"""
    
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        self._run_scene()
    
    def _run_scene(self):
        title = Text("Bellman-Ford vs Dijkstra's", font_size=HEADING_SIZE, color=TEXT_PRIMARY)
        title.move_to(UP * TITLE_Y)
        self.play(Write(title), run_time=NORMAL)
        
        # Headers
        headers = ["", "Dijkstra's", "Bellman-Ford"]
        header_grp = VGroup()
        for i, h in enumerate(headers):
            color = TEXT_PRIMARY if i == 0 else (DIJKSTRA_COLOR if i == 1 else BELLMAN_COLOR)
            h_text = Text(h, font_size=LABEL_SIZE, color=color, weight=BOLD)
            h_text.move_to(LEFT * 2 + RIGHT * 2.5 * i + UP * 2)
            header_grp.add(h_text)
        
        self.play(LaggedStart(*[Write(h) for h in header_grp], lag_ratio=0.1), run_time=NORMAL)
        
        # Comparison rows
        rows = [
            ("Negative edges", "✗ No", "✓ Yes"),
            ("Cycle detection", "✗ No", "✓ Yes"),
            ("Time Complexity", "O(E log V)", "O(VE)"),
            ("Approach", "Greedy", "Dynamic Prog"),
            ("Speed", "Faster", "Slower"),
        ]
        
        y = 1.3
        for feature, dijk, bf in rows:
            row_grp = VGroup()
            
            f_text = Text(feature, font_size=SMALL_SIZE, color=TEXT_SECONDARY)
            f_text.move_to(LEFT * 2 + UP * y)
            
            d_color = WARNING_RED if "✗" in dijk else TEXT_PRIMARY
            d_text = Text(dijk, font_size=SMALL_SIZE, color=d_color)
            d_text.move_to(LEFT * 2 + RIGHT * 2.5 + UP * y)
            
            b_color = SUCCESS_GREEN if "✓" in bf else TEXT_PRIMARY
            b_text = Text(bf, font_size=SMALL_SIZE, color=b_color)
            b_text.move_to(LEFT * 2 + RIGHT * 5 + UP * y)
            
            row_grp.add(f_text, d_text, b_text)
            self.play(FadeIn(row_grp), run_time=FAST)
            y -= 0.55
        
        self.wait(PAUSE)
        
        # Decision tree
        decision_title = Text("When to use which?", font_size=BODY_SIZE, color=TEXT_ACCENT)
        decision_title.move_to(DOWN * 1.8)
        self.play(Write(decision_title), run_time=NORMAL)
        
        decision1 = Text("Has negative edges? → Bellman-Ford", font_size=SMALL_SIZE, color=BELLMAN_COLOR)
        decision1.move_to(DOWN * 2.4)
        
        decision2 = Text("All positive weights? → Dijkstra's (faster)", font_size=SMALL_SIZE, color=DIJKSTRA_COLOR)
        decision2.move_to(DOWN * 2.9)
        
        decision3 = Text("Need cycle detection? → Bellman-Ford", font_size=SMALL_SIZE, color=BELLMAN_COLOR)
        decision3.move_to(DOWN * 3.4)
        
        self.play(Write(decision1), run_time=NORMAL)
        self.play(Write(decision2), run_time=NORMAL)
        self.play(Write(decision3), run_time=NORMAL)
        self.wait(LONG_PAUSE)
