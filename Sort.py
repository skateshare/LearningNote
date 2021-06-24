"""
why sorting sorting is so important :
when it comes to mega data, it cost lots of time !
Ex: google search result, Amazon products ...

bubble sort
insertion sort
select sort
merge sort
quick sort

when to use which cheet sheet:
buble sort and selection sort >> don't use it
insertion sort >> if most data are already sorted, or useful for small size of data!
merge sort and quick sort are pretty much the same in thinking ,
but quck sort trade worst case time complexity for good memory space
when stable issue is considered >> use merge sort
"""
from LinkList import LinkList

class Sort():
    def __init__(self, arr):
        self.arr = arr

    # buble sort  time:O(N^2) space:O(1)
    def bubbleSort(self):
        for i in range(len(self.arr)-1):
            for p in range(len(self.arr)-1):
                if self.arr[p] > self.arr[p+1]:
                    temp = self.arr[p+1]
                    self.arr[p+1] = self.arr[p]
                    self.arr[p] = temp
        return self.arr

    def selectionSort(self):
        for i in range(len(self.arr)-1):
            mini = i
            for j in range(i+1, len(self.arr)):
                if self.arr[j] < self.arr[mini]:
                    mini = j
            temp = self.arr[i]
            self.arr[i] = self.arr[mini]
            self.arr[mini] = temp
        return self.arr


    # suitable when arr is almost sorted !!  O(N^2)
    # insertion sort 適合用於 almost sorted 的 case  會很快
    # 但我用link list 的方師來 implement 就會失去 insertion sort 的優勢！
    def insertionSort_NoGood(self):
        linklist = LinkList()
        linklist.append(self.arr[0])
        for i in range(1, len(self.arr)):
            counter = 0
            ptr = linklist.head
            while True:
                if ptr.val < self.arr[i]:
                    counter += 1
                if ptr.next == None:
                    break

                ptr = ptr.next

            linklist.insert(counter, self.arr[i])
        return linklist.outputArray()

    # 使用此方式則假設大筆資料幾乎sort 完成 只有K 筆資料未排序
    # 則 time complexity = O(KN)
    def insertionSort(self):
        for i in range(1, len(self.arr)):
            if self.arr[i] > self.arr[i-1]:
                continue
            elif self.arr[i] < self.arr[0]:
                self.arr[:i+1] = [self.arr[i]] + self.arr[:i]
            else:
                for j in range(i):
                    if self.arr[:i][j] < self.arr[i] and self.arr[:i][j+1] > self.arr[i]:
                        self.arr[:i+1] = self.arr[:j+1] + [self.arr[i]] + self.arr[j+1:i]
                        break
        return self.arr

    def get(self):
        return self.arr

    # time complexity O(NlogN) is a stable sort !
    def mergeSort(self, arr):
        if len(arr) == 1:
            return arr

        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]

        return self.merge(self.mergeSort(left), self.mergeSort(right))



    def merge(self, left, right):
        temp = []
        lptr = 0
        rptr = 0

        while True:
            if lptr == len(left) and rptr == len(right):
                return temp
            elif lptr == len(left) and rptr != len(right):
                return temp + right[rptr:]
            elif lptr != len(left) and rptr == len(right):
                return temp + left[lptr:]
            else:
                if left[lptr] <= right[rptr]:
                    temp.append(left[lptr])
                    lptr += 1
                else:
                    temp.append(right[rptr])
                    rptr += 1

    # 這個 implementation 方法不是一班的 quick sort , 因為 space complexity 不是O(logN)
    # 但是這個 implementation 可以維持 stable 的特性！
    """def quickSort(self, arr):
        if len(arr) == 0:
            return []
        if len(arr) == 1:
            return arr

        pivot = arr[-1]
        left = []
        right = []
        for i in range(len(arr)-1):
            if arr[i] < pivot:
                left.append(arr[i])
            else:
                right.append(arr[i])

        return self.quickSort(left) + [pivot] + self.quickSort(right)"""

    def quickSort(self, arr):
        if len(arr) == 0:
            return []
        if len(arr) == 1:
            return arr

        pos = len(arr) - 1
        pivot = arr[pos]
        index = 0
        for i in range(len(arr)-1):
            if arr[i] <= pivot:
                temp = arr[i]
                arr[i] = arr[index]
                arr[index] = temp
                index += 1
        temp = arr[index]
        arr[index] = pivot
        arr[pos] = temp

        return self.quickSort(arr[:index]) + [arr[index]] + self.quickSort(arr[index+1:])







"""arr = [99, 44, 6, 2, 15, 5, 63, 87, 283, 4, 0]
mySort = Sort(arr)
print(mySort.insertionSort())"""

"""# test mergeSort
arr = [99, 44, 6, 2, 15, 5, 63, 87, 283, 4, 0]
mySort = Sort(arr)
print(mySort.mergeSort(mySort.get()))"""

arr = [99, 44, 6, 2, 15, 5, 63, 87, 283, 4, 0]
mySort = Sort(arr)
print(mySort.quickSort(mySort.get()))



