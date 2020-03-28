import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans

angajati = pd.read_csv('angajati_salarii_majorate.csv')
angajati_date = pd.read_csv('angajati_date.csv')

X = np.column_stack([angajati_date['Vechime'], angajati['Salariu']])

kmeans = KMeans(n_clusters=3)
kmeans.fit(X)
print(kmeans.cluster_centers_)
print(kmeans.labels_)
f1 = plt.figure()
plt.scatter(X[:, 0], X[:, 1], label='True Position')
f2 = plt.figure()
plt.scatter(X[:, 0], X[:, 1], c=kmeans.labels_, cmap='rainbow')
f3 = plt.figure()
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], color='black')
plt.show()
