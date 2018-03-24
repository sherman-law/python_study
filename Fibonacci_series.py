# Fibonacci series

a, b = 0, 1            # a = 0, b = 1
while b < 10:
    print(b, end=',')  # how to use "end" key word
    a, b = b, a+b      # a = b, b = a + b

b = 1
a = 0
while b < 10:          # while statement
    print(b)
    a, b = b, a+b      # a = b, b = a + b
