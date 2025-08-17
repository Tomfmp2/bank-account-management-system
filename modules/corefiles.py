from modules.tools import limpiar,precionar_continuar
import os
import json
from typing import Dict, List, Optional, Any, Union, Callable

# almacena las cuentas bacarias registradas
CUENTAS_BANCARIAS = "data/cuentas_registradas.json"
CUENTAS_CANCELADAS = "data/cuentas_canceladas.json"

def read_json(file_path: str) -> Dict[str, Any]:
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def write_json(file_path: str, data: Dict[str, Any]) -> None:
    # Asegurarse de que la carpeta exista
    directory = os.path.dirname(file_path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


def crear_archivo_json(file_path: str, inicial: Optional[Dict[str, Any]] = None) -> None:
    """
    Crea el archivo si no existe con 'inicial' (por defecto {}).
    Si existe, agrega claves faltantes de 'inicial' sin borrar lo que ya haya.
    """
    if inicial is None:
        inicial = {}

    if not os.path.exists(file_path):
        # crear el archivo con el contenido inicial
        write_json(file_path, inicial)
    else:
        datos_ingresados = read_json(file_path)
        if not isinstance(datos_ingresados, dict):
            datos_ingresados = {}
        # agregar solo claves que falten
        for key, value in inicial.items():
            if key not in datos_ingresados:
                datos_ingresados[key] = value
        write_json(file_path, datos_ingresados)


def registrar_datos(
    file_path: str,
    datos_usuario_input: Union[Dict[str, Any], Callable[[], Dict[str, Any]]]
) -> Dict[str, Any]:
    """
    Registra datos dentro del JSON.
    Acepta un diccionario o una función que devuelva un diccionario.
    Para cuentas canceladas, usa la clave como viene.
    Para cuentas normales, busca 'cc' dentro de los datos del usuario.
    """
    contenido = read_json(file_path)
    if not isinstance(contenido, dict):
        contenido = {}

    # obtener el diccionario de datos
    data = datos_usuario_input() if callable(datos_usuario_input) else datos_usuario_input

    if not isinstance(data, dict):
        raise TypeError("datos_usuario_input debe ser un dict o una función que retorne un dict")

    # Determinar la clave a usar
    if len(data) == 1:
        # Si hay solo una clave (como cancelacion_1), usar esa clave
        clave = list(data.keys())[0]
        contenido.update(data)
    else:
        # Buscar la clave 'cc' en la estructura de datos
        cc = None
        if 'cc' in data:
            cc = data['cc']
        elif 'usuario' in data and isinstance(data['usuario'], dict) and 'cc' in data['usuario']:
            cc = data['usuario']['cc']
        
        if cc is None:
            raise ValueError("No se pudo encontrar la cédula (cc) en los datos proporcionados")
        
        contenido[cc] = data

    write_json(file_path, contenido)
    return contenido