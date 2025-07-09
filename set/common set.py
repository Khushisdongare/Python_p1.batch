# Create the sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Union
union_set = set1 | set2
print("Union:", union_set)

# Intersection
intersection_set = set1 & set2

print("Intersection:", intersection_set)

# Difference (set1 - set2)
difference_set = set1 - set2
print("Difference (set1 - set2):", difference_set)

# Symmetric Difference
symmetric_difference_set = set1 ^ set2
print("Symmetric Difference:", symmetric_difference_set)

# Check if set1 is a subset of set2
is_subset = set1.issubset(set2)
print("Is set1 a subset of set2?:", is_subset)

# Modify sets
set1.add(9)
set2.discard(8)  # discard won't raise an error if 8 is not in set2

# Print final modified sets
print("Modified set1:", set1)
print("Modified set2:", set2)
