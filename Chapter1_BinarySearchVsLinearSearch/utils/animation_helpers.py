"""
Reusable animation helper functions.
"""
from manim import *


def create_title(text: str, font_size: int, color: str, y_pos: float = 3.3):
    """Create a title positioned at the top."""
    title = Text(text, font_size=font_size, color=color)
    title.move_to(UP * y_pos)
    return title


def create_step_label(text: str, font_size: int, color: str, y_pos: float = 2.3):
    """Create a step indicator label."""
    label = Text(text, font_size=font_size, color=color)
    label.move_to(UP * y_pos)
    return label


def fade_all(scene, mobjects, run_time=0.5):
    """Fade out all mobjects."""
    if mobjects:
        scene.play(*[FadeOut(m) for m in mobjects], run_time=run_time)


def smooth_transition(scene, run_time=0.3):
    """Add a smooth pause between scenes."""
    scene.wait(run_time)
