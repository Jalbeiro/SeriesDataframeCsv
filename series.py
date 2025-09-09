import pandas as pd


# ----------------- Funciones de Nombres -----------------
'''
El código proporcionado muestra una variedad de operaciones y métodos comunes para manipular Series de pandas. 
Una Serie es una estructura de datos unidimensional, similar a un array o una lista, pero con la característica 
clave de que cada elemento tiene una etiqueta de índice.'''
def metodoSeries():
    """
    Demuestra varios métodos y atributos de las Series de pandas
    utilizando una Serie de cadenas de texto (nombres).
    """
    # Crea una Serie llamada 'nombres'
    nombres = pd.Series(['Hugo', 'Luis', 'Paco', 'Hugo'])

    # Imprime la Serie completa.
    print(nombres)

    # Accede al elemento en la posición de índice 0.
    print(nombres[0])

    # Realiza un 'slicing' (corte) para obtener los elementos
    # desde la posición 1 hasta la 3 (sin incluir la 3).
    print(nombres[1:3])

    # Imprime el índice de la Serie.
    print(nombres.index)

    # Imprime los valores de la Serie como un array de NumPy.
    print(nombres.values)

    # Imprime el tipo de dato de los elementos de la Serie.
    print(nombres.dtype)

    # Imprime el número total de elementos en la Serie.
    print(nombres.size)

    # Imprime la forma (shape) de la Serie. Como es unidimensional,
    # el resultado es una tupla con un solo elemento.
    print(nombres.shape)

    # Imprime los valores únicos de la Serie.
    print(nombres.unique())

    # Cuenta la frecuencia de cada valor único.
    print(nombres.value_counts())

    # Devuelve una Serie booleana con 'True' si el valor es nulo (NaN),
    # y 'False' en caso contrario.
    print(nombres.isnull())

    # Devuelve una Serie booleana con 'True' si el valor NO es nulo,
    # y 'False' en caso contrario. Es lo opuesto a isnull().
    print(nombres.notnull())

    # Muestra los primeros 2 elementos de la Serie.
    print(nombres.head(2))

    # Muestra los últimos 2 elementos de la Serie.
    print(nombres.tail(2))

    # Muestra una muestra aleatoria de 2 elementos de la Serie.
    print(nombres.sample(2))

    # Ordena los valores de la Serie de forma ascendente.
    print(nombres.sort_values())

    # Ordena la Serie por su índice.
    print(nombres.sort_index())

    # Convierte todas las cadenas de la Serie a mayúsculas.
    print(nombres.str.upper())

    # Convierte todas las cadenas a minúsculas.
    print(nombres.str.lower())

    # Calcula la longitud de cada cadena en la Serie.
    print(nombres.str.len())

    # Comprueba si cada cadena contiene la letra 'a'.
    # Devuelve una Serie booleana.
    print(nombres.str.contains('a'))

    # Reemplaza todas las ocurrencias de 'a' por 'o' en las cadenas.
    print(nombres.str.replace('a', 'o'))


def filtrarNombres():
    """
    Demuestra cómo filtrar una Serie de nombres utilizando
    condiciones lógicas.
    """
    nombres = pd.Series(['Hugo', 'Luis', 'Paco', 'Hugo'])

    # Filtra la Serie para mostrar solo los nombres que contienen 'a'.
    print(nombres[nombres.str.contains('a')])

    # Filtra la Serie para mostrar los nombres que están en la lista
    # ['Hugo', 'Paco'].
    print(nombres[nombres.isin(['Hugo', 'Paco'])])


def agregarNombres():
    """
    Demuestra cómo agregar elementos a una Serie.
    """
    nombres = pd.Series(['Hugo', 'Luis', 'Paco', 'Hugo'])

    # Agrega una nueva Serie a la existente.
    # El método 'append' está obsoleto en versiones recientes de pandas,
    # se recomienda usar 'pd.concat'.
    nombres = nombres.append(pd.Series(['Ana', 'Marta']))
    print(nombres)

    # Reinicia el índice de la Serie, asignando nuevos índices secuenciales.
    # El parámetro 'drop=True' elimina el índice antiguo.
    nombres = nombres.reset_index(drop=True)
    print(nombres)


def eliminarNombres():
    """
    Demuestra cómo eliminar elementos de una Serie.
    """
    nombres = pd.Series(['Hugo', 'Luis', 'Paco', 'Hugo'])

    # Elimina los elementos en los índices 1 y 3.
    nombres = nombres.drop([1, 3])
    print(nombres)

    # Reinicia el índice de la Serie después de la eliminación.
    nombres = nombres.reset_index(drop=True)
    print(nombres)


