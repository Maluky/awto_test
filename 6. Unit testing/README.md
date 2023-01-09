# Nuestro equipo nuevamente se ve enfrentado a dificultades tecnicas..
## En este momento tenemos que arreglar una función mal realizada y corroborar que funciones para variados casos.

La función en dañada es la siguiente:
```python
# [TODO]: arreglar la funcion
def sum_current_time(time_str: str) -> int:
    """Expects data in the format HH:MM:SS"""
    list_of_nums = time_str.split(":")
    return sum(list_of_nums)
```
Podemos notar que el error se produce al momento de retornar la suma de valores, ya que posterior al split, se conservan caracteres del tipo string, por lo que no se pueden sumar strings.

Habilmente nuestro equipo captó con agilidad el error y propuso la siguiente función.
```python
def sum_current_time(time_str: str) -> int:
    """Expects data in the format HH:MM:SS"""
    list_of_nums = time_str.split(":")
    return sum(int(n) for n in list_of_nums)
```
Meticulosamente, y de forma agil, el resto del equipo desarrolla las pruebas de test unitarios.
```python
def test_sum_current_time():
    print(sum_current_time("12:34:56") == 12 + 34 + 56)
    print(sum_current_time("00:01:59") == 0 + 1 + 59)
    print(sum_current_time("23:59:59") == 23 + 59 + 59)
```
Gracias al esfuerzo de todo el equipo, se pudo corregir la función y realizar pruebas unitarias para verificar su funcionamiento.