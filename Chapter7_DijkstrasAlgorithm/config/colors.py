"""
Color constants for Chapter 7: Dijkstra's Algorithm
Follows semantic color rules from project guidelines.
"""

# Background
BACKGROUND_COLOR = "#0F172A"  # Deep slate

# Text Colors
TEXT_PRIMARY = "#FFFFFF"
TEXT_SECONDARY = "#94A3B8"
TEXT_ACCENT = "#3B82F6"

# Node States (CRITICAL - must follow exactly)
NODE_DEFAULT = "#475569"       # Slate gray - unprocessed
NODE_PROCESSING = "#3B82F6"    # Electric blue - current focus
NODE_PROCESSED = "#10B981"     # Emerald green - completed
NODE_CHEAPEST = "#FBBF24"      # Gold - candidate for next step
NODE_START = "#06B6D4"         # Cyan - origin
NODE_FINISH = "#EC4899"        # Hot pink - destination

# Edge States
EDGE_DEFAULT = "#64748B"       # Neutral gray
EDGE_CONSIDERING = "#3B82F6"   # Blue - being evaluated
EDGE_PATH = "#22C55E"          # Bright green - solution path
EDGE_BETTER = "#10B981"        # Green - better path found
EDGE_NEGATIVE = "#EF4444"      # Red - negative weight warning

# Weight/Cost Colors
COST_IMPROVING = "#10B981"     # Green - better path found
COST_UNCHANGED = "#94A3B8"     # Light gray - no improvement
COST_INFINITY = "#6B7280"      # Dim gray - unreachable

# Data Structure Colors
COST_TABLE = "#F59E0B"         # Amber - tracking costs
PARENT_TABLE = "#8B5CF6"       # Purple - tracking paths
PROCESSED_SET = "#14B8A6"      # Teal - completed nodes

# Comparison
COMPARISON_COLOR = "#EC4899"   # Pink

# Warning
WARNING_RED = "#EF4444"        # Red - danger/error
