# main.py

import customtkinter as ctk

from database import create_database
from dashboard import DashboardPage
from transactions import TransactionsPage
from budgets import BudgetsPage
from savings import SavingsPage
from reports import ReportsPage
from settings import SettingsPage


class FinanceApp(ctk.CTk):

    def __init__(self):
        super().__init__()

        # -------------------------------------------------
        # WINDOW
        # -------------------------------------------------

        self.title("Finance Manager")
        self.geometry("1250x780")
        self.minsize(1050, 680)

        # -------------------------------------------------
        # DATABASE
        # -------------------------------------------------

        create_database()

        # -------------------------------------------------
        # APPEARANCE
        # -------------------------------------------------

        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("blue")

        self.configure(
            fg_color=(
                "#F5F5F7",
                "#000000"
            )
        )

        # -------------------------------------------------
        # GRID
        # -------------------------------------------------

        self.grid_columnconfigure(
            1,
            weight=1
        )

        self.grid_rowconfigure(
            0,
            weight=1
        )

        self.pages = {}

        # -------------------------------------------------
        # BUILD UI
        # -------------------------------------------------

        self.create_sidebar()
        self.create_pages()

        # -------------------------------------------------
        # DEFAULT PAGE
        # -------------------------------------------------

        self.show_page("Dashboard")

    # =====================================================
    # SIDEBAR
    # =====================================================

    def create_sidebar(self):

        self.sidebar = ctk.CTkFrame(
            self,
            width=230,
            corner_radius=0,
            fg_color=(
                "#FFFFFF",
                "#1C1C1E"
            )
        )

        self.sidebar.grid(
            row=0,
            column=0,
            sticky="nsew"
        )

        self.sidebar.grid_propagate(False)

        # -------------------------------------------------
        # BRAND
        # -------------------------------------------------

        title = ctk.CTkLabel(
            self.sidebar,
            text="Finance",
            font=(
                "Arial",
                25,
                "bold"
            ),
            text_color=(
                "#1D1D1F",
                "#F5F5F7"
            )
        )

        title.pack(
            padx=25,
            pady=(35, 3),
            anchor="w"
        )

        subtitle = ctk.CTkLabel(
            self.sidebar,
            text="Personal Manager",
            font=(
                "Arial",
                12
            ),
            text_color=(
                "#6E6E73",
                "#98989D"
            )
        )

        subtitle.pack(
            padx=25,
            pady=(0, 30),
            anchor="w"
        )

        # -------------------------------------------------
        # NAVIGATION
        # -------------------------------------------------

        self.nav_buttons = {}

        navigation = [
            ("Dashboard", "Dashboard"),
            ("Transactions", "Transactions"),
            ("Budgets", "Budgets"),
            ("Savings", "Savings"),
            ("Reports", "Reports"),
            ("Settings", "Settings")
        ]

        for text, page_name in navigation:

            button = ctk.CTkButton(
                self.sidebar,
                text=text,
                height=44,
                corner_radius=10,
                anchor="w",
                font=(
                    "Arial",
                    13,
                    "bold"
                ),
                fg_color="transparent",
                hover_color=(
                    "#F2F2F7",
                    "#2C2C2E"
                ),
                text_color=(
                    "#1D1D1F",
                    "#F5F5F7"
                ),
                command=lambda p=page_name:
                    self.show_page(p)
            )

            button.pack(
                fill="x",
                padx=15,
                pady=3
            )

            self.nav_buttons[page_name] = button

        # -------------------------------------------------
        # VERSION
        # -------------------------------------------------

        bottom_frame = ctk.CTkFrame(
            self.sidebar,
            fg_color="transparent"
        )

        bottom_frame.pack(
            side="bottom",
            fill="x",
            padx=20,
            pady=20
        )

        version = ctk.CTkLabel(
            bottom_frame,
            text="Finance Manager\nVersion 2.1",
            font=(
                "Arial",
                11
            ),
            justify="left",
            text_color=(
                "#86868B",
                "#636366"
            )
        )

        version.pack(
            anchor="w"
        )

    # =====================================================
    # PAGES
    # =====================================================

    def create_pages(self):

        self.pages["Dashboard"] = DashboardPage(
            self,
            self
        )

        self.pages["Transactions"] = TransactionsPage(
            self,
            self
        )

        self.pages["Budgets"] = BudgetsPage(
            self,
            self
        )

        self.pages["Savings"] = SavingsPage(
            self,
            self
        )

        self.pages["Reports"] = ReportsPage(
            self,
            self
        )

        self.pages["Settings"] = SettingsPage(
            self,
            self
        )

    # =====================================================
    # PAGE NAVIGATION
    # =====================================================

    def show_page(self, page_name):

        for page in self.pages.values():
            page.grid_forget()

        page = self.pages.get(page_name)

        if page is None:
            return

        page.grid(
            row=0,
            column=1,
            sticky="nsew",
            padx=25,
            pady=25
        )

        # -------------------------------------------------
        # ACTIVE NAVIGATION
        # -------------------------------------------------

        for name, button in self.nav_buttons.items():

            if name == page_name:

                button.configure(
                    fg_color=(
                        "#E8E8ED",
                        "#2C2C2E"
                    )
                )

            else:

                button.configure(
                    fg_color="transparent"
                )

        # -------------------------------------------------
        # REFRESH PAGE
        # -------------------------------------------------

        if hasattr(page, "refresh"):

            try:
                page.refresh()

            except Exception as error:
                print(
                    f"Could not refresh {page_name}: {error}"
                )


# =========================================================
# RUN APPLICATION
# =========================================================

if __name__ == "__main__":

    app = FinanceApp()

    app.mainloop()
