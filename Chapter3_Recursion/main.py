#!/usr/bin/env python3
"""
Chapter 3: Recursion
====================
Educational animation demonstrating recursion and the call stack.
3Blue1Brown-style with smooth motion, clear visuals, and minimal text.

Usage:
    manim -pql main.py Chapter3Animation    # Preview (480p)
    manim -pqh main.py Chapter3Animation    # HD quality (1080p)
    
Individual scenes:
    manim -pql main.py IntroScene
    manim -pql main.py BaseCaseScene
    manim -pql main.py CallStackScene
    manim -pql main.py FactorialScene
    manim -pql main.py ComparisonScene
    manim -pql main.py SummaryScene
"""
import sys
sys.path.insert(0, '/home/hg/Desktop/algorthims/Chapter3_Recursion')

from manim import *

# Import configurations
from config.colors import (
    BACKGROUND_COLOR, TEXT_PRIMARY, TEXT_SECONDARY, TEXT_ACCENT,
    UNPROCESSED, ACTIVE, COMPLETED, HIGHLIGHT,
    BASE_CASE, RECURSIVE_CASE, STACK_FRAME, STACK_ACTIVE, RETURN_VALUE,
    BOX_OUTER, BOX_INNER, KEY_FOUND,
    STACK_PUSH, STACK_POP, STACK_BASE,
    ITERATIVE_COLOR, RECURSIVE_COLOR
)
from config.fonts import (
    TITLE_SIZE, SUBTITLE_SIZE, HEADING_SIZE, BODY_SIZE,
    LABEL_SIZE, SMALL_SIZE, TINY_SIZE
)
from config.animation_constants import (
    INSTANT, FAST, NORMAL, SLOW, PAUSE, LONG_PAUSE,
    TITLE_Y, CONTENT_TOP, CONTENT_MID, CONTENT_BOT,
    STACK_FRAME_HEIGHT, STACK_FRAME_WIDTH
)


