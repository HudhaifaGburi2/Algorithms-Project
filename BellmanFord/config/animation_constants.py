"""
Animation timing and layout constants for Bellman-Ford.
Emphasizes systematic edge processing and iteration visibility.
"""

# Animation Timing (seconds)
INSTANT = 0.3
FAST = 0.4
NORMAL = 0.6
SLOW = 0.8
PAUSE = 0.5
LONG_PAUSE = 1.0

# Edge relaxation timing
EDGE_GLOW_TIME = 0.3          # Edge glow before processing
RELAXATION_TIME = 0.6         # Per-edge relaxation
DISTANCE_UPDATE_TIME = 0.4    # Distance value flash
ITERATION_TRANSITION = 0.8    # Counter increment
CYCLE_DETECTION_TIME = 1.2    # Dramatic negative cycle reveal
CALC_TYPEWRITER = 0.05        # Per-character for calculation

# Layout Constants
TITLE_Y = 3.3
CONTENT_TOP = 2.5
GRAPH_CENTER_X = -1.5
TABLE_X = 5.0

# Iteration Counter Position
ITERATION_Y = 3.0
ITERATION_WIDTH = 4.0
ITERATION_HEIGHT = 0.8

# Node dimensions
NODE_RADIUS = 0.45
NODE_SPACING = 2.0

# Distance Table dimensions
TABLE_WIDTH = 3.5
TABLE_ROW_HEIGHT = 0.5
TABLE_HEADER_SIZE = 24

# Edge properties
EDGE_WIDTH = 4
EDGE_ACTIVE_WIDTH = 6
EDGE_NEGATIVE_WIDTH = 4  # Always prominent

# Calculation box
CALC_BOX_WIDTH = 4.0
CALC_BOX_HEIGHT = 1.0
CALC_BOX_RADIUS = 0.15

# Negative cycle animation
CYCLE_FLASH_COUNT = 5
CYCLE_FLASH_DURATION = 0.2
CYCLE_GLOW_RADIUS = 0.15
