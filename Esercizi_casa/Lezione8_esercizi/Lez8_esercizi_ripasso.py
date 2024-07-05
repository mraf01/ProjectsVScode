# Esercizio 1: Number of Beautiful Subsets

def is_beautiful(subset, k):
    for i in range(len(subset)):
        for j in range(i + 1, len(subset)):
            if abs(subset[j] - subset[i]) == k:
                return False
    return True

def count_beautiful_subsets(nums, k):
    def generate_subsets(index, current):
        if index == len(nums):
            if current:
                subsets.append(current[:])
            return
        current.append(nums[index])
        generate_subsets(index + 1, current)
        current.pop()
        generate_subsets(index + 1, current)

    subsets = []
    generate_subsets(0, [])
    
    count = 0
    for subset in subsets:
        if is_beautiful(subset, k):
            count += 1
    return count

# Esercizio 2: Combinations

def combine(n, k):
    def backtrack(start, path):
        if len(path) == k:
            result.append(path[:])
            return
        for i in range(start, n + 1):
            path.append(i)
            backtrack(i + 1, path)
            path.pop()
    
    result = []
    backtrack(1, [])
    return result

# Esercizio 3: Generate Parentheses

def generate_parenthesis(n):
    def backtrack(S, left, right):
        if len(S) == 2 * n:
            result.append(S)
            return
        if left < n:
            backtrack(S + "(", left + 1, right)
        if right < left:
            backtrack(S + ")", left, right + 1)
    
    result = []
    backtrack("", 0, 0)
    return result

if __name__ == "__main__":
    # Test esercizio 1
    print("Number of Beautiful Subsets:")
    print(count_beautiful_subsets([2, 4, 6], 2))  # Output: 4
    print(count_beautiful_subsets([1], 1))        # Output: 1

    # Test esercizio 2
    print("\nCombinations:")
    print(combine(4, 2))  # Output: [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
    print(combine(1, 1))  # Output: [[1]]

    # Test esercizio 3
    print("\nGenerate Parentheses:")
    print(generate_parenthesis(3))  # Output: ["((()))","(()())","(())()","()(())","()()()"]
    print(generate_parenthesis(1))  # Output: ["()"]