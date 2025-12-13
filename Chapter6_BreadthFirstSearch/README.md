# Chapter 6: Breadth-First Search

Educational animation demonstrating BFS, graphs, queues, and shortest path finding using Manim (3Blue1Brown style).

## Overview

This animation covers:
1. **Introduction** - Wave exploration concept
2. **What is a Graph** - Nodes, edges, neighbors
3. **Mango Seller Search** - Full BFS walkthrough with queue
4. **Shortest Path Guarantee** - Why queue order matters
5. **Queue Deep Dive** - FIFO operations
6. **Graph as Hash Table** - Implementation
7. **Complexity Analysis** - O(V + E)
8. **Applications** - Social networks, GPS, spell checkers
9. **Summary** - Key takeaways

## Project Structure

```
Chapter6_BreadthFirstSearch/
├── main.py                    # Main animation script
├── config/
│   ├── colors.py              # Node/edge state colors
│   ├── fonts.py               # Font constants
│   └── animation_constants.py # Timing/layout constants
├── core/
│   └── graph_view.py          # Graph visualization components
├── algorithms/
│   └── bfs/logic.py           # Pure BFS algorithm
├── utils/
├── assets/
└── output/
```

## Usage

### Render Full Animation

```bash
# Preview quality (480p)
manim -pql main.py Chapter6Animation

# HD quality (1080p)
manim -pqh main.py Chapter6Animation
```

### Render Individual Scenes

```bash
manim -pql main.py IntroScene
manim -pql main.py GraphScene
manim -pql main.py MangoSellerScene
manim -pql main.py ShortestPathScene
manim -pql main.py QueueScene
manim -pql main.py ImplementationScene
manim -pql main.py ComplexityScene
manim -pql main.py ApplicationsScene
manim -pql main.py SummaryScene
```

## Color Semantics (CRITICAL)

| Color | Meaning |
|-------|---------|
| Gray (#4A5568) | Node default - unvisited |
| Blue (#3B82F6) | Node active - currently exploring |
| Amber (#FBBF24) | Node queued - waiting in queue |
| Green (#10B981) | Node visited - already checked |
| Pink (#EC4899) | Node target - found! |
| Cyan (#06B6D4) | 1st degree connection |
| Purple (#8B5CF6) | 2nd degree connection |
| Teal (#14B8A6) | 3rd degree connection |
| Orange (#F59E0B) | Queue structure |

## Key Concepts

### BFS Algorithm
```python
def bfs(graph, start, is_target):
    queue = deque([start])
    visited = set([start])
    
    while queue:
        current = queue.popleft()  # FIFO
        
        if is_target(current):
            return True  # Found!
        
        for neighbor in graph[current]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
    
    return False  # Not found
```

### Why Shortest Path?
- Queue maintains order: 1st degree → 2nd degree → 3rd degree
- Closer nodes always checked before farther nodes
- First match = shortest path guaranteed

### Complexity
- **Time**: O(V + E)
  - V = vertices (each processed once)
  - E = edges (each followed once)
- **Space**: O(V) for queue and visited set

### Graph Implementation
```python
graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["alice"] = ["peggy"]
graph["bob"] = ["anuj", "peggy"]
```

## Key Takeaways

1. BFS explores **layer by layer** (breadth-first)
2. Uses **Queue (FIFO)** to maintain exploration order
3. **Guarantees shortest path** in unweighted graphs
4. Must **track visited nodes** to avoid infinite loops
5. Time complexity: **O(V + E)** - linear!

## Applications

- **Social Networks**: Find closest friend who...
- **GPS Navigation**: Shortest route
- **Web Crawlers**: Explore pages by depth
- **Spell Checkers**: Minimum edit distance
- **Game AI**: Fewest moves to win

## Dependencies

- Python 3.8+
- Manim Community Edition

## License

Educational use. Based on "Grokking Algorithms" Chapter 6.
