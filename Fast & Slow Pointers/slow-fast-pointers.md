# Fast and Slow Pointers (Floyd's Cycle Detection) Pattern

## Overview

The **Fast and Slow Pointers** technique is an algorithmic pattern that uses two pointers moving through a data structure at **different speeds**.

This technique is extremely useful when working with:

* Linked lists
* Cyclic structures
* Repeated transformations of numbers
* Detecting cycles

It is also known as **Floyd’s Cycle Detection Algorithm** or the **Tortoise and Hare algorithm**.

The core idea is simple:

* One pointer moves **one step at a time** → `slow`
* Another pointer moves **two steps at a time** → `fast`

If a **cycle exists**, the fast pointer will eventually meet the slow pointer.

---

# Core Idea

Two pointers traverse the structure with different speeds.

Typical setup:

```
slow = head
fast = head
```

Loop structure:

```
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
```

Possible outcomes:

* `fast` reaches the end → **no cycle**
* `fast` meets `slow` → **cycle detected**

---

# When to Use Fast & Slow Pointers

You should consider this technique when:

### 1. Detecting a cycle

Most classic usage.

Example:

* Linked List Cycle

The fast pointer eventually "laps" the slow pointer if a cycle exists.

---

### 2. Finding the start of a cycle

After detecting a cycle, you can find the **entry point** of the loop.

Steps:

1. Detect the meeting point
2. Reset one pointer to the head
3. Move both pointers one step at a time

The point where they meet again is the **start of the cycle**.

---

### 3. Finding the middle of a linked list

Example problem:

```
1 -> 2 -> 3 -> 4 -> 5
```

Result:

```
3
```

Algorithm:

```
slow = head
fast = head

while fast and fast.next:
    slow = slow.next
    fast = fast.next.next

return slow
```

When the fast pointer reaches the end, the slow pointer is at the **middle**.

---

### 4. Checking if a Linked List is a Palindrome

Steps:

1. Find the middle using fast & slow pointers
2. Reverse the second half
3. Compare both halves

---

### 5. Finding duplicate numbers in arrays

Some problems model arrays as **implicit linked lists**.

Example:

```
Find the duplicate number in an array
```

This can be solved using Floyd's algorithm without modifying the array.

---

# Why This Works

Imagine a circular track.

* Slow pointer moves **1 step**
* Fast pointer moves **2 steps**

Eventually, the faster runner will **catch up**.

This guarantees that if a cycle exists, the pointers will meet.

Mathematically, the distance between them decreases modulo the cycle length.

---

# Complexity

| Metric | Complexity |
| ------ | ---------- |
| Time   | O(n)       |
| Space  | O(1)       |

Only two pointers are used and each element is visited a constant number of times.

---

# Common Mistakes

### Forgetting null checks

Always write the loop as:

```
while fast and fast.next:
```

Otherwise you may get a **null pointer exception**.

---

### Confusing pointer speeds

Correct movement:

```
slow = slow.next
fast = fast.next.next
```

---

### Returning wrong middle element

For even length lists:

```
1 -> 2 -> 3 -> 4
```

Some implementations return:

* `2` (left middle)
* `3` (right middle)

Most interview solutions return **right middle**.

---

# Example Problem

## Linked List Cycle

Determine whether a linked list contains a cycle.

Example:

```
1 -> 2 -> 3 -> 4 -> 5
           ^       |
           |_______|
```

Solution:

```
def hasCycle(head):

    slow = head
    fast = head

    while fast and fast.next:

        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False
```

Time Complexity:

```
O(n)
```

Space Complexity:

```
O(1)
```

---

# Classic Interview Problems

Easy:

* Middle of the Linked List
* Linked List Cycle

Medium:

* Linked List Cycle II
* Find the Duplicate Number
* Palindrome Linked List

Hard:

* Circular Array Loop

---

# Mental Template for Recognizing the Pattern

Ask yourself:

1. Is there a **cycle or loop** in the structure?
2. Am I working with a **linked list**?
3. Do I need to detect repetition without extra memory?
4. Do I need the **middle element** of a list?

If the answer is yes, **fast & slow pointers may be the right approach**.

---

# Helpful Video Resources

### 1. NeetCode – Fast & Slow Pointers

[https://www.youtube.com/watch?v=gBTe7lFR3vc](https://www.youtube.com/watch?v=gBTe7lFR3vc)

Clear explanation with typical interview problems.

---

### 2. Floyd's Cycle Detection Algorithm

[https://www.youtube.com/watch?v=2Kd0KKmmHFc](https://www.youtube.com/watch?v=2Kd0KKmmHFc)

Excellent visualization of why the algorithm works.

---

### 3. Linked List Cycle – LeetCode Explanation

[https://www.youtube.com/watch?v=-YiQZi3mLq0](https://www.youtube.com/watch?v=-YiQZi3mLq0)

Practical walkthrough of solving the problem.

---

# Summary

The **Fast and Slow Pointers** pattern is a powerful technique used mainly with linked lists and cyclic structures.

Key advantages:

* Detects cycles efficiently
* Finds middle elements
* Uses constant extra memory
* Runs in linear time

Mastering this pattern will help you solve many classic interview problems involving linked lists and cycles.
