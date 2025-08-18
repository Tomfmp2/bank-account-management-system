# Autor

**Tomas Felipe Medina Prada**

# Descripción

Este proyecto corresponde a un **sistema bancario en entorno de consola** desarrollado en Python, cuyo propósito es la gestión integral de cuentas bancarias y créditos de clientes.
 Entre las principales funcionalidades se incluyen:

- Creación de cuentas bancarias (corriente, ahorro, CDT).
- Solicitud y administración de créditos (libre inversión, vivienda, compra de vehículo).
- Operaciones financieras: depósitos y retiros.
- Pago de cuotas de créditos activos.
- Cancelación de cuentas, con registro histórico en un archivo independiente.
- Persistencia de la información en archivos JSON, asegurando integridad y continuidad de datos entre sesiones.

# Requerimientos

- **Versión de Python:** 3.10 o superior (indispensable debido al uso de `match-case`).
- **Dependencias externas:** No se requieren, el proyecto utiliza exclusivamente librerías estándar de Python:
  - `os`
  - `json`
  - `typing`

# Ejecución

## En Linux

1. Clonar o descargar el repositorio.

2. Acceder a la carpeta raíz del proyecto.

3. Ejecutar el comando:

   ```bash
   python3 main.py
   ```

## En Windows

1. Clonar o descargar el repositorio.

2. Abrir una terminal (CMD o PowerShell) en la carpeta raíz del proyecto.

3. Ejecutar el comando:

   ```bash
   python main.py
   ```

# Estructura de Archivos

```
📂 bank-account-management-system/
│── main.py                # Archivo principal, inicia la ejecución del sistema.
│
├── modules/               # Módulos que contienen la lógica del sistema.
│   ├── tools.py           # Funciones utilitarias (limpieza de pantalla, pausa).
│   ├── menus.py           # Definición y despliegue de menús interactivos.
│   ├── data_manager.py    # Gestión central: cuentas, créditos, depósitos, retiros.
│   └── corefiles.py       # Control de archivos JSON: lectura, escritura y creación.
│
├── data/                  # Carpeta destinada a la persistencia de información.
│   ├── cuentas_registradas.json   # Registro de cuentas activas.
│   └── cuentas_canceladas.json    # Historial de cuentas canceladas.
```

# Librerías externas

Este proyecto **no requiere librerías externas**. Toda la implementación se realiza con módulos estándar de Python, garantizando portabilidad y simplicidad en la instalación.

------



