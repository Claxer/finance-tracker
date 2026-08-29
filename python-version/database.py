import sqlite3
from pathlib import Path


# Get the folder where this file is located
BASE_DIR = Path(__file__).resolve().parent

# Database file
DATABASE_PATH = BASE_DIR / "finance.db"


def connect_database():
    return sqlite3.connect(DATABASE_PATH)


def create_database():

    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            type TEXT NOT NULL,
            amount REAL NOT NULL,
            category TEXT NOT NULL,
            description TEXT,
            date TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()


def add_transaction(transaction_type, amount, category, description, date):

    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO transactions
        (type, amount, category, description, date)
        VALUES (?, ?, ?, ?, ?)
    """, (
        transaction_type,
        amount,
        category,
        description,
        date
    ))

    connection.commit()
    connection.close()


def get_transactions():

    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, type, amount, category, description, date
        FROM transactions
        ORDER BY date DESC, id DESC
    """)

    transactions = cursor.fetchall()

    connection.close()

    return transactions


def delete_transaction(transaction_id):

    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute("""
        DELETE FROM transactions
        WHERE id = ?
    """, (transaction_id,))

    connection.commit()
    connection.close()


def get_total_income():

    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT COALESCE(SUM(amount), 0)
        FROM transactions
        WHERE type = 'Income'
    """)

    total = cursor.fetchone()[0]

    connection.close()

    return total


def get_total_expenses():

    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT COALESCE(SUM(amount), 0)
        FROM transactions
        WHERE type = 'Expense'
    """)

    total = cursor.fetchone()[0]

    connection.close()

    return total


def get_balance():

    income = get_total_income()
    expenses = get_total_expenses()

    return income - expenses
