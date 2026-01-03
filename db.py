import sqlite3

class BackendDatabase:
    def __init__(self) -> None:    
        self.DB_NAME = "contacts.db"
        self.create_table()

    def get_connection(self):
        return sqlite3.connect(self.DB_NAME, check_same_thread=False)

    def create_table(self):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS contacts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                subject TEXT NOT NULL,
                message TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        conn.commit()
        conn.close()
    
    def insert_contact(self, name: str, email: str, subject: str, message: str):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO contacts (name, email, subject, message)
            VALUES (?, ?, ?, ?)
        """, (name, email, subject, message))
        conn.commit()
        conn.close()
    
    def fetch_all_contacts(self):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM contacts")
        rows = cursor.fetchall()
        conn.close()
        return rows
