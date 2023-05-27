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
    else:
        res = []
        for n in range(len(nums)):
            new_num = nums[n+1:]
            temp_res = n_sum(new_num, target - nums[n], level - 1)
            res.extend([x + [nums[n]] for x in temp_res])
        return res

if __name__ == "__main__":
    nums = [1,2,3,4,5,6,7,8,9,10]
    target = 22
    print(n_sum(nums, target, 5))