import re

msg = "0917-872011-october"
pattern = "(\d{4})-(\d{6})-(\w*)"

res = re.search(pattern, msg)
print(re)
# res 本身是一個 re 物件

print(res.group())
# 0917-872011-october

print(res.group(0))
#0917-872011-october

print(res.group(1))
# 0917

print(res.group(2))
# 872011

print(res.group(3))
# october

res = re.findall(pattern, msg)
print(res)
# [('0917', '872011', 'october')]


res = re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')
print(res)
#['foot', 'fell', 'fastest']