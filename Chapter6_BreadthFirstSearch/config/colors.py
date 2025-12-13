"""
Color constants for Chapter 6: Breadth-First Search
Follows semantic color rules from project guidelines.
"""

# Background
BACKGROUND_COLOR = "#1A1A2E"  # Dark navy

# Text Colors
TEXT_PRIMARY = "#FFFFFF"
TEXT_SECONDARY = "#A0A0A0"
TEXT_ACCENT = "#58C4DD"

# Node States (CRITICAL - must follow exactly)
NODE_DEFAULT = "#4A5568"       # Neutral gray - unvisited
NODE_ACTIVE = "#3B82F6"        # Bright blue - currently exploring
NODE_QUEUED = "#FBBF24"        # Amber - waiting in queue
NODE_VISITED = "#10B981"       # Green - already checked
NODE_TARGET = "#EC4899"        # Hot pink - target found!

# Edge States
EDGE_DEFAULT = "#64748B"       # Slate gray
EDGE_ACTIVE = "#3B82F6"        # Blue - being traversed
EDGE_PATH = "#10B981"          # Green - shortest path

# Queue Structure
QUEUE_COLOR = "#F59E0B"        # Orange - warm, orderly

# Degree/Distance Colors (connection distance)
DEGREE_1 = "#06B6D4"           # Cyan - 1st degree (immediate)
DEGREE_2 = "#8B5CF6"           # Purple - 2nd degree
DEGREE_3 = "#14B8A6"           # Teal - 3rd degree

# Warning/Error
INFINITE_LOOP = "#EF4444"      # Red - danger

# Success
PATH_FOUND = "#10B981"         # Green

# Graph Elements
VISITED_LIST = "#10B981"       # Green - tracked nodes
