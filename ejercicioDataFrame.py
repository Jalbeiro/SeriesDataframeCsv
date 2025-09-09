

'''
Imagina que eres un analista de marketing en una empresa de e-commerce. Tu tarea es analizar un conjunto de datos de clientes para entender mejor sus hábitos de compra. Los datos están organizados en una tabla (un DataFrame) y tu trabajo es extraer información valiosa para la toma de decisiones.
Tu objetivo es usar los métodos de pandas para responder preguntas clave sobre tus clientes, como:
¿Cuál es el rango de edad de tus clientes?
¿Dónde se concentran la mayoría de tus clientes?
¿Cuál es el método de pago más popular?
¿Hay alguna relación entre la edad y el gasto de los clientes?
Paso 1: Configuración
Primero, crea un DataFrame de pandas con los datos de clientes proporcionados. Este DataFrame contendrá columnas como el ID del cliente, su edad, la ciudad donde reside, su método de pago preferido y el total gastado en su última compra.
'''

data = {
    'customer_id': [101, 102, 103, 104, 105, 106, 107, 108],
    'age': [25, 34, 45, 29, 38, 52, 22, 41],
    'city': ['Medellín', 'Bogotá', 'Medellín', 'Cali', 'Barranquilla', 'Bogotá', 'Medellín', 'Cali'],
    'payment_method': ['Credit Card', 'Cash', 'Debit Card', 'Credit Card', 'Cash', 'Debit Card', 'Credit Card', 'Cash'],
    'total_spent': [50.5, 75.2, 120.0, 30.8, 90.1, 150.0, 45.0, 85.5]
}
clientes_df = pd.DataFrame(data)


'''
Ahora, usa los conceptos de DataFrame que has aprendido para completar las siguientes tareas. ¡Recuerda que puedes combinar métodos para lograr tus objetivos!
1. Exploración de datos:
Muestra un resumen estadístico de la columna age y total_spent.
Muestra el nombre de todas las columnas.
Muestra solo las filas de los clientes que residen en 'Medellín'.
2. Análisis de datos:
Calcula el promedio de edad de los clientes.
Encuentra el cliente que ha gastado la mayor cantidad de dinero. (Pista: puedes ordenar el DataFrame y luego seleccionar la primera fila).
Cuenta cuántos clientes hay en cada ciudad.
Muestra la distribución de los métodos de pago.
3. Filtrado avanzado y manipulación:
Filtra el DataFrame para encontrar clientes mayores de 35 años que pagaron con 'Credit Card'.
Crea una nueva columna llamada is_high_spender que sea True si el cliente ha gastado más de $100.0 y False en caso contrario.
'''

