# a, b, c, d, e, f, g, h, i = 1, 2, 3.14, 4.20, "es", "sa", 2+5j, 3+4j, "koniec"
# print(a, b, c, d, e, f, g, h, i)
# print(type(a), type(b), type(c), type(d), type(e), type(f), type(g), type(h), type(i))

# liczba = int(input("Wpisz 1 liczbę: "))
# liczba2= int(input("Wpisz 2 liczbę: "))
# znak = (input("Wpisz odpowiedni znak(+, -, *, /): "))
# if znak=="+":
#     print("Wynik działania {:d} {} {:d} =".format(liczba, znak, liczba2), liczba+liczba2)
# elif znak=="-":
#     print("Wynik działania {:d} {} {:d} =".format(liczba, znak, liczba2), liczba-liczba2)
# elif(znak=="*"):
#     print("Wynik działania {:d} {} {:d} =".format(liczba, znak, liczba2), liczba*liczba2)
# elif(znak=="/"):
#     print("Wynik działania {:d} {} {:d} =".format(liczba, znak, liczba2), liczba/liczba2)
# else:
#     print("Błąd")

# liczba= int(input("Podaj 1 liczbe: "))
# liczba2= int(input("Podaj 2 liczbe: "))
# znak=  (input("Podaj znak(+,-,*,/,**,%: "))
#
# if znak=="+":
#     liczba += liczba2
#     print(liczba)
# elif znak == "-":
#     liczba -= liczba2
#     print(liczba)
# elif znak == "*":
#     liczba *= liczba2
#     print(liczba)
# elif znak == "/":
#     liczba /= liczba2
#     print(liczba)
# elif znak == "**":
#     liczba **= liczba2
#     print(liczba)
# elif znak == "%":
#     liczba %= liczba2
#     print(liczba)
# else:
#     print("Błąd")

# import math as m
#
# essa = pow(m.e, 10)
# print(essa)
#
# podp= (m.log(5+pow(m.sin(8), 2)))**1/6
# print(podp)
#
# print(m.floor(3.55))
# print(m.ceil(4.80))

# eesa = "MARCEL"
# essa = "BUDNY"
# print(eesa.capitalize(), essa.capitalize())

# a= "Takie już mnie la la la kochały i szalały tu za mną panny la la la Kupowały mi wciąż la la la szampany i na jachty mnie porywały"
# print(a.count("la"))

# essa="Jeden"
# print(essa[1], essa[4])

# a= "Takie już mnie la la la kochały i szalały tu za mną panny la la la Kupowały mi wciąż la la la szampany i na jachty mnie porywały"
# print(a.split())
#
# a, b, c = "essa", 2.13, 0x2003
# print(a, b, hex(c))

# import sys
# sys.stdout.write("Podaj cos: ")
# napis = sys.stdin.readline()
# sys.stdout.write(napis)

# lista = ["pilka nozna", "pilka reczna", "pilka siatowa"]
# print(lista)
# lista.append("koszykowka")
# print(lista)
# slownik = {"etc":"et cetera", "itp":"i tym podobne", "itd":"i tak dalej"}
# print(slownik)
# slownik = {"BG3":"Baldur's Gate III", "CS2":"Counter-Strike 2", "DS":"Dark Souls"}
# print(len(slownik))

# a= input("Napisz zdanie: ")
# print("A występuje w zdaniu", a.count("a"), "razy.")

# import sys
# sys.stdout.write("Podaj liczbę a: ")
# a = int(sys.stdin.readline())
# sys.stdout.write("Podaj liczbę b: ")
# b = int(sys.stdin.readline())
# sys.stdout.write("Podaj liczbę c: ")
# c = int(sys.stdin.readline())
#
# print((a**b)+c)

# a= int(input("Podaj liczbę A:"))
# b= int(input("Podaj liczbę B:"))
# c= int(input("Podaj liczbę C:"))
#
# if a>b and a>c:
#     print("{:d} jest największa".format(a))
# elif b>a and b>c:
#     print("{:d} jest największa".format(b))
# elif c>a and c>b:
#     print("{:d} jest największa".format(c))
# else:
#     print("Błąd")

# lista = [1,2,3,4,5, 1.1, 1.2, 1.3, 1.4, 1.5]
# for i in range(len(lista)):
#     lista[i] = lista[i]**2
# else:
#     print(lista)

# lista=[]
# a=0
# print("Podaj 10 liczb do dodania do listy: ")
# while len(lista)<10:
#     a+=1
#     liczba=int(input("{:d} liczba: ".format(a)))
#     if liczba%2==0:
#         lista.append(liczba)
#     else:
#         print("Liczba musi być parzysta.")
#         a-=1
#         continue
# print(lista)
# import math as m
# a = int(input("Podaj liczbę: "))
# try:
#     print(m.sqrt(a))
# except ValueError:
#         print("Podałeś wartość ujemną")
import math
# def dodawanie(a, b):
#     return a+b
# a= int(input("Podaj 1 liczbe: "))
# b= int(input("Podaj 2 liczbe: "))
# print(dodawanie(a, b))

# plik = open("teks.txt", 'w+', encoding='utf8')
# tekst = plik.readlines()
# a = 5
# plik.write(str(a))
# plik.seek(0)
# b = plik.readline()
# plik.close()
# print(tekst)
# print(b)

import numpy as np
# a = np.arange(2)
# print(a)


# tablica = np.arange(3, 48, 3)
#
# print(tablica)

# a= np.arange(1.5 ,5, 0.6)
# print(a)
# b= a.astype(np.int64)
# print(b)

# def tablica(n):
#     return np.arange(1, n*n+1).reshape(n,n)
# n=int(input("Podaj liczbę: "))
# print(tablica(n))

# def potega(a, b):
#     return np.logspace(1, b, base=a, num=b)
#
# print(potega(2, 4))

# def wektor(n):
#     a = np.arange(n, 0, -1)
#     return np.diag(a)
#
# print(wektor(2))
# a='gnog'
# b='unte'
# c='mkoj'
# d='aerm'
# print(np.array(list(a)))
# print(np.array(list(b)))
# print(np.array(list(c)))
# print(np.array(list(d)))

# import math as m
#
# print(round(pow((pow(m.e, 4)-m.log2(34)), 1/3),2))
# print(round(pow((m.log(20)+m.cos(45)+m.e),1/3),2))
# print(round(pow(m.log(20, 3)+m.sin(45)*(5/8),1/4),2))
# print(round(m.log(23, 3)+pow(m.sin(34)+5, 1/3),2))
# print(round(pow((m.log2(32)+m.pi+m.sin(56)),1/4),2))

# def wieza(n):
#     if n>10:
#         print("Nie większe niż 10.")
#     else:
#         for i in range(1, n+1):
#             print("A"*i)
# wieza(10)
#
# def pira(n):
#     if n>10:
#         print("Nie wieksze niz 10.")
#     else:
#         for i in range(1, n+1):
#             print(" " * (n-i) + "A" * i + "A"*(i-1))
#
# pira(10)

# def sumawierszy(n):
#     macierz = np.random.rand(n, n)
#
#     suma = np.sum(macierz, axis=1)
#
#     return suma
#
# print(sumawierszy(5))


