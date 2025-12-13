---
trigger: always_on
---

## 1. Non-Negotiable Project Rules

### R1 — Visual Meaning Over Decoration

Every animation must **encode information**, not aesthetics.

* Color, motion, position, and scale must each have **one semantic meaning**
* No animation is allowed unless it explains a concept

---

### R2 — One Concept per Scene

* Each Manim `Scene` explains **exactly one idea**
* No scene may explain algorithm logic *and* complexity simultaneously
* If logic changes → new scene

---

### R3 — Deterministic Animations

* All arrays, pivots, and recursion paths must be **predefined**
* No randomness at runtime
* Output must be frame-identical across renders

---

### R4 — Consistent Color Semantics (Global)

| Meaning                        | Color  |
| ------------------------------ | ------ |
| Unprocessed element            | Blue   |
| Active comparison              | Red    |
| Pivot (Quick Sort)             | Yellow |
| Correctly placed               | Green  |
| Temporary storage (Merge Sort) | Purple |

Changing colors without justification is forbidden.

---

### R5 — Recursion Is Spatial, Not Textual

* Recursion must be shown via **position in space**
* Vertical depth = recursion depth
* No recursion explanation via text blocks

---

### R6 — No Hard-Coded Coordinates

* All positioning must be relative:

  * `next_to`
  * `align_to`
  * `arrange`
* Absolute coordinates are prohibited

---

### R7 — Algorithm Logic ≠ Animation Logic

* Sorting logic must live in **pure Python modules**
* Animation code must **only visualize states**
* No algorithm logic inside `Scene` methods

---

### R8 — Scene Duration Control

* No single animation step > 1.5 seconds
* Use pacing, not speed, to show complexity
* Prefer `LaggedStart` for comparisons

---

### R9 — No Text Explanations Longer Than One Line

* Explanations must be visual
* Text is only for labels, titles, or complexity summaries

---

### R10 — Reusability Is Mandatory

* Array bars, pointers, labels, and highlights must be reusable components
* Copy-paste animation logic is forbidden

---

## 2. Mandatory Folder Structure

```
sorting_visualization/
│
├── main.py
│
├── config/
│   ├── colors.py
│   ├── fonts.py
│   └── animation_constants.py
│
├── core/
│   ├── array_element.py
│   ├── array_group.py
│   ├── pointers.py
│   └── recursion_layout.py
│
├── algorithms/
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
├── scenes/
│   ├── intro/
│   │   └── title_scene.py
│   │
│   ├── quick_sort/
│   │   ├── overview_scene.py
│   │   ├── partition_scene.py
│   │   ├── recursion_scene.py
│   │   └── complexity_scene.py
│   │
│   ├── merge_sort/
│   │   ├── overview_scene.py
│   │   ├── split_scene.py
│   │   ├── merge_scene.py
│   │   └── complexity_scene.py
│   │
│   └── comparison/
│       ├── side_by_side_scene.py
│       └── final_summary_scene.py
│
├── assets/
│   ├── audio/
│   ├── images/
│   └── fonts/
│
├── utils/
│   ├── animation_helpers.py
│   ├── easing.py
│   └── validators.py
│
└── README.md
```

---

## 3. Folder Responsibilities (Strict)

### `algorithms/*/logic.py`

* Pure algorithm implementation
* No Manim imports allowed
* Outputs step-by-step states

---

### `algorithms/*/states.py`

* Converts algorithm steps into animation-ready states
* No rendering logic

---

### `core/`

* Visual primitives only (bars, arrows, containers)
* No algorithm awareness

---

### `scenes/`

* Assemble visuals using states
* No computation
* One concept per scene rule enforced

---

### `config/`

* Global constants only
* No animation code

---

## 4. Naming Rules

* Scene classes must end with `Scene`
* Visual components must end with `View`
* Algorithm state objects must end with `State`
* Constants files may not contain functions

---

## 5. Quality Gate (Must Pass Before Rendering)

Before rendering **any** scene:

* Colors follow semantic rules
* Motion communicates logic
* Scene explains only one idea
* No magic numbers
* No duplicated animation code


