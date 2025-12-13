#!/usr/bin/env python3
"""
Chapter 7: Dijkstra's Algorithm
===============================
Educational animation demonstrating weighted graphs, shortest paths, and Dijkstra's algorithm.
3Blue1Brown-style with smooth motion, clear visuals, and minimal text.

Usage:
    manim -pql main.py Chapter7Animation    # Preview (480p)
    manim -pqh main.py Chapter7Animation    # HD quality (1080p)
"""
import sys
sys.path.insert(0, '/home/hg/Desktop/algorthims/Chapter7_DijkstrasAlgorithm')

from manim import *

from config.colors import (
    BACKGROUND_COLOR, TEXT_PRIMARY, TEXT_SECONDARY, TEXT_ACCENT,
    NODE_DEFAULT, NODE_PROCESSING, NODE_PROCESSED, NODE_CHEAPEST,
    NODE_START, NODE_FINISH, EDGE_DEFAULT, EDGE_PATH, EDGE_BETTER,
    EDGE_NEGATIVE, COST_TABLE, PARENT_TABLE, PROCESSED_SET,
    COST_IMPROVING, COST_INFINITY, WARNING_RED
)
from config.fonts import (
    TITLE_SIZE, SUBTITLE_SIZE, HEADING_SIZE, BODY_SIZE,
    LABEL_SIZE, SMALL_SIZE, TINY_SIZE, NODE_LABEL_SIZE,
    WEIGHT_LABEL_SIZE, STEP_SIZE
)
from config.animation_constants import (
    INSTANT, FAST, NORMAL, SLOW, PAUSE, LONG_PAUSE,
    TITLE_Y, NODE_RADIUS
)


