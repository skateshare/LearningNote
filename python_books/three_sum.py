from two_sum import two_sum
import copy


def three_sum(nums, target):
    res = []
    for n in range(len(nums)):
        new_num = nums[n+1:]
        temp_res = two_sum(new_num, target - nums[n])
        # print(temp_res)
        # print([x + [nums[n]] for x in temp_res])
        res.extend([x + [nums[n]] for x in temp_res])
    return res


if __name__ == "__main__":
    print(three_sum([1,2,3,4,5,6,7,8], 12))