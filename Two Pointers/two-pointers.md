# Two Pointers Pattern

## Overview

The **Two Pointers** technique is a common algorithmic pattern used to solve problems involving arrays, strings, or linked lists by maintaining two indices (pointers) that move through the data structure.

Instead of using nested loops (which often leads to `O(n^2)` time complexity), the two pointers technique usually reduces the complexity to **O(n)**.

It is extremely common in coding interviews and appears frequently in problems involving:

* Sorted arrays
* Pairs or triplets of elements
* Palindromes
* Subarrays or substrings
* In‑place modifications

---

# Core Idea

Two variables (pointers) track positions in a data structure and move based on some condition.

Example:

```
left = 0
right = len(array) - 1
```

The pointers move depending on the problem constraints.

Typical movements:

* Move **left pointer right** → `left += 1`
* Move **right pointer left** → `right -= 1`

The goal is usually to **reduce the search space** efficiently.

---

# When to Use Two Pointers

You should consider this pattern when:

### 1. The input is sorted

Many two‑pointer problems rely on sorted data.

Examples:

* Two Sum (sorted array)
* 3Sum
* Container With Most Water

### 2. You need to check pairs

Example:

Find two elements whose sum equals a target.

Instead of checking every pair (`O(n^2)`), you can solve it in `O(n)`.

### 3. Palindrome problems

Checking if a string reads the same forward and backward.

```
left -> start
right -> end
```

Compare characters and move inward.

### 4. In‑place array operations

Examples:

* Remove duplicates
* Move zeros
* Reverse array

### 5. Merging two sorted arrays

Used heavily in merge algorithms.

---

# Opposite Direction Pointers

Pointers start at both ends of the array.

```
left = 0
right = n - 1
```

They move toward each other.

Used in:

* Palindrome checking
* Pair sum problems
* Container With Most Water

Example logic:

```
while left < right:
    current_sum = nums[left] + nums[right]

    if current_sum == target:
        return [left, right]

    elif current_sum < target:
        left += 1

    else:
        right -= 1
```

Why this works:

Because the array is sorted, moving pointers changes the sum in a predictable direction.

---

# Complexity

Typical complexity:

| Metric | Complexity |
| ------ | ---------- |
| Time   | O(n)       |
| Space  | O(1)       |

Because each pointer usually moves across the array **at most once**.

---

# Common Mistakes

### Off‑by‑one errors

Confusion between:

```
while left < right
```

and

```
while left <= right
```

### Forgetting sorted requirement

Some problems require sorting first.

Sorting cost:

```
O(n log n)
```

### Pointer updates

Moving the wrong pointer can break the logic.

Always reason about:

"Which movement brings us closer to the answer?"

---

# Example Problem

## Two Sum (Sorted Array)

Given a sorted array of integers, find two numbers that add up to a target.

Example:

```
nums = [1,2,4,6,10]
target = 8
```

Solution:

```
def two_sum(nums, target):
    left = 0
    right = len(nums) - 1

    while left < right:
        s = nums[left] + nums[right]

        if s == target:
            return [left, right]

        elif s < target:
            left += 1

        else:
            right -= 1
```

Time complexity:

```
O(n)
```

---

# Classic Interview Problems

Practice these problems to master the pattern:

Easy:

* Two Sum II
* Valid Palindrome
* Reverse String
* Remove Duplicates from Sorted Array

Medium:

* Container With Most Water
* 3Sum
* 3Sum Closest
* Sort Colors

Hard:

* Trapping Rain Water

---

# Mental Template for Recognizing Two Pointers

Ask yourself:

1. Is the array sorted?
2. Am I looking for pairs or triplets?
3. Can I reduce `O(n^2)` to `O(n)` by tracking two indices?
4. Can I solve this in‑place with two indices?

If the answer is **yes**, two pointers may work.

---

# Additional Learning Resources

### NeetCode Roadmap

[https://neetcode.io/roadmap](https://neetcode.io/roadmap)

Great structured path for coding interview preparation.

---

### LeetCode Two Pointers Tag

[https://leetcode.com/tag/two-pointers/](https://leetcode.com/tag/two-pointers/)

A large collection of problems using this pattern.

---

# Summary

The **Two Pointers** pattern is one of the most important techniques for coding interviews.

Key benefits:

* Reduces `O(n^2)` brute force solutions to `O(n)`
* Uses constant extra memory
* Works extremely well with sorted arrays and pair problems

Mastering this technique will significantly improve your ability to solve array and string problems efficiently.
