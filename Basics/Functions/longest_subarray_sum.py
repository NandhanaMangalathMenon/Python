# Returns length of the longest subarray with sum k
def longest_subarray_sum(arr, k):
    max_len = 0
    for i in range(len(arr)):
        total = 0
        for j in range(i, len(arr)):
            total += arr[j]
            if total == k:
                max_len = max(max_len, j - i + 1)
    return max_len

print(longest_subarray_sum([10, 5, 2, 7, 1, -10], 15))  # 6
print(longest_subarray_sum([-5, 8, -14, 2, 4, 12], -5)) # 5
print(longest_subarray_sum([10, -10, 20, 30], 5))  # 0
