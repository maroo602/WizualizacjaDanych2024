# l1=[1, 2, 3, 4, 5, 6, 7, 8, 9]
# l2=[]
# for i in l1:
#     l2.append(i**2)
# print(l2)
# l2=[i**2 for i in l1]
# print(l2)
# l3=[3**y for y in range(1,6)]
# print(l3)
# l4=[x for x in l1 if x%2==1]
# print(l4)
# l5=[(x,y) for x in l2 for y in l3]
# print(l5)
#
# l6=[]
# for i in l2:
#     for j in l3:
#         l6.append((i,j))
# print(l6)

# s1= {1: 2, 2:3, 3:4, 4:5, 5:6, 6:7, 7:8, 8:9}
# s2={}
# for key, value in s1.items():
#     s2[value] = key
# print(s2)
# s3={v:k for k, v in s1.items()}
# print(s3)
import math

# def rownanie_kwadratowe(a, b, c):
#     delta = b**2-4*a*c
#     if delta<0:
#         print("Brak pierwiastkow")
#         return 0
#     elif delta ==0:
#         print("Jeden pierwiastek")
#         x=(-b)/(2*a)
#         return x
#     elif delta>0:
#         print("Dwa pierwiastki")
#         x1=(-b + math.sqrt(delta))/(2*a)
#         x2 = (-b - math.sqrt(delta)) / (2 * a)
#         return x1, x2
#
# print(rownanie_kwadratowe(6, 3, 1))
# print(rownanie_kwadratowe(1, 2, 1))
# print(rownanie_kwadratowe(2, 6, 1))

def dlugosc_odcinka(x1=1, x2=2, y1=3, y2=4):