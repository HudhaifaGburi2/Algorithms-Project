# Chapter 5: Hash Tables

Educational animation demonstrating hash tables, hash functions, and O(1) lookup using Manim (3Blue1Brown style).

## Overview

This animation covers:
1. **Introduction** - The O(1) lookup problem vs O(n) and O(log n)
2. **Hash Functions** - String → Number mapping
3. **Phone Book** - Lookup use case
4. **Preventing Duplicates** - Voting system
5. **Caching** - Browser/server cache
6. **Collisions** - Chaining solution
7. **Performance** - Average O(1) vs Worst O(n)
8. **Load Factor** - When to resize
9. **Summary** - Key takeaways

## Project Structure

```
Chapter5_HashTables/
├── main.py                    # Main animation script
├── config/
│   ├── colors.py              # Hash table colors
│   ├── fonts.py               # Font constants
│   └── animation_constants.py # Timing/layout constants
├── core/
│   └── hash_table_view.py     # Hash table visualization
├── algorithms/
│   └── hash_table/logic.py    # Pure hash table logic
├── scenes/                    # Individual scene files
├── utils/
├── assets/
└── output/
```

## Usage

### Render Full Animation

```bash
# Preview quality (480p)
manim -pql main.py Chapter5Animation

# HD quality (1080p)
manim -pqh main.py Chapter5Animation
```

### Render Individual Scenes

```bash
manim -pql main.py IntroScene
manim -pql main.py HashFunctionScene
manim -pql main.py PhoneBookScene
manim -pql main.py DuplicatesScene
manim -pql main.py CachingScene
manim -pql main.py CollisionsScene
manim -pql main.py PerformanceScene
manim -pql main.py LoadFactorScene
manim -pql main.py SummaryScene
```

## Color Semantics

| Color | Meaning |
|-------|---------|
| Purple (#8B5CF6) | Hash function |
| Cyan (#06B6D4) | Keys (input) |
| Pink (#EC4899) | Values (stored) |
| Orange (#F97316) | Linked list chains |
| Teal (#14B8A6) | Cache operations |
| Green (#10B981) | O(1) / Success |
| Amber (#F59E0B) | Warning / O(log n) |
| Red (#EF4444) | Error / O(n) |

## Key Concepts

### Hash Function
```
hash("apple") → 3
hash("milk") → 0
```
- Same input always gives same output
- Maps any key to array index
- Good hash = even distribution

### Hash Table Operations
```python
# Create
book = {}

# Insert - O(1)
book["apple"] = 0.67

# Lookup - O(1)
price = book["apple"]

# Delete - O(1)
del book["apple"]
```

### Complexity

| Operation | Average | Worst |
|-----------|---------|-------|
| Search | O(1) | O(n) |
| Insert | O(1) | O(n) |
| Delete | O(1) | O(n) |

### Collisions
- Same hash value for different keys
- Solution: Chaining (linked list)
- Worst case: All keys in one chain → O(n)

### Load Factor
```
Load Factor = Items / Slots
```
- Keep below 0.7
- When exceeded: Double size, rehash all
- Resizing is O(n) but rare → Amortized O(1)

## Use Cases

1. **Phone Book** - Name → Number lookup
2. **DNS** - Domain → IP address
3. **Caching** - URL → Page content
4. **Voting** - Prevent duplicate votes
5. **Deduplication** - Check if item exists

## Key Takeaways

1. Hash tables provide O(1) average lookup
2. Hash function maps keys to array indices
3. Collisions handled by chaining
4. Keep load factor < 0.7
5. Perfect for lookups, caching, deduplication

## Dependencies

- Python 3.8+
- Manim Community Edition

## License

Educational use. Based on "Grokking Algorithms" Chapter 5.
