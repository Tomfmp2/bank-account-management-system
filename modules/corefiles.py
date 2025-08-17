from modules.tools import limpiar, precionar_continuar
import os
import json
from typing import Dict, List, Optional, Any, Union, Callable

# Rutas de archivos JSON
CUENTAS_BANCARIAS = "data/cuentas_registradas.json"
CUENTAS_CANCELADAS = "data/cuentas_canceladas.json"

def read_json(file_path: str) -> Dict[str, Any]:
    """Lee y retorna datos desde archivo JSON"""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def write_json(file_path: str, data: Dict[str, Any]) -> None:
    """Escribe datos al archivo JSON asegurando que la carpeta exista"""
    directory = os.path.dirname(file_path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def crear_archivo_json(file_path: str, inicial: Optional[Dict[str, Any]] = None) -> None:
    """Crea archivo JSON si no existe o agrega claves faltantes si existe"""
    if inicial is None:
        inicial = {}

    if not os.path.exists(file_path):
        write_json(file_path, inicial)
    else:
        datos_existentes = read_json(file_path)
        if not isinstance(datos_existentes, dict):
            datos_existentes = {}
        # Agregar solo claves que falten sin sobrescribir existentes
        for key, value in inicial.items():
            if key not in datos_existentes:
                datos_existentes[key] = value
        write_json(file_path, datos_existentes)

def registrar_datos(
    file_path: str,
    datos_usuario_input: Union[Dict[str, Any], Callable[[], Dict[str, Any]]]
) -> Dict[str, Any]:
    """Registra datos dentro del archivo JSON"""
    
    contenido = read_json(file_path)
    if not isinstance(contenido, dict):
        contenido = {}

    # Obtener el diccionario de datos
    data = datos_usuario_input() if callable(datos_usuario_input) else datos_usuario_input

    if not isinstance(data, dict):
        raise TypeError("datos_usuario_input debe ser un dict o una funcion que retorne un dict")

    # Determinar la clave a usar
    if len(data) == 1:
        # Si hay solo una clave usar esa clave directamente
        contenido.update(data)
    else:
        # Buscar la cedula en la estructura de datos
        cc = None
        if 'cc' in data:
            cc = data['cc']
        elif 'usuario' in data and isinstance(data['usuario'], dict) and 'cc' in data['usuario']:
            cc = data['usuario']['cc']
        
        if cc is None:
            raise ValueError("No se pudo encontrar la cedula (cc) en los datos proporcionados")
        
        contenido[cc] = data

    write_json(file_path, contenido)
    return contenido