# dashboard.py

import customtkinter as ctk

from database import get_totals, get_transactions
from theme import COLORS


class DashboardPage(ctk.CTkFrame):

    def __init__(self, parent, app):
        super().__init__(
            parent,
            fg_color="transparent"
        )

        self.app = app

        self.grid_columnconfigure(
            (0, 1, 2),
            weight=1
        )

        self.create_header()
        self.create_cards()
        self.create_recent_transactions()

        self.refresh()

    # -----------------------------------------------------
    # HEADER
    # -----------------------------------------------------

    def create_header(self):

        header = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        header.grid(
            row=0,
            column=0,
            columnspan=3,
            sticky="ew",
            pady=(0, 25)
        )

        title = ctk.CTkLabel(
            header,
            text="Dashboard",
            font=("Arial", 30, "bold"),
            text_color=(
                COLORS["text"],
                COLORS["dark_text"]
            )
        )

        title.pack(anchor="w")

        subtitle = ctk.CTkLabel(
            header,
            text="A clear overview of your financial activity.",
            font=("Arial", 13),
            text_color=(
                COLORS["secondary_text"],
                COLORS["dark_secondary"]
            )
        )

        subtitle.pack(
            anchor="w",
            pady=(3, 0)
        )

    # -----------------------------------------------------
    # CARDS
    # -----------------------------------------------------

    def create_cards(self):

        self.balance_card = self.create_card(
            0,
            "Current Balance",
            COLORS["accent"]
        )

        self.income_card = self.create_card(
            1,
            "Total Income",
            COLORS["success"]
        )

        self.expense_card = self.create_card(
            2,
            "Total Expenses",
            COLORS["danger"]
        )

    def create_card(self, column, title, accent):

        card = ctk.CTkFrame(
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

        card.grid(
            row=1,
            column=column,
            sticky="nsew",
            padx=6
        )

        label = ctk.CTkLabel(
            card,
            text=title,
            font=("Arial", 13),
            text_color=(
                COLORS["secondary_text"],
                COLORS["dark_secondary"]
            )
        )

        label.pack(
            anchor="w",
            padx=20,
            pady=(20, 4)
        )

        value = ctk.CTkLabel(
            card,
            text="₱0.00",
            font=("Arial", 27, "bold"),
            text_color=(
                COLORS["text"],
                COLORS["dark_text"]
            )
        )

        value.pack(
            anchor="w",
            padx=20,
            pady=(0, 20)
        )

        card.value_label = value

        return card

    # -----------------------------------------------------
    # RECENT TRANSACTIONS
    # -----------------------------------------------------

    def create_recent_transactions(self):

        section = ctk.CTkFrame(
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

        section.grid(
            row=2,
            column=0,
            columnspan=3,
            sticky="nsew",
            pady=(25, 0)
        )

        self.grid_rowconfigure(
            2,
            weight=1
        )

        title = ctk.CTkLabel(
            section,
            text="Recent Transactions",
            font=("Arial", 18, "bold"),
            text_color=(
                COLORS["text"],
                COLORS["dark_text"]
            )
        )

        title.pack(
            anchor="w",
            padx=20,
            pady=(20, 15)
        )

        self.transaction_container = ctk.CTkScrollableFrame(
            section,
            fg_color="transparent"
        )

        self.transaction_container.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=(0, 15)
        )

    # -----------------------------------------------------
    # REFRESH
    # -----------------------------------------------------

    def refresh(self):

        income, expenses, balance = get_totals()

        self.balance_card.value_label.configure(
            text=f"₱{balance:,.2f}"
        )

        self.income_card.value_label.configure(
            text=f"₱{income:,.2f}"
        )

        self.expense_card.value_label.configure(
            text=f"₱{expenses:,.2f}"
        )

        for widget in self.transaction_container.winfo_children():
            widget.destroy()

        transactions = get_transactions()[:8]

        if not transactions:

            empty = ctk.CTkLabel(
                self.transaction_container,
                text="No transactions yet.",
                font=("Arial", 13),
                text_color=(
                    COLORS["secondary_text"],
                    COLORS["dark_secondary"]
                )
            )

            empty.pack(
                pady=30
            )

            return

        for transaction in transactions:

            transaction_id, t_type, category, amount, description, date = transaction

            row = ctk.CTkFrame(
                self.transaction_container,
                height=55,
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

            row.grid_columnconfigure(1, weight=1)

            category_label = ctk.CTkLabel(
                row,
                text=category,
                font=("Arial", 13, "bold"),
                text_color=(
                    COLORS["text"],
                    COLORS["dark_text"]
                )
            )

            category_label.grid(
                row=0,
                column=0,
                padx=15
            )

            description_label = ctk.CTkLabel(
                row,
                text=description or "-",
                font=("Arial", 12),
                text_color=(
                    COLORS["secondary_text"],
                    COLORS["dark_secondary"]
                )
            )

            description_label.grid(
                row=0,
                column=1,
                sticky="w"
            )

            color = (
                COLORS["success"]
                if t_type == "Income"
                else COLORS["danger"]
            )

            amount_label = ctk.CTkLabel(
                row,
                text=(
                    f"+₱{amount:,.2f}"
                    if t_type == "Income"
                    else f"-₱{amount:,.2f}"
                ),
                font=("Arial", 13, "bold"),
                text_color=color
            )

            amount_label.grid(
                row=0,
                column=2,
                padx=15
            )

            date_label = ctk.CTkLabel(
                row,
                text=date,
                font=("Arial", 11),
                text_color=(
                    COLORS["muted_text"],
                    COLORS["dark_secondary"]
                )
            )

            date_label.grid(
                row=0,
                column=3,
                padx=(0, 15)
            )
