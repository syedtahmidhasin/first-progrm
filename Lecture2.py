a = "Hi.\nMy name is Tahmid" #para dawa
a = "Hi.\tMy name is Tahmid" #tab space dawa

#concatenation
a = "Tah"
b = "mid"
print(a+b) #kono space chara 2ta str add kora
a = "Syed"
b = "Tahmid"
print(a + " " + b) #space die 2ta str add kora

#Length of str
a = "Tahmid" #str e koyta word ase 
print(len(a))

#indexing
a = "Syed Tahmid Hasin"
print(a[0]) #a str er moddhe particular charecter identify kora

#slicing
a = "Syed Tahmid Hasin"
print(a[0:4]) #starting indx theke ending indx er age porjonto shob indx 
print(a[0:]) #starting indx theke last porjonto
print(a[0:len(a)]) #starting indx theke last porjonto
print(a[:len(a)]) #staring indx(ekdom left) 0 dhorbe
print(a[-3:-1]) #str er ekdom last(ekdom right) indx -1

#str functions
a = "syed Tahmid Hasin"
print(a.endswith("sin")) #substr er shathe shes hoile True ashbe 
print(a.capitalize()) #str er 1st cahrecter ke capital letter kore, new str creat kore real str ke change kore na
b = a.capitalize() 
print(b)
print(a.replace(" ", "_")) #kono ekta charecter ke replace kore
print(a.find("a")) #kono ekta charecter or word kothay ase oitar 1st indx
print(a.count("a")) #kono ekta charecter or word koybar ase

#conditional statements
#condition 'if' diye start hoy then elif hoy ar last e else hoy
marks = int(input("Your Marks :"))
if(marks >= 90):
    Grade = 'A'
elif(marks >= 80 and marks < 90):
    Grade = 'B'
elif(marks >= 70 and marks < 80):
    Grade = 'C'
else:
    Grade = 'D'
print("Your Grade is :", Grade)  

#pracice
num = int(input("Enter a number: "))
if(num % 2 == 0):
    print("Even")
else:
    print("Odd")

a = int(input("Num1:"))
b = int(input("Num2:"))
c = int(input("Num3:"))

if(a > b and a > c):
    print("Num1 is greatest")
elif(b >c):
    print("Num2 is greatest")
else:
    print("Num3 is greatest")
