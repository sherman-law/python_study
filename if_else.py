age = int(input("please the age of your dog :\r\n"))
if age < 0:
    print("are you kidding me ?")
elif age == 1:
    print("the equivalent of 14-year-old.")
elif age == 2:
    print("the equivalent of 22-year-old.")
elif age > 2:
    human = 22 + (age - 2) * 5
    print("the age of person is %d." % human)

# tips of quit
input("click enter to quit")
