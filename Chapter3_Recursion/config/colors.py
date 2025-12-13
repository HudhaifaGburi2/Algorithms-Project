"""
Color constants for Chapter 3: Recursion
Follows semantic color rules from project guidelines.
"""

# Background
BACKGROUND_COLOR = "#0E1117"

# Text Colors
TEXT_PRIMARY = "#FFFFFF"
TEXT_SECONDARY = "#A0A0A0"
TEXT_ACCENT = "#58C4DD"

# Element States (Semantic Colors)
UNPROCESSED = "#3B82F6"        # Blue - not yet processed
ACTIVE = "#EF4444"             # Red - currently executing
COMPLETED = "#22C55E"          # Green - completed/returned
HIGHLIGHT = "#FACC15"          # Yellow - current focus

# Recursion-Specific Colors
BASE_CASE = "#22C55E"          # Green - base case (stops recursion)
RECURSIVE_CASE = "#F97316"     # Orange - recursive case (continues)
STACK_FRAME = "#8B5CF6"        # Purple - stack frame
STACK_ACTIVE = "#EC4899"       # Pink - currently active frame
RETURN_VALUE = "#06B6D4"       # Cyan - return value

# Box/Memory Metaphor
BOX_OUTER = "#374151"          # Gray - outer box
BOX_INNER = "#6366F1"          # Indigo - inner box
KEY_FOUND = "#FACC15"          # Yellow - key/target found

# Stack Visualization
STACK_PUSH = "#22C55E"         # Green - push operation
STACK_POP = "#EF4444"          # Red - pop operation
STACK_BASE = "#1F2937"         # Dark gray - stack base

# Comparison
ITERATIVE_COLOR = "#F97316"    # Orange - iterative approach
RECURSIVE_COLOR = "#8B5CF6"    # Purple - recursive approach
