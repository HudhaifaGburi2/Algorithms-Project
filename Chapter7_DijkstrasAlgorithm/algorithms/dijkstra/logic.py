"""
Pure Dijkstra's algorithm implementation.
No Manim imports.
"""
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass


@dataclass
class DijkstraState:
    """Represents one step in Dijkstra's algorithm."""
    current_node: str
    costs: Dict[str, float]
    parents: Dict[str, Optional[str]]
    processed: List[str]
    action: str  # "find_cheapest", "update_neighbor", "mark_processed", "done"
    neighbor: Optional[str]
    old_cost: Optional[float]
    new_cost: Optional[float]
    is_improvement: bool


def dijkstra_steps(
    graph: Dict[str, Dict[str, int]],
    start: str,
    finish: str
) -> List[DijkstraState]:
    """
    Generate step-by-step states for Dijkstra's algorithm.
    
    Args:
        graph: Weighted adjacency list {node: {neighbor: weight}}
        start: Starting node
        finish: Target node
        
    Returns:
        List of DijkstraState objects for animation
    """
    states = []
    
    # Initialize costs
    costs = {node: float('inf') for node in graph}
    for neighbor, weight in graph.get(start, {}).items():
        costs[neighbor] = weight
    
    # Initialize parents
    parents = {node: None for node in graph}
    for neighbor in graph.get(start, {}):
        parents[neighbor] = start
    
    processed = []
    
    # Initial state
    states.append(DijkstraState(
        current_node=start,
        costs=costs.copy(),
        parents=parents.copy(),
        processed=processed.copy(),
        action="initialize",
        neighbor=None,
        old_cost=None,
        new_cost=None,
        is_improvement=False
    ))
    
    def find_lowest_cost_node():
        lowest_cost = float('inf')
        lowest_node = None
        for node in costs:
            if node not in processed and costs[node] < lowest_cost:
                lowest_cost = costs[node]
                lowest_node = node
        return lowest_node
    
    node = find_lowest_cost_node()
    
    while node is not None:
        # Find cheapest state
        states.append(DijkstraState(
            current_node=node,
            costs=costs.copy(),
            parents=parents.copy(),
            processed=processed.copy(),
            action="find_cheapest",
            neighbor=None,
            old_cost=None,
            new_cost=None,
            is_improvement=False
        ))
        
        cost = costs[node]
        neighbors = graph.get(node, {})
        
        # Update each neighbor
        for neighbor, weight in neighbors.items():
            new_cost = cost + weight
            old_cost = costs.get(neighbor, float('inf'))
            
            is_improvement = new_cost < old_cost
            
            if is_improvement:
                costs[neighbor] = new_cost
                parents[neighbor] = node
            
            states.append(DijkstraState(
                current_node=node,
                costs=costs.copy(),
                parents=parents.copy(),
                processed=processed.copy(),
                action="update_neighbor",
                neighbor=neighbor,
                old_cost=old_cost,
                new_cost=new_cost,
                is_improvement=is_improvement
            ))
        
        # Mark as processed
        processed.append(node)
        
        states.append(DijkstraState(
            current_node=node,
            costs=costs.copy(),
            parents=parents.copy(),
            processed=processed.copy(),
            action="mark_processed",
            neighbor=None,
            old_cost=None,
            new_cost=None,
            is_improvement=False
        ))
        
        node = find_lowest_cost_node()
    
    # Done
    states.append(DijkstraState(
        current_node=finish,
        costs=costs.copy(),
        parents=parents.copy(),
        processed=processed.copy(),
        action="done",
        neighbor=None,
        old_cost=None,
        new_cost=None,
        is_improvement=False
    ))
    
    return states


def get_path(parents: Dict[str, Optional[str]], start: str, finish: str) -> List[str]:
    """Reconstruct path from parents dictionary."""
    path = []
    current = finish
    while current is not None and current != start:
        path.append(current)
        current = parents.get(current)
    if current == start:
        path.append(start)
    path.reverse()
    return path


# Demo graphs
SIMPLE_GRAPH = {
    "Start": {"A": 6, "B": 2},
    "A": {"Fin": 1},
    "B": {"A": 3, "Fin": 5},
    "Fin": {}
}

TRADING_GRAPH = {
    "Book": {"Poster": 0, "LP": 5},
    "Poster": {"Guitar": 30, "Drums": 35},
    "LP": {"Guitar": 15, "Drums": 20},
    "Guitar": {"Piano": 20},
    "Drums": {"Piano": 10},
    "Piano": {}
}

NEGATIVE_GRAPH = {
    "Book": {"Poster": 0, "LP": 5},
    "LP": {"Poster": -7, "Drums": 20},  # Negative weight!
    "Poster": {"Drums": 35},
    "Drums": {}
}

# Complexity
DIJKSTRA_COMPLEXITY = {
    "time": "O((V + E) log V)",
    "space": "O(V)",
    "description": "V = vertices, E = edges, log V from priority queue"
}
