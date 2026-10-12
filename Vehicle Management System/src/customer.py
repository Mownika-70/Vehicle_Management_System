
class CustomerPanel:

    def __init__(self, customers, vehicles):
        self.customers = customers
        self.vehicles = vehicles

   
    def register_customer(self, customer_id, customer_name):
        try:
            customer_id = str(customer_id).strip()
            customer_name = str(customer_name).strip()

            if not customer_id:
                print("❌ Customer ID cannot be empty.")
                return

            if not customer_name:
                print("❌ Customer name cannot be empty.")
                return

            if customer_id in self.customers:
                print(f"❌ Customer ID {customer_id} already exists.")
                return

            self.customers[customer_id] = {
                "name": customer_name,
                "rented_vehicle": None
            }

            print(f"✅ Customer {customer_name} registered successfully.")

        except (TypeError, AttributeError) as e:
            print(f"❌ Error registering customer: {e}")

   
    def view_available_vehicles(self):
        try:
            print("\n------ Available Vehicles ------")

            Available = False

            for vehicle_id, vehicle_data in self.vehicles.items():
                if not isinstance(vehicle_data, dict):
                    print(f"❌ Invalid data for vehicle {vehicle_id}.")
                    continue

                if "Available" not in vehicle_data:
                    print(f"❌ Availability information missing for {vehicle_id}.")
                    continue

                if vehicle_data["Available"]:
                    required_keys = ("type", "brand", "rent")

                    if not all(key in vehicle_data for key in required_keys):
                        print(f"❌ Incomplete details for vehicle {vehicle_id}.")
                        continue

                    print(
                        f"ID: {vehicle_id}, "
                        f"Type: {vehicle_data['type']}, "
                        f"Brand: {vehicle_data['brand']}, "
                        f"Rent: ₹{vehicle_data['rent']}"
                    )
                    Available = True

            if not Available:
                print("❌ No valid available vehicles found.")

        except (TypeError, AttributeError) as e:
            print(f"❌ Error displaying vehicles: {e}")

   
    def rent_vehicle(self, customer_id, vehicle_id):
        try:
            customer_id = str(customer_id).strip()
            vehicle_id = str(vehicle_id).strip()

            if not customer_id or not vehicle_id:
                print("❌ Customer ID and vehicle ID cannot be empty.")
                return

            if customer_id not in self.customers:
                print("❌ Customer not found.")
                return

            if vehicle_id not in self.vehicles:
                print("❌ Vehicle ID not found.")
                return

            customer = self.customers[customer_id]
            vehicle = self.vehicles[vehicle_id]

            if not isinstance(customer, dict) or not isinstance(vehicle, dict):
                print("❌ Invalid customer or vehicle data.")
                return

            if "rented_vehicle" not in customer:
                print("❌ Customer rental information is missing.")
                return

            if "Available" not in vehicle:
                print("❌ Vehicle availability information is missing.")
                return

            if customer["rented_vehicle"] is not None:
                print("❌ Customer has already rented a vehicle.")
                return

            if not vehicle["Available"]:
                print("❌ Vehicle is already rented.")
                return

            if "brand" not in vehicle or "name" not in customer:
                print("❌ Customer or vehicle details are incomplete.")
                return

            customer["rented_vehicle"] = vehicle_id
            vehicle["Available"] = False

            print(
                f"✅ Vehicle {vehicle['brand']} rented to "
                f"customer {customer['name']} successfully."
            )

        except (TypeError, AttributeError) as e:
            print(f"❌ Error renting vehicle: {e}")

    # 4. Return vehicle
    def return_vehicle(self, customer_id):
        try:
            customer_id = str(customer_id).strip()

            if not customer_id:
                print("❌ Customer ID cannot be empty.")
                return

            if customer_id not in self.customers:
                print("❌ Customer not found.")
                return

            customer = self.customers[customer_id]

            if not isinstance(customer, dict):
                print("❌ Invalid customer data.")
                return

            if "rented_vehicle" not in customer:
                print("❌ Customer rental information is missing.")
                return

            rented = customer["rented_vehicle"]

            if rented is None:
                print("❌ This customer has not rented any vehicle.")
                return

            if rented not in self.vehicles:
                print("❌ Rented vehicle not found in inventory.")
                return

            vehicle = self.vehicles[rented]

            if not isinstance(vehicle, dict):
                print("❌ Invalid vehicle data.")
                return

            if "Available" not in vehicle or "brand" not in vehicle:
                print("❌ Vehicle information is incomplete.")
                return

            if vehicle["Available"]:
                print("❌ Vehicle is already marked as available.")
                return

            vehicle["Available"] = True
            customer["rented_vehicle"] = None

            print(
                f"✅ Vehicle {vehicle['brand']} returned successfully "
                f"by customer {customer['name']}."
            )

        except (TypeError, AttributeError) as e:
            print(f"❌ Error returning vehicle: {e}")
