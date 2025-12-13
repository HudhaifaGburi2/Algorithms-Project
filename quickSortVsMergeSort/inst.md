

# 🎬 Manim Animation Specification

## **Quick Sort vs Merge Sort — Visual & Conceptual Comparison**

### 1. Objective

Create a **high-quality educational animation** using the **Manim library** that:

* Visually explains **Quick Sort** and **Merge Sort**
* Animates each algorithm step-by-step
* Compares **time complexity, space complexity, and behavior**
* Matches the **3Blue1Brown style**: clean visuals, smooth motion, strong intuition, minimal text, maximum clarity

---

### 2. Technical Requirements

* **Library**: Manim Community Edition (latest stable)
* **Resolution**: 1920×1080 (Full HD)
* **Frame Rate**: 60 FPS
* **Color Theme**: Dark background (`#0E1117`)
* **Font**: CMU Serif / Latin Modern Math
* **Camera**: Fixed frame with subtle zooms and pans

---

### 3. Visual Style (3Blue1Brown Inspired)

* Arrays represented as **bars or blocks**
* Motion conveys logic (not just movement)
* Color encodes meaning:

  * 🔵 Blue → Unprocessed elements
  * 🟡 Yellow → Pivot / Active element
  * 🟢 Green → Correctly placed
  * 🔴 Red → Comparisons
  * 🟣 Purple → Temporary storage (Merge Sort)
* Smooth easing (`rate_functions.ease_in_out_cubic`)
* No cluttered UI, no excessive labels

---

### 4. Scene Breakdown

---

## 🎥 Scene 1 — Title & Motivation

**Purpose**: Set context visually

**Animation**:

* Fade in title:

  ```
  Quick Sort vs Merge Sort
  ```
* Subtitle:

  ```
  Two Divide-and-Conquer Algorithms
  ```
* Show an unsorted array morphing into two branches

**Manim Objects**:

* `Text`, `VGroup`, `FadeIn`, `Transform`

---

## 🎥 Scene 2 — Initial Array Setup

**Purpose**: Introduce the data visually

**Animation**:

* Array of bars appears from bottom
* Values animate into place
* Bars labeled numerically (subtle)

**Example Array**:

```
[7, 2, 9, 4, 3, 8, 5]
```

---

## 🎥 Scene 3 — Quick Sort: Conceptual Overview

**Purpose**: Explain the intuition

**Animation**:

* Highlight a **pivot element** (middle or last)
* Draw arrows splitting array into:

  * Less than pivot
  * Greater than pivot

**Narrative Flow**:

> “Quick Sort selects a pivot and partitions the array around it.”

---

## 🎥 Scene 4 — Quick Sort: Step-by-Step Animation

**Purpose**: Show mechanics clearly

**Animation Details**:

1. Pivot turns **yellow**
2. Comparisons flash **red**
3. Elements slide left/right based on pivot
4. Pivot locks into position → turns **green**
5. Recursive calls visually shrink subarrays
6. Depth shown vertically (tree layout)

**Important**:

* Recursion shown spatially, not textually
* Use smooth rearrangement (`ReplacementTransform`)

---

## 🎥 Scene 5 — Quick Sort: Complexity Insight

**Overlay (minimal text)**:

```
Average: O(n log n)
Worst: O(n²)
Space: O(log n)
```

**Visual**:

* Balanced recursion tree → fast
* Skewed tree → slow (worst case)

---

## 🎥 Scene 6 — Merge Sort: Conceptual Overview

**Purpose**: Contrast approach

**Animation**:

* Original array splits in half
* Halves continue splitting until single elements
* Tree is **perfectly balanced**

**Narrative Flow**:

> “Merge Sort always divides evenly, regardless of values.”

---

## 🎥 Scene 7 — Merge Sort: Merging Process

**Purpose**: Show the key difference

**Animation Details**:

1. Single elements rise upward
2. Merge containers appear (**purple**)
3. Elements compared pairwise
4. Smaller element slides into output array
5. Final merge forms sorted array

**Key Emphasis**:

* Temporary arrays clearly visible
* Stable ordering preserved

---

## 🎥 Scene 8 — Merge Sort: Complexity Insight

**Overlay**:

```
Time: O(n log n)
Space: O(n)
Stable: Yes
```

**Visual**:

* Balanced recursion tree
* Extra memory highlighted

---

## 🎥 Scene 9 — Side-by-Side Comparison

**Purpose**: Direct visual contrast

**Layout**:

| Quick Sort     | Merge Sort        |
| -------------- | ----------------- |
| In-place       | Extra memory      |
| Faster average | Predictable       |
| Worst O(n²)    | Always O(n log n) |

**Animation**:

* Both algorithms sort the same array simultaneously
* Speed difference subtly visualized

---

## 🎥 Scene 10 — Final Summary

**Animation**:

* Sorted array fades to center
* Final takeaway text:

```
Quick Sort: Faster in practice
Merge Sort: Safer and stable
```

---

### 5. Manim Implementation Notes

* Use `VGroup` for array elements
* Use `always_redraw` for dynamic pointers
* Encapsulate logic in reusable classes:

  * `ArrayBar`
  * `PartitionScene`
  * `MergeTree`
* Avoid excessive narration text — let motion explain

---

### 6. Expected Output

* One **polished animation video**
* Suitable for:

  * YouTube
  * University lectures
  * Algorithm courses
* Quality comparable to **3Blue1Brown** educational visuals


