# Primera parte de la prueba
## El objetivo es realizar una conección a una base de datos, realizar la carga de datos y crear una tabla vista de los archivos.

```python
import mysql.connector

# Reemplazar estos valores con las credenciales de su base de datos
server = "localhost"
username = "my_username"
password = "my_password"
database = "my_database"

# Crear conexión
cnx = mysql.connector.connect(
    host=server,
    user=username,
    password=password,
    database=database
)

# Crear cursor
cursor = cnx.cursor()

# Crear tabla "vehicle_actions"
query = """
CREATE TABLE vehicle_actions (
  vehicle_action_id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  vehicle_id INT(6) NOT NULL,
  start_date DATETIME NOT NULL,
  va_status_id INT(6) NOT NULL
);
"""
cursor.execute(query)
# Cargar datos del archivo dummy_data en la tabla "vehicle_actions"
query = """
LOAD DATA INFILE '/path/to/dummy_data.csv' INTO TABLE vehicle_actions
FIELDS TERMINATED BY ',' ENCLOSED BY '\"'
LINES TERMINATED BY '\n'
(vehicle_action_id, vehicle_id, start_date, va_status_id);
"""
cursor.execute(query)

# Crear vista "juan_perez"
query = """
CREATE VIEW jp.juan_perez AS
SELECT vehicle_id, MONTH(start_date) AS month, SUM(TIMESTAMPDIFF(HOUR, start_date, end_date)) AS hours_stand_by
FROM vehicle_actions
WHERE va_status_id = 1
GROUP BY vehicle_id, month;
"""
cursor.execute(query)

# Cerrar cursor y conexión
cursor.close()
cnx.close()


```
### El problema se abordó con python, en donde se crea un script que realice la conección, las credenciales para server, username, password y database son "localhost", "my_username", "my_password" y "my_database" respectivamente, y finalmente se crea el cursor respectivo.
### Despúes se se crea la tabla solicitada usando el siguiente script
```python
# Crear tabla "vehicle_actions"
query = """
CREATE TABLE vehicle_actions (
  vehicle_action_id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  vehicle_id INT(6) NOT NULL,
  start_date DATETIME NOT NULL,
  va_status_id INT(6) NOT NULL
);
"""
cursor.execute(query)
```
### Continuamos con la carga de datos, en donde '/path/to/dummy_data.csv' especifica la ruta del archivo, el resto de argumentos es para el parseo de datos
```python
# Cargar datos del archivo dummy_data en la tabla "vehicle_actions"
query = """
LOAD DATA INFILE '/path/to/dummy_data.txt' INTO TABLE vehicle_actions
FIELDS TERMINATED BY ',' ENCLOSED BY '\"'
LINES TERMINATED BY '\n'
(vehicle_action_id, vehicle_id, start_date, va_status_id);
"""
cursor.execute(query)
```
### Finalmente se realiza la tabla vista y se cierran las conexiones
```python
# Crear vista "juan_perez"
query = """
CREATE VIEW jp.juan_perez AS
SELECT vehicle_id, MONTH(start_date) AS month, SUM(TIMESTAMPDIFF(HOUR, start_date, end_date)) AS hours_stand_by
FROM vehicle_actions
WHERE va_status_id = 1
GROUP BY vehicle_id, month;
"""
cursor.execute(query)

# Cerrar cursor y conexión
cursor.close()
cnx.close()
```