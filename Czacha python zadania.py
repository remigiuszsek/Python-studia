import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns


////////////////////////////////
x = np.arange(0, 5, 0.1)


y1 = np.sin(x)
y2 = np.cos(x)


w1 = sns.lineplot(data=y1, linestyle="dotted", color="orange", label='sin(x)')
w1 = sns.lineplot(data=y2, linestyle="dotted", color="brown", label='cos(x)')

plt.ylim(-1,1)

plt.legend(loc=8)


plt.xlabel("oś dolna")
plt.ylabel("oś lewa", color="green")
w1.set_title("To jest tytuł wykresu")

plt.show()



////////////////////////////////////////////////
df = pd.read_excel("sprzedaz21.xlsx")
df = pd.DataFrame(df)
grupa = df.groupby(["Produkt"])["Sprzedaż"].sum()

produkt = df["Produkt"].unique()

plt.barh(produkt, grupa,color="blue", label="Marchew")
plt.barh(produkt, grupa,color="green", label="Pomidor")
plt.barh(produkt, grupa, color="red", label="Ogórek")


plt.legend()
plt.ylabel("produkty")
plt.xlabel("sprzedaż")
plt.title("To jest tytuł wykresu")
print(grupa)
print(df)

plt.savefig("zadanie2.jpg")


plt.show()

//////////////////////////////////////
df = pd.read_csv("dosw21.csv", sep="$")

df = df.dropna(axis="rows", how="any")

x= df["Czas"]
y = df["Zmienna1"]
y2 = df["Zmienna2"]
y3 = df["Zmienna3"]


w1 = plt.plot(x,y,linestyle="dotted", color="red", label='Zmienna1')
w1 = plt.plot(x,y2,linestyle="dashdot", color="green", label='Zmienna2')
w1 = plt.plot(x,y3,linestyle="dashed", color="blue", label='Zmienna3')


plt.text(0,0,"164460")
plt.legend()
plt.ylabel("zmienna")
plt.xlabel("czas")
plt.title("To jest tytuł wykresu")


print(df)
plt.savefig("zadanie3.png")

plt.show()

/////////////////////////////////////////////////

x = np.arange(-2,2)
d1 = 3*x**2 + 2*x + 7
d2 = -4*x + 2
d3 = np.sin(2*x)

plt.grid(True)
w1 = sns.lineplot(data= d1, linestyle ='dotted', color = 'r')
w1 = sns.lineplot(data = d2, linestyle = 'dashed', color = 'g')
w1 = sns.lineplot(data = d3, linestyle = 'dashdot', color = 'b')

w1.set(xlabel='oś x', ylabel='oś y')
plt.xlim(0,3)
plt.ylim(-2.5,15)
plt.title('Zadanie 1')
plt.legend(labels=['3*x**2 + 2*x + 7','-4*x + 2','sin(2*x)'])

plt.savefig("zadanie1.png")
plt.show()
//////////////////////////////////////////////////////////////////

df = pd.read_excel('sprzedaz11.xlsx')
grupa = df.groupby(["Produkt"])
df1 = grupa.sum()
print(df1)


w1 = df.plot.bar( x ='Rok',y='Sprzedaż')
w1.text(0,2000,'164460')

plt.title('Zadanie 2')
w1.set(xlabel='Produkty', ylabel='Sprzedaż')



plt.savefig("zadanie2.png")
plt.show()

print(df)
///////////////////////////////////////////////////////////////////////
zad3 = pd.read_csv('dosw11.csv', sep=';')

zad3c = zad3.dropna(axis="rows", how="any")


x = (zad3c["Czas"])
y = (zad3c["Zmienna1"])
y1 = (zad3c["Zmienna2"])
y2 = (zad3c["Zmienna3"])

w= plt.plot(x,y, linestyle="dotted", color='r')
w= plt.plot(x,y1, linestyle="dashed", color='g')
w= plt.plot(x,y2, linestyle="dashdot", color='b')
plt.legend(labels=['zmienna1','zmienna2','zmienna3'])


plt.xlabel('Cas')
plt.ylabel('Zmienne')
plt.title('Zadanie 3')
plt.savefig("zadanie3.jpg")
print(zad3c)



plt.show()
///////////////////////////////////////////////
# wczytujesz dane i transponujesz je czyli kolumne zmieniasz w wiersz a wiersz w kolumne
df = pd.read_excel("./2020i2021/z3/handel3.xlsx").T
# po transpozycji kolumny nazywają się 0 i 1 więc zmieniasz ich nazwy na takie jakie chcesz
# po transpozycji na indexach czyli tak jakby nazwie każdego wiersza masz zduplikowane nazwy czyli 2x hipermarkety i żeby nie bawić sie w regex(bo przy duplikatach dodaje ci .1) to standaryzujesz nazwy
df = df.rename(columns={0: "Rok", 1: "Wartosc"}, index={
               "hipermarkety.1": "hipermarkety", "supermarkety.1": "supermarkety", "domy towarowe.1": "domy towarowe", "domy handlowe.1": "domy handlowe"})
