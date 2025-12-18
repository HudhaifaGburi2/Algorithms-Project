#!/usr/bin/env python3
"""Scene 10: Final Recap"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from manim import *
from config.colors import *
from config.fonts import *
from config.animation_constants import *


class Scene10_Recap(Scene):
    """Final Recap (45s)"""
    
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        self._run_scene()
    
    def _run_scene(self):
        title = Text("Key Takeaways", font_size=HEADING_SIZE, color=TEXT_PRIMARY)
        title.move_to(UP * TITLE_Y)
        self.play(Write(title), run_time=NORMAL)
        
        # Four key cards
        cards_data = [
            ("Handles Negative Weights", EDGE_NEGATIVE, "✓"),
            ("Relaxes ALL edges V-1 times", ITERATION_BG, "∀"),
            ("Detects Negative Cycles", WARNING_RED, "⚠"),
            ("Guarantees Correctness", SUCCESS_GREEN, "✓"),
        ]
        
        cards = VGroup()
        for text, color, icon in cards_data:
            card = VGroup()
            bg = RoundedRectangle(width=3, height=1.5, corner_radius=0.15,
                                 fill_color=color, fill_opacity=0.2,
                                 stroke_color=color, stroke_width=2)
            
            icon_text = Text(icon, font_size=HEADING_SIZE, color=color)
            icon_text.move_to(bg.get_center() + UP * 0.25)
            
            label = Text(text, font_size=TINY_SIZE, color=TEXT_PRIMARY)
            label.move_to(bg.get_center() + DOWN * 0.4)
            
            card.add(bg, icon_text, label)
            cards.add(card)
        
        cards.arrange_in_grid(rows=2, cols=2, buff=0.4)
        cards.move_to(UP * 0.5)
        
        self.play(
            LaggedStart(*[FadeIn(card, scale=0.8) for card in cards], lag_ratio=0.15),
            run_time=SLOW
        )
        self.wait(PAUSE)
        
        # Final message
        final_box = VGroup()
        final_bg = RoundedRectangle(width=8, height=1.5, corner_radius=0.15,
                                   fill_color=BELLMAN_COLOR, fill_opacity=0.2,
                                   stroke_color=BELLMAN_COLOR, stroke_width=3)
        final_bg.move_to(DOWN * 2.3)
        
        final_title = Text("BELLMAN-FORD", font_size=HEADING_SIZE, 
                          color=BELLMAN_COLOR, weight=BOLD)
        final_title.move_to(final_bg.get_center() + UP * 0.25)
        
        final_subtitle = Text("When correctness matters more than speed", 
                             font_size=SMALL_SIZE, color=TEXT_SECONDARY)
        final_subtitle.move_to(final_bg.get_center() + DOWN * 0.35)
        
        final_box.add(final_bg, final_title, final_subtitle)
        
        self.play(FadeIn(final_box), run_time=NORMAL)
        self.wait(PAUSE)
        
        # Comparison reminder
        vs_text = Text("Dijkstra = Fast | Bellman-Ford = Versatile", 
                      font_size=LABEL_SIZE, color=TEXT_ACCENT)
        vs_text.move_to(DOWN * 3.5)
        self.play(Write(vs_text), run_time=NORMAL)
        self.wait(LONG_PAUSE)
