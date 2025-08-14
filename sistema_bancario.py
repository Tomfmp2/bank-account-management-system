import os

# almacena las cuentas bacarias registradas
cuentas_bancarias = {
}
# almacena las cuentas bancarias tienen algun tipo de credito
cuentas_con_credito = {
}
# Almacena las cuentas bancarias que han sido canceladas
cuentas_canceladas = {
}
# Almacena los productos por cliente
productos_cliente = {
}

def limpiar():
    # Limpia la consola dependiendo del sistema operativo.
    os.system('cls' if os.name == 'nt' else 'clear')


def precionar_continuar():
    # entrada para que el usuario pueda leer mensajes antes de ser limpiados por la siguiente seccion
    input('\nPresione cualquier tecla para continuar..')


def fecha():
    try:
        if os.name == 'nt':
            return os.popen('cmd /c echo %DATE% %TIME%').read().strip()
        else:
            return os.popen("date '+%Y-%m-%d %H:%M:%S'").read().strip()
    except Exception:
        return 'fecha'


# Helpers
def solo_letras_y_espacios(texto: str) -> bool:
    texto = texto.strip()
    if not texto:
        return False
    for c in texto:
        if not (c.isalpha() or c.isspace()):
            return False
    return True


# registro del historial
def registrar_historial(cc, id_producto, valor, tipo_mov):
    # Crea historial como diccionario: {mov_1:{...}, mov_2:{...}}
    if cc in productos_cliente and id_producto in productos_cliente[cc]:
        historial = productos_cliente[cc][id_producto].get('historial', {})
        nuevo_id = 'mov_' + str(len(historial) + 1)
        historial[nuevo_id] = {
            'id': nuevo_id,
            'fechaMov': fecha(),
            'valor': valor,
            'tipoMov': tipo_mov
        }
        productos_cliente[cc][id_producto]['historial'] = historial


# interface grafica del gestor de cuentas bancarias
def mostrar_menu_principal():
    # Muestra el menú principal de la aplicación.
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
    # Muestra el menú de tipo de cuenta bancaria.
    limpiar()
    print("----------------------------------")
    print("______Tipo De Cuenta Bancaria_____")
    print("\n1. Cuenta Bancaria Corriente")
    print("2. Cuenta Bancaria de Ahorros")
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


def registro_tipo_cuenta_bancaria():
    while True:
        menu_tipo_cuenta_bancaria()
        tipo_cuenta_elegida = input('Ingrese la opcion que desee:')
        match tipo_cuenta_elegida:
            case '1':
                return 'cuenta_corriente'
            case '2':
                return 'cuenta_ahorro'
            case '3':
                return 'CDT'
            case _:
                limpiar()
                print('El dato ingresado es invalido por favor eliga una opcion del (1 - 4).')
                precionar_continuar()
                continue


def registrar_nombre():
    limpiar()
    print('------------------------------')
    print('     DATOS PERSONALES ')
    print('------------------------------')

    while True:
        nombre = input("Ingrese el nombre del titular de la cuenta: ").strip().lower()
        if not nombre:
            print("El nombre no puede estar vacío.")
            precionar_continuar()
            continue
        else:
            return nombre


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
                numero_contacto = input('Ingresa el numero de tu telefono movil: ').strip()
                if not numero_contacto:
                    print('El numero movil no puede estar vacío.')
                    precionar_continuar()
                    continue
                if not numero_contacto.isdigit():
                    print('El numero movil solo debe tener números.')
                    precionar_continuar()
                    continue
                if len(numero_contacto) != 10:
                    print('El numero movil debe tener 10 dígitos.')
                    precionar_continuar()
                    continue
                return {'movil': numero_contacto}
            case '2':
                numero_contacto = input('Ingresa el numero de tu telefono Fijo: ').strip()
                if not numero_contacto:
                    print('El numero Fijo no puede estar vacío.')
                    precionar_continuar()
                    continue
                if not numero_contacto.isdigit():
                    print('El numero Fijo solo debe tener números.')
                    precionar_continuar()
                    continue
                if len(numero_contacto) != 8:
                    print('El numero Fijo debe tener 8 dígitos.')
                    precionar_continuar()
                    continue
                return {'fijo': numero_contacto}
            case _:
                limpiar()
                print('El dato ingresado no es una opcion valida.')
                precionar_continuar()
                continue


def registrar_edad():
    limpiar()
    while True:
        edad = input('Ingrese su edad: ').strip()
        if not edad:  # Si está vacío o solo espacios
            print('La edad no puede estar vacía.')
            precionar_continuar()
            continue
        if not edad.isdigit():  # Si no son solo números
            print('La edad debe ser un número.')
            precionar_continuar()
            continue
        else:
            return int(edad)


