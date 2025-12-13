"""
Merge Sort Split Scene.
R2 compliant: One concept - the splitting phase.
R5 compliant: Recursion depth shown spatially.
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
    UNPROCESSED, CORRECTLY_PLACED, SUBARRAY_LEFT, SUBARRAY_RIGHT
)
from config.fonts import HEADING_SIZE, LABEL_SIZE, SMALL_SIZE
from config.animation_constants import (
    DURATION_FAST, DURATION_NORMAL, DURATION_SLOW,
    PAUSE_SHORT, PAUSE_NORMAL, RECURSION_VERTICAL_SPACING
)


class MergeSortSplitScene(Scene):
    """
    Scene: Merge Sort Split Phase.
    Concept: Visualize the divide phase as a tree.
    """
    
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        
        # Title
        title = Text(
            "Divide Phase",
            font_size=HEADING_SIZE,
            color=TEXT_PRIMARY
        )
        title.to_edge(UP, buff=0.3)
        self.play(Write(title), run_time=DURATION_NORMAL)
        
        # Build split tree
        self._build_split_tree()
        
        self.wait(PAUSE_NORMAL)
    
    def _create_mini_array(self, values, color=UNPROCESSED, scale=1.0):
        """Create a small array visualization."""
        bars = VGroup()
        for val in values:
            bar = Rectangle(
                width=0.35 * scale,
                height=val * 0.22 * scale,
                fill_color=color,
                fill_opacity=0.9,
                stroke_color=color,
                stroke_width=1.5
            )
            bars.add(bar)
        
        bars.arrange(RIGHT, buff=0.05 * scale)
        return bars
    
    def _build_split_tree(self):
        """Build and animate the split tree."""
        # Level 0: Original array
        level0 = self._create_mini_array([7, 2, 9, 4, 3, 8, 5])
        level0.move_to(UP * 2.2)
        
        label0 = Text("[7,2,9,4,3,8,5]", font_size=SMALL_SIZE, color=TEXT_SECONDARY)
        label0.next_to(level0, DOWN, buff=0.15)
        
        self.play(FadeIn(level0), FadeIn(label0), run_time=DURATION_NORMAL)
        self.wait(PAUSE_SHORT)
        
        # Level 1: Split into [7,2,9] and [4,3,8,5]
        level1_left = self._create_mini_array([7, 2, 9], SUBARRAY_LEFT, 0.9)
        level1_right = self._create_mini_array([4, 3, 8, 5], SUBARRAY_RIGHT, 0.9)
        
        level1_left.move_to(LEFT * 2.8 + UP * 0.6)
        level1_right.move_to(RIGHT * 2.8 + UP * 0.6)
        
        label1_left = Text("[7,2,9]", font_size=SMALL_SIZE, color=SUBARRAY_LEFT)
        label1_right = Text("[4,3,8,5]", font_size=SMALL_SIZE, color=SUBARRAY_RIGHT)
        label1_left.next_to(level1_left, DOWN, buff=0.15)
        label1_right.next_to(level1_right, DOWN, buff=0.15)
        
        # Connection lines
        line1_left = Line(level0.get_bottom(), level1_left.get_top(), color=TEXT_SECONDARY, stroke_width=2)
        line1_right = Line(level0.get_bottom(), level1_right.get_top(), color=TEXT_SECONDARY, stroke_width=2)
        
        self.play(
            Create(line1_left), Create(line1_right),
            FadeIn(level1_left), FadeIn(level1_right),
            FadeIn(label1_left), FadeIn(label1_right),
            run_time=DURATION_NORMAL
        )
        self.wait(PAUSE_SHORT)
        
        # Level 2: Further splits
        # [7,2,9] -> [7] and [2,9]
        level2_ll = self._create_mini_array([7], SUBARRAY_LEFT, 0.8)
        level2_lr = self._create_mini_array([2, 9], SUBARRAY_LEFT, 0.8)
        
        # [4,3,8,5] -> [4,3] and [8,5]
        level2_rl = self._create_mini_array([4, 3], SUBARRAY_RIGHT, 0.8)
        level2_rr = self._create_mini_array([8, 5], SUBARRAY_RIGHT, 0.8)
        
        level2_ll.move_to(LEFT * 4 + DOWN * 0.8)
        level2_lr.move_to(LEFT * 2 + DOWN * 0.8)
        level2_rl.move_to(RIGHT * 2 + DOWN * 0.8)
        level2_rr.move_to(RIGHT * 4 + DOWN * 0.8)
        
        # Labels
        label2_ll = Text("[7]", font_size=SMALL_SIZE, color=TEXT_SECONDARY)
        label2_lr = Text("[2,9]", font_size=SMALL_SIZE, color=TEXT_SECONDARY)
        label2_rl = Text("[4,3]", font_size=SMALL_SIZE, color=TEXT_SECONDARY)
        label2_rr = Text("[8,5]", font_size=SMALL_SIZE, color=TEXT_SECONDARY)
        
        label2_ll.next_to(level2_ll, DOWN, buff=0.15)
        label2_lr.next_to(level2_lr, DOWN, buff=0.15)
        label2_rl.next_to(level2_rl, DOWN, buff=0.15)
        label2_rr.next_to(level2_rr, DOWN, buff=0.15)
        
        # Connection lines
        lines2 = VGroup(
            Line(level1_left.get_bottom(), level2_ll.get_top(), color=TEXT_SECONDARY, stroke_width=1.5),
            Line(level1_left.get_bottom(), level2_lr.get_top(), color=TEXT_SECONDARY, stroke_width=1.5),
            Line(level1_right.get_bottom(), level2_rl.get_top(), color=TEXT_SECONDARY, stroke_width=1.5),
            Line(level1_right.get_bottom(), level2_rr.get_top(), color=TEXT_SECONDARY, stroke_width=1.5),
        )
        
        self.play(
            Create(lines2),
            FadeIn(level2_ll), FadeIn(level2_lr), FadeIn(level2_rl), FadeIn(level2_rr),
            FadeIn(label2_ll), FadeIn(label2_lr), FadeIn(label2_rl), FadeIn(label2_rr),
            run_time=DURATION_NORMAL
        )
        self.wait(PAUSE_SHORT)
        
        # Level 3: Single elements
        level3_items = [
            (level2_lr, [[2], [9]], LEFT * 2.5, LEFT * 1.5),
            (level2_rl, [[4], [3]], RIGHT * 1.5, RIGHT * 2.5),
            (level2_rr, [[8], [5]], RIGHT * 3.5, RIGHT * 4.5),
        ]
        
        level3_arrays = []
        level3_labels = []
        level3_lines = VGroup()
        
        for parent, values_list, pos1, pos2 in level3_items:
            arr1 = self._create_mini_array(values_list[0], CORRECTLY_PLACED, 0.7)
            arr2 = self._create_mini_array(values_list[1], CORRECTLY_PLACED, 0.7)
            
            arr1.move_to(pos1 + DOWN * 2.2)
            arr2.move_to(pos2 + DOWN * 2.2)
            
            lbl1 = Text(str(values_list[0]), font_size=SMALL_SIZE, color=CORRECTLY_PLACED)
            lbl2 = Text(str(values_list[1]), font_size=SMALL_SIZE, color=CORRECTLY_PLACED)
            lbl1.next_to(arr1, DOWN, buff=0.1)
            lbl2.next_to(arr2, DOWN, buff=0.1)
            
            level3_arrays.extend([arr1, arr2])
            level3_labels.extend([lbl1, lbl2])
            
            level3_lines.add(
                Line(parent.get_bottom(), arr1.get_top(), color=TEXT_SECONDARY, stroke_width=1),
                Line(parent.get_bottom(), arr2.get_top(), color=TEXT_SECONDARY, stroke_width=1)
            )
        
        # Also mark [7] as single element (already single)
        self.play(
            level2_ll[0].animate.set_fill(CORRECTLY_PLACED).set_stroke(CORRECTLY_PLACED),
            label2_ll.animate.set_color(CORRECTLY_PLACED),
            run_time=DURATION_FAST
        )
        
        self.play(
            Create(level3_lines),
            *[FadeIn(arr) for arr in level3_arrays],
            *[FadeIn(lbl) for lbl in level3_labels],
            run_time=DURATION_NORMAL
        )
        
        # Final message
        msg = Text("All single elements - ready to merge!", font_size=LABEL_SIZE, color=CORRECTLY_PLACED)
        msg.to_edge(DOWN, buff=0.3)
        
        self.play(Write(msg), run_time=DURATION_FAST)
