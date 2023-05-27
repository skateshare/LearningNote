from three_sum import three_sum


def four_sum(nums, taarget):
    res = []
    for n in range(len(nums)):
        new_nums = nums[n+1:]
        temp = three_sum(new_nums, target - nums[n])
        res.extend([x + [nums[n]] for x in temp])
    return res



if __name__ == "__main__":
    nums = [1,2,3,4,5,6,7,8]
    target = 15
    print(four_sum(nums, target))