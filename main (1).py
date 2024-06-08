import matplotlib.pyplot as plt
import numpy as np
#NORMALNY WYKRES
# # Miesiące
# miesiace = ['Styczeń', 'Luty', 'Marzec', 'Kwiecień', 'Maj', 'Czerwiec']
#
# # Zyski z filmów i gier
# zyski_filmy = [50, 42, 38, 22, 24, 30]  # Przykładowe wartości
# zyski_gry = [23, 36, 43, 77, 66, 50]  # Przykładowe wartości
#
# plt.figure(figsize=(7,5))
#
# # Wykres dla filmów
# plt.plot(miesiace, zyski_filmy, 'b--', label='Filmy')
#
# # Wykres dla gier
# plt.plot(miesiace, zyski_gry, 'g-', label='Gry')
# plt.yticks(np.arange(0, 101, 20))
# plt.grid(True)
# plt.title('Zyski z filmów i gier')
# plt.xlabel('Miesiąc')
# plt.ylabel('Zyski')
# plt.legend(loc='upper left')
#
# plt.show()
#WYKRES Z INNYM NAPISEM Z BOKU
# lata = ['2017', '2018', '2019', '2020']
# popm = [18.6, 18.58, 18.56, 18.4]
# popk = [19.8, 19.78, 19.76, 19.6]
# plt.plot(lata, popm, color="blue", label='mężczyźni')
# plt.plot(lata, popk, color="orange", label='kobiety')
#
# plt.ylim(18, 20)
# plt.yticks([18, 19, 20], ['18 mln', '19 mln', '20 mln'])
# plt.legend(loc='right')
# plt.title("Liczba ludności w Polsce według płci")
# plt.savefig("wykres.pdf")
# plt.show()

#Wykres kołowy
# labels = ['RMF FM', 'Radio Zet', 'Eska', 'Inne']
# sizes = [24.8, 13.0, 6.7, 55.5]
# colors = ['pink', 'cyan', 'lime', 'violet']
# explode = (0.1 , 0, 0, 0)  # "eksploduje" pierwszy segment
#

# fig1, ax1 = plt.subplots()
# ax1.pie(sizes, explode=explode, colors=colors, labels=labels, autopct='%1.1f%%', startangle=80, shadow=True)
#
# plt.title('Wyniki słuchalności - II-IV 2017')
#
# plt.show()
#WYKRES PUNKTOWY
# plt.figure(figsize=(7,5))
# punkty=[(13.5, 9.8), (18.5, 12.4), (20.5, 17.5), (30.2, 15.5)]
# kolory=['Yellow', 'Brown', 'Brown', 'Orange']
# plt.ylim([10, 18])
# plt.xlim([14.5, 31])
# plt.yticks(np.arange(9, 18, 1) ,color="Brown")
# plt.xticks(np.arange(12.5, 31, 2.5), color="Blue")
# plt.grid(True)
# plt.title("Wykres punktowy - 4 plusy")
# plt.xlabel("Oś pozioma", color="Green")
# plt.ylabel("Oś pionowa", color="Brown")
# for i in range(4):
#     plt.scatter(*punkty[i], color=kolory[i], marker="+", s=100)
# plt.show()
#WYKRES KOLOWY 2
# wartosci=['A', 'B', 'C', 'D', 'E', 'F']
# liczby=['11.11', '22.22', '13.33', '23.89', '17.22', '12.22']
# kolory=['Orange', 'Yellow', 'Purple', 'Blue', 'cyan', 'Green']
# explode=(0, 0, 0.1, 0, 0, 0.1)
# plt.pie(liczby, explode=explode, labels=wartosci, colors=kolory, autopct='%1.1f', startangle=20)
# plt.title('Tytuł')
# plt.show()

