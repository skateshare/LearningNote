

def devisor(x, y):
    return x // y



def complete_devisor(target):   # complete_devisor is the decorator, target is the function you want to decorates
    def helper(*args):  # helper hepls you , *args is the parameters of your target function 
        if not all(list(map(lambda x : isinstance(x, int), args))):
            return "value not right"
        return target(*args)

    return helper # return helper



@complete_devisor
def devisor(x, y):
    return x // y


print(devisor("i",5))

def newer(*args):
    return list(filter(lambda x : x == "a", args))

print(newer("a", "b", "c"))