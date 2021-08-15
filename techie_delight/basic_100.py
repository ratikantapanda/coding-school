#reverse a string

def reverse_string(a):
    b = [0]*len(a)
    j = 0
    for i in range(len(a) - 1, -1, -1):
        b[j] = a[i]
        j = j + 1
    return ''.join(b)


s1 = 'ABCDEFGH'
result = reverse_string(s1)
print(result)

s2 ="RKPPANDA"
s3=s2[::-1]
s4=''.join(reversed(s2))
print(s3)
print(s4)
