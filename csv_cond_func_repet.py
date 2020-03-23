import pandas as pd
date = pd.read_csv("angajati.csv")
salarii = date["Salariu"].tolist()
print("Salarii inainte de majorare: ", salarii)


def majorare_salarii(lista_salarii):
    for idx in range(len(lista_salarii)):
        if lista_salarii[idx] >= 2000 & lista_salarii[idx] < 5000:
            lista_salarii[idx] += lista_salarii[idx] * 0.05
        elif lista_salarii[idx] >= 5000 & lista_salarii[idx] < 7000:
            lista_salarii[idx] += lista_salarii[idx] * 0.03
        else:
            lista_salarii[idx] += lista_salarii[idx] * 0.02
    return lista_salarii


salarii = majorare_salarii(salarii)
print("Salarii dupa majorare: ", salarii)

