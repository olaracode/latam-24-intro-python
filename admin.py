employees = [
    {"department": "HR", "name": "John", "last_name": "Doe", "salary": 50000},
    {"department": "IT", "name": "Jane", "last_name": "Smith", "salary": 60000},
    {"department": "Sales", "name": "Mike", "last_name": "Johnson", "salary": 55000},
    {"department": "Finance", "name": "Emily", "last_name": "Brown", "salary": 65000},
    {"department": "HR", "name": "David", "last_name": "Wilson", "salary": 52000},
    {"department": "IT", "name": "Sarah", "last_name": "Davis", "salary": 58000},
    {"department": "Sales", "name": "Alex", "last_name": "Taylor", "salary": 53000},
    {"department": "Finance", "name": "Olivia", "last_name": "Miller", "salary": 67000},
    {"department": "HR", "name": "Daniel", "last_name": "Anderson", "salary": 51000},
    {"department": "IT", "name": "Sophia", "last_name": "Wilson", "salary": 59000},
    {"department": "Sales", "name": "William", "last_name": "Thomas", "salary": 54000},
    {"department": "Finance", "name": "Ava", "last_name": "Martinez", "salary": 63000},
    {"department": "HR", "name": "Michael", "last_name": "Harris", "salary": 53000},
    {"department": "IT", "name": "Mia", "last_name": "Clark", "salary": 57000},
    {"department": "Sales", "name": "James", "last_name": "Lewis", "salary": 52000},
    {"department": "Finance", "name": "Emma", "last_name": "Lee", "salary": 66000},
    {"department": "HR", "name": "Matthew", "last_name": "Walker", "salary": 54000},
    {"department": "IT", "name": "Liam", "last_name": "Hall", "salary": 61000},
    {"department": "Sales", "name": "Grace", "last_name": "Young", "salary": 55000},
    {"department": "Finance", "name": "Benjamin", "last_name": "Gonzalez", "salary": 64000}
]


def employee_by_name():
    print("Filtrando por nombre de empleado")
    filtro = input("Ingrese el nombre: ")
    for employee in employees:
        if employee["name"].upper() == filtro.upper():
            return employee
        
def edit_employee(employee):
    index_employee = employees.index(employee)
    for key,value in employee.items():
        edit  = input(f"Editar campo {key} : ")
        if edit:
            employee[key]=edit
    employees[index_employee] = employee

def initial_menu():
    print("Bienvenido al Panel de Administración")
    print("-------------------------------------")
    print("0.- Salir")
    print("1.- Filtrar por nombre de empleado")
    print("2.- Filtrar por apellido")
    print("3.- Filtrar por el salario")

def panel_admin():
    initial_menu()
    opcion = int(input("Elija una opción: "))
    if opcion == 1:
        employee_result = employee_by_name()
        if employee_result:
            print("------------------")
            for key, value in employee_result.items():
                print(f"{key}: {value}")
            print("--------------------")
            sub_menu = input("Desea editar?  Y / N : ")
            if sub_menu.upper() ==  "Y":
                edit_employee(employee_result)
                

        else:
            print("Empleado no encontrado")
    
    elif opcion == 2:
        print("Filtrando por apellido")
    elif opcion == 3:
        print("Filtrando por  salario")
    elif opcion == 0:
        return
    else:
        print ("Opcion invalida")
    continuar = input("Pulse cualquier tecla para continuar ...")
    panel_admin()
panel_admin()