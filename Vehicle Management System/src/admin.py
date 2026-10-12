
import math

class AdminPanel:

    def __init__(self, vehicles):
        self.vehicles = vehicles

    def add_vehicle(self, vehicle_number, vehicle_brand, vehicle_type, vehicle_rent):

        vehicle_number = str(vehicle_number).strip()

        if not vehicle_number:
            print("❌ Vehicle number cannot be empty.")
            return

        if vehicle_number in self.vehicles:
            print(f"❌ Vehicle number {vehicle_number} already exists.")
            return

        vehicle_brand = str(vehicle_brand).strip()

        if not vehicle_brand:
            print("❌ Vehicle brand cannot be empty.")
            return

        vehicle_type = str(vehicle_type).strip()

        if not vehicle_type:
            print("❌ Vehicle type cannot be empty.")
            return

        try:
            vehicle_rent = float(vehicle_rent)

        except (ValueError, TypeError):
            print("❌ Invalid rent! Please enter a valid number.")
            return

        if not math.isfinite(vehicle_rent) or vehicle_rent <= 0:
            print("❌ Rent must be a positive, finite number.")
            return

        self.vehicles[vehicle_number] = {
            'number': vehicle_number,
            'brand': vehicle_brand,
            'type': vehicle_type,
            'rent': vehicle_rent,
            'Available': True
        }

        print(f"✅ Vehicle {vehicle_brand} added successfully!")

    def view_inventory(self):

        print("\n------ Vehicle Inventory ------")

        if not self.vehicles:
            print("❌ No vehicles found in inventory.")
            return

        for vehicle_number, vehicle_data in self.vehicles.items():
            print(
                f"Number: {vehicle_number}, "
                f"Brand: {vehicle_data['brand']}, "
                f"Type: {vehicle_data['type']}, "
                f"Rent: ₹{vehicle_data['rent']:.2f}, "
                f"Available: {vehicle_data['Available']}"
            )

    
    def remove_vehicle(self, vehicle_number):
        vehicle_number = str(vehicle_number).strip()

        if not vehicle_number:
            print("❌ Vehicle number cannot be empty.")
            return False

        if vehicle_number not in self.vehicles:
            print("❌ Vehicle not found.")
            return False

        vehicle = self.vehicles[vehicle_number]

        # Prevent removal of a currently rented vehicle
        if vehicle.get("Available", True) is False:
            print("❌ Cannot remove a rented vehicle. Return it first.")
            return False

        del self.vehicles[vehicle_number]
        print(f"✅ Vehicle {vehicle_number} removed successfully!")
        return True



if __name__ == '__main__':
    import math

    vehicles = {}
    admin_panel = AdminPanel(vehicles)

    admin_panel.add_vehicle('KA01VE7662', 'Honda', 'Car', 2000)
    admin_panel.add_vehicle('KA02AB1234', 'Royal Enfield', 'Bike', 1000)

    admin_panel.view_inventory()
