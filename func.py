# funciones
# las funciones son bloques de codigo reutilizables

# function nombreFuncion(parametro1, parametro2){ // tu codigo }

# def nombre_funcion(parametro1, parametro2):
#   bloque de codigo
def suma(a, b):
    return a + b

# function suma(){}
def resta(a, b):
    return a - b

def divide(a, b):
    return a / b 

def multiply(a, b):
    return a * b

def suma_usuario():
    num_1 = input("Ingresa el primer numero: ")
    num_1 = int(num_1)
    num_2 = input("Ingresa el segundo numero: ")
    num_2 = int(num_2)
    print("SUMA")
    print(num_1 + num_2)

## DE CLI Command Line Interface

## Somos un sistema administrativo de los años 90

# tenga una base de datos de empleados(Una lista de diccionarios)
# Nos permite filtrar por nombre del empleado
# Nos permita filtrar por el salario
# Nos permita eliminar el usuario
# Nos pregunte si queremos hacer otra operacion al final

def interfaz_administrativa():
    pass