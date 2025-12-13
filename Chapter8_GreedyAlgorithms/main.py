#!/usr/bin/env python3
"""
Chapter 8: Greedy Algorithms
============================
Educational animation demonstrating greedy strategy, approximation algorithms,
and NP-complete problems.
3Blue1Brown-style with smooth motion, clear visuals, and minimal text.

Usage:
    manim -pql main.py Chapter8Animation    # Preview (480p)
    manim -pqh main.py Chapter8Animation    # HD quality (1080p)
"""
import sys
sys.path.insert(0, '/home/hg/Desktop/algorthims/Chapter8_GreedyAlgorithms')

from manim import *

from config.colors import (
    BACKGROUND_COLOR, TEXT_PRIMARY, TEXT_SECONDARY, TEXT_ACCENT,
    GREEDY_CHOICE, SELECTED_ITEM, REJECTED_ITEM, AVAILABLE_ITEM,
    EXPONENTIAL_DANGER, APPROXIMATION, EXACT_SOLUTION,
    SET_A_COLOR, SET_B_COLOR, INTERSECTION_COLOR,
    STATE_COVERED, STATE_UNCOVERED, STATION_COLOR
)
from config.fonts import (
    TITLE_SIZE, SUBTITLE_SIZE, HEADING_SIZE, BODY_SIZE,
    LABEL_SIZE, SMALL_SIZE, TINY_SIZE, VALUE_SIZE, WARNING_SIZE
)
from config.animation_constants import (
    INSTANT, FAST, NORMAL, SLOW, GREEDY_SELECT, ELIMINATION,
    PAUSE, LONG_PAUSE, TITLE_Y
)


