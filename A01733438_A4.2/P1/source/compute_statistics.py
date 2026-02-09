"""
Programa para calcular estadísticas descriptivas (Media, Mediana, Moda, SD, Varianza).
Cumple con PEP-8 y manejo de errores.
"""

import sys
import time


def compute_statistics(numbers):
    """Calcula las estadísticas descriptivas de una lista de números."""
    n = len(numbers)
    if n == 0:
        return None

    # Media
    total_sum = 0
    for num in numbers:
        total_sum += num
    mean = total_sum / n

    # Mediana
    sorted_numbers = sorted(numbers)
    if n % 2 == 0:
        median = (sorted_numbers[n // 2 - 1] + sorted_numbers[n // 2]) / 2
    else:
        median = sorted_numbers[n // 2]

    # Moda
    counts = {}
    for num in numbers:
        counts[num] = counts.get(num, 0) + 1
    max_count = max(counts.values())
    modes = [val for val, count in counts.items() if count == max_count]
    mode = modes[0] if len(modes) == 1 else modes

    # Varianza
    sum_sq_diff = 0
    for num in numbers:
        sum_sq_diff += (num - mean) ** 2
    variance = sum_sq_diff / n

    # Desviación Estándar (Raíz cuadrada manual usando exponente 0.5)
    std_dev = variance ** 0.5

    return mean, median, mode, variance, std_dev


def main():
    """Función principal para manejar archivos y flujo de ejecución."""
    start_time = time.time()
    if len(sys.argv) < 2:
        print("Uso: python computeStatistics.py fileWithData.txt")
        return

    filename = sys.argv[1]
    numbers = []

    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                try:
                    val = float(line.strip())
                    numbers.append(val)
                except ValueError:
                    print(f"Error: Dato inválido detectado y omitido: {line.strip()}")
    except FileNotFoundError:
        print(f"Error: El archivo '{filename}' no existe.")
        return

    results = compute_statistics(numbers)
    if results:
        mean, median, mode, variance, std_dev = results
        elapsed_time = time.time() - start_time

        output = (
            f"--- Estadísticas: {filename} ---\n"
            f"Media: {mean}\n"
            f"Mediana: {median}\n"
            f"Moda: {mode}\n"
            f"Varianza: {variance}\n"
            f"Desviación Estándar: {std_dev}\n"
            f"Tiempo de ejecución: {elapsed_time:.6f} segundos\n"
        )

        # Imprimir en pantalla
        print(output)

        # Guardar en archivo
        with open("StatisticsResults.txt", 'a', encoding='utf-8') as f_out:
            f_out.write(output + "\n")


if __name__ == "__main__":
    main()
    