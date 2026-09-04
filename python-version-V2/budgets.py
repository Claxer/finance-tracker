# budgets.py

import customtkinter as ctk

from database import add_budget, get_budgets
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
    "Other"
]


class BudgetsPage(ctk.CTkFrame):

    def __init__(self, parent, app):

        super().__init__(
            parent,
            fg_color="transparent"
        )

        self.app = app

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=1)

        self.create_header()
        self.create_form()
        self.create_budget_list()

        self.refresh()

    def create_header(self):

        ctk.CTkLabel(
            self,
            text="Budgets",
            font=("Arial", 30, "bold"),
            text_color=(
                COLORS["text"],
                COLORS["dark_text"]
            )
        ).grid(
            row=0,
            column=0,
            sticky="w"
        )

        ctk.CTkLabel(
            self,
            text="Set spending limits for your categories.",
            font=("Arial", 13),
            text_color=(
                COLORS["secondary_text"],
                COLORS["dark_secondary"]
            )
        ).grid(
            row=1,
            column=0,
            sticky="w",
            pady=(3, 20)
        )

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
            sticky="ew"
        )

        ctk.CTkLabel(
            form,
            text="Create Budget",
            font=("Arial", 18, "bold")
        ).pack(
            anchor="w",
            padx=20,
            pady=(20, 15)
        )

        self.category = ctk.CTkOptionMenu(
            form,
            values=CATEGORIES,
            height=38,
            corner_radius=10
        )

        self.category.pack(
            side="left",
            padx=(20, 8),
            pady=(0, 20)
        )

        self.amount = ctk.CTkEntry(
            form,
            width=180,
            height=38,
            corner_radius=10,
            placeholder_text="Budget amount"
        )

        self.amount.pack(
            side="left",
            padx=8,
            pady=(0, 20)
        )

        self.month = ctk.CTkEntry(
            form,
            width=150,
            height=38,
            corner_radius=10,
            placeholder_text="Month"
        )

        self.month.pack(
            side="left",
            padx=8,
            pady=(0, 20)
        )

        ctk.CTkButton(
            form,
            text="Add Budget",
            height=38,
            corner_radius=10,
            fg_color=COLORS["accent"],
            hover_color=COLORS["accent_hover"],
            command=self.add
        ).pack(
            side="left",
            padx=8,
            pady=(0, 20)
        )

    def create_budget_list(self):

        self.list_frame = ctk.CTkScrollableFrame(
            self,
            fg_color="transparent"
        )

        self.list_frame.grid(
            row=3,
            column=0,
            sticky="nsew",
            pady=(20, 0)
        )

        self.grid_rowconfigure(
            3,
            weight=1
        )

    def add(self):

        try:
            amount = float(
                self.amount.get()
            )

            if amount <= 0:
                raise ValueError

        except ValueError:
            self.message(
                "Please enter a valid budget amount."
            )
            return

        month = self.month.get().strip()

        if not month:
            month = "Current"

        add_budget(
            self.category.get(),
            amount,
            month
        )

        self.amount.delete(0, "end")
        self.month.delete(0, "end")

        self.refresh()

    def refresh(self):

        for widget in self.list_frame.winfo_children():
            widget.destroy()

        budgets = get_budgets()

        if not budgets:

            ctk.CTkLabel(
                self.list_frame,
                text="No budgets created yet.",
                font=("Arial", 13),
                text_color=(
                    COLORS["secondary_text"],
                    COLORS["dark_secondary"]
                )
            ).pack(
                pady=30
            )

            return

        for budget_id, category, amount, month in budgets:

            card = ctk.CTkFrame(
                self.list_frame,
                corner_radius=15,
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

            card.pack(
                fill="x",
                pady=5
            )

            ctk.CTkLabel(
                card,
                text=category,
                font=("Arial", 15, "bold")
            ).pack(
                side="left",
                padx=20,
                pady=18
            )

            ctk.CTkLabel(
                card,
                text=month,
                font=("Arial", 12),
                text_color=(
                    COLORS["secondary_text"],
                    COLORS["dark_secondary"]
                )
            ).pack(
                side="left"
            )

            ctk.CTkLabel(
                card,
                text=f"₱{amount:,.2f}",
                font=("Arial", 15, "bold"),
                text_color=COLORS["accent"]
            ).pack(
                side="right",
                padx=20
            )

    def message(self, text):

        dialog = ctk.CTkToplevel(self)
        dialog.title("Finance")
        dialog.geometry("350x160")
        dialog.resizable(False, False)

        ctk.CTkLabel(
            dialog,
            text=text,
            wraplength=300
        ).pack(
            pady=30
        )

        ctk.CTkButton(
            dialog,
            text="OK",
            width=100,
            command=dialog.destroy
        ).pack()
