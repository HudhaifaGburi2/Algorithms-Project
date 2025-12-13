"""
Global color semantics for sorting visualization.
Colors encode meaning, not aesthetics.
"""
from manim import ManimColor

# Background
BACKGROUND_COLOR = "#0E1117"

# Semantic colors (R4 compliant)
UNPROCESSED = "#3B82F6"      # Blue - elements not yet processed
ACTIVE_COMPARISON = "#EF4444" # Red - elements being compared
PIVOT = "#EAB308"            # Yellow - pivot element (Quick Sort)
CORRECTLY_PLACED = "#22C55E"  # Green - element in final position
TEMPORARY_STORAGE = "#A855F7" # Purple - temporary arrays (Merge Sort)

# Additional semantic colors
HIGHLIGHT = "#F97316"        # Orange - general highlight
SUBARRAY_LEFT = "#06B6D4"    # Cyan - left subarray indicator
SUBARRAY_RIGHT = "#EC4899"   # Pink - right subarray indicator

# Text colors
TEXT_PRIMARY = "#FFFFFF"
TEXT_SECONDARY = "#9CA3AF"
TEXT_MUTED = "#6B7280"

# Complexity visualization
COMPLEXITY_GOOD = "#22C55E"  # Green - efficient
COMPLEXITY_BAD = "#EF4444"   # Red - inefficient
COMPLEXITY_NEUTRAL = "#EAB308" # Yellow - average
