#File I/O
file = open("demo.txt", "r") #1st e file er name/path then mode
data = file.read() #file er shob data str e print hbe
print(data)
file.close()

data = file.read(11) #file er 1st 11ta letter print hbe
print(data)

line1 = file.readline() #file er 1st line print hbe
print(line1)
line2 = file.readline() #file er 1st line print hbe
print(line2)
file.close()
