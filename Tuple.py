from pickle import TUPLE1


fruits = ("apple", "bananan", "cherry")
print(fruits[0])

fruits = ("apple", "bananan", "cherry", "orange", "kiwi", "melon", "mango")
print(fruits[2:5])
print(fruits[:5])
print(fruits[2:])

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x= tuple(y)
print(x)

x = ("apple", "banana", "cherry")
y = list(x)
y.remove("apple")
x= tuple(y)
print(x)

tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)

x = range(3, 6)
for n in x:
    print(n)

x = range(3, 20, 2)
for n in x:
    print(n)

#นายจิรวัฒน์ ผุดผ่อง เลขที่ 2 ม.6/14