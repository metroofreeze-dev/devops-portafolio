import os
import re
import requests
import json
from datetime import datetime

API_URL = "https://jsonplaceholder.typicode.com"
LOG_FILE = "../dia1/notas.txt"

def recopilar_sistema():
    usuario = os.getenv("USER")
    hostname = os.uname().nodename
    fecha = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    return{
        "usuario": usuario,
        "hostname": hostname,
        "fecha": fecha
    }

def analizar_logs():
    try:
        with open(LOG_FILE, 'r') as archivo:
            lineas = archivo.readlines()

        errores = [l for l in lineas if "ERROR" in l]
        warnings = [l for l in lineas if "WARN" in l]

        return {
            "total_lineas": len(lineas),
            "errores": len(errores),
            "warnings": len(warnings)
        }

    except FileNotFoundError:
        print(f"ERROR: No se encontró el archivo {LOG_FILE}")
        return None

def verificar_api():
    print("Verificando disponibilidad de la API...")
    try:
        respuesta = requests.get(API_URL, timeout=5)
        if respuesta.status_code == 200:
            print("API disponible ✓")
            return True
        else:
            print(f"API no disponible — código {respuesta.status_code}")
            return False
    except requests.exceptions.ConnectionError:
        print("ERROR: No se puede conectar a la API")
        return False

def obtener_usuario():
    try:
        respuesta = requests.get(f"{API_URL}/users/1")
        
        if respuesta.status_code == 200:
            usuario = respuesta.json()
            return {
                "nombre": usuario['name'],
                "email": usuario['email'],
                "ciudad": usuario['address']['city']
            }
        else:
            print(f"ERROR: La API respondió con código {respuesta.status_code}")
            return None

    except:
        return None
    
def generar_reporte(sistema, logs, usuario):
    reporte = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Reporte DevOps</title>
    <style>
        body {{ font-family: Arial; padding: 20px; background: #1a1a2e; color: #eee; }}
        h1 {{ color: #00d4ff; }}
        .seccion {{ background: #16213e; padding: 15px; margin: 10px 0; border-radius: 8px; border-left: 4px solid #00d4ff; }}
        .error {{ color: #ff6b6b; }}
        .ok {{ color: #51cf66; }}
    </style>
</head>
<body>
    <h1>Reporte DevOps — Semana 1</h1>

    <div class="seccion">
        <h2>Sistema</h2>
        <p>Usuario: {sistema['usuario']}</p>
        <p>Hostname: {sistema['hostname']}</p>
        <p>Fecha: {sistema['fecha']}</p>
    </div>

    <div class="seccion">
        <h2>Análisis de Logs</h2>
        <p>Total líneas: {logs['total_lineas']}</p>
        <p class="error">Errores: {logs['errores']}</p>
        <p>Warnings: {logs['warnings']}</p>
    </div>

    <div class="seccion">
        <h2>API Status</h2>
        <p>Nombre: {usuario['nombre']}</p>
        <p>Email: {usuario['email']}</p>
        <p>Ciudad: {usuario['ciudad']}</p>
    </div>
</body>
</html>
"""
    with open("reports/reporte.html", "w") as f:
        f.write(reporte)
    
    print("Reporte generado: reports/reporte.html")

def main():
    print("Iniciando reporte DevOps...")
    
    sistema = recopilar_sistema()
    logs = analizar_logs()
    usuario = obtener_usuario()
    
    generar_reporte(sistema, logs, usuario)
    
    print("Listo.")

if __name__ == "__main__":
    main()