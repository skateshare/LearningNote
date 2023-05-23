
import copy 


target = [1,2,3,[4,5]]

assing_target = target
shallow_target = copy.copy(target)
deep_target = copy.deepcopy(target)


print("=================")
print(id(target))
print(id(assing_target))
print(id(shallow_target))
print(id(deep_target))

target[0] = 10


print("=================")
print(target)
print(assing_target)
print(shallow_target)
print(deep_target)


target[3][0] = 7

print("=================")
print(target)
print(assing_target)
print(shallow_target)
print(deep_target)

shallow_target[3][1] = 11

print("=================")
print(target)
print(assing_target)
print(shallow_target)
print(deep_target)



shallow_target[2] = 0

print("=================")
print(target)
print(assing_target)
print(shallow_target)
print(deep_target)



deep_target[2] = 1

print("=================")
print(target)
print(assing_target)
print(shallow_target)
print(deep_target)