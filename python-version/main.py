import customtkinter as ctk

import database
from transactions import TransactionsPage
from charts import ChartsPage
from settings import SettingsPage


# Create database
database.create_database()


class FinanceTracker(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Personal Finance Tracker")
        self.geometry("1100x700")
        self.minsize(900, 600)

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.sidebar = None
        self.content_frame = None

        self.create_sidebar()
        self.create_content_frame()

        self.show_dashboard()

    # ---------------------------------------------------------
    # SIDEBAR
    # ---------------------------------------------------------

    def create_sidebar(self):

        self.sidebar = ctk.CTkFrame(
            self,
            width=220,
            corner_radius=0
        )

        self.sidebar.grid(
            row=0,
            column=0,
            sticky="nsew"
        )

        self.sidebar.grid_propagate(False)

        logo = ctk.CTkLabel(
            self.sidebar,
            text="Finance Tracker",
            font=ctk.CTkFont(
                size=22,
                weight="bold"
            )
        )

        logo.pack(
            padx=20,
            pady=(30, 40)
        )

        self.dashboard_button = ctk.CTkButton(
            self.sidebar,
            text="Dashboard",
            height=45,
            command=self.show_dashboard
        )

        self.dashboard_button.pack(
            padx=20,
            pady=10,
            fill="x"
        )

        self.transactions_button = ctk.CTkButton(
            self.sidebar,
            text="Transactions",
            height=45,
            command=self.show_transactions
        )

        self.transactions_button.pack(
            padx=20,
            pady=10,
            fill="x"
        )

        self.charts_button = ctk.CTkButton(
            self.sidebar,
            text="Charts",
            height=45,
            command=self.show_charts
        )

        self.charts_button.pack(
            padx=20,
            pady=10,
            fill="x"
        )

        self.settings_button = ctk.CTkButton(
            self.sidebar,
            text="Settings",
            height=45,
            command=self.show_settings
        )

        self.settings_button.pack(
            padx=20,
            pady=10,
            fill="x"
        )

        # Appearance

        appearance_label = ctk.CTkLabel(
            self.sidebar,
            text="Appearance"
        )

        appearance_label.pack(
            side="bottom",
            pady=(0, 5)
        )

        appearance_menu = ctk.CTkOptionMenu(
            self.sidebar,
            values=["Dark", "Light", "System"],
            command=self.change_appearance
        )

        appearance_menu.pack(
            side="bottom",
            padx=20,
            pady=(0, 25)
        )

    # ---------------------------------------------------------
    # CONTENT FRAME
    # ---------------------------------------------------------

    def create_content_frame(self):

        self.content_frame = ctk.CTkFrame(
            self,
            corner_radius=0,
            fg_color="transparent"
        )

        self.content_frame.grid(
            row=0,
            column=1,
            sticky="nsew"
        )

    # ---------------------------------------------------------
    # CLEAR CONTENT
    # ---------------------------------------------------------

    def clear_content(self):

        for widget in self.content_frame.winfo_children():
            widget.destroy()

    # ---------------------------------------------------------
    # DASHBOARD
    # ---------------------------------------------------------

    def show_dashboard(self):

        self.clear_content()

        dashboard = ctk.CTkFrame(
            self.content_frame,
            fg_color="transparent"
        )

        dashboard.pack(
            fill="both",
            expand=True,
            padx=30,
            pady=30
        )

        title = ctk.CTkLabel(
            dashboard,
            text="Dashboard",
            font=ctk.CTkFont(
                size=32,
                weight="bold"
            )
        )

        title.pack(
            anchor="w",
            pady=(0, 25)
        )

        income = database.get_total_income()
        expenses = database.get_total_expenses()
        balance = database.get_balance()

        cards = ctk.CTkFrame(
            dashboard,
            fg_color="transparent"
        )

        cards.pack(
            fill="x"
        )

        cards.grid_columnconfigure(
            (0, 1, 2),
            weight=1
        )

        self.create_card(
            cards,
            "Current Balance",
            f"₱{balance:,.2f}",
            0
        )

        self.create_card(
            cards,
            "Total Income",
            f"₱{income:,.2f}",
            1
        )

        self.create_card(
            cards,
            "Total Expenses",
            f"₱{expenses:,.2f}",
            2
        )

        recent_title = ctk.CTkLabel(
            dashboard,
            text="Recent Transactions",
            font=ctk.CTkFont(
                size=22,
                weight="bold"
            )
        )

        recent_title.pack(
            anchor="w",
            pady=(40, 15)
        )

        transactions = database.get_transactions()

        if not transactions:

            label = ctk.CTkLabel(
                dashboard,
                text="No transactions yet."
            )

            label.pack(
                pady=20
            )

        else:

            for transaction in transactions[:5]:

                (
                    transaction_id,
                    transaction_type,
                    amount,
                    category,
                    description,
                    transaction_date
                ) = transaction

                text = (
                    f"{transaction_date}  |  "
                    f"{transaction_type}  |  "
                    f"{category}  |  "
                    f"₱{amount:,.2f}"
                )

                label = ctk.CTkLabel(
                    dashboard,
                    text=text,
                    anchor="w"
                )

                label.pack(
                    fill="x",
                    pady=5
                )

    # ---------------------------------------------------------
    # CARD
    # ---------------------------------------------------------

    def create_card(
        self,
        parent,
        title,
        value,
        column
    ):

        card = ctk.CTkFrame(
            parent,
            corner_radius=15
        )

        card.grid(
            row=0,
            column=column,
            padx=8,
            sticky="nsew"
        )

        title_label = ctk.CTkLabel(
            card,
            text=title
        )

        title_label.pack(
            pady=(20, 5)
        )

        value_label = ctk.CTkLabel(
            card,
            text=value,
            font=ctk.CTkFont(
                size=24,
                weight="bold"
            )
        )

        value_label.pack(
            pady=(5, 20)
        )

    # ---------------------------------------------------------
    # TRANSACTIONS
    # ---------------------------------------------------------

    def show_transactions(self):

        self.clear_content()

        transactions_page = TransactionsPage(
            self.content_frame,
            refresh_dashboard=self.show_dashboard
        )

        transactions_page.pack(
            fill="both",
            expand=True
        )

    # ---------------------------------------------------------
    # OTHER PAGES
    # ---------------------------------------------------------

    def show_charts(self):

        self.clear_content()

        charts_page = ChartsPage(
            self.content_frame
        )

        charts_page.pack(
            fill="both",
            expand=True
        )

    def show_settings(self):

        self.clear_content()

        settings_page = SettingsPage(
            self.content_frame,
            refresh_dashboard=self.show_dashboard
        )

        settings_page.pack(
            fill="both",
            expand=True
        )

    # ---------------------------------------------------------
    # APPEARANCE
    # ---------------------------------------------------------

    def change_appearance(self, mode):

        ctk.set_appearance_mode(mode)


# -------------------------------------------------------------
# START APPLICATION
# -------------------------------------------------------------

if __name__ == "__main__":

    app = FinanceTracker()

    app.mainloop()