import pandas as pd
import matplotlib.pyplot as plt
#
# # Załaduj dane z pliku Excel
# file_path = 'mieszkania1.xlsx'
# df = pd.read_excel(file_path)
#
# # Wybierz dane za 2016 rok
# data_2016 = df[df['Rok'] == 2016]
#
# # Tworzenie wykresu kołowego
# labels = data_2016['Formy budownictwa']
# sizes = data_2016['Wartość']
# colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99']
#
#
# fig, ax = plt.subplots()
# ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%',
#        shadow=True, startangle=140)
# ax.axis('equal')  # Równy wykres kołowy
#
# # Dodanie tytułu
# plt.title('Podział wartości mieszkań wg form budownictwa w 2016 roku')
#
# # Zapisanie wykresu w formacie PDF
# plt.savefig('wykres_mieszkania_2016.pdf')
#
# # Pokaż wykres
# plt.show()

# xd = pd.read_excel('turcja.xlsx')
# ankara = xd[xd['city']=='Ankara']
# a= ankara['years']
# b= ankara['pop']
# fig, ax = plt.subplots()
# ax.bar(a, b, width=0.5, align='center')
#
#
#
# plt.xlabel("Lata")
# plt.ylabel("Populacja")
# plt.title("Populacja Ankary")
# plt.xlim(2004.5, 2010.5)
# plt.yticks(np.arange(1000000, 5000001, 1000000),
#            ['1 mln', '2 mln', '3 mln', '4 mln', '5 mln'])
# plt.show()

# dupa = pd.read_excel("konie.xlsx")
# dupalo = dupa[dupa['Nazwa']== 'ŁÓDZKIE']
# a=dupalo['Rok']
# b=dupalo['Wartość']
# fig, ax=plt.subplots()
# ax.bar(a, b, color="pink", align="center", width=0.5)
# plt.xlabel("Lata")
# plt.ylabel("Wartość w sztukach")
# plt.savefig('wykreskonie.png')
# plt.show()


# essa= pd.read_excel("licea12.xlsx")
# essa2= essa[essa['Rok']==2018]
# a=essa2['Nazwa']
# b=essa2['Wartość']
# c=['Red', 'Green', 'Blue', 'Orange', 'Pink', 'Violet']
# fig, ax = plt.subplots(figsize=(14, 12))
# ax.bar(a, b, color=c, width=0.75, align='center')
# plt.xticks(a, rotation=45, ha='right', fontsize=8)
# plt.xlabel("Województwo")
# plt.ylabel("Wartość w ob.")
# plt.savefig("wykreslicea.png")
# plt.show()

# essa= pd.read_excel("stacjepaliw.xlsx")
#
# essa = essa.melt(id_vars='Nazwa', var_name='Rok', value_name='Wartosc')
#
# essa2= essa[essa['Nazwa']== 'ŚLĄSKIE']
# essa3= essa[essa['Nazwa']== 'MAŁOPOLSKIE']
#
# plt.plot(essa2['Rok'], essa2['Wartosc'], label='Śląskie')
# plt.plot(essa3['Rok'], essa3['Wartosc'], label='Małopolskie')
#
# plt.xlabel('Lata')
# plt.ylabel('Dane')
# plt.title('Dane dla województw śląskiego i małopolskiego')
# plt.legend()
# plt.show()

# essa= pd.read_excel("lasy17.xlsx")
# essa = essa.melt(id_vars='Województwo', var_name='Rok', value_name='Wartość')
# essa2=essa[essa['Województwo']=='POMORSKIE']
# essa3=essa[essa['Województwo']=='OPOLSKIE']
# essa4=essa[essa['Województwo']=='MAŁOPOLSKIE']
# essa5=essa[essa['Województwo']=='MAZOWIECKIE']
# plt.figure(figsize=(10, 6))
# plt.scatter(essa2['Rok'], essa2['Wartość'], label="POMORKSIE", color="Red", marker='+')
# plt.scatter(essa3['Rok'], essa3['Wartość'], label="OPOLSKIE", color="Blue", marker='*')
# plt.scatter(essa4['Rok'], essa4['Wartość'], label="MAŁOPOLSKIE", color="Black", marker='4')
# plt.scatter(essa5['Rok'], essa5['Wartość'], label="MAZOWIECKIE", color="Green", marker='x')
# plt.legend()
# plt.xlabel("Lata")
# plt.ylabel("Wartość")
# plt.show()

