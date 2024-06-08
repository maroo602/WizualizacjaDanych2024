import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
#Zad1
# x=np.arange(-5, 5.5)
# a=np.tan(x)*x
# plt.plot(a, x)
# plt.title('Wykres tan(x)*x')
# plt.xlabel('Oś X')
# plt.ylabel('Oś Y')
# plt.xlim(-5,5)
# plt.xticks(np.arange(-5,6))
# plt.show()
#Zad2
# df=pd.read_csv('flags.csv', header=0, sep=';', decimal='.')
# df2=df[df['Landmass'].isin(['Africa', 'Asia'])]
# print(df2)
# grupa=df2.groupby('Landmass')['Country'].count()
# print(grupa)
# grupa.plot(kind='bar', figsize=(10,7))
# plt.xlabel('Kontynent')
# plt.ylabel('Ilość krajów')
# plt.title('Ilość krajów w Afryce i Azji')
# plt.show()

#Zad3
# df=pd.read_csv('flags.csv', header=0, sep=';', decimal='.')
# df2=df['Religion'].value_counts(normalize=True)*100
# df2.plot(kind='pie', autopct='%1.2f%%', fontsize=14)
# plt.ylabel('')
# plt.title('Wykres procentowy religii')
# plt.show()
#Zad4

x=np.arange(-3, 4, 0.1)
a=(4*(x**2)-5*x+12)
b=x**2/(10+x)+20


fig, ax=plt.subplots()
ax.plot(x, a, color='red')
ax.plot(x, b, 'b:')
plt.xlim(-3,3.5)
plt.xticks(np.arange(-3, 4))
plt.ylim(10.0,30.0)
plt.yticks(np.arange(10,32.5,2.5))
plt.legend(loc='lower left')
plt.title("Drugi wykres")
plt.xlabel('x')
plt.ylabel('wykres funkcji')
plt.grid(True)
plt.savefig('marceli_budny_zad4.png')
plt.show()
