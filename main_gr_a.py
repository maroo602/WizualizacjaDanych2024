import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x = np.arange(-5,6,0.5)
a = (x**3) + (2*x**2)

plt.plot(x,a)
plt.xlim(-5,5)
plt.xticks(np.arange(-5,6))
plt.ylim(-100,200)
plt.ylabel("Y")
plt.xlabel("X")
plt.title("Wykres funkcji f(x)=x^3+2x^2")
plt.show()


df=pd.read_csv('flags.csv', header=0, sep=';', decimal='.')
df2=df[df['Zone'] == "NE"]
df3=df[df['Zone'] == "NW"]
print(df2,df3)

gr = df.groupby('Landmass')['Area'].sum()
print(gr)
plt.figure(figsize=(10,6))
gr.plot(kind='pie', subplots=True, autopct='%.2f%%', fontsize=14, figsize=(6,6))
plt.legend(loc = "best")
plt.title("Wielkośc kontynentów")
plt.show()



x = np.arange(-3,4,0.1)
a = 4*x**2-5*x+12
b = x**2/(10+x)+20

plt.plot(x,a,'-r',label="a = 4*x**2-5*x+12")
plt.plot(x,b,':b',label="b = x**2/(10+x")
plt.xlim(-3,3)
plt.xticks(np.arange(-3,4,1))
plt.ylim(10,30)
plt.ylabel("Wykres funkcji")
plt.xlabel("X")
plt.title("Drugi wykres")
plt.grid()
plt.legend(loc='lower left')
plt.savefig('krystian_dobrolecki_zad4.png')
plt.show()





df = pd.read_csv('flags.csv', header=0, sep=';', decimal='.')
gr = df.groupby('Zone').agg({'Country': ['count']})
print(gr)

plt.bar(gr.index, gr['Country']['count'])
plt.xlabel('Zone')
plt.ylabel('Count')
plt.title('Number of Countries per Zone')
plt.show()

