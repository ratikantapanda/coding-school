# bubble sort
###############################################################
# Time complexcity - O(N^2)
# In bestcase - O(N), When aray is sorted
# Space complexcity - O(1)
###################################################################
# helper function
def swap(a, i, j):
    a[i],a[j] = a[j], a[i]

def bubble_sort(a):
    isSorted = False
    counter = 0
    while isSorted != True:
        isSorted = True
        for i in range(len(a) - 1 - counter):
            if a[i] > a[i+1]:
                swap(a, i, i+1)
                isSorted = False
        counter += 1
    return a
##########################################################################
# Insertion sort
# O(N^2) time / O(1)  space
# In bestcase - O(N) time, When aray is sorted
#########################################################################
def insertion_sort(a):
    for i in range(1,len(a)):
        j=i
        while j > 0 and a[j] < a[j-1]:
            swap(a,j-1,j)
            j -= 1
##############################################################################
# selection sort
# O(N ^ 2) time /O(1) space
#################################################################################
def selection_sort(a):
    current_index=0
    while current_index < len(a) - 1:
        smallest_index = current_index
        for i in range(current_index + 1, len(a)):
            if a[i] < a[smallest_index]:
                smallest_index = i
        swap(a, smallest_index, current_index)
        current_index += 1

a=[3,5,2,8,10,6]
selection_sort(a)
print(a)