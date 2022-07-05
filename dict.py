car = {"brand": "Ford",
  "model": "Mustang",
  "year": 1954
}
print(car['brand'])
print(car)
x = car.keys()
print(x)
car["color"] = "white"
print(car)
car["color"] = "red"
print(car)
car.update({"light": "blue"})
print(car)
car.pop("light")
print(car)
del car["color"]
print(car)
car.update({"part": ["body","wheel","light"]})
print(car)
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
 },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
 },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
 }
}
print(myfamily['child1'])
