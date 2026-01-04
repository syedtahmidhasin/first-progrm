#Dictionary
info = {
    "name" : "Tahmid",
    "age" : 12,
    True : 99.9,
    57.3 : ["Math", "Physics"],
    69 : ("algebra", "force")
}
print(info)
print(type(info))
print(info["age"]) #dict er kono key er value print kora
print(info["name"])
info["marks"] = 100 #dict er kono value change kora
info["grade"] = "A" #dict e kono new key & value add kora
print(info)

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
