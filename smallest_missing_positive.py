def solution(A):
    """
    Find the smallest positive integer (greater than 0) that does not occur in array A.

    Args:
        A: List of integers

    Returns:
        The smallest positive integer not in A

    Time Complexity: O(N) where N is the length of A
    Space Complexity: O(N) for the set storage
    """
    # Convert array to set for O(1) lookup
    num_set = set(A)

    # The answer must be in range [1, len(A) + 1]
    # If A contains all integers from 1 to N, the answer is N + 1
    # Otherwise, it's the first missing positive integer
    for i in range(1, len(A) + 2):
        if i not in num_set:
            return i


def test_solution():
    """Test the solution with the provided examples and edge cases"""

    # Test case 1: From problem description
    assert solution([1, 3, 6, 4, 1, 2]) == 5, "Test case 1 failed"
    print("✓ Test case 1 passed: [1, 3, 6, 4, 1, 2] → 5")

    # Test case 2: From problem description
    assert solution([1, 2, 3]) == 4, "Test case 2 failed"
    print("✓ Test case 2 passed: [1, 2, 3] → 4")

    # Test case 3: From problem description
    assert solution([-1, -3]) == 1, "Test case 3 failed"
    print("✓ Test case 3 passed: [-1, -3] → 1")

    # Additional edge cases
    assert solution([1]) == 2, "Test case 4 failed"
    print("✓ Test case 4 passed: [1] → 2")

    assert solution([2]) == 1, "Test case 5 failed"
    print("✓ Test case 5 passed: [2] → 1")

    assert solution([1, 2, 3, 4, 5]) == 6, "Test case 6 failed"
    print("✓ Test case 6 passed: [1, 2, 3, 4, 5] → 6")

    assert solution([2, 3, 4, 5]) == 1, "Test case 7 failed"
    print("✓ Test case 7 passed: [2, 3, 4, 5] → 1")

    assert solution([1000000]) == 1, "Test case 8 failed"
    print("✓ Test case 8 passed: [1000000] → 1")

    assert solution([-1000000, 0, 1000000]) == 1, "Test case 9 failed"
    print("✓ Test case 9 passed: [-1000000, 0, 1000000] → 1")

    print("\n✅ All test cases passed!")


if __name__ == "__main__":
    test_solution()
