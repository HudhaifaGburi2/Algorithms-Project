"""
Color constants for Chapter 4: Divide & Conquer and Quicksort
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
ACTIVE = "#EF4444"             # Red - currently active
COMPLETED = "#22C55E"          # Green - completed/sorted
HIGHLIGHT = "#FACC15"          # Yellow - highlight

# Quicksort-Specific Colors (CRITICAL)
PIVOT = "#F97316"              # Orange - pivot element
LESS_THAN = "#3B82F6"          # Blue - less than pivot partition
GREATER_THAN = "#22C55E"       # Green - greater than pivot partition
BASE_CASE = "#6B7280"          # Gray - base case (size 0 or 1)
ACTIVE_FRAME = "#EC4899"       # Pink - active recursion frame

# Divide & Conquer
DIVIDE_COLOR = "#8B5CF6"       # Purple - divide phase
CONQUER_COLOR = "#06B6D4"      # Cyan - conquer/combine phase
PROBLEM_COLOR = "#F59E0B"      # Amber - problem representation

# Farm Problem
FARM_COLOR = "#84CC16"         # Lime - farm land
SQUARE_COLOR = "#22D3EE"       # Cyan - valid square
INVALID_COLOR = "#EF4444"      # Red - invalid tiling

# Call Stack
STACK_FRAME = "#8B5CF6"        # Purple - stack frame
STACK_ACTIVE = "#EC4899"       # Pink - active frame
STACK_RETURNING = "#06B6D4"    # Cyan - returning value

# Big O
O_LOG_N = "#22C55E"            # Green - O(log n) - best case depth
O_N = "#F97316"                # Orange - O(n) - worst case depth
O_N_LOG_N = "#3B82F6"          # Blue - O(n log n)
O_N_SQUARED = "#EF4444"        # Red - O(n²)
