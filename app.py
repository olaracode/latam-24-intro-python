students = ["Byron", "Maruan", "Jessica", "Lina", "Moises", "Juan", "Hector"]
student_data = {
    "id": 123,
    "cohort": "latam-24"
}
student_data["id"]
# iteramos una lista
for student in students:
    print(student)

# Iteramos en un rango
for i in range(20):
    print(i)

# Iteramos un diccionario
for key in student_data:
    if key == "id":
        print(student_data[key])

i = 0
# mientras la condicion se cumpla, imprime el numero incremental
# ==, <, <=, >=, >, or, and, !=, not

while i < 10:
    # print(i)
    i += 1

edad = 18
print(18 < 18)

if edad >= 18:
    print("Si puedes entrar")
else:
    print("No puedes entrar")

password = "12345678"
# si uno u el otro | el or
# si las dos o mas condiciones se cumplen | and

if len(password) < 8 or len(password) > 10:
    print("Tu contraseña tiene que tener entre 8 y 10 caracteres")
else:
    print("usuario creado")

if len(password) > 0 and len(password) < 10:
    print("La contraseña no puede estar vacia y debe ser menor a 10 caracteres")

