import customtkinter as ctk
import sqlite3
from collections import defaultdict
from datetime import datetime

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import database


class ChartsPage(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(
            parent,
            corner_radius=0,
            fg_color="transparent"
        )

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.create_header()
        self.create_chart_area()

    # =========================================================
    # HEADER
    # =========================================================

    def create_header(self):

        title = ctk.CTkLabel(
            self,
            text="Financial Charts",
            font=ctk.CTkFont(
                size=32,
                weight="bold"
            )
        )

        title.grid(
            row=0,
            column=0,
            sticky="w",
            padx=30,
            pady=(30, 20)
        )

    # =========================================================
    # CHART AREA
    # =========================================================

    def create_chart_area(self):

        self.chart_frame = ctk.CTkScrollableFrame(
            self,
            corner_radius=15
        )

        self.chart_frame.grid(
            row=1,
            column=0,
            sticky="nsew",
            padx=30,
            pady=(0, 30)
        )

        self.create_income_expense_chart()
        self.create_category_chart()
        self.create_monthly_chart()

    # =========================================================
    # INCOME VS EXPENSES
    # =========================================================

    def create_income_expense_chart(self):

        income = database.get_total_income()
        expenses = database.get_total_expenses()

        figure = Figure(
            figsize=(7, 4),
            dpi=100
        )

        axis = figure.add_subplot(111)

        axis.bar(
            ["Income", "Expenses"],
            [income, expenses]
        )

        axis.set_title(
            "Income vs. Expenses"
        )

        axis.set_ylabel(
            "Amount (₱)"
        )

        axis.ticklabel_format(
            style="plain",
            axis="y"
        )

        figure.tight_layout()

        canvas = FigureCanvasTkAgg(
            figure,
            master=self.chart_frame
        )

        canvas.draw()

        canvas.get_tk_widget().pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )

    # =========================================================
    # SPENDING BY CATEGORY
    # =========================================================

    def create_category_chart(self):

        connection = database.connect_database()
        cursor = connection.cursor()

        cursor.execute("""
            SELECT category, SUM(amount)
            FROM transactions
            WHERE type = 'Expense'
            GROUP BY category
            ORDER BY SUM(amount) DESC
        """)

        results = cursor.fetchall()

        connection.close()

        if not results:
            return

        categories = [
            row[0]
            for row in results
        ]

        amounts = [
            row[1]
            for row in results
        ]

        figure = Figure(
            figsize=(7, 4),
            dpi=100
        )

        axis = figure.add_subplot(111)

        axis.pie(
            amounts,
            labels=categories,
            autopct="%1.1f%%"
        )

        axis.set_title(
            "Expenses by Category"
        )

        figure.tight_layout()

        canvas = FigureCanvasTkAgg(
            figure,
            master=self.chart_frame
        )

        canvas.draw()

        canvas.get_tk_widget().pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )

    # =========================================================
    # MONTHLY EXPENSES
    # =========================================================

    def create_monthly_chart(self):

        connection = database.connect_database()
        cursor = connection.cursor()

        cursor.execute("""
            SELECT date, amount
            FROM transactions
            WHERE type = 'Expense'
            ORDER BY date
        """)

        results = cursor.fetchall()

        connection.close()

        if not results:
            return

        monthly_totals = defaultdict(float)

        for transaction_date, amount in results:

            try:

                parsed_date = datetime.strptime(
                    transaction_date,
                    "%Y-%m-%d"
                )

                month = parsed_date.strftime(
                    "%Y-%m"
                )

                monthly_totals[month] += amount

            except ValueError:

                continue

        if not monthly_totals:
            return

        months = list(
            monthly_totals.keys()
        )

        amounts = list(
            monthly_totals.values()
        )

        figure = Figure(
            figsize=(7, 4),
            dpi=100
        )

        axis = figure.add_subplot(111)

        axis.plot(
            months,
            amounts,
            marker="o"
        )

        axis.set_title(
            "Monthly Expenses"
        )

        axis.set_xlabel(
            "Month"
        )

        axis.set_ylabel(
            "Expenses (₱)"
        )

        axis.tick_params(
            axis="x",
            rotation=45
        )

        figure.tight_layout()

        canvas = FigureCanvasTkAgg(
            figure,
            master=self.chart_frame
        )

        canvas.draw()

        canvas.get_tk_widget().pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )
