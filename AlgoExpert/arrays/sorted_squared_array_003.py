def sorted_squared_array(array):
    array.sort()
    sorted_array=[None] * len(array)
    left=0
    right=len(array) -1
    i=len(sorted_array) -1
    while left <= right:
        x=array[left] ** 2
        y=array[right] ** 2
        if x > y:
            sorted_array[i]=x
            i -= 1
            left += 1
        else:
            sorted_array[i]=y
            i -= 1
            right -= 1
    return sorted_array

def sorted_sqr_arr(arr):
    arr.sort()
    sorted_arr = [None for _ in arr]
    left=0
    right = len(arr) - 1
    for i in reversed(range(len(arr))):
        if abs(arr[left]) > abs(arr[right]):
            sorted_arr[i]=arr[left] * arr[left]
            left += 1
        else:
            sorted_arr[i] = arr[right] * arr[right]
            right -= 1
    return sorted_arr



a=[-9,-3,2,5,8,11]
b=sorted_squared_array(a)
print(a, '===>',b )

b=sorted_sqr_arr(a)
print(a, '===>',b )



