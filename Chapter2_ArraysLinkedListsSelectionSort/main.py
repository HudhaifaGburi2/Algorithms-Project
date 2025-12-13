#!/usr/bin/env python3
"""
Chapter 2: Arrays, Linked Lists, and Selection Sort
====================================================
Educational animation demonstrating data structures and sorting.
3Blue1Brown-style with smooth motion, clear visuals, and minimal text.

Usage:
    manim -pql main.py Chapter2Animation    # Preview (480p)
    manim -pqh main.py Chapter2Animation    # HD quality (1080p)
    
Individual scenes:
    manim -pql main.py IntroScene
    manim -pql main.py ArrayScene
    manim -pql main.py LinkedListScene
    manim -pql main.py ComparisonScene
    manim -pql main.py SelectionSortScene
    manim -pql main.py SummaryScene
"""
import sys
sys.path.insert(0, '/home/hg/Desktop/algorthims/Chapter2_ArraysLinkedListsSelectionSort')

from manim import *

# Import configurations
from config.colors import (
    BACKGROUND_COLOR, TEXT_PRIMARY, TEXT_SECONDARY, TEXT_ACCENT,
    UNPROCESSED, ACTIVE_COMPARISON, SORTED_ELEMENT, CURRENT_MIN, HIGHLIGHT,
    ARRAY_COLOR, LINKED_LIST_COLOR, POINTER_COLOR, MEMORY_BOX,
    MEMORY_CONTIGUOUS, MEMORY_SCATTERED,
    READ_OP, INSERT_OP, DELETE_OP,
    O_1, O_N, O_N_SQUARED
)
from config.fonts import (
    TITLE_SIZE, SUBTITLE_SIZE, HEADING_SIZE, BODY_SIZE,
    LABEL_SIZE, SMALL_SIZE, TINY_SIZE
)
from config.animation_constants import (
    INSTANT, FAST, NORMAL, SLOW, PAUSE, LONG_PAUSE,
    TITLE_Y, CONTENT_TOP, CONTENT_MID, CONTENT_BOT
)

# Demo data
DEMO_ARRAY = [64, 25, 12, 22, 11]


