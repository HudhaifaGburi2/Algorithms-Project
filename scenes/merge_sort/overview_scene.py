"""
Merge Sort Overview Scene.
R2 compliant: One concept - Merge Sort intuition.
R5 compliant: Recursion shown spatially.
"""
from manim import (
    Scene, Text, VGroup, Rectangle, Arrow, Line,
    FadeIn, FadeOut, Write, Create, Transform,
    UP, DOWN, LEFT, RIGHT, ORIGIN,
    LaggedStart, AnimationGroup
)
import sys
sys.path.insert(0, '/home/hg/Desktop/algorthims/quickSortVsMergeSort')

from config.colors import (
    BACKGROUND_COLOR, TEXT_PRIMARY, TEXT_SECONDARY,
    UNPROCESSED, TEMPORARY_STORAGE, CORRECTLY_PLACED,
    SUBARRAY_LEFT, SUBARRAY_RIGHT
)
from config.fonts import HEADING_SIZE, BODY_SIZE, LABEL_SIZE
from config.animation_constants import (
    DURATION_FAST, DURATION_NORMAL, DURATION_SLOW,
    PAUSE_SHORT, PAUSE_NORMAL, EASE_DEFAULT,
    BAR_WIDTH, BAR_HEIGHT_SCALE
)


class MergeSortOverviewScene(Scene):
    """
    Scene 6: Merge Sort Conceptual Overview.
    Concept: Always divide evenly, then merge.
    """
    
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        
        # Title
        title = Text(
            "Merge Sort",
            font_size=HEADING_SIZE,
            color=TEXT_PRIMARY
        )
        title.to_edge(UP, buff=0.5)
        
        self.play(Write(title), run_time=DURATION_NORMAL)
        
        # Create array visualization
        values = [7, 2, 9, 4, 3, 8, 5]
        array_group = self._create_array_bars(values)
        array_group.next_to(title, DOWN, buff=0.8)
        
        self.play(
            LaggedStart(
                *[FadeIn(bar, shift=UP * 0.3) for bar in array_group],
                lag_ratio=0.1
            ),
            run_time=DURATION_NORMAL
        )
        self.wait(PAUSE_NORMAL)
        
        # Show splitting concept
        self._show_split_concept(array_group)
        
        self.wait(PAUSE_NORMAL)
    
    def _create_array_bars(self, values):
        """Create array bar visualization."""
        bars = VGroup()
        for val in values:
            bar = Rectangle(
                width=BAR_WIDTH,
                height=val * BAR_HEIGHT_SCALE,
                fill_color=UNPROCESSED,
                fill_opacity=0.9,
                stroke_color=UNPROCESSED,
                stroke_width=2
            )
            label = Text(str(val), font_size=LABEL_SIZE, color=TEXT_PRIMARY)
            label.next_to(bar, UP, buff=0.1)
            bar_group = VGroup(bar, label)
            bars.add(bar_group)
        
        bars.arrange(RIGHT, buff=0.15)
        return bars
    
    def _show_split_concept(self, array_group):
        """Visualize the splitting concept."""
        # Split indicator
        mid = len(array_group) // 2
        
        # Color left and right halves
        left_half = VGroup(*[array_group[i] for i in range(mid)])
        right_half = VGroup(*[array_group[i] for i in range(mid, len(array_group))])
        
        # Color them
        self.play(
            *[bar[0].animate.set_fill(SUBARRAY_LEFT).set_stroke(SUBARRAY_LEFT) 
              for bar in left_half],
            *[bar[0].animate.set_fill(SUBARRAY_RIGHT).set_stroke(SUBARRAY_RIGHT) 
              for bar in right_half],
            run_time=DURATION_NORMAL
        )
        
        # Add labels
        left_label = Text("Left Half", font_size=LABEL_SIZE, color=SUBARRAY_LEFT)
        right_label = Text("Right Half", font_size=LABEL_SIZE, color=SUBARRAY_RIGHT)
        
        left_label.next_to(left_half, DOWN, buff=0.5)
        right_label.next_to(right_half, DOWN, buff=0.5)
        
        self.play(
            Write(left_label),
            Write(right_label),
            run_time=DURATION_FAST
        )
        
        # Split animation
        self.play(
            left_half.animate.shift(LEFT * 0.8),
            right_half.animate.shift(RIGHT * 0.8),
            left_label.animate.shift(LEFT * 0.8),
            right_label.animate.shift(RIGHT * 0.8),
            run_time=DURATION_NORMAL
        )
        self.wait(PAUSE_SHORT)
        
        # Show key insight text
        insight = Text(
            "Always splits in half",
            font_size=BODY_SIZE,
            color=TEXT_SECONDARY
        )
        insight.next_to(VGroup(left_label, right_label), DOWN, buff=0.8)
        
        self.play(Write(insight), run_time=DURATION_NORMAL)
        self.wait(PAUSE_SHORT)
        
        # Show further splitting
        self._show_recursive_split(left_half, right_half, left_label, right_label, insight)
    
    def _show_recursive_split(self, left_half, right_half, left_label, right_label, insight):
        """Show recursive splitting to single elements."""
        # Fade out labels
        self.play(
            FadeOut(left_label),
            FadeOut(right_label),
            FadeOut(insight),
            run_time=DURATION_FAST
        )
        
        # Continue splitting left half
        left_mid = len(left_half) // 2
        left_left = VGroup(*[left_half[i] for i in range(left_mid)])
        left_right = VGroup(*[left_half[i] for i in range(left_mid, len(left_half))])
        
        # Continue splitting right half
        right_mid = len(right_half) // 2
        right_left = VGroup(*[right_half[i] for i in range(right_mid)])
        right_right = VGroup(*[right_half[i] for i in range(right_mid, len(right_half))])
        
        # Animate second level split
        self.play(
            left_left.animate.shift(LEFT * 0.5 + DOWN * 0.8),
            left_right.animate.shift(RIGHT * 0.3 + DOWN * 0.8),
            right_left.animate.shift(LEFT * 0.3 + DOWN * 0.8),
            right_right.animate.shift(RIGHT * 0.5 + DOWN * 0.8),
            run_time=DURATION_NORMAL
        )
        
        # Show "divide until single elements" message
        divide_msg = Text(
            "Divide until single elements",
            font_size=LABEL_SIZE,
            color=TEXT_SECONDARY
        )
        divide_msg.to_edge(DOWN, buff=0.5)
        
        self.play(Write(divide_msg), run_time=DURATION_FAST)
        self.wait(PAUSE_SHORT)
        
        # Change all to single element color (sorted)
        all_bars = VGroup(left_left, left_right, right_left, right_right)
        
        self.play(
            *[bar[0].animate.set_fill(CORRECTLY_PLACED).set_stroke(CORRECTLY_PLACED) 
              for group in [left_left, left_right, right_left, right_right]
              for bar in group],
            run_time=DURATION_NORMAL
        )
