# Chapter 1: Binary Search vs Linear Search

Educational animation demonstrating search algorithms and Big O notation using Manim (3Blue1Brown style).

## Overview

This animation covers:
1. **Introduction to Algorithms** - The search problem
2. **Linear Search** - Step-by-step O(n) demonstration
3. **Binary Search** - Step-by-step O(log n) demonstration
4. **Side-by-Side Comparison** - Visual comparison with scaling examples
5. **Big O Notation** - Growth curve visualization
6. **Summary** - Key takeaways

## Project Structure

```
Chapter1_BinarySearchVsLinearSearch/
├── main.py                    # Main animation script
├── config/
│   ├── colors.py              # Color constants
│   ├── fonts.py               # Font size constants
│   └── animation_constants.py # Timing and layout constants
├── core/
│   ├── array_element.py       # Array element visual component
│   ├── array_group.py         # Array group visual component
│   └── pointers.py            # Pointer visual components
├── algorithms/
│   ├── linear_search/
│   │   └── logic.py           # Pure linear search algorithm
│   └── binary_search/
│       └── logic.py           # Pure binary search algorithm
├── scenes/                    # Individual scene files (optional)
├── utils/
│   └── animation_helpers.py   # Helper functions
├── assets/                    # Audio, images, fonts
└── output/                    # Rendered videos
```

## Usage

### Render Full Animation

```bash
# Preview quality (480p, faster)
manim -pql main.py Chapter1Animation

# HD quality (1080p)
manim -pqh main.py Chapter1Animation

# 4K quality
manim -pqk main.py Chapter1Animation
```

### Render Individual Scenes

```bash
manim -pql main.py IntroScene
manim -pql main.py LinearSearchScene
manim -pql main.py BinarySearchScene
manim -pql main.py ComparisonScene
manim -pql main.py BigOScene
manim -pql main.py SummaryScene
```

## Color Semantics

| Color | Meaning |
|-------|---------|
| Blue (#3B82F6) | Unprocessed elements |
| Red (#EF4444) | Active comparison |
| Green (#22C55E) | Found / Correct |
| Gray (#6B7280) | Eliminated from search |
| Yellow (#FACC15) | Highlight / Focus |
| Orange (#F97316) | Linear search theme |
| Purple (#8B5CF6) | Binary search theme |

## Key Concepts Demonstrated

### Linear Search (Simple Search)
- Checks each element sequentially from start to end
- Time complexity: O(n)
- Works on any list (sorted or unsorted)
- Simple but slow for large lists

### Binary Search
- Requires sorted array
- Halves search space each step
- Time complexity: O(log n)
- Much faster for large lists

### Big O Notation
- Measures algorithm efficiency by growth rate
- Not actual time (seconds), but operation count growth
- O(log n) grows much slower than O(n)

## Scaling Examples

| List Size | Linear Search | Binary Search |
|-----------|---------------|---------------|
| 100 | 100 steps | 7 steps |
| 1,000 | 1,000 steps | 10 steps |
| 1,000,000 | 1,000,000 steps | 20 steps |
| 1,000,000,000 | 1,000,000,000 steps | 30 steps |

## Dependencies

- Python 3.8+
- Manim Community Edition

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.

![GPLv3 License](https://img.shields.io/badge/License-GPLv3-blue.svg)