class Chapter2Animation(Scene):
    """
    Complete Chapter 2 animation covering:
    1. Introduction to Data Structures
    2. Arrays - memory layout and operations
    3. Linked Lists - nodes and pointers
    4. Comparison - Arrays vs Linked Lists
    5. Selection Sort demonstration
    6. Summary and key takeaways
    """
    
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        
        # Scene 1: Introduction
        self._intro_scene()
        self._clear()
        
        # Scene 2: Arrays
        self._array_scene()
        self._clear()
        
        # Scene 3: Linked Lists
        self._linked_list_scene()
        self._clear()
        
        # Scene 4: Comparison
        self._comparison_scene()
        self._clear()
        
        # Scene 5: Selection Sort
        self._selection_sort_scene()
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
    
    def _cell(self, value, color=UNPROCESSED, width=0.8, height=0.6, show_index=True, index=0):
        """Create memory cell."""
        grp = VGroup()
        
        rect = Rectangle(
            width=width, height=height,
            fill_color=color, fill_opacity=0.85,
            stroke_color=TEXT_PRIMARY, stroke_width=2
        )
        
        lbl = Text(str(value), font_size=int(LABEL_SIZE * 0.9), color=TEXT_PRIMARY)
        lbl.move_to(rect.get_center())
        
        grp.add(rect, lbl)
        grp.rect = rect
        grp.value = value
        
        if show_index:
            idx = Text(str(index), font_size=TINY_SIZE, color=TEXT_SECONDARY)
            idx.next_to(rect, DOWN, buff=0.1)
            grp.add(idx)
        
        return grp
    
    def _array(self, values, color=ARRAY_COLOR, spacing=0.0, show_indices=True):
        """Create array visualization."""
        arr = VGroup()
        cells = []
        
        for i, v in enumerate(values):
            cell = self._cell(v, color, show_index=show_indices, index=i)
            cells.append(cell)
            arr.add(cell)
        
        arr.arrange(RIGHT, buff=spacing)
        arr.cells = cells
        return arr
    
    def _node(self, value, color=LINKED_LIST_COLOR, width=1.2, height=0.6):
        """Create linked list node."""
        grp = VGroup()
        
        # Value box
        val_width = width * 0.65
        val_box = Rectangle(
            width=val_width, height=height,
            fill_color=color, fill_opacity=0.85,
            stroke_color=TEXT_PRIMARY, stroke_width=2
        )
        
        # Pointer box
        ptr_width = width * 0.35
        ptr_box = Rectangle(
            width=ptr_width, height=height,
            fill_color=MEMORY_BOX, fill_opacity=0.7,
            stroke_color=TEXT_PRIMARY, stroke_width=2
        )
        ptr_box.next_to(val_box, RIGHT, buff=0)
        
        # Value label
        lbl = Text(str(value), font_size=int(LABEL_SIZE * 0.85), color=TEXT_PRIMARY)
        lbl.move_to(val_box.get_center())
        
        # Pointer dot
        dot = Dot(color=POINTER_COLOR, radius=0.08)
        dot.move_to(ptr_box.get_center())
        
        grp.add(val_box, ptr_box, lbl, dot)
        grp.val_box = val_box
        grp.ptr_box = ptr_box
        grp.value = value
        
        return grp
    
    def _color_cell(self, cell, color):
        """Return animation for changing cell color."""
        return cell.rect.animate.set_fill(color)
    
    def _color_node(self, node, color):
        """Return animation for changing node color."""
        return node.val_box.animate.set_fill(color)
    
    # ==================== SCENE 1: INTRODUCTION ====================
    
    def _intro_scene(self):
        """Introduction to data structures."""
        # Main title
        title = Text("Chapter 2: Data Structures", font_size=TITLE_SIZE, color=TEXT_PRIMARY)
        title.move_to(UP * 2)
        
        self.play(Write(title), run_time=SLOW)
        self.wait(PAUSE)
        
        # Subtitle
        subtitle = Text("Arrays, Linked Lists & Selection Sort", 
                       font_size=SUBTITLE_SIZE, color=TEXT_ACCENT)
        subtitle.next_to(title, DOWN, buff=0.5)
        
        self.play(FadeIn(subtitle, shift=UP * 0.3), run_time=NORMAL)
        self.wait(PAUSE)
        
        # Move title up
        self.play(
            title.animate.scale(0.7).move_to(UP * 3.2),
            FadeOut(subtitle),
            run_time=NORMAL
        )
        
        # Memory metaphor
        memory_title = Text("Computer Memory: Like a Row of Drawers", 
                           font_size=BODY_SIZE, color=TEXT_SECONDARY)
        memory_title.move_to(UP * 2.2)
        self.play(Write(memory_title), run_time=NORMAL)
        
        # Draw memory boxes
        memory_boxes = VGroup()
        for i in range(10):
            box = Rectangle(
                width=0.7, height=0.7,
                fill_color=MEMORY_BOX, fill_opacity=0.6,
                stroke_color=TEXT_SECONDARY, stroke_width=1.5
            )
            addr = Text(f"{i}", font_size=TINY_SIZE, color=TEXT_SECONDARY)
            addr.next_to(box, DOWN, buff=0.08)
            memory_boxes.add(VGroup(box, addr))
        
        memory_boxes.arrange(RIGHT, buff=0.1)
        memory_boxes.move_to(UP * 0.5)
        
        self.play(
            LaggedStart(*[FadeIn(box, shift=UP * 0.2) for box in memory_boxes], lag_ratio=0.05),
            run_time=NORMAL
        )
        self.wait(PAUSE)
        
        # Two approaches labels
        question = Text("How do we store data?", font_size=BODY_SIZE, color=TEXT_PRIMARY)
        question.move_to(DOWN * 1)
        self.play(Write(question), run_time=FAST)
        
        array_label = Text("Arrays", font_size=LABEL_SIZE, color=ARRAY_COLOR)
        array_label.move_to(DOWN * 2 + LEFT * 2.5)
        
        list_label = Text("Linked Lists", font_size=LABEL_SIZE, color=LINKED_LIST_COLOR)
        list_label.move_to(DOWN * 2 + RIGHT * 2.5)
        
        self.play(Write(array_label), Write(list_label), run_time=NORMAL)
        
        # Descriptions
        array_desc = Text("Contiguous", font_size=SMALL_SIZE, color=ARRAY_COLOR)
        array_desc.next_to(array_label, DOWN, buff=0.2)
        
        list_desc = Text("Scattered", font_size=SMALL_SIZE, color=LINKED_LIST_COLOR)
        list_desc.next_to(list_label, DOWN, buff=0.2)
        
        self.play(Write(array_desc), Write(list_desc), run_time=FAST)
        self.wait(LONG_PAUSE)
    
    # ==================== SCENE 2: ARRAYS ====================
    
    def _array_scene(self):
        """Demonstrate arrays and their operations."""
        # Title
        title = self._title("Arrays: Contiguous Memory")
        self.play(Write(title), run_time=NORMAL)
        
        # Concept
        concept = Text("Elements stored next to each other in memory", 
                      font_size=BODY_SIZE, color=TEXT_SECONDARY)
        concept.move_to(UP * 2.2)
        self.play(Write(concept), run_time=FAST)
        
        # Create array
        arr = self._array([10, 20, 30, 40, 50], ARRAY_COLOR)
        arr.move_to(UP * 0.8)
        
        self.play(
            LaggedStart(*[FadeIn(cell, shift=UP * 0.2) for cell in arr.cells], lag_ratio=0.1),
            run_time=NORMAL
        )
        self.wait(PAUSE)
        
        # Show memory addresses
        addr_label = Text("Memory addresses:", font_size=SMALL_SIZE, color=TEXT_SECONDARY)
        addr_label.next_to(arr, LEFT, buff=0.5)
        self.play(Write(addr_label), run_time=FAST)
        
        addresses = VGroup()
        for i, cell in enumerate(arr.cells):
            addr = Text(f"0x{100 + i * 4:03X}", font_size=TINY_SIZE, color=MEMORY_CONTIGUOUS)
            addr.next_to(cell, UP, buff=0.15)
            addresses.add(addr)
        
        self.play(LaggedStart(*[Write(a) for a in addresses], lag_ratio=0.1), run_time=NORMAL)
        self.wait(PAUSE)
        
        # Demonstrate READ operation - O(1)
        self.play(FadeOut(addr_label), FadeOut(addresses), run_time=FAST)
        
        read_label = Text("Read by Index: O(1) - Instant!", font_size=BODY_SIZE, color=READ_OP)
        read_label.move_to(DOWN * 0.5)
        self.play(Write(read_label), run_time=FAST)
        
        # Highlight index 2
        pointer = Triangle(fill_color=POINTER_COLOR, fill_opacity=1, stroke_width=0)
        pointer.scale(0.12).rotate(PI)
        pointer.next_to(arr.cells[2], UP, buff=0.25)
        
        idx_text = Text("arr[2]", font_size=LABEL_SIZE, color=POINTER_COLOR)
        idx_text.next_to(pointer, UP, buff=0.1)
        
        self.play(FadeIn(pointer), Write(idx_text), run_time=FAST)
        self.play(self._color_cell(arr.cells[2], HIGHLIGHT), run_time=FAST)
        
        result = Text("= 30", font_size=LABEL_SIZE, color=READ_OP)
        result.next_to(idx_text, RIGHT, buff=0.2)
        self.play(Write(result), run_time=FAST)
        self.wait(PAUSE)
        
        # Clear and show INSERT
        self.play(
            FadeOut(pointer), FadeOut(idx_text), FadeOut(result), FadeOut(read_label),
            self._color_cell(arr.cells[2], ARRAY_COLOR),
            run_time=FAST
        )
        
        insert_label = Text("Insert at Start: O(n) - Must shift all!", font_size=BODY_SIZE, color=INSERT_OP)
        insert_label.move_to(DOWN * 0.5)
        self.play(Write(insert_label), run_time=FAST)
        
        # Show shifting animation
        new_elem = self._cell(5, INSERT_OP, show_index=False)
        new_elem.next_to(arr, LEFT, buff=0.8)
        new_label = Text("Insert 5", font_size=SMALL_SIZE, color=INSERT_OP)
        new_label.next_to(new_elem, UP, buff=0.2)
        
        self.play(FadeIn(new_elem), Write(new_label), run_time=FAST)
        
        # Shift all elements right
        shift_arrows = VGroup()
        for cell in arr.cells:
            arrow = Arrow(
                cell.get_center(), cell.get_center() + RIGHT * 0.8,
                color=DELETE_OP, stroke_width=2, buff=0.1
            )
            shift_arrows.add(arrow)
        
        self.play(
            LaggedStart(*[GrowArrow(a) for a in shift_arrows], lag_ratio=0.1),
            run_time=NORMAL
        )
        
        shift_text = Text("Shift n elements!", font_size=SMALL_SIZE, color=DELETE_OP)
        shift_text.move_to(DOWN * 1.5)
        self.play(Write(shift_text), run_time=FAST)
        self.wait(PAUSE)
        
        # Clean up
        self.play(
            FadeOut(shift_arrows), FadeOut(shift_text), FadeOut(new_elem),
            FadeOut(new_label), FadeOut(insert_label),
            run_time=FAST
        )
        
        # Summary
        summary = VGroup(
            Text("Array Operations:", font_size=BODY_SIZE, color=TEXT_PRIMARY),
            Text("Read: O(1) - Direct access", font_size=SMALL_SIZE, color=READ_OP),
            Text("Insert/Delete (end): O(1)", font_size=SMALL_SIZE, color=READ_OP),
            Text("Insert/Delete (start): O(n)", font_size=SMALL_SIZE, color=DELETE_OP),
        )
        summary.arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        summary.move_to(DOWN * 2)
        
        self.play(
            LaggedStart(*[Write(t) for t in summary], lag_ratio=0.15),
            run_time=SLOW
        )
        self.wait(LONG_PAUSE)
    
    # ==================== SCENE 3: LINKED LISTS ====================
    
    def _linked_list_scene(self):
        """Demonstrate linked lists and their operations."""
        # Title
        title = self._title("Linked Lists: Scattered Memory")
        self.play(Write(title), run_time=NORMAL)
        
        # Concept
        concept = Text("Nodes connected by pointers - anywhere in memory", 
                      font_size=BODY_SIZE, color=TEXT_SECONDARY)
        concept.move_to(UP * 2.2)
        self.play(Write(concept), run_time=FAST)
        
        # Create nodes
        nodes = []
        values = [10, 20, 30, 40]
        
        for i, v in enumerate(values):
            node = self._node(v, LINKED_LIST_COLOR)
            nodes.append(node)
        
        # Position nodes with slight vertical offset (scattered look)
        nodes[0].move_to(LEFT * 4.5 + UP * 0.8)
        nodes[1].move_to(LEFT * 1.5 + UP * 1.0)
        nodes[2].move_to(RIGHT * 1.5 + UP * 0.6)
        nodes[3].move_to(RIGHT * 4.5 + UP * 0.9)
        
        # Show nodes appearing
        node_group = VGroup(*nodes)
        self.play(
            LaggedStart(*[FadeIn(n, shift=UP * 0.2) for n in nodes], lag_ratio=0.15),
            run_time=NORMAL
        )
        
        # Add arrows between nodes
        arrows = []
        for i in range(len(nodes) - 1):
            arrow = Arrow(
                start=nodes[i].ptr_box.get_right(),
                end=nodes[i+1].val_box.get_left(),
                color=POINTER_COLOR,
                stroke_width=3,
                buff=0.1
            )
            arrows.append(arrow)
        
        # NULL terminator
        null_text = Text("NULL", font_size=TINY_SIZE, color=TEXT_SECONDARY)
        null_text.next_to(nodes[-1].ptr_box, RIGHT, buff=0.3)
        
        self.play(
            LaggedStart(*[GrowArrow(a) for a in arrows], lag_ratio=0.15),
            Write(null_text),
            run_time=NORMAL
        )
        
        # Head pointer
        head_label = Text("head", font_size=SMALL_SIZE, color=POINTER_COLOR)
        head_arrow = Arrow(
            head_label.get_right() + RIGHT * 0.1,
            nodes[0].val_box.get_left(),
            color=POINTER_COLOR, stroke_width=3, buff=0.1
        )
        head_label.next_to(head_arrow, LEFT, buff=0.1)
        
        self.play(Write(head_label), GrowArrow(head_arrow), run_time=FAST)
        self.wait(PAUSE)
        
        # Demonstrate traversal for READ
        read_label = Text("Read index 2: O(n) - Must traverse!", font_size=BODY_SIZE, color=DELETE_OP)
        read_label.move_to(DOWN * 0.8)
        self.play(Write(read_label), run_time=FAST)
        
        # Traverse animation
        for i in range(3):
            self.play(self._color_node(nodes[i], ACTIVE_COMPARISON), run_time=FAST)
            if i < 2:
                self.play(self._color_node(nodes[i], LINKED_LIST_COLOR), run_time=INSTANT)
        
        result = Text("= 30 (after 3 hops)", font_size=LABEL_SIZE, color=DELETE_OP)
        result.move_to(DOWN * 1.5)
        self.play(Write(result), run_time=FAST)
        self.wait(PAUSE)
        
        # Reset colors
        self.play(
            self._color_node(nodes[2], LINKED_LIST_COLOR),
            FadeOut(read_label), FadeOut(result),
            run_time=FAST
        )
        
        # Demonstrate INSERT at start
        insert_label = Text("Insert at Start: O(1) - Just update head!", font_size=BODY_SIZE, color=READ_OP)
        insert_label.move_to(DOWN * 0.8)
        self.play(Write(insert_label), run_time=FAST)
        
        # New node
        new_node = self._node(5, INSERT_OP)
        new_node.move_to(LEFT * 5.5 + DOWN * 0.5)
        
        self.play(FadeIn(new_node, shift=UP * 0.3), run_time=FAST)
        
        # New arrow from new node to old head
        new_arrow = Arrow(
            new_node.ptr_box.get_right(),
            nodes[0].val_box.get_left(),
            color=POINTER_COLOR, stroke_width=3, buff=0.1
        )
        
        self.play(GrowArrow(new_arrow), run_time=FAST)
        
        # Update head (visual)
        new_head_arrow = Arrow(
            head_label.get_right() + RIGHT * 0.1,
            new_node.val_box.get_left(),
            color=POINTER_COLOR, stroke_width=3, buff=0.1
        )
        
        self.play(
            ReplacementTransform(head_arrow, new_head_arrow),
            run_time=NORMAL
        )
        
        done_text = Text("Done! No shifting needed", font_size=SMALL_SIZE, color=READ_OP)
        done_text.move_to(DOWN * 1.5)
        self.play(Write(done_text), run_time=FAST)
        self.wait(PAUSE)
        
        # Clean up and summary
        self.play(
            FadeOut(insert_label), FadeOut(done_text),
            FadeOut(new_node), FadeOut(new_arrow), FadeOut(new_head_arrow),
            run_time=FAST
        )
        
        # Restore head arrow
        head_arrow = Arrow(
            head_label.get_right() + RIGHT * 0.1,
            nodes[0].val_box.get_left(),
            color=POINTER_COLOR, stroke_width=3, buff=0.1
        )
        self.play(GrowArrow(head_arrow), run_time=FAST)
        
        # Summary
        summary = VGroup(
            Text("Linked List Operations:", font_size=BODY_SIZE, color=TEXT_PRIMARY),
            Text("Read: O(n) - Must traverse", font_size=SMALL_SIZE, color=DELETE_OP),
            Text("Insert/Delete (start): O(1)", font_size=SMALL_SIZE, color=READ_OP),
            Text("Insert/Delete (middle): O(n) traverse + O(1)", font_size=SMALL_SIZE, color=INSERT_OP),
        )
        summary.arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        summary.move_to(DOWN * 2.3)
        
        self.play(
            LaggedStart(*[Write(t) for t in summary], lag_ratio=0.15),
            run_time=SLOW
        )
        self.wait(LONG_PAUSE)
    
    # ==================== SCENE 4: COMPARISON ====================
    
    def _comparison_scene(self):
        """Side-by-side comparison of arrays vs linked lists."""
        # Title
        title = self._title("Arrays vs Linked Lists")
        self.play(Write(title), run_time=NORMAL)
        
        # Divider
        divider = DashedLine(UP * 2.5, DOWN * 3, color=TEXT_SECONDARY, stroke_width=1.5)
        self.play(Create(divider), run_time=FAST)
        
        # Headers
        array_head = Text("Arrays", font_size=BODY_SIZE, color=ARRAY_COLOR)
        list_head = Text("Linked Lists", font_size=BODY_SIZE, color=LINKED_LIST_COLOR)
        array_head.move_to(LEFT * 3.5 + UP * 2.2)
        list_head.move_to(RIGHT * 3.5 + UP * 2.2)
        
        self.play(Write(array_head), Write(list_head), run_time=FAST)
        
        # Memory visualization
        # Array - contiguous
        array_mem = VGroup()
        for i in range(5):
            box = Rectangle(width=0.5, height=0.5, fill_color=ARRAY_COLOR, 
                          fill_opacity=0.8, stroke_color=TEXT_PRIMARY, stroke_width=1.5)
            array_mem.add(box)
        array_mem.arrange(RIGHT, buff=0)
        array_mem.move_to(LEFT * 3.5 + UP * 1.2)
        
        array_mem_label = Text("Contiguous", font_size=SMALL_SIZE, color=ARRAY_COLOR)
        array_mem_label.next_to(array_mem, DOWN, buff=0.15)
        
        # Linked List - scattered
        list_mem = VGroup()
        positions = [RIGHT * 2.5, RIGHT * 3.3 + UP * 0.3, RIGHT * 4.1, 
                    RIGHT * 4.9 + DOWN * 0.2, RIGHT * 5.7 + UP * 0.1]
        for pos in positions:
            box = Rectangle(width=0.4, height=0.4, fill_color=LINKED_LIST_COLOR,
                          fill_opacity=0.8, stroke_color=TEXT_PRIMARY, stroke_width=1.5)
            box.move_to(pos + UP * 1.2)
            list_mem.add(box)
        
        list_mem_label = Text("Scattered", font_size=SMALL_SIZE, color=LINKED_LIST_COLOR)
        list_mem_label.next_to(list_mem, DOWN, buff=0.15)
        
        self.play(
            LaggedStart(*[FadeIn(b) for b in array_mem], lag_ratio=0.1),
            LaggedStart(*[FadeIn(b) for b in list_mem], lag_ratio=0.1),
            run_time=NORMAL
        )
        self.play(Write(array_mem_label), Write(list_mem_label), run_time=FAST)
        self.wait(PAUSE)
        
        # Comparison table
        table_data = [
            ("Operation", "Array", "Linked List"),
            ("Read", "O(1)", "O(n)"),
            ("Insert (start)", "O(n)", "O(1)"),
            ("Insert (end)", "O(1)", "O(n)"),
            ("Delete (start)", "O(n)", "O(1)"),
            ("Memory", "Fixed", "Flexible"),
        ]
        
        table = VGroup()
        for i, (op, arr_c, list_c) in enumerate(table_data):
            if i == 0:
                # Header row
                row = VGroup(
                    Text(op, font_size=SMALL_SIZE, color=TEXT_PRIMARY),
                    Text(arr_c, font_size=SMALL_SIZE, color=ARRAY_COLOR),
                    Text(list_c, font_size=SMALL_SIZE, color=LINKED_LIST_COLOR)
                )
            else:
                # Determine colors based on which is better
                arr_color = READ_OP if "1" in arr_c else DELETE_OP
                list_color = READ_OP if "1" in list_c else DELETE_OP
                if "Fixed" in arr_c:
                    arr_color = INSERT_OP
                    list_color = READ_OP
                
                row = VGroup(
                    Text(op, font_size=SMALL_SIZE, color=TEXT_SECONDARY),
                    Text(arr_c, font_size=SMALL_SIZE, color=arr_color),
                    Text(list_c, font_size=SMALL_SIZE, color=list_color)
                )
            
            row.arrange(RIGHT, buff=1.5)
            table.add(row)
        
        table.arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        table.move_to(DOWN * 1.2)
        
        self.play(
            LaggedStart(*[FadeIn(row) for row in table], lag_ratio=0.12),
            run_time=SLOW
        )
        self.wait(LONG_PAUSE)
        
        # Key insight
        insight = Text("Choose based on your access pattern!", font_size=BODY_SIZE, color=TEXT_ACCENT)
        insight.move_to(DOWN * 3)
        self.play(Write(insight), run_time=NORMAL)
        self.wait(LONG_PAUSE)
    
    # ==================== SCENE 5: SELECTION SORT ====================
    
    def _selection_sort_scene(self):
        """Demonstrate selection sort algorithm."""
        # Title
        title = self._title("Selection Sort")
        self.play(Write(title), run_time=NORMAL)
        
        # Concept
        concept = Text("Find smallest, move to front, repeat", 
                      font_size=BODY_SIZE, color=TEXT_SECONDARY)
        concept.move_to(UP * 2.2)
        self.play(Write(concept), run_time=FAST)
        
        # Create array
        values = list(DEMO_ARRAY)  # [64, 25, 12, 22, 11]
        arr = self._array(values, UNPROCESSED)
        arr.move_to(UP * 0.8)
        
        self.play(FadeIn(arr), run_time=NORMAL)
        self.wait(PAUSE)
        
        # Complexity note
        complexity = Text("Time: O(n²)", font_size=LABEL_SIZE, color=O_N_SQUARED)
        complexity.move_to(DOWN * 2.8)
        self.play(Write(complexity), run_time=FAST)
        
        # Step counter
        step_text = Text("Pass: 0", font_size=LABEL_SIZE, color=TEXT_SECONDARY)
        step_text.move_to(DOWN * 0.5)
        self.play(Write(step_text), run_time=FAST)
        
        # Current minimum pointer
        min_ptr = Triangle(fill_color=CURRENT_MIN, fill_opacity=1, stroke_width=0)
        min_ptr.scale(0.1).rotate(PI)
        
        # Scan pointer
        scan_ptr = Triangle(fill_color=ACTIVE_COMPARISON, fill_opacity=1, stroke_width=0)
        scan_ptr.scale(0.1).rotate(PI)
        
        n = len(values)
        
        # Selection sort animation
        for i in range(n - 1):
            # Update pass counter
            new_step = Text(f"Pass: {i + 1}", font_size=LABEL_SIZE, color=TEXT_SECONDARY)
            new_step.move_to(step_text.get_center())
            self.play(ReplacementTransform(step_text, new_step), run_time=INSTANT)
            step_text = new_step
            
            min_idx = i
            
            # Position min pointer at i
            min_ptr.next_to(arr.cells[i], UP, buff=0.25)
            min_label = Text("min", font_size=TINY_SIZE, color=CURRENT_MIN)
            min_label.next_to(min_ptr, UP, buff=0.05)
            
            self.play(
                FadeIn(min_ptr), Write(min_label),
                self._color_cell(arr.cells[i], CURRENT_MIN),
                run_time=FAST
            )
            
            # Scan for minimum
            for j in range(i + 1, n):
                # Position scan pointer
                scan_ptr.next_to(arr.cells[j], UP, buff=0.25)
                
                if j == i + 1:
                    self.play(FadeIn(scan_ptr), run_time=INSTANT)
                else:
                    self.play(scan_ptr.animate.next_to(arr.cells[j], UP, buff=0.25), run_time=INSTANT)
                
                # Highlight comparison
                self.play(self._color_cell(arr.cells[j], ACTIVE_COMPARISON), run_time=INSTANT)
                
                # Check if new minimum
                if values[j] < values[min_idx]:
                    # Found new minimum
                    self.play(
                        self._color_cell(arr.cells[min_idx], UNPROCESSED if min_idx > i - 1 else SORTED_ELEMENT),
                        run_time=INSTANT
                    )
                    min_idx = j
                    self.play(
                        min_ptr.animate.next_to(arr.cells[j], UP, buff=0.25),
                        min_label.animate.next_to(min_ptr, UP, buff=0.05),
                        self._color_cell(arr.cells[j], CURRENT_MIN),
                        run_time=FAST
                    )
                else:
                    # Reset color
                    self.play(
                        self._color_cell(arr.cells[j], UNPROCESSED),
                        run_time=INSTANT
                    )
            
            self.play(FadeOut(scan_ptr), run_time=INSTANT)
            
            # Swap if needed
            if min_idx != i:
                # Swap animation
                cell_i = arr.cells[i]
                cell_min = arr.cells[min_idx]
                
                # Get current positions
                pos_i = cell_i.get_center()
                pos_min = cell_min.get_center()
                
                # Animate swap
                self.play(
                    cell_i.animate.move_to(pos_min),
                    cell_min.animate.move_to(pos_i),
                    run_time=NORMAL
                )
                
                # Update array state
                arr.cells[i], arr.cells[min_idx] = arr.cells[min_idx], arr.cells[i]
                values[i], values[min_idx] = values[min_idx], values[i]
            
            # Mark as sorted
            self.play(
                self._color_cell(arr.cells[i], SORTED_ELEMENT),
                FadeOut(min_ptr), FadeOut(min_label),
                run_time=FAST
            )
        
        # Last element is automatically sorted
        self.play(self._color_cell(arr.cells[-1], SORTED_ELEMENT), run_time=FAST)
        
        # Final result
        result_text = Text("Sorted!", font_size=BODY_SIZE, color=SORTED_ELEMENT)
        result_text.move_to(DOWN * 1.5)
        self.play(Write(result_text), run_time=NORMAL)
        self.wait(LONG_PAUSE)
    
    # ==================== SCENE 6: SUMMARY ====================
    
    def _summary_scene(self):
        """Final summary and key takeaways."""
        # Title
        title = self._title("Key Takeaways")
        self.play(Write(title), run_time=NORMAL)
        
        # Takeaways
        takeaways = [
            ("1.", "Arrays: Fast reads O(1), slow inserts O(n)", ARRAY_COLOR),
            ("2.", "Linked Lists: Slow reads O(n), fast start inserts O(1)", LINKED_LIST_COLOR),
            ("3.", "Selection Sort: O(n²) - finds minimum each pass", O_N_SQUARED),
            ("4.", "Choose data structure based on access patterns", TEXT_ACCENT),
        ]
        
        items = VGroup()
        for num, text, color in takeaways:
            num_text = Text(num, font_size=BODY_SIZE, color=TEXT_PRIMARY)
            content = Text(text, font_size=LABEL_SIZE, color=color)
            content.next_to(num_text, RIGHT, buff=0.2)
            row = VGroup(num_text, content)
            items.add(row)
        
        items.arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        items.move_to(UP * 0.5)
        
        self.play(
            LaggedStart(*[FadeIn(item, shift=LEFT * 0.3) for item in items], lag_ratio=0.2),
            run_time=SLOW
        )
        self.wait(PAUSE)
        
        # Quick reference
        ref_title = Text("Quick Reference:", font_size=BODY_SIZE, color=TEXT_PRIMARY)
        ref_title.move_to(DOWN * 1.8)
        
        ref_table = VGroup(
            Text("Arrays → lots of reads", font_size=SMALL_SIZE, color=ARRAY_COLOR),
            Text("Linked Lists → lots of inserts/deletes", font_size=SMALL_SIZE, color=LINKED_LIST_COLOR),
        )
        ref_table.arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        ref_table.next_to(ref_title, DOWN, buff=0.3)
        
        self.play(Write(ref_title), run_time=FAST)
        self.play(
            LaggedStart(*[Write(t) for t in ref_table], lag_ratio=0.2),
            run_time=NORMAL
        )
        self.wait(LONG_PAUSE)


# Individual scene classes for separate rendering
class IntroScene(Scene):
    """Introduction scene only."""
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        Chapter2Animation._intro_scene(self)


class ArrayScene(Scene):
    """Array scene only."""
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        Chapter2Animation._array_scene(self)


class LinkedListScene(Scene):
    """Linked list scene only."""
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        Chapter2Animation._linked_list_scene(self)


class ComparisonScene(Scene):
    """Comparison scene only."""
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        Chapter2Animation._comparison_scene(self)


class SelectionSortScene(Scene):
    """Selection sort scene only."""
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        Chapter2Animation._selection_sort_scene(self)


class SummaryScene(Scene):
    """Summary scene only."""
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        Chapter2Animation._summary_scene(self)
