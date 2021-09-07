def bubble_sort_1(a):
    for i in range(len(a)):
        for j in range(1, len(a) - i):
            if a[j] < a[j-1]:
                temp = a[j]
                a[j] = a[j-1]
                a[j-1] = temp

def bubble_sort_2(a):
    for i in range(len(a)):
        for j in range(len(a) -1 - i):
            if a[j + 1] < a[j]:
                temp = a[j]
                a[j] = a[j + 1]
                a[j + 1] = temp

def dutch_national_flag(a):
    low = 0
    middle = 0
    high = len(a) - 1
    pivot = 1
    while middle < high :
        if a[middle] > pivot:
            temp = a[middle]
            a[middle] = a[high]
            a[high] = temp
            high = high - 1
        if a[middle] < pivot:
            temp = a[middle]
            a[middle] = a[low]
            a[low] = temp
            low = low + 1
            middle = middle + 1
        if a[middle] == pivot:
            middle = middle + 1

a = [ 2,1,0,1,1,0,0,2,2,0,1,2,0]
dutch_national_flag(a)
print(a)

