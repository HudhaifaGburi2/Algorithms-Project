# Algorithms Visualized

Professional-grade **algorithm visualization** built with **Manim Community Edition**, inspired by **3Blue1Brown** style animations.

Each chapter covers concepts from "Grokking Algorithms" with smooth motion, semantic colors, and visual explanations.

---

## 📚 Chapters

| Chapter | Topic | Folder |
|---------|-------|--------|
| 1 | Binary Search vs Linear Search, Big O | `Chapter1_BinarySearchVsLinearSearch/` |
| 2 | Arrays, Linked Lists, Selection Sort | `Chapter2_ArraysLinkedListsSelectionSort/` |
| 3 | Recursion, Call Stack, Base/Recursive Case | `Chapter3_Recursion/` |
| 4 | Divide & Conquer, Quicksort, Pivot Analysis | `Chapter4_DivideConquerQuicksort/` |
| 5 | Hash Tables, Hash Functions, Collisions | `Chapter5_HashTables/` |
| 6 | Breadth-First Search, Graphs, Queues | `Chapter6_BreadthFirstSearch/` |
| 7 | Dijkstra's Algorithm, Weighted Graphs | `Chapter7_DijkstrasAlgorithm/` |
| 8 | Greedy Algorithms, NP-Complete | `Chapter8_GreedyAlgorithms/` |
| - | Quick Sort vs Merge Sort | `quickSortVsMergeSort/` |

---

## 🧠 Design Philosophy

- **Motion explains logic** — movement encodes meaning
- **One concept per scene** — no overloaded animations
- **Color is semantic** — consistent across all chapters
- **No randomness** — deterministic, reproducible renders

---

## 🎨 Color Semantics

| Color | Meaning |
|-------|---------|
| Blue | Unprocessed element |
| Red | Active comparison |
| Green | Found / Correctly placed |
| Yellow | Pivot / Highlight |
| Purple | Temporary storage |
| Gray | Eliminated |

---

## 🛠 Tech Stack

- Python 3.10+
- Manim Community Edition
- Full HD (1920×1080 @ 60 FPS)

---

## ▶️ Quick Start

```bash
# Install Manim
pip install manim

# Render Chapter 1 - Binary Search
cd Chapter1_BinarySearchVsLinearSearch
manim -pqh main.py Chapter1Animation

# Render Chapter 2 - Arrays & Selection Sort
cd Chapter2_ArraysLinkedListsSelectionSort
manim -pqh main.py Chapter2Animation

# Render Chapter 3 - Recursion
cd Chapter3_Recursion
manim -pqh main.py Chapter3Animation

# Render Chapter 4 - Quicksort
cd Chapter4_DivideConquerQuicksort
manim -pqh main.py Chapter4Animation

# Render Chapter 5 - Hash Tables
cd Chapter5_HashTables
manim -pqh main.py Chapter5Animation

# Render Chapter 6 - BFS
cd Chapter6_BreadthFirstSearch
manim -pqh main.py Chapter6Animation

# Render Chapter 7 - Dijkstra's
cd Chapter7_DijkstrasAlgorithm
manim -pqh main.py Chapter7Animation

# Render Chapter 8 - Greedy
cd Chapter8_GreedyAlgorithms
manim -pqh main.py Chapter8Animation

# Render QuickSort vs MergeSort
cd quickSortVsMergeSort
manim -pqh main.py FullAnimation
```

---

## 📁 Project Structure

```
algorithms/
├── .windsurf/rules/rules.md       # Project rules
├── Chapter1_BinarySearchVsLinearSearch/
│   ├── main.py                    # Binary Search animation
│   ├── config/
│   ├── core/
│   ├── algorithms/
│   └── README.md
├── Chapter2_ArraysLinkedListsSelectionSort/
│   ├── main.py                    # Arrays & Selection Sort
│   ├── config/
│   ├── core/
│   ├── algorithms/
│   └── README.md
├── Chapter3_Recursion/
│   ├── main.py                    # Recursion & Call Stack
│   ├── config/
│   ├── core/
│   ├── algorithms/
│   └── README.md
├── Chapter4_DivideConquerQuicksort/
│   ├── main.py                    # D&C & Quicksort
│   ├── config/
│   ├── core/
│   ├── algorithms/
│   └── README.md
├── Chapter5_HashTables/
│   ├── main.py                    # Hash Tables
│   ├── config/
│   ├── core/
│   ├── algorithms/
│   └── README.md
├── Chapter6_BreadthFirstSearch/
│   ├── main.py                    # BFS & Graphs
│   ├── config/
│   ├── core/
│   ├── algorithms/
│   └── README.md
├── Chapter7_DijkstrasAlgorithm/
│   ├── main.py                    # Dijkstra's Algorithm
│   ├── config/
│   ├── core/
│   ├── algorithms/
│   └── README.md
├── Chapter8_GreedyAlgorithms/
│   ├── main.py                    # Greedy & NP-Complete
│   ├── config/
│   ├── core/
│   ├── algorithms/
│   └── README.md
├── quickSortVsMergeSort/
│   ├── main.py                    # QuickSort vs MergeSort
│   ├── config/
│   ├── core/
│   ├── algorithms/
│   └── README.md
└── README.md                      # This file
```

---

## 🚦 Rules

- Algorithm logic separate from animation code
- No hard-coded coordinates (use relative positioning)
- Each scene explains exactly one concept
- Reusable visual components


---
## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.

![GPLv3 License](https://img.shields.io/badge/License-GPLv3-blue.svg)



