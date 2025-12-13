"""
Pure greedy algorithm implementations.
No Manim imports.
"""
from typing import Dict, List, Set, Tuple
from dataclasses import dataclass
import math


@dataclass
class ScheduleClass:
    """A class with start and end times."""
    name: str
    start: float  # Hour (e.g., 9.0 for 9am)
    end: float


@dataclass
class KnapsackItem:
    """Item with value and weight."""
    name: str
    value: int
    weight: int


def greedy_classroom_schedule(classes: List[ScheduleClass]) -> List[ScheduleClass]:
    """
    Greedy classroom scheduling - pick class that ends soonest.
    
    Returns list of non-overlapping classes.
    """
    # Sort by end time
    sorted_classes = sorted(classes, key=lambda c: c.end)
    
    selected = []
    current_end = 0
    
    for cls in sorted_classes:
        if cls.start >= current_end:
            selected.append(cls)
            current_end = cls.end
    
    return selected


def greedy_knapsack(items: List[KnapsackItem], capacity: int) -> Tuple[List[KnapsackItem], int]:
    """
    Greedy knapsack - pick most valuable that fits.
    
    Returns (selected items, total value).
    """
    # Sort by value (highest first)
    sorted_items = sorted(items, key=lambda i: i.value, reverse=True)
    
    selected = []
    total_value = 0
    remaining = capacity
    
    for item in sorted_items:
        if item.weight <= remaining:
            selected.append(item)
            total_value += item.value
            remaining -= item.weight
    
    return selected, total_value


def optimal_knapsack(items: List[KnapsackItem], capacity: int) -> Tuple[List[KnapsackItem], int]:
    """
    Find optimal knapsack solution (for comparison).
    Uses brute force for small item counts.
    """
    n = len(items)
    best_value = 0
    best_combo = []
    
    # Try all 2^n combinations
    for mask in range(1 << n):
        combo = []
        total_weight = 0
        total_value = 0
        
        for i in range(n):
            if mask & (1 << i):
                combo.append(items[i])
                total_weight += items[i].weight
                total_value += items[i].value
        
        if total_weight <= capacity and total_value > best_value:
            best_value = total_value
            best_combo = combo
    
    return best_combo, best_value


def greedy_set_cover(states_needed: Set[str], 
                     stations: Dict[str, Set[str]]) -> List[str]:
    """
    Greedy set covering - pick station covering most uncovered states.
    
    Returns list of selected station names.
    """
    selected_stations = []
    remaining_states = states_needed.copy()
    
    while remaining_states:
        best_station = None
        states_covered = set()
        
        for station, coverage in stations.items():
            covered = remaining_states & coverage
            if len(covered) > len(states_covered):
                best_station = station
                states_covered = covered
        
        if best_station is None:
            break
            
        selected_stations.append(best_station)
        remaining_states -= states_covered
    
    return selected_stations


def factorial(n: int) -> int:
    """Calculate n!"""
    if n <= 1:
        return 1
    return n * factorial(n - 1)


def tsp_greedy(cities: Dict[str, Tuple[float, float]], 
               start: str) -> Tuple[List[str], float]:
    """
    Greedy TSP - always go to nearest unvisited city.
    
    Returns (route, total distance).
    """
    def distance(c1: str, c2: str) -> float:
        x1, y1 = cities[c1]
        x2, y2 = cities[c2]
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    
    visited = [start]
    current = start
    total_distance = 0
    
    while len(visited) < len(cities):
        nearest = None
        nearest_dist = float('inf')
        
        for city in cities:
            if city not in visited:
                d = distance(current, city)
                if d < nearest_dist:
                    nearest = city
                    nearest_dist = d
        
        if nearest:
            visited.append(nearest)
            total_distance += nearest_dist
            current = nearest
    
    return visited, total_distance


# Demo data
CLASSROOM_CLASSES = [
    ScheduleClass("Art", 9.0, 10.0),
    ScheduleClass("Eng", 9.5, 10.5),
    ScheduleClass("Math", 10.0, 11.0),
    ScheduleClass("CS", 10.5, 11.5),
    ScheduleClass("Music", 11.0, 12.0),
]

KNAPSACK_ITEMS = [
    KnapsackItem("Stereo", 3000, 30),
    KnapsackItem("Laptop", 2000, 20),
    KnapsackItem("Guitar", 1500, 15),
]

RADIO_STATES = {"MT", "WA", "OR", "ID", "NV", "UT", "CA", "AZ"}

RADIO_STATIONS = {
    "KONE": {"ID", "NV", "UT"},
    "KTWO": {"WA", "ID", "MT"},
    "KTHREE": {"OR", "NV", "CA"},
    "KFOUR": {"NV", "UT"},
    "KFIVE": {"CA", "AZ"},
}

TSP_CITIES = {
    "Marin": (0, 2),
    "SF": (1, 1),
    "Berkeley": (2, 2),
    "Palo Alto": (1, -1),
    "Fremont": (2, -1),
}

# NP-Complete examples
NP_COMPLETE_SIGNS = [
    "Fast with few items, slow with many",
    "Must calculate ALL combinations",
    "Can't break into sub-problems",
    "Involves sequences or sets",
    "Similar to known NP-complete problems",
]
