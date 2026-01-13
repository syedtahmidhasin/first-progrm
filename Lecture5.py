#While loops
i = 1
while i <= 5: #jotokkhon count er value <= 5 thakbe totokkhon print korbe
    print(i)
    i += 1 #totokkhon porjonto count er shathe 1 add korbe jotokkhon na count er value <= 5 hoy
    
print("The loop is end")

#Practice
i = 1
while i <= 100:
    print(i)
    i += 1

i = 100
while i >= 1:
    print(i)
    i -= 1

n = int(input("enter number :"))
i = 1
while i <= 10:
    print(n * i)
    i += 1

num =  [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
indx = 0

while indx <= len(num):
    print(indx ** 2)
    indx +=1

num =  (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x = 36
i = 0
while i < len(num):
    if(num[i] == x):
        print("The number is found at", i)
    i += 1

#Break
i = 0
while i <= 5:
    print(i)
    if(i == 3): #ei condition e eshe loop close hbe
        break 
    i += 1
print("The loop is end")

#Continue
i = 0
while i <= 10:
    if(i % 2 == 0): #skip
        i +=1
        continue
    print(i)
    i +=1
    
#For loops
num = [1, 2, 3, 4, 5]
for a in num: #num er elimantes a te store hoye 1ta sequence e kaj kore
    print(a)

#Practice
num = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
for a in num:
    print(a)

num = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 49)
x = 49
indx = 0
for ele in num:
    if(ele == x):
        print("FOUND at indx", indx)
        break
    indx += 1

#Range
seq = range(10) #numbers er sequence print kore(start hoy 0 theke ar end hoy range er ager number e)
for i in seq:
    print(i)

for a in range(5):
    print(a)

for i in range(2, 10, 2): #1st start, 2nd stop, 3rd step
    print(i)

#Practice
for i in range(1, 101):
    print(i)

for i in range(100, 0, -1):
    print(i)

num = int(input("number :"))
for i in range(11):
    print(num * i)

#Pass
for i in range(5):
    pass #loop e kono kaj na korano
print("Hello World")

#Practice
sum = 0
n = 5
i = 1
while i <= n:
    sum += i
    i += 1

print("total is", sum)

n = 5
a = 1
for i in range(1, n+1):
    a *= i
print(a)
