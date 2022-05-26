import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

sprzedaz = pd.read_excel('sprzedaz12.xlsx')
df = pd.DataFrame(sprzedaz) 
produktyCeny = df.groupby(['Produkt']).agg({'Sprzedaż':['sum']})

produktyLen = len(df['Produkt'].unique())
rodzajeP = []
def prodArr():
    for i in range(0, produktyLen):
        rodzajeP.append(df['Produkt'][i])
        
prodArr()
cenyLen = produktyLen
cena1 = int(produktyCeny.iloc[0])
cena2 = int(produktyCeny.iloc[1])
cena3 = int(produktyCeny.iloc[2])
cenyArr = [cena1, cena2, cena3]

dataNowa = {'Produkt': rodzajeP, 'Cena razem': cenyArr}
print(dataNowa)

plt.pie(cenyArr, labels=rodzajeP, autopct='%.2f %%')
plt.title('Sprzedaż procentowo według rodzajów warzyw')
plt.annotate('164428', xy=(-1, 1), xytext=(-1.2, 1.2))
plt.legend()
plt.savefig('wyk1.jpg')
plt.show()

produktyIlosci = df.groupby(['Produkt']).agg({'Sprzedaż':['count']})
cena1 = int(produktyIlosci.iloc[0])
cena2 = int(produktyIlosci.iloc[1])
cena3 = int(produktyIlosci.iloc[2])
cenyArr = [cena1, cena2, cena3]

plt.pie(cenyArr, labels=rodzajeP, autopct=lambda p: '{:.0f}'.format(cenyArr[0]))
plt.title('Sprzedaż ilościowo według rodzajów warzyw')
plt.legend()
plt.savefig('wyk2.jpg')
plt.show()

Wykres prezentujący dane procentowo:
plt.pie(nTotal, labels=opis, autopct='%.2f %%')

###

# Zadanie 2.