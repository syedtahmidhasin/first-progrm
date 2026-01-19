#Functions
def calc_sum(a, b): #def die function start hoy erpore function er name ar last e variable
    sum = a + b
    print(sum)
    return sum
calc_sum(5, 5) #5 a te & 10 b te store hoye kaj kore
calc_sum(6, 6)
calc_sum(7, 8)

def Hello():
    print("Hello")
Hello()

def average(a, b, c): #a,b,c holo parameters
    sum = a + b + c
    avg = sum / 3
    print(avg)
    return avg
average(10, 20, 30) #average holo function call & er vitore thake arguments
average(98, 97, 96)

def multuply(a=0, b=0): #kono argument chara function run korate parameter ke defaulte value pass kora hoy
    print(a * b)
    return a * b
multuply()

#Practice
cities = ["dhaka", "chitagang", "rangpur", "khulna", "rajshahi"]
def lenth(a):
    print(len(a))
    return a
lenth(cities)

def list(a):
    print(a, end=" ")
list(cities[0])
list(cities[1])

def cal_fact(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print(fact)
cal_fact(5)

def taka(usd):
    print(usd * 122.2)
taka(5)

#Recursion
def show(n):
    if(n == 0): #base case
        return
    print(n)
    show(n-1) #function er vitore call function
show(5)

def fact(n):
    if(n == 1 or n == 0):
        return 1
    else:
        return n * fact(n-1)
print(fact(3))

#Practice
def calc_sum(n):
    if(n == 0):
        return 0
    return calc_sum(n-1) + n

sum = calc_sum(5)
print(sum)

