#!/usr/bin/env python3
"""
Chapter 4: Divide & Conquer and Quicksort
=========================================
Educational animation demonstrating D&C strategy and Quicksort algorithm.
3Blue1Brown-style with smooth motion, clear visuals, and minimal text.

Usage:
    manim -pql main.py Chapter4Animation    # Preview (480p)
    manim -pqh main.py Chapter4Animation    # HD quality (1080p)
    
Individual scenes:
    manim -pql main.py DNCIntroScene
    manim -pql main.py FarmProblemScene
    manim -pql main.py RecursiveSumScene
    manim -pql main.py QuicksortConceptScene
    manim -pql main.py QuicksortWalkthroughScene
    manim -pql main.py PivotComparisonScene
    manim -pql main.py BigOAnalysisScene
    manim -pql main.py SummaryScene
"""
import sys
import math
sys.path.insert(0, '/home/hg/Desktop/algorthims/Chapter4_DivideConquerQuicksort')

from manim import *

# Import configurations
from config.colors import (
    BACKGROUND_COLOR, TEXT_PRIMARY, TEXT_SECONDARY, TEXT_ACCENT,
    UNPROCESSED, ACTIVE, COMPLETED, HIGHLIGHT,
    PIVOT, LESS_THAN, GREATER_THAN, BASE_CASE, ACTIVE_FRAME,
    DIVIDE_COLOR, CONQUER_COLOR, PROBLEM_COLOR,
    FARM_COLOR, SQUARE_COLOR, INVALID_COLOR,
    STACK_FRAME, STACK_ACTIVE, STACK_RETURNING,
    O_LOG_N, O_N, O_N_LOG_N, O_N_SQUARED
)
from config.fonts import (
    TITLE_SIZE, SUBTITLE_SIZE, HEADING_SIZE, BODY_SIZE,
    LABEL_SIZE, SMALL_SIZE, TINY_SIZE
)
from config.animation_constants import (
    INSTANT, FAST, NORMAL, SLOW, PAUSE, LONG_PAUSE,
    TITLE_Y, CONTENT_TOP, CONTENT_MID, CONTENT_BOT,
    STACK_FRAME_HEIGHT, STACK_FRAME_WIDTH
)


