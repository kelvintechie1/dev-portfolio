import json

stream = open("testyyctemplate.json", "r")
file = json.load(stream)

i = 0
for iterations, thing in enumerate((var := file["Notes"])):
    for item in (var2 := file["Notes"][iterations]):
        print(item + ":" + str(var2[item]))