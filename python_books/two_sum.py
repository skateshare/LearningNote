

def two_sum(nums, target):
    ref = dict()
    res = []
    for n in nums:
        if n not in ref.keys():
            ref[target - n] = n
        else:
            res.append([n, ref[n]])
    return res



res = two_sum([1,2,3,4,5,6], 7)
print(res)