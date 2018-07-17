f = open("test_file", "r")
f2 = open("test_file2", "w")
line = f.readlines()

for data in line:
    print("it is the first file: %s" % data)
    f2.write(data)

f.close()
f2.close()
