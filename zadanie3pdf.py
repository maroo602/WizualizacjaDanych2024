# a = [1-x for x in range(11)]
# b = [4**i for i in range(8)]
# c = [x for x in b if x % 2 == 0]
# print(a)
# print(b)
# print(c)
#
# import random
#
# lista1 =[]
# for i in range (10):
#     i = random.randint(1, 100)
#     lista1.append(i)
# print(lista1)
# lista2 = [i for i in lista1 if i % 2 == 0]
# print(lista2)
# dokup = {"mleko": "ml", "piwo": "ml", "chleb": "sztuki", "bulka": "sztuki"}
# dokup2={}
# print(dokup)
#
# dokup2 = [key for key, value in dokup.items() if value == "sztuki"]
# print(dokup2)

# def prostokatny(a, b, c):
#     if (a**2+b**2==c**2 or a**2+c**2==b**2 or c**2+b**2==a**2):
#         return("Trojkat jest prostokatny")
#     else:
#         return("Trojkat nie jest prostokatny")
#
# a= int(input("Podaj 1 liczbe:"))
# b= int(input("Podaj 2 liczbe:"))
# c= int(input("Podaj 3 liczbe:"))
# print(prostokatny(a, b, c))
# print(prostokatny(2, 1, 3))
# print(prostokatny(3, 4, 5))
# print(prostokatny(10, 1, 3))
# print(prostokatny(5, 13, 12))

# def trapez(a=4, b=5, h=7):
#     return ((a+b)*h)/2
#
# print(trapez())

def iloczyn(a=1, b=4, ile=10)