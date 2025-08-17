import os
from modules.tools import limpiar, precionar_continuar
from modules.menus import mostrar_menu_principal, menu_tipo_credito, menu_tipo_cuenta_bancaria
from modules.corefiles import crear_archivo_json, registrar_datos, read_json, write_json, CUENTAS_BANCARIAS, CUENTAS_CANCELADAS

# Cargar datos al inicio
cuentas_bancarias = {}
productos_cliente = {}
cuentas_canceladas = {}

def cargar_datos():
    """Carga los datos desde JSON al inicio del programa"""
    global cuentas_bancarias, productos_cliente
    
    datos_json = read_json(CUENTAS_BANCARIAS)
    if isinstance(datos_json, dict):
        for cc, datos_completos in datos_json.items():
            if isinstance(datos_completos, dict) and 'usuario' in datos_completos:
                # Estructura unificada
                cuentas_bancarias[cc] = datos_completos['usuario']
                productos_cliente[cc] = datos_completos.get('productos', {})
            else:
                # Estructura antigua - mantener compatibilidad
                cuentas_bancarias[cc] = datos_completos

def guardar_datos():
    """Guarda todos los datos actualizados en JSON"""
    datos_para_guardar = {}
    for cc in cuentas_bancarias:
        datos_para_guardar[cc] = {
            'usuario': cuentas_bancarias[cc],
            'productos': productos_cliente.get(cc, {})
        }
    write_json(CUENTAS_BANCARIAS, datos_para_guardar)

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
    """Crea historial como diccionario y guarda en JSON"""
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
        # Guardar cambios en JSON
        guardar_datos()

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
            case '4':
                return None  # Opción salir
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
        nombre = input("Ingrese el nombre del titular de la cuenta: ").strip().title()
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
                    print('\nEl numero movil no puede estar vacío.')
                    precionar_continuar()
                    continue
                if not numero_contacto.isdigit():
                    print('\nEl numero movil solo debe tener números.')
                    precionar_continuar()
                    continue
                if len(numero_contacto) != 10:
                    print('\nEl numero movil debe tener 10 dígitos.')
                    precionar_continuar()
                    continue
                return {'movil': numero_contacto}
            case '2':
                numero_contacto = input('Ingresa el numero de tu telefono Fijo: ').strip()
                if not numero_contacto:
                    print('\nEl numero Fijo no puede estar vacío.')
                    precionar_continuar()
                    continue
                if not numero_contacto.isdigit():
                    print('\nEl numero Fijo solo debe tener números.')
                    precionar_continuar()
                    continue
                if len(numero_contacto) != 8:
                    print('\nEl numero Fijo debe tener 8 dígitos.')
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
        try:
            edad_input = input('Ingrese su edad: ').strip()
            if not edad_input:  # Si está vacío o solo espacios
                limpiar()
                print('La edad no puede estar vacía.')
                precionar_continuar()
                continue
            edad = int(edad_input)
            if edad < 18:
                limpiar()
                print('La cuenta no puede ser creada por un menor de edad.')
                precionar_continuar()
                continue
            else:
                return edad
        except ValueError:
            print('El dato ingresado no es un número, vuelva a intentar.')
            precionar_continuar()
            continue

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
        limpiar()
        try:
            pais = input('Ingrese el nombre del país en el que reside: ').strip().title()
            if not solo_letras_y_espacios(pais):
                print('El país debe contener solo letras y espacios y no estar vacío.')
                precionar_continuar()
                continue
            ciudad = input('\nIngrese el nombre de la ciudad en la que reside: ').strip().title()
            if not solo_letras_y_espacios(ciudad):
                print('La ciudad debe contener solo letras y espacios y no estar vacía.')
                precionar_continuar()
                continue
            direccion = str(input('\nIngrese la dirección en la que reside: ')).strip()
            if len(direccion) < 5:
                print('La dirección es demasiado corta, ingrese más detalles.')
                precionar_continuar()
                continue
            else:
                # Si todo es válido, retornar
                ubicacion = {
                    "pais": pais,
                    "ciudad": ciudad,
                    "direccion": direccion
                }
                return ubicacion
        except KeyboardInterrupt:
            print("\nRegistro cancelado por dato invalido ingresado.")
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

