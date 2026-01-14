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
