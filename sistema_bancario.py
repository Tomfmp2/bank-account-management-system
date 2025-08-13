import os
from email.utils import parseaddr

cuentas_bancarias = {
    
}

def limpiar ():
    #"""Limpia la consola dependiendo del sistema operativo.
    os.system('cls' if os.name == 'nt' else 'clear')

# interface gradica del gestor de cuentas bancarias

def mostrar_menu_principal():
    #Muestra el menú principal de la aplicación.
    limpiar()
    print("-----------------------------")
    print("______Sistema Bancario_____")
    print("\n1. Crear Cuenta")
    print("2. Silicitar Credito")
    print("3. Pago Cuota Credito")
    print("4. Depositar Dinero")
    print("5. Retirar Dinero")
    print("6. Cancelar Cuenta")
    print("7. Salir")
    print("-----------------------------")

def crear_cuenta(cuentas_bancarias):
    #crear una nueva cuenta bancaria.
    while True:
        try:
            while True:
                # crearr nombre y contraseña de la cuenta
                nombre = input("Ingrese el nombre del titular de la cuenta: ").strip().lower()
                if not nombre:
                    print("El nombre no puede estar vacío.")
                    continue
                break
            # verificar si la cuenta ya existe
            if nombre in cuentas_bancarias:
                print("El nombre ya está registrado. Por favor, elija otro nombre.")
                continue
            # Usuario ingresa la contraseña a crear 

            while True:
                contraseña = input("Ingrese una contraseña para la cuenta: ").strip()
                if not contraseña:
                    raise ValueError("La contraseña no puede estar vacía.")
                    continue
                else: 
                    break
            limpiar()
            print('------------------------------')
            print('     DATOS PERSONALES ')
            print('------------------------------')
            
            while True:
                edad = input('Ingrese su edad: ')
                if not edad.strip():  # Si está vacío o solo espacios
                    print('La edad no puede estar vacía.')
                    continue
                if not edad.isdigit():  # Si no son solo números
                    print('La edad debe ser un número.')
                    continue
                else:
                    break
            while True:
                limpiar()
                print('-------------------------')
                print('  1. Tefono Fijo.')
                print('  2. Telefono Movil.')
                print('-------------------------')
                tipo_contacto = input('Ingrese el tipo de contacto que desea registras: ')
                match tipo_contacto:
                    case '1':
                        numero_movil = int(input('Ingresa el numero de tu telefono movil: '))
                        if not numero_movil.strip():  # Si está vacío o solo espacios
                            print('El numero movil no puede estar vacío.')
                            continue
                        if not numero_movil.isdigit():  # Si no son solo números
                            print('El numero movil solo debe tener números.')
                            continue
                    case '2':
                        numero_fijo = int(input('Ingresa el numero de tu telefono Fijo: '))
                        if not numero_movil.strip():  # Si está vacío o solo espacios
                            print('El numero Fijo no puede estar vacío.')
                            continue
                        if not numero_movil.isdigit():  # Si no son solo números
                            print('El numero Fijo solo debe tener números.')
                            continue
                    case '3':
                        numero_movil = int(input('Ingresa el numero de tu telefono movil: '))
                        if not numero_movil.strip():  # Si está vacío o solo espacios
                            print('El numero movil no puede estar vacío.')
                            continue
                        if not numero_movil.isdigit():  # Si no son solo números
                            print('El numero movil solo debe tener números.')
                            continue
                        numero_fijo = int(input('Ingresa el numero de tu telefono Fijo: '))
                        if not numero_movil.strip():  # Si está vacío o solo espacios
                            print('El numero Fijo no puede estar vacío.')
                            continue
                        if not numero_movil.isdigit():  # Si no son solo números
                            print('El numero Fijo solo debe tener números.')
                            continue
                    case _:
                        pass
            while True:
                email = input('Ingrese un correo electronico: ')
                # Verificacion de correo electronico 
                if "@" in parseaddr(email)[1]:
                    print("Correo válido")
                    break
                else:
                    print("Correo inválido") 
                    continue
            
            # crear y adjuntar valores
            """
            datos = {'nombre','edad','email','cc','movil','fijo'}
            valores = {nombre,}
            print('La cuenta registrada con nombre: ',)
            """
            # Crear otra cuenta si el usuario lo desea
            crear_otra_cuenta = input('¿Desea crear otra cuenta? (s/n): ').strip().lower()
            if crear_otra_cuenta != 's':
                break       
        except ValueError as e:
            print(f'Error: {e}, por favor solo ingresar letras.') 
            continue



# Ciclo principal del programa
while True:
    mostrar_menu_principal()
    try:
        opcion = input("Seleccione una opción: ")
        match opcion:
            case '1':
                crear_cuenta(cuentas_bancarias)
            case '2':
                pass
            case '3':
                pass
            case '4':
                pass
            case '5':
                pass
            case '6':
                pass
            case '7':
                print('Saliendo del sistem...')
                break
            case _:
                print('Opción no válida. Por favor, intente de nuevo.')
                continue
    except ValueError:
            print('Error: Entrada inválida. Por favor, ingrese un número del 1 al 5.')
            continue