# database.py

import sqlite3
import os
from datetime import datetime


# =========================================================
# DATABASE LOCATION
# =========================================================

BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

DATABASE_NAME = os.path.join(
    BASE_DIR,
    "finance.db"
)


# =========================================================
# DATABASE CONNECTION
# =========================================================

def get_connection():

    return sqlite3.connect(
        DATABASE_NAME
    )


# =========================================================
# CREATE DATABASE
# =========================================================

def create_database():

    conn = get_connection()
    cursor = conn.cursor()

    # -----------------------------------------------------
    # TRANSACTIONS
    # -----------------------------------------------------

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS transactions (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            type TEXT NOT NULL,

            category TEXT NOT NULL,

            amount REAL NOT NULL,

            description TEXT DEFAULT '',

            date TEXT NOT NULL
        )
    """)

    # -----------------------------------------------------
    # BUDGETS
    # -----------------------------------------------------

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS budgets (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            category TEXT NOT NULL,

            amount REAL NOT NULL,

            month TEXT NOT NULL
        )
    """)

    # -----------------------------------------------------
    # SAVINGS GOALS
    # -----------------------------------------------------

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS savings_goals (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            name TEXT NOT NULL,

            target REAL NOT NULL,

            saved REAL DEFAULT 0,

            target_date TEXT DEFAULT ''
        )
    """)

    conn.commit()

    conn.close()


# =========================================================
# TRANSACTION FUNCTIONS
# =========================================================

def add_transaction(
    transaction_type,
    category,
    amount,
    description="",
    date=None
):

    if date is None:

        date = datetime.now().strftime(
            "%Y-%m-%d"
        )

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO transactions
        (
            type,
            category,
            amount,
            description,
            date
        )
        VALUES (?, ?, ?, ?, ?)
    """, (
        transaction_type,
        category,
        amount,
        description,
        date
    ))

    conn.commit()
    conn.close()


# =========================================================
# GET ALL TRANSACTIONS
# =========================================================

def get_transactions():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            id,
            type,
            category,
            amount,
            description,
            date

        FROM transactions

        ORDER BY
            date DESC,
            id DESC
    """)

    transactions = cursor.fetchall()

    conn.close()

    return transactions


# =========================================================
# GET SINGLE TRANSACTION
# =========================================================

def get_transaction(transaction_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            id,
            type,
            category,
            amount,
            description,
            date

        FROM transactions

        WHERE id = ?
    """, (
        transaction_id,
    ))

    transaction = cursor.fetchone()

    conn.close()

    return transaction


# =========================================================
# UPDATE TRANSACTION
# =========================================================

def update_transaction(
    transaction_id,
    transaction_type,
    category,
    amount,
    description,
    date
):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE transactions

        SET
            type = ?,
            category = ?,
            amount = ?,
            description = ?,
            date = ?

        WHERE id = ?
    """, (
        transaction_type,
        category,
        amount,
        description,
        date,
        transaction_id
    ))

    conn.commit()
    conn.close()


# =========================================================
# DELETE TRANSACTION
# =========================================================

def delete_transaction(
    transaction_id
):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        DELETE FROM transactions

        WHERE id = ?
    """, (
        transaction_id,
    ))

    conn.commit()
    conn.close()


# =========================================================
# TOTALS
# =========================================================

def get_totals():

    conn = get_connection()
    cursor = conn.cursor()

    # -----------------------------------------------------
    # TOTAL INCOME
    # -----------------------------------------------------

    cursor.execute("""
        SELECT
            COALESCE(
                SUM(amount),
                0
            )

        FROM transactions

        WHERE type = 'Income'
    """)

    income = cursor.fetchone()[0]

    # -----------------------------------------------------
    # TOTAL EXPENSES
    # -----------------------------------------------------

    cursor.execute("""
        SELECT
            COALESCE(
                SUM(amount),
                0
            )

        FROM transactions

        WHERE type = 'Expense'
    """)

    expenses = cursor.fetchone()[0]

    conn.close()

    # -----------------------------------------------------
    # BALANCE
    # -----------------------------------------------------

    balance = income - expenses

    return (
        income,
        expenses,
        balance
    )


