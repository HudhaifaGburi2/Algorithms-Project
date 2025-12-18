#!/usr/bin/env python3
"""
Bellman-Ford Algorithm Animation
================================
Educational animation demonstrating the Bellman-Ford algorithm for shortest paths.
Handles negative weights and detects negative cycles.
3Blue1Brown-style with smooth motion, clear visuals, and systematic edge processing.

Usage:
    manim -pql main.py BellmanFordAnimation    # Full animation (480p)
    manim -pqh main.py BellmanFordAnimation    # HD quality (1080p)
    
Individual Scenes:
    manim -pql main.py Scene1_WhyNotDijkstra
    manim -pql main.py Scene2_AlgorithmOverview
    manim -pql main.py Scene3_StepByStep
    manim -pql main.py Scene4_NegativeCycle
    manim -pql main.py Scene5_WhyVMinus1
    manim -pql main.py Scene6_Implementation
    manim -pql main.py Scene7_Comparison
    manim -pql main.py Scene8_Applications
    manim -pql main.py Scene9_Complexity
    manim -pql main.py Scene10_Recap
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))

from manim import *

from config.colors import *
from config.fonts import *
from config.animation_constants import *

# Import individual scenes for standalone rendering
from scenes.scene1_why_not_dijkstra import Scene1_WhyNotDijkstra
from scenes.scene2_algorithm_overview import Scene2_AlgorithmOverview
from scenes.scene3_step_by_step import Scene3_StepByStep
from scenes.scene4_negative_cycle import Scene4_NegativeCycle
from scenes.scene5_why_v_minus_1 import Scene5_WhyVMinus1
from scenes.scene6_implementation import Scene6_Implementation
from scenes.scene7_comparison import Scene7_Comparison
from scenes.scene8_applications import Scene8_Applications
from scenes.scene9_complexity import Scene9_Complexity
from scenes.scene10_recap import Scene10_Recap


class BellmanFordAnimation(Scene):
    """
    Complete Bellman-Ford animation covering all 10 scenes.
    Run individual scenes separately for faster iteration.
    """
    
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        
        self._scene1_why_not_dijkstra()
        self._clear()
        
        self._scene2_overview()
        self._clear()
        
        self._scene3_step_by_step()
        self._clear()
        
        self._scene4_negative_cycle()
        self._clear()
        
        self._scene5_why_v_minus_1()
        self._clear()
        
        self._scene6_implementation()
        self._clear()
        
        self._scene7_comparison()
        self._clear()
        
        self._scene8_applications()
        self._clear()
        
        self._scene9_complexity()
        self._clear()
        
        self._scene10_recap()
    
    def _clear(self):
        if self.mobjects:
            self.play(*[FadeOut(m) for m in self.mobjects], run_time=FAST)
        self.wait(0.2)
    
    def _node(self, label, pos=ORIGIN, color=NODE_DEFAULT, radius=0.45):
        grp = VGroup()
        circle = Circle(radius=radius, fill_color=color, fill_opacity=0.9,
                       stroke_color=TEXT_PRIMARY, stroke_width=3)
        circle.move_to(pos)
        lbl = Text(str(label), font_size=NODE_LABEL_SIZE, color=TEXT_PRIMARY)
        lbl.move_to(circle.get_center())
        grp.add(circle, lbl)
        grp.circle = circle
        return grp
    
    def _edge(self, n1, n2, weight, is_negative=False):
        grp = VGroup()
        color = EDGE_NEGATIVE if is_negative else EDGE_POSITIVE
        arrow = Arrow(n1.get_center(), n2.get_center(), color=color,
                     stroke_width=4, buff=0.5, max_tip_length_to_length_ratio=0.1)
        mid = (n1.get_center() + n2.get_center()) / 2
        badge_color = WARNING_RED if is_negative else EDGE_POSITIVE
        badge_bg = Circle(radius=0.22, fill_color=BACKGROUND_COLOR, fill_opacity=0.95,
                         stroke_color=badge_color, stroke_width=2)
        badge_bg.move_to(mid)
        badge_text = Text(str(weight), font_size=WEIGHT_LABEL_SIZE, 
                         color=WARNING_RED if is_negative else TEXT_PRIMARY)
        badge_text.move_to(mid)
        grp.add(arrow, badge_bg, badge_text)
        grp.arrow = arrow
        grp.weight = weight
        grp.is_negative = is_negative
        return grp
    
    def _iteration_counter(self, current, total):
        grp = VGroup()
        bg = RoundedRectangle(width=4, height=0.9, corner_radius=0.15,
                             fill_color=ITERATION_BG, fill_opacity=1,
                             stroke_color=TEXT_PRIMARY, stroke_width=2)
        bg.move_to(UP * 3)
        text = Text(f"ITERATION {current}/{total}", font_size=ITERATION_SIZE,
                   color=ITERATION_TEXT, weight=BOLD)
        text.move_to(bg.get_center())
        grp.add(bg, text)
        return grp
    
    # ==================== SCENE 1 ====================
    def _scene1_why_not_dijkstra(self):
        title = Text("The Problem with Dijkstra's", font_size=TITLE_SIZE, color=TEXT_PRIMARY)
        title.move_to(UP * 2.8)
        self.play(Write(title), run_time=SLOW)
        
        subtitle = Text("Negative weights break the algorithm", font_size=SUBTITLE_SIZE, color=WARNING_RED)
        subtitle.next_to(title, DOWN, buff=0.3)
        self.play(FadeIn(subtitle, shift=UP * 0.2), run_time=NORMAL)
        self.wait(PAUSE)
        
        self.play(title.animate.scale(0.6).move_to(UP * 3.4), FadeOut(subtitle), run_time=NORMAL)
        
        # Graph with negative edge
        book = self._node("Book", LEFT * 4 + UP * 0.5, NODE_SOURCE, 0.4)
        lp = self._node("LP", LEFT * 1 + UP * 1.2, NODE_DEFAULT, 0.4)
        poster = self._node("Post", LEFT * 1 + DOWN * 1.2, NODE_DEFAULT, 0.4)
        piano = self._node("Piano", RIGHT * 2 + UP * 0.5, NODE_DEFAULT, 0.4)
        
        nodes = [book, lp, poster, piano]
        self.play(LaggedStart(*[FadeIn(n) for n in nodes], lag_ratio=0.1), run_time=NORMAL)
        
        edges = [
            self._edge(book, lp, 5),
            self._edge(book, poster, 0),
            self._edge(lp, piano, 30),
            self._edge(poster, lp, -7, is_negative=True),
            self._edge(poster, piano, 35),
        ]
        
        for e in edges:
            self.play(GrowArrow(e.arrow), run_time=INSTANT)
            self.play(FadeIn(VGroup(e[1], e[2])), run_time=INSTANT)
        
        neg_label = Text("Negative edge!", font_size=SMALL_SIZE, color=WARNING_RED)
        neg_label.next_to(edges[3], LEFT, buff=0.3)
        self.play(edges[3].arrow.animate.set_stroke(width=6), Write(neg_label), run_time=NORMAL)
        self.wait(PAUSE)
        
        # Show comparison boxes
        dijk_bg = RoundedRectangle(width=4.5, height=1.3, corner_radius=0.1,
                                  fill_color=DIJKSTRA_COLOR, fill_opacity=0.2,
                                  stroke_color=DIJKSTRA_COLOR, stroke_width=2)
        dijk_bg.move_to(RIGHT * 4.5 + UP * 1.5)
        dijk_title = Text("Dijkstra's: $35", font_size=SMALL_SIZE, color=DIJKSTRA_COLOR)
        dijk_title.move_to(dijk_bg.get_center())
        self.play(FadeIn(dijk_bg), Write(dijk_title), run_time=NORMAL)
        
        actual_bg = RoundedRectangle(width=4.5, height=1.3, corner_radius=0.1,
                                    fill_color=SUCCESS_GREEN, fill_opacity=0.2,
                                    stroke_color=SUCCESS_GREEN, stroke_width=2)
        actual_bg.move_to(RIGHT * 4.5 + DOWN * 0.5)
        actual_title = Text("Actual best: $28", font_size=SMALL_SIZE, color=SUCCESS_GREEN)
        actual_title.move_to(actual_bg.get_center())
        self.play(FadeIn(actual_bg), Write(actual_title), run_time=NORMAL)
        
        self.play(
            edges[1].arrow.animate.set_color(SUCCESS_GREEN),
            edges[3].arrow.animate.set_color(SUCCESS_GREEN),
            edges[2].arrow.animate.set_color(SUCCESS_GREEN),
            run_time=NORMAL
        )
        self.wait(PAUSE)
        
        # Clear and show needs
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=FAST)
        
        need_title = Text("We need an algorithm that:", font_size=BODY_SIZE, color=TEXT_PRIMARY)
        need_title.move_to(UP * 1.5)
        self.play(Write(need_title), run_time=NORMAL)
        
        needs = VGroup()
        for text in ["✓ Handles negative weights", "✓ Detects negative cycles", "✓ Guarantees correctness"]:
            t = Text(text, font_size=LABEL_SIZE, color=SUCCESS_GREEN)
            needs.add(t)
        needs.arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        needs.move_to(UP * 0.3)
        
        self.play(LaggedStart(*[FadeIn(n, shift=LEFT * 0.3) for n in needs], lag_ratio=0.2), run_time=NORMAL)
        
        bf_title = Text("BELLMAN-FORD", font_size=TITLE_SIZE, color=BELLMAN_COLOR, weight=BOLD)
        bf_title.move_to(DOWN * 1.5)
        self.play(Write(bf_title), run_time=SLOW)
        self.wait(LONG_PAUSE)
    
    # ==================== SCENE 2 ====================
    def _scene2_overview(self):
        title = Text("Bellman-Ford: The Core Idea", font_size=HEADING_SIZE, color=TEXT_PRIMARY)
        title.move_to(UP * TITLE_Y)
        self.play(Write(title), run_time=NORMAL)
        
        core = Text("Relax ALL edges, V-1 times", font_size=SUBTITLE_SIZE, color=TEXT_ACCENT, weight=BOLD)
        core.move_to(UP * 2)
        self.play(Write(core), run_time=SLOW)
        self.wait(PAUSE)
        
        # Simple graph
        n0 = self._node("0", LEFT * 3, NODE_SOURCE, 0.4)
        n1 = self._node("1", LEFT * 0.5 + UP * 1, NODE_DEFAULT, 0.4)
        n2 = self._node("2", LEFT * 0.5 + DOWN * 1, NODE_DEFAULT, 0.4)
        n3 = self._node("3", RIGHT * 2, NODE_DEFAULT, 0.4)
        
        nodes = [n0, n1, n2, n3]
        self.play(LaggedStart(*[FadeIn(n) for n in nodes], lag_ratio=0.1), run_time=NORMAL)
        
        edges = [
            self._edge(n0, n1, 4), self._edge(n0, n2, 2),
            self._edge(n1, n2, -1, is_negative=True),
            self._edge(n1, n3, 2), self._edge(n2, n3, 3),
        ]
        for e in edges:
            self.play(GrowArrow(e.arrow), FadeIn(VGroup(e[1], e[2])), run_time=INSTANT)
        
        v_text = Text("V = 4 → 3 iterations needed", font_size=LABEL_SIZE, color=TEXT_SECONDARY)
        v_text.move_to(DOWN * 2)
        self.play(Write(v_text), run_time=NORMAL)
        
        # Pulse all edges
        self.play(*[e.arrow.animate.set_stroke(width=6, color=ITERATION_BG) for e in edges], run_time=NORMAL)
        self.play(*[e.arrow.animate.set_stroke(width=4, color=EDGE_POSITIVE if not e.is_negative else EDGE_NEGATIVE) for e in edges], run_time=NORMAL)
        
        self.wait(LONG_PAUSE)
    
    # ==================== SCENE 3 ====================
    def _scene3_step_by_step(self):
        title = Text("Step-by-Step Example", font_size=HEADING_SIZE, color=TEXT_PRIMARY)
        title.move_to(UP * TITLE_Y)
        self.play(Write(title), run_time=NORMAL)
        self.play(title.animate.scale(0.7).move_to(UP * 3.5), run_time=FAST)
        
        # 5-vertex graph
        positions = {
            0: LEFT * 4 + UP * 0.5, 1: LEFT * 1.5 + UP * 1.5, 2: LEFT * 1.5 + DOWN * 1,
            3: RIGHT * 1.5 + DOWN * 0.5, 4: RIGHT * 1.5 + UP * 1.5,
        }
        
        nodes = {v: self._node(str(v), pos, NODE_SOURCE if v == 0 else NODE_DEFAULT, 0.4) 
                for v, pos in positions.items()}
        self.play(LaggedStart(*[FadeIn(n) for n in nodes.values()], lag_ratio=0.08), run_time=NORMAL)
        
        edges_data = [(0,1,6,False), (0,2,7,False), (1,2,5,False), (1,3,-4,True),
                      (1,4,8,False), (2,4,-3,True), (3,2,9,False), (4,3,2,False)]
        edges = {(u,v): self._edge(nodes[u], nodes[v], w, neg) for u,v,w,neg in edges_data}
        
        for e in edges.values():
            self.play(GrowArrow(e.arrow), FadeIn(VGroup(e[1], e[2])), run_time=INSTANT)
        
        # Distance labels
        distances = {0: 0, 1: float('inf'), 2: float('inf'), 3: float('inf'), 4: float('inf')}
        dist_header = Text("DISTANCES", font_size=SMALL_SIZE, color=TEXT_ACCENT, weight=BOLD)
        dist_header.move_to(RIGHT * TABLE_X + UP * 2.5)
        self.play(FadeIn(dist_header), run_time=FAST)
        
        dist_labels = {}
        y = 2.0
        for v in range(5):
            d_str = "0" if v == 0 else "∞"
            d_text = Text(f"{v}: {d_str}", font_size=DISTANCE_SIZE, 
                         color=DIST_FINITE if v == 0 else DIST_INFINITY)
            d_text.move_to(RIGHT * TABLE_X + UP * y)
            self.play(FadeIn(d_text), run_time=INSTANT)
            dist_labels[v] = d_text
            y -= 0.55
        
        iter_counter = self._iteration_counter(1, 4)
        self.play(FadeIn(iter_counter), run_time=ITERATION_TRANSITION)
        
        # Quick iteration simulation (simplified for combined animation)
        for iteration in range(1, 5):
            if iteration > 1:
                new_counter = self._iteration_counter(iteration, 4)
                self.play(Transform(iter_counter, new_counter), run_time=ITERATION_TRANSITION)
            
            for (u, v), edge in edges.items():
                self.play(edge.arrow.animate.set_color(EDGE_CURRENT), run_time=INSTANT)
                
                dist_u = distances[u]
                if dist_u != float('inf'):
                    new_dist = dist_u + edge.weight
                    if new_dist < distances[v]:
                        distances[v] = new_dist
                        new_text = Text(f"{v}: {new_dist}", font_size=DISTANCE_SIZE, color=DIST_IMPROVING)
                        new_text.move_to(dist_labels[v].get_center())
                        self.play(Transform(dist_labels[v], new_text), run_time=FAST)
                
                orig_color = EDGE_NEGATIVE if edge.is_negative else EDGE_POSITIVE
                self.play(edge.arrow.animate.set_color(orig_color), run_time=INSTANT)
        
        success = Text("✓ Shortest paths found!", font_size=BODY_SIZE, color=SUCCESS_GREEN)
        success.move_to(DOWN * 2.5)
        self.play(Write(success), run_time=NORMAL)
        self.wait(LONG_PAUSE)
    
    # ==================== SCENE 4 ====================
    def _scene4_negative_cycle(self):
        title = Text("Negative Cycle Detection", font_size=HEADING_SIZE, color=TEXT_PRIMARY)
        title.move_to(UP * TITLE_Y)
        self.play(Write(title), run_time=NORMAL)
        
        # Cycle graph
        a = self._node("A", LEFT * 2, NODE_SOURCE, 0.5)
        b = self._node("B", RIGHT * 2 + UP * 1.5, NODE_DEFAULT, 0.5)
        c = self._node("C", RIGHT * 2 + DOWN * 1.5, NODE_DEFAULT, 0.5)
        
        self.play(FadeIn(a), FadeIn(b), FadeIn(c), run_time=NORMAL)
        
        e_ab = self._edge(a, b, 2)
        e_bc = self._edge(b, c, 3)
        e_ca = self._edge(c, a, -8, is_negative=True)
        
        for e in [e_ab, e_bc, e_ca]:
            self.play(GrowArrow(e.arrow), FadeIn(VGroup(e[1], e[2])), run_time=FAST)
        
        cycle_sum = Text("Cycle: 2 + 3 + (-8) = -3", font_size=LABEL_SIZE, color=WARNING_RED)
        cycle_sum.move_to(DOWN * 2.5)
        self.play(Write(cycle_sum), run_time=NORMAL)
        self.wait(PAUSE)
        
        # Alarm
        alarm = Text("⚠️ NEGATIVE CYCLE DETECTED!", font_size=WARNING_SIZE, color=WARNING_RED, weight=BOLD)
        alarm.move_to(DOWN * 3.2)
        self.play(
            Write(alarm),
            *[e.arrow.animate.set_color(CYCLE_GLOW).set_stroke(width=8) for e in [e_ab, e_bc, e_ca]],
            run_time=NORMAL
        )
        
        for _ in range(3):
            self.play(*[e.arrow.animate.set_stroke(width=10) for e in [e_ab, e_bc, e_ca]], run_time=0.2)
            self.play(*[e.arrow.animate.set_stroke(width=6) for e in [e_ab, e_bc, e_ca]], run_time=0.2)
        
        self.wait(LONG_PAUSE)
    
    # ==================== SCENE 5 ====================
    def _scene5_why_v_minus_1(self):
        title = Text("Why V-1 Iterations?", font_size=HEADING_SIZE, color=TEXT_PRIMARY)
        title.move_to(UP * TITLE_Y)
        self.play(Write(title), run_time=NORMAL)
        
        explanation = Text("Longest simple path has V-1 edges", font_size=BODY_SIZE, color=TEXT_SECONDARY)
        explanation.move_to(UP * 2)
        self.play(Write(explanation), run_time=NORMAL)
        
        # Path visualization
        path_nodes = VGroup()
        for i in range(5):
            n = self._node(str(i), LEFT * 4 + RIGHT * 2 * i, NODE_DEFAULT, 0.35)
            path_nodes.add(n)
        path_nodes[0][0].set_fill(NODE_SOURCE)
        path_nodes.move_to(ORIGIN)
        
        self.play(FadeIn(path_nodes), run_time=NORMAL)
        
        for i in range(4):
            arrow = Arrow(path_nodes[i].get_center(), path_nodes[i+1].get_center(),
                         color=EDGE_POSITIVE, stroke_width=3, buff=0.4)
            count = Text(str(i+1), font_size=SMALL_SIZE, color=ITERATION_BG)
            count.next_to(arrow, UP, buff=0.15)
            self.play(GrowArrow(arrow), FadeIn(count), run_time=FAST)
        
        conclusion = Text("5 vertices → 4 edges → 4 iterations", font_size=BODY_SIZE, color=SUCCESS_GREEN)
        conclusion.move_to(DOWN * 2)
        self.play(Write(conclusion), run_time=NORMAL)
        self.wait(LONG_PAUSE)
    
    # ==================== SCENE 6 ====================
    def _scene6_implementation(self):
        title = Text("Python Implementation", font_size=HEADING_SIZE, color=TEXT_PRIMARY)
        title.move_to(UP * TITLE_Y)
        self.play(Write(title), run_time=NORMAL)
        
        code_lines = [
            "def bellman_ford(graph, V, src):",
            "    dist = [inf] * V",
            "    dist[src] = 0",
            "    for i in range(V - 1):      # V-1 iterations",
            "        for u, v, w in graph:   # All edges",
            "            if dist[u] + w < dist[v]:",
            "                dist[v] = dist[u] + w",
            "    # Negative cycle check",
            "    for u, v, w in graph:",
            "        if dist[u] + w < dist[v]:",
            "            return 'Negative cycle!'",
            "    return dist",
        ]
        
        code_grp = VGroup()
        y = 2.0
        for line in code_lines:
            color = SUCCESS_GREEN if "V-1" in line or "All edges" in line else (
                    WARNING_RED if "Negative" in line else TEXT_PRIMARY)
            t = Text(line, font_size=CODE_SIZE, color=color, font="monospace")
            t.move_to(LEFT * 1 + UP * y)
            t.align_to(LEFT * 5, LEFT)
            code_grp.add(t)
            y -= 0.4
        
        self.play(LaggedStart(*[Write(t) for t in code_grp], lag_ratio=0.1), run_time=SLOW)
        self.wait(LONG_PAUSE)
    
    # ==================== SCENE 7 ====================
    def _scene7_comparison(self):
        title = Text("Bellman-Ford vs Dijkstra's", font_size=HEADING_SIZE, color=TEXT_PRIMARY)
        title.move_to(UP * TITLE_Y)
        self.play(Write(title), run_time=NORMAL)
        
        rows = [
            ("Negative edges", "✗ No", "✓ Yes"),
            ("Cycle detection", "✗ No", "✓ Yes"),
            ("Time", "O(E log V)", "O(VE)"),
            ("Speed", "Faster", "Slower"),
        ]
        
        y = 1.5
        for feature, dijk, bf in rows:
            f_text = Text(feature, font_size=SMALL_SIZE, color=TEXT_SECONDARY)
            f_text.move_to(LEFT * 2 + UP * y)
            
            d_text = Text(dijk, font_size=SMALL_SIZE, color=WARNING_RED if "✗" in dijk else TEXT_PRIMARY)
            d_text.move_to(RIGHT * 0.5 + UP * y)
            
            b_text = Text(bf, font_size=SMALL_SIZE, color=SUCCESS_GREEN if "✓" in bf else TEXT_PRIMARY)
            b_text.move_to(RIGHT * 3 + UP * y)
            
            self.play(FadeIn(f_text), FadeIn(d_text), FadeIn(b_text), run_time=FAST)
            y -= 0.6
        
        decision = Text("Negative weights? → Bellman-Ford", font_size=BODY_SIZE, color=BELLMAN_COLOR)
        decision.move_to(DOWN * 2)
        self.play(Write(decision), run_time=NORMAL)
        self.wait(LONG_PAUSE)
    
    # ==================== SCENE 8 ====================
    def _scene8_applications(self):
        title = Text("Real-World Applications", font_size=HEADING_SIZE, color=TEXT_PRIMARY)
        title.move_to(UP * TITLE_Y)
        self.play(Write(title), run_time=NORMAL)
        
        apps = [
            ("Network Routing (RIP)", BELLMAN_COLOR),
            ("Currency Arbitrage", WARNING_ORANGE),
            ("Financial Modeling", TEXT_ACCENT),
        ]
        
        items = VGroup()
        for text, color in apps:
            t = Text(text, font_size=LABEL_SIZE, color=color, weight=BOLD)
            items.add(t)
        items.arrange(DOWN, buff=0.5)
        items.move_to(ORIGIN)
        
        self.play(LaggedStart(*[FadeIn(i, shift=RIGHT * 0.3) for i in items], lag_ratio=0.3), run_time=SLOW)
        
        example = Text("$100 → €92 → £80 → $103 = Profit!", font_size=SMALL_SIZE, color=SUCCESS_GREEN)
        example.move_to(DOWN * 2.5)
        self.play(Write(example), run_time=NORMAL)
        self.wait(LONG_PAUSE)
    
    # ==================== SCENE 9 ====================
    def _scene9_complexity(self):
        title = Text("Time Complexity: O(VE)", font_size=HEADING_SIZE, color=TEXT_PRIMARY)
        title.move_to(UP * TITLE_Y)
        self.play(Write(title), run_time=NORMAL)
        
        outer = Text("Outer loop: O(V)", font_size=LABEL_SIZE, color=TEXT_ACCENT)
        outer.move_to(UP * 1)
        inner = Text("Inner loop: O(E)", font_size=LABEL_SIZE, color=TEXT_ACCENT)
        inner.move_to(UP * 0.3)
        total = Text("Total: O(V × E)", font_size=BODY_SIZE, color=SUCCESS_GREEN, weight=BOLD)
        total.move_to(DOWN * 0.5)
        
        self.play(Write(outer), run_time=NORMAL)
        self.play(Write(inner), run_time=NORMAL)
        self.play(Write(total), run_time=NORMAL)
        
        tradeoff = Text("Slower than Dijkstra's, but handles negative weights", 
                       font_size=SMALL_SIZE, color=TEXT_SECONDARY)
        tradeoff.move_to(DOWN * 2)
        self.play(Write(tradeoff), run_time=NORMAL)
        self.wait(LONG_PAUSE)
    
    # ==================== SCENE 10 ====================
    def _scene10_recap(self):
        title = Text("Key Takeaways", font_size=HEADING_SIZE, color=TEXT_PRIMARY)
        title.move_to(UP * TITLE_Y)
        self.play(Write(title), run_time=NORMAL)
        
        takeaways = [
            ("✓ Handles negative weights", EDGE_NEGATIVE),
            ("✓ Relaxes ALL edges V-1 times", ITERATION_BG),
            ("✓ Detects negative cycles", WARNING_RED),
            ("✓ Guarantees correctness", SUCCESS_GREEN),
        ]
        
        items = VGroup()
        for text, color in takeaways:
            t = Text(text, font_size=LABEL_SIZE, color=color)
            items.add(t)
        items.arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        items.move_to(UP * 0.5)
        
        self.play(LaggedStart(*[FadeIn(i, shift=LEFT * 0.3) for i in items], lag_ratio=0.2), run_time=SLOW)
        
        final = Text("BELLMAN-FORD: When correctness > speed", 
                    font_size=BODY_SIZE, color=BELLMAN_COLOR, weight=BOLD)
        final.move_to(DOWN * 2)
        self.play(Write(final), run_time=NORMAL)
        self.wait(LONG_PAUSE)


# Re-export individual scenes for direct access
__all__ = [
    'BellmanFordAnimation',
    'Scene1_WhyNotDijkstra',
    'Scene2_AlgorithmOverview', 
    'Scene3_StepByStep',
    'Scene4_NegativeCycle',
    'Scene5_WhyVMinus1',
    'Scene6_Implementation',
    'Scene7_Comparison',
    'Scene8_Applications',
    'Scene9_Complexity',
    'Scene10_Recap',
]
