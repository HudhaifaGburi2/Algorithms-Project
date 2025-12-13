# Quick Sort vs Merge Sort - Manim Animation

A professional educational animation comparing Quick Sort and Merge Sort algorithms, created with Manim Community Edition and inspired by 3Blue1Brown's visual style.

## Features

- **Visual Algorithm Comparison**: Step-by-step animation of both sorting algorithms
- **3Blue1Brown Style**: Clean dark theme, smooth motion, semantic colors
- **Educational Focus**: Each scene explains exactly one concept
- **Reusable Components**: Modular design following best practices

## Requirements

- Python 3.8+
- Manim Community Edition

## Installation

```bash
# Install Manim Community Edition
pip install manim

# Or with conda
conda install -c conda-forge manim
```

## Usage

### Render Full Animation

```bash
# High quality (1080p, 60fps) - recommended for final output
manim -pqh main.py FullAnimation

# Medium quality (720p, 30fps) - good for preview
manim -pqm main.py FullAnimation

# Low quality (480p, 15fps) - fast preview
manim -pql main.py FullAnimation
```

### Render Individual Scenes

```bash
# Title scene
manim -pql main.py TitleScene

# Quick Sort scenes
manim -pql main.py QuickSortOverviewScene
manim -pql main.py QuickSortPartitionScene
manim -pql main.py QuickSortRecursionScene
manim -pql main.py QuickSortComplexityScene

# Merge Sort scenes
manim -pql main.py MergeSortOverviewScene
manim -pql main.py MergeSortSplitScene
manim -pql main.py MergeSortMergeScene
manim -pql main.py MergeSortComplexityScene

# Comparison scenes
manim -pql main.py SideBySideScene
manim -pql main.py FinalSummaryScene
manim -pql main.py ClosingScene
```

### Quality Options

| Flag | Resolution | FPS | Use Case |
|------|------------|-----|----------|
| `-ql` | 480p | 15 | Fast preview |
| `-qm` | 720p | 30 | Draft review |
| `-qh` | 1080p | 60 | Final output |
| `-qk` | 4K | 60 | High-end output |

## Project Structure

```
quickSortVsMergeSort/
├── main.py                 # Entry point, full animation
├── config/                 # Global configuration
│   ├── colors.py          # Semantic color definitions
│   ├── fonts.py           # Typography settings
│   └── animation_constants.py  # Timing and easing
├── core/                   # Reusable visual components
│   ├── array_element.py   # Array bar visualization
│   ├── pointers.py        # Pointer indicators
│   └── recursion_layout.py # Tree layout helpers
├── algorithms/             # Pure algorithm logic
│   ├── quick_sort/        # Quick Sort implementation
│   │   ├── logic.py       # Algorithm (no Manim)
│   │   ├── states.py      # Animation states
│   │   └── constants.py   # Algorithm constants
│   └── merge_sort/        # Merge Sort implementation
│       ├── logic.py
│       ├── states.py
│       └── constants.py
├── scenes/                 # Animation scenes
│   ├── intro/             # Title and motivation
│   ├── quick_sort/        # Quick Sort scenes
│   ├── merge_sort/        # Merge Sort scenes
│   └── comparison/        # Comparison scenes
├── utils/                  # Helper utilities
│   ├── animation_helpers.py
│   ├── easing.py
│   └── validators.py
└── assets/                 # Media assets
    ├── audio/
    ├── images/
    └── fonts/
```

## Color Semantics

| Color | Meaning |
|-------|---------|
| 🔵 Blue | Unprocessed elements |
| 🔴 Red | Active comparison |
| 🟡 Yellow | Pivot (Quick Sort) |
| 🟢 Green | Correctly placed |
| 🟣 Purple | Temporary storage (Merge Sort) |

## Scene Breakdown

1. **TitleScene**: Introduction and motivation
2. **QuickSortOverviewScene**: Quick Sort intuition
3. **QuickSortPartitionScene**: Partition mechanism
4. **QuickSortRecursionScene**: Recursion tree visualization
5. **QuickSortComplexityScene**: Time/space complexity
6. **MergeSortOverviewScene**: Merge Sort intuition
7. **MergeSortSplitScene**: Divide phase
8. **MergeSortMergeScene**: Merge process
9. **MergeSortComplexityScene**: Complexity analysis
10. **SideBySideScene**: Direct comparison
11. **FinalSummaryScene**: Key takeaways
12. **ClosingScene**: Final sorted array

## Design Principles

- **R1**: Every animation encodes information, not decoration
- **R2**: One concept per scene
- **R3**: Deterministic animations (predefined arrays)
- **R4**: Consistent color semantics
- **R5**: Recursion shown spatially (vertical depth)
- **R6**: No hard-coded coordinates (relative positioning)
- **R7**: Algorithm logic separated from animation
- **R8**: No animation step > 1.5 seconds
- **R9**: Minimal text, visual explanations
- **R10**: Reusable components

## License

Educational use permitted.
