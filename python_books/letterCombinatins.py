def find_combinations(nums1, nums2):
    res = []
    for n1 in nums1:
        for n2 in nums2:
            res.append(n1+n2)
    return res

from functools import reduce
print(find_combinations(["ab", "c"], ["z", "zz"]))


def fine_letter_combo(nums):
    phone = {
        "2" : "abc",
        "3" : "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "9": "tuv",
        "0" : "xyz"
    }
    target = list(map(lambda x: phone[x], list(str(nums))))
    res = reduce(find_combinations, target)
    return res

print(fine_letter_combo(23))