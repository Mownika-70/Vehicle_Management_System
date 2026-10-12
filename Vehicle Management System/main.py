
import json
from pathlib import Path

from src.admin import AdminPanel
from src.customer import CustomerPanel


DATA_FILE = Path(__file__).resolve().parent / "data.json"


def load_data():
    """Load saved vehicles and customers."""
    if not DATA_FILE.exists():
        return {}, {}

    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            data = json.load(file)

        if not isinstance(data, dict):
            raise ValueError("Invalid data file format.")

        vehicles = data.get("vehicles", {})
        customers = data.get("customers", {})

        if not isinstance(vehicles, dict) or not isinstance(customers, dict):
            raise ValueError("Vehicles and customers must be dictionaries.")

        return vehicles, customers

    except (json.JSONDecodeError, OSError, ValueError) as error:
        raise RuntimeError(
            f"Could not load saved data: {error}. "
            "Check data.json before restarting."
        ) from error


def save_data(vehicles, customers):
    """Save all data permanently to JSON."""
    temporary_file = DATA_FILE.with_suffix(".tmp")

    try:
        with temporary_file.open("w", encoding="utf-8") as file:
            json.dump(
                {"vehicles": vehicles, "customers": customers},
                file,
                indent=4,
                ensure_ascii=False,
                allow_nan=False
            )

        temporary_file.replace(DATA_FILE)
        return True

    except (OSError, TypeError, ValueError) as error:
        print(f"❌ Could not save data: {error}")
        print("⚠️ Your latest changes may not be saved.")
        return False


def main_display():
    print("\n==== Welcome to Mownika Rentals ====")
    print("1. Admin panel")
    print("2. Customer panel")
    print("3. Exit application")


def admin_display():
    print("\n------------------------------")
    print("Welcome to Admin Panel")
    print("------------------------------")
    print("1. Add a vehicle")
    print("2. View inventory")
    print("3. Remove a vehicle")
    print("4. Exit admin panel")


def customer_display():
    print("\n------------------------------")
    print("Welcome to Customer Panel")
    print("------------------------------")
    print("1. Register customer")
    print("2. View available vehicles")
    print("3. Rent vehicle")
    print("4. Return a vehicle")
    print("5. Exit customer panel")


def main():
    try:
        vehicles, customers = load_data()
    except RuntimeError as error:
        print(f"❌ {error}")
        return

    admin = AdminPanel(vehicles)
    customer_panel = CustomerPanel(customers, vehicles)

    print(f"Loaded {len(vehicles)} vehicle(s) and "
          f"{len(customers)} customer(s).")

    while True:
        main_display()
        user_choice = input("Enter your choice (1/2/3): ").strip()

        if user_choice == "3":
            print("Thank you for using Mownika Rentals!")
            break

        elif user_choice == "1":
            while True:
                admin_display()
                choice = input("Enter your choice: ").strip()

                if choice == "4":
                    print("Exiting Admin Panel!")
                    break

                elif choice == "1":
                    print("\nAdding a new vehicle")
                    number = input("Enter vehicle number: ").strip()
                    brand = input("Enter vehicle brand: ").strip()
                    vehicle_type = input("Enter vehicle type: ").strip()
                    rent = input("Enter vehicle rent: ").strip()

                    admin.add_vehicle(number, brand, vehicle_type, rent)
                    save_data(vehicles, customers)

                elif choice == "2":
                    admin.view_inventory()

                elif choice == "3":
                    vehicle_number = input("Enter vehicle number to remove: ").strip()
                    admin.remove_vehicle(vehicle_number)
                    save_data(vehicles, customers)

                else:
                    print("❌ Invalid choice. Choose 1, 2, 3 or 4.")

        elif user_choice == "2":
            while True:
                customer_display()
                choice = input("Enter your choice: ").strip()

                if choice == "5":
                    print("Exiting Customer Panel!")
                    break

                elif choice == "1":
                    customer_id = input("Enter customer ID: ").strip()
                    name = input("Enter customer name: ").strip()

                    customer_panel.register_customer(customer_id, name)
                    save_data(vehicles, customers)

                elif choice == "2":
                    customer_panel.view_available_vehicles()

                elif choice == "3":
                    customer_id = input("Enter customer ID: ").strip()
                    vehicle_id = input("Enter vehicle ID: ").strip()

                    customer_panel.rent_vehicle(customer_id, vehicle_id)
                    save_data(vehicles, customers)

                elif choice == "4":
                    customer_id = input("Enter customer ID: ").strip()

                    customer_panel.return_vehicle(customer_id)
                    save_data(vehicles, customers)

                else:
                    print("❌ Invalid choice. Choose 1, 2, 3, 4, or 5.")

        else:
            print("❌ Invalid choice. Choose 1, 2, or 3.")

    print("Application closed.")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nApplication closed safely.")
