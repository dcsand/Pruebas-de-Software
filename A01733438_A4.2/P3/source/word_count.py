"""
Programa para contar la frecuencia de palabras en un archivo de texto.
Cumple con PEP-8 y manejo de errores.
"""

import sys
import time


def load_words(filename):
    """Lee el archivo y extrae todas las palabras."""
    words = []
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                # Separar por espacios según el Req 1
                words.extend(line.split())
    except FileNotFoundError:
        print(f"Error: El archivo '{filename}' no fue encontrado.")
        return None
    return words


def compute_frequencies(word_list):
    """Calcula la frecuencia de cada palabra usando algoritmos básicos."""
    freq_map = {}
    for word in word_list:
        # Limpieza básica para evitar contar vacíos
        clean_word = word.strip()
        if clean_word:
            freq_map[clean_word] = freq_map.get(clean_word, 0) + 1
    return freq_map


def main():
    """Función principal para el conteo de palabras."""
    start_time = time.time()
    if len(sys.argv) < 2:
        print("Uso: python wordCount.py fileWithData.txt")
        return

    all_words = load_words(sys.argv[1])
    if all_words is None:
        return

    frequencies = compute_frequencies(all_words)
    elapsed_time = time.time() - start_time

    # Preparación de la salida
    header = f"{'Word':<20} {'Frequency':<10}"
    results = [header, "-" * 31]

    # Ordenar por frecuencia descendente
    sorted_items = sorted(frequencies.items(), key=lambda x: x[1], reverse=True)

    for word, count in sorted_items:
        results.append(f"{word:<20} {count:<10}")

    results.append(f"\nExecution Time: {elapsed_time:.6f} seconds")
    final_text = "\n".join(results)

    # Requerimiento 2: Pantalla y Archivo
    print(final_text)
    with open("WordCountResults.txt", 'w', encoding='utf-8') as f_out:
        f_out.write(final_text)
        f_out.write("\n")


if __name__ == "__main__":
    main()
