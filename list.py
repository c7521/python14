fruits = ["apple", "banana", "cherry", "watermelon", "blueberry"]
print(fruits[1])

fruits[1] = "blackcurrant"
print(fruits[2])

fruits[1:3] = ["kiwi", "mango", "pineapple"]
print(fruits)

fruits.append("orange")
print(fruits)

fruits.insert(1,"grage")
print(fruits)

tropical = ["mango", "pineapple", "papaya"]
fruits.extend(tropical)
print(fruits)

fruits.remove("watermelon")
print(fruits)

fruits.pop(1)
print(fruits)

#del fruits
fruits.sort()
print(fruits)
#ชื่อ จิรวัฒน์ ผุดผ่อง ชั้น ม.6/14 เลขที่ 2