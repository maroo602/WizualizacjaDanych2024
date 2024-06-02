import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
#
# plt.plot([1,2,3,4])
# plt.ylabel('jakies liczby')
# plt.show()

# plt.plot([1,2,3,4],[1,4,9,16],'ro-')
# plt.axis((0,6,0,20))
# plt.show()
# plt.plot([1,2,3,4],[1,4,9,16],'b')
# plt.plot([1,2,3,4], [1,4,9,16], 'o')
# plt.axis((0,6,0,20))
# plt.show()
# x=np.linspace(0,2,100)
# plt.plot(x,x,label="liniowa")
# plt.plot(x,x**2,label="kwadratowa")
# plt.plot(x,x**3, label="sześcienna")
# plt.xlabel('etykieta x')
# plt.ylabel('etykieta y')
# plt.title("Prosty wykres")
# plt.legend(labels=['liniowa'],'kwadratowa'])
# plt.savefig('wykres matplot.png')
# plt.show()
# im1 = Image.open('wykres matplot.png')
# im1=im1.convert('RGB')
# im1.save('nowy.jpg')

#
# x=np.arange(0,10,0.1)
# s=np.sin(x)
# plt.plot(x,s,label='sin(x)')
# plt.xlabel('x')
# plt.ylabel('sin(x)')
# plt.title('Wykres sin(x)')
# plt.legend()
# plt.show()

# data={'a': np.arange(50),
#       'c': np.random.randint(0,50,50),
#       'd': np.random.randn(50)}
# data['b']=data['a']+10*np.random.randn(50)
# data['d']=np.abs(data['d'])*100
# print(f"a={data['a'][0]}, b={data['b'][0]}, c={data['c'][0]},d={data['d'][0]}")
# plt.scatter('a','b', c='c', cmap='magma', s='d', data=data)
# plt.show()

# x1=np.arange(0,2,0.02)
# x2=np.arange(0,2,0.02)
# y1=np.sin(2*np.pi*x1)
# y2=np.cos(2*np.pi*x2)
# plt.subplot(2,1,1)
# plt.plot(x1,y1,'-')
# plt.title('wykres sin(x)')
# plt.xlabel('x')
# plt.ylabel('sin(x)')
#
# plt.subplot(2,1,2)
# plt.plot(x2,y2,'r-')
# plt.xlabel('x')
# plt.ylabel('cos(x)')
# plt.title('wykres cos(x)')
# plt.subplots_adjust(hspace=0.5, left=0.1)
# plt.show()

# x1=np.arange(0.0, 2.0, 0.02)
# x2=np.arange(0.0,2.0,0.02)
# y1=np.sin(2*np.pi*x1)
# y2=np.cos(2*np.pi*x2)
# fig, axs = plt.subplots(3,2)
# plt.subplots_adjust(left=0.1)
# axs[0,0].plot(x1,y1,'-')
# axs[0,0].set_title('wykres sin(x)')
# axs[0,0].set_xlabel('x')
# axs[0,0].set_ylabel('sin(x)')
# axs[1,1].plot(x2,y2,'r-')
# axs[1,1].set_title('wykres cos(x)')
# axs[1,1].set_xlabel('x')
# axs[1,1].set_ylabel('cos(x)')
# axs[2,0].plot(x2,y2,'r-')
# axs[2,0].set_title('wykres cos(x)')
# axs[2,0].set_xlabel('x')
# axs[2,0].set_ylabel('cos(x)')
# fig.delaxes(axs[0,1])
# fig.delaxes(axs[1,0])
# fig.delaxes(axs[2,1])
# plt.show()

# data={'Kraj': ['Belgia', 'Indie', 'Brazylia', 'Polska'],
#       'Stolica': ['Bruksela', 'New Delhi', 'Brasilia', 'Warszawa'],
#       'Kontynent': ['Europa', 'Azja', 'Ameryka Południowa', 'Europa'],
#       'Populacja': [11190846,1303171035,207847528,38675467]}
# df=pd.DataFrame(data)
# print(df)
# grupa=df.groupby('Kontynent')
# etykiety=list(grupa.groups.keys())
# wartosci=list(grupa.agg('Populacja').sum())
# fig, ax = plt.subplots()
# ax.bar(x=etykiety, height=wartosci, color=['yellow', 'green', 'red'])
# ax.set_xlabel('Kontynenty')
# ax.set_ylabel('Populacja w mld')
# ax.ticklabel_format(axis='y', style='plain')
# fig.subplots_adjust(left=0.2)
# plt.show()

df=pd.read_csv('dane.csv', header=0, sep=';', decimal=".")
print(df)
explode=(0.0, 0.1)
seria=df.groupby('Imię i nazwisko')['Wartość zamówienia'].sum()
wedges,texts,autotext=plt.pie(x=seria, labels=seria.index, autopct=lambda pct:"{:.1f}%".format(pct),textprops=dict(color="black"),colors=['red','green'],
                              pctdistance=1.2,labeldistance=1.1,hatch=['*O','O'],shadow=True,explode=explode)
plt.title('Suma zamówień dla sprzedawców')
plt.legend(loc='lower right')
plt.ylabel('Procentowy wynik wartości zamówienia')
plt.show()