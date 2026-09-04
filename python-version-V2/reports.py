# reports.py

import customtkinter as ctk

from database import (
    get_totals,
    get_monthly_totals,
    get_expenses_by_category,
    get_income_by_category,
    get_recent_transactions
)

from theme import COLORS, FONTS


class ReportsPage(ctk.CTkFrame):

    def __init__(self, parent, app):

        super().__init__(
            parent,
            fg_color=COLORS["background"]
        )

        self.app = app

        self.create_ui()
        self.refresh()

    # =====================================================
    # CREATE UI
    # =====================================================

    def create_ui(self):

        # -------------------------------------------------
        # MAIN CONTAINER
        # -------------------------------------------------

        self.container = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        self.container.pack(
            fill="both",
            expand=True,
            padx=35,
            pady=30
        )

        # -------------------------------------------------
        # HEADER
        # -------------------------------------------------

        header = ctk.CTkFrame(
            self.container,
            fg_color="transparent"
        )

        header.pack(
            fill="x",
            pady=(0, 25)
        )

        title = ctk.CTkLabel(
            header,
            text="Reports",
            font=FONTS["title"],
            text_color=COLORS["text"]
        )

        title.pack(
            anchor="w"
        )

        subtitle = ctk.CTkLabel(
            header,
            text="Review your financial activity and spending.",
            font=FONTS["body"],
            text_color=COLORS["secondary_text"]
        )

        subtitle.pack(
            anchor="w",
            pady=(5, 0)
        )

        # -------------------------------------------------
        # SUMMARY CARDS
        # -------------------------------------------------

        summary_frame = ctk.CTkFrame(
            self.container,
            fg_color="transparent"
        )

        summary_frame.pack(
            fill="x",
            pady=(0, 25)
        )

        summary_frame.grid_columnconfigure(
            0,
            weight=1
        )

        summary_frame.grid_columnconfigure(
            1,
            weight=1
        )

        summary_frame.grid_columnconfigure(
            2,
            weight=1
        )

        # Income Card
        self.income_card = self.create_summary_card(
            summary_frame,
            "Total Income",
            "₱0.00",
            COLORS["success"]
        )

        self.income_card.grid(
            row=0,
            column=0,
            sticky="nsew",
            padx=(0, 8)
        )

        # Expense Card
        self.expense_card = self.create_summary_card(
            summary_frame,
            "Total Expenses",
            "₱0.00",
            COLORS["danger"]
        )

        self.expense_card.grid(
            row=0,
            column=1,
            sticky="nsew",
            padx=8
        )

        # Balance Card
        self.balance_card = self.create_summary_card(
            summary_frame,
            "Current Balance",
            "₱0.00",
            COLORS["accent"]
        )

        self.balance_card.grid(
            row=0,
            column=2,
            sticky="nsew",
            padx=(8, 0)
        )

        # -------------------------------------------------
        # CONTENT AREA
        # -------------------------------------------------

        content = ctk.CTkFrame(
            self.container,
            fg_color="transparent"
        )

        content.pack(
            fill="both",
            expand=True
        )

        content.grid_columnconfigure(
            0,
            weight=1
        )

        content.grid_columnconfigure(
            1,
            weight=1
        )

        content.grid_rowconfigure(
            0,
            weight=1
        )

        # -------------------------------------------------
        # CATEGORY REPORT
        # -------------------------------------------------

        category_card = ctk.CTkFrame(
            content,
            fg_color=COLORS["card"],
            corner_radius=18,
            border_width=1,
            border_color=COLORS["border"]
        )

        category_card.grid(
            row=0,
            column=0,
            sticky="nsew",
            padx=(0, 10)
        )

        category_title = ctk.CTkLabel(
            category_card,
            text="Expense Breakdown",
            font=FONTS["heading"],
            text_color=COLORS["text"]
        )

        category_title.pack(
            anchor="w",
            padx=22,
            pady=(20, 5)
        )

        category_subtitle = ctk.CTkLabel(
            category_card,
            text="Where your money is being spent",
            font=FONTS["small"],
            text_color=COLORS["secondary_text"]
        )

        category_subtitle.pack(
            anchor="w",
            padx=22,
            pady=(0, 15)
        )

        self.category_scroll = ctk.CTkScrollableFrame(
            category_card,
            fg_color="transparent"
        )

        self.category_scroll.pack(
            fill="both",
            expand=True,
            padx=12,
            pady=(0, 15)
        )

        # -------------------------------------------------
        # RECENT ACTIVITY
        # -------------------------------------------------

        activity_card = ctk.CTkFrame(
            content,
            fg_color=COLORS["card"],
            corner_radius=18,
            border_width=1,
            border_color=COLORS["border"]
        )

        activity_card.grid(
            row=0,
            column=1,
            sticky="nsew",
            padx=(10, 0)
        )

        activity_title = ctk.CTkLabel(
            activity_card,
            text="Recent Activity",
            font=FONTS["heading"],
            text_color=COLORS["text"]
        )

        activity_title.pack(
            anchor="w",
            padx=22,
            pady=(20, 5)
        )

        activity_subtitle = ctk.CTkLabel(
            activity_card,
            text="Your latest financial transactions",
            font=FONTS["small"],
            text_color=COLORS["secondary_text"]
        )

        activity_subtitle.pack(
            anchor="w",
            padx=22,
            pady=(0, 15)
        )

        self.activity_scroll = ctk.CTkScrollableFrame(
            activity_card,
            fg_color="transparent"
        )

        self.activity_scroll.pack(
            fill="both",
            expand=True,
            padx=12,
            pady=(0, 15)
        )

    # =====================================================
    # SUMMARY CARD
    # =====================================================

    def create_summary_card(
        self,
        parent,
        title,
        value,
        accent
    ):

        card = ctk.CTkFrame(
            parent,
            fg_color=COLORS["card"],
            corner_radius=18,
            border_width=1,
            border_color=COLORS["border"],
            height=120
        )

        card.pack_propagate(False)

        title_label = ctk.CTkLabel(
            card,
            text=title,
            font=FONTS["small"],
            text_color=COLORS["secondary_text"]
        )

        title_label.pack(
            anchor="w",
            padx=20,
            pady=(18, 0)
        )

        value_label = ctk.CTkLabel(
            card,
            text=value,
            font=FONTS["number"],
            text_color=accent
        )

        value_label.pack(
            anchor="w",
            padx=20,
            pady=(5, 0)
        )

        card.value_label = value_label

        return card

    # =====================================================
    # REFRESH
    # =====================================================

    def refresh(self):

        # -------------------------------------------------
        # GET TOTALS
        # -------------------------------------------------

        income, expenses, balance = get_totals()

        # -------------------------------------------------
        # UPDATE SUMMARY CARDS
        # -------------------------------------------------

        self.income_card.value_label.configure(
            text=self.format_currency(income)
        )

        self.expense_card.value_label.configure(
            text=self.format_currency(expenses)
        )

        self.balance_card.value_label.configure(
            text=self.format_currency(balance)
        )

        # Change balance color depending on value

        if balance >= 0:

            self.balance_card.value_label.configure(
                text_color=COLORS["accent"]
            )

        else:

            self.balance_card.value_label.configure(
                text_color=COLORS["danger"]
            )

        # -------------------------------------------------
        # REFRESH CATEGORY REPORT
        # -------------------------------------------------

        self.refresh_categories()

        # -------------------------------------------------
        # REFRESH RECENT ACTIVITY
        # -------------------------------------------------

        self.refresh_recent_activity()

    # =====================================================
    # REFRESH CATEGORIES
    # =====================================================

    def refresh_categories(self):

        # Clear old widgets

        for widget in self.category_scroll.winfo_children():

            widget.destroy()

        categories = get_expenses_by_category()

        if not categories:

            empty_label = ctk.CTkLabel(
                self.category_scroll,
                text="No expense data available.",
                font=FONTS["body"],
                text_color=COLORS["secondary_text"]
            )

            empty_label.pack(
                pady=40
            )

            return

        # Calculate total expenses

        total_expenses = sum(
            amount
            for category, amount in categories
        )

        for category, amount in categories:

            if total_expenses > 0:

                percentage = (
                    amount /
                    total_expenses
                ) * 100

            else:

                percentage = 0

            row = ctk.CTkFrame(
                self.category_scroll,
                fg_color="transparent"
            )

            row.pack(
                fill="x",
                pady=8
            )

            # Category name

            category_label = ctk.CTkLabel(
                row,
                text=str(category),
                font=FONTS["body"],
                text_color=COLORS["text"]
            )

            category_label.pack(
                side="left"
            )

            # Amount

            amount_label = ctk.CTkLabel(
                row,
                text=self.format_currency(amount),
                font=FONTS["body"],
                text_color=COLORS["text"]
            )

            amount_label.pack(
                side="right"
            )

            # Percentage

            percentage_label = ctk.CTkLabel(
                row,
                text=f"{percentage:.1f}%",
                font=FONTS["small"],
                text_color=COLORS["secondary_text"]
            )

            percentage_label.pack(
                side="right",
                padx=(0, 15)
            )

            # Progress bar

            progress = ctk.CTkProgressBar(
                self.category_scroll,
                height=8,
                corner_radius=4,
                progress_color=COLORS["accent"],
                fg_color=COLORS["hover"]
            )

            progress.pack(
                fill="x",
                padx=5,
                pady=(0, 5)
            )

            progress.set(
                percentage / 100
            )

    # =====================================================
    # RECENT ACTIVITY
    # =====================================================

    def refresh_recent_activity(self):

        # Clear old widgets

        for widget in self.activity_scroll.winfo_children():

            widget.destroy()

        transactions = get_recent_transactions(
            limit=10
        )

        if not transactions:

            empty_label = ctk.CTkLabel(
                self.activity_scroll,
                text="No transactions available.",
                font=FONTS["body"],
                text_color=COLORS["secondary_text"]
            )

            empty_label.pack(
                pady=40
            )

            return

        for transaction in transactions:

            transaction_id = transaction[0]
            transaction_type = transaction[1]
            category = transaction[2]
            amount = transaction[3]
            description = transaction[4]
            date = transaction[5]

            row = ctk.CTkFrame(
                self.activity_scroll,
                fg_color=COLORS["hover"],
                corner_radius=12,
                height=70
            )

            row.pack(
                fill="x",
                pady=5,
                padx=2
            )

            row.pack_propagate(False)

            # -------------------------------------------------
            # LEFT SIDE
            # -------------------------------------------------

            left = ctk.CTkFrame(
                row,
                fg_color="transparent"
            )

            left.pack(
                side="left",
                fill="y",
                padx=15
            )

            category_label = ctk.CTkLabel(
                left,
                text=str(category),
                font=FONTS["body"],
                text_color=COLORS["text"]
            )

            category_label.pack(
                anchor="w",
                pady=(12, 0)
            )

            detail = description if description else date

            detail_label = ctk.CTkLabel(
                left,
                text=str(detail),
                font=FONTS["small"],
                text_color=COLORS["secondary_text"]
            )

            detail_label.pack(
                anchor="w"
            )

            # -------------------------------------------------
            # RIGHT SIDE
            # -------------------------------------------------

            if transaction_type == "Income":

                prefix = "+ "
                amount_color = COLORS["success"]

            else:

                prefix = "- "
                amount_color = COLORS["danger"]

            amount_label = ctk.CTkLabel(
                row,
                text=prefix + self.format_currency(amount),
                font=FONTS["subheading"],
                text_color=amount_color
            )

            amount_label.pack(
                side="right",
                padx=15
            )

    # =====================================================
    # FORMAT CURRENCY
    # =====================================================

    def format_currency(self, amount):

        try:

            return f"₱{float(amount):,.2f}"

        except (
            ValueError,
            TypeError
        ):

            return "₱0.00"
