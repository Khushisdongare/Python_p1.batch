# Create two frozensets
A = frozenset([10, 20, 30, 40])
B = frozenset([30, 40, 50, 60])

# Union
print("Union:", A | B)

# Intersection
print("Intersection:", A & B)

# Difference (A - B)
print("Difference (A - B):", A - B)

# Symmetric Difference
print("Symmetric Difference:", A ^ B)

# Superset check
print("Is A a superset of {10, 20}?:", A.issuperset({10, 20}))

# Try to add an element to A (will raise an error)
try:
    
    A.add(70)
except AttributeError as e:
    print("Error when trying to add to frozenset A:", e)

# Length of A and B
print("Length of A:", len(A))
print("Length of B:", len(B))
