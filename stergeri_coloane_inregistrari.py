import pandas as pd

date = pd.read_csv("angajati.csv")

date_stergere_functie = date.drop("Functie", axis=1)
print(date_stergere_functie)

date_stergere_salariu = date.drop(columns="Salariu")
print(date_stergere_salariu)

date_stergere_developer = date.set_index("Functie")
date_stergere_developer = date_stergere_developer.drop("Front End Developer", axis=0)
print(date_stergere_developer)

