"""
Merge Sort Merge Scene.
R2 compliant: One concept - the merging process.
R4 compliant: Purple for temporary storage.
"""
from manim import (
    Scene, Text, VGroup, Rectangle, RoundedRectangle, Arrow,
    FadeIn, FadeOut, Write, Create, Transform, MoveToTarget,
    UP, DOWN, LEFT, RIGHT, ORIGIN,
    LaggedStart, AnimationGroup
)
import sys
sys.path.insert(0, '/home/hg/Desktop/algorthims/quickSortVsMergeSort')

from config.colors import (
    BACKGROUND_COLOR, TEXT_PRIMARY, TEXT_SECONDARY,
    UNPROCESSED, TEMPORARY_STORAGE, CORRECTLY_PLACED,
    ACTIVE_COMPARISON, SUBARRAY_LEFT, SUBARRAY_RIGHT
)
from config.fonts import HEADING_SIZE, BODY_SIZE, LABEL_SIZE, SMALL_SIZE
from config.animation_constants import (
    DURATION_FAST, DURATION_NORMAL, DURATION_SLOW,
    PAUSE_SHORT, PAUSE_NORMAL, BAR_WIDTH, BAR_HEIGHT_SCALE
)


class MergeSortMergeScene(Scene):
    """
    Scene 7: Merge Sort Merging Process.
    Concept: How two sorted arrays merge into one.
    """
    
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        
        # Title
        title = Text(
            "Merge Process",
            font_size=HEADING_SIZE,
            color=TEXT_PRIMARY
        )
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=DURATION_NORMAL)
        
        # Show merge of two small arrays
        self._animate_merge_process()
        
        self.wait(PAUSE_NORMAL)
    
    def _create_bar(self, value, color=UNPROCESSED):
        """Create a single bar with label."""
        bar = Rectangle(
            width=BAR_WIDTH * 0.8,
            height=value * BAR_HEIGHT_SCALE * 0.8,
            fill_color=color,
            fill_opacity=0.9,
            stroke_color=color,
            stroke_width=2
        )
        label = Text(str(value), font_size=LABEL_SIZE, color=TEXT_PRIMARY)
        label.next_to(bar, UP, buff=0.1)
        return VGroup(bar, label)
    
    def _animate_merge_process(self):
        """Animate merging [2, 7] and [4, 9]."""
        # Create two sorted arrays
        left_values = [2, 7]
        right_values = [4, 9]
        
        left_bars = VGroup(*[self._create_bar(v, SUBARRAY_LEFT) for v in left_values])
        right_bars = VGroup(*[self._create_bar(v, SUBARRAY_RIGHT) for v in right_values])
        
        left_bars.arrange(RIGHT, buff=0.2)
        right_bars.arrange(RIGHT, buff=0.2)
        
        left_bars.move_to(LEFT * 2.5 + UP * 1)
        right_bars.move_to(RIGHT * 2.5 + UP * 1)
        
        # Labels
        left_label = Text("Left", font_size=SMALL_SIZE, color=SUBARRAY_LEFT)
        right_label = Text("Right", font_size=SMALL_SIZE, color=SUBARRAY_RIGHT)
        left_label.next_to(left_bars, UP, buff=0.4)
        right_label.next_to(right_bars, UP, buff=0.4)
        
        self.play(
            FadeIn(left_bars), FadeIn(right_bars),
            Write(left_label), Write(right_label),
            run_time=DURATION_NORMAL
        )
        
        # Create output container (temporary storage - purple)
        output_container = RoundedRectangle(
            width=4.5,
            height=1.8,
            corner_radius=0.15,
            fill_color=TEMPORARY_STORAGE,
            fill_opacity=0.15,
            stroke_color=TEMPORARY_STORAGE,
            stroke_width=2
        )
        output_container.move_to(DOWN * 1.8)
        
        output_label = Text("Merged Output", font_size=SMALL_SIZE, color=TEMPORARY_STORAGE)
        output_label.next_to(output_container, UP, buff=0.2)
        
        self.play(
            Create(output_container),
            Write(output_label),
            run_time=DURATION_NORMAL
        )
        
        # Pointers
        left_ptr = self._create_pointer("↓", SUBARRAY_LEFT)
        right_ptr = self._create_pointer("↓", SUBARRAY_RIGHT)
        
        left_ptr.next_to(left_bars[0], DOWN, buff=0.2)
        right_ptr.next_to(right_bars[0], DOWN, buff=0.2)
        
        self.play(FadeIn(left_ptr), FadeIn(right_ptr), run_time=DURATION_FAST)
        
        # Merge process
        output_bars = VGroup()
        left_idx = 0
        right_idx = 0
        output_positions = [
            output_container.get_left() + RIGHT * 0.8,
            output_container.get_left() + RIGHT * 1.6,
            output_container.get_left() + RIGHT * 2.4,
            output_container.get_left() + RIGHT * 3.2,
        ]
        output_idx = 0
        
        merge_order = [(0, 'left'), (1, 'right'), (0, 'left'), (1, 'right')]  # 2, 4, 7, 9
        
        for step_idx, (arr_idx, source) in enumerate(merge_order):
            if source == 'left':
                # Highlight comparison
                self.play(
                    left_bars[left_idx][0].animate.set_fill(ACTIVE_COMPARISON).set_stroke(ACTIVE_COMPARISON),
                    run_time=DURATION_FAST
                )
                
                # Move to output
                bar_copy = self._create_bar(left_values[left_idx], CORRECTLY_PLACED)
                bar_copy.move_to(output_positions[output_idx])
                
                self.play(
                    Transform(left_bars[left_idx].copy(), bar_copy),
                    left_bars[left_idx].animate.set_opacity(0.3),
                    run_time=DURATION_NORMAL
                )
                
                output_bars.add(bar_copy)
                self.add(bar_copy)
                
                left_idx += 1
                if left_idx < len(left_bars):
                    left_ptr.generate_target()
                    left_ptr.target.next_to(left_bars[left_idx], DOWN, buff=0.2)
                    self.play(MoveToTarget(left_ptr), run_time=DURATION_FAST)
                else:
                    self.play(FadeOut(left_ptr), run_time=DURATION_FAST)
            else:
                # Highlight comparison
                self.play(
                    right_bars[right_idx][0].animate.set_fill(ACTIVE_COMPARISON).set_stroke(ACTIVE_COMPARISON),
                    run_time=DURATION_FAST
                )
                
                # Move to output
                bar_copy = self._create_bar(right_values[right_idx], CORRECTLY_PLACED)
                bar_copy.move_to(output_positions[output_idx])
                
                self.play(
                    Transform(right_bars[right_idx].copy(), bar_copy),
                    right_bars[right_idx].animate.set_opacity(0.3),
                    run_time=DURATION_NORMAL
                )
                
                output_bars.add(bar_copy)
                self.add(bar_copy)
                
                right_idx += 1
                if right_idx < len(right_bars):
                    right_ptr.generate_target()
                    right_ptr.target.next_to(right_bars[right_idx], DOWN, buff=0.2)
                    self.play(MoveToTarget(right_ptr), run_time=DURATION_FAST)
                else:
                    self.play(FadeOut(right_ptr), run_time=DURATION_FAST)
            
            output_idx += 1
            self.wait(PAUSE_SHORT)
        
        # Final highlight
        self.play(
            output_container.animate.set_stroke(CORRECTLY_PLACED),
            output_label.animate.set_color(CORRECTLY_PLACED),
            run_time=DURATION_NORMAL
        )
        
        # Show result
        result_text = Text("[2, 4, 7, 9]", font_size=BODY_SIZE, color=CORRECTLY_PLACED)
        result_text.next_to(output_container, DOWN, buff=0.4)
        
        self.play(Write(result_text), run_time=DURATION_FAST)
    
    def _create_pointer(self, symbol, color):
        """Create a simple pointer."""
        return Text(symbol, font_size=LABEL_SIZE, color=color)
