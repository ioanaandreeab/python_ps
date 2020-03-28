import pandas as pd

date = pd.read_csv("angajati.csv")
date_angajati = pd.read_csv("angajati_date.csv")

result = pd.merge(date,
                  date_angajati[['Nume', 'Vechime', 'Studii']],
                  on='Nume',
                  how='outer')
print(result)
print('Structura fisier user_usage.csv ', date.shape)
print('Structura fisier user_device.csv ', date_angajati.shape)
print(date['Nume'].isin(date_angajati['Nume']).value_counts())
