# La funcion no funciona correctamente, deberia sumar todos los numeros de la hora actual.
# Por ejemplo, 01:02:03 deberia retornar 6. Mejore y arregle la funcion, escriba un test(s)
# para esta. Use el framework que quiera.


# [TODO]: arreglar la funcion
def sum_current_time(time_str: str) -> int:
    """Expects data in the format HH:MM:SS"""
    list_of_nums = time_str.split(":")
    return sum(list_of_nums)