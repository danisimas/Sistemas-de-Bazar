import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
import numpy as np

# Conjunto de treinamento
X_train = np.array([[30, 95, 205, 119], [25, 58, 160, 60], [50, 73, 150, 70], [28, 102, 200, 123], [60, 80, 204, 90], [37, 64, 170, 54], [40, 75, 142, 92]])
y_train = np.array(['S', 'N', 'N', 'S', 'S', 'N', 'S'])

# Instância desconhecida
X_test = np.array([[36, 65, 140, 75]])

# Treinamento da árvore de decisão
dtc = DecisionTreeClassifier()
dtc.fit(X_train, y_train)

# Identificação do grupo de pacientes mais semelhante à instância desconhecida
group = dtc.predict(X_test)

# Seleção dos pacientes dentro do grupo identificado
X_train_group = X_train[y_train == group[0]]
y_train_group = y_train[y_train == group[0]]

# Previsão com k-NN
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train_group, y_train_group)
y_pred_knn = knn.predict(X_test)

# Previsão final combinando a árvore de decisão e k-NN
if group == y_pred_knn:
    y_pred = y_pred_knn
else:
    y_pred = dtc.predict(X_test)

print("Previsão final:", y_pred)
