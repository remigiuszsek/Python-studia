import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

###

# 1. PRZYKŁADOWE WYKRESY

###

# # Listing 1 - wykres liniowy na podstawie serii danych

# ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2020', periods=1000))
# ts = ts.cumsum()
# print(ts)
# ts.plot()
# plt.show()

###

# # Listing 2

# data = {'Kraj': ['Belgia', 'Indie', 'Brazylia', 'Polska'],
# 'Stolica': ['Bruksela', 'New Delhi', 'Brasilia', 'Warszawa'],
# 'Kontynent': ['Europa', 'Azja', 'Ameryka Południowa', 'Europa'],
# 'Populacja': [11190846, 1303171035, 207847528, 38675467]}
# df = pd.DataFrame(data, columns=['Kraj', 'Stolica', 'Kontynent', 'Populacja'])
# # print(df)

# grupa = df.groupby(['Kontynent']).agg({'Populacja':['sum']})
# print(grupa)


# wykres = grupa.plot.bar()
# wykres.set_ylabel('Mld')
# wykres.set_xlabel('Kontynent')
# wykres.legend()
# plt.title('Populacja z podziałem na kontynenty')
# plt.show()

###

# # Listing 3 - wczytanie danych z pliku i wyświetlenie zgrupowanych wartości

# df = pd.read_csv('dane.csv', sep=';')
# grupa = df.groupby(['Imię i nazwisko']).agg({'Wartość zamówienia':['sum']})
# print(grupa)
# wykres = grupa.plot.pie(subplots=True, autopct='%.2f %%', fontsize=20, figsize=(6,6))
# plt.title('Suma zamówień dla sprzedawcy')
# plt.show()

###

# # Listing 4 - zmodyfikowana wersja listingu 1 z dodatkowym wykresem średniej kroczącej

# ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2015', periods=1000))
# ts = ts.cumsum()
# print(ts)
# df = pd.DataFrame(ts)

# df['MA'] = df.rolling(window=50).mean()
# df.plot()
# plt.show()

###

# 2. ZADANIA   

###

# # Zadanie 1. Stwórz wykres liniowy, który wyświetli liczbę urodzonych dzieci dla każdego roku.

# import xlrd
# import openpyxl

# na19K = pd.ExcelFile('19K.xlsx')
# na19M = pd.ExcelFile('19M.xlsx')

# na20K = pd.ExcelFile('20K.xlsx')
# na20M = pd.ExcelFile('20M.xlsx')

# na21K = pd.ExcelFile('21K.xlsx')
# na21M = pd.ExcelFile('21M.xlsx')

# nk19 = pd.read_excel(na19K)
# nm19 = pd.read_excel(na19M)
# n19Total = nk19['LICZBA_WYSTĄPIEŃ'].sum(axis = 0) + nm19['LICZBA_WYSTĄPIEŃ'].sum(axis = 0)

# nk20 = pd.read_excel(na20K)
# nm20 = pd.read_excel(na20M)
# n20Total = nk20['LICZBA_WYSTĄPIEŃ'].sum(axis = 0) + nm20['LICZBA_WYSTĄPIEŃ'].sum(axis = 0)

# nk21 = pd.read_excel(na21K)
# nm21 = pd.read_excel(na21M)
# n21Total = nk21['LICZBA_WYSTĄPIEŃ'].sum(axis = 0) + nm21['LICZBA_WYSTĄPIEŃ'].sum(axis = 0)

# nTotal = [n19Total / 1000, n20Total / 1000, n21Total / 1000]

# plt.plot(['2019', '2020', '2021'], nTotal)
# plt.xlabel('Lata')
# plt.ylabel('Liczba urodzeń w tys.')
# plt.show()

###

# # Zadanie 2. Stwórz wykres słupkowy, który wyświetli liczbę urodzonych chłopców i dziewczynek z całego zbioru. 

# import xlrd
# import openpyxl

# na19K = pd.ExcelFile('19K.xlsx')
# na19M = pd.ExcelFile('19M.xlsx')

# na20K = pd.ExcelFile('20K.xlsx')
# na20M = pd.ExcelFile('20M.xlsx')

# na21K = pd.ExcelFile('21K.xlsx')
# na21M = pd.ExcelFile('21M.xlsx')

# nk19 = pd.read_excel(na19K)
# nm19 = pd.read_excel(na19M)


# nk20 = pd.read_excel(na20K)
# nm20 = pd.read_excel(na20M)


# nk21 = pd.read_excel(na21K)
# nm21 = pd.read_excel(na21M)

