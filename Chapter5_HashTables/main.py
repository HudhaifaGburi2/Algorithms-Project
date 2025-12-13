#!/usr/bin/env python3
"""
Chapter 5: Hash Tables
======================
Educational animation demonstrating hash tables, hash functions, and O(1) lookup.
3Blue1Brown-style with smooth motion, clear visuals, and minimal text.

Usage:
    manim -pql main.py Chapter5Animation    # Preview (480p)
    manim -pqh main.py Chapter5Animation    # HD quality (1080p)
    
Individual scenes:
    manim -pql main.py IntroScene
    manim -pql main.py HashFunctionScene
    manim -pql main.py PhoneBookScene
    manim -pql main.py DuplicatesScene
    manim -pql main.py CachingScene
    manim -pql main.py CollisionsScene
    manim -pql main.py PerformanceScene
    manim -pql main.py LoadFactorScene
    manim -pql main.py SummaryScene
"""
import sys
sys.path.insert(0, '/home/hg/Desktop/algorthims/Chapter5_HashTables')

from manim import *

from config.colors import (
    BACKGROUND_COLOR, TEXT_PRIMARY, TEXT_SECONDARY, TEXT_ACCENT,
    CELL_EMPTY, CELL_FILLED, CELL_HIGHLIGHT,
    HASH_FUNCTION, KEY_COLOR, VALUE_COLOR, LINKED_LIST, CACHE_COLOR,
    COMPLETED, WARNING, ERROR,
    O_1, O_LOG_N, O_N,
    LOAD_LOW, LOAD_MED, LOAD_HIGH
)
from config.fonts import (
    TITLE_SIZE, SUBTITLE_SIZE, HEADING_SIZE, BODY_SIZE,
    LABEL_SIZE, SMALL_SIZE, TINY_SIZE
)
from config.animation_constants import (
    INSTANT, FAST, NORMAL, SLOW, PAUSE, LONG_PAUSE,
    TITLE_Y, CONTENT_TOP, CONTENT_MID
)