# import matplotlib.pyplot as plt
# import numpy as np
#
# x=np.arange(-3,3.5,0.5)
# funkcja = np.sin(x)*x
# y=funkcja
# plt.plot(x,y)
# plt.xticks(np.arange(-3, 3.5, 0.5))
# plt.grid()
# plt.title("Wykres sin(x)*x")
# plt.xlabel('x')
# plt.ylabel('f(x)')
# plt.show()
# x=['Styczeń', 'Luty', 'Marzec', 'Kwiecień', 'Maj', 'Czerwiec']
# y=(50, 42,39,21,25,30)
# z=(22,33,42,75,65,50)
# plt.plot(x, y, 'b--', label='Filmy')
# plt.plot(x, z, 'g-', label='Gry' )
# plt.grid()
# plt.yticks(np.arange(0,120,20))
# plt.legend(loc='upper left')
# plt.title("Zyski z filmow i gier")
# plt.xlabel("Miesiąc")
# plt.ylabel("Zyski")
# plt.show()

# df=pd.read_excel('mieszkania1.xlsx')
# df2=df[df['Rok']==2016]
# a=df2['Formy budownictwa']
# b=df2['Wartość']
# colors=('olivedrab', 'pink', 'red')
# explode=[0,0.3,0.1]
# fig,ax=plt.subplots()
# ax.pie(b, colors=colors, labels=a,autopct='%1.1f%%', shadow=True, startangle=150, explode=explode)
# plt.title('Wykres mieszkań za rok 2016')
# plt.legend(b, loc='upper right')
# plt.savefig('wykres2.pdf')
# plt.show()

# a=['RMF FM', 'Radio Zet', 'Eska', 'Inne']
# b=[24.8,13.0,6.7,55.5]
# colors=['pink', 'blue', 'green', 'purple']
# explode=[0.1,0,0,0]
# plt.pie(b, labels=a, autopct='%1.1f%%', colors=colors, explode=explode,shadow=True, startangle=80)
# plt.title("Wyniki słuchalności - II-IV 2017")
# plt.savefig("Wykres2.pdf")
# plt.show()

# df=pd.read_excel('turcja.xlsx')
# df2=df[df['city']=='Ankara']
# fig, ax = plt.subplots()
# ax.bar(df2['years'],df2['pop'], color="red")
# plt.xlim(2004.5, 2010.5)
# plt.yticks(np.arange(1000000,6000000, 1000000), ['1mln', '2mln', '3mln', '4mln', '5mln'])
# plt.xlabel("Lata 2005-2010")
# plt.ylabel("Populacja w mln")
# plt.title("Populacja Ankary w latach 2005-2010")
# plt.show()

# df=pd.read_excel('stacjepaliw.xlsx')
# df=pd.melt(df, id_vars='Nazwa', var_name='Rok', value_name='Wartość')
# df2=df[df['Nazwa']=='ŚLĄSKIE']
# df3=df[df['Nazwa']=='MAŁOPOLSKIE']
# fig, ax= plt.subplots()
# ax.plot(df2['Rok'], df2['Wartość'],'b--',label='Śląskie')
# ax.plot(df3['Rok'], df3['Wartość'],'r-.',label='Małopolskie')
# plt.legend(loc='upper left')
# plt.grid()
# plt.title('Wykres województwa Małopolskiego i Śląskiego')
# plt.yticks(np.arange(600, 1300, 100))
# plt.xlabel('Lata')
# plt.ylabel('Wartość')
# plt.show()

