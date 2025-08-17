import os
from modules.tools import limpiar, precionar_continuar
from modules.menus import mostrar_menu_principal, menu_tipo_credito, menu_tipo_cuenta_bancaria
from modules.corefiles import crear_archivo_json, registrar_datos, read_json, write_json, CUENTAS_BANCARIAS, CUENTAS_CANCELADAS

# Variables globales para almacenamiento de datos
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
                if cc not in productos_cliente:
                    productos_cliente[cc] = {}

def guardar_datos():
    """Guarda todos los datos en el archivo JSON"""
    datos_para_guardar = {}
    for cc in cuentas_bancarias:
        datos_para_guardar[cc] = {
            'usuario': cuentas_bancarias[cc],
            'productos': productos_cliente.get(cc, {})
        }
    write_json(CUENTAS_BANCARIAS, datos_para_guardar)

def fecha():
    """Obtiene fecha y hora actual del sistema"""
    try:
        if os.name == 'nt':
            return os.popen('cmd /c echo %DATE% %TIME%').read().strip()
        else:
            return os.popen("date '+%Y-%m-%d %H:%M:%S'").read().strip()
    except Exception:
        return 'fecha'

def solo_letras_y_espacios(texto: str) -> bool:
    """Valida que el texto contenga solo letras, espacios y caracteres especiales comunes"""
    texto = texto.strip()
    if not texto:
        return False
    caracteres_validos = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZáéíóúÁÉÍÓÚñÑüÜ "
    return all(c in caracteres_validos for c in texto)

def registrar_historial(cc, id_producto, valor, tipo_mov):
    """Registra movimiento en el historial del producto"""
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
        guardar_datos()

def sincronizar_saldos(cc):
    """Sincroniza el saldo general con la suma de saldos de productos"""
    if cc not in cuentas_bancarias or cc not in productos_cliente:
        return
    
    saldo_total = 0
    for producto_id, datos in productos_cliente[cc].items():
        if not producto_id.startswith(('credito_libre_inversion', 'credito_vivienda', 'credito_compra_auto')):
            saldo_total += datos.get('saldo', 0)
    
    cuentas_bancarias[cc]['saldo'] = saldo_total

def registro_tipo_cuenta_bancaria():
    """Maneja la selección del tipo de cuenta bancaria"""
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
                return None
            case _:
                limpiar()
                print('El dato ingresado es invalido por favor eliga una opcion del (1 - 4).')
                precionar_continuar()
                continue

def registrar_nombre():
    """Captura y valida el nombre del titular"""
    limpiar()
    print('------------------------------')
    print('     DATOS PERSONALES ')
    print('------------------------------')

    while True:
        nombre = input("Ingrese el nombre del titular de la cuenta: ").strip().title()
        if not nombre:
            print("El nombre no puede estar vacio.")
            precionar_continuar()
            continue
        if not solo_letras_y_espacios(nombre):
            print("El nombre solo puede contener letras, espacios y acentos.")
            precionar_continuar()
            continue
        return nombre

def registro_numero_contacto():
    """Captura y valida número de contacto"""
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
                    print('\nEl numero movil no puede estar vacio.')
                    precionar_continuar()
                    continue
                if not numero_contacto.isdigit():
                    print('\nEl numero movil solo debe tener numeros.')
                    precionar_continuar()
                    continue
                if len(numero_contacto) != 10:
                    print('\nEl numero movil debe tener 10 digitos.')
                    precionar_continuar()
                    continue
                return {'movil': numero_contacto}
            case '2':
                numero_contacto = input('Ingresa el numero de tu telefono Fijo: ').strip()
                if not numero_contacto:
                    print('\nEl numero Fijo no puede estar vacio.')
                    precionar_continuar()
                    continue
                if not numero_contacto.isdigit():
                    print('\nEl numero Fijo solo debe tener numeros.')
                    precionar_continuar()
                    continue
                if len(numero_contacto) != 8:
                    print('\nEl numero Fijo debe tener 8 digitos.')
                    precionar_continuar()
                    continue
                return {'fijo': numero_contacto}
            case _:
                limpiar()
                print('El dato ingresado no es una opcion valida.')
                precionar_continuar()
                continue

def registrar_edad():
    """Captura y valida la edad del usuario"""
    limpiar()
    while True:
        try:
            edad_input = input('Ingrese su edad: ').strip()
            if not edad_input:
                limpiar()
                print('La edad no puede estar vacia.')
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
            print('El dato ingresado no es un numero, vuelva a intentar.')
            precionar_continuar()
            continue

