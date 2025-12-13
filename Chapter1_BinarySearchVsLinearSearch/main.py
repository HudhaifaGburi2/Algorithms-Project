#!/usr/bin/env python3
"""
Chapter 1: Binary Search vs Linear Search
==========================================
Educational animation demonstrating search algorithms and Big O notation.
3Blue1Brown-style with smooth motion, clear visuals, and minimal text.

Usage:
    manim -pql main.py Chapter1Animation    # Preview (480p)
    manim -pqh main.py Chapter1Animation    # HD quality (1080p)
    
Individual scenes:
    manim -pql main.py IntroScene
    manim -pql main.py LinearSearchScene
    manim -pql main.py BinarySearchScene
    manim -pql main.py ComparisonScene
    manim -pql main.py BigOScene
    manim -pql main.py SummaryScene
"""
import sys
import math
sys.path.insert(0, '/home/hg/Desktop/algorthims/Chapter1_BinarySearchVsLinearSearch')

from manim import *

# Import configurations
from config.colors import (
    BACKGROUND_COLOR, TEXT_PRIMARY, TEXT_SECONDARY, TEXT_ACCENT,
    UNPROCESSED, ACTIVE_COMPARISON, FOUND_ELEMENT, ELIMINATED, HIGHLIGHT,
    LINEAR_COLOR, BINARY_COLOR,
    O_1, O_LOG_N, O_N, O_N_LOG_N, O_N_SQUARED, O_N_FACTORIAL,
    LOW_POINTER, MID_POINTER, HIGH_POINTER
)
from config.fonts import (
    TITLE_SIZE, SUBTITLE_SIZE, HEADING_SIZE, BODY_SIZE, 
    LABEL_SIZE, SMALL_SIZE, TINY_SIZE
)
from config.animation_constants import (
    INSTANT, FAST, NORMAL, SLOW, PAUSE, LONG_PAUSE,
    TITLE_Y, CONTENT_TOP, CONTENT_MID, CONTENT_BOT
)

# Import algorithm logic
from algorithms.linear_search.logic import linear_search_steps
from algorithms.binary_search.logic import binary_search_steps, binary_search_max_steps

# Demo data - sorted array for searching
DEMO_ARRAY = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]
TARGET_VALUE = 23  # Target to search for


