"""
Final Summary Scene.
R2 compliant: One concept - final takeaways.
R9 compliant: Minimal text, clear summary.
"""
from manim import (
    Scene, Text, VGroup, Rectangle, Table, Line,
    FadeIn, FadeOut, Write, Create, Transform,
    UP, DOWN, LEFT, RIGHT, ORIGIN,
    LaggedStart, AnimationGroup
)
import sys
sys.path.insert(0, '/home/hg/Desktop/algorthims/quickSortVsMergeSort')

from config.colors import (
    BACKGROUND_COLOR, TEXT_PRIMARY, TEXT_SECONDARY,
    COMPLEXITY_GOOD, COMPLEXITY_BAD, COMPLEXITY_NEUTRAL,
    PIVOT, TEMPORARY_STORAGE, CORRECTLY_PLACED
)
from config.fonts import HEADING_SIZE, BODY_SIZE, LABEL_SIZE, SMALL_SIZE
from config.animation_constants import (
    DURATION_FAST, DURATION_NORMAL, DURATION_SLOW,
    PAUSE_SHORT, PAUSE_NORMAL, PAUSE_LONG
)


class FinalSummaryScene(Scene):
    """
    Scene 10: Final Summary.
    Concept: Key takeaways and when to use each algorithm.
    """
    
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        
        # Title
        title = Text(
            "Summary",
            font_size=HEADING_SIZE,
            color=TEXT_PRIMARY
        )
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=DURATION_NORMAL)
        
        # Comparison table
        self._show_comparison_table()
        
        # Final takeaways
        self._show_takeaways()
        
        self.wait(PAUSE_LONG)
    
    def _show_comparison_table(self):
        """Show comparison table."""
        # Headers
        header_row = VGroup(
            Text("", font_size=LABEL_SIZE),
            Text("Quick Sort", font_size=LABEL_SIZE, color=PIVOT),
            Text("Merge Sort", font_size=LABEL_SIZE, color=TEMPORARY_STORAGE)
        )
        header_row.arrange(RIGHT, buff=1.5)
        header_row.move_to(UP * 1.5)
        
        # Data rows
        rows_data = [
            ("Best Case", "O(n log n)", "O(n log n)", COMPLEXITY_GOOD, COMPLEXITY_GOOD),
            ("Average", "O(n log n)", "O(n log n)", COMPLEXITY_GOOD, COMPLEXITY_GOOD),
            ("Worst Case", "O(n²)", "O(n log n)", COMPLEXITY_BAD, COMPLEXITY_GOOD),
            ("Space", "O(log n)", "O(n)", COMPLEXITY_GOOD, COMPLEXITY_BAD),
            ("Stable", "No", "Yes", COMPLEXITY_BAD, COMPLEXITY_GOOD),
            ("In-place", "Yes", "No", COMPLEXITY_GOOD, COMPLEXITY_BAD),
        ]
        
        table_rows = VGroup()
        
        for label, qs_val, ms_val, qs_color, ms_color in rows_data:
            row = VGroup(
                Text(label, font_size=SMALL_SIZE, color=TEXT_SECONDARY),
                Text(qs_val, font_size=SMALL_SIZE, color=qs_color),
                Text(ms_val, font_size=SMALL_SIZE, color=ms_color)
            )
            row.arrange(RIGHT, buff=1.5)
            # Align with header
            row[0].align_to(header_row[0], LEFT)
            row[1].align_to(header_row[1], LEFT)
            row[2].align_to(header_row[2], LEFT)
            table_rows.add(row)
        
        table_rows.arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        table_rows.next_to(header_row, DOWN, buff=0.4)
        
        # Animate
        self.play(
            LaggedStart(
                *[Write(h) for h in header_row],
                lag_ratio=0.2
            ),
            run_time=DURATION_NORMAL
        )
        
        self.play(
            LaggedStart(
                *[FadeIn(row, shift=LEFT * 0.2) for row in table_rows],
                lag_ratio=0.1
            ),
            run_time=DURATION_SLOW
        )
        
        self.wait(PAUSE_NORMAL)
        
        # Store for later
        self.table_group = VGroup(header_row, table_rows)
    
    def _show_takeaways(self):
        """Show final takeaways."""
        # Move table up
        self.play(
            self.table_group.animate.scale(0.75).shift(UP * 1.2),
            run_time=DURATION_NORMAL
        )
        
        # Takeaway boxes
        qs_box = self._create_takeaway_box(
            "Quick Sort",
            "Faster in practice",
            "Use when memory is limited",
            PIVOT
        )
        
        ms_box = self._create_takeaway_box(
            "Merge Sort", 
            "Predictable & stable",
            "Use when stability matters",
            TEMPORARY_STORAGE
        )
        
        qs_box.move_to(LEFT * 3 + DOWN * 1.8)
        ms_box.move_to(RIGHT * 3 + DOWN * 1.8)
        
        self.play(
            FadeIn(qs_box, shift=UP * 0.3),
            FadeIn(ms_box, shift=UP * 0.3),
            run_time=DURATION_NORMAL
        )
        
        self.wait(PAUSE_NORMAL)
        
        # Final message
        final_msg = Text(
            "Choose based on your constraints!",
            font_size=BODY_SIZE,
            color=CORRECTLY_PLACED
        )
        final_msg.to_edge(DOWN, buff=0.5)
        
        self.play(Write(final_msg), run_time=DURATION_NORMAL)
    
    def _create_takeaway_box(self, title, line1, line2, color):
        """Create a takeaway box."""
        from manim import RoundedRectangle
        
        box = RoundedRectangle(
            width=4.5,
            height=1.8,
            corner_radius=0.15,
            fill_color=color,
            fill_opacity=0.1,
            stroke_color=color,
            stroke_width=2
        )
        
        title_text = Text(title, font_size=LABEL_SIZE, color=color)
        line1_text = Text(line1, font_size=SMALL_SIZE, color=TEXT_PRIMARY)
        line2_text = Text(line2, font_size=SMALL_SIZE, color=TEXT_SECONDARY)
        
        content = VGroup(title_text, line1_text, line2_text)
        content.arrange(DOWN, buff=0.15)
        content.move_to(box.get_center())
        
        return VGroup(box, content)


class ClosingScene(Scene):
    """
    Closing scene with sorted array.
    """
    
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        
        # Final sorted array
        values = [2, 3, 4, 5, 7, 8, 9]
        
        bars = VGroup()
        for val in values:
            bar = Rectangle(
                width=0.6,
                height=val * 0.4,
                fill_color=CORRECTLY_PLACED,
                fill_opacity=0.9,
                stroke_color=CORRECTLY_PLACED,
                stroke_width=2
            )
            bars.add(bar)
        
        bars.arrange(RIGHT, buff=0.15)
        bars.move_to(ORIGIN)
        
        self.play(
            LaggedStart(
                *[FadeIn(bar, shift=UP * 0.5) for bar in bars],
                lag_ratio=0.1
            ),
            run_time=DURATION_NORMAL
        )
        
        # Title
        title = Text(
            "Sorting Complete",
            font_size=HEADING_SIZE,
            color=TEXT_PRIMARY
        )
        title.next_to(bars, UP, buff=1.0)
        
        self.play(Write(title), run_time=DURATION_NORMAL)
        
        # Subtitle
        subtitle = Text(
            "Quick Sort vs Merge Sort",
            font_size=BODY_SIZE,
            color=TEXT_SECONDARY
        )
        subtitle.next_to(bars, DOWN, buff=1.0)
        
        self.play(FadeIn(subtitle), run_time=DURATION_FAST)
        
        self.wait(PAUSE_LONG)
