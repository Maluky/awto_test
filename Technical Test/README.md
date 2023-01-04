# Awto DS/DE Technical Test
Esta prueba esta desarrollada para medir las capacidades de los integrantes del candidatos al equipo de ingenieria de awto. En especial este desafio esta pensado para el rol de DS/DE Lead.

## PARTE 1

### SQL TEST

Conectarse a la base de datos, especificada e la credenciales entregadas, para efectuar la prueba utilizando cualquier IDE de su elección.

Los datos para la conexión serán otorgados al inicio de la evaluación

Utilizar el archivo dummy_data y cargarlos en el esquema con tus iniciales, crear una tabla con el nombre "vehicle_actions"

Los campos del archivo corresponden a los cambios de estado de cada vehiculos, reflejado en cada registro:

- vehicle_action_id (Id del cambio de estado)
- vehicle_id (id del vehículo)
- start_date (fecha del comienxo del estado)
- va_status_id (Id del estado, donde 1 stand by, 2 reservado, 4 desactivado)
 
Se debe crear una vista en el esquema (ejemplo jp.juan_perez) la cual muestre por mes, cuantas horas permaneció cada vehículo en estado stand by.
 
SE EVALUARÁ LA PROLIJIDAD DE LA CONSULTA Y OBTENCIÓN DEL RESULTADO ESPERADO Y SE MEDIRA EL TIEMPO DE EJECUCIÓN.

## PARTE 2

### Data Pipelines

El objetivos de este ejercicio es diseñar e implementar una solución para procesar data en intervalos regulares (ej. diario). Asumimos que hay dos archivos con datos `dataset1.csv` y `dataset2.csv`. Programe una solucion que procese estos datos y un componente que permita a la tarea ejecutarse de forma periodicamente. El formato del output es un JSON/Diccionario.

Como orquestador de tareas, **se debe usar Apache Airflow** para implementar la solucion. Asumimos que la data usada para este ejercicio va a estar disponible a las 4am, todos los dias. Por favor proveea una documentacion clara y ordenada que explique la solucion, en formato markdown.

### Definición de la tarea: Transformacion de la data:
- Separar el campo `nombre` en `nombre` y `apellido`
- Redondear el campo `precio` a dos decimales
- Eliminar cualquier fila que no tenga un `nombre`
- Crear un nuevo campo `sobre_100`, el cual es `verdadero` cuando el precio es mayo a 100

*Nota: Adjunte el dataset procesado tambien.*

### Creditos Extra
No es necesario, pero de poder realizarlo, deseariamos poder correr el procesamiento de los dataset dentro de un container de docker (Ya sabes temas de costos), para este punto nos podemos olvidar de la orquestacion de la tarea y con que compilar la imagen. Entregar el dataset transformado como un output del contenedor en un volumen local es mas que suficiente.

### Bases de Datos
Un concesionario de automóviles lo contrata para crear su infraestructura de base de datos en una sola tienda. En cada día hábil, un equipo se dedica a la venta de automóviles, por consecuencia, cada transacción contendra información sobre la fecha y la hora de la transacción, en donde el cliente realizó la transacción, junto al automóvil que se vendió.

#### Los requerimientos son los siguientes:

- Cada auto solo puede ser vendido por una persona
- Hay vehiculos de multiples marcas vendiendose
- Cada auto tiene las siguientes caracteristicas
    - Marca
    - Modelo
    - Numero de Serializacion
    - Peso
    - Precio
- Cada venta/transaccion contiene la siguiente informacion:
    - Nombre del cliente
    - Telefono del Cliente
    - Vendedor
    - Caracteristicas del auto vendido

Crear un diagrama entidad relacion con la representacion de las base de datos, explicando la normalización llevada a cabo y los argumentos teoricos para dicha normalización.

#### Creditos Extra
1. Levantar un base de datos en PostgreSQL usando una imagen base de docker, esperando como resultado esperado un `Dockerfile` que permita levantar la base de datos y de manera automatica hidrate el modelo de datos DLL durante el bootstraping del contenedor. 

2. Tu equipo comercial, **necesita urgente** que le saques una query, para despejar las siguientes dudas:
    - Quiero saber la lista de nuestros clientes y su gasto.
    - Quiero saber el top 3 de marcas mas compradas en cantidad y el total de ventas en el mes actual.

### Arquitectura

Actualmente tu rol es ser el arquitecto de datos, y en este contexto estás diseñando una infraestructura en la nube para una empresa cuyo negocio principal es el procesamiento de imágenes.

La empresa dispone de una aplicación web que consolida las imágenes subidas por los clientes. Ademas, dicha compañia también tiene una aplicación web independiente que proporciona un flujo de imágenes utilizando Kafka Streams. Los ingenieros de software de la empresa ya tienen algo de código escrito para procesar las imágenes (De todas formas no podemos confiar en ello). A la empresa le gustaría guardar las imágenes procesadas durante un mínimo de 7 días con fines de archivo. Idealmente, la empresa desea tener Business Intelligence (BI) sobre estadísticas clave, incluido el número y el tipo de imágenes procesadas, y por cuales clientes.

Genere un diagrama de la arquitectura del sistema (p. ej., Visio, Powerpoint, Draw.io) utilizando cualquiera de los ecosistemas de proveedores de nube comerciales para explicar su diseño. Indique también claramente si ha hecho alguna suposición en algún momento para construir su modelo. Favor argumentar de forma clara la convergencia utilizada para llegar a la solución (Pathway).

### Graficos y APIs
Su equipo decidió diseñar un tablero para mostrar la estadística de casos de COVID19. Le han asignado la tarea de mostrar uno de los componentes del tablero, mostrando una representación de visualización de la cantidad de casos de COVID19 en Singapur a lo largo del tiempo.

Para esto, su equipo decidió usar los datos públicos ubicados en un conocido repositorio de información que utiliza el siguiente contrato: https://documenter.getpostman.com/view/10808728/SzS8rjbc#b07f97ba-24f4-4ebe-ad71-97fa35f3b683.

Fabrique un gráfico para mostrar el número de casos en Singapur a lo largo del tiempo, utilizando las API indicadas, las cuales estan ubicadas en: https://covid19api.com/.

### Unit Testing
En el archivo `broken_function.py` se encuentra una funcion que hay que reparar y luego realizar unit testing sobre la misma, o al reves si es que usted considera adecuado. Complete la solución indicando cual de los dos caminos siguio y porque.

### Caso de aplicación (Final countdown).
Navegue por la app de awto y su solución para entender brevemente el producto. Segun sus recomendaciones de experto e innovador en materia de DS, proponga una forma de implementar mecanismos de machine learning o modelos predictivos, que permitan mejorar la experiencia de los usuarios y su conversión. Para este fin, establesca los supuestos que crea necesario y argumente su propuesta de forma tanto teorica, como tecnica, indicando su impacto en el negocio.


### Guias para la Resolución
Por favor cree un repositorio publico con su desarrollo y envie un email con el link al mismo, adjuntando un PR o MR hacia la rama master donde documenta el test entregado. La parte teorica debe ser respondida en formato markdown, usando para las imagenes links que adjunten el contenido.

### Buenas Practicas
- Commits frecuentes y un historial (Git logs) claro en su desarrollo.
- Mensajes descriptivos en los commits
- Una documentacion clara
- Comentarios precisos en tu código
- Código limpio y legible
