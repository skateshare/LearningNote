
test = [[1,2], [2,3], [2,4], [2,2], [3,5]]


res1 = sorted(test, key=lambda x: x[0])
print(res1)

# sort by first element , if first element is same , sort by second element
res2 = sorted(test, key=lambda x: (x[0], x[1]))
print(res2)

"""
expected
[[1,2], [2,2], [2,3], [2,4]]
"""


test = [-8,5,9,-2,-11,12,1,10,-5]


res = sorted(test, key=lambda x: x<0)
print(res)
# [5, 9, 12, 1, 10, -8, -2, -11, -5]

res = sorted(test, key=lambda x: (x<0, abs(x)))
print(res)
#[1, 5, 9, 10, 12, -2, -5, -8, -11]



