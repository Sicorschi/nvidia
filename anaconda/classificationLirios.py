# Carga de modulos y librerias

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
%matplotlib inline

"""
A continuación, cargaremos los datos. Lo vamos a hacer directamente desde el repositorio de Machine Learning UCI . 
Para ello usamos la librería pandas, que acabamos de cargar, y que también nos será útil para el análisis exploratorio de los datos,
porque dispone de herramientas de visualización de datos y de estadística descriptiva.
Tan sólo necesitamos conocer la URL del dataset y especificar los nombres de cada columna al cargar los datos (‘sepal-length’, ‘sepal-width’, ‘petal-length’, ‘petal-width’, ‘class’).
"""

# Carga del dataset del repositorio uando pandas:

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = pandas.read_csv(url, names=names)

"""
En la fase de ecploracion vamos a fijarnos en temas como la dimensión de los datos, 
qué aspecto tienen, vamos a hacer un pequeño análisis estadístico de sus atributos y vamos a agruparlos por clases. 
Cada una de estas acciones no reviste mayor dificultad que la ejecución  de un comando que, además podrás reutilizar una y otra vez en proyectos futuros.
En particular, trabajaremos con la función shape, que nos dará las dimensiones del dataset, 
la función head, que nos mostrará los datos (le indicaremos el número de registros que queremos que nos muestre), 
y la función describe, que nos dará valores estadísticos sobre el dataset.
"""

# Dimensiones del dataset
print(dataset.shape)

# Muestra los 20 primeros
print(dataset.head(20))

# Descripción del dataset
print(dataset.describe())

"""
Pasamos a visualizar los datos. Podemos realizar gráficos de una variable, que nos ayudarán a entender mejor cada atributo individual,
o gráficos multivariable, que permiten analizar las relaciones entre atributos.
"""

# Box and whisker plots:

dataset.plot(kind='box', subplots=True, layout=(
    2, 2), sharex=False, sharey=False)
plt.show()

"""
También podemos crear un histograma de cada atributo o variable para hacernos una idea de qué tipo de distribución siguen. 
"""

# histogramas
dataset.hist()
plt.show()

"""
Con el siguiente código, que, como hemos hecho hasta ahora podemos teclear o copiar y pegar en nuestro Jupyter Notebook,
separamos los datos en los conjuntos de entrenamiento X_train, Y_train, y los de validación X_validation, Y_validation.
Normalmente la tendencia es reservar el 80% de tus datos en entrenar el modelo y el 20% restante en validar la precion de tu modelo.
"""


# Split-out validation dataset
array = dataset.values
X = array[:, 0:4]
Y = array[:, 4]
validation_size = 0.20
seed = 7
X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(
    X, Y, test_size=validation_size, random_state=seed)

"""
Como a priori no sabemos qué algoritmos pueden funcionar mejor para este problema, 
vamos a probar con 6 diferentes, tanto lineales (LR, LDA), como no lineales (KNN, CART, NB y SVM).
Las gráficas iniciales ya indican que podemor ir por buen camino, porque que se aprecia que algunas clases van a ser linealmente separables en alguna dimensión. 
Vamos a evaluar los siguientes algoritmos:

Regresión logística (LR)
Análisis del Discriminante lineal (LDA)
K- Vecinos más cercanos (KNN)
Árboles de clasificación y regresión (CART)
Gaussiana Naive Bayes (NB)
Máquinas de vectores de soporte (SVM)

Antes de cada ejecución resetearemos el valor inicial (seed) 
para asegurarnos que la evaluación de cada algoritmo se realiza usando el mismo conjunto de datos (data split),
para asegurarnos de que los resultados sean directamente comparables.
"""

# Spot Check Algorithms
models = []
models.append(('LR', LogisticRegression()))
models.append(('LDA', LinearDiscriminantAnalysis()))
models.append(('KNN', KNeighborsClassifier()))
models.append(('CART', DecisionTreeClassifier()))
models.append(('NB', GaussianNB()))
models.append(('SVM', SVC()))

# evaluate each model in turn
results = []
names = []
for name, model in models:
    kfold = skmodel.KFold(n_splits=10, random_state=seed)
    cv_results = skmodel.cross_val_score(
        model, X_train, Y_train, cv=kfold, scoring=scoring)
    results.append(cv_results)
    names.append(name)
    msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
    print(msg)
