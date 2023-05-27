

def three_sum(nums, target):
    res = []
    for n in range(len(nums)):
        new_num = nums[n+1:]
        temp_res = two_sum(new_num, target - nums[n])
        res.extend([x + [nums[n]] for x in temp_res])
    return res

def four_sum(nums, taarget):
    res = []
    for n in range(len(nums)):
        new_nums = nums[n+1:]
        temp = three_sum(new_nums, target - nums[n])
        res.extend([x + [nums[n]] for x in temp])
    return res


def n_sum(nums, target,level):
    if level == 2:
        res = []
        ref = dict()
        for n in nums:
            if n not in ref.keys():
                ref[target -n] = n
            else:
                res.append([n, ref[n]])
        return res
    # elif level == 3:
    #     res = []
    #     for n in range(len(nums)):
    #         new_num = nums[n+1:]
    #         temp_res = n_sum(new_num, target - nums[n], 2)
    #         res.extend([x + [nums[n]] for x in temp_res])
    #     return res
    else:
        res = []
        for n in range(len(nums)):
            new_num = nums[n+1:]
            temp_res = n_sum(new_num, target - nums[n], level - 1)
            res.extend([x + [nums[n]] for x in temp_res])
        return res

if __name__ == "__main__":
    nums = [1,2,3,4,5,6,7,8,9,10]
    target = 19
    print(n_sum(nums, target, 3))