def data_cuenta():
    global cuentas_bancarias, productos_cliente

    tipo_cuenta = registro_tipo_cuenta_bancaria()
    if tipo_cuenta is None:  # Usuario eligió salir
        return None

    cuenta_creada = {
        "tipo_cuenta_bancaria": tipo_cuenta,
        "nombre": registrar_nombre(),
        "edad": registrar_edad(),
        "cc": registrar_documento(),
        "email": registrar_email(),
        "numero_telefono": registro_numero_contacto(),
        "ubicacion": registrar_ubicacion(),
        "saldo": 0.0
    }

    # Producto inicial
    producto = {
        cuenta_creada['tipo_cuenta_bancaria']: {
            "fechaInicio": fecha(),
            "estado": "Activo",
            "saldo": 0.0,
            "historial": {}
        }
    }

    # Guardar en memoria
    cuentas_bancarias[cuenta_creada["cc"]] = cuenta_creada
    productos_cliente[cuenta_creada["cc"]] = producto

    # Guardar en JSON
    guardar_datos()

    print("Cuenta creada con éxito y guardada en cuentas_registradas.json")
    return {
        "usuario": cuenta_creada,
        "productos": producto
    }

# funcion para depositar dinero
def depositar_dinero():
    global cuentas_bancarias, productos_cliente

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
    
    # Actualizar saldo del usuario
    cuentas_bancarias[cc]['saldo'] += monto
    
    # Actualizar producto
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
    
    # Registrar en historial
    registrar_historial(cc, id_producto, monto, 'Deposito')
    
    print('Deposito exitoso. Saldo:', cuentas_bancarias[cc]['saldo'])

def solicitar_credito():
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
            menu_tipo_credito()
            opcion_usuario = input('Ingrese la opcion que desee: ')
            match opcion_usuario:
                case '1':
                    id_credito = 'credito_libre_inversion'
                case '2':
                    id_credito = 'credito_vivienda'
                case '3':
                    id_credito = 'credito_compra_auto'
                case '4':
                    salir = 'n'
                    break
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
        if cuentas_bancarias[cuenta_ingresada]["saldo"] <= 0:
            print('Tu saldo actual es: ', cuentas_bancarias[cuenta_ingresada]["saldo"])
            print('no puedes pagar ninguna cuenta.')
            precionar_continuar()
            break
        else:
            print('Actualmente tu cuenta esta registrada como: ', cuentas_bancarias[cuenta_ingresada]["tipo_cuenta_bancaria"])
            print('Función de pago de cuota pendiente de implementar.')
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
                print(f'Debido a que el saldo de la cuenta {cuenta_ingresada} es 0 no se podra hacer ningun retiro.')
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
                        # Actualizar saldo
                        cuentas_bancarias[cuenta_ingresada]['saldo'] -= cantidad_retirada
                        
                        # Actualizar producto
                        id_producto = cuentas_bancarias[cuenta_ingresada]['tipo_cuenta_bancaria']
                        if cc in productos_cliente and id_producto in productos_cliente[cuenta_ingresada]:
                            productos_cliente[cuenta_ingresada][id_producto]['saldo'] -= cantidad_retirada
                        
                        # Registrar en historial
                        registrar_historial(cuenta_ingresada, id_producto, cantidad_retirada, 'Retiro')
                        
                        print('Retiro exitoso')
                        print(f'Tu saldo actual es: {cuentas_bancarias[cuenta_ingresada]["saldo"]}')
                        print(f'La cantidad retirada fue: {cantidad_retirada}')
                        precionar_continuar()
                        seguir = 'n'
                        break

# funcion para cancelar cuenta
def cancelar_cuenta():
    global cuentas_bancarias, productos_cliente, cuentas_canceladas
    while True:
        cedula = input("Ingrese la cédula de la cuenta a eliminar: ").strip()
        if not cedula:
            limpiar()
            print("La cédula no puede estar vacía.")
            precionar_continuar()
            continue

        if cedula in cuentas_bancarias:
            # Recuperar datos del usuario
            datos_usuario = cuentas_bancarias.pop(cedula)

            # Recuperar productos asociados (si existen)
            datos_producto = productos_cliente.pop(cedula, {})

            # Unir la info en un solo diccionario
            datos_completos = {
                "usuario": datos_usuario,
                "productos": datos_producto
            }

            # Guardar también en el diccionario en memoria
            id_cancelacion = f'cancelacion_{len(cuentas_canceladas)+1}'
            cuentas_canceladas[id_cancelacion] = datos_completos

            # Persistir en JSON de cuentas canceladas
            crear_archivo_json(CUENTAS_CANCELADAS, {})
            registrar_datos(CUENTAS_CANCELADAS, {id_cancelacion: datos_completos})

            # Actualizar JSON principal
            guardar_datos()

            print('Cuenta cancelada y registrada en cuentas_canceladas.json')
            precionar_continuar()
            break
        else:
            limpiar()
            print("No existe una cuenta con esa cédula.")
            precionar_continuar()
            continue

def main():
    # Cargar datos al inicio
    cargar_datos()
    
    # Ciclo principal del programa
    while True:
        mostrar_menu_principal()
        try:
            opcion = input("Seleccione una opción: ")
            match opcion:
                case '1':
                    resultado = data_cuenta()
                    if resultado:
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
        except KeyboardInterrupt:
            print('\n\nSaliendo del sistema...')
            break