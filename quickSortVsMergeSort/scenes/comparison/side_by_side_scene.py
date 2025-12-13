"""
Side-by-Side Comparison Scene.
R2 compliant: One concept - direct visual comparison.
"""
from manim import (
    Scene, Text, VGroup, Rectangle, Line, DashedLine,
    FadeIn, FadeOut, Write, Create, Transform, MoveToTarget,
    UP, DOWN, LEFT, RIGHT, ORIGIN,
    LaggedStart, AnimationGroup, Succession,
    PI
)
import sys
sys.path.insert(0, '/home/hg/Desktop/algorthims/quickSortVsMergeSort')

from config.colors import (
    BACKGROUND_COLOR, TEXT_PRIMARY, TEXT_SECONDARY,
    UNPROCESSED, PIVOT, CORRECTLY_PLACED, TEMPORARY_STORAGE,
    ACTIVE_COMPARISON, SUBARRAY_LEFT, SUBARRAY_RIGHT
)
from config.fonts import HEADING_SIZE, BODY_SIZE, LABEL_SIZE, SMALL_SIZE
from config.animation_constants import (
    DURATION_FAST, DURATION_NORMAL, DURATION_SLOW,
    PAUSE_SHORT, PAUSE_NORMAL, BAR_WIDTH, BAR_HEIGHT_SCALE
)


