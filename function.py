

def func():      # function 1
    print("this is function 1")


def print_welcome(name):
    print("welcome %s" % name)


def func_arg(a, b, *args, **kwargs):
    print("a = ", a)
    print("b = ", b)
    print("arg = ", args)
    print("kwargs: ")

    for key, value in kwargs.items():
        print(key, "=", value)


func()
print_welcome("sherman")
func_arg(1, 2, 3, 4, m=5, n=6)

print("-----------")

c = (3, 4, 5)
d = {"m": 6, "n": 7}
func_arg(1, 2, *c, **d)   # pay attention to the function argument

a = 100
print("value address is %X " % id(a))  # use id() to check the value address
