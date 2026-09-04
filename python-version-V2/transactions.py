# transactions.py

import customtkinter as ctk
from datetime import datetime

from database import (
    add_transaction,
    get_transactions,
    get_transaction,
    update_transaction,
    delete_transaction
)

from theme import COLORS


CATEGORIES = [
    "Food",
    "Transportation",
    "Bills",
    "Shopping",
    "Entertainment",
    "Education",
    "Health",
    "Housing",
    "Salary",
    "Allowance",
    "Freelance",
    "Investment",
    "Other"
]


class TransactionsPage(ctk.CTkFrame):

    def __init__(self, parent, app):

        super().__init__(
            parent,
            fg_color="transparent"
        )

        self.app = app
        self.editing_id = None

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)

        self.create_header()
        self.create_form()
        self.create_table()

        self.refresh()

    # -----------------------------------------------------
    # HEADER
    # -----------------------------------------------------

    def create_header(self):

        title = ctk.CTkLabel(
            self,
            text="Transactions",
            font=("Arial", 30, "bold"),
            text_color=(
                COLORS["text"],
                COLORS["dark_text"]
            )
        )

        title.grid(
            row=0,
            column=0,
            columnspan=2,
            sticky="w"
        )

        subtitle = ctk.CTkLabel(
            self,
            text="Manage your income and expenses.",
            font=("Arial", 13),
            text_color=(
                COLORS["secondary_text"],
                COLORS["dark_secondary"]
            )
        )

        subtitle.grid(
            row=1,
            column=0,
            columnspan=2,
            sticky="w",
            pady=(3, 20)
        )

    # -----------------------------------------------------
    # FORM
    # -----------------------------------------------------

    def create_form(self):

        form = ctk.CTkFrame(
            self,
            corner_radius=18,
            fg_color=(
                COLORS["card"],
                COLORS["dark_card"]
            ),
            border_width=1,
            border_color=(
                COLORS["border"],
                COLORS["dark_border"]
            )
        )

        form.grid(
            row=2,
            column=0,
            sticky="ns",
            padx=(0, 15)
        )

        title = ctk.CTkLabel(
            form,
            text="Add Transaction",
            font=("Arial", 18, "bold"),
            text_color=(
                COLORS["text"],
                COLORS["dark_text"]
            )
        )

        title.pack(
            padx=20,
            pady=(20, 15),
            anchor="w"
        )

        # Type
        ctk.CTkLabel(
            form,
            text="Type",
            font=("Arial", 12),
            text_color=(
                COLORS["secondary_text"],
                COLORS["dark_secondary"]
            )
        ).pack(
            padx=20,
            anchor="w"
        )

        self.type_menu = ctk.CTkOptionMenu(
            form,
            values=["Income", "Expense"],
            height=38,
            corner_radius=10,
            fg_color=(
                "#F2F2F7",
                "#2C2C2E"
            ),
            button_color=COLORS["accent"],
            button_hover_color=COLORS["accent_hover"],
            text_color=(
                COLORS["text"],
                COLORS["dark_text"]
            )
        )

        self.type_menu.pack(
            padx=20,
            pady=(5, 12),
            fill="x"
        )

        # Category
        ctk.CTkLabel(
            form,
            text="Category",
            font=("Arial", 12),
            text_color=(
                COLORS["secondary_text"],
                COLORS["dark_secondary"]
            )
        ).pack(
            padx=20,
            anchor="w"
        )

        self.category_menu = ctk.CTkOptionMenu(
            form,
            values=CATEGORIES,
            height=38,
            corner_radius=10,
            fg_color=(
                "#F2F2F7",
                "#2C2C2E"
            ),
            button_color=COLORS["accent"],
            button_hover_color=COLORS["accent_hover"]
        )

        self.category_menu.pack(
            padx=20,
            pady=(5, 12),
            fill="x"
        )

        # Amount
        ctk.CTkLabel(
            form,
            text="Amount",
            font=("Arial", 12),
            text_color=(
                COLORS["secondary_text"],
                COLORS["dark_secondary"]
            )
        ).pack(
            padx=20,
            anchor="w"
        )

        self.amount_entry = ctk.CTkEntry(
            form,
            height=38,
            corner_radius=10,
            placeholder_text="0.00"
        )

        self.amount_entry.pack(
            padx=20,
            pady=(5, 12),
            fill="x"
        )

        # Date
        ctk.CTkLabel(
            form,
            text="Date",
            font=("Arial", 12),
            text_color=(
                COLORS["secondary_text"],
                COLORS["dark_secondary"]
            )
        ).pack(
            padx=20,
            anchor="w"
        )

        self.date_entry = ctk.CTkEntry(
            form,
            height=38,
            corner_radius=10,
            placeholder_text="YYYY-MM-DD"
        )

        self.date_entry.pack(
            padx=20,
            pady=(5, 12),
            fill="x"
        )

        self.date_entry.insert(
            0,
            datetime.now().strftime("%Y-%m-%d")
        )

        # Description
        ctk.CTkLabel(
            form,
            text="Description",
            font=("Arial", 12),
            text_color=(
                COLORS["secondary_text"],
                COLORS["dark_secondary"]
            )
        ).pack(
            padx=20,
            anchor="w"
        )

        self.description_entry = ctk.CTkEntry(
            form,
            height=38,
            corner_radius=10,
            placeholder_text="Optional"
        )

        self.description_entry.pack(
            padx=20,
            pady=(5, 15),
            fill="x"
        )

        # Save
        self.save_button = ctk.CTkButton(
            form,
            text="Add Transaction",
            height=42,
            corner_radius=12,
            font=("Arial", 13, "bold"),
            fg_color=COLORS["accent"],
            hover_color=COLORS["accent_hover"],
            command=self.save_transaction
        )

        self.save_button.pack(
            padx=20,
            pady=(0, 8),
            fill="x"
        )

        self.clear_button = ctk.CTkButton(
            form,
            text="Clear",
            height=38,
            corner_radius=12,
            fg_color="transparent",
            border_width=1,
            border_color=(
                COLORS["border"],
                COLORS["dark_border"]
            ),
            text_color=(
                COLORS["text"],
                COLORS["dark_text"]
            ),
            hover_color=(
                COLORS["hover"],
                COLORS["dark_hover"]
            ),
            command=self.clear_form
        )

        self.clear_button.pack(
            padx=20,
            pady=(0, 20),
            fill="x"
        )

    # -----------------------------------------------------
    # TABLE
    # -----------------------------------------------------

    def create_table(self):

        container = ctk.CTkFrame(
            self,
            corner_radius=18,
            fg_color=(
                COLORS["card"],
                COLORS["dark_card"]
            ),
            border_width=1,
            border_color=(
                COLORS["border"],
                COLORS["dark_border"]
            )
        )

        container.grid(
            row=2,
            column=1,
            sticky="nsew"
        )

        container.grid_rowconfigure(
            2,
            weight=1
        )

        container.grid_columnconfigure(
            0,
            weight=1
        )

        title = ctk.CTkLabel(
            container,
            text="All Transactions",
            font=("Arial", 18, "bold"),
            text_color=(
                COLORS["text"],
                COLORS["dark_text"]
            )
        )

        title.grid(
            row=0,
            column=0,
            padx=20,
            pady=(20, 12),
            sticky="w"
        )

        # Search/filter
        controls = ctk.CTkFrame(
            container,
            fg_color="transparent"
        )

        controls.grid(
            row=1,
            column=0,
            sticky="ew",
            padx=20,
            pady=(0, 12)
        )

        controls.grid_columnconfigure(
            0,
            weight=1
        )

        self.search_entry = ctk.CTkEntry(
            controls,
            height=38,
            corner_radius=10,
            placeholder_text="Search transactions..."
        )

        self.search_entry.grid(
            row=0,
            column=0,
            sticky="ew",
            padx=(0, 8)
        )

        self.search_entry.bind(
            "<KeyRelease>",
            lambda event: self.refresh()
        )

        self.filter_menu = ctk.CTkOptionMenu(
            controls,
            values=["All", "Income", "Expense"],
            width=120,
            height=38,
            corner_radius=10,
            command=lambda value: self.refresh()
        )

        self.filter_menu.grid(
            row=0,
            column=1
        )

        self.table = ctk.CTkScrollableFrame(
            container,
            fg_color="transparent"
        )

        self.table.grid(
            row=2,
            column=0,
            sticky="nsew",
            padx=10,
            pady=(0, 10)
        )

    # -----------------------------------------------------
    # SAVE
    # -----------------------------------------------------

    def save_transaction(self):

        try:
            amount = float(
                self.amount_entry.get()
            )

            if amount <= 0:
                raise ValueError

        except ValueError:
            self.message(
                "Please enter a valid amount."
            )
            return

        date = self.date_entry.get().strip()

        try:
            datetime.strptime(
                date,
                "%Y-%m-%d"
            )
        except ValueError:
            self.message(
                "Date must use YYYY-MM-DD."
            )
            return

        transaction_type = self.type_menu.get()
        category = self.category_menu.get()
        description = self.description_entry.get().strip()

        if self.editing_id:

            update_transaction(
                self.editing_id,
                transaction_type,
                category,
                amount,
                description,
                date
            )

        else:

            add_transaction(
                transaction_type,
                category,
                amount,
                description,
                date
            )

        self.clear_form()
        self.refresh()

        self.app.pages["Dashboard"].refresh()

    # -----------------------------------------------------
    # EDIT
    # -----------------------------------------------------

    def edit_transaction(self, transaction_id):

        transaction = get_transaction(
            transaction_id
        )

        if not transaction:
            return

        _, t_type, category, amount, description, date = transaction

        self.editing_id = transaction_id

        self.type_menu.set(t_type)
        self.category_menu.set(category)

        self.amount_entry.delete(
            0,
            "end"
        )

        self.amount_entry.insert(
            0,
            str(amount)
        )

        self.date_entry.delete(
            0,
            "end"
        )

        self.date_entry.insert(
            0,
            date
        )

        self.description_entry.delete(
            0,
            "end"
        )

        self.description_entry.insert(
            0,
            description or ""
        )

        self.save_button.configure(
            text="Save Changes"
        )

    # -----------------------------------------------------
    # DELETE
    # -----------------------------------------------------

    def delete_transaction(self, transaction_id):

        confirm = self.confirm(
            "Delete Transaction",
            "Are you sure you want to delete this transaction?"
        )

        if confirm:

            delete_transaction(
                transaction_id
            )

            self.refresh()
            self.app.pages["Dashboard"].refresh()

    # -----------------------------------------------------
    # REFRESH
    # -----------------------------------------------------

    def refresh(self, *args):

        for widget in self.table.winfo_children():
            widget.destroy()

        transactions = get_transactions()

        search = self.search_entry.get().lower().strip()
        filter_type = self.filter_menu.get()

        filtered = []

        for transaction in transactions:

            transaction_id, t_type, category, amount, description, date = transaction

            text = (
                f"{category} "
                f"{description or ''} "
                f"{date}"
            ).lower()

            if search and search not in text:
                continue

            if filter_type != "All" and t_type != filter_type:
                continue

            filtered.append(transaction)

        if not filtered:

            label = ctk.CTkLabel(
                self.table,
                text="No transactions found.",
                font=("Arial", 13),
                text_color=(
                    COLORS["secondary_text"],
                    COLORS["dark_secondary"]
                )
            )

            label.pack(
                pady=30
            )

            return

        for transaction in filtered:

            transaction_id, t_type, category, amount, description, date = transaction

            row = ctk.CTkFrame(
                self.table,
                corner_radius=12,
                fg_color=(
                    COLORS["hover"],
                    COLORS["dark_hover"]
                )
            )

            row.pack(
                fill="x",
                pady=4
            )

            row.grid_columnconfigure(
                1,
                weight=1
            )

            ctk.CTkLabel(
                row,
                text=category,
                font=("Arial", 13, "bold")
            ).grid(
                row=0,
                column=0,
                padx=12,
                pady=10
            )

            ctk.CTkLabel(
                row,
                text=description or "-",
                font=("Arial", 12)
            ).grid(
                row=0,
                column=1,
                sticky="w"
            )

            ctk.CTkLabel(
                row,
                text=date,
                font=("Arial", 11),
                text_color=(
                    COLORS["secondary_text"],
                    COLORS["dark_secondary"]
                )
            ).grid(
                row=0,
                column=2,
                padx=10
            )

            amount_color = (
                COLORS["success"]
                if t_type == "Income"
                else COLORS["danger"]
            )

            ctk.CTkLabel(
                row,
                text=(
                    f"+₱{amount:,.2f}"
                    if t_type == "Income"
                    else f"-₱{amount:,.2f}"
                ),
                font=("Arial", 13, "bold"),
                text_color=amount_color
            ).grid(
                row=0,
                column=3,
                padx=10
            )

            edit = ctk.CTkButton(
                row,
                text="Edit",
                width=60,
                height=30,
                corner_radius=8,
                fg_color=COLORS["accent"],
                hover_color=COLORS["accent_hover"],
                command=lambda i=transaction_id:
                    self.edit_transaction(i)
            )

            edit.grid(
                row=0,
                column=4,
                padx=3
            )

            delete = ctk.CTkButton(
                row,
                text="Delete",
                width=65,
                height=30,
                corner_radius=8,
                fg_color=COLORS["danger"],
                hover_color="#D70015",
                command=lambda i=transaction_id:
                    self.delete_transaction(i)
            )

            delete.grid(
                row=0,
                column=5,
                padx=(3, 10)
            )

    # -----------------------------------------------------
    # CLEAR
    # -----------------------------------------------------

    def clear_form(self):

        self.editing_id = None

        self.type_menu.set("Expense")
        self.category_menu.set("Food")

        self.amount_entry.delete(
            0,
            "end"
        )

        self.description_entry.delete(
            0,
            "end"
        )

        self.date_entry.delete(
            0,
            "end"
        )

        self.date_entry.insert(
            0,
            datetime.now().strftime("%Y-%m-%d")
        )

        self.save_button.configure(
            text="Add Transaction"
        )

    # -----------------------------------------------------
    # MESSAGE
    # -----------------------------------------------------

    def message(self, text):

        dialog = ctk.CTkToplevel(self)
        dialog.title("Finance")
        dialog.geometry("350x170")
        dialog.resizable(False, False)

        dialog.transient(self)
        dialog.grab_set()

        ctk.CTkLabel(
            dialog,
            text=text,
            font=("Arial", 13),
            wraplength=300
        ).pack(
            pady=(35, 20)
        )

        ctk.CTkButton(
            dialog,
            text="OK",
            width=100,
            command=dialog.destroy
        ).pack()

    # -----------------------------------------------------
    # CONFIRM
    # -----------------------------------------------------

    def confirm(self, title, text):

        result = {"value": False}

        dialog = ctk.CTkToplevel(self)
        dialog.title(title)
        dialog.geometry("380x190")
        dialog.resizable(False, False)

        dialog.transient(self)
        dialog.grab_set()

        ctk.CTkLabel(
            dialog,
            text=text,
            font=("Arial", 13),
            wraplength=320
        ).pack(
            pady=(35, 25)
        )

        buttons = ctk.CTkFrame(
            dialog,
            fg_color="transparent"
        )

        buttons.pack()

        def yes():
            result["value"] = True
            dialog.destroy()

        ctk.CTkButton(
            buttons,
            text="Cancel",
            width=100,
            fg_color="transparent",
            border_width=1,
            command=dialog.destroy
        ).pack(
            side="left",
            padx=5
        )

        ctk.CTkButton(
            buttons,
            text="Delete",
            width=100,
            fg_color=COLORS["danger"],
            hover_color="#D70015",
            command=yes
        ).pack(
            side="left",
            padx=5
        )

        self.wait_window(dialog)

        return result["value"]
