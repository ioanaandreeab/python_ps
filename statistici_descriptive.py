import pandas as pd

date = pd.read_csv("angajati_salarii_majorate.csv")

print('Statistici descriptive')
print(date['Functie'].describe())
print(date['Salariu'].describe())

print(date.groupby(['Functie']).agg({'Salariu': [min, max, sum],
                                     'Nume': "count"}))


