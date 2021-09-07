# Time Complexity = O(n)
# Space complexcity = O(1)
def get_nth_fib(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    t1,t2 = 0,1
    i=0
    while i <= n-2 :
        t1,t2 = t2, t1 + t2
        i += 1
    return t1 + t2
def get_nth_fib_2(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    last_two=[0,1]
    counter = 3
    while counter <= n:
        next_fib= last_two[0] + last_two[1]
        last_two[0]=last_two[1]
        last_two[1] = next_fib
        counter += 1
    return last_two[1]
# Time Complexity = O(2 ^ n)
# Space complexcity = O(n)

def getNthFib(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return getNthFib(n - 1) + getNthFib(n - 2)



r=get_nth_fib_2(5)
print(r)
s=getNthFib(5)
print(s)