# Bubble
## Concept
Definition: A sorting algorithm that compares adjacent elements and swaps them based on a specific criterion

Key Characteristic: The largest value "bubbles up" to the end of the list, similar to air bubbles rising in water.

Difficulty/ Efficiency: Esay to implement / Low effieciency(O(n^2))

---
## Working Principle

Bubbles sort operates by progressively "fixing" the position of the largest number at the end of the list with each pass

1. Compare & Swap: Start from the beginning and compare two adjacent numbers.
2. Move: If the front number is larger than the back number, they swap postions.
3. Fix: By the end of one pass, the largest number is guaranteed to be in the last postion.
4. Repeat: Repeat steps 1-3 for the remaining unsorted postion of the list.

---
Optimized Implementation
Optimization Logic: Even if the list is already sorted, the basic code continues comparing.
By using a Flag variable, we can check if any swap occurred.
If noo swap happened during a pass, the list is already sorted, and we break the loop early.

```py
def bubble_sort_optimized():
    n = len(arr)

    for i in range(n-1, 0, -1):
        swapped = False
```

## Code Analysis
range(n -1, 0, -1)
range(i)