"""
Script de automatización de pruebas para el programa compute_statistics.py.
Organiza la ejecución de casos de prueba y gestiona los archivos de salida
hacia la carpeta de resultados siguiendo los estándares académicos.
"""

import os
import subprocess
import shutil


# Configuración de constantes según los requerimientos del proyecto
# Nota: El Req 4 especifica el nombre computeStatistics.py
SOURCE_SCRIPT = "compute_statistics.py"
RESULT_FILE = "StatisticsResults.txt"


def run_test_suite():
    """
    Ejecuta la suite de pruebas localizando el código fuente en la carpeta
    adyacente y moviendo los reportes generados a la carpeta de resultados.
    """
    # Establecer el directorio de trabajo actual en la ubicación del script
    base_path = os.path.dirname(os.path.abspath(__file__))
    os.chdir(base_path)

    # Definición de rutas relativas
    source_path = os.path.join("..", "source", SOURCE_SCRIPT)
    results_dir = os.path.join("..", "results")

    # Validación de entorno
    if not os.path.exists(source_path):
        print(f"Error: No se encontró el script de origen en {source_path}")
        return

    if not os.path.exists(results_dir):
        os.makedirs(results_dir)

    # Identificación de archivos de entrada (TC*.txt)
    test_cases = sorted([f for f in os.listdir('.')
                        if f.startswith('TC') and f.endswith('.txt')])

    if not test_cases:
        print("No se localizaron archivos de prueba con el prefijo 'TC'.")
        return

    print("=" * 60)
    print(f"EJECUCIÓN DE PRUEBAS: {SOURCE_SCRIPT}")
    print("=" * 60)

    for test_file in test_cases:
        print(f"Procesando: {test_file}")

        try:
            # Ejecución del programa mediante subprocess
            subprocess.run(['python', source_path, test_file], check=True)
            print(f"Estado: Ejecución exitosa")
        except subprocess.CalledProcessError as err:
            print(f"Estado: Error en ejecución - {err}")

        print("-" * 60)

    # Gestión y transferencia de resultados
    if os.path.exists(RESULT_FILE):
        destination = os.path.join(results_dir, RESULT_FILE)

        if os.path.exists(destination):
            os.remove(destination)

        shutil.move(RESULT_FILE, destination)
        print("\nINFORME FINAL")
        print(f"Archivo de resultados consolidado en: {destination}")
    else:
        print("\nAdvertencia: El archivo de salida no fue generado.")

    print("\nProceso de pruebas finalizado.")
    print("=" * 60)


if __name__ == "__main__":
    run_test_suite()