# a=['2017', '2018', '2019', '2020']
# b=[19.8,19.78,19.76,19.6]
# c=[18.8,18.78,18.76,18.6]
#
# fig,ax=plt.subplots()
# ax.plot(a,b,color='orange')
# ax.plot(a,c,color='blue' )
# plt.yticks([18,19, 20], ['18 mln', '19 mln', '20 mln'])
# plt.title('Liczba ludności w Polsce według płci')
# plt.show()

# df=pd.read_excel('konie.xlsx')
# df2=df[df['Nazwa']=='ŁÓDZKIE']
# fig, ax =plt.subplots()
# ax.bar(df2['Rok'], df2['Wartość'], width=0.4, color='pink')
# plt.xlabel('Lata 2015-2020')
# plt.ylabel('Wartość w szt')
# plt.title('Wykres koni')
# plt.savefig('konie.jpg')
# plt.show()

# df=pd.read_excel('lasy17.xlsx')
# df=pd.melt(df, id_vars='Województwo', var_name='Rok',value_name='Wartość')
# df2=df[df['Województwo']=='POMORSKIE']
# df3=df[df['Województwo']=='OPOLSKIE']
# df4=df[df['Województwo']=='MAŁOPOLSKIE']
# df5=df[df['Województwo']=='MAZOWIECKIE']
# fig, ax = plt.subplots(figsize=(10, 6))
# ax.scatter(df2['Rok'],df2['Wartość'], label='Pomorskie', color='red',marker='*')
# ax.scatter(df3['Rok'],df3['Wartość'],label='Opolskie',color='blue',marker='+')
# ax.scatter(df4['Rok'],df4['Wartość'],label='Małopolskie',color='black',marker='x')
# ax.scatter(df5['Rok'],df5['Wartość'],label='Mazowieckie',color='green',marker='2')
# plt.legend(loc='best')
# plt.xlabel('Lata')
# plt.ylabel('Wartość')
# plt.show()
# fig, ax=plt.subplots()
# plt.ylim([9.5, 18])
# plt.xlim([12.5, 31])
# plt.yticks(np.arange(10, 18, 1) ,color="Brown")
# plt.xticks(np.arange(15, 31, 2.5), color="Blue")
# plt.grid()
# ax.scatter(13,10,color="olivedrab", marker="+",s=100, linewidths=4)
# ax.scatter(18.5,12.3,color="brown", marker="+",s=100,linewidths=4)
# ax.scatter(22,17.5,color="brown", marker="+",s=100,linewidths=4)
# ax.scatter(30.2,15.7,color="orange", marker="+",s=100,linewidths=4)
# plt.title('Wykres punktowy - 4 punkty')
# plt.ylabel('Oś pionowa', color='Brown')
# plt.xlabel('Oś pozioma', color='Green')
# plt.show()

# df=pd.read_excel('licea12.xlsx')
# fig,ax = plt.subplots(figsize=(15,10))
# ax.bar(df['Nazwa'], df['Wartość'], width=0.75)
# plt.ylim(0,160)
# plt.title('Liczba liceów w województwach')
# plt.xlabel('Wartość')
# plt.ylabel('Województwo')
# plt.show()

# a=['11.11','22.22','13.33','23.89','17.22','12.22']
# b=['A','B','C','D','E','F']
# colors=['Orange', 'Yellow', 'Purple', 'Cyan', 'Blue', 'Green']
# explode=(0,0,0.1,0,0,0.1)
# plt.pie(a, labels=b,colors=colors, autopct='%1.1f%%', startangle=30,explode=explode)
# plt.title('Tytuł')
# plt.show()

# df=pd.read_excel('licea3.xlsx')
# fig, ax=plt.subplots(figsize=(15,10))
# ax.bar(df['Nazwa'], df['Wartość'])
# plt.show()

