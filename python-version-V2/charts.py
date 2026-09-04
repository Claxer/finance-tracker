# charts.py

import customtkinter as ctk
import matplotlib.pyplot as plt

from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg
)

from database import get_transactions
from theme import COLORS


def show_expense_chart(parent):

    transactions = get_transactions()

    expenses = {}

    for transaction in transactions:

        _, transaction_type, category, amount, _, _ = transaction

        if transaction_type == "Expense":

            expenses[category] = (
                expenses.get(category, 0)
                + amount
            )

    if not expenses:

        dialog = ctk.CTkToplevel(parent)

        dialog.title("Expense Chart")
        dialog.geometry("350x160")

        ctk.CTkLabel(
            dialog,
            text="No expense data available yet.",
            font=("Arial", 13)
        ).pack(
            pady=35
        )

        ctk.CTkButton(
            dialog,
            text="OK",
            width=100,
            command=dialog.destroy
        ).pack()

        return

    window = ctk.CTkToplevel(parent)

    window.title("Expense Breakdown")
    window.geometry("850x600")

    window.configure(
        fg_color=(
            COLORS["background"],
            COLORS["dark_background"]
        )
    )

    figure, axis = plt.subplots(
        figsize=(8, 5)
    )

    labels = list(expenses.keys())
    values = list(expenses.values())

    axis.pie(
        values,
        labels=labels,
        autopct="%1.1f%%",
        startangle=90
    )

    axis.set_title(
        "Expense Breakdown"
    )

    canvas = FigureCanvasTkAgg(
        figure,
        master=window
    )

    canvas.draw()

    canvas.get_tk_widget().pack(
        fill="both",
        expand=True,
        padx=20,
        pady=20
    )

    plt.close(figure)
