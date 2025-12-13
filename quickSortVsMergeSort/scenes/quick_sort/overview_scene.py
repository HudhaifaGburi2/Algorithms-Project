"""
Quick Sort Overview Scene.
R2 compliant: One concept - Quick Sort intuition.
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
    UNPROCESSED, PIVOT, CORRECTLY_PLACED, ACTIVE_COMPARISON,
    SUBARRAY_LEFT, SUBARRAY_RIGHT
)
from config.fonts import HEADING_SIZE, BODY_SIZE, LABEL_SIZE
from config.animation_constants import (
    DURATION_FAST, DURATION_NORMAL, DURATION_SLOW,
    PAUSE_SHORT, PAUSE_NORMAL, EASE_DEFAULT,
    BAR_WIDTH, BAR_HEIGHT_SCALE
)


class QuickSortOverviewScene(Scene):
    """
    Scene 3: Quick Sort Conceptual Overview.
    Concept: Pivot selection and partitioning intuition.
    """
    
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        
        # Title
        title = Text(
            "Quick Sort",
            font_size=HEADING_SIZE,
            color=TEXT_PRIMARY
        )
        title.to_edge(UP, buff=0.5)
        
        self.play(Write(title), run_time=DURATION_NORMAL)
        
        # Create array visualization
        values = [7, 2, 9, 4, 3, 8, 5]
        array_group = self._create_array_bars(values)
        array_group.next_to(title, DOWN, buff=1.0)
        
        self.play(
            LaggedStart(
                *[FadeIn(bar, shift=UP * 0.3) for bar in array_group],
                lag_ratio=0.1
            ),
            run_time=DURATION_NORMAL
        )
        self.wait(PAUSE_NORMAL)
        
        # Highlight pivot (last element)
        pivot_idx = len(values) - 1
        pivot_bar = array_group[pivot_idx]
        
        pivot_label = Text("pivot", font_size=LABEL_SIZE, color=PIVOT)
        pivot_label.next_to(pivot_bar, UP, buff=0.3)
        
        self.play(
            pivot_bar.animate.set_fill(PIVOT).set_stroke(PIVOT),
            FadeIn(pivot_label),
            run_time=DURATION_NORMAL
        )
        self.wait(PAUSE_SHORT)
        
        # Show partitioning concept with arrows
        self._show_partition_concept(array_group, pivot_idx, pivot_label)
        
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
    
    def _show_partition_concept(self, array_group, pivot_idx, pivot_label):
        """Visualize the partitioning concept."""
        pivot_val = 5  # Known pivot value
        
        # Create "less than" and "greater than" labels
        less_label = Text("< 5", font_size=BODY_SIZE, color=SUBARRAY_LEFT)
        greater_label = Text("> 5", font_size=BODY_SIZE, color=SUBARRAY_RIGHT)
        
        less_label.next_to(array_group, DOWN, buff=1.5)
        less_label.shift(LEFT * 2)
        greater_label.next_to(array_group, DOWN, buff=1.5)
        greater_label.shift(RIGHT * 2)
        
        # Create arrows showing partition direction
        left_arrow = Arrow(
            array_group.get_bottom() + LEFT * 0.5,
            less_label.get_top(),
            color=SUBARRAY_LEFT,
            buff=0.2
        )
        right_arrow = Arrow(
            array_group.get_bottom() + RIGHT * 0.5,
            greater_label.get_top(),
            color=SUBARRAY_RIGHT,
            buff=0.2
        )
        
        self.play(
            Create(left_arrow),
            Create(right_arrow),
            Write(less_label),
            Write(greater_label),
            run_time=DURATION_NORMAL
        )
        
        # Color elements based on comparison with pivot
        values = [7, 2, 9, 4, 3, 8, 5]
        animations = []
        
        for i, val in enumerate(values):
            if i == pivot_idx:
                continue
            bar = array_group[i][0]  # Get rectangle from group
            if val < pivot_val:
                animations.append(bar.animate.set_fill(SUBARRAY_LEFT).set_stroke(SUBARRAY_LEFT))
            else:
                animations.append(bar.animate.set_fill(SUBARRAY_RIGHT).set_stroke(SUBARRAY_RIGHT))
        
        self.play(*animations, run_time=DURATION_NORMAL)
        self.wait(PAUSE_NORMAL)
        
        # Show elements moving to their sides
        left_elements = VGroup()
        right_elements = VGroup()
        
        for i, val in enumerate(values):
            if i == pivot_idx:
                continue
            if val < pivot_val:
                left_elements.add(array_group[i])
            else:
                right_elements.add(array_group[i])
        
        pivot_group = array_group[pivot_idx]
        
        # Animate partition
        self.play(
            left_elements.animate.shift(LEFT * 1.5 + DOWN * 0.5),
            right_elements.animate.shift(RIGHT * 1.5 + DOWN * 0.5),
            pivot_group.animate.shift(DOWN * 0.5),
            pivot_label.animate.shift(DOWN * 0.5),
            run_time=DURATION_SLOW
        )
        
        # Mark pivot as correctly placed
        self.play(
            pivot_group[0].animate.set_fill(CORRECTLY_PLACED).set_stroke(CORRECTLY_PLACED),
            run_time=DURATION_FAST
        )
        
        # Add "sorted" indicator
        sorted_label = Text("✓", font_size=LABEL_SIZE, color=CORRECTLY_PLACED)
        sorted_label.next_to(pivot_group, DOWN, buff=0.2)
        
        self.play(FadeIn(sorted_label), run_time=DURATION_FAST)
