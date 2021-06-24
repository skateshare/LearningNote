"""
Minimum Subsequence in Non-Increasing Order(LeetCode 1403)
Given the array nums, obtain a subsequence of the array whose sum of elements is strictly
greater than the sum of the non included elements in such subsequence.
If there are multiple solutions, return the subsequence with minimum size and if there still exist
multiple solutions, return the subsequence with the maximum total sum of all its elements. A
subsequence of an array can be obtained by erasing some (possibly zero) elements from the array.
Note that the solution with the given constraints is guaranteed to be unique. Also return the answer
sorted in non-increasing order.

"""

def sol(nums):
    if len(nums) == 1:
        return nums
    nums.sort(reverse=True)
    res = [nums[0]]

    total = sum(nums)
    for i in range(1, len(nums) + 1):

        if res[-1] > total // 2:
            return nums[:len(res)]
        res.append(nums[i] + res[-1])


nums = [4,4,7,6,7]
print(sol(nums))