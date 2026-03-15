Given a 1-based indexed integer array `nums` that **is sorted in non-decreasing order**, along with an integer `target`,
find two elements in the array such that their sum is equal to `target`.

If such a pair exists, return the indices of the two elements in **increasing** order. 

If **no** such pair exists, return `[-1, -1]`.

---
**Example 1**:

**Input**: `nums` = [2,7,11,15], `target` = 9

**Output**: `[1,2]`

**Explanation**: The sum of 2 and 7 is 9. Therefore, `index1` = 1, `index2` = 2. We return `[1, 2]`.

---

**Example 2**:

**Input**: `numbers` = [1, 3, 4, 6, 8, 11], `target` = 6

**Output**: `[1,3]`

**Explanation**: The sum of 2 and 4 is 6. Therefore `index1` = 1, `index2` = 3. We return `[1, 3]`.

---

**Example 3**:

**Input**: `numbers` = [-1,0], `target` = -1

**Output**: `[1,2]`

**Explanation**: The sum of -1 and 0 is -1. Therefore `index1` = 1, `index2` = 2. We return `[1, 2]`.

---

**Constraints**:

2 <= numbers.length <= 3 * 104

-1000 <= numbers[i] <= 1000

numbers is sorted in non-decreasing order.

-1000 <= target <= 1000

The tests are generated such that there is exactly one solution.

---

**SOURCE**:
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

---