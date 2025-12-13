#!/usr/bin/env python3
"""
Chapter 6: Breadth-First Search
===============================
Educational animation demonstrating BFS, graphs, queues, and shortest paths.
3Blue1Brown-style with smooth motion, clear visuals, and minimal text.

Usage:
    manim -pql main.py Chapter6Animation    # Preview (480p)
    manim -pqh main.py Chapter6Animation    # HD quality (1080p)
"""
import sys
sys.path.insert(0, '/home/hg/Desktop/algorthims/Chapter6_BreadthFirstSearch')

from manim import *

from config.colors import (
    BACKGROUND_COLOR, TEXT_PRIMARY, TEXT_SECONDARY, TEXT_ACCENT,
    NODE_DEFAULT, NODE_ACTIVE, NODE_QUEUED, NODE_VISITED, NODE_TARGET,
    EDGE_DEFAULT, EDGE_ACTIVE, EDGE_PATH, QUEUE_COLOR,
    DEGREE_1, DEGREE_2, DEGREE_3, INFINITE_LOOP, PATH_FOUND, VISITED_LIST
)
from config.fonts import (
    TITLE_SIZE, SUBTITLE_SIZE, HEADING_SIZE, BODY_SIZE,
    LABEL_SIZE, SMALL_SIZE, TINY_SIZE, NODE_LABEL_SIZE
)
from config.animation_constants import (
    INSTANT, FAST, NORMAL, SLOW, PAUSE, LONG_PAUSE,
    TITLE_Y, NODE_RADIUS
)


