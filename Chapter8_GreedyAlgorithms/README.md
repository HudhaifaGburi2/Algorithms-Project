# Chapter 8: Greedy Algorithms

Educational animation demonstrating greedy strategy, approximation algorithms, and NP-complete problems using Manim (3Blue1Brown style).

## Overview

This animation covers:
1. **Introduction** - Greedy strategy concept
2. **Classroom Scheduling** - Greedy works perfectly
3. **Knapsack Problem** - Greedy is approximate (86% optimal)
4. **Set Covering** - Radio stations example with O(n²) greedy
5. **Traveling Salesperson** - NP-complete factorial explosion
6. **NP-Complete Recognition** - Warning signs
7. **Summary** - When to use greedy

## Project Structure

```
Chapter8_GreedyAlgorithms/
├── main.py                    # Main animation script
├── config/
│   ├── colors.py              # Greedy/NP-complete colors
│   ├── fonts.py               # Font constants
│   └── animation_constants.py # Timing constants
├── core/
│   └── greedy_view.py         # Timeline, knapsack, coverage views
├── algorithms/
│   └── greedy/logic.py        # Pure greedy algorithms
├── utils/
├── assets/
└── output/
```

## Usage

### Render Full Animation

```bash
# Preview quality (480p)
manim -pql main.py Chapter8Animation

# HD quality (1080p)
manim -pqh main.py Chapter8Animation
```

### Render Individual Scenes

```bash
manim -pql main.py IntroScene
manim -pql main.py ClassroomScene
manim -pql main.py KnapsackScene
manim -pql main.py SetCoveringScene
manim -pql main.py TSPScene
manim -pql main.py NPCompleteScene
manim -pql main.py SummaryScene
```

## Color Semantics (CRITICAL)

| Color | Meaning |
|-------|---------|
| Gold (#FBBF24) | Greedy choice - optimal pick at this step |
| Green (#10B981) | Selected - chosen solution |
| Red (#EF4444) | Rejected - conflicts/invalid |
| Gray (#64748B) | Available - not yet considered |
| Amber (#F59E0B) | Approximation - good enough |
| Red (#DC2626) | Exponential danger - impossible |
| Purple (#8B5CF6) | Exact solution - ideal but impractical |

## Key Concepts

### Greedy Strategy
```python
def greedy_schedule(classes):
    # Sort by end time (soonest first)
    sorted_classes = sorted(classes, key=lambda c: c.end)
    
    selected = []
    current_end = 0
    
    for cls in sorted_classes:
        if cls.start >= current_end:
            selected.append(cls)  # Greedy pick!
            current_end = cls.end
    
    return selected
```

### When Greedy Works
| Problem | Greedy Result |
|---------|---------------|
| Classroom scheduling | ✓ Optimal |
| Knapsack | ≈ 86% optimal |
| Set covering | ≈ 90%+ optimal |
| Traveling salesperson | ≈ 90%+ optimal |

### NP-Complete Warning Signs
1. Fast with few items, slow with many
2. Must calculate ALL combinations
3. Can't break into sub-problems
4. Involves sequences or sets
5. Similar to known NP-complete problems

### Factorial Explosion (TSP)
| Cities | Routes |
|--------|--------|
| 5 | 120 |
| 10 | 3,628,800 |
| 15 | 1.3 trillion |
| 20 | 2.4 × 10¹⁸ |

## Complexity

| Algorithm | Greedy | Exact |
|-----------|--------|-------|
| Classroom | O(n log n) | O(n log n) |
| Knapsack | O(n log n) | O(2ⁿ) |
| Set Covering | O(n²) | O(2ⁿ) |
| TSP | O(n²) | O(n!) |

## Key Takeaways

1. **Greedy** = Pick locally optimal at each step
2. **Sometimes optimal** (scheduling)
3. **Sometimes approximate** (knapsack, TSP)
4. **NP-Complete** = No fast exact solution exists
5. **Use greedy** for fast, good-enough solutions

## Dependencies

- Python 3.8+
- Manim Community Edition

## License

Educational use. Based on "Grokking Algorithms" Chapter 8.