class Chapter8Animation(Scene):
    """
    Complete Chapter 8 animation covering:
    1. Classroom Scheduling (greedy works perfectly)
    2. Knapsack Problem (greedy is approximate)
    3. Set Covering (greedy approximation)
    4. Set Operations (union, intersection, difference)
    5. Traveling Salesperson (NP-complete)
    6. NP-Complete Recognition
    7. Summary
    """
    
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        
        self._intro_scene()
        self._clear()
        
        self._classroom_scene()
        self._clear()
        
        self._knapsack_scene()
        self._clear()
        
        self._set_covering_scene()
        self._clear()
        
        self._tsp_scene()
        self._clear()
        
        self._np_complete_scene()
        self._clear()
        
        self._summary_scene()
    
    def _clear(self):
        if self.mobjects:
            self.play(*[FadeOut(m) for m in self.mobjects], run_time=FAST)
        self.wait(0.2)
    
    # ==================== HELPERS ====================
    
    def _title(self, text, y=TITLE_Y):
        t = Text(text, font_size=HEADING_SIZE, color=TEXT_PRIMARY)
        t.move_to(UP * y)
        return t
    
    def _class_block(self, name, start, end, y_offset=0, color=AVAILABLE_ITEM):
        """Create a class block for timeline."""
        grp = VGroup()
        
        # Timeline spans 9am-12pm (3 hours) over width 10
        hour_width = 10 / 3
        x_start = (start - 9) * hour_width - 5
        width = (end - start) * hour_width
        
        rect = Rectangle(
            width=width, height=0.5,
            fill_color=color, fill_opacity=0.8,
            stroke_color=TEXT_PRIMARY, stroke_width=2
        )
        rect.move_to(RIGHT * (x_start + width/2) + UP * y_offset)
        
        label = Text(name, font_size=14, color=TEXT_PRIMARY)
        label.move_to(rect.get_center())
        
        end_label = Text(f"{int(end)}:00", font_size=12, color=TEXT_PRIMARY)
        end_label.next_to(rect, UR, buff=0.05)
        
        grp.add(rect, label, end_label)
        grp.rect = rect
        grp.end_time = end
        return grp
    
    def _item_card(self, name, value, weight, color=AVAILABLE_ITEM):
        """Create item card for knapsack."""
        grp = VGroup()
        
        box = RoundedRectangle(
            width=2.0, height=1.0, corner_radius=0.1,
            fill_color=color, fill_opacity=0.8,
            stroke_color=TEXT_PRIMARY, stroke_width=2
        )
        
        name_text = Text(name, font_size=SMALL_SIZE, color=TEXT_PRIMARY)
        name_text.move_to(box.get_center() + UP * 0.2)
        
        val_text = Text(f"${value}", font_size=TINY_SIZE, color=GREEDY_CHOICE)
        wgt_text = Text(f"{weight}lb", font_size=TINY_SIZE, color=TEXT_SECONDARY)
        val_text.move_to(box.get_center() + DOWN * 0.2 + LEFT * 0.4)
        wgt_text.move_to(box.get_center() + DOWN * 0.2 + RIGHT * 0.4)
        
        grp.add(box, name_text, val_text, wgt_text)
        grp.box = box
        grp.value = value
        grp.weight = weight
        return grp
    
    # ==================== SCENE 1: INTRO ====================
    
    def _intro_scene(self):
        """Introduction to greedy algorithms."""
        title = Text("Chapter 8: Greedy Algorithms", font_size=TITLE_SIZE, color=TEXT_PRIMARY)
        title.move_to(UP * 2)
        self.play(Write(title), run_time=SLOW)
        self.wait(PAUSE)
        
        subtitle = Text("Pick the best choice at each step", font_size=SUBTITLE_SIZE, color=GREEDY_CHOICE)
        subtitle.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(subtitle, shift=UP * 0.3), run_time=NORMAL)
        self.wait(PAUSE)
        
        self.play(
            title.animate.scale(0.6).move_to(UP * 3.3),
            FadeOut(subtitle),
            run_time=NORMAL
        )
        
        # Three concepts
        concepts = [
            ("Greedy Strategy", "Locally optimal choices", GREEDY_CHOICE),
            ("Approximation", "Good enough solutions", APPROXIMATION),
            ("NP-Complete", "Fundamentally hard", EXPONENTIAL_DANGER),
        ]
        
        cards = VGroup()
        for name, desc, color in concepts:
            card = VGroup()
            bg = RoundedRectangle(width=3.5, height=1.5, corner_radius=0.1,
                                 fill_color=color, fill_opacity=0.2,
                                 stroke_color=color, stroke_width=3)
            name_text = Text(name, font_size=LABEL_SIZE, color=color)
            name_text.move_to(bg.get_center() + UP * 0.3)
            desc_text = Text(desc, font_size=TINY_SIZE, color=TEXT_SECONDARY)
            desc_text.move_to(bg.get_center() + DOWN * 0.3)
            card.add(bg, name_text, desc_text)
            cards.add(card)
        
        cards.arrange(RIGHT, buff=0.5)
        cards.move_to(UP * 0.5)
        
        self.play(
            LaggedStart(*[FadeIn(c, shift=UP * 0.3) for c in cards], lag_ratio=0.2),
            run_time=NORMAL
        )
        self.wait(LONG_PAUSE)
    
    # ==================== SCENE 2: CLASSROOM SCHEDULING ====================
    
    def _classroom_scene(self):
        """Classroom scheduling - greedy works perfectly."""
        title = self._title("Classroom Scheduling")
        self.play(Write(title), run_time=NORMAL)
        
        problem = Text("Maximize classes without conflicts", font_size=BODY_SIZE, color=TEXT_SECONDARY)
        problem.move_to(UP * 2.2)
        self.play(Write(problem), run_time=FAST)
        
        # Timeline
        timeline = Line(LEFT * 5, RIGHT * 5, color=TEXT_SECONDARY, stroke_width=2)
        timeline.move_to(UP * 1)
        
        time_labels = VGroup()
        for hour in [9, 10, 11, 12]:
            x = (hour - 9) * (10/3) - 5
            label = Text(f"{hour}am" if hour < 12 else "12pm", font_size=12, color=TEXT_SECONDARY)
            label.move_to(RIGHT * x + UP * 0.6)
            time_labels.add(label)
        
        self.play(Create(timeline), Write(time_labels), run_time=FAST)
        
        # Classes (with overlaps)
        classes = [
            ("Art", 9.0, 10.0, 0.3),
            ("Eng", 9.5, 10.5, -0.3),
            ("Math", 10.0, 11.0, 0.3),
            ("CS", 10.5, 11.5, -0.3),
            ("Music", 11.0, 12.0, 0.3),
        ]
        
        class_blocks = {}
        for name, start, end, y_off in classes:
            block = self._class_block(name, start, end, y_off)
            block.shift(UP * 1)
            class_blocks[name] = block
        
        self.play(
            LaggedStart(*[FadeIn(b) for b in class_blocks.values()], lag_ratio=0.1),
            run_time=NORMAL
        )
        self.wait(PAUSE)
        
        # Strategy
        strategy = Text("Strategy: Pick class that ends SOONEST", font_size=LABEL_SIZE, color=GREEDY_CHOICE)
        strategy.move_to(DOWN * 0.5)
        self.play(Write(strategy), run_time=FAST)
        self.wait(PAUSE)
        
        # Selected collection
        selected_label = Text("Selected:", font_size=SMALL_SIZE, color=SELECTED_ITEM)
        selected_label.move_to(DOWN * 1.5 + LEFT * 4)
        self.play(Write(selected_label), run_time=FAST)
        
        # Step 1: Art (ends 10:00)
        step1 = Text("Art ends first (10:00)", font_size=SMALL_SIZE, color=GREEDY_CHOICE)
        step1.move_to(DOWN * 2.5)
        self.play(
            class_blocks["Art"].rect.animate.set_fill(GREEDY_CHOICE),
            Write(step1),
            run_time=GREEDY_SELECT
        )
        self.play(class_blocks["Art"].rect.animate.set_fill(SELECTED_ITEM), run_time=FAST)
        
        # Eliminate English (conflicts)
        self.play(
            class_blocks["Eng"].rect.animate.set_fill(REJECTED_ITEM).set_opacity(0.4),
            run_time=ELIMINATION
        )
        
        self.play(FadeOut(step1), run_time=FAST)
        
        # Step 2: Math (ends 11:00)
        step2 = Text("Math ends next (11:00)", font_size=SMALL_SIZE, color=GREEDY_CHOICE)
        step2.move_to(DOWN * 2.5)
        self.play(
            class_blocks["Math"].rect.animate.set_fill(GREEDY_CHOICE),
            Write(step2),
            run_time=GREEDY_SELECT
        )
        self.play(class_blocks["Math"].rect.animate.set_fill(SELECTED_ITEM), run_time=FAST)
        
        # Eliminate CS
        self.play(
            class_blocks["CS"].rect.animate.set_fill(REJECTED_ITEM).set_opacity(0.4),
            run_time=ELIMINATION
        )
        
        self.play(FadeOut(step2), run_time=FAST)
        
        # Step 3: Music (ends 12:00)
        step3 = Text("Music available (12:00)", font_size=SMALL_SIZE, color=GREEDY_CHOICE)
        step3.move_to(DOWN * 2.5)
        self.play(
            class_blocks["Music"].rect.animate.set_fill(SELECTED_ITEM),
            Write(step3),
            run_time=GREEDY_SELECT
        )
        
        self.play(FadeOut(step3), run_time=FAST)
        
        # Result
        result = Text("Result: 3 classes (Art, Math, Music)", font_size=BODY_SIZE, color=SELECTED_ITEM)
        result.move_to(DOWN * 2.5)
        self.play(Write(result), run_time=NORMAL)
        
        insight = Text("Greedy = Optimal here!", font_size=LABEL_SIZE, color=GREEDY_CHOICE)
        insight.move_to(DOWN * 3.2)
        self.play(Write(insight), run_time=FAST)
        self.wait(LONG_PAUSE)
    
    # ==================== SCENE 3: KNAPSACK ====================
    
    def _knapsack_scene(self):
        """Knapsack problem - greedy is approximate."""
        title = self._title("The Knapsack Problem")
        self.play(Write(title), run_time=NORMAL)
        
        problem = Text("Capacity: 35 lbs - Maximize value", font_size=BODY_SIZE, color=TEXT_SECONDARY)
        problem.move_to(UP * 2.2)
        self.play(Write(problem), run_time=FAST)
        
        # Items
        stereo = self._item_card("Stereo", 3000, 30)
        laptop = self._item_card("Laptop", 2000, 20)
        guitar = self._item_card("Guitar", 1500, 15)
        
        items = VGroup(stereo, laptop, guitar)
        items.arrange(RIGHT, buff=0.5)
        items.move_to(UP * 0.8)
        
        self.play(
            LaggedStart(*[FadeIn(i) for i in items], lag_ratio=0.15),
            run_time=NORMAL
        )
        self.wait(PAUSE)
        
        # Greedy strategy
        strategy = Text("Greedy: Pick most valuable that fits", font_size=LABEL_SIZE, color=GREEDY_CHOICE)
        strategy.move_to(DOWN * 0.3)
        self.play(Write(strategy), run_time=FAST)
        
        # Capacity gauge
        gauge_label = Text("Capacity:", font_size=SMALL_SIZE, color=TEXT_PRIMARY)
        gauge_label.move_to(DOWN * 1.2 + LEFT * 3)
        
        gauge_bg = Rectangle(width=4, height=0.35, fill_color="#1E293B", fill_opacity=1,
                            stroke_color=TEXT_PRIMARY, stroke_width=2)
        gauge_bg.move_to(DOWN * 1.2 + RIGHT * 0.5)
        
        gauge_text = Text("0/35 lbs", font_size=TINY_SIZE, color=TEXT_PRIMARY)
        gauge_text.next_to(gauge_bg, RIGHT, buff=0.2)
        
        self.play(Write(gauge_label), Create(gauge_bg), Write(gauge_text), run_time=FAST)
        
        # Select stereo (most valuable)
        self.play(stereo.box.animate.set_fill(GREEDY_CHOICE), run_time=FAST)
        
        action1 = Text("Stereo: $3000, 30 lbs ✓", font_size=SMALL_SIZE, color=SELECTED_ITEM)
        action1.move_to(DOWN * 2)
        self.play(
            stereo.box.animate.set_fill(SELECTED_ITEM),
            Write(action1),
            run_time=FAST
        )
        
        # Update gauge
        gauge_fill = Rectangle(width=3.4, height=0.25, fill_color=SELECTED_ITEM, 
                              fill_opacity=0.9, stroke_width=0)
        gauge_fill.align_to(gauge_bg, LEFT).shift(RIGHT * 0.05)
        new_gauge_text = Text("30/35 lbs", font_size=TINY_SIZE, color=TEXT_PRIMARY)
        new_gauge_text.next_to(gauge_bg, RIGHT, buff=0.2)
        
        self.play(
            FadeIn(gauge_fill),
            Transform(gauge_text, new_gauge_text),
            run_time=FAST
        )
        
        # Laptop and Guitar don't fit
        action2 = Text("Laptop (20 lbs) - doesn't fit!", font_size=SMALL_SIZE, color=REJECTED_ITEM)
        action2.move_to(DOWN * 2.5)
        self.play(
            laptop.box.animate.set_fill(REJECTED_ITEM).set_opacity(0.5),
            FadeOut(action1),
            Write(action2),
            run_time=FAST
        )
        
        action3 = Text("Guitar (15 lbs) - doesn't fit!", font_size=SMALL_SIZE, color=REJECTED_ITEM)
        action3.move_to(DOWN * 3)
        self.play(
            guitar.box.animate.set_fill(REJECTED_ITEM).set_opacity(0.5),
            Write(action3),
            run_time=FAST
        )
        
        greedy_total = Text("Greedy total: $3000", font_size=LABEL_SIZE, color=GREEDY_CHOICE)
        greedy_total.move_to(DOWN * 3.5)
        self.play(FadeOut(action2), FadeOut(action3), Write(greedy_total), run_time=FAST)
        self.wait(PAUSE)
        
        # Show better solution
        self.play(FadeOut(greedy_total), run_time=FAST)
        
        better = Text("But wait... Laptop + Guitar = $3500!", font_size=BODY_SIZE, color=APPROXIMATION)
        better.move_to(DOWN * 2.5)
        
        self.play(
            stereo.box.animate.set_fill(AVAILABLE_ITEM).set_opacity(1),
            laptop.box.animate.set_fill(SELECTED_ITEM).set_opacity(1),
            guitar.box.animate.set_fill(SELECTED_ITEM).set_opacity(1),
            Write(better),
            run_time=NORMAL
        )
        
        comparison = Text("Greedy $3000 vs Optimal $3500 (86%)", font_size=LABEL_SIZE, color=TEXT_ACCENT)
        comparison.move_to(DOWN * 3.2)
        self.play(Write(comparison), run_time=FAST)
        
        lesson = Text("Greedy ≠ Optimal, but close enough!", font_size=SMALL_SIZE, color=APPROXIMATION)
        lesson.move_to(DOWN * 3.7)
        self.play(Write(lesson), run_time=FAST)
        self.wait(LONG_PAUSE)
    
    # ==================== SCENE 4: SET COVERING ====================
    
    def _set_covering_scene(self):
        """Set covering with radio stations."""
        title = self._title("Set Covering Problem")
        self.play(Write(title), run_time=NORMAL)
        
        problem = Text("Cover all states with minimum stations", font_size=BODY_SIZE, color=TEXT_SECONDARY)
        problem.move_to(UP * 2.2)
        self.play(Write(problem), run_time=FAST)
        
        # States needed
        states_text = Text("States: WA, MT, ID, OR, NV, UT, CA, AZ", font_size=SMALL_SIZE, color=TEXT_PRIMARY)
        states_text.move_to(UP * 1.5)
        self.play(Write(states_text), run_time=FAST)
        
        # Stations and coverage
        stations_data = [
            ("KONE", "ID, NV, UT", LEFT * 4 + UP * 0.3),
            ("KTWO", "WA, ID, MT", LEFT * 4 + DOWN * 0.5),
            ("KTHREE", "OR, NV, CA", RIGHT * 0 + UP * 0.3),
            ("KFOUR", "NV, UT", RIGHT * 0 + DOWN * 0.5),
            ("KFIVE", "CA, AZ", RIGHT * 4 + UP * 0.3),
        ]
        
        station_cards = {}
        for name, coverage, pos in stations_data:
            card = VGroup()
            bg = RoundedRectangle(width=2.5, height=0.6, corner_radius=0.08,
                                 fill_color=AVAILABLE_ITEM, fill_opacity=0.6,
                                 stroke_color=STATION_COLOR, stroke_width=2)
            bg.move_to(pos)
            name_text = Text(name, font_size=TINY_SIZE, color=STATION_COLOR)
            name_text.move_to(bg.get_center() + LEFT * 0.6)
            cov_text = Text(coverage, font_size=12, color=TEXT_SECONDARY)
            cov_text.move_to(bg.get_center() + RIGHT * 0.4)
            card.add(bg, name_text, cov_text)
            card.bg = bg
            station_cards[name] = card
        
        self.play(
            LaggedStart(*[FadeIn(c) for c in station_cards.values()], lag_ratio=0.1),
            run_time=NORMAL
        )
        self.wait(PAUSE)
        
        # Greedy strategy
        strategy = Text("Greedy: Pick station covering MOST uncovered", 
                       font_size=LABEL_SIZE, color=GREEDY_CHOICE)
        strategy.move_to(DOWN * 1.2)
        self.play(Write(strategy), run_time=FAST)
        
        # Round 1: KTWO (3 states)
        round1 = Text("Round 1: KTWO covers 3 (WA, ID, MT)", font_size=SMALL_SIZE, color=GREEDY_CHOICE)
        round1.move_to(DOWN * 2)
        self.play(
            station_cards["KTWO"].bg.animate.set_fill(SELECTED_ITEM),
            Write(round1),
            run_time=FAST
        )
        self.wait(0.5)
        
        # Round 2: KTHREE (3 states)
        round2 = Text("Round 2: KTHREE covers 3 (OR, NV, CA)", font_size=SMALL_SIZE, color=GREEDY_CHOICE)
        round2.move_to(DOWN * 2.5)
        self.play(
            station_cards["KTHREE"].bg.animate.set_fill(SELECTED_ITEM),
            Write(round2),
            run_time=FAST
        )
        self.wait(0.5)
        
        # Round 3: KONE (UT remaining)
        round3 = Text("Round 3: KONE covers UT", font_size=SMALL_SIZE, color=GREEDY_CHOICE)
        round3.move_to(DOWN * 3)
        self.play(
            station_cards["KONE"].bg.animate.set_fill(SELECTED_ITEM),
            Write(round3),
            run_time=FAST
        )
        self.wait(0.5)
        
        # Round 4: KFIVE (AZ remaining)
        round4 = Text("Round 4: KFIVE covers AZ", font_size=SMALL_SIZE, color=GREEDY_CHOICE)
        round4.move_to(DOWN * 3.5)
        self.play(
            station_cards["KFIVE"].bg.animate.set_fill(SELECTED_ITEM),
            Write(round4),
            run_time=FAST
        )
        
        self.wait(PAUSE)
        
        # Result
        self.play(FadeOut(round1), FadeOut(round2), FadeOut(round3), FadeOut(round4), run_time=FAST)
        
        result = Text("Result: 4 stations - O(n²) time!", font_size=BODY_SIZE, color=SELECTED_ITEM)
        result.move_to(DOWN * 2.5)
        self.play(Write(result), run_time=NORMAL)
        
        compare = Text("Exact solution: O(2ⁿ) - impossible for large n", font_size=SMALL_SIZE, color=EXPONENTIAL_DANGER)
        compare.move_to(DOWN * 3.2)
        self.play(Write(compare), run_time=FAST)
        self.wait(LONG_PAUSE)
    
    # ==================== SCENE 5: TRAVELING SALESPERSON ====================
    
    def _tsp_scene(self):
        """Traveling salesperson - NP-complete."""
        title = self._title("Traveling Salesperson (NP-Complete)")
        self.play(Write(title), run_time=NORMAL)
        
        problem = Text("Visit all cities, minimize total distance", font_size=BODY_SIZE, color=TEXT_SECONDARY)
        problem.move_to(UP * 2.2)
        self.play(Write(problem), run_time=FAST)
        
        # Factorial explosion
        explosion_data = [
            ("5 cities", "120 routes"),
            ("10 cities", "3,628,800"),
            ("15 cities", "1.3 trillion"),
            ("20 cities", "2.4 × 10¹⁸"),
        ]
        
        table = VGroup()
        for cities, routes in explosion_data:
            row = VGroup()
            c_text = Text(cities, font_size=SMALL_SIZE, color=TEXT_PRIMARY)
            r_text = Text(routes, font_size=SMALL_SIZE, color=EXPONENTIAL_DANGER)
            c_text.move_to(LEFT * 2)
            r_text.move_to(RIGHT * 2)
            row.add(c_text, r_text)
            table.add(row)
        
        table.arrange(DOWN, buff=0.4)
        table.move_to(UP * 0.3)
        
        self.play(
            LaggedStart(*[FadeIn(row) for row in table], lag_ratio=0.3),
            run_time=SLOW
        )
        self.wait(PAUSE)
        
        impossible = Text("IMPOSSIBLE to solve exactly!", font_size=BODY_SIZE, color=EXPONENTIAL_DANGER)
        impossible.move_to(DOWN * 1.8)
        self.play(Write(impossible), run_time=NORMAL)
        self.wait(PAUSE)
        
        # Greedy solution
        self.play(FadeOut(impossible), run_time=FAST)
        
        greedy = Text("Greedy: Always go to NEAREST city", font_size=LABEL_SIZE, color=GREEDY_CHOICE)
        greedy.move_to(DOWN * 1.8)
        self.play(Write(greedy), run_time=FAST)
        
        result = Text("Result: ~10% longer than optimal, but INSTANT", font_size=SMALL_SIZE, color=APPROXIMATION)
        result.move_to(DOWN * 2.5)
        self.play(Write(result), run_time=FAST)
        
        tradeoff = Text("Good enough!", font_size=BODY_SIZE, color=SELECTED_ITEM)
        tradeoff.move_to(DOWN * 3.2)
        self.play(Write(tradeoff), run_time=NORMAL)
        self.wait(LONG_PAUSE)
    
    # ==================== SCENE 6: NP-COMPLETE RECOGNITION ====================
    
    def _np_complete_scene(self):
        """How to recognize NP-complete problems."""
        title = self._title("Recognizing NP-Complete Problems")
        self.play(Write(title), run_time=NORMAL)
        
        signs = [
            "⚠️ Fast with few items, slow with many",
            "⚠️ Must calculate ALL combinations",
            "⚠️ Can't break into sub-problems",
            "⚠️ Involves sequences or sets",
            "⚠️ Similar to known NP-complete problems",
        ]
        
        sign_texts = VGroup()
        for sign in signs:
            text = Text(sign, font_size=SMALL_SIZE, color=APPROXIMATION)
            sign_texts.add(text)
        
        sign_texts.arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        sign_texts.move_to(UP * 0.5)
        
        self.play(
            LaggedStart(*[FadeIn(s, shift=LEFT * 0.3) for s in sign_texts], lag_ratio=0.2),
            run_time=SLOW
        )
        self.wait(PAUSE)
        
        # Solution
        solution = Text("Solution: Use greedy approximation!", font_size=BODY_SIZE, color=SELECTED_ITEM)
        solution.move_to(DOWN * 2)
        self.play(Write(solution), run_time=NORMAL)
        
        examples = Text("Set covering, TSP, Knapsack...", font_size=SMALL_SIZE, color=TEXT_SECONDARY)
        examples.move_to(DOWN * 2.7)
        self.play(Write(examples), run_time=FAST)
        self.wait(LONG_PAUSE)
    
    # ==================== SCENE 7: SUMMARY ====================
    
    def _summary_scene(self):
        """Final summary."""
        title = self._title("Key Takeaways")
        self.play(Write(title), run_time=NORMAL)
        
        takeaways = [
            ("1.", "Greedy = Pick locally optimal at each step", GREEDY_CHOICE),
            ("2.", "Sometimes optimal (scheduling)", SELECTED_ITEM),
            ("3.", "Sometimes approximate (knapsack, TSP)", APPROXIMATION),
            ("4.", "NP-Complete = No fast exact solution", EXPONENTIAL_DANGER),
            ("5.", "Greedy approximations: fast + good enough", TEXT_ACCENT),
        ]
        
        items = VGroup()
        for num, text, color in takeaways:
            num_text = Text(num, font_size=BODY_SIZE, color=TEXT_PRIMARY)
            content = Text(text, font_size=SMALL_SIZE, color=color)
            content.next_to(num_text, RIGHT, buff=0.2)
            row = VGroup(num_text, content)
            items.add(row)
        
        items.arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        items.move_to(UP * 0.3)
        
        self.play(
            LaggedStart(*[FadeIn(item, shift=LEFT * 0.3) for item in items], lag_ratio=0.15),
            run_time=SLOW
        )
        self.wait(PAUSE)
        
        # Final message
        final = VGroup(
            Text("Greedy algorithms:", font_size=BODY_SIZE, color=TEXT_PRIMARY),
            Text("✓ Easy to write  ✓ Fast to run  ✓ Often good enough", 
                font_size=SMALL_SIZE, color=SELECTED_ITEM),
        )
        final.arrange(DOWN, buff=0.2)
        final.move_to(DOWN * 2.5)
        
        self.play(Write(final), run_time=NORMAL)
        self.wait(LONG_PAUSE)


# Individual scene classes
class IntroScene(Chapter8Animation):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        self._intro_scene()

class ClassroomScene(Chapter8Animation):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        self._classroom_scene()

class KnapsackScene(Chapter8Animation):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        self._knapsack_scene()

class SetCoveringScene(Chapter8Animation):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        self._set_covering_scene()

class TSPScene(Chapter8Animation):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        self._tsp_scene()

class NPCompleteScene(Chapter8Animation):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        self._np_complete_scene()

class SummaryScene(Chapter8Animation):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        self._summary_scene()
