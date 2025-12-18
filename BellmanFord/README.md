# Bellman-Ford Algorithm Animation

Educational animation explaining the Bellman-Ford algorithm in 3Blue1Brown style.

## Overview

This animation covers:
1. **Why Not Dijkstra's** - Problem introduction with negative weights
2. **Algorithm Overview** - Core concept: Relax ALL edges V-1 times
3. **Step-by-Step Example** - Main demonstration with 5 vertices
4. **Negative Cycle Detection** - The Vth iteration trick
5. **Why V-1 Iterations** - Path length reasoning
6. **Implementation** - Python code walkthrough
7. **Comparison** - Bellman-Ford vs Dijkstra's
8. **Applications** - Real-world use cases
9. **Time Complexity** - O(VE) analysis
10. **Final Recap** - Key takeaways

## Usage

### Full Animation
```bash
# Preview quality (480p)
manim -pql main.py BellmanFordAnimation

# HD quality (1080p)
manim -pqh main.py BellmanFordAnimation

# 4K quality
manim -pqk main.py BellmanFordAnimation
```

### Individual Scenes
```bash
manim -pql main.py Scene1_WhyNotDijkstra
manim -pql main.py Scene2_AlgorithmOverview
manim -pql main.py Scene3_StepByStep
manim -pql main.py Scene4_NegativeCycle
manim -pql main.py Scene5_WhyVMinus1
manim -pql main.py Scene6_Implementation
manim -pql main.py Scene7_Comparison
manim -pql main.py Scene8_Applications
manim -pql main.py Scene9_Complexity
manim -pql main.py Scene10_Recap
```

## Visual Design

### Color Palette
- **Background:** #0a0e27 (deep navy)
- **Negative edges:** #ef4444 (red) - key differentiator
- **Positive edges:** #3b82f6 (blue)
- **Relaxation success:** #10b981 (green)
- **Current edge:** #fbbf24 (gold)
- **Negative cycle:** #dc2626 (danger red)

### Key Visual Elements
- Prominent iteration counter (gold badge)
- Distance table sidebar with real-time updates
- Calculation boxes showing relaxation math
- Dramatic negative cycle detection alarm

## Algorithm Summary

```python
def bellman_ford(graph, V, src):
    dist = [float('inf')] * V
    dist[src] = 0
    
    # Relax edges V-1 times
    for i in range(V - 1):
        for u, v, w in graph:
            if dist[u] != float('inf'):
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
    
    # Check for negative cycle
    for u, v, w in graph:
        if dist[u] + w < dist[v]:
            return "Negative cycle!"
    
    return dist
```

## Project Structure

```
BellmanFord/
├── main.py              # Main entry point
├── README.md            # This file
├── config/
│   ├── __init__.py
│   ├── colors.py        # Color constants
│   ├── fonts.py         # Typography settings
│   └── animation_constants.py
├── scenes/
│   ├── __init__.py
│   ├── scene1_why_not_dijkstra.py
│   ├── scene2_algorithm_overview.py
│   ├── scene3_step_by_step.py
│   ├── scene4_negative_cycle.py
│   ├── scene5_why_v_minus_1.py
│   ├── scene6_implementation.py
│   ├── scene7_comparison.py
│   ├── scene8_applications.py
│   ├── scene9_complexity.py
│   └── scene10_recap.py
├── assets/
│   ├── icons/
│   └── diagrams/
└── media/               # Output directory
```

## Key Concepts

### Bellman-Ford vs Dijkstra's

| Feature | Dijkstra's | Bellman-Ford |
|---------|-----------|--------------|
| Negative edges | ✗ No | ✓ Yes |
| Cycle detection | ✗ No | ✓ Yes |
| Time Complexity | O(E log V) | O(VE) |
| Approach | Greedy | Dynamic Prog |

### When to Use
- **Dijkstra's:** All positive weights, need speed
- **Bellman-Ford:** Negative weights exist, need cycle detection

## Requirements

- Python 3.8+
- Manim Community Edition

```bash
pip install manim
```
