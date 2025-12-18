#!/usr/bin/env python3
"""Scene 6: Implementation Code"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from manim import *
from config.colors import *
from config.fonts import *
from config.animation_constants import *


class Scene6_Implementation(Scene):
    """Implementation Code (90s)"""
    
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        self._run_scene()
    
    def _run_scene(self):
        title = Text("Python Implementation", font_size=HEADING_SIZE, color=TEXT_PRIMARY)
        title.move_to(UP * TITLE_Y)
        self.play(Write(title), run_time=NORMAL)
        self.play(title.animate.scale(0.7).move_to(UP * 3.5), run_time=FAST)
        
        # Code sections as text (more reliable than Code mobject)
        code_lines = [
            ("def bellman_ford(graph, V, src):", TEXT_ACCENT),
            ("    dist = [float('inf')] * V", TEXT_PRIMARY),
            ("    dist[src] = 0", TEXT_PRIMARY),
            ("", TEXT_PRIMARY),
            ("    # Relax edges V-1 times", TEXT_SECONDARY),
            ("    for i in range(V - 1):", SUCCESS_GREEN),
            ("        for u, v, w in graph:", SUCCESS_GREEN),
            ("            if dist[u] != float('inf'):", TEXT_PRIMARY),
            ("                if dist[u] + w < dist[v]:", ITERATION_BG),
            ("                    dist[v] = dist[u] + w", ITERATION_BG),
            ("", TEXT_PRIMARY),
            ("    # Check for negative cycle", WARNING_RED),
            ("    for u, v, w in graph:", WARNING_RED),
            ("        if dist[u] + w < dist[v]:", WARNING_RED),
            ("            return 'Negative cycle!'", WARNING_RED),
            ("", TEXT_PRIMARY),
            ("    return dist", SUCCESS_GREEN),
        ]
        
        code_group = VGroup()
        y_pos = 2.5
        for line, color in code_lines:
            if line:
                text = Text(line, font_size=CODE_SIZE, color=color, font="monospace")
                text.move_to(LEFT * 2 + UP * y_pos)
                text.align_to(LEFT * 5, LEFT)
                code_group.add(text)
            y_pos -= 0.35
        
        # Animate code appearing in sections
        # Section 1: Function def and init (lines 0-2)
        init_section = VGroup(*[code_group[i] for i in range(3)])
        self.play(Write(init_section), run_time=NORMAL)
        
        init_note = Text("Initialize: source=0, others=∞", font_size=TINY_SIZE, color=TEXT_ACCENT)
        init_note.move_to(RIGHT * 4 + UP * 2)
        self.play(FadeIn(init_note), run_time=FAST)
        self.wait(PAUSE)
        
        # Section 2: Main loop (lines 3-9)
        main_section = VGroup(*[code_group[i] for i in range(3, 10)])
        self.play(Write(main_section), run_time=NORMAL)
        
        main_note = Text("Core: V-1 iterations over ALL edges", font_size=TINY_SIZE, color=SUCCESS_GREEN)
        main_note.move_to(RIGHT * 4 + UP * 0.5)
        self.play(FadeIn(main_note), run_time=FAST)
        self.wait(PAUSE)
        
        # Section 3: Detection (lines 10-14)
        detect_section = VGroup(*[code_group[i] for i in range(10, 15)])
        self.play(Write(detect_section), run_time=NORMAL)
        
        detect_note = Text("Detection: Vth iteration check", font_size=TINY_SIZE, color=WARNING_RED)
        detect_note.move_to(RIGHT * 4 + DOWN * 1.5)
        self.play(FadeIn(detect_note), run_time=FAST)
        self.wait(PAUSE)
        
        # Section 4: Return
        return_section = VGroup(*[code_group[i] for i in range(15, 17)])
        self.play(Write(return_section), run_time=FAST)
        
        # Highlight key insight
        key_box = VGroup()
        key_bg = RoundedRectangle(width=5.5, height=1.2, corner_radius=0.1,
                                 fill_color=ITERATION_BG, fill_opacity=0.2,
                                 stroke_color=ITERATION_BG, stroke_width=2)
        key_bg.move_to(DOWN * 3)
        key_text = Text("Key: Relaxation condition", font_size=SMALL_SIZE, color=TEXT_PRIMARY)
        key_formula = Text("dist[u] + w < dist[v]", font_size=LABEL_SIZE, color=ITERATION_BG)
        key_text.move_to(key_bg.get_center() + UP * 0.25)
        key_formula.move_to(key_bg.get_center() + DOWN * 0.2)
        key_box.add(key_bg, key_text, key_formula)
        
        self.play(FadeIn(key_box), run_time=NORMAL)
        self.wait(LONG_PAUSE)