class Chapter5Animation(Scene):
    """
    Complete Chapter 5 animation covering:
    1. Introduction - The O(1) Lookup Problem
    2. Hash Functions - String to Number
    3. Phone Book Use Case
    4. Preventing Duplicates Use Case
    5. Caching Use Case
    6. Collisions and Chaining
    7. Performance Analysis
    8. Load Factor and Resizing
    9. Summary
    """
    
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        
        # Scene 1: Introduction
        self._intro_scene()
        self._clear()
        
        # Scene 2: Hash Functions
        self._hash_function_scene()
        self._clear()
        
        # Scene 3: Phone Book
        self._phone_book_scene()
        self._clear()
        
        # Scene 4: Preventing Duplicates
        self._duplicates_scene()
        self._clear()
        
        # Scene 5: Caching
        self._caching_scene()
        self._clear()
        
        # Scene 6: Collisions
        self._collisions_scene()
        self._clear()
        
        # Scene 7: Performance
        self._performance_scene()
        self._clear()
        
        # Scene 8: Load Factor
        self._load_factor_scene()
        self._clear()
        
        # Scene 9: Summary
        self._summary_scene()
    
    def _clear(self):
        if self.mobjects:
            self.play(*[FadeOut(m) for m in self.mobjects], run_time=FAST)
        self.wait(0.2)
    
    # ==================== HELPERS ====================
    
    def _title(self, text, y=TITLE_Y):
        t = Text(text, font_size=HEADING_SIZE, color=TEXT_PRIMARY)
        t.move_to(UP * y)
        return t
    
    def _cell(self, index, content=None, color=CELL_EMPTY, width=0.75, height=0.55):
        grp = VGroup()
        rect = Rectangle(width=width, height=height, fill_color=color,
                        fill_opacity=0.85, stroke_color=TEXT_PRIMARY, stroke_width=2)
        
        idx = Text(str(index), font_size=TINY_SIZE, color=TEXT_SECONDARY)
        idx.next_to(rect, UP, buff=0.05)
        
        grp.add(rect, idx)
        grp.rect = rect
        
        if content:
            lbl = Text(content, font_size=TINY_SIZE, color=TEXT_PRIMARY)
            lbl.move_to(rect.get_center())
            grp.add(lbl)
            grp.content = lbl
        
        return grp
    
    def _hash_table(self, slots=10):
        table = VGroup()
        cells = []
        for i in range(slots):
            cell = self._cell(i)
            cells.append(cell)
            table.add(cell)
        table.arrange(RIGHT, buff=0.08)
        table.cells = cells
        return table
    
    def _hash_box(self, width=1.8, height=1.0):
        grp = VGroup()
        box = RoundedRectangle(width=width, height=height, corner_radius=0.12,
                              fill_color=HASH_FUNCTION, fill_opacity=0.75,
                              stroke_color=TEXT_PRIMARY, stroke_width=2)
        lbl = Text("hash()", font_size=SMALL_SIZE, color=TEXT_PRIMARY)
        lbl.move_to(box.get_center())
        grp.add(box, lbl)
        grp.box = box
        return grp
    
    def _simple_hash(self, key, size=10):
        return sum(ord(c) for c in key.lower()) % size
    
    # ==================== SCENE 1: INTRODUCTION ====================
    
    def _intro_scene(self):
        """Introduction to the O(1) lookup problem."""
        # Title
        title = Text("Chapter 5: Hash Tables", font_size=TITLE_SIZE, color=TEXT_PRIMARY)
        title.move_to(UP * 2)
        self.play(Write(title), run_time=SLOW)
        self.wait(PAUSE)
        
        # Subtitle
        subtitle = Text("The Magic of O(1) Lookup", font_size=SUBTITLE_SIZE, color=TEXT_ACCENT)
        subtitle.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(subtitle, shift=UP * 0.3), run_time=NORMAL)
        self.wait(PAUSE)
        
        # Move title
        self.play(
            title.animate.scale(0.7).move_to(UP * 3.2),
            FadeOut(subtitle),
            run_time=NORMAL
        )
        
        # Problem setup - grocery store
        problem = Text("Problem: Price lookup in a grocery store", 
                      font_size=BODY_SIZE, color=TEXT_SECONDARY)
        problem.move_to(UP * 2.2)
        self.play(Write(problem), run_time=FAST)
        
        # Comparison: Linear vs Binary vs Hash
        methods = VGroup()
        
        # Linear search
        linear = VGroup(
            Text("Linear Search", font_size=LABEL_SIZE, color=O_N),
            Text("Check each item", font_size=SMALL_SIZE, color=TEXT_SECONDARY),
            Text("O(n)", font_size=LABEL_SIZE, color=O_N),
        )
        linear.arrange(DOWN, buff=0.15)
        
        # Binary search
        binary = VGroup(
            Text("Binary Search", font_size=LABEL_SIZE, color=O_LOG_N),
            Text("Sorted list, halve", font_size=SMALL_SIZE, color=TEXT_SECONDARY),
            Text("O(log n)", font_size=LABEL_SIZE, color=O_LOG_N),
        )
        binary.arrange(DOWN, buff=0.15)
        
        # Hash table
        hash_t = VGroup(
            Text("Hash Table", font_size=LABEL_SIZE, color=O_1),
            Text("Direct access!", font_size=SMALL_SIZE, color=TEXT_SECONDARY),
            Text("O(1)", font_size=LABEL_SIZE, color=O_1),
        )
        hash_t.arrange(DOWN, buff=0.15)
        
        methods.add(linear, binary, hash_t)
        methods.arrange(RIGHT, buff=1.5)
        methods.move_to(UP * 0.3)
        
        self.play(
            LaggedStart(*[FadeIn(m) for m in methods], lag_ratio=0.3),
            run_time=SLOW
        )
        self.wait(PAUSE)
        
        # Highlight hash table
        highlight_box = SurroundingRectangle(hash_t, color=O_1, buff=0.2)
        self.play(Create(highlight_box), run_time=FAST)
        
        # Key insight
        insight = Text("Instant lookup regardless of data size!", 
                      font_size=BODY_SIZE, color=O_1)
        insight.move_to(DOWN * 2)
        self.play(Write(insight), run_time=NORMAL)
        
        # Question
        question = Text("How? Using a hash function!", 
                       font_size=LABEL_SIZE, color=TEXT_ACCENT)
        question.move_to(DOWN * 2.8)
        self.play(Write(question), run_time=FAST)
        self.wait(LONG_PAUSE)
    
    # ==================== SCENE 2: HASH FUNCTIONS ====================
    
    def _hash_function_scene(self):
        """Demonstrate hash functions."""
        # Title
        title = self._title("Hash Functions: String → Number")
        self.play(Write(title), run_time=NORMAL)
        
        # Concept
        concept = Text("Maps any key to an array index", 
                      font_size=BODY_SIZE, color=TEXT_SECONDARY)
        concept.move_to(UP * 2.2)
        self.play(Write(concept), run_time=FAST)
        
        # Hash function box
        hash_box = self._hash_box()
        hash_box.move_to(UP * 0.8)
        self.play(FadeIn(hash_box), run_time=NORMAL)
        
        # Array below
        table = self._hash_table(10)
        table.move_to(DOWN * 1.2)
        self.play(FadeIn(table), run_time=NORMAL)
        self.wait(PAUSE)
        
        # Demo items
        items = [
            ("apple", 0.67),
            ("milk", 1.49),
            ("banana", 0.59),
        ]
        
        for key, value in items:
            # Show key input
            key_text = Text(f'"{key}"', font_size=LABEL_SIZE, color=KEY_COLOR)
            key_text.next_to(hash_box, UP, buff=0.4)
            
            self.play(FadeIn(key_text, shift=DOWN * 0.2), run_time=FAST)
            
            # Hash function processes
            self.play(
                hash_box.box.animate.scale(1.1),
                run_time=FAST
            )
            self.play(
                hash_box.box.animate.scale(1/1.1),
                run_time=FAST
            )
            
            # Calculate hash
            idx = self._simple_hash(key, 10)
            
            # Show output
            idx_text = Text(str(idx), font_size=LABEL_SIZE, color=VALUE_COLOR)
            idx_text.next_to(hash_box, DOWN, buff=0.4)
            self.play(FadeIn(idx_text, shift=DOWN * 0.2), run_time=FAST)
            
            # Arrow to cell
            target_cell = table.cells[idx]
            arrow = Arrow(
                idx_text.get_bottom(),
                target_cell.rect.get_top(),
                color=TEXT_ACCENT, stroke_width=2, buff=0.1
            )
            self.play(GrowArrow(arrow), run_time=FAST)
            
            # Fill cell
            content = Text(f"{key[:3]}:{value}", font_size=TINY_SIZE, color=TEXT_PRIMARY)
            content.move_to(target_cell.rect.get_center())
            
            self.play(
                target_cell.rect.animate.set_fill(CELL_FILLED),
                FadeIn(content),
                run_time=FAST
            )
            
            # Clean up for next
            self.play(
                FadeOut(key_text), FadeOut(idx_text), FadeOut(arrow),
                run_time=FAST
            )
            self.wait(0.2)
        
        # Lookup demo
        lookup_title = Text("Lookup: What's the price of apple?", 
                           font_size=LABEL_SIZE, color=TEXT_ACCENT)
        lookup_title.move_to(DOWN * 2.8)
        self.play(Write(lookup_title), run_time=FAST)
        
        # Show instant lookup
        apple_idx = self._simple_hash("apple", 10)
        self.play(
            table.cells[apple_idx].rect.animate.set_fill(CELL_HIGHLIGHT),
            run_time=FAST
        )
        
        result = Text("→ $0.67 (instant!)", font_size=LABEL_SIZE, color=O_1)
        result.next_to(lookup_title, RIGHT, buff=0.3)
        self.play(Write(result), run_time=FAST)
        self.wait(LONG_PAUSE)
    
    # ==================== SCENE 3: PHONE BOOK ====================
    
    def _phone_book_scene(self):
        """Phone book use case."""
        # Title
        title = self._title("Use Case: Phone Book")
        self.play(Write(title), run_time=NORMAL)
        
        # Code
        code = VGroup(
            Text("phone_book = {}", font_size=SMALL_SIZE, color=TEXT_PRIMARY),
            Text('phone_book["jenny"] = "867-5309"', font_size=SMALL_SIZE, color=TEXT_PRIMARY),
            Text('phone_book["emergency"] = "911"', font_size=SMALL_SIZE, color=TEXT_PRIMARY),
        )
        code.arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        code.move_to(LEFT * 3 + UP * 1.2)
        
        self.play(
            LaggedStart(*[Write(c) for c in code], lag_ratio=0.3),
            run_time=SLOW
        )
        self.wait(PAUSE)
        
        # Visual hash table
        table = self._hash_table(8)
        table.move_to(RIGHT * 2 + DOWN * 0.5)
        self.play(FadeIn(table), run_time=NORMAL)
        
        # Add entries
        entries = [
            ("jenny", "867-5309", 2),
            ("emergency", "911", 5),
        ]
        
        for name, number, idx in entries:
            content = Text(f"{name[:4]}:{number[:3]}", font_size=TINY_SIZE, color=TEXT_PRIMARY)
            content.move_to(table.cells[idx].rect.get_center())
            
            self.play(
                table.cells[idx].rect.animate.set_fill(CELL_FILLED),
                FadeIn(content),
                run_time=FAST
            )
        
        self.wait(PAUSE)
        
        # Lookup
        lookup = Text('phone_book["jenny"]', font_size=LABEL_SIZE, color=KEY_COLOR)
        lookup.move_to(DOWN * 2.3)
        
        result = Text('→ "867-5309" (O(1))', font_size=LABEL_SIZE, color=O_1)
        result.next_to(lookup, RIGHT, buff=0.3)
        
        self.play(Write(lookup), run_time=FAST)
        self.play(
            table.cells[2].rect.animate.set_fill(CELL_HIGHLIGHT),
            Write(result),
            run_time=FAST
        )
        
        # Real world note
        note = Text("Real use: DNS (domain → IP address)", 
                   font_size=SMALL_SIZE, color=TEXT_SECONDARY)
        note.move_to(DOWN * 3)
        self.play(Write(note), run_time=FAST)
        self.wait(LONG_PAUSE)
    
    # ==================== SCENE 4: DUPLICATES ====================
    
    def _duplicates_scene(self):
        """Preventing duplicates use case."""
        # Title
        title = self._title("Use Case: Prevent Duplicates")
        self.play(Write(title), run_time=NORMAL)
        
        # Scenario
        scenario = Text("Voting: Each person votes once", 
                       font_size=BODY_SIZE, color=TEXT_SECONDARY)
        scenario.move_to(UP * 2.2)
        self.play(Write(scenario), run_time=FAST)
        
        # Hash table for voters
        table = self._hash_table(6)
        table.move_to(UP * 0.5)
        self.play(FadeIn(table), run_time=NORMAL)
        
        # Voter attempts
        voters = [
            ("tom", True, 2),    # First time - OK
            ("mike", True, 4),   # First time - OK
            ("tom", False, 2),   # Duplicate - REJECT
        ]
        
        for name, allowed, idx in voters:
            # Voter arrives
            voter_text = Text(f'"{name}" wants to vote', 
                            font_size=LABEL_SIZE, color=KEY_COLOR)
            voter_text.move_to(DOWN * 1)
            self.play(Write(voter_text), run_time=FAST)
            
            # Check hash table
            self.play(table.cells[idx].rect.animate.set_fill(CELL_HIGHLIGHT), run_time=FAST)
            
            if allowed:
                # First time - allow and record
                result = Text("Not found → Let them vote!", 
                            font_size=LABEL_SIZE, color=O_1)
                result.move_to(DOWN * 1.8)
                self.play(Write(result), run_time=FAST)
                
                # Add to table
                content = Text(name, font_size=TINY_SIZE, color=TEXT_PRIMARY)
                content.move_to(table.cells[idx].rect.get_center())
                self.play(
                    table.cells[idx].rect.animate.set_fill(CELL_FILLED),
                    FadeIn(content),
                    run_time=FAST
                )
            else:
                # Duplicate - reject
                result = Text("Found! → Already voted - REJECT!", 
                            font_size=LABEL_SIZE, color=ERROR)
                result.move_to(DOWN * 1.8)
                self.play(Write(result), run_time=FAST)
                
                # Flash red
                self.play(
                    table.cells[idx].rect.animate.set_fill(ERROR),
                    run_time=FAST
                )
                self.play(
                    table.cells[idx].rect.animate.set_fill(CELL_FILLED),
                    run_time=FAST
                )
            
            self.wait(0.5)
            self.play(FadeOut(voter_text), FadeOut(result), run_time=FAST)
        
        # Efficiency note
        note = Text("O(1) duplicate check vs O(n) list scan", 
                   font_size=LABEL_SIZE, color=TEXT_ACCENT)
        note.move_to(DOWN * 2.5)
        self.play(Write(note), run_time=NORMAL)
        self.wait(LONG_PAUSE)
    
    # ==================== SCENE 5: CACHING ====================
    
    def _caching_scene(self):
        """Caching use case."""
        # Title
        title = self._title("Use Case: Caching")
        self.play(Write(title), run_time=NORMAL)
        
        # Setup: Server and Cache
        server = VGroup()
        server_box = RoundedRectangle(width=1.5, height=1.0, corner_radius=0.1,
                                     fill_color=TEXT_SECONDARY, fill_opacity=0.5,
                                     stroke_color=TEXT_PRIMARY, stroke_width=2)
        server_label = Text("Server", font_size=SMALL_SIZE, color=TEXT_PRIMARY)
        server_label.move_to(server_box.get_center())
        server.add(server_box, server_label)
        server.move_to(RIGHT * 4 + UP * 1)
        
        cache = VGroup()
        cache_box = RoundedRectangle(width=2.0, height=1.2, corner_radius=0.1,
                                    fill_color=CACHE_COLOR, fill_opacity=0.5,
                                    stroke_color=TEXT_PRIMARY, stroke_width=2)
        cache_label = Text("Cache", font_size=SMALL_SIZE, color=TEXT_PRIMARY)
        cache_label.move_to(cache_box.get_center())
        cache.add(cache_box, cache_label)
        cache.move_to(ORIGIN + UP * 1)
        
        browser = VGroup()
        browser_box = RoundedRectangle(width=1.5, height=1.0, corner_radius=0.1,
                                      fill_color=KEY_COLOR, fill_opacity=0.5,
                                      stroke_color=TEXT_PRIMARY, stroke_width=2)
        browser_label = Text("Browser", font_size=SMALL_SIZE, color=TEXT_PRIMARY)
        browser_label.move_to(browser_box.get_center())
        browser.add(browser_box, browser_label)
        browser.move_to(LEFT * 4 + UP * 1)
        
        self.play(FadeIn(browser), FadeIn(cache), FadeIn(server), run_time=NORMAL)
        self.wait(PAUSE)
        
        # Request 1: Not cached
        req1 = Text("Request: /login page", font_size=LABEL_SIZE, color=KEY_COLOR)
        req1.move_to(DOWN * 0.5)
        self.play(Write(req1), run_time=FAST)
        
        # Arrow to cache (miss)
        arrow1 = Arrow(browser.get_right(), cache.get_left(), color=KEY_COLOR, buff=0.1)
        self.play(GrowArrow(arrow1), run_time=FAST)
        
        miss = Text("Cache miss!", font_size=SMALL_SIZE, color=WARNING)
        miss.next_to(cache, DOWN, buff=0.2)
        self.play(Write(miss), run_time=FAST)
        
        # Arrow to server
        arrow2 = Arrow(cache.get_right(), server.get_left(), color=KEY_COLOR, buff=0.1)
        self.play(GrowArrow(arrow2), run_time=FAST)
        
        # Server responds (slow)
        slow = Text("2 seconds...", font_size=SMALL_SIZE, color=WARNING)
        slow.next_to(server, DOWN, buff=0.2)
        self.play(Write(slow), run_time=FAST)
        self.wait(1)
        
        # Store in cache
        stored = Text("Stored in cache", font_size=SMALL_SIZE, color=CACHE_COLOR)
        stored.move_to(DOWN * 1.5)
        self.play(
            cache_box.animate.set_fill(CACHE_COLOR, opacity=0.8),
            Write(stored),
            run_time=FAST
        )
        
        self.play(FadeOut(miss), FadeOut(slow), FadeOut(arrow1), FadeOut(arrow2),
                 FadeOut(req1), FadeOut(stored), run_time=FAST)
        
        # Request 2: Cached
        req2 = Text("Request: /login page (again)", font_size=LABEL_SIZE, color=KEY_COLOR)
        req2.move_to(DOWN * 0.5)
        self.play(Write(req2), run_time=FAST)
        
        arrow3 = Arrow(browser.get_right(), cache.get_left(), color=KEY_COLOR, buff=0.1)
        self.play(GrowArrow(arrow3), run_time=FAST)
        
        hit = Text("Cache hit!", font_size=SMALL_SIZE, color=O_1)
        hit.next_to(cache, DOWN, buff=0.2)
        self.play(Write(hit), run_time=FAST)
        
        # Instant response
        fast_resp = Text("Instant! (0.001s)", font_size=LABEL_SIZE, color=O_1)
        fast_resp.move_to(DOWN * 1.5)
        self.play(Write(fast_resp), run_time=FAST)
        
        # Server stays idle
        idle = Text("Server idle", font_size=SMALL_SIZE, color=TEXT_SECONDARY)
        idle.next_to(server, DOWN, buff=0.2)
        self.play(Write(idle), run_time=FAST)
        
        self.wait(PAUSE)
        
        # Benefits
        benefits = Text("Benefits: Faster + Less server load", 
                       font_size=BODY_SIZE, color=TEXT_ACCENT)
        benefits.move_to(DOWN * 2.8)
        self.play(Write(benefits), run_time=NORMAL)
        self.wait(LONG_PAUSE)
    
    # ==================== SCENE 6: COLLISIONS ====================
    
    def _collisions_scene(self):
        """Collision handling."""
        # Title
        title = self._title("Collisions: When Keys Clash")
        self.play(Write(title), run_time=NORMAL)
        
        # Problem
        problem = Text("What if two keys hash to the same index?", 
                      font_size=BODY_SIZE, color=TEXT_SECONDARY)
        problem.move_to(UP * 2.2)
        self.play(Write(problem), run_time=FAST)
        
        # Hash table
        table = self._hash_table(8)
        table.move_to(UP * 0.5)
        self.play(FadeIn(table), run_time=NORMAL)
        
        # First item: apple → index 0
        apple_text = Text('"apple" → index 0', font_size=LABEL_SIZE, color=KEY_COLOR)
        apple_text.move_to(DOWN * 1)
        self.play(Write(apple_text), run_time=FAST)
        
        apple_content = Text("apple", font_size=TINY_SIZE, color=TEXT_PRIMARY)
        apple_content.move_to(table.cells[0].rect.get_center())
        self.play(
            table.cells[0].rect.animate.set_fill(CELL_FILLED),
            FadeIn(apple_content),
            run_time=FAST
        )
        self.play(FadeOut(apple_text), run_time=FAST)
        
        # Second item: avocado → also index 0!
        avocado_text = Text('"avocado" → index 0 (COLLISION!)', 
                           font_size=LABEL_SIZE, color=WARNING)
        avocado_text.move_to(DOWN * 1)
        self.play(Write(avocado_text), run_time=FAST)
        
        # Collision effect
        self.play(
            table.cells[0].rect.animate.set_fill(ERROR),
            run_time=FAST
        )
        
        collision_label = Text("COLLISION!", font_size=BODY_SIZE, color=ERROR)
        collision_label.next_to(table.cells[0], UP, buff=0.6)
        self.play(Write(collision_label), run_time=FAST)
        self.wait(PAUSE)
        
        self.play(FadeOut(avocado_text), FadeOut(collision_label), run_time=FAST)
        
        # Solution: Chaining
        solution = Text("Solution: Linked List (Chaining)", 
                       font_size=BODY_SIZE, color=LINKED_LIST)
        solution.move_to(DOWN * 1)
        self.play(Write(solution), run_time=FAST)
        
        # Show chain
        node1 = RoundedRectangle(width=0.9, height=0.4, corner_radius=0.05,
                                fill_color=LINKED_LIST, fill_opacity=0.8,
                                stroke_color=TEXT_PRIMARY, stroke_width=2)
        node1_label = Text("avocado", font_size=TINY_SIZE - 2, color=TEXT_PRIMARY)
        node1_label.move_to(node1.get_center())
        node1_grp = VGroup(node1, node1_label)
        node1_grp.next_to(table.cells[0], DOWN, buff=0.3)
        
        arrow = Arrow(table.cells[0].rect.get_bottom(), node1.get_top(),
                     color=LINKED_LIST, stroke_width=2, buff=0.05)
        
        self.play(
            table.cells[0].rect.animate.set_fill(CELL_FILLED),
            GrowArrow(arrow),
            FadeIn(node1_grp),
            run_time=NORMAL
        )
        self.wait(PAUSE)
        
        # Worst case warning
        warning = Text("Worst case: All items in one chain → O(n)", 
                      font_size=LABEL_SIZE, color=ERROR)
        warning.move_to(DOWN * 2.5)
        self.play(Write(warning), run_time=FAST)
        
        good_hash = Text("Good hash function → even distribution → O(1)", 
                        font_size=LABEL_SIZE, color=O_1)
        good_hash.move_to(DOWN * 3.1)
        self.play(Write(good_hash), run_time=FAST)
        self.wait(LONG_PAUSE)
    
    # ==================== SCENE 7: PERFORMANCE ====================
    
    def _performance_scene(self):
        """Performance analysis."""
        # Title
        title = self._title("Performance Analysis")
        self.play(Write(title), run_time=NORMAL)
        
        # Performance table
        table_data = [
            ("Operation", "Average", "Worst"),
            ("Search", "O(1)", "O(n)"),
            ("Insert", "O(1)", "O(n)"),
            ("Delete", "O(1)", "O(n)"),
        ]
        
        table = VGroup()
        for i, (op, avg, worst) in enumerate(table_data):
            if i == 0:
                # Header
                row = VGroup(
                    Text(op, font_size=LABEL_SIZE, color=TEXT_PRIMARY),
                    Text(avg, font_size=LABEL_SIZE, color=TEXT_PRIMARY),
                    Text(worst, font_size=LABEL_SIZE, color=TEXT_PRIMARY),
                )
            else:
                row = VGroup(
                    Text(op, font_size=LABEL_SIZE, color=TEXT_SECONDARY),
                    Text(avg, font_size=LABEL_SIZE, color=O_1),
                    Text(worst, font_size=LABEL_SIZE, color=O_N),
                )
            row.arrange(RIGHT, buff=1.5)
            table.add(row)
        
        table.arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        table.move_to(UP * 0.8)
        
        self.play(
            LaggedStart(*[FadeIn(row) for row in table], lag_ratio=0.2),
            run_time=SLOW
        )
        self.wait(PAUSE)
        
        # Key insight
        insight = Text("Average case is O(1) - that's what matters!", 
                      font_size=BODY_SIZE, color=O_1)
        insight.move_to(DOWN * 1.2)
        self.play(Write(insight), run_time=NORMAL)
        
        # Comparison
        comparison = Text("vs Arrays: O(n) search | vs Binary Search: O(log n)", 
                         font_size=LABEL_SIZE, color=TEXT_SECONDARY)
        comparison.move_to(DOWN * 2)
        self.play(Write(comparison), run_time=FAST)
        
        winner = Text("Hash Tables win for lookup-heavy tasks!", 
                     font_size=BODY_SIZE, color=TEXT_ACCENT)
        winner.move_to(DOWN * 2.8)
        self.play(Write(winner), run_time=NORMAL)
        self.wait(LONG_PAUSE)
    
    # ==================== SCENE 8: LOAD FACTOR ====================
    
    def _load_factor_scene(self):
        """Load factor and resizing."""
        # Title
        title = self._title("Load Factor & Resizing")
        self.play(Write(title), run_time=NORMAL)
        
        # Formula
        formula = Text("Load Factor = Items / Slots", 
                      font_size=BODY_SIZE, color=TEXT_SECONDARY)
        formula.move_to(UP * 2.2)
        self.play(Write(formula), run_time=FAST)
        
        # Hash table (5 slots)
        table = self._hash_table(5)
        table.move_to(UP * 0.8)
        self.play(FadeIn(table), run_time=NORMAL)
        
        # Load factor gauge
        gauge_bg = Rectangle(width=4, height=0.4, fill_color=CELL_EMPTY, fill_opacity=0.5,
                            stroke_color=TEXT_PRIMARY, stroke_width=2)
        gauge_bg.move_to(DOWN * 0.5)
        
        gauge_fill = Rectangle(width=0, height=0.35, fill_color=LOAD_LOW, fill_opacity=0.9,
                              stroke_width=0)
        gauge_fill.align_to(gauge_bg, LEFT)
        gauge_fill.move_to(gauge_bg.get_center())
        
        gauge_label = Text("Load: 0%", font_size=LABEL_SIZE, color=TEXT_PRIMARY)
        gauge_label.next_to(gauge_bg, LEFT, buff=0.3)
        
        self.play(FadeIn(gauge_bg), FadeIn(gauge_fill), Write(gauge_label), run_time=FAST)
        
        # Add items
        for i in range(4):
            # Fill cell
            content = Text(f"item{i}", font_size=TINY_SIZE - 2, color=TEXT_PRIMARY)
            content.move_to(table.cells[i].rect.get_center())
            
            load = (i + 1) / 5
            load_pct = int(load * 100)
            
            # Determine color
            if load < 0.5:
                color = LOAD_LOW
            elif load < 0.7:
                color = LOAD_MED
            else:
                color = LOAD_HIGH
            
            new_label = Text(f"Load: {load_pct}%", font_size=LABEL_SIZE, color=color)
            new_label.next_to(gauge_bg, LEFT, buff=0.3)
            
            self.play(
                table.cells[i].rect.animate.set_fill(CELL_FILLED),
                FadeIn(content),
                gauge_fill.animate.set_width(4 * load).set_fill(color),
                Transform(gauge_label, new_label),
                run_time=FAST
            )
            
            if load >= 0.7:
                warning = Text("Time to resize!", font_size=LABEL_SIZE, color=LOAD_HIGH)
                warning.move_to(DOWN * 1.3)
                self.play(Write(warning), run_time=FAST)
        
        self.wait(PAUSE)
        
        # Resize explanation
        resize_text = Text("When load > 0.7: Double array size, rehash all items", 
                          font_size=LABEL_SIZE, color=TEXT_ACCENT)
        resize_text.move_to(DOWN * 2.3)
        self.play(Write(resize_text), run_time=NORMAL)
        
        cost_text = Text("Resizing is O(n), but rare → Amortized O(1)", 
                        font_size=LABEL_SIZE, color=O_1)
        cost_text.move_to(DOWN * 2.9)
        self.play(Write(cost_text), run_time=FAST)
        self.wait(LONG_PAUSE)
    
    # ==================== SCENE 9: SUMMARY ====================
    
    def _summary_scene(self):
        """Final summary."""
        # Title
        title = self._title("Key Takeaways")
        self.play(Write(title), run_time=NORMAL)
        
        # Takeaways
        takeaways = [
            ("1.", "Hash tables provide O(1) average lookup", O_1),
            ("2.", "Hash function maps keys to array indices", HASH_FUNCTION),
            ("3.", "Collisions handled by chaining", LINKED_LIST),
            ("4.", "Keep load factor < 0.7", LOAD_MED),
            ("5.", "Perfect for: lookups, caching, duplicates", TEXT_ACCENT),
        ]
        
        items = VGroup()
        for num, text, color in takeaways:
            num_text = Text(num, font_size=BODY_SIZE, color=TEXT_PRIMARY)
            content = Text(text, font_size=SMALL_SIZE, color=color)
            content.next_to(num_text, RIGHT, buff=0.2)
            row = VGroup(num_text, content)
            items.add(row)
        
        items.arrange(DOWN, buff=0.35, aligned_edge=LEFT)
        items.move_to(UP * 0.3)
        
        self.play(
            LaggedStart(*[FadeIn(item, shift=LEFT * 0.3) for item in items], lag_ratio=0.15),
            run_time=SLOW
        )
        self.wait(PAUSE)
        
        # Use cases
        use_cases = VGroup(
            Text("Use Cases:", font_size=BODY_SIZE, color=TEXT_PRIMARY),
            Text("Phone books, DNS, Caching, Voting, Deduplication", 
                font_size=LABEL_SIZE, color=TEXT_ACCENT),
        )
        use_cases.arrange(DOWN, buff=0.2)
        use_cases.move_to(DOWN * 2.3)
        
        self.play(Write(use_cases), run_time=NORMAL)
        self.wait(LONG_PAUSE)


# Individual scene classes
class IntroScene(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        Chapter5Animation._intro_scene(self)

class HashFunctionScene(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        Chapter5Animation._hash_function_scene(self)

class PhoneBookScene(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        Chapter5Animation._phone_book_scene(self)

class DuplicatesScene(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        Chapter5Animation._duplicates_scene(self)

class CachingScene(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        Chapter5Animation._caching_scene(self)

class CollisionsScene(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        Chapter5Animation._collisions_scene(self)

class PerformanceScene(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        Chapter5Animation._performance_scene(self)

class LoadFactorScene(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        Chapter5Animation._load_factor_scene(self)

class SummaryScene(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        Chapter5Animation._summary_scene(self)
