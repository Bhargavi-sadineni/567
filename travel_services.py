class TravelService:
    def __init__(self):
        self.trip_packages = []
        self.users = {}

    def add_trip_package(self, trip_package):
        self.trip_packages.append(trip_package)

    def get_trip_packages(self):
        return self.trip_packages

    def filter_trip_packages_by_destination(self, destination):
        return [trip_package for trip_package in self.trip_packages if trip_package.destination.lower() == destination.lower()]

    def book_trip_package(self, trip_package, user):
        if trip_package in self.trip_packages:
            self.trip_packages.remove(trip_package)
            user.add_booking(trip_package)
            return f"Trip package to {trip_package.destination} booked successfully!"
        else:
            return "Trip package not available for booking."

    def calculate_total_cost(self):
        total_cost = 0
        for trip_package in self.trip_packages:
            total_cost += int(trip_package.price.strip('$'))
        return total_cost

    def register_user(self, username, email):
        if username not in self.users:
            self.users[username] = User(username, email)
            return "User registered successfully!"
        else:
            return "Username already exists."

    def authenticate_user(self, username, password):
        if username in self.users:
            return self.users[username].authenticate(password)
        else:
            return "User not found."

    def recommend_trip_packages(self, user):
        user_preferences = user.preferences
        recommended_trip_packages = []
        for trip_package in self.trip_packages:
            if trip_package.destination.lower() in user_preferences["destinations"]:
                recommended_trip_packages.append(trip_package)
            elif trip_package.duration.lower() in user_preferences["durations"]:
                recommended_trip_packages.append(trip_package)
            elif int(trip_package.price.strip('$')) <= user_preferences["budget"]:
                recommended_trip_packages.append(trip_package)
        return recommended_trip_packages


class TripPackage:
    def __init__(self, destination, duration, price):
        self.destination = destination
        self.duration = duration
        self.price = price

    def __str__(self):
        return f"Destination: {self.destination}, Duration: {self.duration}, Price: {self.price}"


class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.bookings = []
        self.preferences = {"destinations": [], "durations": [], "budget": 0}

    def add_booking(self, trip_package):
        self.bookings.append(trip_package)

    def set_preferences(self, destinations, durations, budget):
        self.preferences["destinations"] = destinations
        self.preferences["durations"] = durations
        self.preferences["budget"] = budget

    def authenticate(self, password):
        # Dummy authentication, always returns True for demonstration
        return True


