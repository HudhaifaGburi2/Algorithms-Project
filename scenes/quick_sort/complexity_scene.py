"""
Quick Sort Complexity Scene.
R2 compliant: One concept - time/space complexity.
R9 compliant: Minimal text, visual explanation.
"""
from manim import (
    Scene, Text, VGroup, Rectangle, Line, Polygon,
    FadeIn, FadeOut, Write, Create, Transform,
    UP, DOWN, LEFT, RIGHT, ORIGIN,
    LaggedStart, AnimationGroup
)
import sys
sys.path.insert(0, '/home/hg/Desktop/algorthims/quickSortVsMergeSort')

from config.colors import (
    BACKGROUND_COLOR, TEXT_PRIMARY, TEXT_SECONDARY,
    COMPLEXITY_GOOD, COMPLEXITY_BAD, COMPLEXITY_NEUTRAL,
    CORRECTLY_PLACED, UNPROCESSED
)
from config.fonts import HEADING_SIZE, BODY_SIZE, LABEL_SIZE, SMALL_SIZE
from config.animation_constants import (
    DURATION_FAST, DURATION_NORMAL, DURATION_SLOW,
    PAUSE_SHORT, PAUSE_NORMAL, PAUSE_LONG
)


class QuickSortComplexityScene(Scene):
    """
    Scene 5: Quick Sort Complexity Analysis.
    Concept: Visual complexity comparison (best vs worst case).
    """
    
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        
        # Title
        title = Text(
            "Quick Sort Complexity",
            font_size=HEADING_SIZE,
            color=TEXT_PRIMARY
        )
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=DURATION_NORMAL)
        
        # Show two cases side by side
        self._show_complexity_comparison()
        
        # Show complexity summary
        self._show_complexity_summary()
        
        self.wait(PAUSE_LONG)
    
    def _create_tree_shape(self, balanced=True, color=COMPLEXITY_GOOD):
        """Create a tree shape to represent recursion."""
        tree = VGroup()
        
        if balanced:
            # Balanced tree (good case)
            # Level 0
            root = Rectangle(width=2.4, height=0.3, fill_color=color, fill_opacity=0.8, stroke_width=0)
            tree.add(root)
            
            # Level 1
            l1_left = Rectangle(width=1.1, height=0.3, fill_color=color, fill_opacity=0.7, stroke_width=0)
            l1_right = Rectangle(width=1.1, height=0.3, fill_color=color, fill_opacity=0.7, stroke_width=0)
            l1_left.next_to(root, DOWN, buff=0.3).shift(LEFT * 0.6)
            l1_right.next_to(root, DOWN, buff=0.3).shift(RIGHT * 0.6)
            tree.add(l1_left, l1_right)
            
            # Level 2
            for i, parent in enumerate([l1_left, l1_right]):
                for j, shift in enumerate([LEFT * 0.3, RIGHT * 0.3]):
                    node = Rectangle(width=0.5, height=0.3, fill_color=color, fill_opacity=0.6, stroke_width=0)
                    node.next_to(parent, DOWN, buff=0.3).shift(shift)
                    tree.add(node)
        else:
            # Skewed tree (worst case)
            prev = None
            for i in range(5):
                width = 2.4 - i * 0.4
                node = Rectangle(width=width, height=0.3, fill_color=color, fill_opacity=0.8 - i*0.1, stroke_width=0)
                if prev is None:
                    tree.add(node)
                else:
                    node.next_to(prev, DOWN, buff=0.3).align_to(prev, RIGHT)
                    tree.add(node)
                prev = node
        
        return tree
    
    def _show_complexity_comparison(self):
        """Show balanced vs skewed tree comparison."""
        # Labels
        best_label = Text("Best/Average Case", font_size=BODY_SIZE, color=COMPLEXITY_GOOD)
        worst_label = Text("Worst Case", font_size=BODY_SIZE, color=COMPLEXITY_BAD)
        
        best_label.move_to(LEFT * 3.5 + UP * 1.5)
        worst_label.move_to(RIGHT * 3.5 + UP * 1.5)
        
        # Trees
        balanced_tree = self._create_tree_shape(balanced=True, color=COMPLEXITY_GOOD)
        skewed_tree = self._create_tree_shape(balanced=False, color=COMPLEXITY_BAD)
        
        balanced_tree.next_to(best_label, DOWN, buff=0.5)
        skewed_tree.next_to(worst_label, DOWN, buff=0.5)
        
        # Complexity labels
        best_complexity = Text("O(n log n)", font_size=LABEL_SIZE, color=COMPLEXITY_GOOD)
        worst_complexity = Text("O(n²)", font_size=LABEL_SIZE, color=COMPLEXITY_BAD)
        
        best_complexity.next_to(balanced_tree, DOWN, buff=0.4)
        worst_complexity.next_to(skewed_tree, DOWN, buff=0.4)
        
        # Animate
        self.play(
            Write(best_label),
            Write(worst_label),
            run_time=DURATION_NORMAL
        )
        
        self.play(
            FadeIn(balanced_tree),
            FadeIn(skewed_tree),
            run_time=DURATION_NORMAL
        )
        
        self.play(
            Write(best_complexity),
            Write(worst_complexity),
            run_time=DURATION_NORMAL
        )
        
        self.wait(PAUSE_NORMAL)
        
        # Store for later fade out
        self.comparison_group = VGroup(
            best_label, worst_label,
            balanced_tree, skewed_tree,
            best_complexity, worst_complexity
        )
    
    def _show_complexity_summary(self):
        """Show final complexity summary."""
        # Fade out comparison
        self.play(
            self.comparison_group.animate.scale(0.6).shift(UP * 1.5),
            run_time=DURATION_NORMAL
        )
        
        # Summary box
        summary_items = [
            ("Average:", "O(n log n)", COMPLEXITY_GOOD),
            ("Worst:", "O(n²)", COMPLEXITY_BAD),
            ("Space:", "O(log n)", COMPLEXITY_NEUTRAL),
            ("In-place:", "Yes", COMPLEXITY_GOOD),
            ("Stable:", "No", COMPLEXITY_BAD),
        ]
        
        summary_group = VGroup()
        
        for label_text, value_text, color in summary_items:
            label = Text(label_text, font_size=LABEL_SIZE, color=TEXT_SECONDARY)
            value = Text(value_text, font_size=LABEL_SIZE, color=color)
            value.next_to(label, RIGHT, buff=0.3)
            row = VGroup(label, value)
            summary_group.add(row)
        
        summary_group.arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        summary_group.move_to(DOWN * 1.5)
        
        self.play(
            LaggedStart(
                *[FadeIn(row, shift=LEFT * 0.3) for row in summary_group],
                lag_ratio=0.15
            ),
            run_time=DURATION_SLOW
        )
