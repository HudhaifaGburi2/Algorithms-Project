# Chapter 4: Divide & Conquer and Quicksort

Educational animation demonstrating the Divide & Conquer strategy and Quicksort algorithm using Manim (3Blue1Brown style).

## Overview

This animation covers:
1. **D&C Introduction** - Problem-solving strategy, pattern
2. **Farm Problem** - Visual metaphor for recursive reduction
3. **Recursive Sum** - D&C on arrays with stack visualization
4. **Quicksort Concept** - High-level algorithm steps
5. **Quicksort Walkthrough** - Step-by-step on [10, 5, 2, 3]
6. **Pivot Comparison** - Best vs Worst case (O(log n) vs O(n) depth)
7. **Big-O Analysis** - Why O(n log n) average, O(n²) worst
8. **Summary** - Key takeaways

## Project Structure

```
Chapter4_DivideConquerQuicksort/
├── main.py                    # Main animation script
├── config/
│   ├── colors.py              # Quicksort-specific colors
│   ├── fonts.py               # Font constants
│   └── animation_constants.py # Timing/layout constants
├── core/
│   ├── partition_view.py      # Array/partition visualization
│   └── recursion_tree.py      # Call stack/tree visualization
├── algorithms/
│   └── quicksort/logic.py     # Pure quicksort algorithm
├── scenes/                    # Individual scene files
├── utils/
├── assets/
└── output/
```

## Usage

### Render Full Animation

```bash
# Preview quality (480p)
manim -pql main.py Chapter4Animation

# HD quality (1080p)
manim -pqh main.py Chapter4Animation
```

### Render Individual Scenes

```bash
manim -pql main.py DNCIntroScene
manim -pql main.py FarmProblemScene
manim -pql main.py RecursiveSumScene
manim -pql main.py QuicksortConceptScene
manim -pql main.py QuicksortWalkthroughScene
manim -pql main.py PivotComparisonScene
manim -pql main.py BigOAnalysisScene
manim -pql main.py SummaryScene
```

## Color Semantics

| Color | Meaning |
|-------|---------|
| Orange (#F97316) | Pivot element |
| Blue (#3B82F6) | Less than pivot partition |
| Green (#22C55E) | Greater than pivot partition |
| Gray (#6B7280) | Base case |
| Purple (#8B5CF6) | Divide phase / Stack frame |
| Cyan (#06B6D4) | Conquer/combine phase |
| Pink (#EC4899) | Active recursion frame |

## Key Concepts

### Divide & Conquer Pattern
```
1. Base Case → Simplest form, solve directly
2. Divide    → Break into smaller subproblems
3. Conquer   → Solve subproblems recursively
4. Combine   → Merge solutions
```

### Quicksort Algorithm
```
quicksort(array):
    if len(array) < 2:
        return array  # base case
    
    pivot = array[-1]
    less = [x for x in array[:-1] if x < pivot]
    greater = [x for x in array[:-1] if x >= pivot]
    
    return quicksort(less) + [pivot] + quicksort(greater)
```

### Complexity Analysis

| Case | Depth | Time |
|------|-------|------|
| Best | O(log n) | O(n log n) |
| Average | O(log n) | O(n log n) |
| Worst | O(n) | O(n²) |

**Why?**
- Each level processes O(n) elements
- Number of levels depends on pivot balance
- Balanced → O(log n) levels
- Unbalanced (sorted input) → O(n) levels

### Pivot Choice Impact
- **Best case**: Pivot splits array in half → balanced tree
- **Worst case**: Already sorted + first/last pivot → skewed tree
- **Solution**: Random pivot → average case expected

## Key Takeaways

1. D&C breaks big problems into smaller identical ones
2. Every D&C has base case + recursive reduction
3. Quicksort: partition around pivot, recurse on parts
4. Pivot choice determines performance
5. Average O(n log n), worst O(n²)
6. Big-O measures growth rate, not actual time

## Dependencies

- Python 3.8+
- Manim Community Edition

## License

Educational use. Based on "Grokking Algorithms" Chapter 4.
