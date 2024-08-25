# vehicle.py

class Vehicle:
    def __init__(self, reg_num, type, owner):
        self.registration_number = reg_num
        self.type = type
        self.owner = owner

    def update_owner(self, new_owner):
        """Update the owner of the vehicle."""
        self.owner = new_owner
        print(f"Owner of vehicle {self.registration_number} updated to {self.owner}.")

# Demonstration script
if __name__ == "__main__":
    # Creating Vehicle instances
    car1 = Vehicle("ABC123", "Sedan", "Alice")
    car2 = Vehicle("XYZ789", "SUV", "Bob")

    # Display initial details
    print(f"Vehicle {car1.registration_number}: Type: {car1.type}, Owner: {car1.owner}")
    print(f"Vehicle {car2.registration_number}: Type: {car2.type}, Owner: {car2.owner}")

    # Updating owner
    car1.update_owner("Charlie")
    car2.update_owner("Diana")

    # Display updated details
    print(f"Vehicle {car1.registration_number}: Type: {car1.type}, Owner: {car1.owner}")
    print(f"Vehicle {car2.registration_number}: Type: {car2.type}, Owner: {car2.owner}")
