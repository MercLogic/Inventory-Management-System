import database
from logic import InventoryManager, AuthSystem
import sys

# This is the entry point of the application
# Fulfills requirement: Clear input/output structure [cite: 22]

def main():
    # 1. Initialize the Database
    database.connect_db()
    
    auth = AuthSystem()
    manager = InventoryManager()
    
    print("\n" + "*"*40)
    print("  SMART INVENTORY MANAGEMENT SYSTEM  ")
    print("*"*40)
    
    # 2. Login Screen
    # Default credentials -> User: admin, Pass: admin123
    user = input("Enter Username: ")
    pwd = input("Enter Password: ")
    
    if not auth.login(user, pwd):
        print("\n[ACCESS DENIED] Invalid Username or Password.")
        print("Hint: Default user is 'admin' with password 'admin123'")
        sys.exit()

    print("\n[ACCESS GRANTED] Welcome, Admin.")

    # 3. Main Menu Loop
    while True:
        print("\n--- MAIN MENU ---")
        print("1. View Inventory & Check Alerts")
        print("2. Add New Item")
        print("3. Delete Item")
        print("4. Exit")
        
        choice = input("\nEnter your choice (1-4): ")
        
        if choice == '1':
            manager.view_inventory()
        elif choice == '2':
            try:
                n = input("Item Name: ")
                q = int(input("Quantity: "))
                p = float(input("Price: "))
                t = int(input("Low Stock Alert Threshold: "))
                manager.add_item(n, q, p, t)
            except ValueError:
                print("\n[ERROR] Please enter valid numbers for Quantity, Price, and Threshold.")
        elif choice == '3':
            try:
                i = int(input("Enter Item ID to delete: "))
                manager.delete_item(i)
            except ValueError:
                print("\n[ERROR] Please enter a valid numeric ID.")
        elif choice == '4':
            print("\nExiting System. Goodbye!")
            break
        else:
            print("\n[INVALID] Please choose an option between 1 and 4.")

if __name__ == "__main__":
    main()
    
