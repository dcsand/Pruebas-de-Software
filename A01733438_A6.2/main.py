"""Script principal para demostrar la ejecución del sistema."""

from reservation_system import Hotel, Customer, Reservation

def main():
    """Ejecuta pruebas manuales en consola."""
    print("=== INICIANDO SISTEMA DE RESERVACIONES ===")
    
    # 1. Mostrar datos cargados desde los JSON (Req 2)
    print("\n--- Catálogo de Hoteles ---")
    Hotel.display_hotel_info("H01")
    Hotel.display_hotel_info("H02")

    print("\n--- Catálogo de Clientes ---")
    Customer.display_customer_info("C01")

    # 2. Hacer una reservación (Req 2)
    print("\n--- Creando una Reservación ---")
    res = Reservation("R01", "C01", "H01")
    if Reservation.create_reservation(res):
        Hotel.reserve_room("H01")
        print("¡Reservación R01 creada con éxito para Daniel en Hotel Tequendama!")

    # 3. Mostrar cómo bajó la disponibilidad
    print("\n--- Disponibilidad Actualizada ---")
    Hotel.display_hotel_info("H01")

if __name__ == "__main__":
    main()