# x=np.arange(-3,3.5, 0.5)
# a=np.sin(x)*x
# plt.plot(x,a)
#
# plt.xticks(np.arange(-3, 3.5, 0.5))
# plt.xlabel('x')
# plt.ylabel('f(x)')
# plt.title('Wykres funkcji sin(x)*x')
# plt.show()
# df= pd.read_csv('automobile.csv')
# df2=df[df['company'].isin(['audi','dodge'])]
# print(df2)
# grupa=df2.groupby('body-style')['mileage'].sum()
# print(grupa)
# fig, ax=plt.subplots(figsize=(7,10))
# grupa.plot(kind='bar')
# plt.title("Mileage of Cars")
# plt.xlabel("Car type")
# plt.ylabel('Mileage')
#
# plt.show()
# df=pd.read_csv('automobile.csv')
# print(df)
# body=df['body-style'].value_counts(normalize=True)*100
# body.plot(kind='pie',autopct='%1.2f%%', fontsize=14)
# plt.legend(title='Typy samochodow', loc='upper right')
# plt.title("Typy samochodow")
# plt.ylabel('')
# plt.show()
# df=pd.read_csv('automobile.csv')
# df2=df[df['company'].isin(['toyota', 'alfa-romero'])]
# print(df2)
# grupa=df2.groupby('body-style')['length'].sum()
# print(grupa)
# grupa.plot(kind='bar', title='gowno', xlabel='typ auta', ylabel='length',figsize=(7,10))
# plt.show()
# df=pd.read_csv('automobile.csv')
# cos=df['engine'].value_counts()*100
# cos.plot(kind='pie', autopct='%1.2f%%', fontsize=14,title="Engine")
# plt.legend(title='Engines', loc='upper right')
# plt.ylabel('')
# plt.show()

# df=pd.read_csv('automobile2.csv',header=0,sep=';',decimal='.')
# print(df)
# df2=df[df['Car model'].isin(['audi','dodge'])]
# print(df2)
# grupa=df2.groupby('Car model')['Price'].sum()
# print(grupa)
# grupa.plot(kind='bar', title='Ceny samochodów', xlabel='Model', ylabel='Cena', figsize=(7,10))
# plt.show()
#
# df=pd.read_csv('automobile2.csv', header=0, sep=';', decimal='.')
# df2=df['Fuel-type'].value_counts()*100
# df2.plot(kind='pie',autopct='%1.2f%%', fontsize=14,title='Paliwo', legend='loc=upper right')
# plt.ylabel('')
# plt.show()

# df=pd.read_excel('lasy17.xlsx')
# print(df)
# df=df.melt(id_vars='Województwo', var_name='Rok', value_name='Wartość')
# print(df)
# df2=df[df['Województwo']=='POMORSKIE']
# df3=df[df['Województwo']=='OPOLSKIE']
# df4=df[df['Województwo']=='MAŁOPOLSKIE']
# df5=df[df['Województwo']=='MAZOWIECKIE']
# fig, ax = plt.subplots()
# ax.scatter(df2['Rok'], df2['Wartość'], marker='+', s=100,linewidths=4)
# plt.show()


fig, ax = plt.subplots()
plt.ylim([9.5, 18])
plt.xlim([12.5, 31])
plt.yticks(np.arange(10, 18, 1),color='brown')
plt.xticks(np.arange(15, 31, 2.5), color='cyan')
ax.scatter(14,9.9, marker='+', s=200, linewidths=5, color='olivedrab')
ax.scatter(18,12.5, marker='+', s=200, linewidths=5, color='brown')
ax.scatter(21,17.5, marker='+', s=200, linewidths=5, color='brown')
ax.scatter(30.5,15.6, marker='+', s=200, linewidths=5, color='orange')
plt.title('Wykres punktowy - 4 plusy')
plt.ylabel('Oś pionowa', color='brown')
plt.xlabel('Oś pozioma', color='green')
plt.grid()

plt.show()