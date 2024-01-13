# string, number, double, float, 
# list, dictionary, bool, None

"""
Comentario multilinea
"""

texto = "Un texto"

# snake_case
nombre_largo = "Un texto"

numero = 0 # number
decimal = 10.321 # float
decimal_segundo = 10.00 # double

# List
lista = ["Un valor", "Dos valores"]
primer_valor = lista[0]

# Tupla (v1,v2,v3,) = lista pero no se puede modificar

# Diccionario
usuario = {
    "nombre": "Octavio",
    "usuario": "octavio"
}

# Accedemos al valor de nombre
usuario["nombre"] # value
usuario.keys() # Te muestra las llaves

es_verdad = True # Verdadero
es_falso = False # Falso



no_existe = None # Igual a Null | Undefined en JS


# print("Hola")

numero_de_prueba = 1

# + - / *


# print("Un texto" + "Con otro")

# print(1 + 1)
# print(2 - 1)
# print(2 * 2)
# print(2 / 2)
# print(2 % 2)

resultado = 20

# str() convierte en string
# print("Tu resultado es " + str(resultado))
# print(int("20") + 10)
# print(float(10))


usuario_nombre = "nombre"
usuario_edad = 20

# Interpolar texto con variables
mensaje_usuario = f"Tu nombre es: {usuario_nombre}, tienes: {usuario_edad}"
text_interpolation = "Texto %s, texto %s " % ("valor1", "valor2")
format_complicado = "Texto {}, Texto 2 {}".format("Valor1", "valor2")

frutas = ["pera", "Manzana", "Cambur", "Mango"]

# array[array.length() - 1]
# print(frutas[0]) # Primer elemento
# print(frutas[-1])

# lista[indice_inicio:indice_final] // El indice final no se incluye
manzana_pera = frutas[0:2]
cambur_mango = frutas[2:4]

# frutas.sort() # Ordena el arreglo modificandolo
# print(frutas)

# print(manzana_pera)
# print(cambur_mango)
# print(frutas)


frutas.append("Naranja") # Append agregamos elementos
frutas.append("Naranja") # Append agregamos elementos
frutas.insert(1, "Fresa") # lista.insert(posicion, valor)
# print("Antes de eliminar", frutas)

frutas.remove("Naranja") # Elimina el primer elemento de la lista que encuentra con el valor que pasas a la funcion
del frutas[0] # Eliminarmos por indice
# print("Despues de eliminar", frutas)

frutas_2 = ["Patilla", "Kiwi", "Mandarina"]

# frutas.extend(frutas_2)
frutas = frutas + frutas_2
# frutas += frutas_2
frutas.pop(0) # elimina el ultimo elemento de la lista o el elemento del indice que le pases
# print(frutas)
# print(len(frutas))
# frutas.extends(["Patilla", "Kiwi", "Mandarina"])

user = {
    "username": "usuario",
    "age": 20,
    "pais": "venezuela"
}

print(user["age"])

user["phone"] = "+589999999" # Para agregar un valor

user["age"] = 20
print(user)

# Las llaves de un diccionario
print(user.keys())
user.pop("phone") # elimina el [key] que le pasemos
key_value_tuplas = user.items() # retorna una lista de tuplas
# [(key, value), (key, value), (key, value)]
print(key_value_tuplas)
print(user.get("age", 1)) # user["age"]


print(type(user)) # typeof