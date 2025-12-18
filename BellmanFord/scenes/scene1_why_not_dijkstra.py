#!/usr/bin/env python3
"""Scene 1: Why Not Dijkstra's? - Problem Introduction"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from manim import *
from config.colors import *
from config.fonts import *
from config.animation_constants import *


class Scene1_WhyNotDijkstra(Scene):
    """The Problem - Why Not Dijkstra's? (90s)"""
    
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
        title = Text("The Problem with Dijkstra's", font_size=TITLE_SIZE, color=TEXT_PRIMARY)
        title.move_to(UP * 2.8)
        self.play(Write(title), run_time=SLOW)
        self.wait(PAUSE)
        
        subtitle = Text("Negative weights break the algorithm", font_size=SUBTITLE_SIZE, 
                       color=WARNING_RED)
        subtitle.next_to(title, DOWN, buff=0.3)
        self.play(FadeIn(subtitle, shift=UP * 0.2), run_time=NORMAL)
        self.wait(PAUSE)
        
        self.play(
            title.animate.scale(0.6).move_to(UP * 3.4),
            FadeOut(subtitle),
            run_time=NORMAL
        )
        
        # Example graph
        book = self._node("Book", LEFT * 4 + UP * 0.5, NODE_SOURCE, 0.4)
        lp = self._node("LP", LEFT * 1 + UP * 1.2, NODE_DEFAULT, 0.4)
        poster = self._node("Post", LEFT * 1 + DOWN * 1.2, NODE_DEFAULT, 0.4)
        piano = self._node("Piano", RIGHT * 2 + UP * 0.5, NODE_DEFAULT, 0.4)
        
        nodes = [book, lp, poster, piano]
        self.play(LaggedStart(*[FadeIn(n) for n in nodes], lag_ratio=0.1), run_time=NORMAL)
        
        # Edges
        e_book_lp = self._edge(book, lp, 5)
        e_book_poster = self._edge(book, poster, 0)
        e_lp_piano = self._edge(lp, piano, 30)
        e_poster_lp = self._edge(poster, lp, -7, is_negative=True)
        e_poster_piano = self._edge(poster, piano, 35)
        
        edges = [e_book_lp, e_book_poster, e_lp_piano, e_poster_lp, e_poster_piano]
        for e in edges:
            self.play(GrowArrow(e.arrow), run_time=INSTANT)
            self.play(FadeIn(VGroup(e[1], e[2])), run_time=INSTANT)
        
        neg_label = Text("Negative edge!", font_size=SMALL_SIZE, color=WARNING_RED)
        neg_label.next_to(e_poster_lp, LEFT, buff=0.3)
        self.play(e_poster_lp.arrow.animate.set_stroke(width=6), Write(neg_label), run_time=NORMAL)
        self.wait(PAUSE)
        
        # Dijkstra result
        dijk_box = VGroup()
        dijk_bg = RoundedRectangle(width=4.5, height=1.5, corner_radius=0.1,
                                  fill_color=DIJKSTRA_COLOR, fill_opacity=0.2,
                                  stroke_color=DIJKSTRA_COLOR, stroke_width=2)
        dijk_bg.move_to(RIGHT * 4.5 + UP * 1.5)
        dijk_title = Text("Dijkstra's says:", font_size=SMALL_SIZE, color=DIJKSTRA_COLOR)
        dijk_result = Text("Book→LP→Piano = $35", font_size=TINY_SIZE, color=TEXT_SECONDARY)
        dijk_title.move_to(dijk_bg.get_center() + UP * 0.3)
        dijk_result.move_to(dijk_bg.get_center() + DOWN * 0.2)
        dijk_box.add(dijk_bg, dijk_title, dijk_result)
        self.play(FadeIn(dijk_box), run_time=NORMAL)
        self.wait(PAUSE)
        
        # Actual best
        actual_box = VGroup()
        actual_bg = RoundedRectangle(width=4.5, height=1.5, corner_radius=0.1,
                                    fill_color=SUCCESS_GREEN, fill_opacity=0.2,
                                    stroke_color=SUCCESS_GREEN, stroke_width=2)
        actual_bg.move_to(RIGHT * 4.5 + DOWN * 0.8)
        actual_title = Text("Actually best:", font_size=SMALL_SIZE, color=SUCCESS_GREEN)
        actual_result = Text("Book→Post→LP→Piano = $28", font_size=TINY_SIZE, color=TEXT_SECONDARY)
        actual_title.move_to(actual_bg.get_center() + UP * 0.3)
        actual_result.move_to(actual_bg.get_center() + DOWN * 0.2)
        actual_box.add(actual_bg, actual_title, actual_result)
        self.play(FadeIn(actual_box), run_time=NORMAL)
        
        self.play(
            e_book_poster.arrow.animate.set_color(SUCCESS_GREEN),
            e_poster_lp.arrow.animate.set_color(SUCCESS_GREEN),
            e_lp_piano.arrow.animate.set_color(SUCCESS_GREEN),
            run_time=NORMAL
        )
        self.wait(PAUSE)
        
        # Clear and show needs
        self.play(
            FadeOut(VGroup(dijk_box, actual_box, neg_label)),
            *[FadeOut(n) for n in nodes],
            *[FadeOut(e) for e in edges],
            run_time=FAST
        )
        
        need_title = Text("We need an algorithm that:", font_size=BODY_SIZE, color=TEXT_PRIMARY)
        need_title.move_to(UP * 1.5)
        
        needs = [
            ("✓", "Handles negative weights", SUCCESS_GREEN),
            ("✓", "Detects negative cycles", SUCCESS_GREEN),
            ("✓", "Guarantees correct answer", SUCCESS_GREEN),
        ]
        
        need_items = VGroup()
        for check, text, color in needs:
            check_text = Text(check, font_size=BODY_SIZE, color=color)
            desc = Text(text, font_size=LABEL_SIZE, color=TEXT_SECONDARY)
            desc.next_to(check_text, RIGHT, buff=0.2)
            item = VGroup(check_text, desc)
            need_items.add(item)
        
        need_items.arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        need_items.move_to(UP * 0.3)
        
        self.play(Write(need_title), run_time=NORMAL)
        self.play(LaggedStart(*[FadeIn(item, shift=LEFT * 0.3) for item in need_items], 
                             lag_ratio=0.2), run_time=NORMAL)
        self.wait(PAUSE)
        
        bf_title = Text("BELLMAN-FORD", font_size=TITLE_SIZE, color=BELLMAN_COLOR, weight=BOLD)
        bf_title.move_to(DOWN * 1.8)
        self.play(Write(bf_title), run_time=SLOW)
        self.wait(LONG_PAUSE)
