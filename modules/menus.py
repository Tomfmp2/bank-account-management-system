from modules.tools import limpiar
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
    print("______Tipo Credito_____")
    print("\n1. Credito Libre Inversion")
    print("2. Credito Vivienda")
    print("3. Credito Compra Auto Movil")
    print("4. Salir")
    print("----------------------------------")