class Chapter1Animation(Scene):
    """
    Complete Chapter 1 animation covering:
    1. Introduction to Algorithms
    2. Linear Search demonstration
    3. Binary Search demonstration
    4. Side-by-side comparison
    5. Big O notation visualization
    6. Summary and key takeaways
    """
    
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        
        # Scene 1: Introduction
        self._intro_scene()
        self._clear()
        
        # Scene 2: Linear Search
        self._linear_search_scene()
        self._clear()
        
        # Scene 3: Binary Search
        self._binary_search_scene()
        self._clear()
        
        # Scene 4: Side-by-side Comparison
        self._comparison_scene()
        self._clear()
        
        # Scene 5: Big O Visualization
        self._big_o_scene()
        self._clear()
        
        # Scene 6: Summary
        self._summary_scene()
    
    def _clear(self):
        """Clear scene with fade transition."""
        if self.mobjects:
            self.play(*[FadeOut(m) for m in self.mobjects], run_time=FAST)
        self.wait(0.2)
    
    # ==================== HELPER METHODS ====================
    
    def _title(self, text, y=TITLE_Y):
        """Create title at top."""
        t = Text(text, font_size=HEADING_SIZE, color=TEXT_PRIMARY)
        t.move_to(UP * y)
        return t
    
    def _step(self, text, y=CONTENT_TOP):
        """Create step label."""
        s = Text(text, font_size=BODY_SIZE, color=TEXT_SECONDARY)
        s.move_to(UP * y)
        return s
    
    def _box(self, value, color=UNPROCESSED, scale=1.0, show_index=False, index=0):
        """Create single array element box."""
        grp = VGroup()
        
        rect = RoundedRectangle(
            width=0.7 * scale,
            height=0.7 * scale,
            corner_radius=0.06 * scale,
            fill_color=color,
            fill_opacity=0.9,
            stroke_color=color,
            stroke_width=2
        )
        
        lbl = Text(str(value), font_size=int(18 * scale), color=TEXT_PRIMARY)
        lbl.move_to(rect.get_center())
        
        grp.add(rect, lbl)
        grp.value = value
        grp.rect = rect
        
        if show_index:
            idx = Text(str(index), font_size=int(14 * scale), color=TEXT_SECONDARY)
            idx.next_to(rect, DOWN, buff=0.08 * scale)
            grp.add(idx)
        
        return grp
    
    def _array(self, values, color=UNPROCESSED, scale=1.0, spacing=0.1, show_indices=False):
        """Create array of boxes."""
        arr = VGroup()
        for i, v in enumerate(values):
            box = self._box(v, color, scale, show_indices, i)
            arr.add(box)
        arr.arrange(RIGHT, buff=spacing * scale)
        return arr
    
    def _color_box(self, box, color):
        """Return animation for changing box color."""
        return box.rect.animate.set_fill(color).set_stroke(color)
    
    def _pointer(self, label, color, direction="down", scale=1.0):
        """Create pointer with label."""
        grp = VGroup()
        
        arrow = Triangle(fill_color=color, fill_opacity=1, stroke_width=0)
        arrow.scale(0.12 * scale)
        if direction == "down":
            arrow.rotate(PI)
        
        lbl = Text(label, font_size=int(SMALL_SIZE * scale), color=color)
        if direction == "down":
            lbl.next_to(arrow, UP, buff=0.08 * scale)
        else:
            lbl.next_to(arrow, DOWN, buff=0.08 * scale)
        
        grp.add(arrow, lbl)
        return grp
    
    # ==================== SCENE 1: INTRODUCTION ====================
    
    def _intro_scene(self):
        """Introduction to algorithms and search problem."""
        # Main title
        title = Text("Chapter 1: Introduction to Algorithms", 
                    font_size=TITLE_SIZE, color=TEXT_PRIMARY)
        title.move_to(UP * 2)
        
        self.play(Write(title), run_time=SLOW)
        self.wait(PAUSE)
        
        # Subtitle
        subtitle = Text("Search Algorithms & Big O Notation", 
                       font_size=SUBTITLE_SIZE, color=TEXT_ACCENT)
        subtitle.next_to(title, DOWN, buff=0.5)
        
        self.play(FadeIn(subtitle, shift=UP * 0.3), run_time=NORMAL)
        self.wait(PAUSE)
        
        # The problem visualization
        self.play(
            title.animate.scale(0.7).move_to(UP * 3.2),
            FadeOut(subtitle),
            run_time=NORMAL
        )
        
        # Show "the problem" - finding a number
        problem = Text("The Problem: Find a number in a list", 
                      font_size=BODY_SIZE, color=TEXT_SECONDARY)
        problem.move_to(UP * 2.2)
        self.play(Write(problem), run_time=NORMAL)
        
        # Show array
        arr = self._array(DEMO_ARRAY[:8], UNPROCESSED, scale=0.85, show_indices=True)
        arr.move_to(UP * 0.5)
        
        self.play(
            LaggedStart(*[FadeIn(box, shift=UP * 0.2) for box in arr], lag_ratio=0.08),
            run_time=NORMAL
        )
        self.wait(PAUSE)
        
        # Target
        target_text = Text(f"Find: {TARGET_VALUE}", font_size=BODY_SIZE, color=HIGHLIGHT)
        target_text.move_to(DOWN * 1)
        
        self.play(Write(target_text), run_time=NORMAL)
        self.wait(PAUSE)
        
        # Two approaches
        approach_title = Text("Two Approaches:", font_size=BODY_SIZE, color=TEXT_PRIMARY)
        approach_title.move_to(DOWN * 2)
        
        linear_label = Text("Linear Search", font_size=LABEL_SIZE, color=LINEAR_COLOR)
        linear_label.move_to(DOWN * 2.7 + LEFT * 2.5)
        
        binary_label = Text("Binary Search", font_size=LABEL_SIZE, color=BINARY_COLOR)
        binary_label.move_to(DOWN * 2.7 + RIGHT * 2.5)
        
        self.play(Write(approach_title), run_time=FAST)
        self.play(
            Write(linear_label),
            Write(binary_label),
            run_time=NORMAL
        )
        self.wait(LONG_PAUSE)
    
    # ==================== SCENE 2: LINEAR SEARCH ====================
    
    def _linear_search_scene(self):
        """Demonstrate linear search step by step."""
        # Title
        title = self._title("Linear Search (Simple Search)")
        self.play(Write(title), run_time=NORMAL)
        
        # Concept explanation
        concept = Text("Check each element from start to end", 
                      font_size=BODY_SIZE, color=TEXT_SECONDARY)
        concept.move_to(UP * 2.2)
        self.play(Write(concept), run_time=FAST)
        
        # Array
        arr = self._array(DEMO_ARRAY[:10], UNPROCESSED, scale=0.8, show_indices=True)
        arr.move_to(UP * 0.8)
        
        self.play(FadeIn(arr), run_time=NORMAL)
        self.wait(PAUSE)
        
        # Target indicator
        target = 19  # In position 9
        target_text = Text(f"Find: {target}", font_size=LABEL_SIZE, color=HIGHLIGHT)
        target_text.next_to(arr, RIGHT, buff=0.5)
        self.play(Write(target_text), run_time=FAST)
        
        # Current pointer
        pointer = self._pointer("current", LINEAR_COLOR, "down")
        pointer.next_to(arr[0], UP, buff=0.3)
        self.play(FadeIn(pointer), run_time=FAST)
        
        # Step counter
        step_counter = Text("Steps: 0", font_size=LABEL_SIZE, color=TEXT_SECONDARY)
        step_counter.move_to(DOWN * 1.5)
        self.play(Write(step_counter), run_time=FAST)
        
        # Search through array
        steps = 0
        for i, box in enumerate(arr):
            steps += 1
            
            # Move pointer
            new_pos = box.get_top() + UP * 0.3
            self.play(pointer.animate.move_to(new_pos), run_time=FAST)
            
            # Highlight current
            self.play(self._color_box(box, ACTIVE_COMPARISON), run_time=FAST)
            
            # Update counter
            new_counter = Text(f"Steps: {steps}", font_size=LABEL_SIZE, color=TEXT_SECONDARY)
            new_counter.move_to(step_counter.get_center())
            self.play(
                ReplacementTransform(step_counter, new_counter),
                run_time=INSTANT
            )
            step_counter = new_counter
            
            # Check if found
            if box.value == target:
                self.play(self._color_box(box, FOUND_ELEMENT), run_time=NORMAL)
                
                found_text = Text("Found!", font_size=BODY_SIZE, color=FOUND_ELEMENT)
                found_text.next_to(box, DOWN, buff=0.8)
                self.play(Write(found_text), run_time=FAST)
                break
            else:
                # Mark as checked
                self.play(self._color_box(box, ELIMINATED), run_time=FAST)
        
        self.wait(PAUSE)
        
        # Complexity note
        complexity = Text("Time: O(n) - checks every element", 
                         font_size=LABEL_SIZE, color=LINEAR_COLOR)
        complexity.move_to(DOWN * 2.8)
        self.play(Write(complexity), run_time=NORMAL)
        self.wait(LONG_PAUSE)
    
    # ==================== SCENE 3: BINARY SEARCH ====================
    
    def _binary_search_scene(self):
        """Demonstrate binary search step by step."""
        # Title
        title = self._title("Binary Search")
        self.play(Write(title), run_time=NORMAL)
        
        # Concept
        concept = Text("Requires sorted array - halves search space each step", 
                      font_size=BODY_SIZE, color=TEXT_SECONDARY)
        concept.move_to(UP * 2.2)
        self.play(Write(concept), run_time=FAST)
        
        # Array (sorted)
        arr = self._array(DEMO_ARRAY, UNPROCESSED, scale=0.65, show_indices=True)
        arr.move_to(UP * 0.8)
        
        self.play(FadeIn(arr), run_time=NORMAL)
        self.wait(PAUSE)
        
        # Target
        target = TARGET_VALUE
        target_text = Text(f"Find: {target}", font_size=LABEL_SIZE, color=HIGHLIGHT)
        target_text.next_to(arr, RIGHT, buff=0.3)
        self.play(Write(target_text), run_time=FAST)
        
        # Pointers: low, mid, high
        low_ptr = self._pointer("low", LOW_POINTER, "down", 0.8)
        mid_ptr = self._pointer("mid", MID_POINTER, "down", 0.8)
        high_ptr = self._pointer("high", HIGH_POINTER, "down", 0.8)
        
        # Step counter
        step_counter = Text("Steps: 0", font_size=LABEL_SIZE, color=TEXT_SECONDARY)
        step_counter.move_to(DOWN * 1.8)
        self.play(Write(step_counter), run_time=FAST)
        
        # Binary search steps
        low, high = 0, len(DEMO_ARRAY) - 1
        steps = 0
        
        while low <= high:
            mid = (low + high) // 2
            steps += 1
            
            # Position pointers
            low_ptr.next_to(arr[low], UP, buff=0.25)
            mid_ptr.next_to(arr[mid], UP, buff=0.55)
            high_ptr.next_to(arr[high], UP, buff=0.25)
            
            if steps == 1:
                self.play(FadeIn(low_ptr), FadeIn(mid_ptr), FadeIn(high_ptr), run_time=NORMAL)
            else:
                self.play(
                    low_ptr.animate.next_to(arr[low], UP, buff=0.25),
                    mid_ptr.animate.next_to(arr[mid], UP, buff=0.55),
                    high_ptr.animate.next_to(arr[high], UP, buff=0.25),
                    run_time=NORMAL
                )
            
            # Highlight mid element
            self.play(self._color_box(arr[mid], ACTIVE_COMPARISON), run_time=FAST)
            
            # Update counter
            new_counter = Text(f"Steps: {steps}", font_size=LABEL_SIZE, color=TEXT_SECONDARY)
            new_counter.move_to(step_counter.get_center())
            self.play(ReplacementTransform(step_counter, new_counter), run_time=INSTANT)
            step_counter = new_counter
            
            mid_value = DEMO_ARRAY[mid]
            
            if mid_value == target:
                # Found!
                self.play(self._color_box(arr[mid], FOUND_ELEMENT), run_time=NORMAL)
                
                found_text = Text("Found!", font_size=BODY_SIZE, color=FOUND_ELEMENT)
                found_text.next_to(arr[mid], DOWN, buff=0.8)
                self.play(Write(found_text), run_time=FAST)
                break
            elif mid_value < target:
                # Eliminate left half
                for i in range(low, mid + 1):
                    self.play(self._color_box(arr[i], ELIMINATED), run_time=INSTANT)
                low = mid + 1
            else:
                # Eliminate right half
                for i in range(mid, high + 1):
                    self.play(self._color_box(arr[i], ELIMINATED), run_time=INSTANT)
                high = mid - 1
            
            self.wait(0.3)
        
        self.wait(PAUSE)
        
        # Complexity note
        complexity = Text("Time: O(log n) - halves search space each step", 
                         font_size=LABEL_SIZE, color=BINARY_COLOR)
        complexity.move_to(DOWN * 2.8)
        self.play(Write(complexity), run_time=NORMAL)
        self.wait(LONG_PAUSE)
    
    # ==================== SCENE 4: COMPARISON ====================
    
    def _comparison_scene(self):
        """Side-by-side comparison of both searches."""
        # Title
        title = self._title("Linear vs Binary Search")
        self.play(Write(title), run_time=NORMAL)
        
        # Divider
        divider = DashedLine(UP * 2.5, DOWN * 3, color=TEXT_SECONDARY, stroke_width=1.5)
        self.play(Create(divider), run_time=FAST)
        
        # Headers
        linear_head = Text("Linear Search", font_size=BODY_SIZE, color=LINEAR_COLOR)
        binary_head = Text("Binary Search", font_size=BODY_SIZE, color=BINARY_COLOR)
        linear_head.move_to(LEFT * 3.5 + UP * 2.2)
        binary_head.move_to(RIGHT * 3.5 + UP * 2.2)
        
        self.play(Write(linear_head), Write(binary_head), run_time=FAST)
        
        # Small arrays for demo
        small_arr = [1, 3, 5, 7, 9, 11, 13, 15]
        
        linear_arr = self._array(small_arr, UNPROCESSED, scale=0.5, spacing=0.05)
        binary_arr = self._array(small_arr, UNPROCESSED, scale=0.5, spacing=0.05)
        
        linear_arr.move_to(LEFT * 3.5 + UP * 1.2)
        binary_arr.move_to(RIGHT * 3.5 + UP * 1.2)
        
        self.play(FadeIn(linear_arr), FadeIn(binary_arr), run_time=NORMAL)
        
        # Target: 13 (index 6)
        target = 13
        target_text = Text(f"Find: {target}", font_size=LABEL_SIZE, color=HIGHLIGHT)
        target_text.move_to(UP * 0.3)
        self.play(Write(target_text), run_time=FAST)
        
        # Animate both searches simultaneously
        # Linear: check 1, 3, 5, 7, 9, 11, 13 (7 steps)
        # Binary: check 7, 11, 13 (3 steps)
        
        linear_steps = [0, 1, 2, 3, 4, 5, 6]  # indices to check
        binary_steps = [(0, 7, 3), (4, 7, 5), (6, 7, 6)]  # (low, high, mid)
        
        linear_count = 0
        binary_count = 0
        
        linear_counter = Text(f"Steps: {linear_count}", font_size=SMALL_SIZE, color=LINEAR_COLOR)
        binary_counter = Text(f"Steps: {binary_count}", font_size=SMALL_SIZE, color=BINARY_COLOR)
        linear_counter.move_to(LEFT * 3.5 + DOWN * 0.5)
        binary_counter.move_to(RIGHT * 3.5 + DOWN * 0.5)
        
        self.play(Write(linear_counter), Write(binary_counter), run_time=FAST)
        
        # Run searches
        for i in range(max(len(linear_steps), len(binary_steps))):
            anims = []
            
            # Linear step
            if i < len(linear_steps):
                idx = linear_steps[i]
                anims.append(self._color_box(linear_arr[idx], ACTIVE_COMPARISON))
                linear_count += 1
            
            # Binary step
            if i < len(binary_steps):
                _, _, mid = binary_steps[i]
                anims.append(self._color_box(binary_arr[mid], ACTIVE_COMPARISON))
                binary_count += 1
            
            self.play(*anims, run_time=FAST)
            
            # Update counters
            new_linear = Text(f"Steps: {linear_count}", font_size=SMALL_SIZE, color=LINEAR_COLOR)
            new_binary = Text(f"Steps: {binary_count}", font_size=SMALL_SIZE, color=BINARY_COLOR)
            new_linear.move_to(linear_counter.get_center())
            new_binary.move_to(binary_counter.get_center())
            
            self.play(
                ReplacementTransform(linear_counter, new_linear),
                ReplacementTransform(binary_counter, new_binary),
                run_time=INSTANT
            )
            linear_counter = new_linear
            binary_counter = new_binary
            
            # Mark result
            if i < len(linear_steps):
                idx = linear_steps[i]
                color = FOUND_ELEMENT if small_arr[idx] == target else ELIMINATED
                self.play(self._color_box(linear_arr[idx], color), run_time=FAST)
            
            if i < len(binary_steps):
                _, _, mid = binary_steps[i]
                if small_arr[mid] == target:
                    self.play(self._color_box(binary_arr[mid], FOUND_ELEMENT), run_time=FAST)
                elif small_arr[mid] < target:
                    self.play(self._color_box(binary_arr[mid], ELIMINATED), run_time=FAST)
                else:
                    self.play(self._color_box(binary_arr[mid], ELIMINATED), run_time=FAST)
        
        self.wait(PAUSE)
        
        # Scaling comparison
        scaling_title = Text("As list size grows...", font_size=BODY_SIZE, color=TEXT_PRIMARY)
        scaling_title.move_to(DOWN * 1.5)
        self.play(Write(scaling_title), run_time=FAST)
        
        # Table of comparisons
        table_data = [
            ("Size", "Linear", "Binary"),
            ("100", "100", "7"),
            ("1,000", "1,000", "10"),
            ("1,000,000", "1,000,000", "20"),
            ("1 Billion", "1,000,000,000", "30"),
        ]
        
        table = VGroup()
        for i, (size, linear, binary) in enumerate(table_data):
            if i == 0:
                row = VGroup(
                    Text(size, font_size=SMALL_SIZE, color=TEXT_SECONDARY),
                    Text(linear, font_size=SMALL_SIZE, color=LINEAR_COLOR),
                    Text(binary, font_size=SMALL_SIZE, color=BINARY_COLOR)
                )
            else:
                row = VGroup(
                    Text(size, font_size=SMALL_SIZE, color=TEXT_SECONDARY),
                    Text(linear, font_size=SMALL_SIZE, color=LINEAR_COLOR),
                    Text(binary, font_size=SMALL_SIZE, color=BINARY_COLOR)
                )
            row.arrange(RIGHT, buff=1.2)
            table.add(row)
        
        table.arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        table.move_to(DOWN * 2.5)
        
        self.play(
            LaggedStart(*[FadeIn(row) for row in table], lag_ratio=0.1),
            run_time=SLOW
        )
        self.wait(LONG_PAUSE)
    
    # ==================== SCENE 5: BIG O VISUALIZATION ====================
    
    def _big_o_scene(self):
        """Visualize Big O growth curves."""
        # Title
        title = self._title("Big O Notation")
        self.play(Write(title), run_time=NORMAL)
        
        # Explanation
        explanation = Text("Measures how operations grow with input size", 
                          font_size=BODY_SIZE, color=TEXT_SECONDARY)
        explanation.move_to(UP * 2.2)
        self.play(Write(explanation), run_time=FAST)
        
        # Create axes without LaTeX labels
        axes = Axes(
            x_range=[0, 20, 5],
            y_range=[0, 100, 20],
            x_length=8,
            y_length=4,
            axis_config={"color": TEXT_SECONDARY, "include_tip": True, "include_numbers": False},
        )
        axes.move_to(DOWN * 0.5)
        
        # Add custom axis labels (avoiding LaTeX)
        x_nums = VGroup()
        for x in [5, 10, 15, 20]:
            num = Text(str(x), font_size=TINY_SIZE, color=TEXT_SECONDARY)
            num.next_to(axes.c2p(x, 0), DOWN, buff=0.15)
            x_nums.add(num)
        
        y_nums = VGroup()
        for y in [20, 40, 60, 80, 100]:
            num = Text(str(y), font_size=TINY_SIZE, color=TEXT_SECONDARY)
            num.next_to(axes.c2p(0, y), LEFT, buff=0.15)
            y_nums.add(num)
        
        # Labels
        x_label = Text("Input Size (n)", font_size=SMALL_SIZE, color=TEXT_SECONDARY)
        x_label.next_to(axes.x_axis, DOWN, buff=0.4)
        
        y_label = Text("Operations", font_size=SMALL_SIZE, color=TEXT_SECONDARY)
        y_label.next_to(axes.y_axis, LEFT, buff=0.5)
        y_label.rotate(PI/2)
        
        self.play(Create(axes), FadeIn(x_nums), FadeIn(y_nums), Write(x_label), Write(y_label), run_time=NORMAL)
        self.wait(PAUSE)
        
        # O(1) - Constant
        o_1_graph = axes.plot(lambda x: 5, x_range=[0.1, 20], color=O_1)
        o_1_label = Text("O(1)", font_size=SMALL_SIZE, color=O_1)
        o_1_label.next_to(o_1_graph.get_end(), RIGHT, buff=0.2)
        
        self.play(Create(o_1_graph), Write(o_1_label), run_time=NORMAL)
        self.wait(0.3)
        
        # O(log n) - Logarithmic
        o_log_graph = axes.plot(lambda x: 10 * math.log2(max(x, 1)) + 5, x_range=[1, 20], color=O_LOG_N)
        o_log_label = Text("O(log n)", font_size=SMALL_SIZE, color=O_LOG_N)
        o_log_label.next_to(o_log_graph.get_end(), RIGHT, buff=0.2)
        
        self.play(Create(o_log_graph), Write(o_log_label), run_time=NORMAL)
        self.wait(0.3)
        
        # O(n) - Linear
        o_n_graph = axes.plot(lambda x: 5 * x, x_range=[0.1, 20], color=O_N)
        o_n_label = Text("O(n)", font_size=SMALL_SIZE, color=O_N)
        o_n_label.next_to(o_n_graph.get_end(), UP, buff=0.2)
        
        self.play(Create(o_n_graph), Write(o_n_label), run_time=NORMAL)
        self.wait(0.3)
        
        # O(n²) - Quadratic (partial, scaled down)
        o_n2_graph = axes.plot(lambda x: 0.25 * x**2, x_range=[0.1, 20], color=O_N_SQUARED)
        o_n2_label = Text("O(n²)", font_size=SMALL_SIZE, color=O_N_SQUARED)
        o_n2_label.next_to(o_n2_graph.get_end(), UP, buff=0.2)
        
        self.play(Create(o_n2_graph), Write(o_n2_label), run_time=NORMAL)
        self.wait(PAUSE)
        
        # Highlight binary vs linear
        highlight_text = Text("Binary Search O(log n) grows much slower than Linear O(n)", 
                             font_size=LABEL_SIZE, color=TEXT_ACCENT)
        highlight_text.move_to(DOWN * 3)
        
        self.play(
            o_log_graph.animate.set_stroke(width=6),
            o_n_graph.animate.set_stroke(width=6),
            Write(highlight_text),
            run_time=NORMAL
        )
        self.wait(LONG_PAUSE)
        
        # Key insight
        self.play(FadeOut(highlight_text), run_time=FAST)
        
        insight = Text("Big O measures growth rate, not exact time!", 
                      font_size=BODY_SIZE, color=HIGHLIGHT)
        insight.move_to(DOWN * 3)
        self.play(Write(insight), run_time=NORMAL)
        self.wait(LONG_PAUSE)
    
    # ==================== SCENE 6: SUMMARY ====================
    
    def _summary_scene(self):
        """Final summary and key takeaways."""
        # Title
        title = self._title("Key Takeaways")
        self.play(Write(title), run_time=NORMAL)
        
        # Takeaways
        takeaways = [
            ("1.", "Linear Search: O(n) - simple but slow for large lists", LINEAR_COLOR),
            ("2.", "Binary Search: O(log n) - fast but requires sorted data", BINARY_COLOR),
            ("3.", "Big O measures growth rate, not seconds", TEXT_ACCENT),
            ("4.", "Choosing the right algorithm matters at scale", HIGHLIGHT),
        ]
        
        items = VGroup()
        for num, text, color in takeaways:
            num_text = Text(num, font_size=BODY_SIZE, color=TEXT_PRIMARY)
            content = Text(text, font_size=LABEL_SIZE, color=color)
            content.next_to(num_text, RIGHT, buff=0.2)
            row = VGroup(num_text, content)
            items.add(row)
        
        items.arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        items.move_to(UP * 0.5)
        
        self.play(
            LaggedStart(*[FadeIn(item, shift=LEFT * 0.3) for item in items], lag_ratio=0.2),
            run_time=SLOW
        )
        self.wait(PAUSE)
        
        # Final comparison box
        comparison = VGroup()
        
        vs_text = Text("At 1 Billion elements:", font_size=BODY_SIZE, color=TEXT_PRIMARY)
        linear_result = Text("Linear: 1,000,000,000 operations", font_size=LABEL_SIZE, color=LINEAR_COLOR)
        binary_result = Text("Binary: ~30 operations", font_size=LABEL_SIZE, color=BINARY_COLOR)
        
        linear_result.next_to(vs_text, DOWN, buff=0.3)
        binary_result.next_to(linear_result, DOWN, buff=0.2)
        
        comparison.add(vs_text, linear_result, binary_result)
        comparison.move_to(DOWN * 2)
        
        self.play(
            LaggedStart(*[Write(t) for t in comparison], lag_ratio=0.3),
            run_time=SLOW
        )
        self.wait(PAUSE)
        
        # Final message
        final = Text("Algorithm efficiency can make impossible tasks possible!", 
                    font_size=BODY_SIZE, color=FOUND_ELEMENT)
        final.move_to(DOWN * 3.3)
        self.play(Write(final), run_time=NORMAL)
        self.wait(LONG_PAUSE)


# Individual scene classes for separate rendering
class IntroScene(Scene):
    """Introduction scene only."""
    def construct(self):
        anim = Chapter1Animation()
        self.camera.background_color = BACKGROUND_COLOR
        anim._intro_scene = lambda: Chapter1Animation._intro_scene(self)
        Chapter1Animation._intro_scene(self)


class LinearSearchScene(Scene):
    """Linear search scene only."""
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        Chapter1Animation._linear_search_scene(self)


class BinarySearchScene(Scene):
    """Binary search scene only."""
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        Chapter1Animation._binary_search_scene(self)


class ComparisonScene(Scene):
    """Comparison scene only."""
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        Chapter1Animation._comparison_scene(self)


class BigOScene(Scene):
    """Big O visualization scene only."""
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        Chapter1Animation._big_o_scene(self)


class SummaryScene(Scene):
    """Summary scene only."""
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        Chapter1Animation._summary_scene(self)
