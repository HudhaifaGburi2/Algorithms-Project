"""
Color constants for Chapter 2: Arrays, Linked Lists, Selection Sort
Follows semantic color rules from project guidelines.
"""

# Background
BACKGROUND_COLOR = "#0E1117"

# Text Colors
TEXT_PRIMARY = "#FFFFFF"
TEXT_SECONDARY = "#A0A0A0"
TEXT_ACCENT = "#58C4DD"

# Element States (Semantic Colors)
UNPROCESSED = "#3B82F6"        # Blue - elements not yet processed
ACTIVE_COMPARISON = "#EF4444"  # Red - currently being compared
SORTED_ELEMENT = "#22C55E"     # Green - correctly placed / sorted
CURRENT_MIN = "#FACC15"        # Yellow - current minimum in selection sort
HIGHLIGHT = "#F97316"          # Orange - general highlight

# Data Structure Colors
ARRAY_COLOR = "#8B5CF6"        # Purple - array elements
LINKED_LIST_COLOR = "#06B6D4"  # Cyan - linked list nodes
POINTER_COLOR = "#F97316"      # Orange - pointers/arrows
MEMORY_BOX = "#374151"         # Gray - memory cell background

# Memory Visualization
MEMORY_USED = "#3B82F6"        # Blue - occupied memory
MEMORY_FREE = "#1F2937"        # Dark gray - free memory
MEMORY_CONTIGUOUS = "#8B5CF6"  # Purple - contiguous allocation
MEMORY_SCATTERED = "#06B6D4"   # Cyan - scattered allocation

# Operation Colors
READ_OP = "#22C55E"            # Green - read operation (fast)
INSERT_OP = "#FACC15"          # Yellow - insert operation
DELETE_OP = "#EF4444"          # Red - delete operation

# Big O Graph Colors
O_1 = "#22C55E"               # Green - O(1) constant
O_N = "#F97316"               # Orange - O(n)
O_N_SQUARED = "#EF4444"       # Red - O(n²)
