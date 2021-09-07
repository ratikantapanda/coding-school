a=[1,2,3,4]

def array_products(a):
    left=[None]*len(a)
    right=[None]*len(a)

    l=1
    r=1
    for i in range(len(a)):
        if i ==0:
            left[i]=1
            right[len(a)-1 -i]=1
        else:
            left[i]=left[i-1]*a[i-1]
            right[len(a) - 1 - i] = right[len(a)-i]*a[len(a)-i]

    prod=[None] * len(a)
    for i in range(len(a)):
        prod[i]=left[i] * right[i]
    print(prod)
def a_prod(a, left,idx):
    if idx == len(a):
        return 1
    curr=a[idx]
    right=a_prod(a,left*curr,idx+1)
    a[idx]=left * right
    return curr * right

b=[1,2,3,4]
print(b)
a_prod(b,1,0)
print(b)