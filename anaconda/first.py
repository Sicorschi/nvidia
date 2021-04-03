import pandas as pd

df = pd.read_csv('http://bit.ly/autompg-csv') # guardamos en la variable df (data feed) la tabla de datos.
df.head() # visualizar los datos.

# %matplotlib inline
df.plot.scatter(x='colX', y='colY')