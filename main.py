#!/usr/bin/env python3
"""
Quick Sort vs Merge Sort - Educational Animation
================================================
Demonstrates Divide & Conquer with clear step-by-step visualization.
HD quality, no overlapping, full visibility.

Usage:
    manim -pql main.py FullAnimation   # Preview (480p)
    manim -pqh main.py FullAnimation   # HD quality (1080p)
"""
import sys
sys.path.insert(0, '/home/hg/Desktop/algorthims/quickSortVsMergeSort')

from manim import *

# Import config
from config.colors import (
    BACKGROUND_COLOR, TEXT_PRIMARY, TEXT_SECONDARY,
    UNPROCESSED, ACTIVE_COMPARISON, PIVOT, CORRECTLY_PLACED, TEMPORARY_STORAGE,
    SUBARRAY_LEFT, SUBARRAY_RIGHT, COMPLEXITY_GOOD, COMPLEXITY_BAD
)
from config.fonts import TITLE_SIZE, SUBTITLE_SIZE, HEADING_SIZE, BODY_SIZE, LABEL_SIZE, SMALL_SIZE

# ============== ANIMATION TIMING (Normal Speed) ==============
FAST = 0.6
NORMAL = 1.0
SLOW = 1.5
PAUSE = 0.8

# ============== SAFE LAYOUT ZONES ==============
# Screen bounds: approximately -7 to 7 horizontal, -4 to 4 vertical
TITLE_Y = 3.3           # Title at very top
STEP_Y = 2.3            # Step label below title
ARRAY_Y = 1.0           # Main array area
LEVEL1_Y = -0.5         # First recursion level
LEVEL2_Y = -2.0         # Second recursion level
RESULT_Y = -3.0         # Final result area
SAFE_LEFT = -6.0        # Safe left margin
SAFE_RIGHT = 6.0        # Safe right margin

# Demo array - 5 elements for clarity
DEMO_ARRAY = [8, 3, 7, 4, 2]


