

def singleNumber(nums):
    nums.sort()
    for i in range(1, len(nums), 2):
        if nums[i] != nums[i-1]:
            return [nums[i-1]]

    return []


print(singleNumber([1,3,1,3,5,4,4]))