def registrar_documento():
    """Captura y valida el número de cédula"""
    limpiar()
    while True:
        cc = input('Ingrese su numero de cedula: ').strip()
        if not cc:
            print('El numero de cedula no puede estar vacio.')
            precionar_continuar()
            continue
        if not cc.isdigit():
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
    """Captura y valida la información de ubicación"""
    while True:
        limpiar()
        try:
            pais = input('Ingrese el nombre del pais en el que reside: ').strip().title()
            if not solo_letras_y_espacios(pais):
                print('El pais debe contener solo letras y espacios y no estar vacio.')
                precionar_continuar()
                continue
            ciudad = input('\nIngrese el nombre de la ciudad en la que reside: ').strip().title()
            if not solo_letras_y_espacios(ciudad):
                print('La ciudad debe contener solo letras y espacios y no estar vacia.')
                precionar_continuar()
                continue
            direccion = str(input('\nIngrese la direccion en la que reside: ')).strip()
            if len(direccion) < 5:
                print('La direccion es demasiado corta, ingrese mas detalles.')
                precionar_continuar()
                continue
            else:
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
    """Captura y valida el email del usuario"""
    limpiar()
    while True:
        email = input('Ingrese un correo electronico: ').strip()
        if not email:
            print("El Correo no puede estar vacio")
            precionar_continuar()
            continue
        if ('@' not in email) or ('.' not in email.split('@')[-1]) or (' ' in email):
            print("El Correo ingresado es invalido")
            precionar_continuar()
            continue
        print("El Correo ha sido registrado exitosamente")
        precionar_continuar()
        return email

def data_cuenta():
    """Proceso principal de creación de cuenta"""
    global cuentas_bancarias, productos_cliente

    tipo_cuenta = registro_tipo_cuenta_bancaria()
    if tipo_cuenta is None:
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

    print("Cuenta creada con exito y guardada en cuentas_registradas.json")
    return {
        "usuario": cuenta_creada,
        "productos": producto
    }

def depositar_dinero():
    """Proceso de depósito de dinero"""
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
    
    # Sincronizar saldo general
    sincronizar_saldos(cc)
    
    # Registrar en historial
    registrar_historial(cc, id_producto, monto, 'Deposito')
    
    print('Deposito exitoso. Saldo:', cuentas_bancarias[cc]['saldo'])

def registro_datos_solicitud_credito(cc, tipo_credito):
    """Registra datos para solicitud de crédito"""
    
    # Solicitar monto del crédito
    while True:
        try:
            monto_credito = float(input('Ingrese monto solicitado: $'))
            if monto_credito <= 0:
                print('El monto debe ser mayor a cero')
                continue
            break
        except ValueError:
            print('Ingrese un monto valido')
            continue
    
    # Generar referencia única del crédito
    if cc not in productos_cliente:
        productos_cliente[cc] = {}
    
    # Contar créditos existentes del mismo tipo
    creditos_existentes = [
        k for k in productos_cliente[cc].keys() 
        if k.startswith(tipo_credito)
    ]
    numero_credito = len(creditos_existentes) + 1
    referencia_credito = f"{tipo_credito}_{numero_credito}"
    
    # Crear estructura del crédito
    credito = {
        referencia_credito: {
            'tipo_credito': tipo_credito,
            'fecha': fecha(),
            'evento': 'Solicitud_Creada',
            'monto': monto_credito,
            'historial': {}
        }
    }
    
    # Agregar el crédito a productos_cliente
    productos_cliente[cc].update(credito)
    
    # Guardar en JSON
    guardar_datos()
    
    return referencia_credito

def solicitar_credito():
    """Proceso principal de solicitud de crédito"""
    salir = 's'
    while salir == 's':
        cuenta_ingresada = input("Ingrese su cedula: ").strip()
        if cuenta_ingresada not in cuentas_bancarias:
            print('cedula invalida no ha sido registrada.')
            respuesta = input('¿Desea salir? (s/n): ').strip().lower()
            while respuesta not in ('s', 'n'):
                print('Opcion invalida.')
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
                    tipo_credito = 'credito_libre_inversion'
                    referencia = registro_datos_solicitud_credito(cuenta_ingresada, tipo_credito)
                    print(f'Credito solicitado con referencia: {referencia}')
                case '2':
                    tipo_credito = 'credito_vivienda'
                    referencia = registro_datos_solicitud_credito(cuenta_ingresada, tipo_credito)
                    print(f'Credito solicitado con referencia: {referencia}')
                case '3':
                    tipo_credito = 'credito_compra_auto'
                    referencia = registro_datos_solicitud_credito(cuenta_ingresada, tipo_credito)
                    print(f'Credito solicitado con referencia: {referencia}')
                case '4':
                    salir = 'n'
                    break
                case _:
                    print('El dato ingresado no es una opcion..')
                    precionar_continuar()
                    continue
            
            precionar_continuar()
            salir = 'n'

