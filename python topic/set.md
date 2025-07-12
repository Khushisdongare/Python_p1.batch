# Python Sets

A **set** is an unordered collection of unique elements. Sets are **mutable**, but the elements must be **immutable** (e.g., numbers, strings, tuples).

### ✅ Creating Sets

- s1 = {1, 2, 3}
- s2 = set([4, 5, 6])
- s3 = set("hello")   # {'e', 'h', 'l', 'o'}
- empty = set()       # NOT {} (that's an empty dict)


## Operation
```python

a = {1, 2, 3}
b = {3, 4, 5}

a.union(b)         # {1, 2, 3, 4, 5}
a.intersection(b)  # {3}
a.difference(b)    # {1, 2}
a.symmetric_difference(b)  # {1, 2, 4, 5}
