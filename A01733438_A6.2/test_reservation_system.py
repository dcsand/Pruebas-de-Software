"""
Módulo de pruebas unitarias para el sistema de reservaciones.

Implementa casos de prueba para Hotel, Customer y Reservation,
asegurando una cobertura superior al 85% y cumpliendo PEP-8.
"""

import unittest
import os
import json
from reservation_system import Hotel, Customer, Reservation, load_data, save_data


class TestDataAccess(unittest.TestCase):
    """Pruebas para las funciones de persistencia de datos."""

    def setUp(self):
        """Configura un archivo temporal para las pruebas."""
        self.test_file = "test_data.json"

    def tearDown(self):
        """Limpia el archivo temporal después de cada prueba."""
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_load_nonexistent_file(self):
        """Prueba la carga de un archivo que no existe."""
        data = load_data("archivo_falso.json")
        self.assertEqual(data, [])

    def test_load_invalid_json(self):
        """Prueba la carga de un archivo con JSON corrupto (Req 5)."""
        with open(self.test_file, 'w', encoding='utf-8') as file:
            file.write("{datos_invalidos: faltan_comillas}")
        data = load_data(self.test_file)
        self.assertEqual(data, [])

    def test_save_and_load_valid_data(self):
        """Prueba guardar y cargar datos válidos."""
        test_data = [{"id": 1, "name": "Test"}]
        save_data(test_data, self.test_file)
        loaded_data = load_data(self.test_file)
        self.assertEqual(loaded_data, test_data)


class TestHotel(unittest.TestCase):
    """Pruebas unitarias para la clase Hotel."""

    def setUp(self):
        self.file = "test_hotels.json"
        self.hotel = Hotel("H1", "Hotel Tequendama", "Bogotá", 2)
        if os.path.exists(self.file):
            os.remove(self.file)

    def tearDown(self):
        if os.path.exists(self.file):
            os.remove(self.file)

    def test_create_hotel(self):
        """Prueba la creación de hoteles y manejo de duplicados."""
        self.assertTrue(Hotel.create_hotel(self.hotel, self.file))
        self.assertFalse(Hotel.create_hotel(self.hotel, self.file))

    def test_delete_hotel(self):
        """Prueba la eliminación de un hotel existente e inexistente."""
        Hotel.create_hotel(self.hotel, self.file)
        self.assertTrue(Hotel.delete_hotel("H1", self.file))
        self.assertFalse(Hotel.delete_hotel("H99", self.file))

    def test_display_hotel_info(self):
        """Prueba la visualización de datos de un hotel."""
        Hotel.create_hotel(self.hotel, self.file)
        self.assertIsNotNone(Hotel.display_hotel_info("H1", self.file))
        self.assertIsNone(Hotel.display_hotel_info("H99", self.file))

    def test_modify_hotel_info(self):
        """Prueba la modificación de atributos de un hotel."""
        Hotel.create_hotel(self.hotel, self.file)
        self.assertTrue(Hotel.modify_hotel_info("H1", "name", "Nuevo", self.file))
        self.assertFalse(Hotel.modify_hotel_info("H1", "falso", "X", self.file))
        self.assertFalse(Hotel.modify_hotel_info("H99", "name", "X", self.file))

    def test_reserve_room(self):
        """Prueba la reserva de habitaciones y límite de disponibilidad."""
        Hotel.create_hotel(self.hotel, self.file)
        self.assertTrue(Hotel.reserve_room("H1", self.file))  # Queda 1
        self.assertTrue(Hotel.reserve_room("H1", self.file))  # Quedan 0
        self.assertFalse(Hotel.reserve_room("H1", self.file)) # Falla por cupo
        self.assertFalse(Hotel.reserve_room("H99", self.file))

    def test_cancel_reservation(self):
        """Prueba la cancelación sumando habitaciones disponibles."""
        Hotel.create_hotel(self.hotel, self.file)
        self.assertTrue(Hotel.cancel_reservation("H1", self.file))
        self.assertFalse(Hotel.cancel_reservation("H99", self.file))


class TestCustomer(unittest.TestCase):
    """Pruebas unitarias para la clase Customer."""

    def setUp(self):
        self.file = "test_customers.json"
        self.customer = Customer("C1", "Daniel", "dan@test.com")
        if os.path.exists(self.file):
            os.remove(self.file)

    def tearDown(self):
        if os.path.exists(self.file):
            os.remove(self.file)

    def test_create_customer(self):
        """Prueba la creación de clientes."""
        self.assertTrue(Customer.create_customer(self.customer, self.file))
        self.assertFalse(Customer.create_customer(self.customer, self.file))

    def test_delete_customer(self):
        """Prueba la eliminación de clientes."""
        Customer.create_customer(self.customer, self.file)
        self.assertTrue(Customer.delete_customer("C1", self.file))
        self.assertFalse(Customer.delete_customer("C99", self.file))

    def test_display_customer_info(self):
        """Prueba la consulta de clientes."""
        Customer.create_customer(self.customer, self.file)
        self.assertIsNotNone(Customer.display_customer_info("C1", self.file))
        self.assertIsNone(Customer.display_customer_info("C99", self.file))

    def test_modify_customer_info(self):
        """Prueba la modificación de atributos del cliente."""
        Customer.create_customer(self.customer, self.file)
        self.assertTrue(Customer.modify_customer_info("C1", "name", "Dani", self.file))
        self.assertFalse(Customer.modify_customer_info("C1", "falso", "X", self.file))
        self.assertFalse(Customer.modify_customer_info("C99", "name", "X", self.file))


class TestReservation(unittest.TestCase):
    """Pruebas unitarias para la clase Reservation."""

    def setUp(self):
        self.file = "test_reservations.json"
        self.reservation = Reservation("R1", "C1", "H1")
        if os.path.exists(self.file):
            os.remove(self.file)

    def tearDown(self):
        if os.path.exists(self.file):
            os.remove(self.file)

    def test_create_reservation(self):
        """Prueba la creación de reservaciones."""
        self.assertTrue(Reservation.create_reservation(self.reservation, self.file))
        self.assertFalse(Reservation.create_reservation(self.reservation, self.file))

    def test_cancel_reservation(self):
        """Prueba la cancelación de reservaciones."""
        Reservation.create_reservation(self.reservation, self.file)
        self.assertTrue(Reservation.cancel_reservation("R1", self.file))
        self.assertFalse(Reservation.cancel_reservation("R99", self.file))


if __name__ == '__main__':
    unittest.main()