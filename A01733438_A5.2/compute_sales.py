"""
Programa para calcular el total de ventas basado en un catálogo de precios.
Cumple con los estándares PEP-8 y manejo de errores.
"""

import json
import sys
import time


def load_json_file(file_path):
    """
    Carga un archivo JSON y maneja posibles errores de lectura.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: El archivo '{file_path}' no fue encontrado.")
    except json.JSONDecodeError:
        print(f"Error: El archivo '{file_path}' no tiene un formato válido.")
    return None


def calculate_total(catalogue, sales):
    """
    Calcula el costo total de las ventas usando el catálogo de precios.
    """
    total_cost = 0.0
    price_map = {item['title']: item['price'] for item in catalogue
                 if 'title' in item and 'price' in item}

    for sale in sales:
        product = sale.get('product')
        quantity = sale.get('quantity')

        if product in price_map and isinstance(quantity, (int, float)):
            total_cost += price_map[product] * quantity
        else:
            print(f"Dato inválido omitido: {sale}")

    return total_cost


def main():
    """
    Función principal para ejecutar la lógica de cálculo de ventas.
    """
    start_time = time.time()

    if len(sys.argv) != 3:
        print("Uso: python computeSales.py "
              "priceCatalogue.json salesRecord.json")
        return

    price_file = sys.argv[1]
    sales_file = sys.argv[2]

    catalogue_data = load_json_file(price_file)
    sales_data = load_json_file(sales_file)

    if catalogue_data is None or sales_data is None:
        return

    total_sales = calculate_total(catalogue_data, sales_data)
    elapsed_time = time.time() - start_time

    # Preparar el resultado
    result_output = (
        "----------- REPORTE DE VENTAS -----------\n"
        f"Costo Total: ${total_sales:,.2f}\n"
        f"Tiempo de ejecución: {elapsed_time:.4f} segundos\n"
        "-----------------------------------------\n"
    )

    # Imprimir en pantalla y guardar en archivo
    print(result_output)
    try:
        with open("SalesResults.txt", "w", encoding='utf-8') as f_out:
            f_out.write(result_output)
    except IOError as error:
        print(f"Error al escribir el archivo de resultados: {error}")


if __name__ == "__main__":
    main()
