import sys

# iterator using methor
list = [1, 2, 3, 4]
it = iter(list)
for x in it:
    print(x, end=" ")

print("\r\n--------------")

list = [9, 8, 7, 6]
it = iter(list)

while True:
    try:
        print(next(it))
    except StopIteration:
        sys.exit()

# maker using methor


def fibonacci(n):
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n):
            return
        yield a
        a, b = b, a + b
        counter += 1


f = fibonacci(11)
while True:
    try:
        print(next(f), end=" ")
    except StopIteration:
        sys.exit()
