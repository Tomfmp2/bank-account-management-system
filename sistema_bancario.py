import os

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
            # crearr nombre y contraseña de la cuenta
            nombre = input("Ingrese el nombre del titular de la cuenta: ").strip().lower()
            if not nombre:
                raise ValueError("El nombre no puede estar vacío.")
            
            # verificar si la cuenta ya existe
            if nombre in cuentas_bancarias:
                print("El nombre ya está registrado. Por favor, elija otro nombre.")
                continue
            contraseña = input("Ingrese una contraseña para la cuenta: ").strip()
            if not contraseña:
                raise ValueError("La contraseña no puede estar vacía.")
            
            # crear y adjuntar valores
            """
            datos = {'nombre','edad','email','cc','movil','fijo'}
            valores = {nombre,}
            print('La cuenta registrada con nombre: ',)
            """
            # Crear otra cuenta si el usuario lo desea
            crear_otra_cuenta = input("¿Desea crear otra cuenta? (s/n): ").strip().lower()
            crear_otra_cuenta = input("¿Desea crear otra cuenta? (s/n): ").strip().lower()
            if crear_otra_cuenta != 's':
                break

        except ValueError as e:
            print(f"Error: {e}, por favor solo ingresar letras.")
            continue

mostrar_menu_principal()

# Ciclo principal del programa
while True:
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
                    print('Saliendo del sistem')
                case _:
                    print('Opción no válida. Por favor, intente de nuevo.')
        except ValueError:
                print('Error: Entrada inválida. Por favor, ingrese un número del 1 al 5.')