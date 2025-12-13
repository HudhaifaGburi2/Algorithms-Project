"""
Quick Sort Recursion Scene.
R2 compliant: One concept - recursion visualization.
R5 compliant: Recursion shown spatially via vertical depth.
"""
from manim import (
    Scene, Text, VGroup, Rectangle, Line,
    FadeIn, FadeOut, Write, Create, Transform,
    UP, DOWN, LEFT, RIGHT, ORIGIN,
    LaggedStart, AnimationGroup
)
import sys
sys.path.insert(0, '/home/hg/Desktop/algorthims/quickSortVsMergeSort')

from config.colors import (
    BACKGROUND_COLOR, TEXT_PRIMARY, TEXT_SECONDARY,
    UNPROCESSED, PIVOT, CORRECTLY_PLACED,
    SUBARRAY_LEFT, SUBARRAY_RIGHT
)
from config.fonts import HEADING_SIZE, LABEL_SIZE, SMALL_SIZE
from config.animation_constants import (
    DURATION_FAST, DURATION_NORMAL, DURATION_SLOW,
    PAUSE_SHORT, PAUSE_NORMAL, EASE_DEFAULT,
    RECURSION_VERTICAL_SPACING, SCALE_RECURSION_DEPTH
)


class QuickSortRecursionScene(Scene):
    """
    Scene: Quick Sort Recursion Tree.
    Concept: Visualize recursive divide-and-conquer spatially.
    R5: Vertical position = recursion depth.
    """
    
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        
        # Title
        title = Text(
            "Recursion Tree",
            font_size=HEADING_SIZE,
            color=TEXT_PRIMARY
        )
        title.to_edge(UP, buff=0.3)
        self.play(Write(title), run_time=DURATION_NORMAL)
        
        # Build recursion tree visualization
        self._build_recursion_tree()
        
        self.wait(PAUSE_NORMAL)
    
    def _create_mini_array(self, values, color=UNPROCESSED, scale=1.0):
        """Create a small array visualization."""
        bars = VGroup()
        for val in values:
            bar = Rectangle(
                width=0.3 * scale,
                height=val * 0.2 * scale,
                fill_color=color,
                fill_opacity=0.9,
                stroke_color=color,
                stroke_width=1.5
            )
            bars.add(bar)
        
        bars.arrange(RIGHT, buff=0.05 * scale)
        
        # Add label showing values
        label = Text(
            str(values),
            font_size=int(SMALL_SIZE * scale),
            color=TEXT_SECONDARY
        )
        label.next_to(bars, DOWN, buff=0.1)
        
        return VGroup(bars, label)
    
    def _build_recursion_tree(self):
        """Build and animate the recursion tree."""
        # Level 0: Original array
        level0 = self._create_mini_array([7, 2, 9, 4, 3, 8, 5])
        level0.move_to(UP * 2)
        
        self.play(FadeIn(level0), run_time=DURATION_NORMAL)
        self.wait(PAUSE_SHORT)
        
        # Highlight pivot and show partition
        pivot_indicator = Text("pivot: 5", font_size=SMALL_SIZE, color=PIVOT)
        pivot_indicator.next_to(level0, RIGHT, buff=0.5)
        self.play(FadeIn(pivot_indicator), run_time=DURATION_FAST)
        self.wait(PAUSE_SHORT)
        
        # Level 1: After first partition [2,4,3] [5] [7,9,8]
        level1_left = self._create_mini_array([2, 4, 3], SUBARRAY_LEFT, 0.85)
        level1_pivot = self._create_mini_array([5], CORRECTLY_PLACED, 0.85)
        level1_right = self._create_mini_array([7, 9, 8], SUBARRAY_RIGHT, 0.85)
        
        level1_left.move_to(LEFT * 3.5 + UP * 0.3)
        level1_pivot.move_to(UP * 0.3)
        level1_right.move_to(RIGHT * 3.5 + UP * 0.3)
        
        # Connection lines
        line_left = Line(
            level0.get_bottom(),
            level1_left.get_top(),
            color=TEXT_SECONDARY,
            stroke_width=2
        )
        line_mid = Line(
            level0.get_bottom(),
            level1_pivot.get_top(),
            color=CORRECTLY_PLACED,
            stroke_width=2
        )
        line_right = Line(
            level0.get_bottom(),
            level1_right.get_top(),
            color=TEXT_SECONDARY,
            stroke_width=2
        )
        
        self.play(
            FadeOut(pivot_indicator),
            Create(line_left),
            Create(line_mid),
            Create(line_right),
            FadeIn(level1_left),
            FadeIn(level1_pivot),
            FadeIn(level1_right),
            run_time=DURATION_SLOW
        )
        self.wait(PAUSE_SHORT)
        
        # Level 2: Further partitions
        # Left subtree: [2,4,3] -> pivot 3 -> [2] [3] [4]
        level2_ll = self._create_mini_array([2], CORRECTLY_PLACED, 0.7)
        level2_lm = self._create_mini_array([3], CORRECTLY_PLACED, 0.7)
        level2_lr = self._create_mini_array([4], CORRECTLY_PLACED, 0.7)
        
        level2_ll.move_to(LEFT * 4.5 + DOWN * 1.2)
        level2_lm.move_to(LEFT * 3.5 + DOWN * 1.2)
        level2_lr.move_to(LEFT * 2.5 + DOWN * 1.2)
        
        # Right subtree: [7,9,8] -> pivot 8 -> [7] [8] [9]
        level2_rl = self._create_mini_array([7], CORRECTLY_PLACED, 0.7)
        level2_rm = self._create_mini_array([8], CORRECTLY_PLACED, 0.7)
        level2_rr = self._create_mini_array([9], CORRECTLY_PLACED, 0.7)
        
        level2_rl.move_to(RIGHT * 2.5 + DOWN * 1.2)
        level2_rm.move_to(RIGHT * 3.5 + DOWN * 1.2)
        level2_rr.move_to(RIGHT * 4.5 + DOWN * 1.2)
        
        # Connection lines for level 2
        lines_l = VGroup(
            Line(level1_left.get_bottom(), level2_ll.get_top(), color=TEXT_SECONDARY, stroke_width=1.5),
            Line(level1_left.get_bottom(), level2_lm.get_top(), color=TEXT_SECONDARY, stroke_width=1.5),
            Line(level1_left.get_bottom(), level2_lr.get_top(), color=TEXT_SECONDARY, stroke_width=1.5),
        )
        
        lines_r = VGroup(
            Line(level1_right.get_bottom(), level2_rl.get_top(), color=TEXT_SECONDARY, stroke_width=1.5),
            Line(level1_right.get_bottom(), level2_rm.get_top(), color=TEXT_SECONDARY, stroke_width=1.5),
            Line(level1_right.get_bottom(), level2_rr.get_top(), color=TEXT_SECONDARY, stroke_width=1.5),
        )
        
        self.play(
            Create(lines_l),
            Create(lines_r),
            FadeIn(level2_ll), FadeIn(level2_lm), FadeIn(level2_lr),
            FadeIn(level2_rl), FadeIn(level2_rm), FadeIn(level2_rr),
            run_time=DURATION_SLOW
        )
        self.wait(PAUSE_SHORT)
        
        # Show final sorted array at bottom
        sorted_array = self._create_mini_array([2, 3, 4, 5, 7, 8, 9], CORRECTLY_PLACED)
        sorted_array.move_to(DOWN * 2.8)
        
        sorted_label = Text("Sorted!", font_size=LABEL_SIZE, color=CORRECTLY_PLACED)
        sorted_label.next_to(sorted_array, DOWN, buff=0.3)
        
        self.play(
            FadeIn(sorted_array),
            Write(sorted_label),
            run_time=DURATION_NORMAL
        )
        
        # Add depth labels on the side
        depth_labels = VGroup()
        for i, y_pos in enumerate([2, 0.3, -1.2]):
            label = Text(f"depth {i}", font_size=SMALL_SIZE, color=TEXT_SECONDARY)
            label.move_to(LEFT * 6 + UP * y_pos)
            depth_labels.add(label)
        
        self.play(
            LaggedStart(*[FadeIn(l) for l in depth_labels], lag_ratio=0.2),
            run_time=DURATION_NORMAL
        )
