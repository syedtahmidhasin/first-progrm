#File I/O
file = open("demo.txt", "r") #1st e file er name/path then mode
data = file.read() #file er shob data str e print hbe
print(data)

data = file.read(11) #file er 1st 11ta letter print hbe
print(data)

line1 = file.readline() #file er 1st line print hbe
print(line1)
line2 = file.readline() #file er 1st line print hbe
print(line2)

file = open("demo.txt", "w")
file.write("I am Tahmid") #file er shob data replace kore new data store kore

file = open("demo.txt", "a")
file.write("I am learning python") #file er last e kono data add kora
file.write("\nI am in class 10") #new data 1ta para diye next line e lekha

file = open("demo.txt", "r+") #no truncate
file.write("Hello") #file er starting data replece hoye new data add hoy

file = open("demo.txt", "w+") #truncate
print(file.read()) #file e kono data thakbe na cuz shob data age delete hoise then new data add hoise
file.write("Hello") #file er shob data delete hoye new data dtore hbe

file = open("demo.txt", "a+") #no truncate
print(file.read()) #pointer last e
file.write("\nTahmid") #file er last e data add hbe

file.close()

with open("demo.txt", "r") as f: 
    data = f.read()
    print(data)

import os #os module import kora
os.remove("demo.txt") #os module er maddhome kono file remode/delete kora
