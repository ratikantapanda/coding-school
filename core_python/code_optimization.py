#  Try decorator caching.
###############################################
# def fibonacci(n):
#   if n == 0: # There is no 0'th number
#     return 0
#   elif n == 1: # We define the first number as 1
#     return 1
#   return fibonacci(n - 1) + fibonacci(n-2)

import functools

@functools.lru_cache(maxsize=128)
def fibonacci(n):
  if n == 0:
    return 0
  elif n == 1:
    return 1
  return fibonacci(n - 1) + fibonacci(n-2)

print(fibonacci(499))
#########################################################
#Learn itertools.
import itertools
iter = itertools.permutations(["Alice", "Bob", "Carol"])
permitations=list(iter)
print(permitations)

# Exit early.

import functools
@functools.lru_cache(maxsize=200)
def f1(name,i=10):
    print(name * i)
    print(f1.cache_info())

f1("rkp")


import functools


@functools.singledispatch
def myfunc(arg):
    print('default myfunc({!r})'.format(arg))


@myfunc.register(int)
def myfunc_int(arg):
    print('myfunc_int({})'.format(arg))


@myfunc.register(list)
def myfunc_list(arg):
    print('myfunc_list()')
    for item in arg:
        print('  {}'.format(item))

@myfunc.register(int,int)
def myfunc_list(arg):
    print('myfunc_int and int')
    print(arg[0] + arg[1])



myfunc('string argument')
myfunc(1)
myfunc(2.3)
myfunc(['a', 'b', 'c'])
