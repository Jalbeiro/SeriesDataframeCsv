import pandas as pd
'''
Este código se enfoca en la carga, exploración y manipulación de datos desde un archivo CSV. 
Un CSV (Comma-Separated Values) es un formato de archivo de texto plano que usa comas 
(u otros delimitadores) para separar valores. Pandas tiene herramientas muy potentes 
para leer y escribir estos archivos, convirtiéndolos en DataFrames, 
que son estructuras ideales para el análisis de datos.
'''

def cargarCSV():
    """
    Carga un archivo CSV en un DataFrame y demuestra diversas operaciones
    de exploración y manipulación de datos.
    """
    # Se utiliza el método 'read_csv' de pandas para leer el archivo CSV
    # './customer_data.csv' y cargarlo en un DataFrame llamado 'clientes'.
    clientes = pd.read_csv('./customer_data.csv')

    # Imprime el DataFrame completo para una vista general.
    print(clientes)

    # Muestra las primeras dos filas del DataFrame para una vista rápida de los datos.
    print(clientes.head(2))

    # Genera un resumen estadístico de las columnas numéricas del DataFrame.
    print(clientes.describe())

    # Muestra los nombres de las columnas del DataFrame.
    print(clientes.columns)

    # Muestra el índice (etiquetas de las filas) del DataFrame.
    print(clientes.index)

    # Muestra los valores del DataFrame como un array de NumPy.
    print(clientes.values)

    # Selecciona y muestra la columna 'customer_id'.
    print(clientes['customer_id'])

    # Selecciona y muestra múltiples columnas: 'customer_id' y 'age'.
    print(clientes[['customer_id', 'age']])

    # Selecciona la fila con el índice de etiqueta 0 usando el método .loc.
    print(clientes.loc[0])

    # Selecciona la fila en la posición entera 1 (la segunda fila) usando el método .iloc.
    print(clientes.iloc[1])

    # Filtra el DataFrame para mostrar solo los clientes con 'age' mayor a 30.
    print(clientes[clientes['age'] > 30])

    # Filtra el DataFrame para mostrar los clientes cuyo 'payment_method'
    # está en la lista ['Credit Card', 'Cash'].
    print(clientes[clientes['payment_method'].isin(['Credit Card', 'Cash'])])

    # Ordena el DataFrame por la columna 'payment_method' de forma ascendente.
    print(clientes.sort_values(by='payment_method'))

    # Ordena el DataFrame por la columna 'age' de forma descendente (los más jóvenes primero).
    print(clientes.sort_values(by='age', ascending=False))

    # Filtrar por edad mayor a 30 y método de pago igual a 'Debit Card'.
    # Se usan paréntesis para asegurar la precedencia de las operaciones lógicas.
    print(clientes[(clientes['age'] > 30) & (clientes['payment_method'] == 'Debit Card')])

    # Agregar una nueva columna llamada 'double_age' con el doble de los valores de la columna 'age'.
    clientes['double_age'] = clientes['age'] * 2
    print(clientes)

    # Realizar operaciones aritméticas en una columna, como sumar 10 a la edad.
    clientes['age_plus_10'] = clientes['age'] + 10
    print(clientes)

    # Realizar operaciones estadísticas en la columna 'age'.

    # Calcula la media de la edad.
    print(clientes['age'].mean())

    # Calcula la mediana de la edad.
    print(clientes['age'].median())

    # Calcula la moda (valor más frecuente) de la edad.
    print(clientes['age'].mode())

    # Calcula la desviación estándar de la edad.
    print(clientes['age'].std())

    # Encuentra el valor mínimo de la edad.
    print(clientes['age'].min())

    # Encuentra el valor máximo de la edad.
    print(clientes['age'].max())

    # Suma todos los valores de la edad.
    print(clientes['age'].sum())

    # Calcula la suma acumulativa de la edad.
    print(clientes['age'].cumsum())

    # Genera un resumen estadístico completo de la edad, incluyendo conteo, media, std, min, percentiles y max.
    print(clientes['age'].describe())


if __name__ == '__main__':
    # Esta es una buena práctica para que el código dentro de la función se ejecute
    # solo cuando el script es el programa principal.
    cargarCSV()