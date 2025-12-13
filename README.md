# Algorithms Visualized

Professional-grade **algorithm visualization** built with **Manim Community Edition**, inspired by **3Blue1Brown** style animations.

Each chapter covers concepts from "Grokking Algorithms" with smooth motion, semantic colors, and visual explanations.

---

## 📚 Chapters

| Chapter | Topic | Folder |
|---------|-------|--------|
| 1 | Binary Search vs Linear Search, Big O | `Chapter1_BinarySearchVsLinearSearch/` |
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

# Render Chapter 1
cd Chapter1_BinarySearchVsLinearSearch
manim -pqh main.py Chapter1Animation

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
│   ├── main.py                    # Chapter 1 animation
│   ├── config/                    # Colors, fonts, constants
│   ├── core/                      # Visual components
│   ├── algorithms/                # Pure algorithm logic
│   └── README.md
├── quickSortVsMergeSort/
│   ├── main.py                    # Sorting animation
│   ├── config/
│   ├── core/
│   ├── algorithms/
│   ├── scenes/
│   └── README.md
└── README.md                      # This file
```

---

## 🚦 Rules

- Algorithm logic separate from animation code
- No hard-coded coordinates (use relative positioning)
- Each scene explains exactly one concept
- Reusable visual components

See `.windsurf/rules/rules.md` for full guidelines.

---

## 📄 License

MIT License — free for educational use.


