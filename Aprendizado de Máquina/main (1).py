import pandas as pd
from pandas.core.arrays.sparse import array
import numpy as np
from sklearn.neural_network import MLPClassifier
import sklearn.metrics as metrics
from sklearn.preprocessing import LabelEncoder

from sklearn.model_selection import train_test_split, cross_val_score

# Carregando arquivo csv
data = pd.read_csv('combined_data.csv')

# Fazendo separação dos dados
x = data.drop(['label'], axis=1)
y = data['label']

x = LabelEncoder().fit_transform(x)
y.ravel()
# Dividindo os dados
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.0001, random_state=42)

# Iniciando a RNA
mlp = MLPClassifier(activation='logistic',
                    max_iter=10000,
                    hidden_layer_sizes=(10, ),
                    alpha=0.01,
                    solver='lbfgs')

# Conjunto de treinamento
mlp.fit(x_train.reshape(-1, 1), y_train.values.ravel())

# Prevendo a saída para os dados de teste
predictions = mlp.predict(x_test.reshape(-1, 1))

print("\nSaídas da RNA:\n", predictions)
print("\nSaídas esperadas:\n", y_test, "\n")

# Cria a matriz de confusão (problemas de classificação)
cm = metrics.confusion_matrix(y_test.values.ravel(), predictions)
print("Matriz de Confusão:\n")
print(cm)

# Calcula a acurácia (problemas de classificação)
accuracy = metrics.accuracy_score(y_test.values.ravel(), predictions)
print("Acurácia:", accuracy, "\n")

# Implemente a validação cruzada
cross_val_scores = cross_val_score(mlp, x.reshape(-1, 1), y, cv=10)  # cv é o número de folds

# Exiba as pontuações de cada fold
print("Pontuações de validação cruzada:", cross_val_scores)

# Exiba a média das pontuações de validação cruzada
print("\nMédia das pontuações de validação cruzada:", cross_val_scores.mean(),
      "\n")

# Link da base de dados: https://www.kaggle.com/datasets/purusinghvi/email-spam-classification-dataset
