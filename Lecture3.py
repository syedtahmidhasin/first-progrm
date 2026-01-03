#Lists
marks = [99.3, 96.2, 92.3]
print(marks[0])
print(len(marks))

student = ["Tashrik", 25, 5.9]
print(student[0])
student[0] = "Tahmid" #list er kono value change kora
print(student)

 #List slicing
marks = [98, 58, 65, 69, 36, 58]
print(marks[1:4])
print(marks[:5]) #[0:5] er moto
print(marks[0:]) #[0:len(marks)] er moto/0 theke last er ager indx print hbe
print(marks[-5:-1]) #Neg indx -1 diye strt hoy(-1 holo last indx)

#List method
list = [2, 5, 4,]
list.append(6) #list er last e just 1ta eliment add kore(eita print korle output None ashbe)
print(list)
list.sort() #list er value ke choto theke boro onujai shajabe(eita print korle output None ashbe)
list.sort(reverse=True) #list er value ke boro theke choto onujai shajabe(eita print korle output None ashbe)

list = ["b", "c", "a", "e", "d"]
list.sort() #list er vitorer str ke 1st letter jeita age ashe shetake age kore shajabe
list.sort(reverse=True) #list er vitorer str ke alphabeticaly 1st letter jeta pore ashe shetake age kore shajabe

list = ["b", "d", "f", "a", "e", "c"]
list.reverse() #pura list ke ultay dibe

list = [2, 4, 5]
list.insert(1, 3) #kono 1ta particular indx e 1ta eliment add kora
print(list1)
list.pop(0) #kono 1ta particular indx ke remove kora
list.remove(4) #kono 1ta eliment ke remove kora(jodi oi eliment onkbar thake tahole age jeita thakbe oita remove hbe)

#Tuple
tup = (9, 5, 3, 6, 2)
print(type(tup))
print(tup[0]) #indexing
print(tup[0:4]) #slicing
print(tup[0:]) #0:len(tup) er moto
print(tup[:4]) #0:4 er moto

tup1 = ("hello",) #1ta eliment thekle comma dite hbe nahole python oitake str/float/int hishebe nibe
print(type(tup1))

#Tuple method
tup = (2, 1, 3, 1)
tup.index(1) #kono eliment jei indx e age thakbe oi indx dekhabe
tup.count(1) #ono eliment oi tuple e koybar ase 
print(tup.index(1))
print(tup.count(1))

#Practice
movie1 = input("First movie name :")
movie2 = input("Second movie name :")
movie3 = input("Third movie name :")

Favourite_movie_list = []
Favourite_movie_list.append(movie1)
Favourite_movie_list.append(movie2)
Favourite_movie_list.append(movie3)

print(Favourite_movie_list)

List1 = [1, 2, 1]
List2 = [1, 2, 3]

copy_List1 = List1.copy()
copy_List1.reverse()
if(List1 == copy_List1):
    print("It's a palindrome")
else:
    print("It's not a palindrome")

copy_List2 = List2.copy()
copy_List2.reverse()
if(List2 == copy_List2):
    print("It's a palindrome")
else:
    print("It's not a palindrome")

Grade = ("C", "D", "A", "A", "B", "B", "A")
A = Grade.count("A")
print("Num of A :", A)

Grade = ["C", "D", "A", "A", "B", "B", "A"]
Grade.sort()
print(Grade)