def obtener_creditos_activos(cc):
    """Obtiene lista de créditos activos para pago de cuotas"""
    creditos_activos = []
    
    if cc in productos_cliente:
        for producto_id, datos in productos_cliente[cc].items():
            if producto_id.startswith(('credito_libre_inversion', 'credito_vivienda', 'credito_compra_auto')):
                # Verificar si es un crédito activo (aprobado y con saldo pendiente)
                if 'cuota_mensual' in datos and datos.get('saldo_pendiente', 0) > 0:
                    # Agregar identificador único para facilitar búsqueda posterior
                    datos_con_id = datos.copy()
                    datos_con_id['producto_id'] = producto_id
                    creditos_activos.append(datos_con_id)
    
    return creditos_activos

def aprobar_credito_automaticamente(cc, producto_id, datos):
    """Aprueba un crédito automáticamente para facilitar pagos"""
    if 'monto' in datos and 'cuota_mensual' not in datos:
        monto = datos['monto']
        cuotas = 12  # Número de cuotas por defecto
        
        # Agregar campos necesarios para la aprobación
        datos.update({
            'evento': 'Aprobado',
            'monto_original': monto,
            'saldo_pendiente': monto,
            'cuota_mensual': monto / cuotas,
            'cuotas_restantes': cuotas,
            'fecha_aprobacion': fecha()
        })
        
        # Guardar cambios
        guardar_datos()
        return True
    return False

def pagar_cuota_credito():
    """Proceso de pago de cuotas de crédito"""
    # Recargar datos desde JSON
    cargar_datos()
    
    salir = 's'
    while salir == 's':
        cuenta_ingresada = input("Ingrese su cedula: ").strip()
        
        if cuenta_ingresada not in cuentas_bancarias:
            print('Cedula invalida, no ha sido registrada.')
            respuesta = input('¿Desea salir? (s/n): ').strip().lower()
            while respuesta not in ('s', 'n'):
                print('Opcion invalida.')
                respuesta = input('¿Desea salir? (s/n): ').strip().lower()
            if respuesta == 's':
                salir = 'n'
                break
            else:
                continue
        
        # Buscar créditos y aprobar automáticamente si es necesario
        if cuenta_ingresada in productos_cliente:
            for producto_id, datos in productos_cliente[cuenta_ingresada].items():
                if producto_id.startswith(('credito_libre_inversion', 'credito_vivienda', 'credito_compra_auto')):
                    aprobar_credito_automaticamente(cuenta_ingresada, producto_id, datos)
        
        # Obtener créditos activos
        creditos_activos = obtener_creditos_activos(cuenta_ingresada)
        
        if not creditos_activos:
            print('No tienes creditos activos para pagar.')
            print('Los creditos deben estar aprobados y tener saldo pendiente.')
            precionar_continuar()
            salir = 'n'
            break
        
        # Mostrar información de la cuenta
        saldo_actual = cuentas_bancarias[cuenta_ingresada]["saldo"]
        print(f'\nTu cuenta esta registrada como: {cuentas_bancarias[cuenta_ingresada]["tipo_cuenta_bancaria"]}')
        print(f'Tu saldo actual es: ${saldo_actual}')
        
        print('\n--- CREDITOS ACTIVOS PARA PAGO ---')
        for i, credito in enumerate(creditos_activos, 1):
            monto_original = credito.get("monto_original", credito.get("monto", 0))
            print(f'{i}. Credito de ${monto_original}')
            print(f'   Saldo pendiente: ${credito["saldo_pendiente"]}')
            print(f'   Cuota mensual: ${credito["cuota_mensual"]}')
            print(f'   Cuotas restantes: {credito["cuotas_restantes"]}')
            print()
        
        # Seleccionar crédito a pagar
        try:
            opcion_credito = int(input('Seleccione el numero del credito a pagar: ')) - 1
            if opcion_credito < 0 or opcion_credito >= len(creditos_activos):
                print('Opcion invalida.')
                continue
        except ValueError:
            print('Ingrese un numero valido.')
            continue
        
        credito_seleccionado = creditos_activos[opcion_credito]
        cuota_mensual = credito_seleccionado["cuota_mensual"]
        producto_id_seleccionado = credito_seleccionado["producto_id"]
        
        # Verificar saldo suficiente
        if saldo_actual < cuota_mensual:
            print(f'Saldo insuficiente. Necesitas ${cuota_mensual} para pagar la cuota.')
            print(f'Tu saldo actual es: ${saldo_actual}')
            precionar_continuar()
            salir = 'n'
            break
        
        # Confirmar pago
        print(f'\nEstas por pagar una cuota de: ${cuota_mensual}')
        confirmacion = input('¿Confirmar pago? (s/n): ').strip().lower()
        
        if confirmacion == 's':
            # Actualizar saldo de la cuenta principal
            id_producto_cuenta = cuentas_bancarias[cuenta_ingresada]['tipo_cuenta_bancaria']
            productos_cliente[cuenta_ingresada][id_producto_cuenta]['saldo'] -= cuota_mensual
            
            # Sincronizar saldo general
            sincronizar_saldos(cuenta_ingresada)
            
            # Actualizar el crédito
            productos_cliente[cuenta_ingresada][producto_id_seleccionado]['saldo_pendiente'] -= cuota_mensual
            productos_cliente[cuenta_ingresada][producto_id_seleccionado]['cuotas_restantes'] -= 1
            
            # Si se pagó completamente
            if productos_cliente[cuenta_ingresada][producto_id_seleccionado]['saldo_pendiente'] <= 0:
                productos_cliente[cuenta_ingresada][producto_id_seleccionado]['evento'] = 'Pagado_Completamente'
                productos_cliente[cuenta_ingresada][producto_id_seleccionado]['saldo_pendiente'] = 0
            
            # Registrar en historial del crédito
            registrar_historial(cuenta_ingresada, producto_id_seleccionado, cuota_mensual, 'Pago_Credito')
            
            # Registrar en historial de la cuenta
            registrar_historial(cuenta_ingresada, id_producto_cuenta, cuota_mensual, 'Retiro_Pago_Credito')
            
            print('¡Pago realizado exitosamente!')
            print(f'Nuevo saldo en cuenta: ${cuentas_bancarias[cuenta_ingresada]["saldo"]:,.2f}')
            
            saldo_restante = credito_seleccionado["saldo_pendiente"] - cuota_mensual
            print(f'Saldo pendiente del credito: ${max(0, saldo_restante):,.2f}')
            
            if saldo_restante <= 0:
                print('¡Felicitaciones! Has pagado completamente este credito.')
            
            precionar_continuar()
        else:
            print('Pago cancelado.')
            precionar_continuar()
        
        salir = 'n'