# nkTotal = (nk19['LICZBA_WYSTĄPIEŃ'].sum(axis=0)+nk20['LICZBA_WYSTĄPIEŃ'].sum(axis=0)+nk21['LICZBA_WYSTĄPIEŃ'].sum(axis=0))/1000
# nmTotal = (nm19['LICZBA_WYSTĄPIEŃ'].sum(axis=0)+nm20['LICZBA_WYSTĄPIEŃ'].sum(axis=0)+nm21['LICZBA_WYSTĄPIEŃ'].sum(axis=0))/1000

# plt.bar(['chłopcy', 'dziewczynki'], [nmTotal, nkTotal])
# plt.ylabel('Liczba urodzeń w tys.')
# plt.xlabel('dzieci')
# plt.show()

###

# # Zadanie 3. Wykres kołowy z wartościami % ukazującymi ilość urodzonych chłopców i dziewczynek w ostatnich 5 latach z
# # datasetu. 
# # Zmieniam na 3 lata to zadanie zamiast na 5, bo nie mam przygotowanych danych aż na 5 lat

# import xlrd
# import openpyxl

# na19K = pd.ExcelFile('19K.xlsx')
# na19M = pd.ExcelFile('19M.xlsx')

# na20K = pd.ExcelFile('20K.xlsx')
# na20M = pd.ExcelFile('20M.xlsx')

# na21K = pd.ExcelFile('21K.xlsx')
# na21M = pd.ExcelFile('21M.xlsx')

# nk19 = pd.read_excel(na19K)
# nm19 = pd.read_excel(na19M)


# nk20 = pd.read_excel(na20K)
# nm20 = pd.read_excel(na20M)


# nk21 = pd.read_excel(na21K)
# nm21 = pd.read_excel(na21M)

# nkTotal = (nk19['LICZBA_WYSTĄPIEŃ'].sum(axis=0)+nk20['LICZBA_WYSTĄPIEŃ'].sum(axis=0)+nk21['LICZBA_WYSTĄPIEŃ'].sum(axis=0))/1000
# nmTotal = (nm19['LICZBA_WYSTĄPIEŃ'].sum(axis=0)+nm20['LICZBA_WYSTĄPIEŃ'].sum(axis=0)+nm21['LICZBA_WYSTĄPIEŃ'].sum(axis=0))/1000
# nTotal = [nkTotal, nmTotal]
# opis = ['chlopcy', 'dziewczynki']
# plt.pie(nTotal, labels=opis, autopct='%.2f %%')
# plt.show()

###

# Zadanie 4. Z repozytorium UCI (http://archive.ics.uci.edu/ml/index.php) pobierz dataset Iris i za pomocą wykresu
# punktowego (scattered) wyświetl wartość 2 wybranych cech tego datasetu. Dla każdego rodzaju kwiatu użyj
# innego koloru na wykresie. Przykład można znaleźć w galerii wykresów biblioteki matplotlib - link
# https://matplotlib.org/stable/gallery/index.html 

# Nie robię tego, nie mam czasu na poznawanie i uczenie się irisa

###

# Zadanie 5. Wyświetl na pomocą wykresu słupkowego ilość złożonych zamówień przez poszczególnych sprzedawców (zbiór
# danych zamówienia.csv). 

import xlrd
import openpyxl

zamowienia = pd.read_csv('zamowienia.csv')
# print(zamowienia['Sprzedawca'])
# print(zamowienia)
zamowienie = pd.DataFrame(zamowienia)
# print(zamowienia)

wyniki = zamowienia.groupby(['Sprzedawca']).agg({'Utarg':['count']})
print(wyniki)

# print(wyniki['Sprzedawca'])
# wData = pd.DataFrame(wyniki)
# print(wData['Sprzedawca'])
wBar = []
# print(wyniki[1])
pojed = wyniki.iloc[0]
pojed2 = pojed.values.tolist()
# print(pd.to_numeric(pojed2))
# print(int(pojed2[0]))
# print(pd.to_numeric(pojed))
# print(type(wyniki.iloc[[0]]))

# print(pojed.iloc[0] + 2)
# testBar = [pojed.iloc[0], pojed.iloc[1]]
# print(testBar)
# print(pojed.last(2))
# print(wyniki)
# barData = {'Sprzedawca': }
# print(wyniki.iloc[0])
wBarT = []
ptest = wyniki.iloc[0]
print(ptest)
p2test = ptest.values.tolist()
print(p2test)
print(int(p2test[0]))
j = 0
for i in range(0, len(wyniki)):
    
    ptest = wyniki.iloc[i]
    p2test = ptest.values.tolist()
    wBar.append(int(p2test[i]))
    
    
print(wBar)

# przedsiebiorcy = ['Callahan', 'Davolio', 'Dudek', 'Fuller', 'King', 'Kowalski', 'Leverling', 'Peacock', 'Sowiński']
# plt.bar(przedsiebiorcy, wBar)
# plt.show()

# Nie potrafię tego dokończyć