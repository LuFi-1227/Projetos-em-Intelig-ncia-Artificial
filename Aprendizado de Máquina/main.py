import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import LabelEncoder

data = pd.read_csv('combined_data.csv')
x = data.drop(['label'], axis=1)
y = data['label']
x = LabelEncoder().fit_transform(x)

kmeans = KMeans(n_clusters=2)
kmeans.fit(y.values.reshape(-1, 1))
centroids = kmeans.cluster_centers_
labels = kmeans.labels_
predict = kmeans.fit_predict(x.reshape(-1, 1))
silhouette_avg = silhouette_score(x.reshape(-1, 1), predict)

plt.scatter(x.reshape(-1, 1), y, s=50)
plt.title("Dados De emails")
plt.show()
#imprime corretamente

plt.scatter(x, y, c=labels, s=50, cmap='viridis')
plt.scatter(centroids, centroids, c='red', marker='x', label='Centróides')
plt.title(f"Coeficiente de Silhueta médio: {silhouette_avg}\n")
plt.legend()
plt.show()
