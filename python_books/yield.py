


def test(target):
    for t in range(len(target)):
        yield target[t]
        print("Thank you")


g = test(["a", "bbb"])

print(next(g))
print(next(g))


# here's the take away : everytime hit yield , the function exit and next time will continue from the latest line 