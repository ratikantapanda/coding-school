def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_whee():
    print("Whee!")

#say_whee = my_decorator(say_whee)

say_whee()

def say_hi(func):
    def wrapper(*args,**kwargs):
        print("Hi")
        func(*args,**kwargs)
        print("Bye")
    return wrapper
@say_hi
def greet(name):
    print(f'{name}')

greet("ratikanta")