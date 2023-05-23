

test1 = [1,1]

print(all(test1))

test2 = [0, 1]
print(all(test2))


test3 = []
print(all(test3))


# this is how all function implemented
def implement_all(iterable_):
    for i in iterable_:
        if not i:
            return False
    return True

print(implement_all(test1))
print(implement_all(test2))
print(implement_all(test3))

