def is_palandrum(s):
    left=0
    right=len(s) -1
    while left < right:
        if s[left] != s[right]:
             return False
        else:
            left += 1
            right -= 1
    return  True

def isPalandrum(s):
    l=[]
    for i in reversed(range(len(s))):
        l.append(s[i])
    s1=''.join(l)
    return s == s1

def is_palandrum_r(s,low,high):
    if low >= high:
        return True
    if s[low] != s[high]:
        return  False
    return is_palandrum_r(s,low+1,high -1)

print(is_palandrum_r('aba',0,2))