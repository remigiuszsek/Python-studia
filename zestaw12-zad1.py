import matplotlib.pyplot as plt
import seaborn as sns

wartosci = [-48, -28, -25, -14, -50]
nazwy = ['A', 'B', 'C', 'D', 'E']
mypalette = ['#daa520', '#8b4513', '#7b68ee', '#b22222', '#1e90ff']

plt.barh(nazwy, wartosci, color=mypalette)
plt.title('Wykres Słupki')
plt.savefig('wykres_odwzorowany1.pdf')

plt.show()

