#Dictionary
info = {
    "name" : "Tahmid",
    "age" : 12,
    "marks" : 99.9,
    57.3 : ["Math", "Physics"],
    69 : ("algebra", "force"),
}
print(info)
print(type(info))
print(info["age"]) #dict er kono key er value print kora
print(info["name"])
info["marks"] = 100 #dict er kono value change kora
info["grade"] = "A" #dict e kono new key & value add kora

#Nested dictionary
student = {
    "name" : "Tahmid",
    "marks in sub" : {
        "phy" : 98,
        "chem" : 96,
        'bio' : 97
    }
}
print(student["marks in sub"]["phy"])

#Dictionary methods
dict = {} #empty dict
student = {
    "name" : "Tahmid",
    "marks in sub" : {
        "phy" : 98,
        "chem" : 96,
        'bio' : 97
    }
}
print(student.keys()) #dict er shob key print kore
print(student.values()) #dict er shob value print kore
print(student.items()) #dict er shob key & value tuple form e print hoy
print(student["name"]) #dict er kono key er value print kora(jodi oi key exist na kore then Error ashbe)
print(student.get("name")) #dict er kono key er value print kora(jodi oi key exist na kore then None print hbe)
student.update({"grade" : {"A+"}}) #dict e kono new key & value add kora
student.update({"name" : {"Tashrik"}}) #dict e kono exsisting key er value change kora
print(student)

#Set
set = {1, 2, 2, 4, "Tahmid"} #set e duplicate value 1bar print hoy
print(set)
print(type(set))
set2 = set() #empty set

#Set method
set = set()
set.add(2) #set e 1ta value add kora
set.add(2)
set.add(3)
set.remove(3) #set e 1ta value remove kora

print(set)
