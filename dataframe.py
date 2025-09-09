
import pandas as pd

'''
El código proporcionado muestra una variedad de operaciones y métodos comunes para manipular Series de pandas.
Una Serie es una estructura de datos unidimensional, similar a un array o una lista, pero con la característica
clave de que cada elemento tiene una etiqueta de índice.
'''

def crearDataFrame():
    """
    Crea un DataFrame a partir de un diccionario de datos y
    demuestra varios métodos de visualización y atributos básicos.
    """
    # Se crea un diccionario de Python con los datos que se convertirán en DataFrame.
    # Cada clave del diccionario será una columna y cada lista será la fila de datos.
    data = {
        'Nombre': ['Hugo', 'Luis', 'Paco', 'Ana'],
        'Edad': [23, 45, 12, 36],
        'Ciudad': ['Medellín', 'Bello', 'Envigado', 'itagui'],
    }

    # Se crea el DataFrame 'df' a partir del diccionario 'data'.
    df = pd.DataFrame(data)

    # Imprime el DataFrame completo para ver su estructura.
    print(df)

    # Muestra las últimas 2 filas del DataFrame.
    print(df.tail(2))

    # Genera un resumen estadístico de las columnas numéricas (solo 'Edad' en este caso).
    print(df.describe())

    # Muestra los nombres de las columnas del DataFrame.
    print(df.columns)

    # Muestra el índice (etiquetas de fila) del DataFrame.
    print(df.index)

    # Muestra los valores del DataFrame como un array de NumPy.
    print(df.values)

    # La función devuelve el DataFrame creado.
    return df


def impimirDataFrame(miDf):
    """
    Demuestra cómo seleccionar, filtrar y ordenar datos en un DataFrame.
    """
    # Se asegura de que la entrada sea un DataFrame.
    df = pd.DataFrame(miDf)

    # Selecciona y muestra la columna 'Nombre'.
    print(df['Nombre'])

    # Selecciona y muestra las columnas 'Nombre' y 'Edad'.
    print(df[['Nombre', 'Edad']])

    # Selecciona la fila con el índice de etiqueta 0 usando .loc.
    print(df.loc[0])

    # Selecciona la fila en la posición entera 1 (la segunda fila) usando .iloc.
    print(df.iloc[1])

    # Filtra el DataFrame para mostrar solo las filas donde 'Edad' es mayor a 30.
    print(df[df['Edad'] > 30])

    # Filtra el DataFrame para mostrar las filas donde la 'Ciudad' está
    # en la lista ['Medellín', 'Bello'].
    print(df[df['Ciudad'].isin(['Medellín', 'Bello'])])

    # Ordena el DataFrame por la columna 'Ciudad' en orden alfabético.
    print(df.sort_values(by='Ciudad'))

    # Ordena el DataFrame por la columna 'Edad' de forma descendente.
    print(df.sort_values(by='Edad', ascending=False))