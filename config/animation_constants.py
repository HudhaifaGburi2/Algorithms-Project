"""
Animation timing and easing constants.
R8 compliant: No single animation step > 1.5 seconds.
"""
from manim import rate_functions

# Duration constants (in seconds)
DURATION_FAST = 0.3
DURATION_NORMAL = 0.5
DURATION_SLOW = 0.8
DURATION_EMPHASIS = 1.0
DURATION_MAX = 1.5  # R8: Maximum allowed duration

# Pause durations
PAUSE_SHORT = 0.2
PAUSE_NORMAL = 0.5
PAUSE_LONG = 1.0

# Easing functions (3Blue1Brown style)
EASE_DEFAULT = rate_functions.ease_in_out_cubic
EASE_SMOOTH = rate_functions.smooth
EASE_BOUNCE = rate_functions.ease_out_bounce
EASE_ELASTIC = rate_functions.ease_out_elastic

# Lag ratios for staggered animations
LAG_RATIO_TIGHT = 0.1
LAG_RATIO_NORMAL = 0.2
LAG_RATIO_LOOSE = 0.4

# Scale factors
SCALE_HIGHLIGHT = 1.2
SCALE_SHRINK = 0.8
SCALE_RECURSION_DEPTH = 0.85

# Opacity values
OPACITY_FULL = 1.0
OPACITY_DIM = 0.4
OPACITY_GHOST = 0.2

# Array visualization
BAR_WIDTH = 0.6
BAR_SPACING = 0.15
BAR_HEIGHT_SCALE = 0.4
MAX_BAR_HEIGHT = 4.0

# Recursion tree layout
RECURSION_VERTICAL_SPACING = 1.5
RECURSION_HORIZONTAL_SPACING = 0.8

# Frame dimensions
FRAME_WIDTH = 14.0
FRAME_HEIGHT = 8.0
