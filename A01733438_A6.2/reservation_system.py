"""
Módulo para la gestión del sistema de reservaciones de hoteles.

Contiene las clases Hotel, Customer y Reservation, permitiendo la
persistencia de datos en archivos JSON y el manejo de errores.
"""

import json
import os


def load_data(filename):
    """
    Carga los datos desde un archivo JSON.
    Maneja datos inválidos mostrando un error y continuando la ejecución.
    """
    if not os.path.exists(filename):
        return []

    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return json.load(file)
    except json.JSONDecodeError:
        print(f"Error: El archivo {filename} contiene datos inválidos.")
        return []
    except IOError as error:
        print(f"Error de lectura en el archivo {filename}: {error}")
        return []


def save_data(data, filename):
    """Guarda los datos en un archivo JSON."""
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4)
    except IOError as error:
        print(f"Error al guardar en el archivo {filename}: {error}")


class Hotel:
    """Representa un hotel en el sistema de reservaciones."""

    def __init__(self, hotel_id, name, location, rooms_available):
        """Inicializa un nuevo hotel."""
        self.hotel_id = hotel_id
        self.name = name
        self.location = location
        self.rooms_available = rooms_available

    def to_dict(self):
        """Convierte la instancia del hotel a un diccionario."""
        return {
            "hotel_id": self.hotel_id,
            "name": self.name,
            "location": self.location,
            "rooms_available": self.rooms_available
        }

    @classmethod
    def create_hotel(cls, hotel_data, filename="hotels.json"):
        """Guarda un nuevo hotel en el archivo."""
        hotels = load_data(filename)

        if any(h.get("hotel_id") == hotel_data.hotel_id for h in hotels):
            print(f"Error: El hotel {hotel_data.hotel_id} ya existe.")
            return False

        hotels.append(hotel_data.to_dict())
        save_data(hotels, filename)
        return True

    @classmethod
    def delete_hotel(cls, hotel_id, filename="hotels.json"):
        """Elimina un hotel del archivo usando su ID."""
        hotels = load_data(filename)
        updated_hotels = [h for h in hotels if h.get("hotel_id") != hotel_id]

        if len(hotels) == len(updated_hotels):
            print("Error: Hotel no encontrado para eliminar.")
            return False

        save_data(updated_hotels, filename)
        return True

    @classmethod
    def display_hotel_info(cls, hotel_id, filename="hotels.json"):
        """Muestra en consola la información de un hotel y la retorna."""
        hotels = load_data(filename)
        for hotel in hotels:
            if hotel.get("hotel_id") == hotel_id:
                print("--- Información del Hotel ---")
                print(f"ID: {hotel['hotel_id']}")
                print(f"Nombre: {hotel['name']}")
                print(f"Ubicación: {hotel['location']}")
                print(f"Habitaciones: {hotel['rooms_available']}")
                return hotel

        print("Error: Hotel no encontrado.")
        return None

    @classmethod
    def modify_hotel_info(cls, hotel_id, key, new_val, filename="hotels.json"):
        """Modifica un campo específico de un hotel existente."""
        hotels = load_data(filename)
        for hotel in hotels:
            if hotel.get("hotel_id") == hotel_id:
                if key in hotel:
                    hotel[key] = new_val
                    save_data(hotels, filename)
                    return True
                print(f"Error: La propiedad '{key}' no existe en el hotel.")
                return False

        print("Error: Hotel no encontrado para modificar.")
        return False

    @classmethod
    def reserve_room(cls, hotel_id, filename="hotels.json"):
        """Resta una habitación de la disponibilidad del hotel."""
        hotels = load_data(filename)
        for hotel in hotels:
            if hotel.get("hotel_id") == hotel_id:
                if hotel["rooms_available"] > 0:
                    hotel["rooms_available"] -= 1
                    save_data(hotels, filename)
                    return True
                print("Error: No hay habitaciones disponibles.")
                return False

        print("Error: Hotel no encontrado para reserva.")
        return False

    @classmethod
    def cancel_reservation(cls, hotel_id, filename="hotels.json"):
        """Suma una habitación a la disponibilidad del hotel."""
        hotels = load_data(filename)
        for hotel in hotels:
            if hotel.get("hotel_id") == hotel_id:
                hotel["rooms_available"] += 1
                save_data(hotels, filename)
                return True

        print("Error: Hotel no encontrado para cancelar reserva.")
        return False


