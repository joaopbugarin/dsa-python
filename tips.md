# Python Tips (WIP)
## Dictionaries

### Regular Dict
```python
d = {}
d["a"] = 1  # Set value
d.get("b", 0)  # Get with default

# Check before use
if "b" not in d:
    d["b"] = []
```

### defaultdict
```python
from collections import defaultdict

d = defaultdict(int)
d["a"] = 1  # Set value
d["b"]  # Auto-creates with default value (0 for int)
d["b"] += 1  # Just works, no KeyError
```

## Working with Lists

### Find Duplicates
Transform list into a set and compare lengths. Sets don't contain duplicates - they're automatically removed.
```python
has_duplicates = len(my_list) != len(set(my_list))
```

### List Comprehensions
A compact way to build lists from iterables.

**General form:**
```python
[expression for item in iterable if condition]
```

**Example:**
```python
filtered_line = [x for x in row if x.isdigit()]
```
This creates a new list containing only items from `row` that are digits.