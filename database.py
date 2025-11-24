import sqlite3

# This module handles all direct interactions with the database
# Fulfills requirement: Data storage and persistence [cite: 76]

def connect_db():
    """Initializes the database and creates tables if they don't exist."""
    conn = sqlite3.connect("inventory.db")
    cursor = conn.cursor()
    
    # Create Users Table for Authentication
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        username TEXT PRIMARY KEY,
        password TEXT NOT NULL
    )
    ''')
    
    # Create Items Table for Inventory
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS items (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        quantity INTEGER NOT NULL,
        price REAL NOT NULL,
        threshold INTEGER NOT NULL
    )
    ''')
    
    # Create a default admin user (Username: admin, Password: admin123)
    cursor.execute("INSERT OR IGNORE INTO users (username, password) VALUES (?, ?)", 
                   ("admin", "admin123"))
    
    conn.commit()
    conn.close()

def execute_query(query, params=()):
    """Executes a modification query (INSERT, UPDATE, DELETE)."""
    conn = sqlite3.connect("inventory.db")
    cursor = conn.cursor()
    cursor.execute(query, params)
    conn.commit()
    conn.close()

def fetch_data(query, params=()):
    """Executes a read query (SELECT) and returns data."""
    conn = sqlite3.connect("inventory.db")
    cursor = conn.cursor()
    cursor.execute(query, params)
    rows = cursor.fetchall()
    conn.close()
    return rows