class FullAnimation(Scene):
    """
    Complete educational animation demonstrating:
    1. Quick Sort with Divide & Conquer
    2. Merge Sort with Divide & Conquer
    3. Side-by-side comparison
    4. Summary and key takeaways
    """
    
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        
        # Scene 1: Introduction
        self._intro_scene()
        self._clear()
        
        # Scene 2: Quick Sort - Full D&C Demonstration
        self._quick_sort_full()
        self._clear()
        
        # Scene 3: Merge Sort - Full D&C Demonstration  
        self._merge_sort_full()
        self._clear()
        
        # Scene 4: Side-by-Side Comparison
        self._comparison_scene()
        self._clear()
        
        # Scene 5: Summary
        self._summary_scene()
    
    def _clear(self):
        """Smooth scene transition."""
        if self.mobjects:
            self.play(*[FadeOut(m) for m in self.mobjects], run_time=FAST)
        self.wait(0.3)
    
    # ==================== HELPER METHODS ====================
    
    def _title(self, text):
        """Create title at safe top position."""
        t = Text(text, font_size=HEADING_SIZE, color=TEXT_PRIMARY)
        t.move_to(UP * TITLE_Y)
        return t
    
    def _step_label(self, text, color=TEXT_SECONDARY):
        """Create step indicator below title."""
        s = Text(text, font_size=BODY_SIZE, color=color)
        s.move_to(UP * STEP_Y)
        return s
    
    def _bar(self, value, color=UNPROCESSED, scale=1.0):
        """Create a single bar with value label."""
        grp = VGroup()
        
        rect = RoundedRectangle(
            width=0.7 * scale,
            height=value * 0.35 * scale,
            corner_radius=0.05 * scale,
            fill_color=color,
            fill_opacity=0.9,
            stroke_color=color,
            stroke_width=2
        )
        
        lbl = Text(str(value), font_size=int(18 * scale), color=TEXT_PRIMARY)
        lbl.move_to(rect.get_center())
        
        grp.add(rect, lbl)
        grp.value = value
        return grp
    
    def _array(self, values, color=UNPROCESSED, scale=1.0, buff=0.15):
        """Create array of bars."""
        arr = VGroup()
        for v in values:
            arr.add(self._bar(v, color, scale))
        arr.arrange(RIGHT, buff=buff * scale)
        return arr
    
    def _color(self, bar, color):
        """Return color change animation."""
        return bar[0].animate.set_fill(color).set_stroke(color)
    
    # ==================== SCENE 1: INTRODUCTION ====================
    
    def _intro_scene(self):
        """Introduction showing the problem: sorting an array."""
        # Main title
        title = Text("Quick Sort vs Merge Sort", font_size=TITLE_SIZE, color=TEXT_PRIMARY)
        title.move_to(UP * 2)
        
        subtitle = Text("Divide and Conquer Algorithms", font_size=SUBTITLE_SIZE, color=TEXT_SECONDARY)
        subtitle.next_to(title, DOWN, buff=0.4)
        
        self.play(Write(title), run_time=SLOW)
        self.wait(PAUSE)
        self.play(FadeIn(subtitle, shift=UP * 0.2), run_time=NORMAL)
        self.wait(PAUSE)
        
        # Show unsorted array
        arr = self._array(DEMO_ARRAY, UNPROCESSED, scale=0.9)
        arr.move_to(DOWN * 0.5)
        
        arr_label = Text("Unsorted Array: [8, 3, 7, 4, 2]", font_size=LABEL_SIZE, color=TEXT_SECONDARY)
        arr_label.next_to(arr, DOWN, buff=0.5)
        
        self.play(
            LaggedStart(*[FadeIn(b, shift=UP * 0.3) for b in arr], lag_ratio=0.1),
            run_time=NORMAL
        )
        self.play(Write(arr_label), run_time=FAST)
        self.wait(PAUSE)
        
        # Transform to sorted
        sorted_arr = self._array(sorted(DEMO_ARRAY), CORRECTLY_PLACED, scale=0.9)
        sorted_arr.move_to(arr.get_center())
        
        sorted_label = Text("Goal: [2, 3, 4, 7, 8]", font_size=LABEL_SIZE, color=CORRECTLY_PLACED)
        sorted_label.next_to(sorted_arr, DOWN, buff=0.5)
        
        self.play(
            ReplacementTransform(arr, sorted_arr),
            ReplacementTransform(arr_label, sorted_label),
            run_time=SLOW
        )
        self.wait(PAUSE)
    
    # ==================== SCENE 2: QUICK SORT FULL D&C ====================
    
    def _quick_sort_full(self):
        """Complete Quick Sort demonstration with Divide & Conquer."""
        # Title
        title = self._title("Quick Sort: Divide & Conquer")
        self.play(Write(title), run_time=NORMAL)
        
        # === STEP 1: Show original array ===
        step = self._step_label("Step 1: Choose Pivot (last element)")
        self.play(Write(step), run_time=FAST)
        
        values = [8, 3, 7, 4, 2]
        arr = self._array(values, UNPROCESSED, scale=0.85)
        arr.move_to(UP * ARRAY_Y)
        
        self.play(FadeIn(arr), run_time=NORMAL)
        self.wait(PAUSE)
        
        # Highlight pivot
        pivot_lbl = Text("Pivot = 2", font_size=LABEL_SIZE, color=PIVOT)
        pivot_lbl.next_to(arr[4], DOWN, buff=0.3)
        
        self.play(self._color(arr[4], PIVOT), FadeIn(pivot_lbl), run_time=NORMAL)
        self.wait(PAUSE)
        
        # === STEP 2: Compare each element with pivot ===
        step2 = self._step_label("Step 2: Compare each element with pivot")
        self.play(ReplacementTransform(step, step2), run_time=FAST)
        
        # Compare: 8>2, 3>2, 7>2, 4>2 (all go to right)
        compare_results = ["8 > 2", "3 > 2", "7 > 2", "4 > 2"]
        for i in range(4):
            # Highlight comparison
            self.play(self._color(arr[i], ACTIVE_COMPARISON), run_time=FAST)
            self.wait(0.3)
            # Result - all are greater
            self.play(self._color(arr[i], SUBARRAY_RIGHT), run_time=FAST)
            self.wait(0.2)
        
        self.wait(PAUSE)
        
        # === STEP 3: Partition result ===
        step3 = self._step_label("Step 3: Pivot goes to final position")
        self.play(ReplacementTransform(step2, step3), FadeOut(pivot_lbl), run_time=FAST)
        
        # Show partition result: [2] is sorted, [8,3,7,4] needs recursion
        pivot_done = self._bar(2, CORRECTLY_PLACED, scale=0.8)
        pivot_done.move_to(LEFT * 4.5 + UP * LEVEL1_Y)
        
        right_sub = self._array([8, 3, 7, 4], SUBARRAY_RIGHT, scale=0.75)
        right_sub.move_to(RIGHT * 1.5 + UP * LEVEL1_Y)
        
        done_lbl = Text("In final position!", font_size=SMALL_SIZE, color=CORRECTLY_PLACED)
        done_lbl.next_to(pivot_done, DOWN, buff=0.25)
        
        recurse_lbl = Text("Recurse on this", font_size=SMALL_SIZE, color=SUBARRAY_RIGHT)
        recurse_lbl.next_to(right_sub, DOWN, buff=0.25)
        
        self.play(
            arr.animate.set_opacity(0.25),
            FadeIn(pivot_done),
            FadeIn(right_sub),
            FadeIn(done_lbl),
            FadeIn(recurse_lbl),
            run_time=NORMAL
        )
        self.wait(PAUSE)
        
        # === STEP 4: Continue recursion on [8,3,7,4] with pivot=4 ===
        step4 = self._step_label("Step 4: Recurse - pivot = 4")
        self.play(ReplacementTransform(step3, step4), run_time=FAST)
        
        # Highlight new pivot
        self.play(self._color(right_sub[3], PIVOT), run_time=NORMAL)
        self.wait(0.3)
        
        # Compare: 8>4 (right), 3<4 (left), 7>4 (right)
        self.play(self._color(right_sub[0], ACTIVE_COMPARISON), run_time=FAST)
        self.wait(0.2)
        self.play(self._color(right_sub[0], SUBARRAY_RIGHT), run_time=FAST)  # 8 > 4
        
        self.play(self._color(right_sub[1], ACTIVE_COMPARISON), run_time=FAST)
        self.wait(0.2)
        self.play(self._color(right_sub[1], SUBARRAY_LEFT), run_time=FAST)   # 3 < 4
        
        self.play(self._color(right_sub[2], ACTIVE_COMPARISON), run_time=FAST)
        self.wait(0.2)
        self.play(self._color(right_sub[2], SUBARRAY_RIGHT), run_time=FAST)  # 7 > 4
        
        self.wait(PAUSE)
        
        # === STEP 5: Show recursion tree result ===
        step5 = self._step_label("Step 5: Recursion continues...")
        self.play(ReplacementTransform(step4, step5), run_time=FAST)
        
        # Level 2: [3] | 4 | [8,7]
        elem_3 = self._bar(3, CORRECTLY_PLACED, scale=0.65)
        elem_3.move_to(LEFT * 1 + UP * LEVEL2_Y)
        
        elem_4 = self._bar(4, CORRECTLY_PLACED, scale=0.65)
        elem_4.move_to(RIGHT * 1 + UP * LEVEL2_Y)
        
        sub_87 = self._array([8, 7], SUBARRAY_RIGHT, scale=0.6)
        sub_87.move_to(RIGHT * 4 + UP * LEVEL2_Y)
        
        self.play(
            right_sub.animate.set_opacity(0.25),
            FadeOut(recurse_lbl),
            FadeIn(elem_3),
            FadeIn(elem_4),
            FadeIn(sub_87),
            run_time=NORMAL
        )
        self.wait(PAUSE)
        
        # Final: [7, 8] sorted
        self.play(
            self._color(sub_87[0], CORRECTLY_PLACED),
            self._color(sub_87[1], CORRECTLY_PLACED),
            run_time=NORMAL
        )
        self.wait(PAUSE)
        
        # === FINAL RESULT ===
        step_final = self._step_label("Result: Array is sorted!", color=CORRECTLY_PLACED)
        self.play(ReplacementTransform(step5, step_final), run_time=FAST)
        
        final_arr = self._array([2, 3, 4, 7, 8], CORRECTLY_PLACED, scale=0.85)
        final_arr.move_to(UP * RESULT_Y)
        
        final_lbl = Text("[2, 3, 4, 7, 8]", font_size=LABEL_SIZE, color=CORRECTLY_PLACED)
        final_lbl.next_to(final_arr, DOWN, buff=0.3)
        
        self.play(FadeIn(final_arr), Write(final_lbl), run_time=SLOW)
        self.wait(PAUSE)
        
        # Key insight
        insight = Text("Key: Pivot always ends up in its correct final position!", 
                      font_size=SMALL_SIZE, color=PIVOT)
        insight.to_edge(DOWN, buff=0.4)
        self.play(Write(insight), run_time=NORMAL)
        self.wait(PAUSE)
    
    # ==================== SCENE 3: MERGE SORT FULL D&C ====================
    
    def _merge_sort_full(self):
        """Complete Merge Sort demonstration with Divide & Conquer."""
        # Title
        title = self._title("Merge Sort: Divide & Conquer")
        self.play(Write(title), run_time=NORMAL)
        
        # === DIVIDE PHASE ===
        step = self._step_label("Divide Phase: Split until single elements")
        self.play(Write(step), run_time=FAST)
        
        # Level 0: Original array
        values = [8, 3, 7, 4, 2]
        level0 = self._array(values, UNPROCESSED, scale=0.75)
        level0.move_to(UP * ARRAY_Y)
        
        l0_label = Text("[8, 3, 7, 4, 2]", font_size=SMALL_SIZE, color=TEXT_SECONDARY)
        l0_label.next_to(level0, LEFT, buff=0.4)
        
        self.play(FadeIn(level0), FadeIn(l0_label), run_time=NORMAL)
        self.wait(PAUSE)
        
        # Level 1: Split into [8,3] and [7,4,2]
        left1 = self._array([8, 3], SUBARRAY_LEFT, scale=0.65)
        right1 = self._array([7, 4, 2], SUBARRAY_RIGHT, scale=0.65)
        
        left1.move_to(LEFT * 3.5 + UP * LEVEL1_Y)
        right1.move_to(RIGHT * 2.5 + UP * LEVEL1_Y)
        
        # Connection lines
        line_l1 = Line(level0.get_bottom() + DOWN * 0.1, left1.get_top() + UP * 0.1,
                      color=TEXT_SECONDARY, stroke_width=2)
        line_r1 = Line(level0.get_bottom() + DOWN * 0.1, right1.get_top() + UP * 0.1,
                      color=TEXT_SECONDARY, stroke_width=2)
        
        self.play(
            Create(line_l1), Create(line_r1),
            FadeIn(left1), FadeIn(right1),
            run_time=NORMAL
        )
        self.wait(PAUSE)
        
        # Level 2: Single elements (base case)
        singles = VGroup()
        single_vals = [8, 3, 7, 4, 2]
        single_positions = [
            LEFT * 5, LEFT * 3,  # from [8,3]
            RIGHT * 1, RIGHT * 3, RIGHT * 5  # from [7,4,2]
        ]
        
        for val, pos in zip(single_vals, single_positions):
            s = self._bar(val, CORRECTLY_PLACED, scale=0.55)
            s.move_to(pos + UP * LEVEL2_Y)
            singles.add(s)
        
        lines2 = VGroup()
        lines2.add(Line(left1.get_bottom() + DOWN * 0.1, singles[0].get_top() + UP * 0.1,
                       color=TEXT_SECONDARY, stroke_width=1.5))
        lines2.add(Line(left1.get_bottom() + DOWN * 0.1, singles[1].get_top() + UP * 0.1,
                       color=TEXT_SECONDARY, stroke_width=1.5))
        lines2.add(Line(right1.get_bottom() + DOWN * 0.1, singles[2].get_top() + UP * 0.1,
                       color=TEXT_SECONDARY, stroke_width=1.5))
        lines2.add(Line(right1.get_bottom() + DOWN * 0.1, singles[3].get_top() + UP * 0.1,
                       color=TEXT_SECONDARY, stroke_width=1.5))
        lines2.add(Line(right1.get_bottom() + DOWN * 0.1, singles[4].get_top() + UP * 0.1,
                       color=TEXT_SECONDARY, stroke_width=1.5))
        
        self.play(Create(lines2), FadeIn(singles), run_time=NORMAL)
        
        base_label = Text("Base case: single elements are sorted!", font_size=SMALL_SIZE, color=CORRECTLY_PLACED)
        base_label.move_to(DOWN * 0.3)
        self.play(Write(base_label), run_time=FAST)
        self.wait(PAUSE)
        
        # === MERGE PHASE ===
        step2 = self._step_label("Merge Phase: Combine in sorted order", color=TEMPORARY_STORAGE)
        self.play(
            ReplacementTransform(step, step2),
            FadeOut(base_label),
            run_time=FAST
        )
        
        # Merge [8] + [3] -> [3,8]
        merge1_label = Text("Merge [8]+[3] → [3,8]", font_size=SMALL_SIZE, color=TEMPORARY_STORAGE)
        merge1_label.move_to(LEFT * 4 + DOWN * 1.0)
        
        merged_38 = self._array([3, 8], TEMPORARY_STORAGE, scale=0.55)
        merged_38.move_to(LEFT * 4 + DOWN * 1.8)
        
        self.play(Write(merge1_label), run_time=FAST)
        self.play(FadeIn(merged_38), run_time=NORMAL)
        self.wait(0.5)
        
        # Merge [7]+[4]+[2] step by step -> [2,4,7]
        merge2_label = Text("Merge [7]+[4]+[2] → [2,4,7]", font_size=SMALL_SIZE, color=TEMPORARY_STORAGE)
        merge2_label.move_to(RIGHT * 3 + DOWN * 1.0)
        
        merged_247 = self._array([2, 4, 7], TEMPORARY_STORAGE, scale=0.55)
        merged_247.move_to(RIGHT * 3 + DOWN * 1.8)
        
        self.play(Write(merge2_label), run_time=FAST)
        self.play(FadeIn(merged_247), run_time=NORMAL)
        self.wait(PAUSE)
        
        # Final merge: [3,8] + [2,4,7] -> [2,3,4,7,8]
        step3 = self._step_label("Final Merge: [3,8] + [2,4,7]", color=CORRECTLY_PLACED)
        self.play(ReplacementTransform(step2, step3), run_time=FAST)
        
        final_arr = self._array([2, 3, 4, 7, 8], CORRECTLY_PLACED, scale=0.8)
        final_arr.move_to(DOWN * RESULT_Y)
        
        final_lbl = Text("Result: [2, 3, 4, 7, 8]", font_size=LABEL_SIZE, color=CORRECTLY_PLACED)
        final_lbl.next_to(final_arr, DOWN, buff=0.3)
        
        self.play(FadeIn(final_arr), Write(final_lbl), run_time=SLOW)
        self.wait(PAUSE)
        
        # Key insight
        insight = Text("Key: Merging sorted subarrays is efficient - O(n)!", 
                      font_size=SMALL_SIZE, color=TEMPORARY_STORAGE)
        insight.to_edge(DOWN, buff=0.4)
        self.play(Write(insight), run_time=NORMAL)
        self.wait(PAUSE)
    
    # ==================== SCENE 4: COMPARISON ====================
    
    def _comparison_scene(self):
        """Side-by-side comparison of both algorithms."""
        title = self._title("Algorithm Comparison")
        self.play(Write(title), run_time=NORMAL)
        
        # Divider
        divider = DashedLine(UP * 2.8, DOWN * 3.0, color=TEXT_SECONDARY, stroke_width=1.5)
        self.play(Create(divider), run_time=FAST)
        
        # Headers
        qs_head = Text("Quick Sort", font_size=BODY_SIZE, color=PIVOT)
        ms_head = Text("Merge Sort", font_size=BODY_SIZE, color=TEMPORARY_STORAGE)
        qs_head.move_to(LEFT * 3.5 + UP * 2.3)
        ms_head.move_to(RIGHT * 3.5 + UP * 2.3)
        
        self.play(Write(qs_head), Write(ms_head), run_time=FAST)
        
        # Initial arrays
        qs_arr = self._array([8, 3, 7, 4, 2], UNPROCESSED, scale=0.5)
        ms_arr = self._array([8, 3, 7, 4, 2], UNPROCESSED, scale=0.5)
        qs_arr.move_to(LEFT * 3.5 + UP * 1.3)
        ms_arr.move_to(RIGHT * 3.5 + UP * 1.3)
        
        self.play(FadeIn(qs_arr), FadeIn(ms_arr), run_time=NORMAL)
        self.wait(PAUSE)
        
        # Quick Sort approach
        qs_approach = Text("Approach: Pivot + Partition", font_size=SMALL_SIZE, color=PIVOT)
        qs_approach.next_to(qs_arr, DOWN, buff=0.3)
        
        ms_approach = Text("Approach: Split + Merge", font_size=SMALL_SIZE, color=TEMPORARY_STORAGE)
        ms_approach.next_to(ms_arr, DOWN, buff=0.3)
        
        self.play(Write(qs_approach), Write(ms_approach), run_time=FAST)
        
        # Animate pivoting vs splitting
        self.play(self._color(qs_arr[4], PIVOT), run_time=NORMAL)
        self.play(
            *[self._color(ms_arr[i], SUBARRAY_LEFT) for i in range(2)],
            *[self._color(ms_arr[i], SUBARRAY_RIGHT) for i in range(2, 5)],
            run_time=NORMAL
        )
        self.wait(PAUSE)
        
        # Final sorted arrays
        qs_final = self._array([2, 3, 4, 7, 8], CORRECTLY_PLACED, scale=0.5)
        ms_final = self._array([2, 3, 4, 7, 8], CORRECTLY_PLACED, scale=0.5)
        qs_final.move_to(LEFT * 3.5 + DOWN * 0.5)
        ms_final.move_to(RIGHT * 3.5 + DOWN * 0.5)
        
        self.play(FadeIn(qs_final), FadeIn(ms_final), run_time=NORMAL)
        self.wait(PAUSE)
        
        # Key differences
        qs_props = VGroup(
            Text("In-place: Yes", font_size=SMALL_SIZE, color=COMPLEXITY_GOOD),
            Text("Space: O(log n)", font_size=SMALL_SIZE, color=COMPLEXITY_GOOD),
            Text("Worst: O(n²)", font_size=SMALL_SIZE, color=COMPLEXITY_BAD),
        )
        qs_props.arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        qs_props.move_to(LEFT * 3.5 + DOWN * 1.8)
        
        ms_props = VGroup(
            Text("In-place: No", font_size=SMALL_SIZE, color=COMPLEXITY_BAD),
            Text("Space: O(n)", font_size=SMALL_SIZE, color=COMPLEXITY_BAD),
            Text("Worst: O(n log n)", font_size=SMALL_SIZE, color=COMPLEXITY_GOOD),
        )
        ms_props.arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        ms_props.move_to(RIGHT * 3.5 + DOWN * 1.8)
        
        self.play(
            LaggedStart(*[FadeIn(p) for p in qs_props], lag_ratio=0.1),
            LaggedStart(*[FadeIn(p) for p in ms_props], lag_ratio=0.1),
            run_time=SLOW
        )
        self.wait(PAUSE)
    
    # ==================== SCENE 5: SUMMARY ====================
    
    def _summary_scene(self):
        """Final summary with comparison table."""
        title = self._title("Summary")
        self.play(Write(title), run_time=NORMAL)
        
        # Comparison table
        headers = VGroup(
            Text("", font_size=SMALL_SIZE),
            Text("Quick Sort", font_size=SMALL_SIZE, color=PIVOT),
            Text("Merge Sort", font_size=SMALL_SIZE, color=TEMPORARY_STORAGE)
        )
        headers.arrange(RIGHT, buff=1.0)
        headers.move_to(UP * 1.8)
        
        rows_data = [
            ("Average", "O(n log n)", "O(n log n)", COMPLEXITY_GOOD, COMPLEXITY_GOOD),
            ("Worst", "O(n²)", "O(n log n)", COMPLEXITY_BAD, COMPLEXITY_GOOD),
            ("Space", "O(log n)", "O(n)", COMPLEXITY_GOOD, COMPLEXITY_BAD),
            ("Stable", "No", "Yes", COMPLEXITY_BAD, COMPLEXITY_GOOD),
            ("In-place", "Yes", "No", COMPLEXITY_GOOD, COMPLEXITY_BAD),
        ]
        
        table = VGroup(headers)
        for label, qs_val, ms_val, qs_color, ms_color in rows_data:
            row = VGroup(
                Text(label, font_size=SMALL_SIZE, color=TEXT_SECONDARY),
                Text(qs_val, font_size=SMALL_SIZE, color=qs_color),
                Text(ms_val, font_size=SMALL_SIZE, color=ms_color)
            )
            row.arrange(RIGHT, buff=1.0)
            table.add(row)
        
        table.arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        table.move_to(UP * 0.8)
        
        self.play(
            LaggedStart(*[FadeIn(row) for row in table], lag_ratio=0.1),
            run_time=SLOW
        )
        self.wait(PAUSE)
        
        # Key takeaways
        take1 = Text("Quick Sort: Faster in practice, lower memory", font_size=LABEL_SIZE, color=PIVOT)
        take2 = Text("Merge Sort: Predictable O(n log n), stable", font_size=LABEL_SIZE, color=TEMPORARY_STORAGE)
        take1.move_to(DOWN * 1.5)
        take2.next_to(take1, DOWN, buff=0.3)
        
        self.play(Write(take1), run_time=NORMAL)
        self.play(Write(take2), run_time=NORMAL)
        self.wait(PAUSE)
        
        # Final message
        final_msg = Text("Choose based on your requirements!", font_size=BODY_SIZE, color=CORRECTLY_PLACED)
        final_msg.move_to(DOWN * 2.8)
        self.play(Write(final_msg), run_time=NORMAL)
        self.wait(PAUSE)
