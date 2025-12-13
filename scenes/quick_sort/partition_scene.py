"""
Quick Sort Partition Scene.
R2 compliant: One concept - partition mechanism.
R7 compliant: Uses states from algorithm module.
"""
from manim import (
    Scene, Text, VGroup, Rectangle, Triangle,
    FadeIn, FadeOut, Write, Create, Transform,
    UP, DOWN, LEFT, RIGHT, ORIGIN,
    LaggedStart, AnimationGroup, MoveToTarget,
    PI
)
import sys
sys.path.insert(0, '/home/hg/Desktop/algorthims/quickSortVsMergeSort')

from config.colors import (
    BACKGROUND_COLOR, TEXT_PRIMARY, TEXT_SECONDARY,
    UNPROCESSED, PIVOT, CORRECTLY_PLACED, ACTIVE_COMPARISON
)
from config.fonts import HEADING_SIZE, BODY_SIZE, LABEL_SIZE, SMALL_SIZE
from config.animation_constants import (
    DURATION_FAST, DURATION_NORMAL, DURATION_SLOW,
    PAUSE_SHORT, PAUSE_NORMAL, EASE_DEFAULT,
    BAR_WIDTH, BAR_HEIGHT_SCALE
)
from algorithms.quick_sort import quick_sort_with_steps, QuickSortStepType


class QuickSortPartitionScene(Scene):
    """
    Scene 4: Quick Sort Step-by-Step Partition.
    Concept: Detailed partition mechanism with pointers.
    """
    
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        
        # Title
        title = Text(
            "Partition Step",
            font_size=HEADING_SIZE,
            color=TEXT_PRIMARY
        )
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=DURATION_NORMAL)
        
        # Initial array
        self.values = [7, 2, 9, 4, 3, 8, 5]
        self.bars = self._create_array_bars(self.values)
        self.bars.next_to(title, DOWN, buff=1.0)
        
        self.play(
            LaggedStart(
                *[FadeIn(bar, shift=UP * 0.3) for bar in self.bars],
                lag_ratio=0.1
            ),
            run_time=DURATION_NORMAL
        )
        
        # Create pointers
        self.i_pointer = self._create_pointer("i", ACTIVE_COMPARISON)
        self.j_pointer = self._create_pointer("j", TEXT_SECONDARY)
        
        # Run partition animation
        self._animate_partition()
        
        self.wait(PAUSE_NORMAL)
    
    def _create_array_bars(self, values):
        """Create array bar visualization with labels."""
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
    
    def _create_pointer(self, label_text, color):
        """Create a pointer indicator."""
        pointer = VGroup()
        
        triangle = Triangle(
            fill_color=color,
            fill_opacity=1.0,
            stroke_width=0
        )
        triangle.scale(0.15)
        triangle.rotate(-PI / 2)
        
        label = Text(label_text, font_size=SMALL_SIZE, color=color)
        label.next_to(triangle, DOWN, buff=0.1)
        
        pointer.add(triangle, label)
        return pointer
    
    def _animate_partition(self):
        """Animate the partition process step by step."""
        # Highlight pivot (last element)
        pivot_idx = len(self.values) - 1
        pivot_bar = self.bars[pivot_idx][0]
        pivot_val = self.values[pivot_idx]
        
        pivot_label = Text("pivot", font_size=SMALL_SIZE, color=PIVOT)
        pivot_label.next_to(self.bars[pivot_idx], UP, buff=0.5)
        
        self.play(
            pivot_bar.animate.set_fill(PIVOT).set_stroke(PIVOT),
            FadeIn(pivot_label),
            run_time=DURATION_NORMAL
        )
        
        # Initialize pointers
        # i starts at -1 (before array), j starts at 0
        i = -1
        
        # Position j pointer at first element
        self.j_pointer.next_to(self.bars[0], DOWN, buff=0.3)
        self.play(FadeIn(self.j_pointer), run_time=DURATION_FAST)
        
        # Process each element
        for j in range(len(self.values) - 1):
            current_val = self.values[j]
            current_bar = self.bars[j][0]
            
            # Move j pointer
            if j > 0:
                self.j_pointer.generate_target()
                self.j_pointer.target.next_to(self.bars[j], DOWN, buff=0.3)
                self.play(MoveToTarget(self.j_pointer), run_time=DURATION_FAST)
            
            # Highlight comparison
            self.play(
                current_bar.animate.set_fill(ACTIVE_COMPARISON).set_stroke(ACTIVE_COMPARISON),
                run_time=DURATION_FAST
            )
            self.wait(PAUSE_SHORT)
            
            if current_val <= pivot_val:
                i += 1
                
                # Show/move i pointer
                if i == 0:
                    self.i_pointer.next_to(self.bars[0], DOWN, buff=0.6)
                    self.play(FadeIn(self.i_pointer), run_time=DURATION_FAST)
                elif i != j:
                    self.i_pointer.generate_target()
                    self.i_pointer.target.next_to(self.bars[i], DOWN, buff=0.6)
                    self.play(MoveToTarget(self.i_pointer), run_time=DURATION_FAST)
                
                # Swap if needed
                if i != j:
                    self._animate_swap(i, j)
                else:
                    # Just mark as processed (less than pivot)
                    self.play(
                        current_bar.animate.set_fill(UNPROCESSED).set_stroke(UNPROCESSED),
                        run_time=DURATION_FAST
                    )
            else:
                # Greater than pivot - reset color
                self.play(
                    current_bar.animate.set_fill(UNPROCESSED).set_stroke(UNPROCESSED),
                    run_time=DURATION_FAST
                )
        
        # Place pivot in correct position
        final_pos = i + 1
        if final_pos != pivot_idx:
            self._animate_swap(final_pos, pivot_idx)
        
        # Mark pivot as correctly placed
        self.play(
            self.bars[final_pos][0].animate.set_fill(CORRECTLY_PLACED).set_stroke(CORRECTLY_PLACED),
            run_time=DURATION_NORMAL
        )
        
        # Fade out pointers and pivot label
        self.play(
            FadeOut(self.i_pointer),
            FadeOut(self.j_pointer),
            FadeOut(pivot_label),
            run_time=DURATION_FAST
        )
    
    def _animate_swap(self, i, j):
        """Animate swapping two elements."""
        bar_i = self.bars[i]
        bar_j = self.bars[j]
        
        pos_i = bar_i.get_center()
        pos_j = bar_j.get_center()
        
        # Swap animation with arc
        bar_i.generate_target()
        bar_j.generate_target()
        
        bar_i.target.move_to(pos_j)
        bar_j.target.move_to(pos_i)
        
        self.play(
            MoveToTarget(bar_i, path_arc=PI/3),
            MoveToTarget(bar_j, path_arc=-PI/3),
            run_time=DURATION_NORMAL
        )
        
        # Update internal tracking
        self.bars[i], self.bars[j] = self.bars[j], self.bars[i]
        self.values[i], self.values[j] = self.values[j], self.values[i]
