"""
Color constants for Chapter 5: Hash Tables
Follows semantic color rules from project guidelines.
"""

# Background
BACKGROUND_COLOR = "#0E1117"

# Text Colors
TEXT_PRIMARY = "#FFFFFF"
TEXT_SECONDARY = "#A0A0A0"
TEXT_ACCENT = "#58C4DD"

# Element States
UNPROCESSED = "#3B82F6"        # Blue
ACTIVE = "#3B82F6"             # Blue - active operations
COMPLETED = "#10B981"          # Green - success
WARNING = "#F59E0B"            # Amber - collisions
ERROR = "#EF4444"              # Red - worst case

# Hash Table Specific
HASH_FUNCTION = "#8B5CF6"      # Purple - hash function magic
KEY_COLOR = "#06B6D4"          # Cyan - input keys
VALUE_COLOR = "#EC4899"        # Pink - stored values
LINKED_LIST = "#F97316"        # Orange - collision chains
CACHE_COLOR = "#14B8A6"        # Teal - cache operations

# Array Cells
CELL_EMPTY = "#2D3748"         # Dark gray - empty cell
CELL_FILLED = "#4A5568"        # Gray - filled cell
CELL_HIGHLIGHT = "#3B82F6"     # Blue - highlighted

# Performance
O_1 = "#10B981"                # Green - O(1)
O_LOG_N = "#F59E0B"            # Amber - O(log n)
O_N = "#EF4444"                # Red - O(n)

# Load Factor
LOAD_LOW = "#10B981"           # Green - good load
LOAD_MED = "#F59E0B"           # Amber - warning
LOAD_HIGH = "#EF4444"          # Red - needs resize