def registrar_documento():
    limpiar()
    while True:
        cc = input('Ingrese su numero de cedula: ').strip()
        if not cc:
            print('El numero de cedula no puede estar vacío.')
            precionar_continuar()
            continue
        if not cc.isdigit():  # Si no son solo números
            print('El numero de cedula solo debe tener numeros.')
            precionar_continuar()
            continue
        if cc in cuentas_bancarias:
            print('El numero de cedula ya existe. \n Ingrese otro numero..')
            precionar_continuar()
            continue
        else:
            return cc


def registrar_ubicacion():
    # Agregar la ubicacion del usuario
    while True:
        try:
            pais = input('Ingrese el nombre del país en el que reside: ').strip().title()
            if not solo_letras_y_espacios(pais):
                print('El país debe contener solo letras y espacios y no estar vacío.')
                precionar_continuar()
                continue
            ciudad = input('Ingrese el nombre de la ciudad en la que reside: ').strip().title()
            if not solo_letras_y_espacios(ciudad):
                print('La ciudad debe contener solo letras y espacios y no estar vacía.')
                precionar_continuar()
                continue
            direccion = input('Ingrese la dirección en la que reside: ').strip()
            if len(direccion) < 5:
                print('La dirección es demasiado corta, ingrese más detalles.')
                precionar_continuar()
                continue

            # Si todo es válido, retornar
            ubicacion = {
                "pais": pais,
                "ciudad": ciudad,
                "direccion": direccion
            }
            return ubicacion
        except KeyboardInterrupt:
            print("\nRegistro cancelado por el usuario.")
            precionar_continuar()
            continue


def registrar_email():
    # Agregar el email del usuario
    limpiar()
    while True:
        email = input('Ingrese un correo electronico: ').strip()
        if not email:
            print("El Correo no puede estar vacío")
            precionar_continuar()
            continue
        # Verificacion basica de correo electronico (sin usar re)
        if ('@' not in email) or ('.' not in email.split('@')[-1]) or (' ' in email):
            print("El Correo ingresado es inválido")
            precionar_continuar()
            continue
        print("El Correo ha sido registrado exitosamente")
        precionar_continuar()
        return email


def crear_cuenta():
    # crear una nueva cuenta bancaria.
    # adjuntar valores a los datos
    cuenta_creada = {
        "tipo_cuenta_bancaria": registro_tipo_cuenta_bancaria(),
        "nombre": registrar_nombre(),
        "edad": registrar_edad(),
        "cc": registrar_documento(),
        "email": registrar_email(),
        "numero_telefono": registro_numero_contacto(),
        "ubicacion": registrar_ubicacion(),
        "saldo": 0.0
    }

    # Guardar la cuenta en el diccionario global usando la cédula como clave
    cuentas_bancarias[cuenta_creada["cc"]] = cuenta_creada
    productos_cliente[cuenta_creada["cc"]] = {
        cuenta_creada['tipo_cuenta_bancaria']: {
            'fechaInicio': fecha(),
            'estado': 'Activo',
            'saldo': 0.0,
            'historial': {}
        }
    }
    print("Cuenta creada con exito")
    return cuenta_creada


# funcion para depositar dinero
def depositar_dinero():
    while True:
        cc = input('Ingrese su cedula: ').strip()
        if cc not in cuentas_bancarias:
            print('Cedula invalida no ha sido registrada.')
            continue
        break
    while True:
        try:
            monto = float(input('Ingrese la cantidad a depositar: ').strip())
        except ValueError:
            print('Solo se pueden ingresar numeros.')
            continue
        if monto <= 0:
            print('La cantidad debe ser mayor a 0.')
            continue
        break
    cuentas_bancarias[cc]['saldo'] += monto
    id_producto = cuentas_bancarias[cc]['tipo_cuenta_bancaria']
    if cc not in productos_cliente:
        productos_cliente[cc] = {}
    if id_producto not in productos_cliente[cc]:
        productos_cliente[cc][id_producto] = {
            'idProducto': id_producto,
            'fechaInicio': fecha(),
            'estado': 'Activo',
            'saldo': 0.0,
            'historial': {}
        }
    productos_cliente[cc][id_producto]['saldo'] += monto
    registrar_historial(cc, id_producto, monto, 'Deposito')
    print('Deposito exitoso. Saldo:', cuentas_bancarias[cc]['saldo'])


def solicitar_credito():
    salir = 's'
    while salir == 's':
        menu_tipo_credito()
        cuenta_ingresada = input("Ingrese su cedula: ").strip()
        if cuenta_ingresada not in cuentas_bancarias:
            print('cedula invalida no ha sido registrada.')
            respuesta = input('¿Desea salir? (s/n): ').strip().lower()
            while respuesta not in ('s', 'n'):
                print('Opción invalida.')
                respuesta = input('¿Desea salir? (s/n): ').strip().lower()
            if respuesta == 's':
                salir = 'n'
                break
            else:
                continue
        else:
            menu_tipo_credito()
            opcion_usuario = input('Ingrese la opcion que desee: ')
            match opcion_usuario:
                case '1':
                    id_credito = 'credito_libre_inversion'
                case '2':
                    id_credito = 'credito_vivienda'
                case '3':
                    id_credito = 'credito_compra_auto'
                case _:
                    print('El dato ingresado no es una opcion..')
                    precionar_continuar()
                    continue
            # Aquí podrías implementar la lógica para crear el crédito usando id_credito
            print(f'Crédito solicitado: {id_credito} (función pendiente de implementar)')
            precionar_continuar()
            salir = 'n'


