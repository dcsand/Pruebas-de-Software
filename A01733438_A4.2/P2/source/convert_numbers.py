"""
Programa para convertir números a binario y hexadecimal.
Cumple con PEP-8 y manejo de errores.
"""

import sys
import time


def to_binary(n):
    """Convierte un número a binario usando algoritmos básicos."""
    if n == 0:
        return "0"
    is_negative = n < 0
    num = abs(int(n))
    binary = ""
    while num > 0:
        binary = str(num % 2) + binary
        num //= 2
    return "-" + binary if is_negative else binary


def to_hexadecimal(n):
    """Convierte un número a hexadecimal usando algoritmos básicos."""
    if n == 0:
        return "0"
    hex_chars = "0123456789ABCDEF"
    is_negative = n < 0
    num = abs(int(n))
    hex_res = ""
    while num > 0:
        hex_res = hex_chars[num % 16] + hex_res
        num //= 16
    return "-" + hex_res if is_negative else hex_res


def process_file(filename):
    """Lee el archivo y retorna una lista con las conversiones."""
    data = []
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                val = line.strip()
                if val:
                    try:
                        num = int(float(val))
                        data.append((num, to_binary(num), to_hexadecimal(num)))
                    except ValueError:
                        print(f"Error: Dato inválido omitido: {val}")
    except FileNotFoundError:
        print(f"Error: El archivo '{filename}' no existe.")
        return None
    return data


def main():
    """Función principal."""
    start_time = time.time()
    if len(sys.argv) < 2:
        print("Uso: python convertNumbers.py fileWithData.txt")
        return

    results = process_file(sys.argv[1])
    if results is None:
        return

    elapsed_time = time.time() - start_time
    header = f"{'ITEM':<6} {'NUMBER':<10} {'BINARY':<18} {'HEX':<12}"
    output = [header, "-" * 50]

    for i, res in enumerate(results, 1):
        output.append(f"{i:<6} {res[0]:<10} {res[1]:<18} {res[2]:<12}")

    output.append(f"\nExecution Time: {elapsed_time:.6f} seconds")
    final_text = "\n".join(output)

    print(final_text)
    with open("ConvertionResults.txt", 'w', encoding='utf-8') as f_out:
        f_out.write(final_text)
        f_out.write("\n")  # Asegura el salto de línea final en el txt


if __name__ == "__main__":
    main()
