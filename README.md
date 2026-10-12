# Mownika Rentals 🚗

A Python-based Vehicle Rental Management System that helps manage vehicles, customer registrations, rentals, and returns through a simple menu-driven interface.

# Features

 **Admin Panel**
  - Add new vehicles
  - View vehicle inventory
  - Remove available vehicles
  - Prevent duplicate vehicle numbers
 **Customer Panel**
  - Register customers
  - View available vehicles
  - Rent vehicles
  - Return rented vehicles
 **Data Persistence**
  - Save vehicle and customer records in a JSON file
  - Preserve rental status when the application restarts
 **Input Validation**
  - Handle duplicate IDs and invalid inputs
  - Validate vehicle availability before renting or returning

## Technologies Used

 Python
 JSON
 Object-Oriented Programming (OOP)

## Project Structure

```text
Mownika-Rentals/
├── main.py
├── data.json
├── src/
│   ├── __init__.py
│   ├── admin.py
│   └── customer.py
└── README.md
```

## How to Run

1. Install Python 3.
2. Clone or download this repository.
3. Open a terminal in the project folder.
4. Run:

```bash
python main.py
```

## Data Storage

Vehicle information, customer registrations, and rental status are stored in `data.json` so the records remain available after restarting the application.

**Note:** Use sample data in the public repository. Do not publish real customer information.

## Future Enhancements
 SQLite database integration
 Rental billing and receipts
 Rental history
 Improved reporting and search

## Author
Mownika V

Python Project — Vehicle Rental Management System
