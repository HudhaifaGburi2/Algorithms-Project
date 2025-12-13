#!/usr/bin/env python3
"""
Quick Sort vs Merge Sort - Animation
====================================
Clean layout, no overlapping, proper sequencing.

Usage:
    manim -pql main.py FullAnimation   # Preview
    manim -pqh main.py FullAnimation   # High quality
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

# Animation timing
FAST = 0.5
NORMAL = 0.8
SLOW = 1.2
PAUSE = 0.6

# Layout constants - prevent overlap
TITLE_Y = 3.2          # Title position (top)
CONTENT_TOP_Y = 2.0    # Content starts below title
CONTENT_MID_Y = 0.0    # Middle content area
CONTENT_BOT_Y = -2.0   # Bottom content area
SAFE_BOTTOM = -3.3     # Safe bottom margin

# Array for demonstration
DEMO_ARRAY = [8, 3, 7, 4, 2]


class FullAnimation(Scene):
    """Complete animation with clean layout - no overlapping."""
    
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        
        # Scene 1: Title
        self._title_scene()
        self._clear_scene()
        
        # Scene 2: Quick Sort Explanation
        self._quick_sort_explained()
        self._clear_scene()
        
        # Scene 3: Quick Sort Complexity
        self._quick_sort_complexity()
        self._clear_scene()
        
        # Scene 4: Merge Sort Explanation
        self._merge_sort_explained()
        self._clear_scene()
        
        # Scene 5: Merge Sort Complexity
        self._merge_sort_complexity()
        self._clear_scene()
        
        # Scene 6: Side-by-Side Comparison
        self._side_by_side_comparison()
        self._clear_scene()
        
        # Scene 7: Final Summary
        self._final_summary()
    
    def _clear_scene(self):
        """Clear with fade transition."""
        if self.mobjects:
            self.play(*[FadeOut(m) for m in self.mobjects], run_time=FAST)
        self.wait(0.2)
    
    # ==================== HELPER METHODS ====================
    
    def _create_title(self, text):
        """Create and show title at safe top position."""
        title = Text(text, font_size=HEADING_SIZE, color=TEXT_PRIMARY)
        title.move_to(UP * TITLE_Y)
        return title
    
    def _create_bar(self, value, color=UNPROCESSED, scale=1.0):
        """Create a single bar with value label inside."""
        bar = VGroup()
        
        rect = RoundedRectangle(
            width=0.8 * scale,
            height=value * 0.4 * scale,
            corner_radius=0.06 * scale,
            fill_color=color,
            fill_opacity=0.9,
            stroke_color=color,
            stroke_width=2
        )
        
        label = Text(str(value), font_size=int(20 * scale), color=TEXT_PRIMARY)
        label.move_to(rect.get_center())
        
        bar.add(rect, label)
        bar.value = value
        return bar
    
    def _create_array(self, values, color=UNPROCESSED, scale=1.0, spacing=0.2):
        """Create array of bars with proper spacing."""
        bars = VGroup()
        for val in values:
            bar = self._create_bar(val, color, scale)
            bars.add(bar)
        bars.arrange(RIGHT, buff=spacing * scale)
        return bars
    
    def _color_bar(self, bar, color):
        """Return animation for color change of a bar."""
        return bar[0].animate.set_fill(color).set_stroke(color)
    
    # ==================== SCENE 1: TITLE ====================
    
    def _title_scene(self):
        """Title and introduction."""
        # Title centered
        title = Text("Quick Sort vs Merge Sort", font_size=TITLE_SIZE, color=TEXT_PRIMARY)
        title.move_to(UP * 1.5)
        
        subtitle = Text("Divide and Conquer Algorithms", font_size=SUBTITLE_SIZE, color=TEXT_SECONDARY)
        subtitle.next_to(title, DOWN, buff=0.4)
        
        self.play(Write(title), run_time=SLOW)
        self.wait(PAUSE)
        self.play(FadeIn(subtitle, shift=UP * 0.2), run_time=NORMAL)
        self.wait(PAUSE)
        
        # Show array below subtitle
        array = self._create_array(DEMO_ARRAY, UNPROCESSED, scale=0.9)
        array.move_to(DOWN * 0.8)
        
        array_label = Text("Unsorted Array", font_size=LABEL_SIZE, color=TEXT_SECONDARY)
        array_label.next_to(array, DOWN, buff=0.4)
        
        self.play(
            LaggedStart(*[FadeIn(bar, shift=UP * 0.3) for bar in array], lag_ratio=0.12),
            run_time=NORMAL
        )
        self.play(Write(array_label), run_time=FAST)
        self.wait(PAUSE)
        
        # Transform to sorted
        sorted_array = self._create_array(sorted(DEMO_ARRAY), CORRECTLY_PLACED, scale=0.9)
        sorted_array.move_to(array.get_center())
        
        sorted_label = Text("Sorted Array", font_size=LABEL_SIZE, color=CORRECTLY_PLACED)
        sorted_label.next_to(sorted_array, DOWN, buff=0.4)
        
        self.play(
            ReplacementTransform(array, sorted_array),
            ReplacementTransform(array_label, sorted_label),
            run_time=SLOW
        )
        self.wait(PAUSE)
    
    # ==================== SCENE 2: QUICK SORT D&C ====================
    
    def _quick_sort_dc_concept(self):
        """Quick Sort Divide & Conquer concept visualization."""
        title = Text("Quick Sort: Divide & Conquer", font_size=HEADING_SIZE, color=TEXT_PRIMARY)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=NORMAL)
        self.wait(PAUSE)
        
        # Step 1: Show array
        values = [8, 3, 7, 4, 2]
        array = self._create_array(values, UNPROCESSED)
        array.move_to(UP * 1.5)
        
        step_label = Text("Step 1: Choose a Pivot", font_size=BODY_SIZE, color=TEXT_SECONDARY)
        step_label.next_to(array, UP, buff=0.4)
        
        self.play(FadeIn(array), Write(step_label), run_time=NORMAL)
        self.wait(PAUSE)
        
        # Highlight pivot (last element = 2)
        pivot_idx = 4
        pivot_val = values[pivot_idx]
        
        pivot_marker = Text(f"Pivot = {pivot_val}", font_size=LABEL_SIZE, color=PIVOT)
        pivot_marker.next_to(array[pivot_idx], DOWN, buff=0.3)
        
        self.play(
            self._color_bar(array[pivot_idx], PIVOT),
            FadeIn(pivot_marker),
            run_time=NORMAL
        )
        self.wait(PAUSE)
        
        # Step 2: Partition concept
        new_step = Text("Step 2: Partition around Pivot", font_size=BODY_SIZE, color=TEXT_SECONDARY)
        new_step.move_to(step_label.get_center())
        
        self.play(ReplacementTransform(step_label, new_step), run_time=FAST)
        self.wait(PAUSE)
        
        # Show comparison concept
        less_label = Text("< 2", font_size=LABEL_SIZE, color=SUBARRAY_LEFT)
        greater_label = Text("> 2", font_size=LABEL_SIZE, color=SUBARRAY_RIGHT)
        
        less_label.move_to(LEFT * 3 + DOWN * 0.5)
        greater_label.move_to(RIGHT * 3 + DOWN * 0.5)
        
        self.play(Write(less_label), Write(greater_label), run_time=NORMAL)
        self.wait(PAUSE)
        
        # Color elements based on comparison
        # 8 > 2 (red), 3 > 2 (red), 7 > 2 (red), 4 > 2 (red), 2 = pivot (yellow)
        for i in range(4):
            self.play(
                self._color_bar(array[i], ACTIVE_COMPARISON, FAST),
                run_time=FAST
            )
            self.wait(0.3)
            self.play(
                self._color_bar(array[i], SUBARRAY_RIGHT, FAST),
                run_time=FAST
            )
        
        self.wait(PAUSE)
        
        # Step 3: Result of partition
        new_step2 = Text("Step 3: Pivot in Final Position", font_size=BODY_SIZE, color=TEXT_SECONDARY)
        new_step2.move_to(new_step.get_center())
        
        self.play(
            ReplacementTransform(new_step, new_step2),
            FadeOut(less_label),
            FadeOut(greater_label),
            run_time=FAST
        )
        
        # Move pivot to correct position (first position since all others are greater)
        # Create new arrangement: [2] | [8, 3, 7, 4]
        pivot_bar = array[pivot_idx].copy()
        
        result_group = VGroup()
        
        # Pivot in position
        pivot_final = self._create_bar(2, CORRECTLY_PLACED)
        pivot_final.move_to(LEFT * 4 + DOWN * 1.5)
        
        # Greater elements
        greater_bars = self._create_array([8, 3, 7, 4], SUBARRAY_RIGHT, scale=0.9)
        greater_bars.move_to(RIGHT * 1 + DOWN * 1.5)
        
        # Labels
        sorted_marker = Text("Sorted!", font_size=SMALL_SIZE, color=CORRECTLY_PLACED)
        sorted_marker.next_to(pivot_final, DOWN, buff=0.2)
        
        recurse_marker = Text("Recurse →", font_size=SMALL_SIZE, color=SUBARRAY_RIGHT)
        recurse_marker.next_to(greater_bars, DOWN, buff=0.2)
        
        self.play(
            FadeOut(array),
            FadeOut(pivot_marker),
            FadeIn(pivot_final),
            FadeIn(greater_bars),
            FadeIn(sorted_marker),
            FadeIn(recurse_marker),
            run_time=SLOW
        )
        self.wait(PAUSE)
        
        # Key insight
        insight = Text(
            "Pivot is now in its final sorted position!",
            font_size=LABEL_SIZE,
            color=CORRECTLY_PLACED
        )
        insight.to_edge(DOWN, buff=0.8)
        
        self.play(Write(insight), run_time=NORMAL)
        self.wait(PAUSE * 2)
    
    # ==================== SCENE 3: QUICK SORT FULL ====================
    
    def _quick_sort_full_example(self):
        """Full Quick Sort step-by-step on 5 elements."""
        title = Text("Quick Sort: Complete Example", font_size=HEADING_SIZE, color=TEXT_PRIMARY)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title), run_time=NORMAL)
        
        # Initial array: [8, 3, 7, 4, 2]
        values = [8, 3, 7, 4, 2]
        array = self._create_array(values, UNPROCESSED, scale=0.85, spacing=0.3)
        array.move_to(UP * 1.8)
        
        self.play(FadeIn(array), run_time=NORMAL)
        self.wait(PAUSE)
        
        # Track sorted positions
        sorted_positions = set()
        
        # === LEVEL 0: Partition with pivot=2 ===
        level_label = Text("Level 0: Pivot = 2", font_size=SMALL_SIZE, color=PIVOT)
        level_label.next_to(array, LEFT, buff=0.5)
        
        self.play(
            Write(level_label),
            self._color_bar(array[4], PIVOT),
            run_time=NORMAL
        )
        self.wait(PAUSE)
        
        # Compare each element
        for i in range(4):
            self.play(self._color_bar(array[i], ACTIVE_COMPARISON), run_time=FAST)
            self.wait(0.3)
            # All are > 2
            self.play(self._color_bar(array[i], UNPROCESSED), run_time=FAST)
        
        # Pivot 2 goes to position 0 (smallest)
        # Result: [2, 3, 7, 4, 8] - but we need to show the swap
        self.play(self._color_bar(array[4], CORRECTLY_PLACED), run_time=NORMAL)
        sorted_positions.add(0)
        
        # Show level 1 arrays below
        level1_label = Text("Level 1", font_size=SMALL_SIZE, color=TEXT_SECONDARY)
        level1_label.move_to(LEFT * 5.5 + UP * 0.2)
        
        # After first partition: 2 is sorted, need to sort [8, 3, 7, 4]
        remaining = self._create_array([8, 3, 7, 4], UNPROCESSED, scale=0.75, spacing=0.25)
        remaining.move_to(UP * 0.2)
        
        sorted_2 = self._create_bar(2, CORRECTLY_PLACED, scale=0.75)
        sorted_2.move_to(LEFT * 4.5 + UP * 0.2)
        
        check_mark = Text("✓", font_size=SMALL_SIZE, color=CORRECTLY_PLACED)
        check_mark.next_to(sorted_2, DOWN, buff=0.15)
        
        self.play(
            FadeOut(level_label),
            array.animate.set_opacity(0.3),
            FadeIn(remaining),
            FadeIn(sorted_2),
            FadeIn(check_mark),
            Write(level1_label),
            run_time=NORMAL
        )
        self.wait(PAUSE)
        
        # === LEVEL 1: Partition [8, 3, 7, 4] with pivot=4 ===
        pivot_label = Text("Pivot = 4", font_size=SMALL_SIZE, color=PIVOT)
        pivot_label.next_to(remaining[3], UP, buff=0.2)
        
        self.play(
            self._color_bar(remaining[3], PIVOT),
            FadeIn(pivot_label),
            run_time=NORMAL
        )
        self.wait(PAUSE)
        
        # Compare: 8>4, 3<4, 7>4
        comparisons = [(0, False), (1, True), (2, False)]  # (index, is_less)
        for idx, is_less in comparisons:
            self.play(self._color_bar(remaining[idx], ACTIVE_COMPARISON), run_time=FAST)
            self.wait(0.3)
            color = SUBARRAY_LEFT if is_less else SUBARRAY_RIGHT
            self.play(self._color_bar(remaining[idx], color), run_time=FAST)
        
        self.wait(PAUSE)
        
        # Show result of partition: [3] | 4 | [8, 7]
        level2_label = Text("Level 2", font_size=SMALL_SIZE, color=TEXT_SECONDARY)
        level2_label.move_to(LEFT * 5.5 + DOWN * 1.5)
        
        left_sub = self._create_bar(3, SUBARRAY_LEFT, scale=0.65)
        left_sub.move_to(LEFT * 2.5 + DOWN * 1.5)
        
        pivot_4 = self._create_bar(4, CORRECTLY_PLACED, scale=0.65)
        pivot_4.move_to(DOWN * 1.5)
        
        right_sub = self._create_array([8, 7], SUBARRAY_RIGHT, scale=0.65, spacing=0.2)
        right_sub.move_to(RIGHT * 2.5 + DOWN * 1.5)
        
        check_4 = Text("✓", font_size=SMALL_SIZE, color=CORRECTLY_PLACED)
        check_4.next_to(pivot_4, DOWN, buff=0.15)
        
        self.play(
            FadeOut(pivot_label),
            remaining.animate.set_opacity(0.3),
            FadeIn(left_sub),
            FadeIn(pivot_4),
            FadeIn(right_sub),
            FadeIn(check_4),
            Write(level2_label),
            run_time=NORMAL
        )
        self.wait(PAUSE)
        
        # === Continue recursion - mark single elements as sorted ===
        # 3 is single element -> sorted
        self.play(self._color_bar(left_sub, CORRECTLY_PLACED), run_time=NORMAL)
        check_3 = Text("✓", font_size=SMALL_SIZE, color=CORRECTLY_PLACED)
        check_3.next_to(left_sub, DOWN, buff=0.15)
        self.play(FadeIn(check_3), run_time=FAST)
        
        # Sort [8, 7] with pivot=7
        pivot_7_label = Text("Pivot = 7", font_size=SMALL_SIZE, color=PIVOT)
        pivot_7_label.next_to(right_sub[1], UP, buff=0.2)
        
        self.play(
            self._color_bar(right_sub[1], PIVOT),
            FadeIn(pivot_7_label),
            run_time=NORMAL
        )
        self.wait(PAUSE)
        
        # 8 > 7
        self.play(self._color_bar(right_sub[0], ACTIVE_COMPARISON), run_time=FAST)
        self.wait(0.3)
        self.play(self._color_bar(right_sub[0], SUBARRAY_RIGHT), run_time=FAST)
        
        # Result: 7 sorted, 8 sorted
        self.play(
            FadeOut(pivot_7_label),
            self._color_bar(right_sub[1], CORRECTLY_PLACED),
            self._color_bar(right_sub[0], CORRECTLY_PLACED),
            run_time=NORMAL
        )
        
        check_7 = Text("✓", font_size=SMALL_SIZE, color=CORRECTLY_PLACED)
        check_7.next_to(right_sub[1], DOWN, buff=0.15)
        check_8 = Text("✓", font_size=SMALL_SIZE, color=CORRECTLY_PLACED)
        check_8.next_to(right_sub[0], DOWN, buff=0.15)
        
        self.play(FadeIn(check_7), FadeIn(check_8), run_time=FAST)
        self.wait(PAUSE)
        
        # === Show final sorted array ===
        final_label = Text("Final Sorted Array", font_size=BODY_SIZE, color=CORRECTLY_PLACED)
        final_label.move_to(DOWN * 3)
        
        final_array = self._create_array([2, 3, 4, 7, 8], CORRECTLY_PLACED, scale=0.8)
        final_array.next_to(final_label, DOWN, buff=0.3)
        
        self.play(
            Write(final_label),
            FadeIn(final_array),
            run_time=NORMAL
        )
        self.wait(PAUSE * 2)
    
    # ==================== SCENE 4: QUICK SORT COMPLEXITY ====================
    
    def _quick_sort_complexity(self):
        """Quick Sort complexity summary."""
        title = Text("Quick Sort Complexity", font_size=HEADING_SIZE, color=TEXT_PRIMARY)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=NORMAL)
        self.wait(PAUSE)
        
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
        
        summary.arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        summary.move_to(ORIGIN)
        
        self.play(
            LaggedStart(*[FadeIn(row, shift=LEFT * 0.3) for row in summary], lag_ratio=0.2),
            run_time=SLOW
        )
        self.wait(PAUSE * 2)
    
    # ==================== SCENE 5: MERGE SORT D&C ====================
    
    def _merge_sort_dc_concept(self):
        """Merge Sort Divide & Conquer concept."""
        title = Text("Merge Sort: Divide & Conquer", font_size=HEADING_SIZE, color=TEXT_PRIMARY)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=NORMAL)
        self.wait(PAUSE)
        
        # Step 1: Show array
        values = [8, 3, 7, 4, 2]
        array = self._create_array(values, UNPROCESSED)
        array.move_to(UP * 1.5)
        
        step_label = Text("Step 1: Divide in Half", font_size=BODY_SIZE, color=TEXT_SECONDARY)
        step_label.next_to(array, UP, buff=0.4)
        
        self.play(FadeIn(array), Write(step_label), run_time=NORMAL)
        self.wait(PAUSE)
        
        # Color left and right halves
        mid = 2
        for i in range(mid):
            self.play(self._color_bar(array[i], SUBARRAY_LEFT), run_time=FAST)
        for i in range(mid, 5):
            self.play(self._color_bar(array[i], SUBARRAY_RIGHT), run_time=FAST)
        
        self.wait(PAUSE)
        
        # Split visually
        left_half = VGroup(*[array[i] for i in range(mid)])
        right_half = VGroup(*[array[i] for i in range(mid, 5)])
        
        self.play(
            left_half.animate.shift(LEFT * 1.5),
            right_half.animate.shift(RIGHT * 1.5),
            run_time=NORMAL
        )
        
        left_label = Text("[8, 3]", font_size=SMALL_SIZE, color=SUBARRAY_LEFT)
        right_label = Text("[7, 4, 2]", font_size=SMALL_SIZE, color=SUBARRAY_RIGHT)
        left_label.next_to(left_half, DOWN, buff=0.3)
        right_label.next_to(right_half, DOWN, buff=0.3)
        
        self.play(FadeIn(left_label), FadeIn(right_label), run_time=FAST)
        self.wait(PAUSE)
        
        # Step 2: Continue dividing
        new_step = Text("Step 2: Keep Dividing Until Single Elements", font_size=BODY_SIZE, color=TEXT_SECONDARY)
        new_step.move_to(step_label.get_center())
        
        self.play(ReplacementTransform(step_label, new_step), run_time=FAST)
        self.wait(PAUSE)
        
        # Show single elements at bottom
        singles = VGroup()
        single_vals = [8, 3, 7, 4, 2]
        positions = [LEFT * 4, LEFT * 2, ORIGIN, RIGHT * 2, RIGHT * 4]
        
        for val, pos in zip(single_vals, positions):
            single = self._create_bar(val, CORRECTLY_PLACED, scale=0.7)
            single.move_to(pos + DOWN * 1)
            singles.add(single)
        
        single_label = Text("Single elements are sorted!", font_size=SMALL_SIZE, color=CORRECTLY_PLACED)
        single_label.next_to(singles, DOWN, buff=0.4)
        
        self.play(
            FadeOut(left_half), FadeOut(right_half),
            FadeOut(left_label), FadeOut(right_label),
            LaggedStart(*[FadeIn(s, shift=DOWN * 0.3) for s in singles], lag_ratio=0.1),
            run_time=NORMAL
        )
        self.play(Write(single_label), run_time=FAST)
        self.wait(PAUSE)
        
        # Step 3: Merge
        new_step2 = Text("Step 3: Merge Back in Sorted Order", font_size=BODY_SIZE, color=TEXT_SECONDARY)
        new_step2.move_to(new_step.get_center())
        
        self.play(ReplacementTransform(new_step, new_step2), run_time=FAST)
        self.wait(PAUSE)
        
        # Show merged result
        merged = self._create_array([2, 3, 4, 7, 8], CORRECTLY_PLACED)
        merged.move_to(DOWN * 2.5)
        
        self.play(
            singles.animate.set_opacity(0.3),
            FadeOut(single_label),
            FadeIn(merged),
            run_time=SLOW
        )
        
        final_label = Text("Sorted!", font_size=BODY_SIZE, color=CORRECTLY_PLACED)
        final_label.next_to(merged, DOWN, buff=0.3)
        self.play(Write(final_label), run_time=FAST)
        self.wait(PAUSE * 2)
    
    # ==================== SCENE 6: MERGE SORT FULL ====================
    
    def _merge_sort_full_example(self):
        """Full Merge Sort step-by-step."""
        title = Text("Merge Sort: Complete Example", font_size=HEADING_SIZE, color=TEXT_PRIMARY)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title), run_time=NORMAL)
        
        # Show divide tree
        # Level 0: [8, 3, 7, 4, 2]
        level0 = self._create_array([8, 3, 7, 4, 2], UNPROCESSED, scale=0.7, spacing=0.15)
        level0.move_to(UP * 2.5)
        
        l0_label = Text("[8, 3, 7, 4, 2]", font_size=SMALL_SIZE, color=TEXT_SECONDARY)
        l0_label.next_to(level0, RIGHT, buff=0.3)
        
        self.play(FadeIn(level0), FadeIn(l0_label), run_time=NORMAL)
        self.wait(PAUSE)
        
        # Level 1: [8, 3] and [7, 4, 2]
        l1_left = self._create_array([8, 3], SUBARRAY_LEFT, scale=0.6, spacing=0.1)
        l1_right = self._create_array([7, 4, 2], SUBARRAY_RIGHT, scale=0.6, spacing=0.1)
        
        l1_left.move_to(LEFT * 3 + UP * 1)
        l1_right.move_to(RIGHT * 3 + UP * 1)
        
        lines1 = VGroup(
            Line(level0.get_bottom(), l1_left.get_top(), color=TEXT_SECONDARY, stroke_width=2),
            Line(level0.get_bottom(), l1_right.get_top(), color=TEXT_SECONDARY, stroke_width=2),
        )
        
        self.play(
            Create(lines1),
            FadeIn(l1_left),
            FadeIn(l1_right),
            run_time=NORMAL
        )
        self.wait(PAUSE)
        
        # Level 2: Single elements
        l2_elements = [
            self._create_bar(8, CORRECTLY_PLACED, scale=0.5),
            self._create_bar(3, CORRECTLY_PLACED, scale=0.5),
            self._create_bar(7, CORRECTLY_PLACED, scale=0.5),
            self._create_bar(4, CORRECTLY_PLACED, scale=0.5),
            self._create_bar(2, CORRECTLY_PLACED, scale=0.5),
        ]
        
        l2_positions = [LEFT * 4.5, LEFT * 2.5, RIGHT * 1.5, RIGHT * 3, RIGHT * 4.5]
        for elem, pos in zip(l2_elements, l2_positions):
            elem.move_to(pos + DOWN * 0.5)
        
        l2_group = VGroup(*l2_elements)
        
        lines2 = VGroup(
            Line(l1_left.get_bottom(), l2_elements[0].get_top(), color=TEXT_SECONDARY, stroke_width=1.5),
            Line(l1_left.get_bottom(), l2_elements[1].get_top(), color=TEXT_SECONDARY, stroke_width=1.5),
            Line(l1_right.get_bottom(), l2_elements[2].get_top(), color=TEXT_SECONDARY, stroke_width=1.5),
            Line(l1_right.get_bottom(), l2_elements[3].get_top(), color=TEXT_SECONDARY, stroke_width=1.5),
            Line(l1_right.get_bottom(), l2_elements[4].get_top(), color=TEXT_SECONDARY, stroke_width=1.5),
        )
        
        self.play(Create(lines2), FadeIn(l2_group), run_time=NORMAL)
        self.wait(PAUSE)
        
        # Merge phase label
        merge_label = Text("MERGE PHASE", font_size=BODY_SIZE, color=TEMPORARY_STORAGE)
        merge_label.move_to(DOWN * 1.5)
        self.play(Write(merge_label), run_time=FAST)
        self.wait(PAUSE)
        
        # Show merge steps
        # Merge [8] and [3] -> [3, 8]
        merge1 = self._create_array([3, 8], TEMPORARY_STORAGE, scale=0.55, spacing=0.1)
        merge1.move_to(LEFT * 3.5 + DOWN * 2.5)
        
        merge1_label = Text("[3, 8]", font_size=SMALL_SIZE, color=TEMPORARY_STORAGE)
        merge1_label.next_to(merge1, DOWN, buff=0.15)
        
        self.play(FadeIn(merge1), FadeIn(merge1_label), run_time=NORMAL)
        self.wait(0.5)
        
        # Merge [7, 4, 2] -> first [4, 7] then [2, 4, 7]
        merge2 = self._create_array([2, 4, 7], TEMPORARY_STORAGE, scale=0.55, spacing=0.1)
        merge2.move_to(RIGHT * 3 + DOWN * 2.5)
        
        merge2_label = Text("[2, 4, 7]", font_size=SMALL_SIZE, color=TEMPORARY_STORAGE)
        merge2_label.next_to(merge2, DOWN, buff=0.15)
        
        self.play(FadeIn(merge2), FadeIn(merge2_label), run_time=NORMAL)
        self.wait(PAUSE)
        
        # Final merge
        final_array = self._create_array([2, 3, 4, 7, 8], CORRECTLY_PLACED, scale=0.7)
        final_array.to_edge(DOWN, buff=0.5)
        
        final_label = Text("Final: [2, 3, 4, 7, 8]", font_size=BODY_SIZE, color=CORRECTLY_PLACED)
        final_label.next_to(final_array, UP, buff=0.3)
        
        self.play(
            FadeOut(merge_label),
            FadeIn(final_array),
            Write(final_label),
            run_time=SLOW
        )
        self.wait(PAUSE * 2)
    
    # ==================== SCENE 7: MERGE SORT COMPLEXITY ====================
    
    def _merge_sort_complexity(self):
        """Merge Sort complexity summary."""
        title = Text("Merge Sort Complexity", font_size=HEADING_SIZE, color=TEXT_PRIMARY)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=NORMAL)
        self.wait(PAUSE)
        
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
        
        summary.arrange(DOWN, buff=0.35, aligned_edge=LEFT)
        summary.move_to(ORIGIN)
        
        self.play(
            LaggedStart(*[FadeIn(row, shift=LEFT * 0.3) for row in summary], lag_ratio=0.15),
            run_time=SLOW
        )
        self.wait(PAUSE * 2)
    
    # ==================== SCENE 8: SIDE-BY-SIDE RACE ====================
    
    def _side_by_side_race(self):
        """Side-by-side comparison showing both algorithms sorting."""
        title = Text("Side-by-Side Comparison", font_size=HEADING_SIZE, color=TEXT_PRIMARY)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title), run_time=NORMAL)
        
        # Divider
        divider = DashedLine(UP * 2.5, DOWN * 3.5, color=TEXT_SECONDARY, stroke_width=2, dash_length=0.15)
        self.play(Create(divider), run_time=FAST)
        
        # Labels
        qs_title = Text("Quick Sort", font_size=BODY_SIZE, color=PIVOT)
        ms_title = Text("Merge Sort", font_size=BODY_SIZE, color=TEMPORARY_STORAGE)
        qs_title.move_to(LEFT * 3.5 + UP * 2)
        ms_title.move_to(RIGHT * 3.5 + UP * 2)
        
        self.play(Write(qs_title), Write(ms_title), run_time=FAST)
        
        # Initial arrays
        values = [8, 3, 7, 4, 2]
        
        qs_array = self._create_array(values, UNPROCESSED, scale=0.6, spacing=0.15)
        ms_array = self._create_array(values, UNPROCESSED, scale=0.6, spacing=0.15)
        
        qs_array.move_to(LEFT * 3.5 + UP * 1)
        ms_array.move_to(RIGHT * 3.5 + UP * 1)
        
        self.play(FadeIn(qs_array), FadeIn(ms_array), run_time=NORMAL)
        self.wait(PAUSE)
        
        # Quick Sort side - show pivot selection
        qs_step1 = Text("1. Select Pivot", font_size=SMALL_SIZE, color=PIVOT)
        qs_step1.next_to(qs_array, DOWN, buff=0.3)
        
        ms_step1 = Text("1. Split in Half", font_size=SMALL_SIZE, color=TEMPORARY_STORAGE)
        ms_step1.next_to(ms_array, DOWN, buff=0.3)
        
        self.play(Write(qs_step1), Write(ms_step1), run_time=FAST)
        
        # Quick Sort: highlight pivot
        self.play(self._color_bar(qs_array[4], PIVOT), run_time=NORMAL)
        
        # Merge Sort: color halves
        self.play(
            *[self._color_bar(ms_array[i], SUBARRAY_LEFT) for i in range(2)],
            *[self._color_bar(ms_array[i], SUBARRAY_RIGHT) for i in range(2, 5)],
            run_time=NORMAL
        )
        self.wait(PAUSE)
        
        # Step 2
        qs_step2 = Text("2. Partition", font_size=SMALL_SIZE, color=PIVOT)
        ms_step2 = Text("2. Divide Recursively", font_size=SMALL_SIZE, color=TEMPORARY_STORAGE)
        
        self.play(
            ReplacementTransform(qs_step1, qs_step2),
            ReplacementTransform(ms_step1, ms_step2),
            run_time=FAST
        )
        qs_step2.next_to(qs_array, DOWN, buff=0.3)
        ms_step2.next_to(ms_array, DOWN, buff=0.3)
        
        # Quick Sort: show partition result
        qs_result1 = self._create_array([2], CORRECTLY_PLACED, scale=0.5)
        qs_result2 = self._create_array([8, 3, 7, 4], UNPROCESSED, scale=0.5, spacing=0.1)
        qs_result1.move_to(LEFT * 5 + DOWN * 0.5)
        qs_result2.move_to(LEFT * 2.5 + DOWN * 0.5)
        
        # Merge Sort: show split
        ms_left = self._create_array([8, 3], SUBARRAY_LEFT, scale=0.5, spacing=0.1)
        ms_right = self._create_array([7, 4, 2], SUBARRAY_RIGHT, scale=0.5, spacing=0.1)
        ms_left.move_to(RIGHT * 2.5 + DOWN * 0.5)
        ms_right.move_to(RIGHT * 4.5 + DOWN * 0.5)
        
        self.play(
            qs_array.animate.set_opacity(0.3),
            ms_array.animate.set_opacity(0.3),
            FadeIn(qs_result1), FadeIn(qs_result2),
            FadeIn(ms_left), FadeIn(ms_right),
            run_time=NORMAL
        )
        self.wait(PAUSE)
        
        # Step 3: Final sorted
        qs_step3 = Text("3. Sorted!", font_size=SMALL_SIZE, color=CORRECTLY_PLACED)
        ms_step3 = Text("3. Merge & Sort!", font_size=SMALL_SIZE, color=CORRECTLY_PLACED)
        
        self.play(
            ReplacementTransform(qs_step2, qs_step3),
            ReplacementTransform(ms_step2, ms_step3),
            run_time=FAST
        )
        qs_step3.next_to(qs_array, DOWN, buff=0.3)
        ms_step3.next_to(ms_array, DOWN, buff=0.3)
        
        # Final sorted arrays
        qs_final = self._create_array([2, 3, 4, 7, 8], CORRECTLY_PLACED, scale=0.6, spacing=0.15)
        ms_final = self._create_array([2, 3, 4, 7, 8], CORRECTLY_PLACED, scale=0.6, spacing=0.15)
        
        qs_final.move_to(LEFT * 3.5 + DOWN * 2)
        ms_final.move_to(RIGHT * 3.5 + DOWN * 2)
        
        self.play(FadeIn(qs_final), FadeIn(ms_final), run_time=NORMAL)
        self.wait(PAUSE)
        
        # Key differences
        qs_note = Text("In-place\nO(log n) space", font_size=SMALL_SIZE, color=PIVOT)
        ms_note = Text("Extra arrays\nO(n) space", font_size=SMALL_SIZE, color=TEMPORARY_STORAGE)
        
        qs_note.move_to(LEFT * 3.5 + DOWN * 3.2)
        ms_note.move_to(RIGHT * 3.5 + DOWN * 3.2)
        
        self.play(Write(qs_note), Write(ms_note), run_time=NORMAL)
        self.wait(PAUSE * 2)
    
    # ==================== SCENE 9: FINAL SUMMARY ====================
    
    def _final_summary(self):
        """Final summary and takeaways."""
        title = Text("Summary", font_size=HEADING_SIZE, color=TEXT_PRIMARY)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=NORMAL)
        self.wait(PAUSE)
        
        # Comparison table
        table_data = [
            ("", "Quick Sort", "Merge Sort"),
            ("Best Case", "O(n log n)", "O(n log n)"),
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
            row.arrange(RIGHT, buff=1.5)
            table.add(row)
        
        table.arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        table.move_to(UP * 0.5)
        
        self.play(
            LaggedStart(*[FadeIn(row, shift=UP * 0.2) for row in table], lag_ratio=0.12),
            run_time=SLOW
        )
        self.wait(PAUSE)
        
        # Takeaways
        qs_take = Text("Quick Sort: Faster in practice, less memory", font_size=LABEL_SIZE, color=PIVOT)
        ms_take = Text("Merge Sort: Predictable, stable, guaranteed O(n log n)", font_size=LABEL_SIZE, color=TEMPORARY_STORAGE)
        
        qs_take.move_to(DOWN * 2)
        ms_take.next_to(qs_take, DOWN, buff=0.4)
        
        self.play(Write(qs_take), run_time=NORMAL)
        self.play(Write(ms_take), run_time=NORMAL)
        self.wait(PAUSE * 2)
        
        # Final message
        final = Text("Choose based on your requirements!", font_size=BODY_SIZE, color=CORRECTLY_PLACED)
        final.to_edge(DOWN, buff=0.5)
        
        self.play(Write(final), run_time=NORMAL)
        self.wait(PAUSE * 2)
