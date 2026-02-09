"""
Script de automatización de pruebas para el programa de conversión de números.
Asegura el cumplimiento de los requerimientos de salida para el Ejercicio 2.
"""

import os
import subprocess
import shutil

SOURCE_SCRIPT = "convert_numbers.py"  
RESULT_FILE = "ConvertionResults.txt"

def run_test_suite():
    """Ejecuta la suite de pruebas y gestiona resultados para P2."""
    base_path = os.path.dirname(os.path.abspath(__file__))
    os.chdir(base_path)

    source_path = os.path.join("..", "source", SOURCE_SCRIPT)
    results_dir = os.path.join("..", "results")

    if not os.path.exists(source_path):
        print(f"Error: No se encontró el script de origen en {source_path}")
        return

    if not os.path.exists(results_dir):
        os.makedirs(results_dir)

    test_cases = sorted([f for f in os.listdir('.')
                        if f.startswith('TC') and f.endswith('.txt')])

    print("=" * 60)
    print(f"SISTEMA DE PRUEBAS: {SOURCE_SCRIPT}")
    print("=" * 60)

    for test_file in test_cases:
        print(f"Procesando: {test_file}")
        try:
            subprocess.run(['python', source_path, test_file], check=True)
            print("Estado: Ejecución exitosa")
        except subprocess.CalledProcessError as err:
            print(f"Estado: Error en ejecución - {err}")
        print("-" * 60)

    if os.path.exists(RESULT_FILE):
        destination = os.path.join(results_dir, RESULT_FILE)
        if os.path.exists(destination):
            os.remove(destination)
        shutil.move(RESULT_FILE, destination)
        print(f"\nInforme de conversiones guardado en: {destination}")
    else:
        print("\nAdvertencia: El archivo 'ConvertionResults.txt' no fue generado.")

    print("=" * 60)

if __name__ == "__main__":
    run_test_suite()