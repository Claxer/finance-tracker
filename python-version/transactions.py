import customtkinter as ctk
from tkinter import messagebox
from datetime import date

import database


class TransactionsPage(ctk.CTkFrame):

    def __init__(self, parent, refresh_dashboard=None):
        super().__init__(
            parent,
            corner_radius=0,
            fg_color="transparent"
        )

        self.refresh_dashboard = refresh_dashboard

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(3, weight=1)

        self.create_header()
        self.create_form()
        self.create_filters()
        self.create_transaction_list()

        self.load_transactions()

    # =========================================================
    # HEADER
    # =========================================================

    def create_header(self):

        title = ctk.CTkLabel(
            self,
            text="Transactions",
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
    # ADD TRANSACTION FORM
    # =========================================================

    def create_form(self):

        self.form_frame = ctk.CTkFrame(
            self,
            corner_radius=15
        )

        self.form_frame.grid(
            row=1,
            column=0,
            sticky="ew",
            padx=30,
            pady=(0, 15)
        )

        self.form_frame.grid_columnconfigure(
            (0, 1, 2, 3, 4),
            weight=1
        )

        # Type

        type_label = ctk.CTkLabel(
            self.form_frame,
            text="Type"
        )

        type_label.grid(
            row=0,
            column=0,
            padx=10,
            pady=(15, 5)
        )

        self.type_menu = ctk.CTkOptionMenu(
            self.form_frame,
            values=["Income", "Expense"]
        )

        self.type_menu.grid(
            row=1,
            column=0,
            padx=10,
            pady=(0, 15),
            sticky="ew"
        )

        # Amount

        amount_label = ctk.CTkLabel(
            self.form_frame,
            text="Amount"
        )

        amount_label.grid(
            row=0,
            column=1,
            padx=10,
            pady=(15, 5)
        )

        self.amount_entry = ctk.CTkEntry(
            self.form_frame,
            placeholder_text="0.00"
        )

        self.amount_entry.grid(
            row=1,
            column=1,
            padx=10,
            pady=(0, 15),
            sticky="ew"
        )

        # Category

        category_label = ctk.CTkLabel(
            self.form_frame,
            text="Category"
        )

        category_label.grid(
            row=0,
            column=2,
            padx=10,
            pady=(15, 5)
        )

        self.category_menu = ctk.CTkOptionMenu(
            self.form_frame,
            values=[
                "Food",
                "Transportation",
                "School",
                "Bills",
                "Entertainment",
                "Shopping",
                "Salary",
                "Allowance",
                "Other"
            ]
        )

        self.category_menu.grid(
            row=1,
            column=2,
            padx=10,
            pady=(0, 15),
            sticky="ew"
        )

        # Date

        date_label = ctk.CTkLabel(
            self.form_frame,
            text="Date"
        )

        date_label.grid(
            row=0,
            column=3,
            padx=10,
            pady=(15, 5)
        )

        self.date_entry = ctk.CTkEntry(
            self.form_frame
        )

        self.date_entry.insert(
            0,
            str(date.today())
        )

        self.date_entry.grid(
            row=1,
            column=3,
            padx=10,
            pady=(0, 15),
            sticky="ew"
        )

        # Add button

        self.add_button = ctk.CTkButton(
            self.form_frame,
            text="Add Transaction",
            height=40,
            command=self.add_transaction
        )

        self.add_button.grid(
            row=1,
            column=4,
            padx=10,
            pady=(0, 15),
            sticky="ew"
        )

        # Description

        description_label = ctk.CTkLabel(
            self.form_frame,
            text="Description"
        )

        description_label.grid(
            row=2,
            column=0,
            padx=10,
            pady=(5, 5)
        )

        self.description_entry = ctk.CTkEntry(
            self.form_frame,
            placeholder_text="Optional description"
        )

        self.description_entry.grid(
            row=3,
            column=0,
            columnspan=4,
            padx=10,
            pady=(0, 15),
            sticky="ew"
        )

    # =========================================================
    # FILTERS
    # =========================================================

    def create_filters(self):

        self.filter_frame = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        self.filter_frame.grid(
            row=2,
            column=0,
            sticky="ew",
            padx=30,
            pady=(0, 15)
        )

        self.filter_frame.grid_columnconfigure(
            0,
            weight=1
        )

        # Search

        self.search_entry = ctk.CTkEntry(
            self.filter_frame,
            placeholder_text="Search transactions..."
        )

        self.search_entry.grid(
            row=0,
            column=0,
            padx=(0, 10),
            sticky="ew"
        )

        self.search_entry.bind(
            "<KeyRelease>",
            lambda event: self.load_transactions()
        )

        # Type filter

        self.type_filter = ctk.CTkOptionMenu(
            self.filter_frame,
            values=[
                "All Types",
                "Income",
                "Expense"
            ],
            command=lambda value: self.load_transactions()
        )

        self.type_filter.grid(
            row=0,
            column=1,
            padx=5
        )

        # Category filter

        self.category_filter = ctk.CTkOptionMenu(
            self.filter_frame,
            values=[
                "All Categories",
                "Food",
                "Transportation",
                "School",
                "Bills",
                "Entertainment",
                "Shopping",
                "Salary",
                "Allowance",
                "Other"
            ],
            command=lambda value: self.load_transactions()
        )

        self.category_filter.grid(
            row=0,
            column=2,
            padx=5
        )

        # Refresh

        refresh_button = ctk.CTkButton(
            self.filter_frame,
            text="Refresh",
            width=100,
            command=self.load_transactions
        )

        refresh_button.grid(
            row=0,
            column=3,
            padx=(10, 0)
        )

    # =========================================================
    # TRANSACTION LIST
    # =========================================================

    def create_transaction_list(self):

        self.list_frame = ctk.CTkScrollableFrame(
            self,
            corner_radius=15
        )

        self.list_frame.grid(
            row=3,
            column=0,
            sticky="nsew",
            padx=30,
            pady=(0, 30)
        )

    # =========================================================
    # ADD TRANSACTION
    # =========================================================

    def add_transaction(self):

        transaction_type = self.type_menu.get()
        amount_text = self.amount_entry.get().strip()
        category = self.category_menu.get()
        description = self.description_entry.get().strip()
        transaction_date = self.date_entry.get().strip()

        if not amount_text:

            messagebox.showerror(
                "Invalid Amount",
                "Please enter an amount."
            )

            return

        try:

            amount = float(amount_text)

        except ValueError:

            messagebox.showerror(
                "Invalid Amount",
                "Please enter a valid number."
            )

            return

        if amount <= 0:

            messagebox.showerror(
                "Invalid Amount",
                "Amount must be greater than zero."
            )

            return

        if not transaction_date:

            messagebox.showerror(
                "Invalid Date",
                "Please enter a date."
            )

            return

        database.add_transaction(
            transaction_type,
            amount,
            category,
            description,
            transaction_date
        )

        messagebox.showinfo(
            "Success",
            "Transaction added successfully."
        )

        self.amount_entry.delete(
            0,
            "end"
        )

        self.description_entry.delete(
            0,
            "end"
        )

        self.load_transactions()

        if self.refresh_dashboard:
            self.refresh_dashboard()

    # =========================================================
    # LOAD TRANSACTIONS
    # =========================================================

    def load_transactions(self):

        for widget in self.list_frame.winfo_children():
            widget.destroy()

        transactions = database.get_transactions()

        # Search filter

        search_text = self.search_entry.get().lower().strip()

        selected_type = self.type_filter.get()

        selected_category = self.category_filter.get()

        filtered_transactions = []

        for transaction in transactions:

            (
                transaction_id,
                transaction_type,
                amount,
                category,
                description,
                transaction_date
            ) = transaction

            description = description or ""

            # Search

            searchable_text = (
                f"{transaction_type} "
                f"{amount} "
                f"{category} "
                f"{description} "
                f"{transaction_date}"
            ).lower()

            if search_text not in searchable_text:
                continue

            # Type

            if (
                selected_type != "All Types"
                and transaction_type != selected_type
            ):
                continue

            # Category

            if (
                selected_category != "All Categories"
                and category != selected_category
            ):
                continue

            filtered_transactions.append(
                transaction
            )

        if not filtered_transactions:

            label = ctk.CTkLabel(
                self.list_frame,
                text="No matching transactions.",
                font=ctk.CTkFont(size=16)
            )

            label.pack(
                pady=30
            )

            return

        # Header

        header = ctk.CTkFrame(
            self.list_frame
        )

        header.pack(
            fill="x",
            padx=5,
            pady=(5, 10)
        )

        headers = [
            "Type",
            "Amount",
            "Category",
            "Description",
            "Date",
            "Action"
        ]

        for column, text in enumerate(headers):

            label = ctk.CTkLabel(
                header,
                text=text,
                font=ctk.CTkFont(
                    weight="bold"
                )
            )

            label.grid(
                row=0,
                column=column,
                padx=10,
                pady=10,
                sticky="w"
            )

        # Rows

        for transaction in filtered_transactions:

            (
                transaction_id,
                transaction_type,
                amount,
                category,
                description,
                transaction_date
            ) = transaction

            row = ctk.CTkFrame(
                self.list_frame
            )

            row.pack(
                fill="x",
                padx=5,
                pady=4
            )

            values = [
                transaction_type,
                f"₱{amount:,.2f}",
                category,
                description if description else "-",
                transaction_date
            ]

            for column, value in enumerate(values):

                label = ctk.CTkLabel(
                    row,
                    text=value
                )

                label.grid(
                    row=0,
                    column=column,
                    padx=10,
                    pady=10,
                    sticky="w"
                )

            delete_button = ctk.CTkButton(
                row,
                text="Delete",
                width=70,
                command=lambda id=transaction_id:
                    self.delete_transaction(id)
            )

            delete_button.grid(
                row=0,
                column=5,
                padx=10,
                pady=5
            )

    # =========================================================
    # DELETE TRANSACTION
    # =========================================================

    def delete_transaction(self, transaction_id):

        confirm = messagebox.askyesno(
            "Delete Transaction",
            "Are you sure you want to delete this transaction?"
        )

        if not confirm:
            return

        database.delete_transaction(
            transaction_id
        )

        self.load_transactions()

        if self.refresh_dashboard:
            self.refresh_dashboard()
