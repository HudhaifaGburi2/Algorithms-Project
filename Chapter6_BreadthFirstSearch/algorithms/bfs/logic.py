"""
Pure BFS algorithm implementation.
No Manim imports.
"""
from typing import Dict, List, Optional, Tuple
from collections import deque
from dataclasses import dataclass


@dataclass
class BFSState:
    """Represents one step in BFS."""
    current_node: str
    queue: List[str]
    visited: List[str]
    action: str  # "dequeue", "check", "enqueue_neighbors", "found", "not_found"
    neighbors_added: List[str]
    path: List[str]
    degree: int  # Distance from start


def bfs_steps(graph: Dict[str, List[str]], start: str, is_target) -> List[BFSState]:
    """
    Generate step-by-step states for BFS.
    
    Args:
        graph: Adjacency list representation
        start: Starting node
        is_target: Function to check if node is target
        
    Returns:
        List of BFSState objects for animation
    """
    states = []
    queue = deque([start])
    visited = set([start])
    parent = {start: None}
    
    # Initial state
    states.append(BFSState(
        current_node=start,
        queue=list(queue),
        visited=list(visited),
        action="start",
        neighbors_added=[],
        path=[],
        degree=0
    ))
    
    # Add initial neighbors
    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            queue.append(neighbor)
            visited.add(neighbor)
            parent[neighbor] = start
    
    states.append(BFSState(
        current_node=start,
        queue=list(queue),
        visited=list(visited),
        action="enqueue_neighbors",
        neighbors_added=graph.get(start, []),
        path=[],
        degree=0
    ))
    
    while queue:
        current = queue.popleft()
        
        # Calculate degree
        degree = 0
        node = current
        while parent.get(node):
            degree += 1
            node = parent[node]
        
        # Dequeue state
        states.append(BFSState(
            current_node=current,
            queue=list(queue),
            visited=list(visited),
            action="dequeue",
            neighbors_added=[],
            path=[],
            degree=degree
        ))
        
        # Check state
        if is_target(current):
            # Build path
            path = []
            node = current
            while node:
                path.append(node)
                node = parent.get(node)
            path.reverse()
            
            states.append(BFSState(
                current_node=current,
                queue=list(queue),
                visited=list(visited),
                action="found",
                neighbors_added=[],
                path=path,
                degree=degree
            ))
            return states
        
        # Check state (not found)
        states.append(BFSState(
            current_node=current,
            queue=list(queue),
            visited=list(visited),
            action="check",
            neighbors_added=[],
            path=[],
            degree=degree
        ))
        
        # Add neighbors
        neighbors_added = []
        for neighbor in graph.get(current, []):
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
                parent[neighbor] = current
                neighbors_added.append(neighbor)
        
        if neighbors_added:
            states.append(BFSState(
                current_node=current,
                queue=list(queue),
                visited=list(visited),
                action="enqueue_neighbors",
                neighbors_added=neighbors_added,
                path=[],
                degree=degree
            ))
    
    # Not found
    states.append(BFSState(
        current_node="",
        queue=[],
        visited=list(visited),
        action="not_found",
        neighbors_added=[],
        path=[],
        degree=-1
    ))
    
    return states


def is_mango_seller(name: str) -> bool:
    """Check if person is a mango seller (name ends with 'm')."""
    return name.lower().endswith('m')


# Demo graphs
MANGO_SELLER_GRAPH = {
    "you": ["alice", "bob", "claire"],
    "alice": ["peggy"],
    "bob": ["anuj", "peggy"],
    "claire": ["thom", "jonny"],
    "peggy": [],
    "anuj": [],
    "thom": [],  # Mango seller!
    "jonny": [],
}

POKER_GRAPH = {
    "alex": ["rama", "tom"],
    "rama": ["tom"],
    "tom": ["adit"],
    "adit": [],
}

MORNING_ROUTINE = {
    "wake_up": ["shower", "brush_teeth"],
    "shower": [],
    "brush_teeth": ["eat_breakfast"],
    "eat_breakfast": [],
}

# Complexity
BFS_COMPLEXITY = {
    "time": "O(V + E)",
    "space": "O(V)",
    "description": "V = vertices, E = edges"
}
