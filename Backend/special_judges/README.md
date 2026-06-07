# Special Judge System

## Purpose

The default judge system compares outputs using:

```python
actual_output == expected_output
```

This works only when a problem has exactly one valid output.

Some problems can have multiple correct outputs that differ only in ordering or formatting. For such problems, a Special Judge is required.

---

## Current Architecture

```text
special_judges/

├── README.md
├── __init__.py
├── registry.py
├── utils.py

└── judges/
    ├── three_sum.py
    ├── group_anagrams.py
    └── top_k_frequent.py
```

---

## Judge Selection Flow

### Run Example

```text
/run-example
        ↓
Check registry.py
        ↓
Special Judge Exists?
        ↓
YES → Use Special Judge
NO  → Use Normal Comparison
```

### Submit

```text
/submit
      ↓
Check registry.py
      ↓
Special Judge Exists?
      ↓
YES → Use Special Judge
NO  → Use Normal Comparison
```

---

## Registry

All Special Judges must be registered in:

```python
SPECIAL_JUDGES = {
    1: judge_three_sum,
    2: judge_group_anagrams,
    5: judge_top_k_frequent
}
```

The key is the problem ID.

The value is the corresponding judge function.

---

## Judge Interface

Every Special Judge must use the same function signature:

```python
def judge_name(
    user_output,
    expected_output,
    testcase
):
    return True
```

Parameters:

### user_output

Output produced by the user's solution.

### expected_output

Output stored in the testcase.

### testcase

Entire testcase dictionary.

Example:

```python
{
    "input": "...",
    "output": "..."
}
```

A judge may use testcase input directly if output comparison is insufficient.

---

## Current Special Judge Problems

### Problem 1 — 3Sum

Reason:

Multiple valid triplet orderings are possible.

Accepted:

```text
-1 -1 2
-1 0 1
```

and

```text
-1 0 1
-1 -1 2
```

Judge normalizes triplets before comparison.

---

### Problem 2 — Group Anagrams

Reason:

Group order and word order inside groups may vary.

Accepted:

```text
eat tea ate
tan nat
bat
```

and

```text
bat
nat tan
ate tea eat
```

Judge validates:

* all words used exactly once
* no extra words
* no missing words
* valid anagram grouping
* no split groups

---

### Problem 5 — Top K Frequent Elements

Reason:

Ordering may vary when frequencies tie.

Accepted:

```text
1 2
```

and

```text
2 1
```

when both values are valid top-k elements.

Judge validates:

* exactly k outputs
* no duplicates
* all outputs belong to the valid top-k frequency set

---

## Adding A New Special Judge

### Step 1

Create a new file:

```text
special_judges/judges/
```

Example:

```text
special_judges/judges/problem_41.py
```

---

### Step 2

Implement the judge function:

```python
def judge_problem_41(
    user_output,
    expected_output,
    testcase
):
    ...
```

Return:

```python
True
```

for accepted solutions.

Return:

```python
False
```

for incorrect solutions.

---

### Step 3

Register the judge inside:

```python
registry.py
```

Example:

```python
SPECIAL_JUDGES[41] = judge_problem_41
```

---

### Step 4

Add hidden testcases.

---

### Step 5

Verify:

* Run Example
* Submit
* Accepted
* Wrong Answer
* Runtime Error
* Time Limit Exceeded

continue to work correctly.

---

## Important Rule

Do not place Special Judge logic inside:

```text
execution_routes.py
```

All problem-specific judging logic must remain inside:

```text
special_judges/judges/
```

This keeps execution routes clean and allows future judges to be added without modifying the main judging workflow.


## Problem Classification

Special Judge Problems

1 -> 3Sum
2 -> Group Anagrams
5 -> Top K Frequent Elements

Normal Judge Problems

3 -> Product of Array Except Self
4 -> Longest Consecutive Sequence
6 -> Longest Substring Without Repeating Characters
7 -> Longest Repeating Character Replacement
8 -> Permutation in String
9 -> Minimum Size Subarray Sum
10 -> Maximum Average Subarray I
11 -> Container With Most Water
12 -> Valid Palindrome
13 -> Two Sum II
14 -> Move Zeroes
15 -> Squares of a Sorted Array