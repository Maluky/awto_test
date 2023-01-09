# El objetivo de este ejercicio es realizar un iterador diario a las 4am usando Apache Airflow como orquestador
## A su vez se tienen que realizar ciertas tareas especificas con los dataset
```python

import airflow
import pandas as pd
import json

# Establecer rutas de archivos
dataset1_path = '/ruta/a/dataset1.csv'
dataset2_path = '/ruta/a/dataset2.csv'
output_path = '/ruta/de/salida/output.json'

# Carga de los frames para ejecución local
# df1 = pd.read_csv("C:/Users/Alonso/Desktop/postulaciones ds/awto/Technical Test/dataset1.csv")
# df2 = pd.read_csv("C:/Users/Alonso/Desktop/postulaciones ds/awto/Technical Test/dataset2.csv")

def remove_prefix(serie, prefixs):
    for prefix in prefixs:
        serie = serie.str.removeprefix(prefix)
    return serie

def extract_tittles(serie):
    return serie.str.extract(r'(\w+\. )')

def fix_miss(serie):
    return serie.replace('Miss ', 'Miss. ', regex=True)

def set_price(serie):
    return serie.astype('float').round(2)

def process_data(df1, df2):
    # Unión de frames
    df = pd.concat([df1,df2])
    # Se eliminan los campos vacios en nombre
    df.dropna(subset='nombre', inplace=True)
    # Se normaliza el titulo de miss
    df['nombre'] = fix_miss(df['nombre'])
    # Se extraen los titulos de las personas
    df['Titulos'] = extract_tittles(df['nombre'])
    # Se realiza una separación con los prefijos
    df['nombre'] = remove_prefix(df['nombre'], list(df['Titulos'].dropna().unique()) )
    # Se crea un frame de soporte
    fd = df.nombre.str.split(' ', expand=True)
    # Con el frame de soporte se anexan las columnas de valor a frame principal
    df['Nombre'], df['Apellido'], df['Grado'] = fd[0], fd[1], fd[2]
    # Se eliminan los nombres que al final del proceso quedan vacios
    df.drop('nombre', axis=1, inplace=True)
    # Se setean los precios a dos decimales
    df['precio'] = set_price(df['precio'])
    # Con el fin de agregar valor a la información se crean 5 quintiles para su segmentación
    df['Quintiles'] = pd.cut(df.precio, bins=5, labels=['Q1','Q2','Q3','Q4','Q5'])
    
    with open(output_path, 'w') as f:
        json.dump(df.to_dict(orient='records'), f)
        
    return df.to_dict(orient='records')

# Ejecución de la función
# df = process_data(df1, df2)

# Crear DAG
dag = airflow.DAG(
    'procesamiento_datos',
    schedule_interval='0 4 * * *',
    start_date=airflow.utils.dates.days_ago(2),
    catchup=False
)

# Añadir tarea de procesamiento de datos
t1 = airflow.operators.PythonOperator(
    task_id='procesar_datos',
    python_callable=process_data,
    op_args=[dataset1_path, dataset2_path],
    dag=dag
)

```

En la función process_data se realiza el procesamiento de los dataset, dentro de ella podemos encontrar las subfunciones que ejecutan los distintos metodos para la progreción del mismo.

###### Este es un dag propuesto en un marco teórico, ya que se trato de levantar Apache Airflow y surguieron varias dificultades tecnicas.