# =========================================================
# BUDGET FUNCTIONS
# =========================================================

def add_budget(
    category,
    amount,
    month
):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO budgets
        (
            category,
            amount,
            month
        )

        VALUES (?, ?, ?)
    """, (
        category,
        amount,
        month
    ))

    conn.commit()
    conn.close()


# =========================================================
# GET BUDGETS
# =========================================================

def get_budgets():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            id,
            category,
            amount,
            month

        FROM budgets

        ORDER BY
            month DESC,
            id DESC
    """)

    budgets = cursor.fetchall()

    conn.close()

    return budgets


# =========================================================
# SAVINGS FUNCTIONS
# =========================================================

def add_savings_goal(
    name,
    target,
    saved=0,
    target_date=""
):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO savings_goals
        (
            name,
            target,
            saved,
            target_date
        )

        VALUES (?, ?, ?, ?)
    """, (
        name,
        target,
        saved,
        target_date
    ))

    conn.commit()
    conn.close()


# =========================================================
# GET SAVINGS GOALS
# =========================================================

def get_savings_goals():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            id,
            name,
            target,
            saved,
            target_date

        FROM savings_goals

        ORDER BY
            id DESC
    """)

    goals = cursor.fetchall()

    conn.close()

    return goals


# =========================================================
# UPDATE SAVINGS GOAL
# =========================================================

def update_savings_goal(
    goal_id,
    name,
    target,
    saved,
    target_date
):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE savings_goals

        SET
            name = ?,
            target = ?,
            saved = ?,
            target_date = ?

        WHERE id = ?
    """, (
        name,
        target,
        saved,
        target_date,
        goal_id
    ))

    conn.commit()
    conn.close()


# =========================================================
# DELETE SAVINGS GOAL
# =========================================================

def delete_savings_goal(
    goal_id
):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        DELETE FROM savings_goals

        WHERE id = ?
    """, (
        goal_id,
    ))

    conn.commit()
    conn.close()


# =========================================================
# MONTHLY TOTALS
# =========================================================

def get_monthly_totals(
    month=None
):

    if month is None:

        month = datetime.now().strftime(
            "%Y-%m"
        )

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            COALESCE(
                SUM(
                    CASE
                        WHEN type = 'Income'
                        THEN amount
                        ELSE 0
                    END
                ),
                0
            ),

            COALESCE(
                SUM(
                    CASE
                        WHEN type = 'Expense'
                        THEN amount
                        ELSE 0
                    END
                ),
                0
            )

        FROM transactions

        WHERE date LIKE ?
    """, (
        f"{month}%",
    ))

    result = cursor.fetchone()

    conn.close()

    income = result[0]
    expenses = result[1]

    balance = income - expenses

    return (
        income,
        expenses,
        balance
    )


# =========================================================
# CATEGORY EXPENSES
# =========================================================

def get_expenses_by_category():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            category,
            SUM(amount)

        FROM transactions

        WHERE type = 'Expense'

        GROUP BY category

        ORDER BY SUM(amount) DESC
    """)

    results = cursor.fetchall()

    conn.close()

    return results


# =========================================================
# CATEGORY INCOME
# =========================================================

def get_income_by_category():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            category,
            SUM(amount)

        FROM transactions

        WHERE type = 'Income'

        GROUP BY category

        ORDER BY SUM(amount) DESC
    """)

    results = cursor.fetchall()

    conn.close()

    return results


# =========================================================
# RECENT TRANSACTIONS
# =========================================================

def get_recent_transactions(
    limit=5
):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            id,
            type,
            category,
            amount,
            description,
            date

        FROM transactions

        ORDER BY
            date DESC,
            id DESC

        LIMIT ?
    """, (
        limit,
    ))

    transactions = cursor.fetchall()

    conn.close()

    return transactions
