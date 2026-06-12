import requests
import json
from datetime import datetime

API_URL = "https://jsonplaceholder.typicode.com"

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

def obtener_usuario(id_usuario):
    print(f"=== Consultando API ===")
    print(f"Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"URL: {API_URL}/users/{id_usuario}")
    print("---")

    try:
        respuesta = requests.get(f"{API_URL}/users/{id_usuario}")
        
        if respuesta.status_code == 200:
            usuario = respuesta.json()
            print(f"Nombre    : {usuario['name']}")
            print(f"Email     : {usuario['email']}")
            print(f"Teléfono  : {usuario['phone']}")
            print(f"Ciudad    : {usuario['address']['city']}")
            print(f"Empresa   : {usuario['company']['name']}")
            with open("../../logs/resultados_api.txt", "a") as archivo:
                archivo.write(f"{datetime.now()} - Usuario: {usuario['name']} - Email: {usuario['email']}\n")

        else:
            print(f"ERROR: La API respondió con código {respuesta.status_code}")

    except requests.exceptions.ConnectionError:
        print("ERROR: No hay conexión a internet")

if __name__ == "__main__":
    if verificar_api():
        print("---")
        for i in range(1, 4):
            obtener_usuario(i)
            print("")
