#basic sort algorithms


def swap(alist, i, j):
    temp = alist[i]
    alist[i] = alist[j]
    alist[j] = temp


def select_sort1(alist):
    if len(alist) <= 1:
        return alist

    i = 0
    while i < len(alist)-1:
        minIndex = i
        j = i + 1
        while j < len(alist):
            if alist[j] < alist[minIndex]:
                minIndex = j
            j += 1


        if minIndex != i:
            swap(alist, minIndex, i)
        i += 1


# l1 = [5,3,1,2,4]
# select_sort(l1)
# print(l1)


def select_sort2(alist):
    # n = len(alist)
    for i in range(len(alist)):
        minIndex = i
        for j in range(i+1, len(alist)):

            if alist[minIndex] > alist[j]:
                # swap(alist, i, j)
                minIndex = j
        if minIndex != i:
            swap(alist, minIndex, i)




def bouble_sort(alist):
    # for i in range(len(alist)-1):
    #     if alist[i] > alist[i+1]:
    #         swap(alist, i, i+1)
    n = len(alist)
    while n > 1:
        swapped = False
        i = 0
        while i < n-1:
            if alist[i] > alist[i+1]:
                swap(alist, i, i+1)
                swapped = True
            i += 1

        if not swapped:
            return
        n -= 1



def insert_sort(alist):
    i = 1
    while i < len(alist):
        itemToInsert = alist[i]
        j = i-1
        while j >= 0:
            if itemToInsert < alist[j]:
                alist[j+1] = alist[j]
                j -= 1
            else:
                break

        alist[j+1] = itemToInsert
        i += 1




#advanced sort algorithms


def quick_sort(alist):
    quick_sort_helper(alist, 0, len(alist)-1)


def quick_sort_helper(alist, left, right):
    if left < right:
        pivotLocation = partition(alist, left, right)
        quick_sort_helper(alist, left, pivotLocation-1)
        quick_sort_helper(alist, pivotLocation+1, right)

def partition(alist, left, right):
    middle = (left + right) // 2
    pivot = alist[middle]
    swap(alist, middle, right)


    boundary = left
    for i in range(left, right):
        if alist[i] < pivot:
            swap(alist, i, boundary)
            boundary += 1
    swap(alist, boundary, right)

    return boundary



#归并排序多了一个辅助空间

def merge_sort(alist):
    if len(alist) <= 1:
        return alist

    middle = len(alist) // 2
    left = merge_sort(alist[:middle])
    right = merge_sort(alist[middle:])

    return merge(left, right)


def merge(left, right):
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result = result + left[i:]
    result = result + right[j:]

    return result



# l1 = [1,3,52,7,4,21]
# a = merge_sort(l1)
# print(a)


#binary search

def binary_search(alist, target):
    if not alist:
        return False
    left = 0
    right = len(alist)-1
    while left <= right:
        middel = (left + right) // 2
        if alist[middel] == target:
            return True
        elif alist[middel] > target:
            right = middel-1
        else:
            left = middel+1
    return False

l1 = [1,3,52,7,4,21]
print(binary_search(l1,2))