class Chapter4Animation(Scene):
    """
    Complete Chapter 4 animation covering:
    1. Introduction to Divide & Conquer
    2. Farm Land Problem (visual metaphor)
    3. Recursive Sum on Arrays
    4. Quicksort Concept
    5. Quicksort Full Walkthrough
    6. Pivot Choice Comparison (Best vs Worst)
    7. Big-O Analysis
    8. Summary
    """
    
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        
        # Scene 1: D&C Introduction
        self._dnc_intro_scene()
        self._clear()
        
        # Scene 2: Farm Problem
        self._farm_problem_scene()
        self._clear()
        
        # Scene 3: Recursive Sum
        self._recursive_sum_scene()
        self._clear()
        
        # Scene 4: Quicksort Concept
        self._quicksort_concept_scene()
        self._clear()
        
        # Scene 5: Quicksort Walkthrough
        self._quicksort_walkthrough_scene()
        self._clear()
        
        # Scene 6: Pivot Comparison
        self._pivot_comparison_scene()
        self._clear()
        
        # Scene 7: Big-O Analysis
        self._big_o_scene()
        self._clear()
        
        # Scene 8: Summary
        self._summary_scene()
    
    def _clear(self):
        """Clear scene with fade transition."""
        if self.mobjects:
            self.play(*[FadeOut(m) for m in self.mobjects], run_time=FAST)
        self.wait(0.2)
    
    # ==================== HELPER METHODS ====================
    
    def _title(self, text, y=TITLE_Y):
        t = Text(text, font_size=HEADING_SIZE, color=TEXT_PRIMARY)
        t.move_to(UP * y)
        return t
    
    def _cell(self, value, color=UNPROCESSED, width=0.7, height=0.6):
        grp = VGroup()
        rect = Rectangle(width=width, height=height, fill_color=color, 
                        fill_opacity=0.85, stroke_color=TEXT_PRIMARY, stroke_width=2)
        lbl = Text(str(value), font_size=int(LABEL_SIZE * 0.9), color=TEXT_PRIMARY)
        lbl.move_to(rect.get_center())
        grp.add(rect, lbl)
        grp.rect = rect
        grp.value = value
        return grp
    
    def _array(self, values, color=UNPROCESSED, spacing=0.08):
        arr = VGroup()
        cells = []
        for v in values:
            cell = self._cell(v, color)
            cells.append(cell)
            arr.add(cell)
        arr.arrange(RIGHT, buff=spacing)
        arr.cells = cells
        return arr
    
    def _stack_frame(self, label, color=STACK_FRAME, width=2.2, height=0.5):
        grp = VGroup()
        rect = Rectangle(width=width, height=height, fill_color=color,
                        fill_opacity=0.85, stroke_color=TEXT_PRIMARY, stroke_width=2)
        text = Text(label, font_size=TINY_SIZE, color=TEXT_PRIMARY)
        text.move_to(rect.get_center())
        grp.add(rect, text)
        grp.rect = rect
        return grp
    
    # ==================== SCENE 1: D&C INTRODUCTION ====================
    
    def _dnc_intro_scene(self):
        """Introduction to Divide & Conquer strategy."""
        # Title
        title = Text("Chapter 4: Divide & Conquer", font_size=TITLE_SIZE, color=TEXT_PRIMARY)
        title.move_to(UP * 2)
        
        self.play(Write(title), run_time=SLOW)
        self.wait(PAUSE)
        
        # Subtitle
        subtitle = Text("A Problem-Solving Strategy", font_size=SUBTITLE_SIZE, color=TEXT_ACCENT)
        subtitle.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(subtitle, shift=UP * 0.3), run_time=NORMAL)
        self.wait(PAUSE)
        
        # Move title
        self.play(
            title.animate.scale(0.7).move_to(UP * 3.2),
            FadeOut(subtitle),
            run_time=NORMAL
        )
        
        # Core concept
        concept = Text("Break big problems into smaller identical problems", 
                      font_size=BODY_SIZE, color=TEXT_SECONDARY)
        concept.move_to(UP * 2.2)
        self.play(Write(concept), run_time=FAST)
        
        # D&C Pattern
        pattern_title = Text("The Pattern:", font_size=LABEL_SIZE, color=TEXT_PRIMARY)
        pattern_title.move_to(UP * 1.2 + LEFT * 3)
        
        pattern = VGroup(
            Text("1. Base Case", font_size=SMALL_SIZE, color=BASE_CASE),
            Text("   → Simplest form, solve directly", font_size=TINY_SIZE, color=TEXT_SECONDARY),
            Text("2. Divide", font_size=SMALL_SIZE, color=DIVIDE_COLOR),
            Text("   → Break into smaller subproblems", font_size=TINY_SIZE, color=TEXT_SECONDARY),
            Text("3. Conquer", font_size=SMALL_SIZE, color=CONQUER_COLOR),
            Text("   → Solve subproblems recursively", font_size=TINY_SIZE, color=TEXT_SECONDARY),
            Text("4. Combine", font_size=SMALL_SIZE, color=COMPLETED),
            Text("   → Merge solutions", font_size=TINY_SIZE, color=TEXT_SECONDARY),
        )
        pattern.arrange(DOWN, buff=0.12, aligned_edge=LEFT)
        pattern.next_to(pattern_title, DOWN, buff=0.3, aligned_edge=LEFT)
        
        self.play(Write(pattern_title), run_time=FAST)
        self.play(
            LaggedStart(*[Write(p) for p in pattern], lag_ratio=0.1),
            run_time=SLOW
        )
        self.wait(PAUSE)
        
        # Visual: Problem shrinking
        problem_visual = VGroup()
        sizes = [2.0, 1.4, 0.9, 0.5]
        colors = [PROBLEM_COLOR, DIVIDE_COLOR, DIVIDE_COLOR, BASE_CASE]
        
        for i, (size, color) in enumerate(zip(sizes, colors)):
            box = RoundedRectangle(width=size, height=size * 0.6, corner_radius=0.1,
                                  fill_color=color, fill_opacity=0.7,
                                  stroke_color=TEXT_PRIMARY, stroke_width=2)
            problem_visual.add(box)
        
        problem_visual.arrange(RIGHT, buff=0.4)
        problem_visual.move_to(RIGHT * 2 + DOWN * 0.5)
        
        # Arrows between
        arrows = VGroup()
        for i in range(len(problem_visual) - 1):
            arrow = Arrow(
                problem_visual[i].get_right(),
                problem_visual[i + 1].get_left(),
                color=TEXT_SECONDARY, stroke_width=2, buff=0.1
            )
            arrows.add(arrow)
        
        self.play(FadeIn(problem_visual[0]), run_time=FAST)
        for i in range(len(arrows)):
            self.play(
                GrowArrow(arrows[i]),
                FadeIn(problem_visual[i + 1]),
                run_time=FAST
            )
        
        shrink_label = Text("Problem shrinks until base case", font_size=SMALL_SIZE, color=TEXT_ACCENT)
        shrink_label.next_to(problem_visual, DOWN, buff=0.3)
        self.play(Write(shrink_label), run_time=FAST)
        self.wait(LONG_PAUSE)
    
    # ==================== SCENE 2: FARM PROBLEM ====================
    
    def _farm_problem_scene(self):
        """The farm land problem - visual D&C metaphor."""
        # Title
        title = self._title("The Farm Problem")
        self.play(Write(title), run_time=NORMAL)
        
        # Problem statement
        problem = Text("Divide land into equal square plots", font_size=BODY_SIZE, color=TEXT_SECONDARY)
        problem.move_to(UP * 2.2)
        self.play(Write(problem), run_time=FAST)
        
        # Draw farm (1680 x 640 scaled down)
        farm_width = 4.2  # scaled
        farm_height = 1.6
        
        farm = Rectangle(width=farm_width, height=farm_height,
                        fill_color=FARM_COLOR, fill_opacity=0.6,
                        stroke_color=TEXT_PRIMARY, stroke_width=2)
        farm.move_to(UP * 0.5)
        
        dim_label = Text("1680 × 640", font_size=SMALL_SIZE, color=TEXT_PRIMARY)
        dim_label.next_to(farm, UP, buff=0.15)
        
        self.play(FadeIn(farm), Write(dim_label), run_time=NORMAL)
        self.wait(PAUSE)
        
        # D&C Question
        question = Text("What's the largest square that divides evenly?", 
                       font_size=LABEL_SIZE, color=TEXT_ACCENT)
        question.move_to(DOWN * 1)
        self.play(Write(question), run_time=FAST)
        
        # Show largest square (640 x 640)
        square_size = farm_height
        square1 = Rectangle(width=square_size, height=square_size,
                           fill_color=SQUARE_COLOR, fill_opacity=0.5,
                           stroke_color=SQUARE_COLOR, stroke_width=3)
        square1.move_to(farm.get_left() + RIGHT * square_size / 2)
        
        square2 = Rectangle(width=square_size, height=square_size,
                           fill_color=SQUARE_COLOR, fill_opacity=0.5,
                           stroke_color=SQUARE_COLOR, stroke_width=3)
        square2.next_to(square1, RIGHT, buff=0)
        
        self.play(FadeIn(square1), run_time=FAST)
        self.play(FadeIn(square2), run_time=FAST)
        
        # Remaining rectangle
        remaining_width = farm_width - 2 * square_size
        remaining = Rectangle(width=remaining_width, height=farm_height,
                             fill_color=PROBLEM_COLOR, fill_opacity=0.5,
                             stroke_color=PROBLEM_COLOR, stroke_width=3)
        remaining.move_to(farm.get_right() - RIGHT * remaining_width / 2)
        
        remaining_label = Text("Remaining: 400 × 640", font_size=TINY_SIZE, color=PROBLEM_COLOR)
        remaining_label.next_to(remaining, DOWN, buff=0.1)
        
        self.play(FadeIn(remaining), Write(remaining_label), run_time=FAST)
        self.wait(PAUSE)
        
        # Key insight
        insight = Text("Same problem, smaller size → RECURSION!", 
                      font_size=BODY_SIZE, color=HIGHLIGHT)
        insight.move_to(DOWN * 2.2)
        self.play(Write(insight), run_time=NORMAL)
        
        # Base case note
        base_note = Text("Base case: when length divides evenly", 
                        font_size=SMALL_SIZE, color=BASE_CASE)
        base_note.move_to(DOWN * 2.9)
        self.play(Write(base_note), run_time=FAST)
        self.wait(LONG_PAUSE)
    
    # ==================== SCENE 3: RECURSIVE SUM ====================
    
    def _recursive_sum_scene(self):
        """D&C on arrays - recursive sum."""
        # Title
        title = self._title("D&C on Arrays: Recursive Sum")
        self.play(Write(title), run_time=NORMAL)
        
        # Problem
        problem = Text("Sum all elements using recursion", font_size=BODY_SIZE, color=TEXT_SECONDARY)
        problem.move_to(UP * 2.2)
        self.play(Write(problem), run_time=FAST)
        
        # Array
        values = [2, 4, 6]
        arr = self._array(values, UNPROCESSED)
        arr.move_to(UP * 1.0)
        
        self.play(FadeIn(arr), run_time=NORMAL)
        self.wait(PAUSE)
        
        # Show splitting
        split_label = Text("Split: first + sum(rest)", font_size=LABEL_SIZE, color=DIVIDE_COLOR)
        split_label.move_to(UP * 0.2)
        self.play(Write(split_label), run_time=FAST)
        
        # Animate split
        first_cell = arr.cells[0].copy()
        rest_arr = VGroup(*[c.copy() for c in arr.cells[1:]])
        
        self.play(
            first_cell.animate.move_to(LEFT * 2 + DOWN * 0.5),
            rest_arr.animate.move_to(RIGHT * 1.5 + DOWN * 0.5),
            run_time=NORMAL
        )
        
        plus = Text("+", font_size=BODY_SIZE, color=TEXT_PRIMARY)
        plus.move_to(DOWN * 0.5)
        
        first_label = Text("2", font_size=LABEL_SIZE, color=DIVIDE_COLOR)
        first_label.next_to(first_cell, DOWN, buff=0.2)
        
        rest_label = Text("sum([4, 6])", font_size=LABEL_SIZE, color=DIVIDE_COLOR)
        rest_label.next_to(rest_arr, DOWN, buff=0.2)
        
        self.play(Write(plus), Write(first_label), Write(rest_label), run_time=FAST)
        self.wait(PAUSE)
        
        # Show stack building
        stack_base = RIGHT * 4.5 + DOWN * 2
        base_line = Line(stack_base + LEFT * 1.3, stack_base + RIGHT * 1.3,
                        color=TEXT_PRIMARY, stroke_width=2)
        self.play(Create(base_line), run_time=FAST)
        
        frames = []
        calls = ["sum([2,4,6])", "sum([4,6])", "sum([6])", "sum([])"]
        
        for i, call in enumerate(calls):
            is_base = (call == "sum([])")
            color = BASE_CASE if is_base else STACK_FRAME
            frame = self._stack_frame(call, color, width=2.0, height=0.45)
            frame.move_to(stack_base + UP * (i * 0.5 + 0.3))
            frames.append(frame)
            
            self.play(FadeIn(frame, shift=UP * 0.2), run_time=FAST)
            
            if is_base:
                base_text = Text("= 0", font_size=TINY_SIZE, color=BASE_CASE)
                base_text.next_to(frame, RIGHT, buff=0.2)
                self.play(Write(base_text), run_time=FAST)
        
        self.wait(PAUSE)
        
        # Unwind with returns
        returns = ["0", "6", "10", "12"]
        
        for i, (frame, ret) in enumerate(zip(reversed(frames), returns)):
            ret_text = Text(f"→ {ret}", font_size=TINY_SIZE, color=CONQUER_COLOR)
            ret_text.next_to(frame, RIGHT, buff=0.2)
            
            self.play(
                frame.rect.animate.set_fill(CONQUER_COLOR),
                Write(ret_text),
                run_time=FAST
            )
            self.wait(0.2)
            self.play(FadeOut(frame), FadeOut(ret_text), run_time=FAST)
        
        # Final result
        result = Text("sum([2, 4, 6]) = 12", font_size=HEADING_SIZE, color=COMPLETED)
        result.move_to(DOWN * 1.5)
        self.play(Write(result), run_time=NORMAL)
        self.wait(LONG_PAUSE)
    
    # ==================== SCENE 4: QUICKSORT CONCEPT ====================
    
    def _quicksort_concept_scene(self):
        """Quicksort high-level concept."""
        # Title
        title = self._title("Quicksort: D&C for Sorting")
        self.play(Write(title), run_time=NORMAL)
        
        # Key question
        question = Text("Can we reduce sorting into smaller sorting problems?", 
                       font_size=BODY_SIZE, color=TEXT_ACCENT)
        question.move_to(UP * 2.2)
        self.play(Write(question), run_time=FAST)
        self.wait(PAUSE)
        
        # The algorithm
        steps_title = Text("Quicksort Steps:", font_size=LABEL_SIZE, color=TEXT_PRIMARY)
        steps_title.move_to(UP * 1.2 + LEFT * 3)
        
        steps = VGroup(
            Text("1. Pick a pivot element", font_size=SMALL_SIZE, color=PIVOT),
            Text("2. Partition array:", font_size=SMALL_SIZE, color=TEXT_PRIMARY),
            Text("   • Elements < pivot", font_size=TINY_SIZE, color=LESS_THAN),
            Text("   • Pivot", font_size=TINY_SIZE, color=PIVOT),
            Text("   • Elements > pivot", font_size=TINY_SIZE, color=GREATER_THAN),
            Text("3. Recursively sort partitions", font_size=SMALL_SIZE, color=DIVIDE_COLOR),
            Text("4. Combine: left + pivot + right", font_size=SMALL_SIZE, color=CONQUER_COLOR),
        )
        steps.arrange(DOWN, buff=0.12, aligned_edge=LEFT)
        steps.next_to(steps_title, DOWN, buff=0.25, aligned_edge=LEFT)
        
        self.play(Write(steps_title), run_time=FAST)
        self.play(
            LaggedStart(*[Write(s) for s in steps], lag_ratio=0.12),
            run_time=SLOW
        )
        self.wait(PAUSE)
        
        # Visual demonstration
        arr = self._array([5, 3, 8, 1, 9, 2], UNPROCESSED)
        arr.move_to(RIGHT * 2 + UP * 0.5)
        self.play(FadeIn(arr), run_time=FAST)
        
        # Highlight pivot (last element = 2)
        pivot_idx = 5
        self.play(arr.cells[pivot_idx].rect.animate.set_fill(PIVOT), run_time=FAST)
        
        pivot_label = Text("pivot = 2", font_size=SMALL_SIZE, color=PIVOT)
        pivot_label.next_to(arr.cells[pivot_idx], UP, buff=0.2)
        self.play(Write(pivot_label), run_time=FAST)
        
        # Partition visualization
        less_indices = [3]  # index of 1
        greater_indices = [0, 1, 2, 4]  # indices of 5, 3, 8, 9
        
        for i in less_indices:
            self.play(arr.cells[i].rect.animate.set_fill(LESS_THAN), run_time=FAST)
        for i in greater_indices:
            self.play(arr.cells[i].rect.animate.set_fill(GREATER_THAN), run_time=FAST)
        
        # Show result
        result_text = Text("[1] + [2] + [5,3,8,9]", font_size=SMALL_SIZE, color=TEXT_ACCENT)
        result_text.next_to(arr, DOWN, buff=0.4)
        self.play(Write(result_text), run_time=FAST)
        
        # Note
        note = Text("Partitions are NOT sorted yet - just separated!", 
                   font_size=LABEL_SIZE, color=HIGHLIGHT)
        note.move_to(DOWN * 2.5)
        self.play(Write(note), run_time=NORMAL)
        self.wait(LONG_PAUSE)
    
    # ==================== SCENE 5: QUICKSORT WALKTHROUGH ====================
    
    def _quicksort_walkthrough_scene(self):
        """Full quicksort walkthrough on small array."""
        # Title
        title = self._title("Quicksort: Step by Step")
        self.play(Write(title), run_time=NORMAL)
        
        # Array [10, 5, 2, 3]
        values = [10, 5, 2, 3]
        arr = self._array(values, UNPROCESSED)
        arr.move_to(UP * 1.5 + LEFT * 2)
        
        arr_label = Text("[10, 5, 2, 3]", font_size=LABEL_SIZE, color=TEXT_PRIMARY)
        arr_label.next_to(arr, UP, buff=0.2)
        
        self.play(FadeIn(arr), Write(arr_label), run_time=NORMAL)
        self.wait(PAUSE)
        
        # Call stack area
        stack_base = RIGHT * 4 + DOWN * 2
        stack_line = Line(stack_base + LEFT * 1.5, stack_base + RIGHT * 1.5,
                         color=TEXT_PRIMARY, stroke_width=2)
        stack_label = Text("Call Stack", font_size=TINY_SIZE, color=TEXT_SECONDARY)
        stack_label.next_to(stack_line, DOWN, buff=0.1)
        self.play(Create(stack_line), Write(stack_label), run_time=FAST)
        
        # Step 1: Select pivot (3)
        step1 = Text("Step 1: Select pivot (last element)", font_size=SMALL_SIZE, color=TEXT_SECONDARY)
        step1.move_to(UP * 0.5)
        self.play(Write(step1), run_time=FAST)
        
        self.play(arr.cells[3].rect.animate.set_fill(PIVOT), run_time=FAST)
        
        # Push first frame
        frame1 = self._stack_frame("qs([10,5,2,3])", STACK_ACTIVE, width=2.2, height=0.45)
        frame1.move_to(stack_base + UP * 0.3)
        self.play(FadeIn(frame1, shift=UP * 0.2), run_time=FAST)
        self.wait(0.3)
        
        # Step 2: Partition
        self.play(FadeOut(step1), run_time=FAST)
        step2 = Text("Step 2: Partition around pivot=3", font_size=SMALL_SIZE, color=TEXT_SECONDARY)
        step2.move_to(UP * 0.5)
        self.play(Write(step2), run_time=FAST)
        
        # 10 > 3, 5 > 3, 2 < 3
        self.play(arr.cells[0].rect.animate.set_fill(GREATER_THAN), run_time=FAST)  # 10
        self.play(arr.cells[1].rect.animate.set_fill(GREATER_THAN), run_time=FAST)  # 5
        self.play(arr.cells[2].rect.animate.set_fill(LESS_THAN), run_time=FAST)     # 2
        self.wait(PAUSE)
        
        # Show partitions
        partition_text = Text("[2] + [3] + [10, 5]", font_size=LABEL_SIZE, color=TEXT_ACCENT)
        partition_text.move_to(DOWN * 0.3)
        self.play(Write(partition_text), run_time=FAST)
        self.wait(PAUSE)
        
        # Step 3: Recurse on left [2] - base case
        self.play(FadeOut(step2), FadeOut(partition_text), run_time=FAST)
        step3 = Text("Step 3: Recurse on [2] - base case!", font_size=SMALL_SIZE, color=BASE_CASE)
        step3.move_to(UP * 0.5)
        self.play(Write(step3), run_time=FAST)
        
        frame2 = self._stack_frame("qs([2])", BASE_CASE, width=2.2, height=0.45)
        frame2.move_to(stack_base + UP * 0.8)
        self.play(FadeIn(frame2, shift=UP * 0.2), run_time=FAST)
        self.wait(0.3)
        self.play(FadeOut(frame2, shift=RIGHT * 0.5), run_time=FAST)  # Pop
        
        # Step 4: Recurse on right [10, 5]
        self.play(FadeOut(step3), run_time=FAST)
        step4 = Text("Step 4: Recurse on [10, 5]", font_size=SMALL_SIZE, color=TEXT_SECONDARY)
        step4.move_to(UP * 0.5)
        self.play(Write(step4), run_time=FAST)
        
        frame3 = self._stack_frame("qs([10,5])", STACK_ACTIVE, width=2.2, height=0.45)
        frame3.move_to(stack_base + UP * 0.8)
        self.play(FadeIn(frame3, shift=UP * 0.2), run_time=FAST)
        
        # Pivot = 5, 10 > 5
        sub_partition = Text("pivot=5: [] + [5] + [10]", font_size=SMALL_SIZE, color=TEXT_ACCENT)
        sub_partition.move_to(DOWN * 0.3)
        self.play(Write(sub_partition), run_time=FAST)
        self.wait(PAUSE)
        
        # Base cases for [10]
        frame4 = self._stack_frame("qs([10])", BASE_CASE, width=2.2, height=0.45)
        frame4.move_to(stack_base + UP * 1.3)
        self.play(FadeIn(frame4, shift=UP * 0.2), run_time=FAST)
        self.play(FadeOut(frame4, shift=RIGHT * 0.5), run_time=FAST)
        
        # Pop remaining frames
        self.play(FadeOut(frame3, shift=RIGHT * 0.5), run_time=FAST)
        self.play(FadeOut(frame1, shift=RIGHT * 0.5), run_time=FAST)
        
        # Final result
        self.play(FadeOut(step4), FadeOut(sub_partition), run_time=FAST)
        
        # Show sorted array
        sorted_arr = self._array([2, 3, 5, 10], COMPLETED)
        sorted_arr.move_to(DOWN * 1.5)
        
        result = Text("Sorted: [2, 3, 5, 10]", font_size=HEADING_SIZE, color=COMPLETED)
        result.next_to(sorted_arr, UP, buff=0.3)
        
        self.play(FadeIn(sorted_arr), Write(result), run_time=NORMAL)
        self.wait(LONG_PAUSE)
    
    # ==================== SCENE 6: PIVOT COMPARISON ====================
    
    def _pivot_comparison_scene(self):
        """Compare best vs worst case pivot selection."""
        # Title
        title = self._title("Pivot Choice Matters!")
        self.play(Write(title), run_time=NORMAL)
        
        # Divider
        divider = DashedLine(UP * 2.5, DOWN * 3, color=TEXT_SECONDARY, stroke_width=1.5)
        self.play(Create(divider), run_time=FAST)
        
        # Headers
        best_head = Text("Best Case", font_size=BODY_SIZE, color=O_LOG_N)
        worst_head = Text("Worst Case", font_size=BODY_SIZE, color=O_N_SQUARED)
        best_head.move_to(LEFT * 3.5 + UP * 2.2)
        worst_head.move_to(RIGHT * 3.5 + UP * 2.2)
        
        self.play(Write(best_head), Write(worst_head), run_time=FAST)
        
        # Best case: balanced partitions
        best_desc = Text("Balanced partitions", font_size=SMALL_SIZE, color=TEXT_SECONDARY)
        best_desc.move_to(LEFT * 3.5 + UP * 1.5)
        
        # Show balanced tree (short)
        best_tree = VGroup()
        # Level 0
        l0 = RoundedRectangle(width=1.8, height=0.35, corner_radius=0.05,
                             fill_color=STACK_FRAME, fill_opacity=0.8)
        l0.move_to(LEFT * 3.5 + UP * 0.8)
        # Level 1
        l1a = RoundedRectangle(width=0.8, height=0.35, corner_radius=0.05,
                              fill_color=STACK_FRAME, fill_opacity=0.8)
        l1b = RoundedRectangle(width=0.8, height=0.35, corner_radius=0.05,
                              fill_color=STACK_FRAME, fill_opacity=0.8)
        l1a.move_to(LEFT * 4.2 + UP * 0.2)
        l1b.move_to(LEFT * 2.8 + UP * 0.2)
        # Level 2
        l2 = VGroup(*[RoundedRectangle(width=0.35, height=0.35, corner_radius=0.05,
                                       fill_color=BASE_CASE, fill_opacity=0.8) for _ in range(4)])
        l2.arrange(RIGHT, buff=0.15)
        l2.move_to(LEFT * 3.5 + DOWN * 0.4)
        
        best_tree.add(l0, l1a, l1b, l2)
        
        self.play(Write(best_desc), run_time=FAST)
        self.play(FadeIn(best_tree), run_time=NORMAL)
        
        best_depth = Text("Depth: O(log n)", font_size=SMALL_SIZE, color=O_LOG_N)
        best_depth.move_to(LEFT * 3.5 + DOWN * 1.2)
        self.play(Write(best_depth), run_time=FAST)
        
        # Worst case: already sorted array
        worst_desc = Text("Unbalanced (sorted input)", font_size=SMALL_SIZE, color=TEXT_SECONDARY)
        worst_desc.move_to(RIGHT * 3.5 + UP * 1.5)
        
        # Show skewed tree (deep)
        worst_tree = VGroup()
        for i in range(5):
            w = 1.8 - i * 0.3
            box = RoundedRectangle(width=max(w, 0.35), height=0.3, corner_radius=0.05,
                                  fill_color=BASE_CASE if i == 4 else STACK_FRAME,
                                  fill_opacity=0.8)
            box.move_to(RIGHT * (3.5 + i * 0.15) + UP * (0.8 - i * 0.4))
            worst_tree.add(box)
        
        self.play(Write(worst_desc), run_time=FAST)
        self.play(
            LaggedStart(*[FadeIn(b) for b in worst_tree], lag_ratio=0.15),
            run_time=NORMAL
        )
        
        worst_depth = Text("Depth: O(n)", font_size=SMALL_SIZE, color=O_N_SQUARED)
        worst_depth.move_to(RIGHT * 3.5 + DOWN * 1.2)
        self.play(Write(worst_depth), run_time=FAST)
        self.wait(PAUSE)
        
        # Complexity comparison
        best_time = Text("Time: O(n log n)", font_size=LABEL_SIZE, color=O_LOG_N)
        worst_time = Text("Time: O(n²)", font_size=LABEL_SIZE, color=O_N_SQUARED)
        best_time.move_to(LEFT * 3.5 + DOWN * 2)
        worst_time.move_to(RIGHT * 3.5 + DOWN * 2)
        
        self.play(Write(best_time), Write(worst_time), run_time=NORMAL)
        
        # Key insight
        insight = Text("Random pivot → average case is O(n log n)!", 
                      font_size=BODY_SIZE, color=TEXT_ACCENT)
        insight.move_to(DOWN * 2.8)
        self.play(Write(insight), run_time=NORMAL)
        self.wait(LONG_PAUSE)
    
    # ==================== SCENE 7: BIG-O ANALYSIS ====================
    
    def _big_o_scene(self):
        """Big-O analysis visualization."""
        # Title
        title = self._title("Big-O Analysis")
        self.play(Write(title), run_time=NORMAL)
        
        # Key insight
        insight = Text("Each level processes all n elements", 
                      font_size=BODY_SIZE, color=TEXT_SECONDARY)
        insight.move_to(UP * 2.2)
        self.play(Write(insight), run_time=FAST)
        
        # Visual: levels processing elements
        levels = VGroup()
        level_labels = []
        
        for i in range(4):
            # Level bar representing O(n) work
            bar = Rectangle(width=4, height=0.4, fill_color=DIVIDE_COLOR,
                           fill_opacity=0.7, stroke_color=TEXT_PRIMARY, stroke_width=2)
            bar.move_to(UP * (0.8 - i * 0.7))
            
            work_label = Text("O(n) work", font_size=TINY_SIZE, color=TEXT_PRIMARY)
            work_label.move_to(bar.get_center())
            
            level_num = Text(f"Level {i}", font_size=TINY_SIZE, color=TEXT_SECONDARY)
            level_num.next_to(bar, LEFT, buff=0.3)
            
            levels.add(VGroup(bar, work_label))
            level_labels.append(level_num)
        
        self.play(
            LaggedStart(*[FadeIn(l) for l in levels], lag_ratio=0.2),
            LaggedStart(*[Write(l) for l in level_labels], lag_ratio=0.2),
            run_time=SLOW
        )
        self.wait(PAUSE)
        
        # Number of levels
        num_levels = VGroup(
            Text("Number of levels:", font_size=LABEL_SIZE, color=TEXT_PRIMARY),
            Text("Best/Average: O(log n)", font_size=SMALL_SIZE, color=O_LOG_N),
            Text("Worst: O(n)", font_size=SMALL_SIZE, color=O_N_SQUARED),
        )
        num_levels.arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        num_levels.move_to(RIGHT * 4 + UP * 0.3)
        
        self.play(Write(num_levels), run_time=NORMAL)
        self.wait(PAUSE)
        
        # Total complexity
        total_title = Text("Total Complexity:", font_size=LABEL_SIZE, color=TEXT_PRIMARY)
        total_title.move_to(DOWN * 1.8)
        
        formula_avg = Text("O(n) × O(log n) = O(n log n)", font_size=LABEL_SIZE, color=O_N_LOG_N)
        formula_avg.move_to(DOWN * 2.3)
        
        formula_worst = Text("O(n) × O(n) = O(n²)", font_size=LABEL_SIZE, color=O_N_SQUARED)
        formula_worst.move_to(DOWN * 2.8)
        
        self.play(Write(total_title), run_time=FAST)
        self.play(Write(formula_avg), run_time=FAST)
        self.play(Write(formula_worst), run_time=FAST)
        self.wait(LONG_PAUSE)
    
    # ==================== SCENE 8: SUMMARY ====================
    
    def _summary_scene(self):
        """Final summary and key takeaways."""
        # Title
        title = self._title("Key Takeaways")
        self.play(Write(title), run_time=NORMAL)
        
        # Takeaways
        takeaways = [
            ("1.", "D&C: Break big problems into smaller identical ones", DIVIDE_COLOR),
            ("2.", "Every D&C has base case + recursive reduction", TEXT_ACCENT),
            ("3.", "Quicksort: Partition around pivot, recurse on parts", PIVOT),
            ("4.", "Pivot choice determines performance", HIGHLIGHT),
            ("5.", "Average O(n log n), Worst O(n²)", O_N_LOG_N),
            ("6.", "Big-O measures growth, not seconds", TEXT_SECONDARY),
        ]
        
        items = VGroup()
        for num, text, color in takeaways:
            num_text = Text(num, font_size=BODY_SIZE, color=TEXT_PRIMARY)
            content = Text(text, font_size=SMALL_SIZE, color=color)
            content.next_to(num_text, RIGHT, buff=0.2)
            row = VGroup(num_text, content)
            items.add(row)
        
        items.arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        items.move_to(UP * 0.3)
        
        self.play(
            LaggedStart(*[FadeIn(item, shift=LEFT * 0.3) for item in items], lag_ratio=0.15),
            run_time=SLOW
        )
        self.wait(PAUSE)
        
        # Visual reminder
        reminder = VGroup(
            Text("Quicksort:", font_size=BODY_SIZE, color=TEXT_PRIMARY),
            Text("partition + recurse + combine", font_size=LABEL_SIZE, color=PIVOT),
        )
        reminder.arrange(DOWN, buff=0.2)
        reminder.move_to(DOWN * 2.5)
        
        self.play(Write(reminder), run_time=NORMAL)
        self.wait(LONG_PAUSE)


# Individual scene classes for separate rendering
class DNCIntroScene(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        Chapter4Animation._dnc_intro_scene(self)

class FarmProblemScene(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        Chapter4Animation._farm_problem_scene(self)

class RecursiveSumScene(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        Chapter4Animation._recursive_sum_scene(self)

class QuicksortConceptScene(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        Chapter4Animation._quicksort_concept_scene(self)

class QuicksortWalkthroughScene(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        Chapter4Animation._quicksort_walkthrough_scene(self)

class PivotComparisonScene(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        Chapter4Animation._pivot_comparison_scene(self)

class BigOAnalysisScene(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        Chapter4Animation._big_o_scene(self)

class SummaryScene(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        Chapter4Animation._summary_scene(self)
