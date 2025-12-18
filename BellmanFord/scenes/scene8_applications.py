#!/usr/bin/env python3
"""Scene 8: Real-World Applications"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from manim import *
from config.colors import *
from config.fonts import *
from config.animation_constants import *


class Scene8_Applications(Scene):
    """Real-World Applications (60s)"""
    
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        self._run_scene()
    
    def _run_scene(self):
        title = Text("Real-World Applications", font_size=HEADING_SIZE, color=TEXT_PRIMARY)
        title.move_to(UP * TITLE_Y)
        self.play(Write(title), run_time=NORMAL)
        
        # Applications list
        apps = [
            ("Network Routing (RIP)", "Distance-vector routing protocol", BELLMAN_COLOR),
            ("Currency Arbitrage", "Detect profitable exchange cycles", WARNING_ORANGE),
            ("Financial Modeling", "Costs (+) and gains (-) analysis", TEXT_ACCENT),
        ]
        
        items = VGroup()
        for app_title, desc, color in apps:
            # Title
            title_text = Text(app_title, font_size=LABEL_SIZE, color=color, weight=BOLD)
            # Description
            desc_text = Text(desc, font_size=SMALL_SIZE, color=TEXT_SECONDARY)
            desc_text.next_to(title_text, DOWN, buff=0.1, aligned_edge=LEFT)
            item = VGroup(title_text, desc_text)
            items.add(item)
        
        items.arrange(DOWN, buff=0.6, aligned_edge=LEFT)
        items.move_to(LEFT * 1 + UP * 0.5)
        
        self.play(
            LaggedStart(*[FadeIn(item, shift=RIGHT * 0.3) for item in items], lag_ratio=0.3),
            run_time=SLOW
        )
        self.wait(PAUSE)
        
        # Currency arbitrage example
        currency_box = VGroup()
        curr_bg = RoundedRectangle(width=5.5, height=2, corner_radius=0.15,
                                  fill_color=WARNING_ORANGE, fill_opacity=0.1,
                                  stroke_color=WARNING_ORANGE, stroke_width=2)
        curr_bg.move_to(DOWN * 2)
        
        curr_title = Text("Currency Arbitrage Example", font_size=SMALL_SIZE, 
                         color=WARNING_ORANGE, weight=BOLD)
        curr_title.move_to(curr_bg.get_center() + UP * 0.6)
        
        curr_example = Text("$100 → €92 → £80 → $103", font_size=LABEL_SIZE, color=TEXT_PRIMARY)
        curr_example.move_to(curr_bg.get_center())
        
        curr_result = Text("Negative cycle = $3 profit!", font_size=SMALL_SIZE, color=SUCCESS_GREEN)
        curr_result.move_to(curr_bg.get_center() + DOWN * 0.5)
        
        currency_box.add(curr_bg, curr_title, curr_example, curr_result)
        
        self.play(FadeIn(currency_box), run_time=NORMAL)
        self.wait(PAUSE)
        
        # Key insight
        insight = Text("Bellman-Ford detects these opportunities!", 
                      font_size=BODY_SIZE, color=SUCCESS_GREEN)
        insight.move_to(DOWN * 3.5)
        self.play(Write(insight), run_time=NORMAL)
        self.wait(LONG_PAUSE)
