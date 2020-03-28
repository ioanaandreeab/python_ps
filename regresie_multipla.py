import pandas as pd
import statsmodels.formula.api as smf

angajati = pd.read_csv('angajati_salarii_majorate.csv')
angajati_date = pd.read_csv('angajati_date.csv')

angajati.fillna(angajati.mean(), inplace=True)
angajati_date.fillna(angajati_date.mean(), inplace=True)

studii = angajati_date['Studii'].tolist()
for index in range(len(studii)):
    if studii[index] == "Licenta":
        studii[index] = 1
    elif studii[index] == "Masterat":
        studii[index] = 2
    else:
        studii[index] = 3

angajati_date['Studii'] = studii

X = pd.DataFrame(angajati_date, columns=['Studii', 'Vechime'])
Y = angajati['Salariu']

results = smf.ols('Y ~ Studii + Vechime', data=angajati_date).fit()
print(results.params)

print(round(results.predict(angajati_date)))