class SideBySideScene(Scene):
    """
    Scene 9: Side-by-Side Comparison.
    Concept: Direct visual comparison of both algorithms.
    """
    
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        
        # Title
        title = Text(
            "Side-by-Side Comparison",
            font_size=HEADING_SIZE,
            color=TEXT_PRIMARY
        )
        title.to_edge(UP, buff=0.4)
        self.play(Write(title), run_time=DURATION_NORMAL)
        
        # Create divider
        divider = DashedLine(
            UP * 2.5, DOWN * 3,
            color=TEXT_SECONDARY,
            stroke_width=1,
            dash_length=0.1
        )
        self.play(Create(divider), run_time=DURATION_FAST)
        
        # Labels
        qs_label = Text("Quick Sort", font_size=BODY_SIZE, color=PIVOT)
        ms_label = Text("Merge Sort", font_size=BODY_SIZE, color=TEMPORARY_STORAGE)
        
        qs_label.move_to(LEFT * 3.5 + UP * 2)
        ms_label.move_to(RIGHT * 3.5 + UP * 2)
        
        self.play(Write(qs_label), Write(ms_label), run_time=DURATION_FAST)
        
        # Create arrays for both sides
        values = [7, 2, 9, 4, 3]  # Shorter for clarity
        
        qs_array = self._create_array(values, UNPROCESSED)
        ms_array = self._create_array(values, UNPROCESSED)
        
        qs_array.move_to(LEFT * 3.5 + UP * 0.8)
        ms_array.move_to(RIGHT * 3.5 + UP * 0.8)
        
        self.play(
            FadeIn(qs_array),
            FadeIn(ms_array),
            run_time=DURATION_NORMAL
        )
        
        # Animate both sorting processes (simplified)
        self._animate_comparison(qs_array, ms_array, values)
        
        self.wait(PAUSE_NORMAL)
    
    def _create_array(self, values, color):
        """Create array visualization."""
        bars = VGroup()
        for val in values:
            bar = Rectangle(
                width=BAR_WIDTH * 0.7,
                height=val * BAR_HEIGHT_SCALE * 0.6,
                fill_color=color,
                fill_opacity=0.9,
                stroke_color=color,
                stroke_width=2
            )
            label = Text(str(val), font_size=SMALL_SIZE, color=TEXT_PRIMARY)
            label.next_to(bar, UP, buff=0.08)
            bars.add(VGroup(bar, label))
        
        bars.arrange(RIGHT, buff=0.1)
        return bars
    
    def _animate_comparison(self, qs_array, ms_array, values):
        """Animate simplified comparison of both algorithms."""
        # Quick Sort: Show pivot selection
        qs_step1 = Text("1. Select pivot", font_size=SMALL_SIZE, color=TEXT_SECONDARY)
        qs_step1.next_to(qs_array, DOWN, buff=0.4)
        
        ms_step1 = Text("1. Split in half", font_size=SMALL_SIZE, color=TEXT_SECONDARY)
        ms_step1.next_to(ms_array, DOWN, buff=0.4)
        
        self.play(Write(qs_step1), Write(ms_step1), run_time=DURATION_FAST)
        
        # Quick Sort: Highlight pivot
        pivot_idx = len(values) - 1
        self.play(
            qs_array[pivot_idx][0].animate.set_fill(PIVOT).set_stroke(PIVOT),
            run_time=DURATION_FAST
        )
        
        # Merge Sort: Color halves
        mid = len(values) // 2
        self.play(
            *[ms_array[i][0].animate.set_fill(SUBARRAY_LEFT).set_stroke(SUBARRAY_LEFT) 
              for i in range(mid)],
            *[ms_array[i][0].animate.set_fill(SUBARRAY_RIGHT).set_stroke(SUBARRAY_RIGHT) 
              for i in range(mid, len(values))],
            run_time=DURATION_FAST
        )
        
        self.wait(PAUSE_SHORT)
        
        # Step 2
        qs_step2 = Text("2. Partition", font_size=SMALL_SIZE, color=TEXT_SECONDARY)
        qs_step2.next_to(qs_step1, DOWN, buff=0.2)
        
        ms_step2 = Text("2. Recurse", font_size=SMALL_SIZE, color=TEXT_SECONDARY)
        ms_step2.next_to(ms_step1, DOWN, buff=0.2)
        
        self.play(
            FadeOut(qs_step1), FadeOut(ms_step1),
            Write(qs_step2), Write(ms_step2),
            run_time=DURATION_FAST
        )
        
        # Quick Sort: Show partition movement
        left_qs = VGroup(*[qs_array[i] for i in range(mid)])
        right_qs = VGroup(*[qs_array[i] for i in range(mid + 1, len(values))])
        
        self.play(
            left_qs.animate.shift(LEFT * 0.3),
            right_qs.animate.shift(RIGHT * 0.3),
            run_time=DURATION_NORMAL
        )
        
        # Merge Sort: Show split
        left_ms = VGroup(*[ms_array[i] for i in range(mid)])
        right_ms = VGroup(*[ms_array[i] for i in range(mid, len(values))])
        
        self.play(
            left_ms.animate.shift(LEFT * 0.3 + DOWN * 0.3),
            right_ms.animate.shift(RIGHT * 0.3 + DOWN * 0.3),
            run_time=DURATION_NORMAL
        )
        
        self.wait(PAUSE_SHORT)
        
        # Step 3: Final sorted
        qs_step3 = Text("3. Sorted!", font_size=SMALL_SIZE, color=CORRECTLY_PLACED)
        qs_step3.next_to(qs_step2, DOWN, buff=0.2)
        
        ms_step3 = Text("3. Merge & Sort!", font_size=SMALL_SIZE, color=CORRECTLY_PLACED)
        ms_step3.next_to(ms_step2, DOWN, buff=0.2)
        
        self.play(
            FadeOut(qs_step2), FadeOut(ms_step2),
            Write(qs_step3), Write(ms_step3),
            run_time=DURATION_FAST
        )
        
        # Show sorted result
        sorted_values = sorted(values)
        
        qs_sorted = self._create_array(sorted_values, CORRECTLY_PLACED)
        ms_sorted = self._create_array(sorted_values, CORRECTLY_PLACED)
        
        qs_sorted.move_to(LEFT * 3.5 + DOWN * 1.8)
        ms_sorted.move_to(RIGHT * 3.5 + DOWN * 1.8)
        
        self.play(
            FadeIn(qs_sorted),
            FadeIn(ms_sorted),
            run_time=DURATION_NORMAL
        )
        
        # Key differences
        self._show_key_differences()
    
    def _show_key_differences(self):
        """Show key differences at bottom."""
        differences = VGroup()
        
        qs_diff = Text("In-place, O(log n) space", font_size=SMALL_SIZE, color=PIVOT)
        ms_diff = Text("Extra O(n) space needed", font_size=SMALL_SIZE, color=TEMPORARY_STORAGE)
        
        qs_diff.move_to(LEFT * 3.5 + DOWN * 2.8)
        ms_diff.move_to(RIGHT * 3.5 + DOWN * 2.8)
        
        self.play(
            Write(qs_diff),
            Write(ms_diff),
            run_time=DURATION_NORMAL
        )
