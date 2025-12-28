#Data types
name = 'Tahmid' #str
age = 10 #int
price = 99.99 #float
statemant = True #bool
box = None #none

print(type(name))
print(type(age))
print(type(price))
print(type(statemant))
print(type(box))

#Arithmetic operators
a = 100
b = 50
sum = a + b
diff = a - b
mul = a * b
div = a / b

print(sum)
print(diff)
print(mul)
print(div)
print(a % b) #Vag shes
print(a ** b) #a^b

#relational operators
a = 100
b = 50

print(a == b) #is equal
print(a != b) #'!' Not bujhay
print(a >= b) #gearter then or equal
print(a <= b) #less then or equal 

#Assingment operators
a = 10
a += 5 #a = a + 5
print(a)
b = 10
b -= 5 #b = b - 5
print(b)
c = 10
c *= 10 #c = c * 10
print(c)
d = 10
d /= 2 #d = d / 2
print(d)
e = 10
e %= 3 #e = e % 3
print(e)
f = 10
f **= 2 #f = f ** 2
print(f)

#Logical operators
a = 50 
b= 20
print("And operator :", (a > b) & (a != b)) #2tai true hoile output true hbe
print("And operator :", (a < b) & (a != b)) #1taw jodi false hoy tahole output false hbe
print("Not operator :", not (a == b)) #opposite output hbe
print("Or operator :", (a > b) or (a < b)) #1taw jodi true hoy tahole output true hbe ar jodi 2tai false hoy tahole output false hbe

#Type conversion
a = 5
b = 5.2
print(a+b) #a int hoileo python a ke float e convert korsi(type convertion)
a = 5 
b = int("2") #2 str kintu amra eikhane 2 ke int e convert korsi(type casting)
print(a+b)

#Input
input("your name :") #always str
age = int(input("age :")) #input ke str bad e onno kono type e cast korte hoy
price = float(input("price :"))
print(type(age), type(price))

#practice project
num1 = float(input("num1 :"))
num2 = float(input("num2 :"))
print("sum :", num1 + num2)
print("diff :", num1 - num2)
print("mul :", num1 * num2)
print("div :", num1 / num2)

a = int(input("num1 :"))
b = int(input('num2 :'))
print(a >= b)
