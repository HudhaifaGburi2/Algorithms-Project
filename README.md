# Algorithms — Visual Sorting Animations

A professional-grade **algorithm visualization repository** built with **Manim Community Edition**, focused on **deep conceptual understanding through motion**.

This project animates and compares **Quick Sort** and **Merge Sort** using a strict visual language inspired by **3Blue1Brown**. Every animation is deterministic, reusable, and designed to encode meaning through space, color, and motion rather than text-heavy explanations.

---

## 🎯 Project Goals

* Visually explain **divide-and-conquer sorting algorithms** with mathematical clarity
* Compare **Quick Sort vs Merge Sort** side by side on the same data
* Achieve **lecture-quality animations** suitable for YouTube, university courses, and self-study
* Enforce a **clean architecture** separating algorithm logic from animation logic

---

## 🧠 Design Philosophy

This repository follows a small set of non-negotiable principles:

* **Motion explains logic** — if an object moves, it must mean something
* **One concept per scene** — no overloaded animations
* **Recursion is spatial** — depth is shown vertically, not with text
* **Color is semantic** — colors never change meaning
* **No randomness** — every render is deterministic and reproducible

Text is minimized. Understanding comes from watching the algorithm *think*.

---

## 🛠 Tech Stack

* **Python 3.10+**
* **Manim Community Edition (CE)**
* Full HD rendering (1920×1080 @ 60 FPS)

---

## 📁 Repository Structure

```
sorting_visualization/
│
├── main.py
│
├── config/                 # Global visual & animation constants
│   ├── colors.py
│   ├── fonts.py
│   └── animation_constants.py
│
├── core/                   # Reusable visual primitives
│   ├── array_element.py
│   ├── array_group.py
│   ├── pointers.py
│   └── recursion_layout.py
│
├── algorithms/             # Pure algorithm logic (no Manim)
│   ├── quick_sort/
│   │   ├── logic.py
│   │   ├── states.py
│   │   └── constants.py
│   │
│   ├── merge_sort/
│   │   ├── logic.py
│   │   ├── states.py
│   │   └── constants.py
│
├── scenes/                 # Manim scenes (visualization only)
│   ├── intro/
│   ├── quick_sort/
│   ├── merge_sort/
│   └── comparison/
│
├── assets/                 # Fonts, audio, static images
│
├── utils/                  # Helpers & validators
│
└── README.md
```

---

## 🧩 Architecture Overview

### Algorithm Layer (`algorithms/`)

* Contains **pure Python implementations** of algorithms
* Produces **step-by-step states** (comparisons, swaps, merges)
* No Manim imports allowed

### Visualization Core (`core/`)

* Defines reusable visual components (bars, arrows, containers)
* Completely algorithm-agnostic

### Scene Layer (`scenes/`)

* Translates algorithm states into animations
* Each scene explains **exactly one concept**

This separation ensures correctness, reusability, and testability.

---

## 🎥 Implemented Animations

### Quick Sort

* Pivot selection and highlighting
* Partitioning via spatial movement
* Recursive subarray visualization
* Best vs worst-case recursion depth

### Merge Sort

* Balanced recursive splitting
* Temporary array usage during merge
* Stable ordering preservation
* Guaranteed O(n log n) behavior

### Comparison

* Side-by-side execution on identical input
* Visual contrast of space usage
* Performance intuition (not benchmarks)

---

## ▶️ How to Run

1. Install Manim Community Edition

   ```bash
   pip install manim
   ```

2. Render a scene

   ```bash
   manim -pqh main.py QuickSortOverviewScene
   ```

3. For full-quality output

   ```bash
   manim -pqh --resolution 1920,1080 main.py ComparisonScene
   ```

---

## 🚦 Contribution Rules

* Do not mix algorithm logic with animation code
* Do not introduce new colors without semantic definition
* Do not hard-code screen coordinates
* Do not add text where motion can explain

Pull requests that violate architectural or visual rules will be rejected.

---

## 📚 Target Audience

* Computer science students
* Educators and lecturers
* Self-learners studying algorithms
* Content creators producing technical videos

---

## 📌 Roadmap

* Add Heap Sort and Counting Sort
* Complexity heat-map visualizations
* Arabic and English narration timing guides
* Export-friendly short-form animations

---

## 📄 License

MIT License — free to use, modify, and distribute for educational purposes.


