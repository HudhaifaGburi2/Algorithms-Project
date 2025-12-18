"""
Color constants for Bellman-Ford Algorithm
Follows semantic color rules with emphasis on negative edges and cycle detection.
"""

# Background
BACKGROUND_COLOR = "#0a0e27"  # Deep navy

# Text Colors
TEXT_PRIMARY = "#FFFFFF"
TEXT_SECONDARY = "#94A3B8"
TEXT_ACCENT = "#3B82F6"

# Node States
NODE_DEFAULT = "#475569"       # Slate gray - unprocessed
NODE_SOURCE = "#06B6D4"        # Cyan - source vertex
NODE_PROCESSING = "#FBBF24"    # Gold - being updated
NODE_UPDATED = "#10B981"       # Green - distance improved
NODE_STABLE = "#6B7280"        # Gray - no change

# Edge States - CRITICAL for Bellman-Ford
EDGE_DEFAULT = "#64748B"       # Neutral gray
EDGE_POSITIVE = "#3B82F6"      # Blue - positive weight
EDGE_NEGATIVE = "#EF4444"      # Red - negative weight (KEY DIFFERENTIATOR)
EDGE_CURRENT = "#FBBF24"       # Gold - being processed
EDGE_RELAXED = "#10B981"       # Green - successful relaxation
EDGE_NO_CHANGE = "#4B5563"     # Dim gray - no improvement
EDGE_CYCLE = "#DC2626"         # Danger red - negative cycle

# Distance Colors
DIST_INFINITY = "#9CA3AF"      # Light gray for ∞
DIST_FINITE = "#FFFFFF"        # White for finite values
DIST_IMPROVING = "#22C55E"     # Bright green flash
DIST_STABLE = "#6B7280"        # Gray - unchanged

# Iteration Counter
ITERATION_BG = "#FBBF24"       # Gold background
ITERATION_TEXT = "#0A0E27"     # Dark text on gold

# Comparison Box
CALC_BG = "#FFFFFF"            # White background
CALC_BORDER = "#FBBF24"        # Gold border
CALC_SUCCESS = "#10B981"       # Green checkmark
CALC_FAIL = "#EF4444"          # Red X

# Negative Cycle Warning
CYCLE_WARNING_BG = "rgba(220, 38, 38, 0.2)"
CYCLE_WARNING_TEXT = "#DC2626"
CYCLE_GLOW = "#EF4444"

# Algorithm Comparison
DIJKSTRA_COLOR = "#3B82F6"     # Blue for Dijkstra
BELLMAN_COLOR = "#10B981"      # Green for Bellman-Ford

# Warning
WARNING_RED = "#EF4444"
WARNING_ORANGE = "#F59E0B"
SUCCESS_GREEN = "#10B981"
