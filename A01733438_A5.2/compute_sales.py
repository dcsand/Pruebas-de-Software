import json
import sys
import time
import os

def load_json_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except Exception as e:
        print(f"Error: {e}")
    return None

def calculate_total(catalogue, sales):
    total = 0.0
    price_map = {item['title']: item['price'] for item in catalogue if 'title' in item and 'price' in item}

    for s in sales:
        p = s.get('product')
        q = s.get('quantity')
        if p in price_map and isinstance(q, (int, float)):
            total += price_map[p] * q
        else:
            print("Dato invalido omitido en el calculo")
    return total

def main():
    start_time = time.time()
    if len(sys.argv) != 3:
        print("Uso: python computeSales.py priceCatalogue.json salesRecord.json")
        return
    
    f1=sys.argv[1]
    f2=sys.argv[2]

    d1 = load_json_file(f1)
    d2 = load_json_file(f2)

    if d1 is not None and d2 is not None:
        res = calculate_total(d1, d2)
        end = time.time() - start_time
        print(f"Total: {res}")
        print(f"Time: {end}")

if __name__ == "__main__":
    main()