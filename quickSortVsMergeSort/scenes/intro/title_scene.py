"""
Title Scene: Introduction and motivation.
R2 compliant: One concept - introducing the comparison topic.
R9 compliant: Minimal text, visual focus.
"""
from manim import (
    Scene, Text, VGroup, 
    FadeIn, FadeOut, Write, Transform,
    UP, DOWN, LEFT, RIGHT, ORIGIN,
    config, LaggedStart
)
import sys
sys.path.insert(0, '/home/hg/Desktop/algorthims/quickSortVsMergeSort')

from config.colors import (
    BACKGROUND_COLOR, TEXT_PRIMARY, TEXT_SECONDARY,
    UNPROCESSED, CORRECTLY_PLACED, PIVOT, TEMPORARY_STORAGE
)
from config.fonts import TITLE_SIZE, SUBTITLE_SIZE, BODY_SIZE
from config.animation_constants import (
    DURATION_NORMAL, DURATION_SLOW, DURATION_EMPHASIS,
    PAUSE_NORMAL, PAUSE_LONG, EASE_DEFAULT
)


class TitleScene(Scene):
    """
    Scene 1: Title and Motivation.
    Concept: Introduce Quick Sort vs Merge Sort comparison.
    """
    
    def construct(self):
        # Set background
        self.camera.background_color = BACKGROUND_COLOR
        
        # Create title
        title = Text(
            "Quick Sort vs Merge Sort",
            font_size=TITLE_SIZE,
            color=TEXT_PRIMARY
        )
        
        # Create subtitle
        subtitle = Text(
            "Two Divide-and-Conquer Algorithms",
            font_size=SUBTITLE_SIZE,
            color=TEXT_SECONDARY
        )
        subtitle.next_to(title, DOWN, buff=0.5)
        
        # Group title elements
        title_group = VGroup(title, subtitle)
        title_group.move_to(ORIGIN)
        
        # Animate title appearance
        self.play(
            Write(title, run_time=DURATION_EMPHASIS),
            rate_func=EASE_DEFAULT
        )
        self.wait(PAUSE_NORMAL)
        
        self.play(
            FadeIn(subtitle, shift=UP * 0.3),
            run_time=DURATION_NORMAL
        )
        self.wait(PAUSE_NORMAL)
        
        # Create visual representation of divide-and-conquer
        self._show_divide_conquer_preview(title_group)
        
        self.wait(PAUSE_LONG)
    
    def _show_divide_conquer_preview(self, title_group):
        """Show visual preview of divide-and-conquer concept."""
        from manim import Rectangle, Arrow, MoveToTarget
        
        # Move title up
        self.play(
            title_group.animate.shift(UP * 2),
            run_time=DURATION_NORMAL
        )
        
        # Create unsorted array representation
        bars = VGroup()
        values = [7, 2, 9, 4, 3, 8, 5]
        
        for i, val in enumerate(values):
            bar = Rectangle(
                width=0.5,
                height=val * 0.35,
                fill_color=UNPROCESSED,
                fill_opacity=0.9,
                stroke_color=UNPROCESSED,
                stroke_width=2
            )
            bars.add(bar)
        
        bars.arrange(RIGHT, buff=0.1)
        bars.next_to(title_group, DOWN, buff=1.0)
        
        # Animate bars appearing
        self.play(
            LaggedStart(
                *[FadeIn(bar, shift=UP * 0.5) for bar in bars],
                lag_ratio=0.1
            ),
            run_time=DURATION_NORMAL
        )
        self.wait(PAUSE_NORMAL)
        
        # Show split into two groups (divide concept)
        left_group = VGroup(*bars[:3])
        right_group = VGroup(*bars[4:])
        pivot_bar = bars[3]
        
        # Color pivot
        self.play(
            pivot_bar.animate.set_fill(PIVOT).set_stroke(PIVOT),
            run_time=DURATION_NORMAL
        )
        
        # Split animation
        self.play(
            left_group.animate.shift(LEFT * 0.8),
            right_group.animate.shift(RIGHT * 0.8),
            run_time=DURATION_NORMAL
        )
        self.wait(PAUSE_NORMAL)
        
        # Show sorted result
        sorted_bars = VGroup()
        sorted_values = [2, 3, 4, 5, 7, 8, 9]
        
        for val in sorted_values:
            bar = Rectangle(
                width=0.5,
                height=val * 0.35,
                fill_color=CORRECTLY_PLACED,
                fill_opacity=0.9,
                stroke_color=CORRECTLY_PLACED,
                stroke_width=2
            )
            sorted_bars.add(bar)
        
        sorted_bars.arrange(RIGHT, buff=0.1)
        sorted_bars.move_to(bars.get_center())
        
        # Transform to sorted
        self.play(
            Transform(VGroup(left_group, pivot_bar, right_group), sorted_bars),
            run_time=DURATION_EMPHASIS
        )
        self.wait(PAUSE_NORMAL)


class MotivationScene(Scene):
    """
    Brief motivation showing why sorting matters.
    Concept: Visual importance of sorting.
    """
    
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        
        # Simple visual: chaos to order
        from manim import Circle, Square, Triangle, Polygon
        
        # Create scattered shapes
        shapes = VGroup()
        positions = [
            LEFT * 3 + UP, RIGHT * 2 + DOWN * 0.5,
            LEFT + DOWN, RIGHT * 3 + UP * 0.5,
            ORIGIN + UP * 1.5, LEFT * 2 + DOWN * 1.5,
            RIGHT + UP
        ]
        
        for i, pos in enumerate(positions):
            shape = Circle(radius=0.3, fill_opacity=0.8, color=UNPROCESSED)
            shape.move_to(pos)
            shapes.add(shape)
        
        self.play(
            LaggedStart(*[FadeIn(s) for s in shapes], lag_ratio=0.1),
            run_time=DURATION_NORMAL
        )
        self.wait(PAUSE_NORMAL)
        
        # Arrange in order
        self.play(
            shapes.animate.arrange(RIGHT, buff=0.3).move_to(ORIGIN),
            run_time=DURATION_EMPHASIS
        )
        
        # Change to sorted color
        self.play(
            *[s.animate.set_fill(CORRECTLY_PLACED).set_stroke(CORRECTLY_PLACED) 
              for s in shapes],
            run_time=DURATION_NORMAL
        )
        
        self.wait(PAUSE_LONG)
