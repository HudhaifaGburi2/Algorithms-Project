# Chapter 2: Arrays, Linked Lists & Selection Sort

Educational animation demonstrating fundamental data structures and sorting using Manim (3Blue1Brown style).

## Overview

This animation covers:
1. **Introduction** - Memory concepts, data storage approaches
2. **Arrays** - Contiguous memory, O(1) reads, O(n) inserts
3. **Linked Lists** - Scattered memory, pointers, O(1) start inserts
4. **Comparison** - Side-by-side: when to use each
5. **Selection Sort** - O(n²) sorting with visual step-by-step
6. **Summary** - Key takeaways and quick reference

## Project Structure

```
Chapter2_ArraysLinkedListsSelectionSort/
├── main.py                    # Main animation script
├── config/
│   ├── colors.py              # Color constants
│   ├── fonts.py               # Font size constants
│   └── animation_constants.py # Timing and layout constants
├── core/
│   ├── memory_cell.py         # Array/memory cell component
│   └── linked_list_node.py    # Linked list node component
├── algorithms/
│   ├── array/logic.py         # Array operation complexities
│   ├── linked_list/logic.py   # Linked list operation complexities
│   └── selection_sort/logic.py # Selection sort algorithm
├── scenes/                    # Individual scene files (optional)
├── utils/
├── assets/                    # Audio, images, fonts
└── output/                    # Rendered videos
```

## Usage

### Render Full Animation

```bash
# Preview quality (480p, faster)
manim -pql main.py Chapter2Animation

# HD quality (1080p)
manim -pqh main.py Chapter2Animation
```

### Render Individual Scenes

```bash
manim -pql main.py IntroScene
manim -pql main.py ArrayScene
manim -pql main.py LinkedListScene
manim -pql main.py ComparisonScene
manim -pql main.py SelectionSortScene
manim -pql main.py SummaryScene
```

## Color Semantics

| Color | Meaning |
|-------|---------|
| Blue (#3B82F6) | Unprocessed elements |
| Red (#EF4444) | Active comparison |
| Green (#22C55E) | Sorted / Correct |
| Yellow (#FACC15) | Current minimum |
| Purple (#8B5CF6) | Array elements |
| Cyan (#06B6D4) | Linked list nodes |
| Orange (#F97316) | Pointers / Highlights |

## Key Concepts Demonstrated

### Arrays
- **Memory**: Contiguous allocation
- **Read**: O(1) - Direct index access
- **Insert/Delete (end)**: O(1)
- **Insert/Delete (start)**: O(n) - Must shift all elements

### Linked Lists
- **Memory**: Scattered allocation with pointers
- **Read**: O(n) - Must traverse from head
- **Insert/Delete (start)**: O(1) - Just update pointers
- **Insert/Delete (middle)**: O(n) to find + O(1) to modify

### Selection Sort
- Find minimum in unsorted portion
- Swap with first unsorted element
- Repeat until sorted
- **Time Complexity**: O(n²) always
- **Space Complexity**: O(1) in-place

## Comparison Table

| Operation | Array | Linked List |
|-----------|-------|-------------|
| Read | O(1) Fast | O(n) Slow |
| Insert (start) | O(n) Slow | O(1) Fast |
| Insert (end) | O(1) Fast | O(n) Slow |
| Delete (start) | O(n) Slow | O(1) Fast |
| Memory | Fixed/Contiguous | Flexible/Scattered |

## When to Use

- **Arrays**: Lots of reads, few inserts/deletes
- **Linked Lists**: Frequent inserts/deletes at start

## Dependencies

- Python 3.8+
- Manim Community Edition

## License

Educational use. Based on "Grokking Algorithms" Chapter 2.