def pagar_cuota_credito():
    salir = 's'
    while salir == 's':
        cuenta_ingresada = input("Ingrese su cedula: ").strip()
        if cuenta_ingresada not in cuentas_bancarias:
            print('cedula invalida no ha sido registrada.')
            respuesta = input('¿Desea salir? (s/n): ').strip().lower()
            while respuesta not in ('s', 'n'):
                print('Opción invalida.')
                respuesta = input('¿Desea salir? (s/n): ').strip().lower()
            if respuesta == 's':
                salir = 'n'
                break
            else:
                continue
        else:
            print('Tu saldo actual es: ', cuentas_bancarias[cuenta_ingresada]["saldo"])
            # Aquí puedes agregar la lógica para pagar la cuota del crédito
            precionar_continuar()
            salir = 'n'


# Funcion para retirar dinero
def retirar_dinero():
    seguir = 's'
    while seguir == 's':
        cuenta_ingresada = input("Ingrese su cedula: ").strip()
        if cuenta_ingresada not in cuentas_bancarias:
            print('cedula invalida no ha sido registrada.')
            while True:
                seguir = input('¿Desea salir? (s/n): ').strip().lower()
                if seguir == 's':
                    seguir = 'n'
                    break
                elif seguir == 'n':
                    break
                else:
                    print('Opción invalida.')
                    precionar_continuar()
                    continue
        else:
            print(f'EL saldo actual de la cuenta {cuenta_ingresada} es: ', cuentas_bancarias[cuenta_ingresada]['saldo'])
            if cuentas_bancarias[cuenta_ingresada]['saldo'] <= 0:
                print(f'Devido a que el saldo de la cuenta {cuenta_ingresada} es 0 no se podra hacer ningun retiro.')
                ingresar_otra_cuenta = input('Deseas ingresar otra cuenta (s/n): ').strip().lower()
                while True:
                    if ingresar_otra_cuenta == 's':
                        break
                    elif ingresar_otra_cuenta == 'n':
                        seguir = 'n'
                        break
                    else:
                        print('Opción invalida.')
                        ingresar_otra_cuenta = input('Deseas ingresar otra cuenta (s/n): ').strip().lower()
                        continue
            else:
                while True:
                    try:
                        cantidad_retirada = float(input('Ingrese la cantidad que desea retirar: ').strip())
                    except ValueError:
                        print('Solo se permiten números.')
                        continue
                    if cantidad_retirada <= 0:
                        print('La cantidad debe ser mayor a 0.')
                        continue
                    saldo_actual = cuentas_bancarias[cuenta_ingresada]['saldo']
                    if cantidad_retirada > saldo_actual:
                        print('EL Saldo de tu cuenta es insuficiente.')
                        precionar_continuar()
                        continue
                    else:
                        cuentas_bancarias[cuenta_ingresada]['saldo'] -= cantidad_retirada
                        print('Retiro exitoso')
                        print(f'Tu saldo actual es: {cuentas_bancarias[cuenta_ingresada]["saldo"]}')
                        print(f'La cantidad retirada fue: {cantidad_retirada}')
                        precionar_continuar()
                        seguir = 'n'
                        break


# funcion para cancelar cuenta
def cancelar_cuenta():
    # solicitar cedula de la cuenta a cancelar
    while True:
        cedula = input("Ingrese la cédula de la cuenta a eliminar: ").strip()
        if not cedula:
            limpiar()
            print("La cédula no puede estar vacía.")
            precionar_continuar()
            continue
        if cedula in cuentas_bancarias:
            id_cancelacion = f'cancelacion_{len(cuentas_canceladas)+1}'
            cuentas_canceladas[id_cancelacion] = cuentas_bancarias.pop(cedula)
            productos_cliente.pop(cedula, None)
            print('Cuenta cancelada')
            precionar_continuar()
            break
        else:
            limpiar()
            print("No existe una cuenta con esa cédula.")
            precionar_continuar()
            continue


# Ciclo principal del programa
while True:
    mostrar_menu_principal()
    # print(cuentas_canceladas)  # comentar para no mostrar datos internos en cada menú
    try:
        opcion = input("Seleccione una opción: ")
        match opcion:
            case '1':
                crear_cuenta()
                print('Cuenta registrada exitosamente..')
                precionar_continuar()
            case '2':
                solicitar_credito()
            case '3':
                pagar_cuota_credito()
            case '4':
                depositar_dinero()
                precionar_continuar()
            case '5':
                retirar_dinero()
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