def modificarNombres():
    """
    Demuestra cómo modificar elementos de una Serie.
    """
    nombres = pd.Series(['Hugo', 'Luis', 'Paco', 'Hugo'])

    # Modifica el elemento en la posición de índice 0.
    nombres[0] = 'Ana'
    print(nombres)

    # Modifica todos los elementos que tienen el valor 'Hugo'
    # a 'Carlos'.
    nombres[nombres == 'Hugo'] = 'Carlos'
    print(nombres)


# ----------------- Funciones de Edades (Números) -----------------

def edades():
    """
    Demuestra varios métodos y atributos de las Series
    con valores numéricos (edades).
    """
    # Crea una Serie de números enteros.
    edades = pd.Series([23, 45, 12, 36, 52, 23, 40])

    # Las siguientes líneas son las mismas que en la función 'metodoSeries',
    # pero aplicadas a números.
    print(edades)
    print(edades[0])
    print(edades[1:3])
    print(edades.index)
    print(edades.values)
    print(edades.dtype)
    print(edades.size)
    print(edades.shape)
    print(edades.unique())
    print(edades.value_counts())
    print(edades.isnull())
    print(edades.notnull())
    print(edades.head(2))
    print(edades.tail(2))
    print(edades.sample(2))
    print(edades.sort_values())
    print(edades.sort_index())

    # Métodos específicos para Series numéricas:
    # Calcula la media de los valores.
    print(edades.mean())

    # Calcula la mediana de los valores.
    print(edades.median())

    # Calcula la moda de los valores (el valor que más se repite).
    print(edades.mode())

    # Calcula la desviación estándar de los valores.
    print(edades.std())

    # Encuentra el valor mínimo.
    print(edades.min())

    # Encuentra el valor máximo.
    print(edades.max())

    # Suma todos los valores.
    print(edades.sum())

    # Calcula la suma acumulativa.
    print(edades.cumsum())

    # Genera estadísticas descriptivas (conteo, media, std, min,
    # percentiles y max).
    print(edades.describe())

    # Calcula el percentil 80.
    print(edades.quantile(0.80))


def filtrarEdades():
    """
    Demuestra cómo filtrar una Serie de edades utilizando
    condiciones lógicas.
    """
    edades = pd.Series([23, 45, 12, 36, 52, 23, 40])

    # Filtra para mostrar solo las edades mayores a 30.
    print(edades[edades > 30])

    # Filtra para mostrar las edades que son mayores a 20 Y menores a 40.
    print(edades[(edades > 20) & (edades < 40)])

    # Filtra para mostrar las edades que están en la lista
    # [23, 36, 52].
    print(edades[edades.isin([23, 36, 52])])


def agregarEdad():
    """
    Demuestra cómo agregar elementos a una Serie de edades.
    """
    edades = pd.Series([23, 45, 12, 36, 52, 23, 40])
    edades = edades.append(pd.Series([30, 25]))
    print(edades)

    edades = edades.reset_index(drop=True)
    print(edades)


def eliminarEdad():
    """
    Demuestra cómo eliminar elementos de una Serie de edades.
    """
    edades = pd.Series([23, 45, 12, 36, 52, 23, 40])
    edades = edades.drop([1, 3])
    print(edades)

    edades = edades.reset_index(drop=True)
    print(edades)


def modificarEdad():
    """
    Demuestra cómo modificar elementos de una Serie de edades.
    """
    edades = pd.Series([23, 45, 12, 36, 52, 23, 40])

    # Modifica la primera edad (índice 0).
    edades[0] = 30
    print(edades)

    # Modifica todas las edades mayores a 30 a 35.
    edades[edades > 30] = 35
    print(edades)


def estadisticasEdades():
    """
    Demuestra el cálculo de estadísticas básicas de una Serie de edades.
    """
    edades = pd.Series([23, 45, 12, 36, 52, 23, 40])

    # Calcula la media.
    print(edades.mean())

    # Calcula la mediana.
    print(edades.median())

    # Encuentra el valor mínimo.
    print(edades.min())

    # Encuentra el valor máximo.
    print(edades.max())

    # Genera estadísticas descriptivas.
    print(edades.describe())

    # Suma todos los valores.
    print(edades.sum())