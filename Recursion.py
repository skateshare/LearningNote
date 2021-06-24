"""
Three element for recursion :
1) base case (to leave recursion)
2) recursive case (call self)
3) recursive case get closer and closer to the base case

times to use recursion:
1) Tree related or convert something into tree
2) divide and conquer has high chance to use recursion !
3) if the problem can be divided into small , identical ones !
suitable for :
merge sort
quick sort
tree traversal
graph traversal

good part of recursion :
1) readable
2) sometimes we don't know the limit to stop iteration

drawback of recursion :
1) stack overflow  space complexity
2) sometimes it cost more time complexity!


"""

def factorial(n):
    if n == 1:
        return 1
    else:
        return n*factorial(n-1)



counter = 0
def fabonicci(n):  # O(2^n)   !!
    global counter
    counter += 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fabonicci(n-1) + fabonicci(n-2)


# this method can be think of DP or bottom up approach
def fabonicci2(n):  # O(n)
    arr = [0,1]
    while True:
        if len(arr) >= n+1:
            break
        arr.append(arr[-1]+arr[-2])

    return arr[n]

# use dynamic programming
# time complexity O(N) but cost more space comlexity
# and besides , still slightly slower thatn fabonicci2 which uses arr method
def fabonicci3(n, rec):
    global counter
    counter += 1
    if rec.get(n) != None:
        return rec[n]
    else:
        if n == 0:
            rec[0] = 0
            return 0
        elif n == 1:
            rec[1] = 1
            return 1
        else:
            rec[n] = fabonicci3(n-1, rec) + fabonicci3(n-2, rec)

            return rec[n]

rec = dict()
fabonicci3(10, rec)
print(counter)



# use recursion
def reverseWord(word):
    if len(word) == 0:
        return ""
    else:
        return word[-1] + reverseWord(word[:-1])

# use iteration
def reverseWord2(word):
    res = ""
    for w in word:
        res = w + res
    return res

print(reverseWord("October"))
print(reverseWord2("October"))