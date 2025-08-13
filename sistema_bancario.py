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
    limpiar()
    while True:
        contraseña = input("Ingrese una contraseña para la cuenta: ").strip()
        if not contraseña:
            print("La contraseña no puede estar vacía.")
            continue
        else: 
            return contraseña
            
def registro_numero_contacto():
    while True:    
        limpiar()
        print('-------------------------')
        print('  1. Telefono Movil.  ')
        print('  2. Tefono Fijo. ')                                  
        print('-------------------------')
        tipo_contacto = input('Ingrese el tipo de contacto que desea registras: ')
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
            case _:
                print('El tipo de contacto no existe.')
                continue
                
                
def registrar_edad():
    limpiar()
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
    limpiar()
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
        if ('@gmail.com' in email or '@hotmail.com' in email) and len(email) > 11:
            print("Correo válido")
            return email
        else:
            print("Correo inválido") 
            continue
    
def crear_cuenta():
    #crear una nueva cuenta bancaria.
    #adjuntar valores a los datos
    cuenta_creada = {
        "nombre": registrar_nombre(),
        "edad": registrar_edad(),
        "cc": registrar_documento(),
        "email": registrar_email(),
        "numero_telefono": registro_numero_contacto(),
        "saldo": 0.0
    }

    # Guardar la cuenta en el diccionario global usando la cédula como clave
    cuentas_bancarias[cuenta_creada["cc"]] = cuenta_creada

    print("\nCuenta creada con éxito:")
    print(cuenta_creada)
    print(cuentas_bancarias)
    return cuenta_creada

def depositar_dinero():
    #solicitar cantidad deseada para agregar al salto de la cuenta
    #actualizar el valor del saldo de la cuenta
    cuenta = cuentas_bancarias[input("Ingrese su cedula: ")]
    cantidad = float(input("Ingrese la cantidad a depositar: "))
    cuenta["saldo"] += cantidad
 
# Ciclo principal del programa
while True:
    mostrar_menu_principal()
    try:
        opcion = input("Seleccione una opción: ")
        match opcion:
            case '1':
                crear_cuenta()
                print('Cuenta registrada exitosamente..') 
                input('Precione cualquier tecla para continuar..')
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