class Chapter3Animation(Scene):
    """
    Complete Chapter 3 animation covering:
    1. Introduction to Recursion (nested boxes metaphor)
    2. Base Case vs Recursive Case (countdown example)
    3. The Call Stack (push/pop visualization)
    4. Factorial with Stack Frames
    5. Recursion vs Iteration Comparison
    6. Summary and Key Takeaways
    """
    
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        
        # Scene 1: Introduction
        self._intro_scene()
        self._clear()
        
        # Scene 2: Base Case vs Recursive Case
        self._base_case_scene()
        self._clear()
        
        # Scene 3: Call Stack
        self._call_stack_scene()
        self._clear()
        
        # Scene 4: Factorial Example
        self._factorial_scene()
        self._clear()
        
        # Scene 5: Recursion vs Iteration
        self._comparison_scene()
        self._clear()
        
        # Scene 6: Summary
        self._summary_scene()
    
    def _clear(self):
        """Clear scene with fade transition."""
        if self.mobjects:
            self.play(*[FadeOut(m) for m in self.mobjects], run_time=FAST)
        self.wait(0.2)
    
    # ==================== HELPER METHODS ====================
    
    def _title(self, text, y=TITLE_Y):
        """Create title at top."""
        t = Text(text, font_size=HEADING_SIZE, color=TEXT_PRIMARY)
        t.move_to(UP * y)
        return t
    
    def _stack_frame(self, func_name, params="", color=STACK_FRAME, width=3.0, height=0.65):
        """Create a stack frame."""
        grp = VGroup()
        
        box = Rectangle(
            width=width, height=height,
            fill_color=color, fill_opacity=0.85,
            stroke_color=TEXT_PRIMARY, stroke_width=2
        )
        
        if params:
            text = Text(f"{func_name}({params})", font_size=SMALL_SIZE, color=TEXT_PRIMARY)
        else:
            text = Text(func_name, font_size=SMALL_SIZE, color=TEXT_PRIMARY)
        text.move_to(box.get_center())
        
        grp.add(box, text)
        grp.box = box
        grp.text = text
        return grp
    
    def _box(self, size=1.0, color=BOX_OUTER, label=""):
        """Create a box for the nested boxes metaphor."""
        grp = VGroup()
        
        rect = RoundedRectangle(
            width=size, height=size,
            corner_radius=0.08,
            fill_color=color, fill_opacity=0.7,
            stroke_color=TEXT_PRIMARY, stroke_width=2
        )
        
        grp.add(rect)
        grp.rect = rect
        
        if label:
            lbl = Text(label, font_size=int(SMALL_SIZE * (size / 1.2)), color=TEXT_PRIMARY)
            lbl.move_to(rect.get_center())
            grp.add(lbl)
        
        return grp
    
    # ==================== SCENE 1: INTRODUCTION ====================
    
    def _intro_scene(self):
        """Introduction to recursion with nested boxes metaphor."""
        # Main title
        title = Text("Chapter 3: Recursion", font_size=TITLE_SIZE, color=TEXT_PRIMARY)
        title.move_to(UP * 2)
        
        self.play(Write(title), run_time=SLOW)
        self.wait(PAUSE)
        
        # Subtitle
        subtitle = Text("A function that calls itself", font_size=SUBTITLE_SIZE, color=TEXT_ACCENT)
        subtitle.next_to(title, DOWN, buff=0.5)
        
        self.play(FadeIn(subtitle, shift=UP * 0.3), run_time=NORMAL)
        self.wait(PAUSE)
        
        # Move title up
        self.play(
            title.animate.scale(0.7).move_to(UP * 3.2),
            FadeOut(subtitle),
            run_time=NORMAL
        )
        
        # Nested boxes metaphor
        metaphor_title = Text("Metaphor: Grandma's Boxes", font_size=BODY_SIZE, color=TEXT_SECONDARY)
        metaphor_title.move_to(UP * 2.2)
        self.play(Write(metaphor_title), run_time=FAST)
        
        # Create nested boxes
        box1 = self._box(2.5, BOX_OUTER, "Box 1")
        box2 = self._box(1.8, BOX_INNER, "Box 2")
        box3 = self._box(1.2, "#818CF8", "Box 3")
        key_box = self._box(0.7, KEY_FOUND)
        
        # Add key emoji
        key = Text("🔑", font_size=24)
        key.move_to(key_box.get_center())
        key_box.add(key)
        
        boxes = VGroup(box1, box2, box3, key_box)
        boxes.move_to(UP * 0.3)
        
        # Show outer box first
        self.play(FadeIn(box1), run_time=NORMAL)
        self.wait(0.3)
        
        # Open and show inner boxes
        self.play(box1.animate.set_opacity(0.3), run_time=FAST)
        self.play(FadeIn(box2), run_time=FAST)
        self.wait(0.3)
        
        self.play(box2.animate.set_opacity(0.3), run_time=FAST)
        self.play(FadeIn(box3), run_time=FAST)
        self.wait(0.3)
        
        self.play(box3.animate.set_opacity(0.3), run_time=FAST)
        self.play(FadeIn(key_box), run_time=FAST)
        
        # Found the key!
        found_text = Text("Found the key!", font_size=BODY_SIZE, color=KEY_FOUND)
        found_text.move_to(DOWN * 1.5)
        self.play(Write(found_text), run_time=FAST)
        self.wait(PAUSE)
        
        # Explanation
        explanation = Text("Each box may contain another box or the key", 
                          font_size=SMALL_SIZE, color=TEXT_SECONDARY)
        explanation.move_to(DOWN * 2.3)
        self.play(Write(explanation), run_time=FAST)
        
        recursion_analogy = Text("Recursion: each call may make another call or return", 
                                font_size=SMALL_SIZE, color=RECURSIVE_COLOR)
        recursion_analogy.move_to(DOWN * 2.9)
        self.play(Write(recursion_analogy), run_time=NORMAL)
        self.wait(LONG_PAUSE)
    
    # ==================== SCENE 2: BASE CASE VS RECURSIVE CASE ====================
    
    def _base_case_scene(self):
        """Demonstrate base case vs recursive case with countdown."""
        # Title
        title = self._title("Base Case vs Recursive Case")
        self.play(Write(title), run_time=NORMAL)
        
        # Concept
        concept = Text("Every recursion needs a stopping condition", 
                      font_size=BODY_SIZE, color=TEXT_SECONDARY)
        concept.move_to(UP * 2.2)
        self.play(Write(concept), run_time=FAST)
        
        # Show countdown code structure
        code_title = Text("countdown(n):", font_size=LABEL_SIZE, color=TEXT_PRIMARY)
        code_title.move_to(UP * 1.2 + LEFT * 3)
        
        base_code = Text("if n <= 0: return", font_size=SMALL_SIZE, color=BASE_CASE)
        base_code.next_to(code_title, DOWN, buff=0.2, aligned_edge=LEFT)
        base_label = Text("← Base Case", font_size=SMALL_SIZE, color=BASE_CASE)
        base_label.next_to(base_code, RIGHT, buff=0.3)
        
        rec_code = Text("countdown(n - 1)", font_size=SMALL_SIZE, color=RECURSIVE_CASE)
        rec_code.next_to(base_code, DOWN, buff=0.2, aligned_edge=LEFT)
        rec_label = Text("← Recursive Case", font_size=SMALL_SIZE, color=RECURSIVE_CASE)
        rec_label.next_to(rec_code, RIGHT, buff=0.3)
        
        self.play(Write(code_title), run_time=FAST)
        self.play(Write(base_code), Write(base_label), run_time=FAST)
        self.play(Write(rec_code), Write(rec_label), run_time=FAST)
        self.wait(PAUSE)
        
        # Countdown visualization
        countdown_title = Text("countdown(3)", font_size=LABEL_SIZE, color=TEXT_ACCENT)
        countdown_title.move_to(RIGHT * 3 + UP * 1.2)
        self.play(Write(countdown_title), run_time=FAST)
        
        # Stack position
        stack_base = DOWN * 2 + RIGHT * 3
        
        # Animate countdown: 3 -> 2 -> 1 -> 0 (base)
        frames = []
        values = [3, 2, 1, 0]
        
        for i, val in enumerate(values):
            # Create frame
            is_base = (val <= 0)
            color = BASE_CASE if is_base else RECURSIVE_CASE
            frame = self._stack_frame(f"countdown", f"n={val}", color)
            frame.move_to(stack_base + UP * (i * 0.75 + 0.4))
            frames.append(frame)
            
            # Push animation
            self.play(FadeIn(frame, shift=UP * 0.3), run_time=FAST)
            
            if is_base:
                # Base case reached
                base_reached = Text("Base case! Stop.", font_size=SMALL_SIZE, color=BASE_CASE)
                base_reached.next_to(frame, RIGHT, buff=0.3)
                self.play(Write(base_reached), run_time=FAST)
                self.wait(PAUSE)
                
                # Pop all frames
                self.play(FadeOut(base_reached), run_time=FAST)
                break
        
        # Pop frames (unwind)
        self.wait(0.3)
        pop_label = Text("Unwinding...", font_size=SMALL_SIZE, color=RETURN_VALUE)
        pop_label.move_to(stack_base + RIGHT * 2.5)
        self.play(Write(pop_label), run_time=FAST)
        
        for frame in reversed(frames):
            self.play(
                frame.animate.shift(RIGHT * 0.5).set_opacity(0),
                run_time=FAST
            )
        
        self.play(FadeOut(pop_label), run_time=FAST)
        
        # Key insight
        insight = VGroup(
            Text("Base case", font_size=LABEL_SIZE, color=BASE_CASE),
            Text(" stops recursion, ", font_size=LABEL_SIZE, color=TEXT_PRIMARY),
            Text("Recursive case", font_size=LABEL_SIZE, color=RECURSIVE_CASE),
            Text(" continues it", font_size=LABEL_SIZE, color=TEXT_PRIMARY)
        )
        insight.arrange(RIGHT, buff=0.1)
        insight.move_to(DOWN * 3)
        self.play(Write(insight), run_time=NORMAL)
        self.wait(LONG_PAUSE)
    
    # ==================== SCENE 3: CALL STACK ====================
    
    def _call_stack_scene(self):
        """Demonstrate the call stack with push/pop operations."""
        # Title
        title = self._title("The Call Stack")
        self.play(Write(title), run_time=NORMAL)
        
        # Concept
        concept = Text("Stack of function calls - Last In, First Out (LIFO)", 
                      font_size=BODY_SIZE, color=TEXT_SECONDARY)
        concept.move_to(UP * 2.2)
        self.play(Write(concept), run_time=FAST)
        
        # Stack base
        stack_base = DOWN * 2.5
        base_line = Line(
            stack_base + LEFT * 1.8,
            stack_base + RIGHT * 1.8,
            color=TEXT_PRIMARY, stroke_width=3
        )
        stack_label = Text("Stack", font_size=SMALL_SIZE, color=TEXT_SECONDARY)
        stack_label.next_to(base_line, DOWN, buff=0.15)
        
        self.play(Create(base_line), Write(stack_label), run_time=FAST)
        
        # Demonstrate with greet example
        example_title = Text("Example: greet('Alice')", font_size=LABEL_SIZE, color=TEXT_ACCENT)
        example_title.move_to(UP * 1.2 + LEFT * 3.5)
        self.play(Write(example_title), run_time=FAST)
        
        # Code visualization
        code = VGroup(
            Text("def greet(name):", font_size=TINY_SIZE, color=TEXT_PRIMARY),
            Text("    print('Hello')", font_size=TINY_SIZE, color=TEXT_SECONDARY),
            Text("    greet2(name)", font_size=TINY_SIZE, color=RECURSIVE_CASE),
            Text("    print('Done')", font_size=TINY_SIZE, color=TEXT_SECONDARY),
        )
        code.arrange(DOWN, buff=0.1, aligned_edge=LEFT)
        code.move_to(LEFT * 4 + DOWN * 0.5)
        self.play(Write(code), run_time=FAST)
        
        # Push frames
        frames = []
        frame_data = [
            ("main", "", STACK_FRAME),
            ("greet", "Alice", STACK_ACTIVE),
            ("greet2", "Alice", "#EC4899"),
        ]
        
        for i, (name, params, color) in enumerate(frame_data):
            frame = self._stack_frame(name, params, color)
            frame.move_to(stack_base + UP * (i * 0.75 + 0.4))
            frames.append(frame)
            
            # Push animation
            push_label = Text("PUSH", font_size=TINY_SIZE, color=STACK_PUSH)
            push_label.next_to(frame, RIGHT, buff=0.5)
            
            self.play(
                FadeIn(frame, shift=UP * 0.3),
                FadeIn(push_label),
                run_time=FAST
            )
            self.play(FadeOut(push_label), run_time=INSTANT)
            self.wait(0.3)
        
        self.wait(PAUSE)
        
        # Pop frames
        for frame in reversed(frames):
            pop_label = Text("POP", font_size=TINY_SIZE, color=STACK_POP)
            pop_label.next_to(frame, RIGHT, buff=0.5)
            
            self.play(FadeIn(pop_label), run_time=INSTANT)
            self.play(
                FadeOut(frame, shift=UP * 0.3),
                FadeOut(pop_label),
                run_time=FAST
            )
            self.wait(0.2)
        
        # Memory note
        memory_note = Text("Each frame uses memory until it returns!", 
                          font_size=LABEL_SIZE, color=HIGHLIGHT)
        memory_note.move_to(DOWN * 3)
        self.play(Write(memory_note), run_time=NORMAL)
        self.wait(LONG_PAUSE)
    
    # ==================== SCENE 4: FACTORIAL ====================
    
    def _factorial_scene(self):
        """Demonstrate factorial recursion with stack frames."""
        # Title
        title = self._title("Factorial: factorial(5)")
        self.play(Write(title), run_time=NORMAL)
        
        # Formula
        formula = Text("n! = n × (n-1) × ... × 1", font_size=BODY_SIZE, color=TEXT_SECONDARY)
        formula.move_to(UP * 2.2)
        self.play(Write(formula), run_time=FAST)
        
        # Code
        code = VGroup(
            Text("def factorial(n):", font_size=SMALL_SIZE, color=TEXT_PRIMARY),
            Text("    if n == 1: return 1", font_size=SMALL_SIZE, color=BASE_CASE),
            Text("    return n * factorial(n-1)", font_size=SMALL_SIZE, color=RECURSIVE_CASE),
        )
        code.arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        code.move_to(LEFT * 4 + UP * 0.8)
        self.play(Write(code), run_time=FAST)
        
        # Stack
        stack_base = DOWN * 2.5 + RIGHT * 2
        base_line = Line(
            stack_base + LEFT * 1.8,
            stack_base + RIGHT * 1.8,
            color=TEXT_PRIMARY, stroke_width=3
        )
        self.play(Create(base_line), run_time=FAST)
        
        # Build stack frames for factorial(5)
        frames = []
        values = [5, 4, 3, 2, 1]
        
        for i, n in enumerate(values):
            is_base = (n == 1)
            color = BASE_CASE if is_base else STACK_FRAME
            frame = self._stack_frame(f"fact", f"n={n}", color)
            frame.move_to(stack_base + UP * (i * 0.65 + 0.35))
            frames.append(frame)
            
            self.play(FadeIn(frame, shift=UP * 0.2), run_time=FAST)
            
            if is_base:
                # Show base case return
                ret_label = Text("returns 1", font_size=TINY_SIZE, color=BASE_CASE)
                ret_label.next_to(frame, RIGHT, buff=0.3)
                self.play(Write(ret_label), run_time=FAST)
                self.wait(PAUSE)
                self.play(FadeOut(ret_label), run_time=FAST)
        
        self.wait(PAUSE)
        
        # Unwind with computed values
        results = [1, 2, 6, 24, 120]  # 1!, 2!, 3!, 4!, 5!
        multipliers = [1, 2, 3, 4, 5]
        
        for i, (frame, result, mult) in enumerate(zip(reversed(frames), results, multipliers)):
            if i == 0:
                ret_text = f"= 1"
            else:
                prev = results[i-1]
                ret_text = f"= {mult} × {prev} = {result}"
            
            ret_label = Text(ret_text, font_size=TINY_SIZE, color=RETURN_VALUE)
            ret_label.next_to(frame, RIGHT, buff=0.3)
            
            self.play(
                frame.box.animate.set_fill(RETURN_VALUE),
                Write(ret_label),
                run_time=FAST
            )
            self.wait(0.3)
            
            self.play(
                FadeOut(frame, shift=RIGHT * 0.5),
                FadeOut(ret_label),
                run_time=FAST
            )
        
        # Final result
        final = Text("factorial(5) = 120", font_size=HEADING_SIZE, color=COMPLETED)
        final.move_to(RIGHT * 2)
        self.play(Write(final), run_time=NORMAL)
        self.wait(LONG_PAUSE)
    
    # ==================== SCENE 5: RECURSION VS ITERATION ====================
    
    def _comparison_scene(self):
        """Compare recursive and iterative approaches."""
        # Title
        title = self._title("Recursion vs Iteration")
        self.play(Write(title), run_time=NORMAL)
        
        # Divider
        divider = DashedLine(UP * 2.5, DOWN * 3, color=TEXT_SECONDARY, stroke_width=1.5)
        self.play(Create(divider), run_time=FAST)
        
        # Headers
        rec_head = Text("Recursion", font_size=BODY_SIZE, color=RECURSIVE_COLOR)
        iter_head = Text("Iteration", font_size=BODY_SIZE, color=ITERATIVE_COLOR)
        rec_head.move_to(LEFT * 3.5 + UP * 2.2)
        iter_head.move_to(RIGHT * 3.5 + UP * 2.2)
        
        self.play(Write(rec_head), Write(iter_head), run_time=FAST)
        
        # Code examples
        rec_code = VGroup(
            Text("def sum(arr):", font_size=TINY_SIZE, color=TEXT_PRIMARY),
            Text("  if len(arr)==0:", font_size=TINY_SIZE, color=BASE_CASE),
            Text("    return 0", font_size=TINY_SIZE, color=BASE_CASE),
            Text("  return arr[0] +", font_size=TINY_SIZE, color=RECURSIVE_COLOR),
            Text("    sum(arr[1:])", font_size=TINY_SIZE, color=RECURSIVE_COLOR),
        )
        rec_code.arrange(DOWN, buff=0.08, aligned_edge=LEFT)
        rec_code.move_to(LEFT * 3.5 + UP * 0.8)
        
        iter_code = VGroup(
            Text("def sum(arr):", font_size=TINY_SIZE, color=TEXT_PRIMARY),
            Text("  total = 0", font_size=TINY_SIZE, color=ITERATIVE_COLOR),
            Text("  for x in arr:", font_size=TINY_SIZE, color=ITERATIVE_COLOR),
            Text("    total += x", font_size=TINY_SIZE, color=ITERATIVE_COLOR),
            Text("  return total", font_size=TINY_SIZE, color=TEXT_PRIMARY),
        )
        iter_code.arrange(DOWN, buff=0.08, aligned_edge=LEFT)
        iter_code.move_to(RIGHT * 3.5 + UP * 0.8)
        
        self.play(Write(rec_code), Write(iter_code), run_time=NORMAL)
        self.wait(PAUSE)
        
        # Characteristics comparison
        rec_traits = VGroup(
            Text("✓ Elegant, clear", font_size=SMALL_SIZE, color=COMPLETED),
            Text("✗ Uses stack memory", font_size=SMALL_SIZE, color=ACTIVE),
            Text("✗ Can overflow", font_size=SMALL_SIZE, color=ACTIVE),
        )
        rec_traits.arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        rec_traits.move_to(LEFT * 3.5 + DOWN * 1.2)
        
        iter_traits = VGroup(
            Text("✓ Memory efficient", font_size=SMALL_SIZE, color=COMPLETED),
            Text("✓ No overflow risk", font_size=SMALL_SIZE, color=COMPLETED),
            Text("✗ Can be verbose", font_size=SMALL_SIZE, color=ACTIVE),
        )
        iter_traits.arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        iter_traits.move_to(RIGHT * 3.5 + DOWN * 1.2)
        
        self.play(
            LaggedStart(*[Write(t) for t in rec_traits], lag_ratio=0.2),
            LaggedStart(*[Write(t) for t in iter_traits], lag_ratio=0.2),
            run_time=SLOW
        )
        self.wait(PAUSE)
        
        # Key insight
        insight = Text("No performance benefit - choose for clarity!", 
                      font_size=BODY_SIZE, color=TEXT_ACCENT)
        insight.move_to(DOWN * 2.8)
        self.play(Write(insight), run_time=NORMAL)
        self.wait(LONG_PAUSE)
    
    # ==================== SCENE 6: SUMMARY ====================
    
    def _summary_scene(self):
        """Final summary and key takeaways."""
        # Title
        title = self._title("Key Takeaways")
        self.play(Write(title), run_time=NORMAL)
        
        # Takeaways
        takeaways = [
            ("1.", "Recursion = function calling itself", RECURSIVE_COLOR),
            ("2.", "Base case stops, recursive case continues", TEXT_ACCENT),
            ("3.", "Call stack tracks function calls (LIFO)", STACK_FRAME),
            ("4.", "Each call uses memory - stack can grow large", HIGHLIGHT),
            ("5.", "Choose recursion for clarity, loops for performance", TEXT_PRIMARY),
        ]
        
        items = VGroup()
        for num, text, color in takeaways:
            num_text = Text(num, font_size=BODY_SIZE, color=TEXT_PRIMARY)
            content = Text(text, font_size=LABEL_SIZE, color=color)
            content.next_to(num_text, RIGHT, buff=0.2)
            row = VGroup(num_text, content)
            items.add(row)
        
        items.arrange(DOWN, buff=0.35, aligned_edge=LEFT)
        items.move_to(UP * 0.3)
        
        self.play(
            LaggedStart(*[FadeIn(item, shift=LEFT * 0.3) for item in items], lag_ratio=0.2),
            run_time=SLOW
        )
        self.wait(PAUSE)
        
        # Visual summary
        summary_box = VGroup()
        
        box_label = Text("Remember:", font_size=BODY_SIZE, color=TEXT_PRIMARY)
        box_content = VGroup(
            Text("Base Case → STOP", font_size=LABEL_SIZE, color=BASE_CASE),
            Text("Recursive Case → CALL AGAIN", font_size=LABEL_SIZE, color=RECURSIVE_CASE),
        )
        box_content.arrange(DOWN, buff=0.2)
        
        summary_box.add(box_label, box_content)
        summary_box.arrange(DOWN, buff=0.3)
        summary_box.move_to(DOWN * 2.3)
        
        self.play(
            Write(box_label),
            LaggedStart(*[Write(t) for t in box_content], lag_ratio=0.3),
            run_time=NORMAL
        )
        self.wait(LONG_PAUSE)


# Individual scene classes for separate rendering
class IntroScene(Scene):
    """Introduction scene only."""
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        Chapter3Animation._intro_scene(self)


class BaseCaseScene(Scene):
    """Base case scene only."""
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        Chapter3Animation._base_case_scene(self)


class CallStackScene(Scene):
    """Call stack scene only."""
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        Chapter3Animation._call_stack_scene(self)


class FactorialScene(Scene):
    """Factorial scene only."""
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        Chapter3Animation._factorial_scene(self)


class ComparisonScene(Scene):
    """Comparison scene only."""
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        Chapter3Animation._comparison_scene(self)


class SummaryScene(Scene):
    """Summary scene only."""
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        Chapter3Animation._summary_scene(self)
