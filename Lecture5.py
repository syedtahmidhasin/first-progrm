#Loops
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