def retirar_dinero():
    """Proceso de retiro de dinero"""
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
                    print('Opcion invalida.')
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
                        print('Opcion invalida.')
                        ingresar_otra_cuenta = input('Deseas ingresar otra cuenta (s/n): ').strip().lower()
                        continue
            else:
                while True:
                    try:
                        cantidad_retirada = float(input('Ingrese la cantidad que desea retirar: ').strip())
                    except ValueError:
                        print('Solo se permiten numeros.')
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
                        # Actualizar producto
                        id_producto = cuentas_bancarias[cuenta_ingresada]['tipo_cuenta_bancaria']
                        if cuenta_ingresada in productos_cliente and id_producto in productos_cliente[cuenta_ingresada]:
                            productos_cliente[cuenta_ingresada][id_producto]['saldo'] -= cantidad_retirada
                        
                        # Sincronizar saldo general
                        sincronizar_saldos(cuenta_ingresada)
                        
                        # Registrar en historial
                        registrar_historial(cuenta_ingresada, id_producto, cantidad_retirada, 'Retiro')
                        
                        print('Retiro exitoso')
                        print(f'Tu saldo actual es: {cuentas_bancarias[cuenta_ingresada]["saldo"]}')
                        print(f'La cantidad retirada fue: {cantidad_retirada}')
                        precionar_continuar()
                        seguir = 'n'
                        break

def cancelar_cuenta():
    """Proceso de cancelación de cuenta"""
    global cuentas_bancarias, productos_cliente, cuentas_canceladas
    while True:
        cedula = input("Ingrese la cedula de la cuenta a eliminar: ").strip()
        if not cedula:
            limpiar()
            print("La cedula no puede estar vacia.")
            precionar_continuar()
            continue

        if cedula in cuentas_bancarias:
            # Recuperar datos del usuario
            datos_usuario = cuentas_bancarias.pop(cedula)

            # Recuperar productos asociados
            datos_producto = productos_cliente.pop(cedula, {})

            # Unir la info en un solo diccionario
            datos_completos = {
                "usuario": datos_usuario,
                "productos": datos_producto
            }

            # Guardar en el diccionario en memoria
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
            print("No existe una cuenta con esa cedula.")
            precionar_continuar()
            continue

def main():
    """Función principal del programa"""
    # Cargar datos al inicio
    cargar_datos()
    
    # Ciclo principal del programa
    while True:
        mostrar_menu_principal()
        try:
            opcion = input("Seleccione una opcion: ")
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
                    print('Opcion no valida. Por favor, intente de nuevo.')
                    precionar_continuar()
        except ValueError:
            print('Error: Entrada invalida.')