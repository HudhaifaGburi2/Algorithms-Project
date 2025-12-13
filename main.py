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
    
    # ==================== SCENE 2: QUICK SORT EXPLAINED ====================
    
    def _quick_sort_explained(self):
        """Quick Sort with D&C concept - single clean scene."""
        # Title at top
        title = self._create_title("Quick Sort")
        self.play(Write(title), run_time=NORMAL)
        
        # Step indicator
        step_text = Text("Step 1: Choose Pivot", font_size=BODY_SIZE, color=TEXT_SECONDARY)
        step_text.move_to(UP * CONTENT_TOP_Y)
        self.play(Write(step_text), run_time=FAST)
        
        # Array in middle area
        values = [8, 3, 7, 4, 2]
        array = self._create_array(values, UNPROCESSED, scale=0.85)
        array.move_to(UP * 0.8)
        
        self.play(FadeIn(array), run_time=NORMAL)
        self.wait(PAUSE)
        
        # Highlight pivot (last element = 2)
        pivot_marker = Text("Pivot = 2", font_size=LABEL_SIZE, color=PIVOT)
        pivot_marker.next_to(array[4], DOWN, buff=0.25)
        
        self.play(
            self._color_bar(array[4], PIVOT),
            FadeIn(pivot_marker),
            run_time=NORMAL
        )
        self.wait(PAUSE)
        
        # Step 2: Compare and Partition
        step2_text = Text("Step 2: Compare with Pivot", font_size=BODY_SIZE, color=TEXT_SECONDARY)
        step2_text.move_to(step_text.get_center())
        self.play(ReplacementTransform(step_text, step2_text), run_time=FAST)
        
        # Compare each element - all > 2
        for i in range(4):
            self.play(self._color_bar(array[i], ACTIVE_COMPARISON), run_time=FAST)
            self.wait(0.2)
            self.play(self._color_bar(array[i], SUBARRAY_RIGHT), run_time=FAST)
        
        self.wait(PAUSE)
        
        # Step 3: Partition result
        step3_text = Text("Step 3: Pivot in Final Position", font_size=BODY_SIZE, color=TEXT_SECONDARY)
        step3_text.move_to(step2_text.get_center())
        self.play(ReplacementTransform(step2_text, step3_text), run_time=FAST)
        
        # Show partition result below - pivot sorted, rest needs recursion
        result_y = -0.8
        
        pivot_sorted = self._create_bar(2, CORRECTLY_PLACED, scale=0.8)
        pivot_sorted.move_to(LEFT * 3.5 + UP * result_y)
        
        remaining = self._create_array([8, 3, 7, 4], SUBARRAY_RIGHT, scale=0.7)
        remaining.move_to(RIGHT * 1.5 + UP * result_y)
        
        sorted_label = Text("Sorted!", font_size=SMALL_SIZE, color=CORRECTLY_PLACED)
        sorted_label.next_to(pivot_sorted, DOWN, buff=0.2)
        
        recurse_label = Text("Need to sort", font_size=SMALL_SIZE, color=SUBARRAY_RIGHT)
        recurse_label.next_to(remaining, DOWN, buff=0.2)
        
        self.play(
            array.animate.set_opacity(0.3),
            FadeOut(pivot_marker),
            FadeIn(pivot_sorted),
            FadeIn(remaining),
            FadeIn(sorted_label),
            FadeIn(recurse_label),
            run_time=NORMAL
        )
        self.wait(PAUSE)
        
        # Step 4: Show recursion continues
        step4_text = Text("Step 4: Recurse on Subarrays", font_size=BODY_SIZE, color=TEXT_SECONDARY)
        step4_text.move_to(step3_text.get_center())
        self.play(ReplacementTransform(step3_text, step4_text), run_time=FAST)
        
        # Final sorted result at bottom
        final_y = -2.3
        final_array = self._create_array([2, 3, 4, 7, 8], CORRECTLY_PLACED, scale=0.8)
        final_array.move_to(UP * final_y)
        
        final_label = Text("Final: [2, 3, 4, 7, 8]", font_size=LABEL_SIZE, color=CORRECTLY_PLACED)
        final_label.next_to(final_array, DOWN, buff=0.3)
        
        self.play(
            FadeOut(remaining),
            FadeOut(recurse_label),
            pivot_sorted.animate.set_opacity(0.3),
            sorted_label.animate.set_opacity(0.3),
            FadeIn(final_array),
            Write(final_label),
            run_time=SLOW
        )
        self.wait(PAUSE)
    
    # ==================== SCENE 3: QUICK SORT COMPLEXITY ====================
    
    def _quick_sort_complexity(self):
        """Quick Sort complexity summary."""
        title = self._create_title("Quick Sort Complexity")
        self.play(Write(title), run_time=NORMAL)
        
        items = [
            ("Average Case:", "O(n log n)", COMPLEXITY_GOOD),
            ("Worst Case:", "O(n²)", COMPLEXITY_BAD),
            ("Space:", "O(log n)", COMPLEXITY_GOOD),
            ("In-place:", "Yes", COMPLEXITY_GOOD),
            ("Stable:", "No", COMPLEXITY_BAD),
        ]
        
        summary = VGroup()
        for label_text, value_text, color in items:
            label = Text(label_text, font_size=BODY_SIZE, color=TEXT_SECONDARY)
            value = Text(value_text, font_size=BODY_SIZE, color=color)
            value.next_to(label, RIGHT, buff=0.5)
            row = VGroup(label, value)
            summary.add(row)
        
        summary.arrange(DOWN, buff=0.35, aligned_edge=LEFT)
        summary.move_to(ORIGIN)
        
        self.play(
            LaggedStart(*[FadeIn(row, shift=LEFT * 0.2) for row in summary], lag_ratio=0.15),
            run_time=SLOW
        )
        self.wait(PAUSE)
    
    # ==================== SCENE 4: MERGE SORT EXPLAINED ====================
    
    def _merge_sort_explained(self):
        """Merge Sort with D&C concept - single clean scene."""
        # Title at top
        title = self._create_title("Merge Sort")
        self.play(Write(title), run_time=NORMAL)
        
        # Step 1: Divide
        step_text = Text("Step 1: Divide in Half", font_size=BODY_SIZE, color=TEXT_SECONDARY)
        step_text.move_to(UP * CONTENT_TOP_Y)
        self.play(Write(step_text), run_time=FAST)
        
        # Array in middle
        values = [8, 3, 7, 4, 2]
        array = self._create_array(values, UNPROCESSED, scale=0.85)
        array.move_to(UP * 0.8)
        
        self.play(FadeIn(array), run_time=NORMAL)
        self.wait(PAUSE)
        
        # Color halves
        mid = 2
        self.play(
            *[self._color_bar(array[i], SUBARRAY_LEFT) for i in range(mid)],
            *[self._color_bar(array[i], SUBARRAY_RIGHT) for i in range(mid, 5)],
            run_time=NORMAL
        )
        self.wait(PAUSE)
        
        # Split visually
        left_half = VGroup(*[array[i] for i in range(mid)])
        right_half = VGroup(*[array[i] for i in range(mid, 5)])
        
        self.play(
            left_half.animate.shift(LEFT * 1.2),
            right_half.animate.shift(RIGHT * 1.2),
            run_time=NORMAL
        )
        self.wait(PAUSE)
        
        # Step 2: Keep dividing
        step2_text = Text("Step 2: Divide Until Single Elements", font_size=BODY_SIZE, color=TEXT_SECONDARY)
        step2_text.move_to(step_text.get_center())
        self.play(ReplacementTransform(step_text, step2_text), run_time=FAST)
        
        # Show single elements
        singles_y = -0.8
        singles = VGroup()
        single_vals = [8, 3, 7, 4, 2]
        positions = [LEFT * 4, LEFT * 2, ORIGIN, RIGHT * 2, RIGHT * 4]
        
        for val, pos in zip(single_vals, positions):
            single = self._create_bar(val, CORRECTLY_PLACED, scale=0.65)
            single.move_to(pos + UP * singles_y)
            singles.add(single)
        
        self.play(
            left_half.animate.set_opacity(0.3),
            right_half.animate.set_opacity(0.3),
            LaggedStart(*[FadeIn(s) for s in singles], lag_ratio=0.1),
            run_time=NORMAL
        )
        self.wait(PAUSE)
        
        # Step 3: Merge
        step3_text = Text("Step 3: Merge in Sorted Order", font_size=BODY_SIZE, color=TEXT_SECONDARY)
        step3_text.move_to(step2_text.get_center())
        self.play(ReplacementTransform(step2_text, step3_text), run_time=FAST)
        
        # Final sorted at bottom
        final_y = -2.3
        final_array = self._create_array([2, 3, 4, 7, 8], CORRECTLY_PLACED, scale=0.8)
        final_array.move_to(UP * final_y)
        
        final_label = Text("Final: [2, 3, 4, 7, 8]", font_size=LABEL_SIZE, color=CORRECTLY_PLACED)
        final_label.next_to(final_array, DOWN, buff=0.3)
        
        self.play(
            singles.animate.set_opacity(0.3),
            FadeIn(final_array),
            Write(final_label),
            run_time=SLOW
        )
        self.wait(PAUSE)
    
    # ==================== SCENE 5: MERGE SORT COMPLEXITY ====================
    
    def _merge_sort_complexity(self):
        """Merge Sort complexity summary."""
        title = self._create_title("Merge Sort Complexity")
        self.play(Write(title), run_time=NORMAL)
        
        items = [
            ("Best Case:", "O(n log n)", COMPLEXITY_GOOD),
            ("Average Case:", "O(n log n)", COMPLEXITY_GOOD),
            ("Worst Case:", "O(n log n)", COMPLEXITY_GOOD),
            ("Space:", "O(n)", COMPLEXITY_BAD),
            ("Stable:", "Yes", COMPLEXITY_GOOD),
            ("In-place:", "No", COMPLEXITY_BAD),
        ]
        
        summary = VGroup()
        for label_text, value_text, color in items:
            label = Text(label_text, font_size=BODY_SIZE, color=TEXT_SECONDARY)
            value = Text(value_text, font_size=BODY_SIZE, color=color)
            value.next_to(label, RIGHT, buff=0.5)
            row = VGroup(label, value)
            summary.add(row)
        
        summary.arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        summary.move_to(ORIGIN)
        
        self.play(
            LaggedStart(*[FadeIn(row, shift=LEFT * 0.2) for row in summary], lag_ratio=0.12),
            run_time=SLOW
        )
        self.wait(PAUSE)
    
    # ==================== SCENE 6: SIDE-BY-SIDE COMPARISON ====================
    
    def _side_by_side_comparison(self):
        """Side-by-side comparison - clean layout."""
        title = self._create_title("Side-by-Side Comparison")
        self.play(Write(title), run_time=NORMAL)
        
        # Divider - stays within safe bounds
        divider = DashedLine(UP * 2.5, DOWN * 2.8, color=TEXT_SECONDARY, stroke_width=1.5, dash_length=0.12)
        self.play(Create(divider), run_time=FAST)
        
        # Labels at top of each side
        qs_title = Text("Quick Sort", font_size=BODY_SIZE, color=PIVOT)
        ms_title = Text("Merge Sort", font_size=BODY_SIZE, color=TEMPORARY_STORAGE)
        qs_title.move_to(LEFT * 3.5 + UP * 2.2)
        ms_title.move_to(RIGHT * 3.5 + UP * 2.2)
        
        self.play(Write(qs_title), Write(ms_title), run_time=FAST)
        
        # Initial arrays - smaller scale to fit
        values = [8, 3, 7, 4, 2]
        
        qs_array = self._create_array(values, UNPROCESSED, scale=0.55)
        ms_array = self._create_array(values, UNPROCESSED, scale=0.55)
        
        qs_array.move_to(LEFT * 3.5 + UP * 1.2)
        ms_array.move_to(RIGHT * 3.5 + UP * 1.2)
        
        self.play(FadeIn(qs_array), FadeIn(ms_array), run_time=NORMAL)
        self.wait(PAUSE)
        
        # Step labels
        qs_step = Text("Select Pivot", font_size=SMALL_SIZE, color=PIVOT)
        ms_step = Text("Split in Half", font_size=SMALL_SIZE, color=TEMPORARY_STORAGE)
        qs_step.next_to(qs_array, DOWN, buff=0.25)
        ms_step.next_to(ms_array, DOWN, buff=0.25)
        
        self.play(Write(qs_step), Write(ms_step), run_time=FAST)
        
        # Quick Sort: highlight pivot
        self.play(self._color_bar(qs_array[4], PIVOT), run_time=NORMAL)
        
        # Merge Sort: color halves
        self.play(
            *[self._color_bar(ms_array[i], SUBARRAY_LEFT) for i in range(2)],
            *[self._color_bar(ms_array[i], SUBARRAY_RIGHT) for i in range(2, 5)],
            run_time=NORMAL
        )
        self.wait(PAUSE)
        
        # Final sorted arrays
        qs_final = self._create_array([2, 3, 4, 7, 8], CORRECTLY_PLACED, scale=0.55)
        ms_final = self._create_array([2, 3, 4, 7, 8], CORRECTLY_PLACED, scale=0.55)
        
        qs_final.move_to(LEFT * 3.5 + DOWN * 0.8)
        ms_final.move_to(RIGHT * 3.5 + DOWN * 0.8)
        
        qs_done = Text("Sorted!", font_size=SMALL_SIZE, color=CORRECTLY_PLACED)
        ms_done = Text("Sorted!", font_size=SMALL_SIZE, color=CORRECTLY_PLACED)
        qs_done.next_to(qs_final, DOWN, buff=0.2)
        ms_done.next_to(ms_final, DOWN, buff=0.2)
        
        self.play(
            ReplacementTransform(qs_step, qs_done),
            ReplacementTransform(ms_step, ms_done),
            FadeIn(qs_final),
            FadeIn(ms_final),
            run_time=NORMAL
        )
        self.wait(PAUSE)
        
        # Key differences at bottom - within bounds
        qs_note = Text("In-place, O(log n) space", font_size=SMALL_SIZE, color=PIVOT)
        ms_note = Text("Extra O(n) space", font_size=SMALL_SIZE, color=TEMPORARY_STORAGE)
        
        qs_note.move_to(LEFT * 3.5 + DOWN * 2.3)
        ms_note.move_to(RIGHT * 3.5 + DOWN * 2.3)
        
        self.play(Write(qs_note), Write(ms_note), run_time=NORMAL)
        self.wait(PAUSE)
    
    # ==================== SCENE 7: FINAL SUMMARY ====================
    
    def _final_summary(self):
        """Final summary and takeaways."""
        title = self._create_title("Summary")
        self.play(Write(title), run_time=NORMAL)
        
        # Comparison table - positioned safely
        table_data = [
            ("", "Quick Sort", "Merge Sort"),
            ("Worst Case", "O(n²)", "O(n log n)"),
            ("Space", "O(log n)", "O(n)"),
            ("Stable", "No", "Yes"),
            ("In-place", "Yes", "No"),
        ]
        
        table = VGroup()
        for i, (label, qs, ms) in enumerate(table_data):
            if i == 0:
                row = VGroup(
                    Text(label, font_size=SMALL_SIZE, color=TEXT_SECONDARY),
                    Text(qs, font_size=SMALL_SIZE, color=PIVOT),
                    Text(ms, font_size=SMALL_SIZE, color=TEMPORARY_STORAGE)
                )
            else:
                qs_good = "log" in qs or qs == "Yes"
                ms_good = "log" in ms or ms == "Yes" or "n log n" in ms
                row = VGroup(
                    Text(label, font_size=SMALL_SIZE, color=TEXT_SECONDARY),
                    Text(qs, font_size=SMALL_SIZE, color=COMPLEXITY_GOOD if qs_good else COMPLEXITY_BAD),
                    Text(ms, font_size=SMALL_SIZE, color=COMPLEXITY_GOOD if ms_good else COMPLEXITY_BAD)
                )
            row.arrange(RIGHT, buff=1.2)
            table.add(row)
        
        table.arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        table.move_to(UP * 1.0)
        
        self.play(
            LaggedStart(*[FadeIn(row, shift=UP * 0.15) for row in table], lag_ratio=0.1),
            run_time=SLOW
        )
        self.wait(PAUSE)
        
        # Takeaways - positioned below table
        qs_take = Text("Quick Sort: Faster in practice", font_size=LABEL_SIZE, color=PIVOT)
        ms_take = Text("Merge Sort: Predictable & stable", font_size=LABEL_SIZE, color=TEMPORARY_STORAGE)
        
        qs_take.move_to(DOWN * 1.2)
        ms_take.next_to(qs_take, DOWN, buff=0.35)
        
        self.play(Write(qs_take), run_time=NORMAL)
        self.play(Write(ms_take), run_time=NORMAL)
        self.wait(PAUSE)
        
        # Final message at safe bottom
        final = Text("Choose based on your requirements!", font_size=BODY_SIZE, color=CORRECTLY_PLACED)
        final.move_to(DOWN * 2.8)
        
        self.play(Write(final), run_time=NORMAL)
        self.wait(PAUSE)
