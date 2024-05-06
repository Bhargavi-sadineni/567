import unittest
from travel_services import TravelService, TripPackage, User

class TestTravelService(unittest.TestCase):
    def setUp(self):
        self.travel_service = TravelService()

    def test_add_trip_package(self):
        self.travel_service.add_trip_package(TripPackage("Paris", "5 days", "$1500"))
        trip_packages = self.travel_service.get_trip_packages()
        self.assertEqual(len(trip_packages), 1)

    def test_filter_trip_packages_by_destination(self):
        self.travel_service.add_trip_package(TripPackage("Paris", "5 days", "$1500"))
        self.travel_service.add_trip_package(TripPackage("Tokyo", "7 days", "$2000"))
        self.travel_service.add_trip_package(TripPackage("Rome", "4 days", "$1200"))
        filtered_packages = self.travel_service.filter_trip_packages_by_destination("Paris")
        self.assertEqual(len(filtered_packages), 1)
        self.assertEqual(filtered_packages[0].destination, "Paris")

    def test_book_trip_package(self):
        trip_package = TripPackage("Paris", "5 days", "$1500")
        self.travel_service.add_trip_package(trip_package)
        user = User("John", "john@example.com")
        self.travel_service.book_trip_package(trip_package, user)
        self.assertEqual(len(self.travel_service.get_trip_packages()), 0)
        self.assertEqual(len(user.bookings), 1)
        self.assertEqual(user.bookings[0].destination, "Paris")

    def test_calculate_total_cost(self):
        self.travel_service.add_trip_package(TripPackage("Paris", "5 days", "$1500"))
        self.travel_service.add_trip_package(TripPackage("Tokyo", "7 days", "$2000"))
        self.travel_service.add_trip_package(TripPackage("Rome", "4 days", "$1200"))
        total_cost = self.travel_service.calculate_total_cost()
        self.assertEqual(total_cost, 4700)

    def test_register_user(self):
        self.assertEqual(len(self.travel_service.users), 0)
        self.travel_service.register_user("John", "john@example.com")
        self.assertEqual(len(self.travel_service.users), 1)
        self.assertIn("John", self.travel_service.users)

    def test_authenticate_user(self):
        self.travel_service.register_user("John", "john@example.com")
        self.assertTrue(self.travel_service.authenticate_user("John", "password"))

if __name__ == '__main__':
    unittest.main()


