import os

# almacena las cuentas bacarias registradas
cuentas_bancarias = {
# almacen a las cuentas bancarias tienen algun tipo de credito
}
cuentas_con_credito = {

}
  
def limpiar ():
    #"""Limpia la consola dependiendo del sistema operativo.
    os.system('cls' if os.name == 'nt' else 'clear')
def precionar_continuar():
    # entrada para que el usuario pueda leer mensajes antes de ser limpiados por la siquiente seccion
    input('Precione cualquier tecla para continuar..')
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
def menu_tipo_cuenta_bancaria():
    #Muestra el menú de tipo de cuenta bancaria.
    limpiar()
    print("----------------------------------")
    print("______Tipo De Cuenta Bancaria_____")
    print("\n1. Cuenta de Corriente")
    print("2. Cuenta de Ahorros")
    print("3. CDT")
    print("4. Salir")
    print("----------------------------------")

def menu_tipo_credito():
    limpiar()
    print("----------------------------------")
    print("______Tipo De Cuenta Bancaria_____")
    print("\n1. Credito Libre Inversion")
    print("2. Credito Vivienda")
    print("3. Credito Compra Auto Movil")
    print("4. Salir")
    print("----------------------------------")    

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
                elif not numero_contacto.isdigit():  # Si no son solo números
                    print('El numero movil solo debe tener números.')
                    continue
                elif len(numero_contacto) != 10:  # Si no tiene 10 dígitos
                    print('El numero movil debe tener 10 dígitos.')
                    continue
                else:
                    return numero_contacto
            case '2':
                numero_contacto = input('Ingresa el numero de tu telefono Fijo: ')
                if not numero_contacto.strip():  # Si está vacío o solo espacios
                    print('El numero Fijo no puede estar vacío.')
                    continue
                elif not numero_contacto.isdigit():  # Si no son solo números
                    print('El numero Fijo solo debe tener números.')
                    continue
                elif len(numero_contacto) != 8:  # Si no tiene 8 dígit
                    print('El numero Fijo debe tener 8 dígitos.')
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
        if cc in cuentas_bancarias:
            print('El numero de cedula ya existe. \n Ingrese otro numero..')
            continue
        else:
            return cc
            
def registrar_ubicacion():
    #Agregar la ubicacion del usuario
    while True:
        try:
            pais = input('Ingrese el nombre del pais en el que reside: ')
            if pais == '':
                print('El pais no puede estar vacio.')
                continue
            ciudad = input('Ingrese el nombre de la ciudad en la que reside: ')
            direccion = input('Ingrese la direccion en la que reside: ')
        except ValueError:
            print('Error al ingresar la ubicacion. (Solo se pueden usar letras al ingresar el pais, ciudad y departamento.)')
            precionar_continuar()
            continue
        ubicacion = {
            "pais": pais,
            "ciudad": ciudad,
            "direcccion": direccion
        }
        return ubicacion

def registrar_email():
    #Agregar el email del usuario
    limpiar()
    while True:
        email = input('Ingrese un correo electronico: ')
        # Verificacion de correo electronico 
        if ('@gmail.com' in email or '@hotmail.com' in email) and len(email) > 11:
            print("El Correo ha sido registrado exitosamente")
            precionar_continuar()
            return email
        else:
            print("El Correo ingresado es inválido") 
            precionar_continuar()
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
        "saldo": 0.0,
        "contraseña": registrar_contraseña()
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
    salir = 's'
    while salir == 's':
        cuenta_ingresada = input("Ingrese su cedula: ")
        if cuenta_ingresada not in cuentas_bancarias:
            print('cedula invalida no ha sido registrada.')
            salir = input('¿Desea salir? (s/n): ')
            while True:
                if salir.lower() == 's':
                    salir = 'n'
                    break
                elif salir.lower() == 'n':
                    continue
                else:
                    print('Opción invalida.')
                    continue
        elif cuenta_ingresada in cuentas_bancarias:
            cantidad_depositada = float(input("Ingrese la cantidad a depositar: "))
            cuentas_bancarias[cuenta_ingresada]["saldo"] += cantidad_depositada
            print('saldo registrado con exito.')
            print('El saldo actual de tu cuentas es: ', cuentas_bancarias[cuenta_ingresada]["saldo"])
            salir = 'n'
        else:
            print('Solo se pueden ingresar numeros.')
            precionar_continuar()
            continue
def retirar_dinero():
    salir = 's'
    while salir == 's':
        cuenta_ingresada = input("Ingrese su cedula: ")
        if cuenta_ingresada not in cuentas_bancarias:
            print('cedula invalida no ha sido registrada.')
            salir = input('¿Desea salir? (s/n): ')
            while True:
                if salir.lower() == 's':
                    salir = 'n'
                    break
                elif salir.lower() == 'n':
                    continue
                else:
                    print('Opción invalida.')
                    continue
        

def solicitar_credito():
    salir = 's'
    while salir == 's':
        cuenta_ingresada = input("Ingrese su cedula: ")
        if cuenta_ingresada not in cuentas_bancarias:
            print('cedula invalida no ha sido registrada.')
            salir = input('¿Desea salir? (s/n): ')
            while True:
                if salir.lower() == 's':
                    salir = 'n'
                    break
                elif salir.lower() == 'n':
                    continue
                else:
                    print('Opción invalida.')
                    continue
        elif cuenta_ingresada in cuentas_bancarias:
            pass
            
def pagar_cuota_credito():
    salir = 's'
    while salir == 's':
        cuenta_ingresada = input("Ingrese su cedula: ")
        if cuenta_ingresada not in cuentas_bancarias:
            print('cedula invalida no ha sido registrada.')
            salir = input('¿Desea salir? (s/n): ')
            while True:
                if salir.lower() == 's':
                    salir = 'n'
                    break
                elif salir.lower() == 'n':
                    continue
                else:
                    print('Opción invalida.')
                    continue
        elif cuenta_ingresada in cuentas_bancarias:
            print('Tu saldo actual es: ', cuentas_bancarias[cuenta_ingresada]["saldo"])
            
def cancelar_cuenta():
     #solicitar cedula de la cuenta a cancelar
    while True:
        cedula = input("Ingrese la cédula de la cuenta a eliminar: ")
        if cedula in cuentas_bancarias:
            del cuentas_bancarias[cedula]
            print("Cuenta eliminada correctamente.")
            precionar_continuar()
            break
        else:
            print("No existe una cuenta con esa cédula.")
            precionar_continuar()
            continue

# Ciclo principal del programa
while True:
    mostrar_menu_principal()
    try:
        opcion = input("Seleccione una opción: ")
        match opcion:
            case '1':
                menu_tipo_cuenta_bancaria()
                crear_cuenta()
                print('Cuenta registrada exitosamente..') 
                precionar_continuar()
            case '2':
                menu_tipo_credito()
            case '3':
                pass
            case '4':
                depositar_dinero()
                precionar_continuar()
                
            case '5':
                pass
            case '6':
                cancelar_cuenta()
            case '7':
                print('Saliendo del sistema...')
                break
            case _:
                limpiar()
                print('Opción no válida. Por favor, intente de nuevo.')
                precionar_continuar()
    except ValueError:
            print('Error: Entrada inválida. Por favor, ingrese un número del 1 al 7.')
            precionar_continuar()
            continue