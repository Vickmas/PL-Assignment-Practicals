# Set Operations Implementation
def union_sets(set1, set2):
    """Return the union of two sets."""
    return set1.union(set2)

# Test Cases for Set Operations
def test_union_sets():
    print("\n# TESTING UNION OF SETS")

    # Test case 1: Union of two disjoint sets
    set1 = {1, 2, 3}
    set2 = {4, 5, 6}
    print("Set 1:", set1)
    print("Set 2:", set2)
    print("Union of Disjoint sets:", union_sets(set1, set2))

    # Test case 2: Union of two intersecting sets
    set1 = {1, 2, 3}
    set2 = {3, 4, 5}
    print("\nSet 1:", set1)
    print("Set 2:", set2)
    print("Union of Intersecting sets:", union_sets(set1, set2))

    # Test case 3: Union of an empty set with another set
    set1 = set()
    set2 = {1, 2, 3}
    print("\nSet 1:", set1)
    print("Set 2:", set2)
    print("Union of empty and full set:", union_sets(set1, set2))

    # Test case 4: Union of two sets with duplicate elements
    set1 = {1, 2, 2, 3}
    set2 = {3, 3, 4, 5}
    print("\nSet 1:", set1)
    print("Set 2:", set2)
    print("Union of similar sets:", union_sets(set1, set2))

# Execute Test Cases
if __name__ == "__main__":
    test_union_sets()
