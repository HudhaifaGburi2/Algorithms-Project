# Chapter 3: Recursion

Educational animation demonstrating recursion and the call stack using Manim (3Blue1Brown style).

## Overview

This animation covers:
1. **Introduction** - Nested boxes metaphor (Grandma's attic)
2. **Base Case vs Recursive Case** - Countdown example with color coding
3. **The Call Stack** - Push/pop visualization, LIFO concept
4. **Factorial Example** - Stack frames building and unwinding
5. **Recursion vs Iteration** - Side-by-side comparison
6. **Summary** - Key takeaways

## Project Structure

```
Chapter3_Recursion/
├── main.py                    # Main animation script
├── config/
│   ├── colors.py              # Color constants
│   ├── fonts.py               # Font size constants
│   └── animation_constants.py # Timing and layout constants
├── core/
│   ├── stack_frame.py         # Stack frame visualization
│   └── nested_box.py          # Nested box metaphor
├── algorithms/
│   └── recursion/logic.py     # Pure recursion examples
├── scenes/                    # Individual scene files (optional)
├── utils/
├── assets/                    # Audio, images, fonts
└── output/                    # Rendered videos
```

## Usage

### Render Full Animation

```bash
# Preview quality (480p, faster)
manim -pql main.py Chapter3Animation

# HD quality (1080p)
manim -pqh main.py Chapter3Animation
```

### Render Individual Scenes

```bash
manim -pql main.py IntroScene
manim -pql main.py BaseCaseScene
manim -pql main.py CallStackScene
manim -pql main.py FactorialScene
manim -pql main.py ComparisonScene
manim -pql main.py SummaryScene
```

## Color Semantics

| Color | Meaning |
|-------|---------|
| Green (#22C55E) | Base case / Completed |
| Orange (#F97316) | Recursive case |
| Purple (#8B5CF6) | Stack frame |
| Pink (#EC4899) | Active stack frame |
| Cyan (#06B6D4) | Return value |
| Yellow (#FACC15) | Key found / Highlight |

## Key Concepts Demonstrated

### Recursion
- A function that calls itself
- Must have a **base case** (stopping condition)
- Must have a **recursive case** (calls itself)

### Call Stack
- **LIFO**: Last In, First Out
- **Push**: Add function call to stack
- **Pop**: Remove when function returns
- Each frame uses memory

### Factorial Example
```
factorial(5) = 5 × 4 × 3 × 2 × 1 = 120

Stack builds:
  fact(1) ← base case, returns 1
  fact(2) ← returns 2 × 1 = 2
  fact(3) ← returns 3 × 2 = 6
  fact(4) ← returns 4 × 6 = 24
  fact(5) ← returns 5 × 24 = 120
```

### Recursion vs Iteration

| Aspect | Recursion | Iteration |
|--------|-----------|-----------|
| Clarity | Often cleaner | Can be verbose |
| Memory | Uses stack | Constant |
| Overflow | Possible | No risk |
| Performance | Similar | Similar |

## Key Takeaways

1. **Recursion** = function calling itself
2. **Base case** stops recursion; **recursive case** continues
3. **Call stack** = push/pop of function calls (LIFO)
4. Recursive calls consume memory; stack can grow large
5. Choose recursion for clarity, loops for performance if needed

## Dependencies

- Python 3.8+
- Manim Community Edition

## License

Educational use. Based on "Grokking Algorithms" Chapter 3.
