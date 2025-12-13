"""
Merge Sort Complexity Scene.
R2 compliant: One concept - time/space complexity.
R9 compliant: Minimal text, visual explanation.
"""
from manim import (
    Scene, Text, VGroup, Rectangle, RoundedRectangle,
    FadeIn, FadeOut, Write, Create, Transform,
    UP, DOWN, LEFT, RIGHT, ORIGIN,
    LaggedStart, AnimationGroup
)
import sys
sys.path.insert(0, '/home/hg/Desktop/algorthims/quickSortVsMergeSort')

from config.colors import (
    BACKGROUND_COLOR, TEXT_PRIMARY, TEXT_SECONDARY,
    COMPLEXITY_GOOD, COMPLEXITY_BAD, COMPLEXITY_NEUTRAL,
    TEMPORARY_STORAGE, CORRECTLY_PLACED
)
from config.fonts import HEADING_SIZE, BODY_SIZE, LABEL_SIZE, SMALL_SIZE
from config.animation_constants import (
    DURATION_FAST, DURATION_NORMAL, DURATION_SLOW,
    PAUSE_SHORT, PAUSE_NORMAL, PAUSE_LONG
)


class MergeSortComplexityScene(Scene):
    """
    Scene 8: Merge Sort Complexity Analysis.
    Concept: Consistent O(n log n) but O(n) space.
    """
    
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        
        # Title
        title = Text(
            "Merge Sort Complexity",
            font_size=HEADING_SIZE,
            color=TEXT_PRIMARY
        )
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=DURATION_NORMAL)
        
        # Show balanced tree (always balanced)
        self._show_balanced_tree()
        
        # Show space complexity
        self._show_space_complexity()
        
        # Show summary
        self._show_complexity_summary()
        
        self.wait(PAUSE_LONG)
    
    def _show_balanced_tree(self):
        """Show that merge sort always creates a balanced tree."""
        tree_label = Text("Always Balanced", font_size=BODY_SIZE, color=COMPLEXITY_GOOD)
        tree_label.move_to(UP * 1.5)
        
        # Create balanced tree visualization
        tree = VGroup()
        
        # Level 0
        root = Rectangle(width=3.0, height=0.25, fill_color=COMPLEXITY_GOOD, fill_opacity=0.8, stroke_width=0)
        tree.add(root)
        
        # Level 1
        l1_left = Rectangle(width=1.4, height=0.25, fill_color=COMPLEXITY_GOOD, fill_opacity=0.7, stroke_width=0)
        l1_right = Rectangle(width=1.4, height=0.25, fill_color=COMPLEXITY_GOOD, fill_opacity=0.7, stroke_width=0)
        l1_left.next_to(root, DOWN, buff=0.35).shift(LEFT * 0.8)
        l1_right.next_to(root, DOWN, buff=0.35).shift(RIGHT * 0.8)
        tree.add(l1_left, l1_right)
        
        # Level 2
        positions = [LEFT * 1.2, LEFT * 0.4, RIGHT * 0.4, RIGHT * 1.2]
        for i, pos in enumerate(positions):
            node = Rectangle(width=0.6, height=0.25, fill_color=COMPLEXITY_GOOD, fill_opacity=0.6, stroke_width=0)
            parent = l1_left if i < 2 else l1_right
            node.next_to(parent, DOWN, buff=0.35).shift(pos - parent.get_center()[0] * RIGHT)
            node.move_to([pos[0], parent.get_bottom()[1] - 0.5, 0])
            tree.add(node)
        
        tree.move_to(DOWN * 0.3)
        
        self.play(Write(tree_label), run_time=DURATION_FAST)
        self.play(FadeIn(tree), run_time=DURATION_NORMAL)
        
        # Complexity label
        time_label = Text("Time: O(n log n) - Always!", font_size=LABEL_SIZE, color=COMPLEXITY_GOOD)
        time_label.next_to(tree, DOWN, buff=0.5)
        
        self.play(Write(time_label), run_time=DURATION_NORMAL)
        self.wait(PAUSE_NORMAL)
        
        # Store for later
        self.tree_group = VGroup(tree_label, tree, time_label)
    
    def _show_space_complexity(self):
        """Show the O(n) space requirement."""
        # Move tree up
        self.play(
            self.tree_group.animate.scale(0.7).shift(UP * 1.5 + LEFT * 2.5),
            run_time=DURATION_NORMAL
        )
        
        # Show memory visualization
        memory_label = Text("Extra Memory Required", font_size=BODY_SIZE, color=TEMPORARY_STORAGE)
        memory_label.move_to(RIGHT * 2.5 + UP * 1.5)
        
        # Original array
        original = VGroup()
        for i in range(7):
            cell = Rectangle(
                width=0.4, height=0.4,
                fill_color=COMPLEXITY_GOOD,
                fill_opacity=0.7,
                stroke_color=COMPLEXITY_GOOD,
                stroke_width=1
            )
            original.add(cell)
        original.arrange(RIGHT, buff=0.05)
        original.next_to(memory_label, DOWN, buff=0.5)
        
        original_label = Text("Original: n", font_size=SMALL_SIZE, color=TEXT_SECONDARY)
        original_label.next_to(original, LEFT, buff=0.3)
        
        # Temporary array
        temp = VGroup()
        for i in range(7):
            cell = Rectangle(
                width=0.4, height=0.4,
                fill_color=TEMPORARY_STORAGE,
                fill_opacity=0.7,
                stroke_color=TEMPORARY_STORAGE,
                stroke_width=1
            )
            temp.add(cell)
        temp.arrange(RIGHT, buff=0.05)
        temp.next_to(original, DOWN, buff=0.4)
        
        temp_label = Text("Temp: n", font_size=SMALL_SIZE, color=TEMPORARY_STORAGE)
        temp_label.next_to(temp, LEFT, buff=0.3)
        
        self.play(
            Write(memory_label),
            FadeIn(original), Write(original_label),
            run_time=DURATION_NORMAL
        )
        
        self.play(
            FadeIn(temp), Write(temp_label),
            run_time=DURATION_NORMAL
        )
        
        # Space complexity
        space_label = Text("Space: O(n)", font_size=LABEL_SIZE, color=COMPLEXITY_BAD)
        space_label.next_to(temp, DOWN, buff=0.5)
        
        self.play(Write(space_label), run_time=DURATION_FAST)
        self.wait(PAUSE_NORMAL)
        
        # Store for later
        self.memory_group = VGroup(memory_label, original, original_label, temp, temp_label, space_label)
    
    def _show_complexity_summary(self):
        """Show final complexity summary."""
        # Fade out previous
        self.play(
            FadeOut(self.tree_group),
            FadeOut(self.memory_group),
            run_time=DURATION_FAST
        )
        
        # Summary
        summary_items = [
            ("Best:", "O(n log n)", COMPLEXITY_GOOD),
            ("Average:", "O(n log n)", COMPLEXITY_GOOD),
            ("Worst:", "O(n log n)", COMPLEXITY_GOOD),
            ("Space:", "O(n)", COMPLEXITY_BAD),
            ("Stable:", "Yes", COMPLEXITY_GOOD),
            ("In-place:", "No", COMPLEXITY_BAD),
        ]
        
        summary_group = VGroup()
        
        for label_text, value_text, color in summary_items:
            label = Text(label_text, font_size=LABEL_SIZE, color=TEXT_SECONDARY)
            value = Text(value_text, font_size=LABEL_SIZE, color=color)
            value.next_to(label, RIGHT, buff=0.3)
            row = VGroup(label, value)
            summary_group.add(row)
        
        summary_group.arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        summary_group.move_to(ORIGIN)
        
        self.play(
            LaggedStart(
                *[FadeIn(row, shift=LEFT * 0.3) for row in summary_group],
                lag_ratio=0.12
            ),
            run_time=DURATION_SLOW
        )
        
        # Key insight
        insight = Text(
            "Predictable performance, but needs extra memory",
            font_size=SMALL_SIZE,
            color=TEXT_SECONDARY
        )
        insight.next_to(summary_group, DOWN, buff=0.8)
        
        self.play(Write(insight), run_time=DURATION_NORMAL)
