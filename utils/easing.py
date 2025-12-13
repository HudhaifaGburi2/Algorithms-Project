"""
Custom easing functions for smooth animations.
3Blue1Brown style motion.
"""
from manim import rate_functions
import math


def ease_in_out_cubic(t: float) -> float:
    """Smooth cubic easing."""
    if t < 0.5:
        return 4 * t * t * t
    else:
        return 1 - pow(-2 * t + 2, 3) / 2


def ease_out_back(t: float) -> float:
    """Overshoot easing for bouncy feel."""
    c1 = 1.70158
    c3 = c1 + 1
    return 1 + c3 * pow(t - 1, 3) + c1 * pow(t - 1, 2)


def ease_out_elastic(t: float) -> float:
    """Elastic easing for emphasis."""
    if t == 0:
        return 0
    if t == 1:
        return 1
    c4 = (2 * math.pi) / 3
    return pow(2, -10 * t) * math.sin((t * 10 - 0.75) * c4) + 1


def ease_in_expo(t: float) -> float:
    """Exponential ease in."""
    return 0 if t == 0 else pow(2, 10 * t - 10)


def ease_out_expo(t: float) -> float:
    """Exponential ease out."""
    return 1 if t == 1 else 1 - pow(2, -10 * t)


def linear(t: float) -> float:
    """Linear interpolation."""
    return t


# Preset easing configurations
EASING_SMOOTH = rate_functions.smooth
EASING_STANDARD = ease_in_out_cubic
EASING_BOUNCY = ease_out_back
EASING_ELASTIC = ease_out_elastic
EASING_FAST_START = ease_out_expo
EASING_SLOW_START = ease_in_expo
