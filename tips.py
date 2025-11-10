# Regular dict
d = {}
d["a"] = 1  # Set value
d.get("b", 0)  # Get with default
if "b" not in d:  # Check before use
    d["b"] = []

# defaultdict
from collections import defaultdict

d = defaultdict(int)
d["a"] = 1  # Set value
d["b"]  # Auto-creates with default
d["b"] += 1  # Just works