# usuwasz indexy czyli wspomiane wyżej opisania wierszy
df.reset_index(inplace=True)
# zmieniasz nazwe index(domyślnie po resecie) na typ czy co tam sobie wyśnisz
df = df.rename(columns={"index": "Typ"})
# i tutaj już normalne rzeczy
wszystko1 = df[df["Rok"] == 2017]["Wartosc"].sum()
x1 = df[df["Rok"] == 2017].groupby("Typ")["Wartosc"].sum()
x1 /= wszystko1
plt.pie(x1, labels=df["Typ"].unique())
plt.show()
/////////////////////////////////////////////////

df = pd.read_csv("./2020i2021/z2/nieruchomosci2.csv", sep=";").T
df = df.rename(columns={0: "metraż", 1: "rok", 2: "cena"}, index={"rynek pierwotny.1": "rynek pierwotny", "rynek pierwotny.2": "rynek pierwotny",
                                                                  "rynek pierwotny.3": "rynek pierwotny", "rynek wtórny.1": "rynek wtórny", "rynek wtórny.2": "rynek wtórny", "rynek wtórny.3": "rynek wtórny", })
df.reset_index(inplace=True)
df = df.rename(columns={"index": "rynek"})
df["cena"] = df["cena"].str.replace(" ", "")
df["cena"] = df["cena"].apply(pd.to_numeric)
wszystko = df["cena"].sum()
pogrupowane = df.groupby("rynek")["cena"].sum()
pogrupowane /= wszystko
plt.pie(pogrupowane, labels=df["rynek"].unique(),
        autopct='%1.1f%%')
plt.title("Procentowy zysk od metra w zależności od rynku w roku 2018")
plt.show()
////////////////////////////////////


x= np.linspace(0.1,3*np.pi,50)

y1 = np.log(x)
y2 = (3*x)-5
y3 = 2*np.cos(x)

w1 = sns.lineplot(x,y1,color='red')
w2 = sns.lineplot(x,y2,color='purple')
w3 = sns.lineplot(x,y3,color='black')


w1.lines[1].set_linestyle("--")
w2.lines[0].set_linestyle("dotted")
plt.grid(True)
plt.title("Zadanie 1")
plt.legend(labels=["log(x)","3x-5","2cos(x)"])
plt.xlabel("X",fontsize=10)
plt.ylabel("Y",fontsize=10)x= np.linspace(0.1,3*np.pi,50)

y1 = np.log(x)
y2 = (3*x)-5
y3 = 2*np.cos(x)

w1 = sns.lineplot(x,y1,color='red')
w2 = sns.lineplot(x,y2,color='purple')
w3 = sns.lineplot(x,y3,color='black')


w1.lines[1].set_linestyle("--")
w2.lines[0].set_linestyle("dotted")
plt.grid(True)
plt.title("Zadanie 1")
plt.legend(labels=["log(x)","3x-5","2cos(x)"])
plt.xlabel("X",fontsize=10)
plt.ylabel("Y",fontsize=10)

////////////////////////////////////////////////
#I punkt
df = pd.read_csv('nieruchomosci2.csv', sep=';').T

#II punkt
df = df.rename(columns={0: "metraz", 1: "rok", 2: "wartosc"},
               index={"rynek pierwotny": "pierwotny",
                      "rynek pierwotny.1": "pierwotny",
                      "rynek pierwotny.2": "pierwotny",
                      "rynek pierwotny.3": "pierwotny",
                      "rynek wtórny": "wtorny",
                      "rynek wtórny.1": "wtorny",
                      "rynek wtórny.2": "wtorny",
                      "rynek wtórny.3": "wtorny"})
df.reset_index(inplace=True)
df = df.rename(columns={"index": "typ"})
print(df)

#III i  IV punkt
df["wartosc"] = df["wartosc"].str.replace(" ", "")
df["wartosc"] = df["wartosc"].apply(pd.to_numeric)

pierwotny = df[df['typ']=='pierwotny']
nazwy_p = pierwotny.metraz
wartosci_p = pierwotny.wartosc

wtorny = df[df['typ']=='wtorny']
nazwy_w = wtorny.metraz
wartosc_w = wtorny.wartosc

fig, axs = plt.subplots(2)
axs[0].pie(wartosci_p, labels=nazwy_p)
axs[0].set_title("Rynek pierwotny")
axs[1].pie(wartosc_w, labels=nazwy_w)
axs[1].set_title("Rynek wtórny")

plt.show()

//////////////////////////////////
