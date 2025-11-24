import database

# This module contains the business logic classes
# Fulfills requirement: Classes and functional modules [cite: 21, 57]

class InventoryManager:
    def add_item(self, name, qty, price, threshold):
        """Adds a new item to the database."""
        try:
            database.execute_query(
                "INSERT INTO items (name, quantity, price, threshold) VALUES (?, ?, ?, ?)",
                (name, qty, price, threshold)
            )
            print(f"\n[SUCCESS] Item '{name}' added successfully.")
        except Exception as e:
            print(f"\n[ERROR] Could not add item: {e}")

    def view_inventory(self):
        """Fetches and displays all items, flagging low stock."""
        items = database.fetch_data("SELECT * FROM items")
        
        if not items:
            print("\nInventory is empty.")
            return

        print("\n" + "="*70)
        print(f"{'ID':<5} {'Name':<25} {'Qty':<10} {'Price':<10} {'Status'}")
        print("="*70)
        
        for item in items:
            # item structure: (id, name, quantity, price, threshold)
            item_id, name, qty, price, threshold = item
            
            status = "OK"
            if qty < threshold:
                status = "LOW STOCK! (Reorder)"
            
            print(f"{item_id:<5} {name:<25} {qty:<10} {price:<10} {status}")
        print("="*70)

    def delete_item(self, item_id):
        """Deletes an item by ID."""
        database.execute_query("DELETE FROM items WHERE id = ?", (item_id,))
        print(f"\n[INFO] Item ID {item_id} deleted (if it existed).")

class AuthSystem:
    def login(self, username, password):
        """Validates user credentials."""
        user = database.fetch_data("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
        if user:
            return True
        else:
            return False