#!/usr/bin/env python3
"""Scene 5: Why V-1 Iterations?"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from manim import *
from config.colors import *
from config.fonts import *
from config.animation_constants import *


class Scene5_WhyVMinus1(Scene):
    """Why V-1 Iterations? (90s)"""
    
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        self._run_scene()
    
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
    
    def _run_scene(self):
        title = Text("Why V-1 Iterations?", font_size=HEADING_SIZE, color=TEXT_PRIMARY)
        title.move_to(UP * TITLE_Y)
        self.play(Write(title), run_time=NORMAL)
        
        # Question
        question = Text("What's the longest possible shortest path?", 
                       font_size=BODY_SIZE, color=TEXT_ACCENT)
        question.move_to(UP * 2)
        self.play(Write(question), run_time=NORMAL)
        self.wait(PAUSE)
        
        # Simple path definition
        simple_def = Text("Simple path = No repeated vertices", font_size=LABEL_SIZE, 
                         color=TEXT_SECONDARY)
        simple_def.move_to(UP * 1.3)
        self.play(Write(simple_def), run_time=NORMAL)
        
        # Visual: 5 nodes in a line
        path_nodes = VGroup()
        for i in range(5):
            n = self._node(str(i), LEFT * 4 + RIGHT * 2 * i, NODE_DEFAULT, 0.35)
            path_nodes.add(n)
        path_nodes[0][0].set_fill(NODE_SOURCE)
        path_nodes.move_to(DOWN * 0.3)
        
        self.play(LaggedStart(*[FadeIn(n) for n in path_nodes], lag_ratio=0.1), run_time=NORMAL)
        
        # Draw edges with count labels
        path_arrows = []
        count_labels = []
        for i in range(4):
            arrow = Arrow(path_nodes[i].get_center(), path_nodes[i+1].get_center(),
                         color=EDGE_POSITIVE, stroke_width=4, buff=0.4)
            path_arrows.append(arrow)
            
            count_text = Text(str(i+1), font_size=SMALL_SIZE, color=ITERATION_BG)
            count_text.next_to(arrow, UP, buff=0.15)
            count_labels.append(count_text)
            
            self.play(GrowArrow(arrow), FadeIn(count_text), run_time=FAST)
        
        # Conclusion
        conclusion = Text("5 vertices → Maximum 4 edges in simple path", 
                         font_size=BODY_SIZE, color=SUCCESS_GREEN)
        conclusion.move_to(DOWN * 2)
        self.play(Write(conclusion), run_time=NORMAL)
        
        formula = Text("V vertices → V-1 edges maximum → V-1 iterations", 
                      font_size=LABEL_SIZE, color=TEXT_ACCENT)
        formula.move_to(DOWN * 2.7)
        self.play(Write(formula), run_time=NORMAL)
        self.wait(PAUSE)
        
        # Clear for wave visualization
        self.play(
            FadeOut(question), FadeOut(simple_def), FadeOut(conclusion), FadeOut(formula),
            FadeOut(path_nodes), 
            *[FadeOut(a) for a in path_arrows],
            *[FadeOut(c) for c in count_labels],
            run_time=FAST
        )
        
        # Wave propagation visualization
        wave_title = Text("Distance Propagation", font_size=HEADING_SIZE, color=TEXT_PRIMARY)
        wave_title.move_to(UP * 2.5)
        self.play(Write(wave_title), run_time=NORMAL)
        
        # Grid of nodes
        grid_nodes = VGroup()
        for i in range(5):
            n = self._node(str(i), LEFT * 4 + RIGHT * 2 * i + DOWN * 0.5, NODE_DEFAULT, 0.35)
            grid_nodes.add(n)
        grid_nodes[0][0].set_fill(NODE_SOURCE)
        
        self.play(FadeIn(grid_nodes), run_time=NORMAL)
        
        # Connect with edges
        grid_edges = []
        for i in range(4):
            e = Arrow(grid_nodes[i].get_center(), grid_nodes[i+1].get_center(),
                     color=EDGE_POSITIVE, stroke_width=3, buff=0.4)
            grid_edges.append(e)
        self.play(*[GrowArrow(e) for e in grid_edges], run_time=FAST)
        
        # Show iterations as waves
        iterations_text = ["Iter 1: 1 hop", "Iter 2: 2 hops", "Iter 3: 3 hops", "Iter 4: 4 hops"]
        
        for i, text in enumerate(iterations_text):
            iter_label = Text(text, font_size=LABEL_SIZE, color=ITERATION_BG)
            iter_label.move_to(DOWN * 2)
            
            self.play(Write(iter_label), run_time=FAST)
            
            # Highlight reachable nodes
            for j in range(i + 2):
                if j < len(grid_nodes):
                    target_color = NODE_SOURCE if j == 0 else SUCCESS_GREEN
                    self.play(
                        grid_nodes[j][0].animate.set_fill(target_color),
                        run_time=0.2
                    )
            
            self.wait(0.5)
            self.play(FadeOut(iter_label), run_time=FAST)
            
            # Reset non-source nodes
            for j in range(1, len(grid_nodes)):
                grid_nodes[j][0].set_fill(NODE_DEFAULT)
        
        # Final guarantee
        guarantee = Text("After V-1 iterations: All shortest paths found!", 
                        font_size=BODY_SIZE, color=SUCCESS_GREEN)
        guarantee.move_to(DOWN * 2.5)
        
        caveat = Text("(If no negative cycle)", font_size=SMALL_SIZE, color=TEXT_SECONDARY)
        caveat.move_to(DOWN * 3)
        
        self.play(Write(guarantee), run_time=NORMAL)
        self.play(Write(caveat), run_time=FAST)
        self.wait(LONG_PAUSE)
