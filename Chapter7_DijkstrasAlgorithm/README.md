# Chapter 7: Dijkstra's Algorithm

Educational animation demonstrating weighted graphs, shortest paths, and Dijkstra's algorithm using Manim (3Blue1Brown style).

## Overview

This animation covers:
1. **BFS vs Dijkstra** - Why we need weighted shortest paths
2. **First Example** - Step-by-step algorithm walkthrough
3. **Path Tracing** - Using parent pointers to reconstruct path
4. **Trading Example** - Complex real-world application (Book → Piano)
5. **Negative Weights** - Why Dijkstra fails with negative edges
6. **Applications** - GPS, routing, games, flights
7. **Summary** - Key takeaways and complexity

## Project Structure

```
Chapter7_DijkstrasAlgorithm/
├── main.py                    # Main animation script
├── config/
│   ├── colors.py              # Node/edge/table colors
│   ├── fonts.py               # Font constants
│   └── animation_constants.py # Timing/layout constants
├── core/
│   └── weighted_graph_view.py # Graph visualization components
├── algorithms/
│   └── dijkstra/logic.py      # Pure Dijkstra algorithm
├── utils/
├── assets/
└── output/
```

## Usage

### Render Full Animation

```bash
# Preview quality (480p)
manim -pql main.py Chapter7Animation

# HD quality (1080p)
manim -pqh main.py Chapter7Animation
```

### Render Individual Scenes

```bash
manim -pql main.py IntroScene
manim -pql main.py FirstExampleScene
manim -pql main.py PathTracingScene
manim -pql main.py TradingScene
manim -pql main.py NegativeWeightsScene
manim -pql main.py ApplicationsScene
manim -pql main.py SummaryScene
```

## Color Semantics (CRITICAL)

| Color | Meaning |
|-------|---------|
| Slate Gray (#475569) | Node default - unprocessed |
| Electric Blue (#3B82F6) | Processing - current focus |
| Emerald Green (#10B981) | Processed - completed |
| Gold (#FBBF24) | Cheapest - next candidate |
| Cyan (#06B6D4) | Start node |
| Hot Pink (#EC4899) | Finish/destination node |
| Bright Green (#22C55E) | Solution path |
| Red (#EF4444) | Negative weight warning |
| Amber (#F59E0B) | Cost table |
| Purple (#8B5CF6) | Parent table |
| Teal (#14B8A6) | Processed set |

## Key Concepts

### Dijkstra's Algorithm
```python
def dijkstra(graph, start, finish):
    costs = {node: infinity for node in graph}
    parents = {node: None for node in graph}
    processed = []
    
    # Initialize from start
    for neighbor, weight in graph[start].items():
        costs[neighbor] = weight
        parents[neighbor] = start
    
    node = find_lowest_cost_node(costs, processed)
    
    while node is not None:
        cost = costs[node]
        neighbors = graph[node]
        
        for neighbor, weight in neighbors.items():
            new_cost = cost + weight
            if new_cost < costs[neighbor]:
                costs[neighbor] = new_cost
                parents[neighbor] = node
        
        processed.append(node)
        node = find_lowest_cost_node(costs, processed)
    
    return costs, parents
```

### BFS vs Dijkstra
| Feature | BFS | Dijkstra's |
|---------|-----|-----------|
| Graph type | Unweighted | Weighted |
| Finds | Fewest edges | Minimum total weight |
| Data structure | Queue | Priority queue |
| Time | O(V + E) | O((V+E) log V) |

### Important Rules
1. **Positive weights only** - Dijkstra fails with negative weights
2. **Greedy approach** - Always process cheapest unprocessed node
3. **Parent tracking** - Required for path reconstruction
4. **Once processed, done** - Node won't be revisited

### Negative Weights
- Dijkstra assumes: once processed, no better path exists
- Negative weights can invalidate this assumption
- Use **Bellman-Ford** algorithm for negative weights

## Complexity

- **Time**: O((V + E) log V) with priority queue
- **Space**: O(V) for costs, parents, and processed set

## Applications

- **GPS Navigation** - Shortest driving routes
- **Network Routing** - OSPF protocol uses Dijkstra
- **Flight Planning** - Cheapest multi-leg routes
- **Game AI** - Character pathfinding
- **Social Networks** - Degrees of separation

## Dependencies

- Python 3.8+
- Manim Community Edition

## License

Educational use. Based on "Grokking Algorithms" Chapter 7.
