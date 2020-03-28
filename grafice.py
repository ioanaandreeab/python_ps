import pandas as pd
import matplotlib.pyplot as plt

date = pd.read_csv('angajati.csv')

date_plot = date.groupby('Functie')['Salariu'].min()
date_plot.sort_values().plot(kind='bar')
plt.xlabel('Functie')
plt.ylabel('Angajati')
plt.show()
