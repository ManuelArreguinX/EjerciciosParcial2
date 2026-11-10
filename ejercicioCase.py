name = []
lastname = []
age = []
birthday = []
email = []
password = []
confirmpass = []
option = 0

while True:
print("Bienvenido al sistema de registro de usuarios.")
print("1. Registrar usuario")
print("2. Ver información del usuario")
print("3. Borrar información del usuario")
print("4. Modificar información del usuario")
print("5. Salir")
option = int(input("Selecciona una opción: "))
match option:
    case 1:
        name.append = input("Ingresa tu nombre: ")
        lastname.append = input("Ingresa tu apellido: ")
        age.append = int(input("Ingresa tu edad: "))
        birthday.append = input("Ingresa tu fecha de nacimiento (dd/mm/aaaa): ")
        email.append = input("Ingresa tu correo electrónico: ")
        password.append = input("Ingresa tu contraseña: ")
        confirmpass.append = input("Confirma tu contraseña: ")
    case 2:
        print("Nombre:", name, "Edad:", age, "Fecha de nacimiento:", birthday, "Correo electrónico:", email, "Contraseña:", password)
    case 3:
        name = ""
        lastName = ""
        age = 0
        birthday = ""
        email = ""
        password = ""
    case 4:
        name = input("Ingresa tu nombre: ")
        lastName = input("Ingresa tu apellido: ")
        age = int(input("Ingresa tu edad: "))
        birthday = input("Ingresa tu fecha de nacimiento: ")
        email = input("Ingresa tu correo electrónico: ")
        password = input("Ingresa tu contraseña: ")
    case 5:
        print("¡Hasta luego!")
        break
    case _:
        print("Opción no válida")