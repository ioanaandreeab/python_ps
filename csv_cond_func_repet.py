import pandas as pd
date = pd.read_csv("angajati.csv")
# salarii = date["Salariu"].tolist()
# print("Salarii inainte de majorare: ", salarii)
#
#
# def majorare_salarii(lista_salarii):
#     for idx in range(len(lista_salarii)):
#         if lista_salarii[idx] >= 2000 & lista_salarii[idx] < 5000:
#             lista_salarii[idx] += lista_salarii[idx] * 0.05
#         elif lista_salarii[idx] >= 5000 & lista_salarii[idx] < 7000:
#             lista_salarii[idx] += lista_salarii[idx] * 0.03
#         else:
#             lista_salarii[idx] += lista_salarii[idx] * 0.02
#     return lista_salarii
#
#
# salarii = majorare_salarii(salarii)
# print("Salarii dupa majorare: ", salarii)

# ACCESARE LOC SI ILOC
# print(date.iloc[0:3, 0:3])
# print(date.loc[0:2, ['Nume', 'Functie', 'Salariu']])

# MODIFICARE DATE
date.loc[7, 'Functie'] = 'Front End Developer'
date.loc[7, 'Salariu'] = 8000
print("Dupa actualizarea functiei, informatiile despre angajat sunt:")
print(date.loc[7])
