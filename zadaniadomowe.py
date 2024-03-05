# Zadanie 1
# a=5+3j
# print(type(a))
# a2=6+1j
# print(type(a2))
# b='ala\nma\nkota'
# print(type(b))
# c='424242'
# print(type(c))
# d,d2=123, 342
# print(type(d))
# print(type(d2))
# e,d= 1.2, 5.4
# print(type(e))
# print(type(d))
# Zadanie 2
# liczba1= int(input("Podaj pierwsza liczbe: "))
# liczba2= int(input("Podaj druga liczbe: "))
# znak= input("Podaj znak rownania(+ - * /): ")
# if znak == "+":
#     print("Wynik: ", liczba1+liczba2)
# elif znak == "-":
#     print("Wynik: ", liczba1-liczba2)
# elif znak == "*":
#     print("Wynik: ", liczba1*liczba2)
# elif znak == "/":
#     print("Wynik: ", liczba1/liczba2)
# else:
#     print("ZLY ZNAK")
#Zadanie 3
# import math
# potega = math.e ** 10
# print(potega)
# sin = math.sin(math.radians(8)) ** 2
# ln = math.log(5 + sin)
# sqrt = math.sqrt(ln)
# print(sqrt)
# floor = math.floor(3.55)
# print(floor)
# ceil = math.ceil(4.80)
# print(ceil)
#Zadanie 4
# a='MARCEL'
# b='BUDNY'
# print(a.capitalize(), b.capitalize())
#Zadanie 5
# a='Nasz życiorys ma przerwę la la la, gram DMT do jointa Tace chyba są srebrne, la la la żyrandole ze złota (uh-huh!) Hajsy lecą przez serwer, la la la ona na Bahama ma konta Ja mam wózek z tylnym napędem, ona wciska gaz, to M5-ka Nasz życiorys ma przerwę, gram DMT do jointa (taa!) la la la Tace chyba są srebrne (woo), la la la żyrandole ze złota (yo!) Hajsy lecą przez serwer, la la la ona na Bahama ma konta Ja mam wózek z tylnym napędem, ona wciska gaz, to M5-ka'
# print(a.count('la'))
#Zadanie 6
# a='python'
# print(a[1],a[5])
#Zadanie 7
# a='Nasz życiorys ma przerwę la la la, gram DMT do jointa Tace chyba są srebrne, la la la żyrandole ze złota (uh-huh!) Hajsy lecą przez serwer, la la la ona na Bahama ma konta Ja mam wózek z tylnym napędem, ona wciska gaz, to M5-ka Nasz życiorys ma przerwę, gram DMT do jointa (taa!) la la la Tace chyba są srebrne (woo), la la la żyrandole ze złota (yo!) Hajsy lecą przez serwer, la la la ona na Bahama ma konta Ja mam wózek z tylnym napędem, ona wciska gaz, to M5-ka'
# print(a.split())
#Zadanie 8
# a= 'python'
# b= 21.37
# c= 0x69
# print(a)
# print(f"{b:.2f}")
# print(f"{c:#0x}")

#Zadanie 2.1
# lista =['pilka nozna', 'koszykowka', 'siatkowka']
# print(lista)
# lista.reverse()
# print(lista)
# lista.append('pilka reczna')
# lista.append('biegi')
# print(lista)
#Zadanie 2.2
# slownik = {"itp : i tym podobne", "etc : et cetera", "itd : i tak dalej"}
# print(slownik)
#Zadanie 2.3
# slownik = {"CS": "Counter Strike", "BG3" : "Baldurs Gate 3", "DS" : "Dark Souls"}
# print(len(slownik))
#Zadanie 2.4
# a= input("Napisz zdanie: ")
# print(a.count('a'))
#Zadanie 2.5
# import sys as system
# system.stdout.write("Podaj pierwsza liczbe calkowita: ")
# a = int(system.stdin.readline())
# system.stdout.write("Podaj druga liczbe calkowita: ")
# b = int(system.stdin.readline())
# system.stdout.write("Podaj trzecia liczbe calkowita: ")
# c = int(system.stdin.readline())
# wynik=a**b+c
# system.stdout.write(str(wynik))
#Zadanie 2.6
# a= int(input("Podaj pierwsza liczbe: "))
# b= int(input("Podaj druga liczbe: "))
# c= int(input("Podaj trzecia liczbe: "))
#
# if (a > b and a > c):
#     print("Liczba 1 jest największa: ", a)
# elif (b > a and b > c):
#     print("Liczba 2 jest największa: ", b)
# elif (c > a and c > b):
#     print("Liczba 3 jest największa: ", c)
# if a==b or a==c or b==c:
#     print("CONAJMNIEJ DWIE LICZBY SA ROWNE")
#Zadanie 2.7
# lista = [1.5, 2.2, 2, 4]
# for i in range(len(lista)):
#     lista[i] = pow(lista[i], 2)
#
# print(lista)
#Zadanie 2.8
# liczby= []
# i=0
# while i<10:
#     liczba= int(input("Podaj liczby: "))
#     if liczba%2==0:
#         liczby.append(liczba)
#     i+=1
# print(liczby)
#Zadanie 2.9
# import math
# liczba= int(input("Podaj liczbe: "))
# if liczba<0:
#     print("Podales liczbe ujemna!")
# else:
#     print(math.sqrt(liczba))

#Zadanie 3.1
# a= input("Napisz zdanie: ")
# print(len(a.split()))
#Zadanie 3.2
# import sys as system
# system.stdout.write("Podaj pierwsza liczbe calkowita: ")
# a = int(system.stdin.readline())
# system.stdout.write("Podaj druga liczbe calkowita: ")
# b = int(system.stdin.readline())
# system.stdout.write("Podaj trzecia liczbe calkowita: ")
# c = int(system.stdin.readline())
# wynik=a**b+c
# system.stdout.write(str(wynik))
#Zadanie 3.3
# a= input("Podaj wyraz: ")
# b= a[::-1]
# if a==b:
#     print("Wyraz jest palindromem")
# else:
#     print("Wyraz nie jest palindromem")
#Zadanie 3.4
# liczba= int(input("Podaj liczbe: "))
# if liczba==3:
#     print("Jest liczba pierwsza")
# elif liczba==1:
#     print("Nie jest liczba pierwsza")
# elif liczba%2==0 or liczba%3==0:
#     print("Nie jest liczba pierwsza")
# else:
#     print("Jest liczba pierwsza")
#Zadanie 3.5
# lista = [1.5, 2.2, 2, 4]
# for i in range(len(lista)):
#     lista[i] = pow(lista[i], 2)
#Zadanie 3.6
# liczby= []
# i=0
# while i<10:
#     liczba= int(input("Podaj liczby: "))
#     if liczba%2==0:
#         liczby.append(liczba)
#     i+=1
# print(liczby)
#Zadanie 3.7
# lista = [1, 2, 2, 'a', 'b', 2.7, 3.4]
# slownik = {element: lista.count(element) for element in lista}
# usun = [klucz for klucz in slownik if not isinstance(klucz, (int, float))]
# for klucz in usun:
#     del slownik[klucz]
# print(slownik)