# La oportunidad consiste en crear un esquema de base de datos para una consecionaria de automóviles
Para fortuna de la consecionaria, contamos con el mejor equipo y se definio el siguiente esquema.

![Diagram](https://github.com/Maluky/awto_test/blob/main/3.%20Data%20Base/Diagrama%20sin%20t%C3%ADtulo.png "Diagrama base de datos")

Este a su vez cumple con los requicitos minimos operantes

- [x] Cada auto solo puede ser vendido por una persona
- [x] Hay vehiculos de multiples marcas vendiendose
- [x] Cada auto tiene las siguientes caracteristicas
	* Marca
	* Modelo
	* Numero de Serializacion
	* Peso
	* Precio
- [x] Cada transaccion contiene la siguiente información
	* Nombre del cliente
	* Telefono del Cliente
	* Vendedor
	* Caracteristicas del auto vendido
### Para entender el esquema lo leemos de la siguiente forma
El cliente al momento de tener la desición de que modelo de auto va a comprar se crea una transacción, la cual tiene que ser gestionada por un vendedor, es decir, cada transacción 
tiene asociada un auto, que como se describe tiene una marca, modelo, numero de serie, peso y precio, esta transacción tiene que ser procesada por un vendedor, que lo registramos con 
nombre y apellido, y para registrar el proceso de venta, quedan como registro el ID de la transacción, la fecha y hora, el ID del auto, ID cliente y ID vendedor

### Si abordamos el plus de montarlo en un postgre en un docker se va a tener que recurrir al equipo especialista en esta materia, no se abordo en la etapa de propuesta.

### Como es común, el equipo de marketing elevó una dudas para poner en marcha lo antes posible sus consultas cotidianas y se elaboraron las siguientes consultas

#### Quiero saber la lista de nuestros clientes y su gasto.
```sql
SELECT c.nombre, SUM(t.precio_total) AS gasto
FROM clientes c
JOIN transacciones t ON t.cliente_id = c.id
GROUP BY c.nombre
```

#### Quiero saber el top 3 de marcas mas compradas en cantidad y el total de ventas en el mes actual.
```sql
SELECT a.marca, COUNT(*) AS cantidad_vendidos, SUM(t.precio_total) AS ventas
FROM autos a
JOIN transacciones t ON t.auto_id = a.id
WHERE t.fecha BETWEEN current_date - INTERVAL '1 month' AND current_date
GROUP BY a.marca
ORDER BY cantidad_vendidos DESC
LIMIT 3;
```

#### Como equipo quedamos conforme con la propuesta levantada a la consecionaria automovilistica, esperamos que sea del agrado del futuro cliente.