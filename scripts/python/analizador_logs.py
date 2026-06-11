import os
import re
from datetime import datetime

LOG_FILE = "../../dia1/notas.txt"

def analizar_log(ruta):
    print(f"=== Analizador de Logs ===")
    print(f"Archivo: {ruta}")
    print(f"Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("---")

    try:
        with open(ruta, 'r') as archivo:
            lineas = archivo.readlines()

        total = len(lineas)
        errores = [l for l in lineas if "ERROR" in l]
        warnings = [l for l in lineas if "WARN" in l]

        print(f"Total líneas  : {total}")
        print(f"Errores       : {len(errores)}")
        print(f"Warnings      : {len(warnings)}")

        if errores:
            print("\n--- Errores encontrados ---")
            for error in errores:
                print(f"  {error.strip()}")
        else:
            print("\nOK — Sin errores detectados")

    except FileNotFoundError:
        print(f"ERROR: No se encontró el archivo {ruta}")

if __name__ == "__main__":
    analizar_log(LOG_FILE)