class Customer:
    """Representa un cliente en el sistema de reservaciones."""

    def __init__(self, customer_id, name, email):
        """Inicializa un nuevo cliente."""
        self.customer_id = customer_id
        self.name = name
        self.email = email

    def to_dict(self):
        """Convierte la instancia a diccionario para JSON."""
        return {
            "customer_id": self.customer_id,
            "name": self.name,
            "email": self.email
        }

    @classmethod
    def create_customer(cls, customer_data, filename="customers.json"):
        """Crea un cliente y lo guarda en el archivo."""
        customers = load_data(filename)

        if any(c.get("customer_id") == customer_data.customer_id
               for c in customers):
            print(f"Error: El cliente {customer_data.customer_id} ya existe.")
            return False

        customers.append(customer_data.to_dict())
        save_data(customers, filename)
        return True

    @classmethod
    def delete_customer(cls, customer_id, filename="customers.json"):
        """Elimina un cliente del archivo."""
        customers = load_data(filename)
        updated = [c for c in customers if c.get("customer_id") != customer_id]

        if len(customers) == len(updated):
            print("Error: Cliente no encontrado para eliminar.")
            return False

        save_data(updated, filename)
        return True

    @classmethod
    def display_customer_info(cls, customer_id, filename="customers.json"):
        """Muestra la información de un cliente específico."""
        customers = load_data(filename)
        for customer in customers:
            if customer.get("customer_id") == customer_id:
                print("--- Información del Cliente ---")
                print(f"ID: {customer['customer_id']}")
                print(f"Nombre: {customer['name']}")
                print(f"Email: {customer['email']}")
                return customer

        print("Error: Cliente no encontrado.")
        return None

    @classmethod
    def modify_customer_info(cls, customer_id, key, new_val,
                             filename="customers.json"):
        """Modifica la información de un cliente existente."""
        customers = load_data(filename)
        for customer in customers:
            if customer.get("customer_id") == customer_id:
                if key in customer:
                    customer[key] = new_val
                    save_data(customers, filename)
                    return True
                print(f"Error: La propiedad '{key}' no existe.")
                return False

        print("Error: Cliente no encontrado para modificar.")
        return False


class Reservation:
    """Maneja las reservaciones vinculando clientes y hoteles."""

    def __init__(self, reservation_id, customer_id, hotel_id):
        """Inicializa una nueva reservación."""
        self.reservation_id = reservation_id
        self.customer_id = customer_id
        self.hotel_id = hotel_id

    def to_dict(self):
        """Convierte la reservación a diccionario."""
        return {
            "reservation_id": self.reservation_id,
            "customer_id": self.customer_id,
            "hotel_id": self.hotel_id
        }

    @classmethod
    def create_reservation(cls, res_data, filename="reservations.json"):
        """Crea una reservación vinculando cliente y hotel."""
        reservations = load_data(filename)

        if any(r.get("reservation_id") == res_data.reservation_id
               for r in reservations):
            print(f"Error: Reservación {res_data.reservation_id} ya existe.")
            return False

        reservations.append(res_data.to_dict())
        save_data(reservations, filename)
        return True

    @classmethod
    def cancel_reservation(cls, reservation_id, filename="reservations.json"):
        """Cancela una reservación existente."""
        reservations = load_data(filename)
        updated = [
            r for r in reservations
            if r.get("reservation_id") != reservation_id
        ]

        if len(reservations) == len(updated):
            print("Error: Reservación no encontrada para cancelar.")
            return False

        save_data(updated, filename)
        return True
