"""
Animation helper functions.
R10 compliant: Reusable animation utilities.
"""
from manim import (
    AnimationGroup, Succession, LaggedStart,
    FadeIn, FadeOut, Transform, ReplacementTransform,
    Write, Create, Uncreate,
    MoveToTarget, ApplyMethod,
    VGroup
)
from config.animation_constants import (
    DURATION_FAST, DURATION_NORMAL, DURATION_SLOW,
    LAG_RATIO_NORMAL, EASE_DEFAULT
)


def create_staggered_fade_in(mobjects: list, lag_ratio: float = LAG_RATIO_NORMAL):
    """
    Create staggered fade in animation for multiple mobjects.
    R8 compliant: Uses LaggedStart for pacing.
    """
    return LaggedStart(
        *[FadeIn(m, shift_direction=UP) for m in mobjects],
        lag_ratio=lag_ratio,
        run_time=DURATION_NORMAL
    )


def create_staggered_fade_out(mobjects: list, lag_ratio: float = LAG_RATIO_NORMAL):
    """Create staggered fade out animation."""
    return LaggedStart(
        *[FadeOut(m) for m in mobjects],
        lag_ratio=lag_ratio,
        run_time=DURATION_FAST
    )


def create_swap_animation(elem1, elem2, duration: float = DURATION_NORMAL):
    """
    Create swap animation between two elements.
    Elements exchange positions smoothly.
    """
    pos1 = elem1.get_center()
    pos2 = elem2.get_center()
    
    elem1.generate_target()
    elem2.generate_target()
    
    elem1.target.move_to(pos2)
    elem2.target.move_to(pos1)
    
    return AnimationGroup(
        MoveToTarget(elem1, path_arc=PI/2),
        MoveToTarget(elem2, path_arc=-PI/2),
        run_time=duration,
        rate_func=EASE_DEFAULT
    )


def create_highlight_pulse(mobject, color, duration: float = DURATION_FAST):
    """Create a pulse highlight effect."""
    from manim import Indicate
    return Indicate(mobject, color=color, run_time=duration)


def create_color_change(mobject, new_color, duration: float = DURATION_FAST):
    """Create smooth color transition."""
    return mobject.animate.set_fill(new_color).set_stroke(new_color)


def create_slide_animation(mobject, direction, distance: float = 1.0, duration: float = DURATION_NORMAL):
    """Create sliding animation in a direction."""
    return mobject.animate.shift(direction * distance)


def create_scale_animation(mobject, scale_factor: float, duration: float = DURATION_FAST):
    """Create scaling animation."""
    return mobject.animate.scale(scale_factor)


def batch_color_change(mobjects: list, colors: list, duration: float = DURATION_FAST):
    """
    Change colors of multiple mobjects simultaneously.
    R8 compliant: Batched for efficiency.
    """
    animations = []
    for mobject, color in zip(mobjects, colors):
        animations.append(
            mobject.animate.set_fill(color).set_stroke(color)
        )
    return AnimationGroup(*animations, run_time=duration)


def create_sequential_animations(animations: list):
    """Create sequential animation chain."""
    return Succession(*animations)


# Import required constants
from manim import UP, PI
