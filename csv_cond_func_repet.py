import pandas as pd
date = pd.read_csv("angajati.csv")
salarii = date["Salariu"].tolist()
print("Salarii inainte de majorare: ", salarii)


def majorare_salarii(lista_salarii):
    for salariu in lista_salarii:
        if salariu >= 2000 & salariu < 5000:
            salariu += salariu * 0.05
        elif salariu >= 5000 & salariu < 7000:
            salariu += salariu * 0.03
        else:
            salariu += salariu * 0.02
    return lista_salarii


salarii = majorare_salarii(salarii)
print("Salarii dupa majorare: ", salarii)