class Chapter6Animation(Scene):
    """
    Complete Chapter 6 animation covering:
    1. Introduction - Wave exploration concept
    2. What is a Graph - Nodes and edges
    3. BFS - The Mango Seller problem
    4. Finding Shortest Path
    5. Queue Data Structure
    6. Graph as Hash Table
    7. Algorithm Implementation
    8. Running Time Analysis
    9. Topological Sort
    10. Trees vs Graphs
    11. Practical Applications
    12. Summary
    """
    
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        
        self._intro_scene()
        self._clear()
        
        self._what_is_graph_scene()
        self._clear()
        
        self._mango_seller_scene()
        self._clear()
        
        self._shortest_path_scene()
        self._clear()
        
        self._queue_scene()
        self._clear()
        
        self._implementation_scene()
        self._clear()
        
        self._complexity_scene()
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
    
    def _node(self, label, pos=ORIGIN, color=NODE_DEFAULT, radius=0.4):
        grp = VGroup()
        circle = Circle(radius=radius, fill_color=color, fill_opacity=0.9,
                       stroke_color=TEXT_PRIMARY, stroke_width=3)
        circle.move_to(pos)
        lbl = Text(label, font_size=NODE_LABEL_SIZE, color=TEXT_PRIMARY)
        lbl.move_to(circle.get_center())
        grp.add(circle, lbl)
        grp.circle = circle
        grp.label_text = label
        return grp
    
    def _edge(self, n1, n2, directed=True, color=EDGE_DEFAULT):
        if directed:
            return Arrow(n1.get_center(), n2.get_center(), color=color,
                        stroke_width=3, buff=0.45, max_tip_length_to_length_ratio=0.12)
        else:
            return Line(n1.get_center(), n2.get_center(), color=color,
                       stroke_width=3).set_opacity(0.6)
    
    def _queue_card(self, label, color=None):
        color = color or QUEUE_COLOR
        grp = VGroup()
        rect = RoundedRectangle(width=1.0, height=0.45, corner_radius=0.08,
                               fill_color=color, fill_opacity=0.9,
                               stroke_color=TEXT_PRIMARY, stroke_width=2)
        lbl = Text(label, font_size=TINY_SIZE, color=TEXT_PRIMARY)
        lbl.move_to(rect.get_center())
        grp.add(rect, lbl)
        grp.rect = rect
        return grp
    
    # ==================== SCENE 1: INTRODUCTION ====================
    
    def _intro_scene(self):
        """Introduction with wave exploration concept."""
        # Title
        title = Text("Chapter 6: Breadth-First Search", font_size=TITLE_SIZE, color=TEXT_PRIMARY)
        title.move_to(UP * 2)
        self.play(Write(title), run_time=SLOW)
        self.wait(PAUSE)
        
        subtitle = Text("Finding Shortest Paths in Graphs", font_size=SUBTITLE_SIZE, color=TEXT_ACCENT)
        subtitle.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(subtitle, shift=UP * 0.3), run_time=NORMAL)
        self.wait(PAUSE)
        
        self.play(
            title.animate.scale(0.7).move_to(UP * 3.2),
            FadeOut(subtitle),
            run_time=NORMAL
        )
        
        # Core concept: wave exploration
        concept = Text("Explore layer by layer, like ripples in water", 
                      font_size=BODY_SIZE, color=TEXT_SECONDARY)
        concept.move_to(UP * 2.2)
        self.play(Write(concept), run_time=FAST)
        
        # Center node
        center = self._node("Start", ORIGIN, NODE_ACTIVE)
        self.play(FadeIn(center), run_time=FAST)
        
        # Wave 1 - immediate neighbors
        wave1_nodes = []
        wave1_positions = [UP * 1.5, RIGHT * 1.5, DOWN * 1.5, LEFT * 1.5]
        for i, pos in enumerate(wave1_positions):
            node = self._node(f"1°", pos, DEGREE_1, 0.35)
            wave1_nodes.append(node)
        
        wave1_label = Text("1st degree", font_size=SMALL_SIZE, color=DEGREE_1)
        wave1_label.move_to(RIGHT * 3 + UP * 1.5)
        
        # Wave animation
        wave1 = Circle(radius=0.5, color=DEGREE_1, stroke_width=3)
        wave1.move_to(ORIGIN)
        
        self.play(
            Create(wave1),
            wave1.animate.scale(3).set_opacity(0),
            LaggedStart(*[FadeIn(n) for n in wave1_nodes], lag_ratio=0.1),
            Write(wave1_label),
            run_time=NORMAL
        )
        self.remove(wave1)
        
        # Wave 2 - second degree
        wave2_nodes = []
        wave2_positions = [UP * 1.5 + RIGHT * 1.5, RIGHT * 1.5 + DOWN * 1.5,
                          DOWN * 1.5 + LEFT * 1.5, LEFT * 1.5 + UP * 1.5]
        for pos in wave2_positions:
            node = self._node("2°", pos, DEGREE_2, 0.3)
            wave2_nodes.append(node)
        
        wave2_label = Text("2nd degree", font_size=SMALL_SIZE, color=DEGREE_2)
        wave2_label.move_to(RIGHT * 3 + UP * 0.5)
        
        wave2 = Circle(radius=1.5, color=DEGREE_2, stroke_width=3)
        wave2.move_to(ORIGIN)
        
        self.play(
            Create(wave2),
            wave2.animate.scale(2).set_opacity(0),
            LaggedStart(*[FadeIn(n) for n in wave2_nodes], lag_ratio=0.1),
            Write(wave2_label),
            run_time=NORMAL
        )
        self.remove(wave2)
        
        self.wait(PAUSE)
        
        # Key insight
        insight = Text("Closer nodes found first → Shortest path guaranteed!", 
                      font_size=BODY_SIZE, color=PATH_FOUND)
        insight.move_to(DOWN * 2.5)
        self.play(Write(insight), run_time=NORMAL)
        self.wait(LONG_PAUSE)
    
    # ==================== SCENE 2: WHAT IS A GRAPH ====================
    
    def _what_is_graph_scene(self):
        """Explain graph fundamentals."""
        title = self._title("What is a Graph?")
        self.play(Write(title), run_time=NORMAL)
        
        concept = Text("Nodes connected by edges (relationships)", 
                      font_size=BODY_SIZE, color=TEXT_SECONDARY)
        concept.move_to(UP * 2.2)
        self.play(Write(concept), run_time=FAST)
        
        # Create poker debt example
        alex = self._node("Alex", LEFT * 3 + UP * 1, NODE_DEFAULT)
        rama = self._node("Rama", RIGHT * 0 + UP * 1, NODE_DEFAULT)
        tom = self._node("Tom", RIGHT * 3 + UP * 1, NODE_DEFAULT)
        adit = self._node("Adit", RIGHT * 3 + DOWN * 1, NODE_DEFAULT)
        
        nodes = [alex, rama, tom, adit]
        
        self.play(LaggedStart(*[FadeIn(n) for n in nodes], lag_ratio=0.15), run_time=NORMAL)
        self.wait(0.3)
        
        # Edges with explanations
        edge1 = self._edge(alex, rama)
        edge1_label = Text("Alex owes Rama", font_size=SMALL_SIZE, color=TEXT_SECONDARY)
        edge1_label.next_to(edge1, UP, buff=0.1)
        
        self.play(GrowArrow(edge1), Write(edge1_label), run_time=FAST)
        self.wait(0.3)
        self.play(FadeOut(edge1_label), run_time=FAST)
        
        # More edges
        edge2 = self._edge(alex, tom)
        edge3 = self._edge(rama, tom)
        edge4 = self._edge(tom, adit)
        
        self.play(
            GrowArrow(edge2), GrowArrow(edge3), GrowArrow(edge4),
            run_time=NORMAL
        )
        self.wait(PAUSE)
        
        # Labels
        node_label = Text("Nodes (vertices)", font_size=LABEL_SIZE, color=NODE_QUEUED)
        node_label.move_to(LEFT * 4 + DOWN * 1.5)
        
        edge_label = Text("Edges (connections)", font_size=LABEL_SIZE, color=EDGE_ACTIVE)
        edge_label.move_to(LEFT * 4 + DOWN * 2.2)
        
        self.play(Write(node_label), Write(edge_label), run_time=FAST)
        
        # Highlight neighbors concept
        neighbor_text = Text("Rama's neighbors: Alex, Tom", font_size=LABEL_SIZE, color=TEXT_ACCENT)
        neighbor_text.move_to(DOWN * 3)
        
        self.play(
            rama.circle.animate.set_fill(NODE_ACTIVE),
            alex.circle.animate.set_fill(NODE_QUEUED),
            tom.circle.animate.set_fill(NODE_QUEUED),
            Write(neighbor_text),
            run_time=NORMAL
        )
        self.wait(LONG_PAUSE)
    
    # ==================== SCENE 3: MANGO SELLER ====================
    
    def _mango_seller_scene(self):
        """The mango seller search problem."""
        title = self._title("BFS: Finding a Mango Seller")
        self.play(Write(title), run_time=NORMAL)
        
        problem = Text("Search your network for someone who sells mangos", 
                      font_size=BODY_SIZE, color=TEXT_SECONDARY)
        problem.move_to(UP * 2.2)
        self.play(Write(problem), run_time=FAST)
        
        # Build social network
        you = self._node("You", LEFT * 4, NODE_ACTIVE)
        alice = self._node("Alice", LEFT * 1.5 + UP * 1.5, NODE_DEFAULT)
        bob = self._node("Bob", LEFT * 1.5, NODE_DEFAULT)
        claire = self._node("Claire", LEFT * 1.5 + DOWN * 1.5, NODE_DEFAULT)
        peggy = self._node("Peggy", RIGHT * 1 + UP * 1, NODE_DEFAULT)
        anuj = self._node("Anuj", RIGHT * 1, NODE_DEFAULT)
        thom = self._node("Thom", RIGHT * 1 + DOWN * 1, NODE_DEFAULT)  # Mango seller!
        jonny = self._node("Jonny", RIGHT * 1 + DOWN * 2, NODE_DEFAULT)
        
        nodes = {"you": you, "alice": alice, "bob": bob, "claire": claire,
                "peggy": peggy, "anuj": anuj, "thom": thom, "jonny": jonny}
        
        # Edges
        edges = [
            (you, alice), (you, bob), (you, claire),
            (alice, peggy), (bob, anuj), (bob, peggy),
            (claire, thom), (claire, jonny)
        ]
        
        edge_objs = []
        for n1, n2 in edges:
            e = self._edge(n1, n2)
            edge_objs.append(e)
        
        self.play(
            LaggedStart(*[FadeIn(n) for n in nodes.values()], lag_ratio=0.08),
            run_time=NORMAL
        )
        self.play(
            LaggedStart(*[GrowArrow(e) for e in edge_objs], lag_ratio=0.05),
            run_time=NORMAL
        )
        self.wait(PAUSE)
        
        # Queue visualization
        queue_label = Text("Queue", font_size=LABEL_SIZE, color=QUEUE_COLOR)
        queue_label.move_to(RIGHT * 5 + UP * 2)
        self.play(Write(queue_label), run_time=FAST)
        
        queue_pos = RIGHT * 5 + UP * 1.3
        
        # Add initial neighbors to queue
        cards = []
        for name in ["Alice", "Bob", "Claire"]:
            card = self._queue_card(name)
            if not cards:
                card.move_to(queue_pos)
            else:
                card.next_to(cards[-1], DOWN, buff=0.1)
            cards.append(card)
        
        self.play(
            LaggedStart(*[FadeIn(c, shift=LEFT * 0.3) for c in cards], lag_ratio=0.15),
            alice.circle.animate.set_fill(NODE_QUEUED),
            bob.circle.animate.set_fill(NODE_QUEUED),
            claire.circle.animate.set_fill(NODE_QUEUED),
            run_time=NORMAL
        )
        self.wait(PAUSE)
        
        # Process Alice
        check_label = Text("Check Alice...", font_size=SMALL_SIZE, color=TEXT_ACCENT)
        check_label.move_to(DOWN * 2.5)
        
        self.play(
            cards[0].animate.shift(LEFT * 0.5).set_opacity(0),
            alice.circle.animate.set_fill(NODE_ACTIVE),
            Write(check_label),
            run_time=FAST
        )
        
        not_seller = Text("Not a seller", font_size=SMALL_SIZE, color=TEXT_SECONDARY)
        not_seller.next_to(check_label, RIGHT, buff=0.3)
        self.play(
            Write(not_seller),
            alice.circle.animate.set_fill(NODE_VISITED),
            run_time=FAST
        )
        
        # Add Peggy
        peggy_card = self._queue_card("Peggy")
        peggy_card.next_to(cards[-1], DOWN, buff=0.1)
        self.play(
            FadeIn(peggy_card, shift=LEFT * 0.3),
            peggy.circle.animate.set_fill(NODE_QUEUED),
            run_time=FAST
        )
        cards.append(peggy_card)
        
        self.play(FadeOut(check_label), FadeOut(not_seller), run_time=FAST)
        
        # Process Bob
        check_label = Text("Check Bob...", font_size=SMALL_SIZE, color=TEXT_ACCENT)
        check_label.move_to(DOWN * 2.5)
        
        self.play(
            cards[1].animate.shift(LEFT * 0.5).set_opacity(0),
            bob.circle.animate.set_fill(NODE_ACTIVE),
            Write(check_label),
            run_time=FAST
        )
        self.play(
            bob.circle.animate.set_fill(NODE_VISITED),
            run_time=FAST
        )
        
        # Add Anuj
        anuj_card = self._queue_card("Anuj")
        anuj_card.next_to(cards[-1], DOWN, buff=0.1)
        self.play(
            FadeIn(anuj_card, shift=LEFT * 0.3),
            anuj.circle.animate.set_fill(NODE_QUEUED),
            run_time=FAST
        )
        cards.append(anuj_card)
        
        self.play(FadeOut(check_label), run_time=FAST)
        
        # Process Claire → finds Thom!
        check_label = Text("Check Claire...", font_size=SMALL_SIZE, color=TEXT_ACCENT)
        check_label.move_to(DOWN * 2.5)
        
        self.play(
            cards[2].animate.shift(LEFT * 0.5).set_opacity(0),
            claire.circle.animate.set_fill(NODE_ACTIVE),
            Write(check_label),
            run_time=FAST
        )
        self.play(claire.circle.animate.set_fill(NODE_VISITED), run_time=FAST)
        
        # Add Thom and Jonny
        thom_card = self._queue_card("Thom")
        jonny_card = self._queue_card("Jonny")
        thom_card.next_to(cards[-1], DOWN, buff=0.1)
        jonny_card.next_to(thom_card, DOWN, buff=0.1)
        
        self.play(
            FadeIn(thom_card), FadeIn(jonny_card),
            thom.circle.animate.set_fill(NODE_QUEUED),
            jonny.circle.animate.set_fill(NODE_QUEUED),
            run_time=FAST
        )
        
        self.play(FadeOut(check_label), run_time=FAST)
        
        # Check Thom - FOUND!
        check_label = Text("Check Thom...", font_size=SMALL_SIZE, color=TEXT_ACCENT)
        check_label.move_to(DOWN * 2.5)
        
        self.play(
            thom.circle.animate.set_fill(NODE_ACTIVE),
            Write(check_label),
            run_time=FAST
        )
        
        found = Text("MANGO SELLER FOUND!", font_size=BODY_SIZE, color=NODE_TARGET)
        found.move_to(DOWN * 3.1)
        
        self.play(
            thom.circle.animate.set_fill(NODE_TARGET).scale(1.3),
            Write(found),
            run_time=NORMAL
        )
        
        # Highlight path
        path_label = Text("Path: You → Claire → Thom (2 hops)", 
                         font_size=LABEL_SIZE, color=PATH_FOUND)
        path_label.move_to(DOWN * 3.7)
        
        self.play(
            edge_objs[2].animate.set_color(PATH_FOUND),  # you→claire
            edge_objs[6].animate.set_color(PATH_FOUND),  # claire→thom
            Write(path_label),
            run_time=NORMAL
        )
        self.wait(LONG_PAUSE)
    
    # ==================== SCENE 4: SHORTEST PATH ====================
    
    def _shortest_path_scene(self):
        """Why BFS finds shortest path."""
        title = self._title("Why BFS Finds Shortest Path")
        self.play(Write(title), run_time=NORMAL)
        
        # Key insight
        insight = Text("1st degree checked BEFORE 2nd degree", 
                      font_size=BODY_SIZE, color=TEXT_SECONDARY)
        insight.move_to(UP * 2.2)
        self.play(Write(insight), run_time=FAST)
        
        # Visual queue order
        queue_visual = VGroup()
        
        # 1st degree section
        first_deg = VGroup()
        for name in ["Alice", "Bob", "Claire"]:
            card = self._queue_card(name, DEGREE_1)
            first_deg.add(card)
        first_deg.arrange(RIGHT, buff=0.1)
        
        first_label = Text("1st degree", font_size=TINY_SIZE, color=DEGREE_1)
        first_label.next_to(first_deg, UP, buff=0.1)
        
        # 2nd degree section
        second_deg = VGroup()
        for name in ["Peggy", "Anuj", "Thom"]:
            card = self._queue_card(name, DEGREE_2)
            second_deg.add(card)
        second_deg.arrange(RIGHT, buff=0.1)
        second_deg.next_to(first_deg, RIGHT, buff=0.3)
        
        second_label = Text("2nd degree", font_size=TINY_SIZE, color=DEGREE_2)
        second_label.next_to(second_deg, UP, buff=0.1)
        
        queue_visual.add(first_deg, first_label, second_deg, second_label)
        queue_visual.move_to(UP * 0.5)
        
        # Front/back labels
        front = Text("Front →", font_size=TINY_SIZE, color=TEXT_SECONDARY)
        front.next_to(first_deg, LEFT, buff=0.2)
        back = Text("← Back", font_size=TINY_SIZE, color=TEXT_SECONDARY)
        back.next_to(second_deg, RIGHT, buff=0.2)
        
        self.play(FadeIn(queue_visual), Write(front), Write(back), run_time=NORMAL)
        self.wait(PAUSE)
        
        # Explanation
        explain1 = Text("Queue order guarantees:", font_size=LABEL_SIZE, color=TEXT_PRIMARY)
        explain1.move_to(DOWN * 1)
        
        explain2 = Text("Closer connections checked first!", font_size=LABEL_SIZE, color=PATH_FOUND)
        explain2.next_to(explain1, DOWN, buff=0.2)
        
        self.play(Write(explain1), run_time=FAST)
        self.play(Write(explain2), run_time=FAST)
        
        # Key rule
        rule = Text("Must search in order added to queue", 
                   font_size=BODY_SIZE, color=TEXT_ACCENT)
        rule.move_to(DOWN * 2.5)
        self.play(Write(rule), run_time=NORMAL)
        self.wait(LONG_PAUSE)
    
    # ==================== SCENE 5: QUEUE ====================
    
    def _queue_scene(self):
        """Queue data structure deep dive."""
        title = self._title("Queue: First In, First Out (FIFO)")
        self.play(Write(title), run_time=NORMAL)
        
        # Visual queue
        queue_box = Rectangle(width=6, height=1.2, fill_color=QUEUE_COLOR,
                             fill_opacity=0.2, stroke_color=QUEUE_COLOR, stroke_width=3)
        queue_box.move_to(UP * 0.5)
        
        front_label = Text("Front", font_size=SMALL_SIZE, color=TEXT_PRIMARY)
        front_label.next_to(queue_box, LEFT, buff=0.3)
        
        back_label = Text("Back", font_size=SMALL_SIZE, color=TEXT_PRIMARY)
        back_label.next_to(queue_box, RIGHT, buff=0.3)
        
        self.play(Create(queue_box), Write(front_label), Write(back_label), run_time=NORMAL)
        
        # Enqueue demonstration
        items = ["A", "B", "C", "D"]
        cards = []
        
        for i, item in enumerate(items):
            card = self._queue_card(item)
            if not cards:
                card.move_to(queue_box.get_left() + RIGHT * 0.7)
            else:
                card.next_to(cards[-1], RIGHT, buff=0.15)
            
            enqueue_text = Text(f"Enqueue '{item}'", font_size=SMALL_SIZE, color=TEXT_ACCENT)
            enqueue_text.move_to(DOWN * 1)
            
            self.play(
                FadeIn(card, shift=DOWN * 0.3),
                Write(enqueue_text),
                run_time=FAST
            )
            cards.append(card)
            self.play(FadeOut(enqueue_text), run_time=INSTANT)
        
        self.wait(PAUSE)
        
        # Dequeue demonstration
        dequeue_label = Text("Dequeue removes from FRONT", font_size=LABEL_SIZE, color=TEXT_ACCENT)
        dequeue_label.move_to(DOWN * 1.5)
        self.play(Write(dequeue_label), run_time=FAST)
        
        for i in range(2):
            card = cards[0]
            result = Text(f"→ '{items[i]}'", font_size=SMALL_SIZE, color=PATH_FOUND)
            result.move_to(DOWN * 2.2)
            
            self.play(
                card.animate.shift(LEFT * 1.5).set_opacity(0),
                Write(result),
                run_time=FAST
            )
            cards.pop(0)
            
            # Shift remaining
            for j, c in enumerate(cards):
                target = queue_box.get_left() + RIGHT * (0.7 + j * 1.15)
                self.play(c.animate.move_to(target), run_time=FAST)
            
            self.play(FadeOut(result), run_time=FAST)
        
        # FIFO summary
        fifo = Text("Same order in = Same order out", font_size=BODY_SIZE, color=TEXT_ACCENT)
        fifo.move_to(DOWN * 2.8)
        self.play(Write(fifo), run_time=NORMAL)
        self.wait(LONG_PAUSE)
    
    # ==================== SCENE 6: IMPLEMENTATION ====================
    
    def _implementation_scene(self):
        """Graph implementation as hash table."""
        title = self._title("Graph as Hash Table")
        self.play(Write(title), run_time=NORMAL)
        
        # Code
        code_lines = [
            'graph = {}',
            'graph["you"] = ["alice", "bob"]',
            'graph["alice"] = ["peggy"]',
            'graph["bob"] = ["anuj"]',
        ]
        
        code = VGroup()
        for line in code_lines:
            t = Text(line, font_size=SMALL_SIZE, color=TEXT_PRIMARY)
            code.add(t)
        code.arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        code.move_to(LEFT * 3 + UP * 0.5)
        
        self.play(
            LaggedStart(*[Write(c) for c in code], lag_ratio=0.3),
            run_time=SLOW
        )
        self.wait(PAUSE)
        
        # Visual graph
        you = self._node("You", RIGHT * 2 + UP * 1, NODE_ACTIVE, 0.35)
        alice = self._node("Alice", RIGHT * 4 + UP * 1.5, NODE_DEFAULT, 0.35)
        bob = self._node("Bob", RIGHT * 4 + UP * 0.5, NODE_DEFAULT, 0.35)
        peggy = self._node("Peggy", RIGHT * 5.5 + UP * 1.5, NODE_DEFAULT, 0.35)
        anuj = self._node("Anuj", RIGHT * 5.5 + UP * 0.5, NODE_DEFAULT, 0.35)
        
        nodes = [you, alice, bob, peggy, anuj]
        
        self.play(LaggedStart(*[FadeIn(n) for n in nodes], lag_ratio=0.1), run_time=NORMAL)
        
        # Edges
        e1 = self._edge(you, alice)
        e2 = self._edge(you, bob)
        e3 = self._edge(alice, peggy)
        e4 = self._edge(bob, anuj)
        
        self.play(
            GrowArrow(e1), GrowArrow(e2), GrowArrow(e3), GrowArrow(e4),
            run_time=NORMAL
        )
        
        # Connection lines
        connect = Text("Hash table → Graph", font_size=LABEL_SIZE, color=TEXT_ACCENT)
        connect.move_to(DOWN * 2)
        self.play(Write(connect), run_time=FAST)
        
        # Directed note
        directed = Text("Arrows = Directed edges (one-way)", font_size=SMALL_SIZE, color=TEXT_SECONDARY)
        directed.move_to(DOWN * 2.7)
        self.play(Write(directed), run_time=FAST)
        self.wait(LONG_PAUSE)
    
    # ==================== SCENE 7: COMPLEXITY ====================
    
    def _complexity_scene(self):
        """Running time analysis."""
        title = self._title("Running Time: O(V + E)")
        self.play(Write(title), run_time=NORMAL)
        
        # Explanation
        v_explain = VGroup(
            Text("V = Vertices (nodes)", font_size=LABEL_SIZE, color=NODE_QUEUED),
            Text("Each node added to queue once", font_size=SMALL_SIZE, color=TEXT_SECONDARY),
        )
        v_explain.arrange(DOWN, buff=0.1, aligned_edge=LEFT)
        v_explain.move_to(LEFT * 2 + UP * 1)
        
        e_explain = VGroup(
            Text("E = Edges (connections)", font_size=LABEL_SIZE, color=EDGE_ACTIVE),
            Text("Each edge followed once", font_size=SMALL_SIZE, color=TEXT_SECONDARY),
        )
        e_explain.arrange(DOWN, buff=0.1, aligned_edge=LEFT)
        e_explain.move_to(LEFT * 2 + DOWN * 0.5)
        
        self.play(Write(v_explain), run_time=NORMAL)
        self.play(Write(e_explain), run_time=NORMAL)
        self.wait(PAUSE)
        
        # Formula
        formula = Text("Total: O(V + E) = Linear time!", font_size=BODY_SIZE, color=PATH_FOUND)
        formula.move_to(DOWN * 2)
        self.play(Write(formula), run_time=NORMAL)
        
        # Example
        example = Text("8 people + 10 connections = O(18) operations", 
                      font_size=LABEL_SIZE, color=TEXT_ACCENT)
        example.move_to(DOWN * 2.8)
        self.play(Write(example), run_time=FAST)
        self.wait(LONG_PAUSE)
    
    # ==================== SCENE 8: APPLICATIONS ====================
    
    def _applications_scene(self):
        """Practical applications."""
        title = self._title("BFS Applications")
        self.play(Write(title), run_time=NORMAL)
        
        apps = [
            ("Social Networks", "Find closest connection", DEGREE_1),
            ("GPS Navigation", "Shortest route", PATH_FOUND),
            ("Web Crawlers", "Explore pages by depth", EDGE_ACTIVE),
            ("Spell Checkers", "Minimum edit distance", TEXT_ACCENT),
        ]
        
        items = VGroup()
        for name, desc, color in apps:
            name_text = Text(name, font_size=LABEL_SIZE, color=color)
            desc_text = Text(f"→ {desc}", font_size=SMALL_SIZE, color=TEXT_SECONDARY)
            desc_text.next_to(name_text, RIGHT, buff=0.3)
            row = VGroup(name_text, desc_text)
            items.add(row)
        
        items.arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        items.move_to(UP * 0.3)
        
        self.play(
            LaggedStart(*[FadeIn(item, shift=LEFT * 0.3) for item in items], lag_ratio=0.2),
            run_time=SLOW
        )
        self.wait(PAUSE)
        
        common = Text("Common thread: Finding shortest path!", 
                     font_size=BODY_SIZE, color=TEXT_ACCENT)
        common.move_to(DOWN * 2.5)
        self.play(Write(common), run_time=NORMAL)
        self.wait(LONG_PAUSE)
    
    # ==================== SCENE 9: SUMMARY ====================
    
    def _summary_scene(self):
        """Final summary."""
        title = self._title("Key Takeaways")
        self.play(Write(title), run_time=NORMAL)
        
        takeaways = [
            ("1.", "BFS explores layer by layer (breadth-first)", NODE_ACTIVE),
            ("2.", "Uses Queue (FIFO) to maintain order", QUEUE_COLOR),
            ("3.", "Guarantees shortest path", PATH_FOUND),
            ("4.", "Track visited nodes to avoid loops", VISITED_LIST),
            ("5.", "Time complexity: O(V + E)", TEXT_ACCENT),
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
        
        # Visual reminder
        reminder = VGroup(
            Text("BFS = Queue + Visited tracking", font_size=BODY_SIZE, color=TEXT_PRIMARY),
            Text("→ Shortest path finder!", font_size=LABEL_SIZE, color=PATH_FOUND),
        )
        reminder.arrange(DOWN, buff=0.2)
        reminder.move_to(DOWN * 2.3)
        
        self.play(Write(reminder), run_time=NORMAL)
        self.wait(LONG_PAUSE)


# Individual scene classes (inherit from Chapter6Animation for helper methods)
class IntroScene(Chapter6Animation):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        self._intro_scene()

class GraphScene(Chapter6Animation):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        self._what_is_graph_scene()

class MangoSellerScene(Chapter6Animation):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        self._mango_seller_scene()

class ShortestPathScene(Chapter6Animation):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        self._shortest_path_scene()

class QueueScene(Chapter6Animation):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        self._queue_scene()

class ImplementationScene(Chapter6Animation):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        self._implementation_scene()

class ComplexityScene(Chapter6Animation):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        self._complexity_scene()

class ApplicationsScene(Chapter6Animation):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        self._applications_scene()

class SummaryScene(Chapter6Animation):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        self._summary_scene()
