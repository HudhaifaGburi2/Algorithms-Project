"""
Color constants for Chapter 1: Binary Search vs Linear Search
Follows semantic color rules from project guidelines.
"""

# Background
BACKGROUND_COLOR = "#0E1117"

# Text Colors
TEXT_PRIMARY = "#FFFFFF"
TEXT_SECONDARY = "#A0A0A0"
TEXT_ACCENT = "#58C4DD"

# Element States (Semantic Colors)
UNPROCESSED = "#3B82F6"       # Blue - elements not yet checked
ACTIVE_COMPARISON = "#EF4444"  # Red - currently being compared
FOUND_ELEMENT = "#22C55E"      # Green - target found / correct
ELIMINATED = "#6B7280"         # Gray - eliminated from search
HIGHLIGHT = "#FACC15"          # Yellow - current focus / pointer

# Search-Specific Colors
LINEAR_COLOR = "#F97316"       # Orange - linear search theme
BINARY_COLOR = "#8B5CF6"       # Purple - binary search theme

# Big O Graph Colors
O_1 = "#22C55E"               # Green - O(1) constant
O_LOG_N = "#8B5CF6"           # Purple - O(log n)
O_N = "#F97316"               # Orange - O(n)
O_N_LOG_N = "#3B82F6"         # Blue - O(n log n)
O_N_SQUARED = "#EF4444"       # Red - O(n²)
O_N_FACTORIAL = "#EC4899"     # Pink - O(n!)

# Pointer Colors
LOW_POINTER = "#22C55E"        # Green - low pointer
MID_POINTER = "#FACC15"        # Yellow - mid pointer
HIGH_POINTER = "#EF4444"       # Red - high pointer