class Chapter7Animation(Scene):
    """
    Complete Chapter 7 animation covering:
    1. BFS vs Dijkstra comparison
    2. First example walkthrough
    3. Path tracing
    4. Trading example (complex)
    5. Negative weights problem
    6. Applications
    7. Comparison & Summary
    """
    
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        
        self._intro_scene()
        self._clear()
        
        self._first_example_scene()
        self._clear()
        
        self._path_tracing_scene()
        self._clear()
        
        self._trading_scene()
        self._clear()
        
        self._negative_weights_scene()
        self._clear()
        
        self._applications_scene()
        self._clear()
        
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
    
    def _node(self, label, pos=ORIGIN, color=NODE_DEFAULT, radius=0.45):
        grp = VGroup()
        circle = Circle(radius=radius, fill_color=color, fill_opacity=0.9,
                       stroke_color=TEXT_PRIMARY, stroke_width=4)
        circle.move_to(pos)
        lbl = Text(label, font_size=NODE_LABEL_SIZE, color=TEXT_PRIMARY)
        lbl.move_to(circle.get_center())
        grp.add(circle, lbl)
        grp.circle = circle
        grp.label_text = label
        return grp
    
    def _weighted_edge(self, n1, n2, weight, color=EDGE_DEFAULT):
        """Create edge with weight label."""
        grp = VGroup()
        arrow = Arrow(n1.get_center(), n2.get_center(), color=color,
                     stroke_width=4, buff=0.5, max_tip_length_to_length_ratio=0.1)
        
        # Weight badge
        mid = (n1.get_center() + n2.get_center()) / 2
        badge_bg = Circle(radius=0.22, fill_color=BACKGROUND_COLOR, fill_opacity=0.95,
                         stroke_color=color, stroke_width=2)
        badge_bg.move_to(mid)
        badge_text = Text(str(weight), font_size=WEIGHT_LABEL_SIZE, color=TEXT_PRIMARY)
        badge_text.move_to(mid)
        
        grp.add(arrow, badge_bg, badge_text)
        grp.arrow = arrow
        grp.weight = weight
        return grp
    
    def _cost_row(self, name, cost, y_pos):
        """Create a cost table row."""
        row = VGroup()
        name_text = Text(name, font_size=TINY_SIZE, color=TEXT_PRIMARY)
        name_text.move_to(LEFT * 0.5 + UP * y_pos)
        
        cost_str = "∞" if cost == float('inf') else str(cost)
        cost_color = COST_INFINITY if cost == float('inf') else COST_TABLE
        cost_text = Text(cost_str, font_size=TINY_SIZE, color=cost_color)
        cost_text.move_to(RIGHT * 0.5 + UP * y_pos)
        
        row.add(name_text, cost_text)
        row.cost_text = cost_text
        return row
    
    def _step_indicator(self, step_num, description):
        """Create step indicator box."""
        box = VGroup()
        bg = RoundedRectangle(width=4, height=0.8, corner_radius=0.1,
                             fill_color=NODE_PROCESSING, fill_opacity=0.3,
                             stroke_color=NODE_PROCESSING, stroke_width=2)
        
        step_text = Text(f"STEP {step_num}", font_size=SMALL_SIZE, 
                        color=NODE_PROCESSING, weight=BOLD)
        desc_text = Text(description, font_size=TINY_SIZE, color=TEXT_SECONDARY)
        
        step_text.move_to(bg.get_center() + UP * 0.15)
        desc_text.move_to(bg.get_center() + DOWN * 0.15)
        
        box.add(bg, step_text, desc_text)
        return box
    
    # ==================== SCENE 1: BFS vs DIJKSTRA ====================
    
    def _intro_scene(self):
        """Introduction comparing BFS and Dijkstra's."""
        # Title
        title = Text("Chapter 7: Dijkstra's Algorithm", font_size=TITLE_SIZE, color=TEXT_PRIMARY)
        title.move_to(UP * 2.5)
        self.play(Write(title), run_time=SLOW)
        self.wait(PAUSE)
        
        subtitle = Text("Finding Shortest Weighted Paths", font_size=SUBTITLE_SIZE, color=TEXT_ACCENT)
        subtitle.next_to(title, DOWN, buff=0.4)
        self.play(FadeIn(subtitle, shift=UP * 0.3), run_time=NORMAL)
        self.wait(PAUSE)
        
        self.play(
            title.animate.scale(0.6).move_to(UP * 3.3),
            FadeOut(subtitle),
            run_time=NORMAL
        )
        
        # Problem setup
        problem = Text("Problem: Find the FASTEST route", font_size=BODY_SIZE, color=TEXT_SECONDARY)
        problem.move_to(UP * 2.3)
        self.play(Write(problem), run_time=FAST)
        
        # Create simple graph with times
        start = self._node("S", LEFT * 3, NODE_START)
        a_node = self._node("A", UP * 1, NODE_DEFAULT)
        b_node = self._node("B", DOWN * 1, NODE_DEFAULT)
        finish = self._node("F", RIGHT * 3, NODE_FINISH)
        
        nodes = [start, a_node, b_node, finish]
        self.play(LaggedStart(*[FadeIn(n) for n in nodes], lag_ratio=0.1), run_time=NORMAL)
        
        # Edges with travel times
        e_sa = self._weighted_edge(start, a_node, 6)
        e_sb = self._weighted_edge(start, b_node, 2)
        e_ba = self._weighted_edge(b_node, a_node, 3)
        e_af = self._weighted_edge(a_node, finish, 1)
        e_bf = self._weighted_edge(b_node, finish, 5)
        
        edges = [e_sa, e_sb, e_ba, e_af, e_bf]
        self.play(LaggedStart(*[GrowArrow(e.arrow) for e in edges], lag_ratio=0.1), run_time=NORMAL)
        self.play(*[FadeIn(VGroup(e[1], e[2])) for e in edges], run_time=FAST)
        
        self.wait(PAUSE)
        
        # BFS Solution
        bfs_label = Text("BFS: Fewest segments", font_size=LABEL_SIZE, color=NODE_PROCESSING)
        bfs_label.move_to(LEFT * 4.5 + DOWN * 2.5)
        self.play(Write(bfs_label), run_time=FAST)
        
        # BFS path: S → A → F (2 segments)
        self.play(
            e_sa.arrow.animate.set_color(NODE_PROCESSING),
            e_af.arrow.animate.set_color(NODE_PROCESSING),
            run_time=NORMAL
        )
        
        bfs_result = Text("S→A→F: 6+1=7 min", font_size=SMALL_SIZE, color=TEXT_SECONDARY)
        bfs_result.next_to(bfs_label, DOWN, buff=0.2)
        self.play(Write(bfs_result), run_time=FAST)
        self.wait(PAUSE)
        
        # Reset edges
        self.play(
            e_sa.arrow.animate.set_color(EDGE_DEFAULT),
            e_af.arrow.animate.set_color(EDGE_DEFAULT),
            run_time=FAST
        )
        
        # Dijkstra's Solution
        dijk_label = Text("Dijkstra's: Smallest total", font_size=LABEL_SIZE, color=EDGE_PATH)
        dijk_label.move_to(RIGHT * 4.5 + DOWN * 2.5)
        self.play(Write(dijk_label), run_time=FAST)
        
        # Better path: S → B → A → F
        self.play(
            e_sb.arrow.animate.set_color(EDGE_PATH),
            e_ba.arrow.animate.set_color(EDGE_PATH),
            e_af.arrow.animate.set_color(EDGE_PATH),
            run_time=NORMAL
        )
        
        dijk_result = Text("S→B→A→F: 2+3+1=6 min", font_size=SMALL_SIZE, color=EDGE_PATH)
        dijk_result.next_to(dijk_label, DOWN, buff=0.2)
        self.play(Write(dijk_result), run_time=FAST)
        
        # Winner
        winner = Text("Dijkstra's finds faster path!", font_size=BODY_SIZE, color=EDGE_PATH)
        winner.move_to(DOWN * 3.3)
        self.play(Write(winner), run_time=NORMAL)
        self.wait(LONG_PAUSE)
    
    # ==================== SCENE 2: FIRST EXAMPLE ====================
    
    def _first_example_scene(self):
        """Step-by-step Dijkstra walkthrough."""
        title = self._title("Dijkstra's Algorithm")
        self.play(Write(title), run_time=NORMAL)
        
        # Build graph
        start = self._node("Start", LEFT * 4, NODE_START, 0.4)
        a_node = self._node("A", LEFT * 1 + UP * 1.2, NODE_DEFAULT, 0.4)
        b_node = self._node("B", LEFT * 1 + DOWN * 1.2, NODE_DEFAULT, 0.4)
        finish = self._node("Fin", RIGHT * 2, NODE_FINISH, 0.4)
        
        nodes = {"Start": start, "A": a_node, "B": b_node, "Fin": finish}
        
        self.play(LaggedStart(*[FadeIn(n) for n in nodes.values()], lag_ratio=0.1), run_time=NORMAL)
        
        # Edges
        e_sa = self._weighted_edge(start, a_node, 6)
        e_sb = self._weighted_edge(start, b_node, 2)
        e_ba = self._weighted_edge(b_node, a_node, 3)
        e_af = self._weighted_edge(a_node, finish, 1)
        e_bf = self._weighted_edge(b_node, finish, 5)
        
        edges = {"sa": e_sa, "sb": e_sb, "ba": e_ba, "af": e_af, "bf": e_bf}
        
        for e in edges.values():
            self.play(GrowArrow(e.arrow), run_time=INSTANT)
            self.play(FadeIn(VGroup(e[1], e[2])), run_time=INSTANT)
        
        self.wait(PAUSE)
        
        # Cost table
        cost_header = Text("COSTS", font_size=SMALL_SIZE, color=COST_TABLE, weight=BOLD)
        cost_header.move_to(RIGHT * 5 + UP * 2)
        self.play(Write(cost_header), run_time=FAST)
        
        # Initial costs
        costs = {"A": 6, "B": 2, "Fin": "∞"}
        cost_rows = {}
        y = 1.4
        for name, cost in costs.items():
            row = VGroup()
            n_text = Text(name, font_size=TINY_SIZE, color=TEXT_PRIMARY)
            n_text.move_to(RIGHT * 4.5 + UP * y)
            c_text = Text(str(cost), font_size=TINY_SIZE, 
                         color=COST_INFINITY if cost == "∞" else COST_TABLE)
            c_text.move_to(RIGHT * 5.5 + UP * y)
            row.add(n_text, c_text)
            cost_rows[name] = {"row": row, "cost_text": c_text}
            self.play(FadeIn(row), run_time=INSTANT)
            y -= 0.5
        
        self.wait(PAUSE)
        
        # STEP 1: Find cheapest (B)
        step1 = self._step_indicator(1, "Find cheapest")
        step1.move_to(UP * 2.5 + LEFT * 1)
        self.play(FadeIn(step1), run_time=FAST)
        
        self.play(b_node.circle.animate.set_fill(NODE_CHEAPEST), run_time=NORMAL)
        
        cheapest_label = Text("B is cheapest (2)", font_size=SMALL_SIZE, color=NODE_CHEAPEST)
        cheapest_label.move_to(DOWN * 2.5)
        self.play(Write(cheapest_label), run_time=FAST)
        self.wait(PAUSE)
        
        # STEP 2: Update B's neighbors
        self.play(
            step1[1].animate.become(Text("STEP 2", font_size=SMALL_SIZE, color=NODE_PROCESSING, weight=BOLD).move_to(step1[1].get_center())),
            step1[2].animate.become(Text("Update neighbors", font_size=TINY_SIZE, color=TEXT_SECONDARY).move_to(step1[2].get_center())),
            b_node.circle.animate.set_fill(NODE_PROCESSING),
            FadeOut(cheapest_label),
            run_time=FAST
        )
        
        # Check B → A: 2+3=5 < 6
        self.play(e_ba.arrow.animate.set_color(NODE_PROCESSING), run_time=FAST)
        
        calc1 = Text("2 + 3 = 5 < 6 ✓", font_size=SMALL_SIZE, color=COST_IMPROVING)
        calc1.move_to(DOWN * 2.5)
        self.play(Write(calc1), run_time=FAST)
        
        # Update cost
        new_cost_a = Text("5", font_size=TINY_SIZE, color=COST_IMPROVING)
        new_cost_a.move_to(cost_rows["A"]["cost_text"].get_center())
        self.play(
            cost_rows["A"]["cost_text"].animate.set_color(WARNING_RED),
            run_time=FAST
        )
        self.play(
            Transform(cost_rows["A"]["cost_text"], new_cost_a),
            e_ba.arrow.animate.set_color(EDGE_BETTER),
            run_time=FAST
        )
        
        self.play(FadeOut(calc1), run_time=FAST)
        
        # Check B → Fin: 2+5=7 < ∞
        self.play(e_bf.arrow.animate.set_color(NODE_PROCESSING), run_time=FAST)
        
        calc2 = Text("2 + 5 = 7 < ∞ ✓", font_size=SMALL_SIZE, color=COST_IMPROVING)
        calc2.move_to(DOWN * 2.5)
        self.play(Write(calc2), run_time=FAST)
        
        new_cost_f = Text("7", font_size=TINY_SIZE, color=COST_IMPROVING)
        new_cost_f.move_to(cost_rows["Fin"]["cost_text"].get_center())
        self.play(
            Transform(cost_rows["Fin"]["cost_text"], new_cost_f),
            e_bf.arrow.animate.set_color(EDGE_BETTER),
            run_time=FAST
        )
        
        self.play(FadeOut(calc2), run_time=FAST)
        
        # Mark B processed
        self.play(b_node.circle.animate.set_fill(NODE_PROCESSED), run_time=NORMAL)
        
        processed_label = Text("Processed: [B]", font_size=SMALL_SIZE, color=PROCESSED_SET)
        processed_label.move_to(RIGHT * 5 + DOWN * 1)
        self.play(Write(processed_label), run_time=FAST)
        
        self.wait(PAUSE)
        
        # STEP 3: Next cheapest (A)
        self.play(
            step1[1].animate.become(Text("STEP 3", font_size=SMALL_SIZE, color=NODE_PROCESSING, weight=BOLD).move_to(step1[1].get_center())),
            step1[2].animate.become(Text("Repeat", font_size=TINY_SIZE, color=TEXT_SECONDARY).move_to(step1[2].get_center())),
            run_time=FAST
        )
        
        self.play(a_node.circle.animate.set_fill(NODE_CHEAPEST), run_time=NORMAL)
        
        a_label = Text("A is cheapest (5)", font_size=SMALL_SIZE, color=NODE_CHEAPEST)
        a_label.move_to(DOWN * 2.5)
        self.play(Write(a_label), run_time=FAST)
        self.wait(PAUSE)
        
        # Update A's neighbors
        self.play(
            a_node.circle.animate.set_fill(NODE_PROCESSING),
            FadeOut(a_label),
            run_time=FAST
        )
        
        # A → Fin: 5+1=6 < 7
        self.play(e_af.arrow.animate.set_color(NODE_PROCESSING), run_time=FAST)
        
        calc3 = Text("5 + 1 = 6 < 7 ✓", font_size=SMALL_SIZE, color=COST_IMPROVING)
        calc3.move_to(DOWN * 2.5)
        self.play(Write(calc3), run_time=FAST)
        
        final_cost = Text("6", font_size=TINY_SIZE, color=COST_IMPROVING)
        final_cost.move_to(cost_rows["Fin"]["cost_text"].get_center())
        self.play(
            Transform(cost_rows["Fin"]["cost_text"], final_cost),
            e_af.arrow.animate.set_color(EDGE_PATH),
            e_bf.arrow.animate.set_color(EDGE_DEFAULT).set_opacity(0.5),
            run_time=FAST
        )
        
        self.play(FadeOut(calc3), run_time=FAST)
        
        # Mark A processed
        self.play(a_node.circle.animate.set_fill(NODE_PROCESSED), run_time=NORMAL)
        
        new_processed = Text("Processed: [B, A]", font_size=SMALL_SIZE, color=PROCESSED_SET)
        new_processed.move_to(processed_label.get_center())
        self.play(Transform(processed_label, new_processed), run_time=FAST)
        
        # Final
        self.play(finish.circle.animate.set_fill(NODE_PROCESSED), run_time=NORMAL)
        
        final = Text("Final cost to Finish: 6", font_size=BODY_SIZE, color=EDGE_PATH)
        final.move_to(DOWN * 3)
        self.play(Write(final), run_time=NORMAL)
        self.wait(LONG_PAUSE)
    
    # ==================== SCENE 3: PATH TRACING ====================
    
    def _path_tracing_scene(self):
        """Trace path using parent pointers."""
        title = self._title("Tracing the Shortest Path")
        self.play(Write(title), run_time=NORMAL)
        
        concept = Text("Follow parent pointers backwards", font_size=BODY_SIZE, color=TEXT_SECONDARY)
        concept.move_to(UP * 2.2)
        self.play(Write(concept), run_time=FAST)
        
        # Parent table
        parent_header = Text("PARENTS", font_size=SMALL_SIZE, color=PARENT_TABLE, weight=BOLD)
        parent_header.move_to(UP * 1)
        self.play(Write(parent_header), run_time=FAST)
        
        parents = [
            ("Fin", "← A"),
            ("A", "← B"),
            ("B", "← Start"),
        ]
        
        parent_rows = VGroup()
        for node, parent in parents:
            row = Text(f"{node} {parent}", font_size=LABEL_SIZE, color=TEXT_PRIMARY)
            parent_rows.add(row)
        parent_rows.arrange(DOWN, buff=0.3)
        parent_rows.next_to(parent_header, DOWN, buff=0.4)
        
        self.play(LaggedStart(*[Write(r) for r in parent_rows], lag_ratio=0.3), run_time=NORMAL)
        self.wait(PAUSE)
        
        # Trace backwards
        trace_label = Text("Trace: Fin → A → B → Start", font_size=BODY_SIZE, color=EDGE_PATH)
        trace_label.move_to(DOWN * 1.5)
        self.play(Write(trace_label), run_time=NORMAL)
        
        # Reverse for final path
        final_path = Text("Path: Start → B → A → Fin", font_size=BODY_SIZE, color=EDGE_PATH)
        final_path.move_to(DOWN * 2.5)
        self.play(Write(final_path), run_time=NORMAL)
        
        cost_label = Text("Total cost: 2 + 3 + 1 = 6", font_size=LABEL_SIZE, color=COST_TABLE)
        cost_label.move_to(DOWN * 3.3)
        self.play(Write(cost_label), run_time=FAST)
        self.wait(LONG_PAUSE)
    
    # ==================== SCENE 4: TRADING EXAMPLE ====================
    
    def _trading_scene(self):
        """Piano trading example."""
        title = self._title("Trading for a Piano")
        self.play(Write(title), run_time=NORMAL)
        
        story = Text("Rama wants to trade his book for a piano", 
                    font_size=BODY_SIZE, color=TEXT_SECONDARY)
        story.move_to(UP * 2.2)
        self.play(Write(story), run_time=FAST)
        
        # Simplified graph
        book = self._node("Book", LEFT * 5, NODE_START, 0.35)
        poster = self._node("Post", LEFT * 2 + UP * 1.2, NODE_DEFAULT, 0.35)
        lp = self._node("LP", LEFT * 2 + DOWN * 1.2, NODE_DEFAULT, 0.35)
        guitar = self._node("Guit", RIGHT * 1 + UP * 1.2, NODE_DEFAULT, 0.35)
        drums = self._node("Drum", RIGHT * 1 + DOWN * 1.2, NODE_DEFAULT, 0.35)
        piano = self._node("Piano", RIGHT * 4, NODE_FINISH, 0.35)
        
        nodes = [book, poster, lp, guitar, drums, piano]
        self.play(LaggedStart(*[FadeIn(n) for n in nodes], lag_ratio=0.08), run_time=NORMAL)
        
        # Edges with costs ($)
        edges_data = [
            (book, poster, "$0"), (book, lp, "$5"),
            (poster, guitar, "$30"), (poster, drums, "$35"),
            (lp, guitar, "$15"), (lp, drums, "$20"),
            (guitar, piano, "$20"), (drums, piano, "$10")
        ]
        
        edge_objs = []
        for n1, n2, cost in edges_data:
            e = VGroup()
            arrow = Arrow(n1.get_center(), n2.get_center(), color=EDGE_DEFAULT,
                         stroke_width=3, buff=0.4, max_tip_length_to_length_ratio=0.08)
            mid = (n1.get_center() + n2.get_center()) / 2
            cost_label = Text(cost, font_size=14, color=COST_IMPROVING)
            cost_label.move_to(mid)
            e.add(arrow, cost_label)
            edge_objs.append(e)
        
        self.play(
            LaggedStart(*[GrowArrow(e[0]) for e in edge_objs], lag_ratio=0.05),
            run_time=NORMAL
        )
        self.play(*[FadeIn(e[1]) for e in edge_objs], run_time=FAST)
        
        self.wait(PAUSE)
        
        # Quick algorithm trace
        steps = [
            ("Poster cheapest ($0)", poster, NODE_CHEAPEST),
            ("Process Poster", poster, NODE_PROCESSED),
            ("LP next ($5)", lp, NODE_CHEAPEST),
            ("Process LP", lp, NODE_PROCESSED),
            ("Guitar ($20 via LP)", guitar, NODE_CHEAPEST),
            ("Process Guitar", guitar, NODE_PROCESSED),
            ("Drums ($25 via LP)", drums, NODE_CHEAPEST),
            ("Process Drums", drums, NODE_PROCESSED),
        ]
        
        status = Text("", font_size=SMALL_SIZE, color=TEXT_ACCENT)
        status.move_to(DOWN * 2.5)
        
        for text, node, color in steps:
            new_status = Text(text, font_size=SMALL_SIZE, color=color)
            new_status.move_to(DOWN * 2.5)
            self.play(
                node.circle.animate.set_fill(color),
                Transform(status, new_status),
                run_time=FAST
            )
            self.wait(0.3)
        
        # Final path
        self.play(piano.circle.animate.set_fill(NODE_PROCESSED), run_time=FAST)
        
        # Highlight final path: Book → LP → Drums → Piano
        final = Text("Best: Book→LP→Drums→Piano = $35", font_size=BODY_SIZE, color=EDGE_PATH)
        final.move_to(DOWN * 3.2)
        self.play(
            edge_objs[1][0].animate.set_color(EDGE_PATH),  # Book→LP
            edge_objs[5][0].animate.set_color(EDGE_PATH),  # LP→Drums
            edge_objs[7][0].animate.set_color(EDGE_PATH),  # Drums→Piano
            Write(final),
            run_time=NORMAL
        )
        self.wait(LONG_PAUSE)
    
    # ==================== SCENE 5: NEGATIVE WEIGHTS ====================
    
    def _negative_weights_scene(self):
        """Warning about negative weight edges."""
        title = self._title("⚠️ Negative Weights Problem")
        self.play(Write(title), run_time=NORMAL)
        
        warning = Text("Dijkstra's algorithm FAILS with negative weights!", 
                      font_size=BODY_SIZE, color=WARNING_RED)
        warning.move_to(UP * 2.2)
        self.play(Write(warning), run_time=FAST)
        
        # Example
        a = self._node("A", LEFT * 2, NODE_START, 0.4)
        b = self._node("B", RIGHT * 2 + UP * 1, NODE_DEFAULT, 0.4)
        c = self._node("C", RIGHT * 2 + DOWN * 1, NODE_DEFAULT, 0.4)
        
        self.play(FadeIn(a), FadeIn(b), FadeIn(c), run_time=FAST)
        
        # Edges
        e_ab = self._weighted_edge(a, b, 5)
        e_ac = self._weighted_edge(a, c, 2)
        
        # Negative edge B → C
        e_bc = VGroup()
        arrow = Arrow(b.get_center(), c.get_center(), color=EDGE_NEGATIVE,
                     stroke_width=4, buff=0.45, max_tip_length_to_length_ratio=0.1)
        mid = (b.get_center() + c.get_center()) / 2
        badge = Circle(radius=0.22, fill_color=BACKGROUND_COLOR, fill_opacity=0.95,
                      stroke_color=EDGE_NEGATIVE, stroke_width=2)
        badge.move_to(mid)
        neg_label = Text("-3", font_size=WEIGHT_LABEL_SIZE, color=EDGE_NEGATIVE)
        neg_label.move_to(mid)
        e_bc.add(arrow, badge, neg_label)
        
        self.play(
            GrowArrow(e_ab.arrow), FadeIn(VGroup(e_ab[1], e_ab[2])),
            GrowArrow(e_ac.arrow), FadeIn(VGroup(e_ac[1], e_ac[2])),
            GrowArrow(e_bc[0]), FadeIn(VGroup(e_bc[1], e_bc[2])),
            run_time=NORMAL
        )
        
        self.wait(PAUSE)
        
        # Dijkstra's result
        dijk_result = Text("Dijkstra says: A→C costs 2", font_size=LABEL_SIZE, color=TEXT_ACCENT)
        dijk_result.move_to(DOWN * 1.5)
        self.play(Write(dijk_result), run_time=FAST)
        
        # Better path
        better = Text("But A→B→C = 5+(-3) = 2 ... same?", font_size=LABEL_SIZE, color=TEXT_SECONDARY)
        better.move_to(DOWN * 2.2)
        self.play(Write(better), run_time=FAST)
        
        # The real problem
        problem = Text("Problem: C might be processed before better path found!", 
                      font_size=SMALL_SIZE, color=WARNING_RED)
        problem.move_to(DOWN * 3)
        self.play(Write(problem), run_time=NORMAL)
        
        self.wait(PAUSE)
        
        # Solution
        solution = Text("Use Bellman-Ford for negative weights", 
                       font_size=BODY_SIZE, color=PROCESSED_SET)
        solution.move_to(DOWN * 3.5)
        self.play(Write(solution), run_time=NORMAL)
        self.wait(LONG_PAUSE)
    
    # ==================== SCENE 6: APPLICATIONS ====================
    
    def _applications_scene(self):
        """Real-world applications."""
        title = self._title("Applications of Dijkstra's")
        self.play(Write(title), run_time=NORMAL)
        
        apps = [
            ("🗺️ GPS Navigation", "Shortest driving route", EDGE_PATH),
            ("🌐 Network Routing", "Fastest data path (OSPF)", NODE_PROCESSING),
            ("✈️ Flight Planning", "Cheapest multi-leg route", COST_TABLE),
            ("🎮 Game AI", "Pathfinding for characters", PARENT_TABLE),
        ]
        
        items = VGroup()
        for icon_name, desc, color in apps:
            name_text = Text(icon_name, font_size=LABEL_SIZE, color=color)
            desc_text = Text(f"→ {desc}", font_size=SMALL_SIZE, color=TEXT_SECONDARY)
            desc_text.next_to(name_text, RIGHT, buff=0.3)
            row = VGroup(name_text, desc_text)
            items.add(row)
        
        items.arrange(DOWN, buff=0.5, aligned_edge=LEFT)
        items.move_to(UP * 0.3)
        
        self.play(
            LaggedStart(*[FadeIn(item, shift=LEFT * 0.3) for item in items], lag_ratio=0.2),
            run_time=SLOW
        )
        self.wait(PAUSE)
        
        common = Text("Common theme: Minimize total cost/time/distance", 
                     font_size=BODY_SIZE, color=TEXT_ACCENT)
        common.move_to(DOWN * 2.5)
        self.play(Write(common), run_time=NORMAL)
        self.wait(LONG_PAUSE)
    
    # ==================== SCENE 7: SUMMARY ====================
    
    def _summary_scene(self):
        """Key takeaways."""
        title = self._title("Key Takeaways")
        self.play(Write(title), run_time=NORMAL)
        
        takeaways = [
            ("1.", "Dijkstra's finds minimum TOTAL weight path", EDGE_PATH),
            ("2.", "Always process cheapest unprocessed node", NODE_CHEAPEST),
            ("3.", "Update neighbors if better path found", COST_IMPROVING),
            ("4.", "Track parents for path reconstruction", PARENT_TABLE),
            ("5.", "Only works with POSITIVE weights!", WARNING_RED),
        ]
        
        items = VGroup()
        for num, text, color in takeaways:
            num_text = Text(num, font_size=BODY_SIZE, color=TEXT_PRIMARY)
            content = Text(text, font_size=SMALL_SIZE, color=color)
            content.next_to(num_text, RIGHT, buff=0.2)
            row = VGroup(num_text, content)
            items.add(row)
        
        items.arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        items.move_to(UP * 0.3)
        
        self.play(
            LaggedStart(*[FadeIn(item, shift=LEFT * 0.3) for item in items], lag_ratio=0.15),
            run_time=SLOW
        )
        self.wait(PAUSE)
        
        # Comparison
        compare = VGroup(
            Text("BFS → Unweighted (fewest edges)", font_size=LABEL_SIZE, color=NODE_PROCESSING),
            Text("Dijkstra → Weighted (minimum cost)", font_size=LABEL_SIZE, color=EDGE_PATH),
        )
        compare.arrange(DOWN, buff=0.2)
        compare.move_to(DOWN * 2.3)
        
        self.play(Write(compare), run_time=NORMAL)
        
        complexity = Text("Time: O((V+E) log V)", font_size=SMALL_SIZE, color=TEXT_ACCENT)
        complexity.move_to(DOWN * 3.3)
        self.play(Write(complexity), run_time=FAST)
        self.wait(LONG_PAUSE)


# Individual scene classes
class IntroScene(Chapter7Animation):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        self._intro_scene()

class FirstExampleScene(Chapter7Animation):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        self._first_example_scene()

class PathTracingScene(Chapter7Animation):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        self._path_tracing_scene()

class TradingScene(Chapter7Animation):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        self._trading_scene()

class NegativeWeightsScene(Chapter7Animation):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        self._negative_weights_scene()

class ApplicationsScene(Chapter7Animation):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        self._applications_scene()

class SummaryScene(Chapter7Animation):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        self._summary_scene()
