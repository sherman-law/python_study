counter = 100     # int variable
tall = 177.5      # float variable
name = "sherman"  # string

print(counter)
print(tall)
print(name)

# define variable
a = b = c = 1
e, f, g = 1, 1.2, "ming"
print(a, b, c)
print(e, f, g)

# --- 5 data type -----

# 1.Number
#    * int
#    * long
#    * float
#    * complex

# 2.String(use identifier: "", '', """""")
string = "hello word,"

print(string)                  # print the whole string
print(string[0])               # print the first character of the string
print(string[6:])              # print string from the sixth character
print(string[0:5])             # print character from 0 to 5
print(string * 2)              # print character twice
print(string + "hello ming")   # print string which append 'hello ming'

# 3.Lis(use identifier: [])
list = ['ming', 1, 2.33, "hello", 100]
tinylist = ['sherman', 2]

print(list)                    # print the whole list
print(list[0])                 # print the first member of list
print(list[1:3])               # print member which from 1 to 3(exclude 3)
print(list[1:])                # print member from 1 to list's end
print(list * 2)                # print list twice
print(list + tinylist)         # print list which append tinylist

# 4.Tuple(use identifier: ())
tuple = ('ming', 1, 2.33, "hello", 100)
tinytuple = ('sherman', 2)

print(tuple)                    # print the whole list
print(tuple[0])                 # print the first member of list
print(tuple[1:3])               # print member which from 1 to 3(exclude 3)
print(tuple[1:])                # print member from 1 to list's end
print(tuple * 2)                # print list twice
print(tuple + tinytuple)        # print list which append tinylist

print("old list[1]:", list[1])
list[1] = "ming"       # list member can be updated
# tuple[1] = 200       # this is error tuple can not be update
print("updated list[1]:" + list[1])

# 5.Dictionary(use identifier: {})
dict = {}
dict['one'] = "this is one"     # create a pair of key-value
dict[2] = "this is two"         # create another pair of key-value

# create a dictionary
tinydict = {'name': 'sherman', 'code': 22.333, 'tall': 120}

print(dict["one"])              # print value which key is "one"
print(dict[2])                  # print value which key is 2
print(tinydict)
print(tinydict.keys())          # print all keys in the tinydict
print(tinydict.values())        # print all values in the tinydict

# data type convert function

print(int("20", 16))            # convert string to hex number(int)
# print(long("20"))               # convert string to hex number(long)
print(float("10"))              # convert string to float
print(complex(1, 3))            # create a complex number
