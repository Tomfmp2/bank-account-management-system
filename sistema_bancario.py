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
def  registrar_nombre():
    limpiar()
    print('------------------------------')
    print('     DATOS PERSONALES ')
    print('------------------------------')
            
    while True:
            # crearr nombre y contraseña de la cuenta
            nombre = input("Ingrese el nombre del titular de la cuenta: ").strip().lower()
            if not nombre:
                print("El nombre no puede estar vacío.")
                continue
            else:
                return nombre        
def registrar_contraseña():
    # Usuario ingresa la contraseña a crear             
    while True:
        contraseña = input("Ingrese una contraseña para la cuenta: ").strip()
        if not contraseña:
            print("La contraseña no puede estar vacía.")
            continue
        else: 
            return contraseña
            
def registro_numero_contacto():
    limpiar()
    print('-------------------------')
    print('  1. Telefono Movil.  ')
    print('  2. Tefono Fijo.     ')                                  
    print('-------------------------')
    tipo_contacto = input('Ingrese el tipo de contacto que desea registras: ')
    while True:
        match tipo_contacto:
            case '1':
                numero_contacto = input('Ingresa el numero de tu telefono movil: ')
                if not numero_contacto.strip():  # Si está vacío o solo espacios
                    print('El numero movil o puede estar vacío.')
                    continue
                if not numero_contacto.isdigit():  # Si no son solo números
                    print('El numero movil solo debe tener números.')
                    continue
                else:
                    return numero_contacto
            case '2':
                numero_contacto = input('Ingresa el numero de tu telefono Fijo: ')
                if not numero_contacto.strip():  # Si está vacío o solo espacios
                    print('El numero Fijo no puede estar vacío.')
                    continue
                if not numero_contacto.isdigit():  # Si no son solo números
                    print('El numero Fijo solo debe tener números.')
                    continue
                else:
                    return numero_contacto
                
                
def registrar_edad():
    while True:
        edad = input('Ingrese su edad: ')
        if not edad.strip():  # Si está vacío o solo espacios
            print('La edad no puede estar vacía.')
            continue
        if not edad.isdigit():  # Si no son solo números
            print('La edad debe ser un número.')
            continue
        else:
            return edad
            
def registrar_documento():
    while True:
        cc = input('Ingrese su numero de cedula: ').strip()
        if not cc.isdigit():  # Si no son solo números
            print('El numero de cedula solo debe tener numeros. ')
        else:
            return cc
            
def registrar_ubicacion():
    pass
def registrar_email():
    while True:
        email = input('Ingrese un correo electronico: ')
        # Verificacion de correo electronico 
        if '@gmail.com'or '@hotmail.com' in email and len(email) > 11:
            print("Correo válido")
            return email
        else:
            print("Correo inválido") 
            continue
    
def crear_cuenta():
    nombre = registrar_nombre()
    edad = registrar_edad()
    documento = registrar_documento()
    email = registrar_email()
    numero_contacto = registro_numero_contacto()
    #crear una nueva cuenta bancaria.
    #adjuntar valores a los datos
    datos = {'nombre','edad','email','cc','movil','fijo'}
    valores = {nombre,edad,email,documento,numero_contacto}
    cuenta_creada = dict(zip(datos,valores))
    print(cuenta_creada)
    return cuenta_creada


# Ciclo principal del programa
while True:
    mostrar_menu_principal()
    try:
        opcion = input("Seleccione una opción: ")
        match opcion:
            case '1':
                crear_otra_cuenta = 's'
                while crear_otra_cuenta == 's':
                        registrar_nombre()
                        registrar_documento()
                        registrar_edad()
                        registrar_email()
                        registro_numero_contacto()
                        crear_cuenta()
                        crear_mas_cuentas = input('¿Desea crear otra cuenta?: ').lower()
                        if crear_mas_cuentas == 's':
                            print('okey...')
                        elif crear_mas_cuentas == 'n':
                            break
                        else:
                            print('el dato ingresado no es correcto')
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