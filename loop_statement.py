# how to use while statement
count = 0
while count < 5:
    print("%d less than 5" % count)
    count += 1
else:
    print("%d more than or equit to 5" % count)

# how to use for statement
print("----------------------")
list = ['ming', 1, 2.33, "hello", 100]
for ming in list:
    if ming == "hello":
        print("I got a hello")
for ming in list:
    print(ming)

# range() function
print("----------------------")
for ming in range(5):
    print(ming)

for ming in range(6, 7):
    print(ming)

# prime number
for num in range(2, 10):
    for i in range(2, num):
        if num % i == 0:
            print(num, "=", i, "*", num//i)
            break
    else:
        print("%d is a prime" % num)
