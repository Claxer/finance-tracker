import customtkinter as ctk
from tkinter import messagebox

import database


class SettingsPage(ctk.CTkFrame):

    def __init__(self, parent, refresh_dashboard=None):
        super().__init__(
            parent,
            corner_radius=0,
            fg_color="transparent"
        )

        self.refresh_dashboard = refresh_dashboard

        self.grid_columnconfigure(0, weight=1)

        self.create_header()
        self.create_appearance_section()
        self.create_data_section()
        self.create_about_section()

    # =========================================================
    # HEADER
    # =========================================================

    def create_header(self):

        title = ctk.CTkLabel(
            self,
            text="Settings",
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
    # APPEARANCE
    # =========================================================

    def create_appearance_section(self):

        frame = ctk.CTkFrame(
            self,
            corner_radius=15
        )

        frame.grid(
            row=1,
            column=0,
            sticky="ew",
            padx=30,
            pady=10
        )

        title = ctk.CTkLabel(
            frame,
            text="Appearance",
            font=ctk.CTkFont(
                size=20,
                weight="bold"
            )
        )

        title.pack(
            anchor="w",
            padx=20,
            pady=(20, 5)
        )

        description = ctk.CTkLabel(
            frame,
            text="Choose how the application looks."
        )

        description.pack(
            anchor="w",
            padx=20,
            pady=(0, 15)
        )

        self.appearance_menu = ctk.CTkOptionMenu(
            frame,
            values=[
                "Dark",
                "Light",
                "System"
            ],
            command=self.change_appearance
        )

        self.appearance_menu.set(
            "Dark"
        )

        self.appearance_menu.pack(
            anchor="w",
            padx=20,
            pady=(0, 20)
        )

    # =========================================================
    # DATA MANAGEMENT
    # =========================================================

    def create_data_section(self):

        frame = ctk.CTkFrame(
            self,
            corner_radius=15
        )

        frame.grid(
            row=2,
            column=0,
            sticky="ew",
            padx=30,
            pady=10
        )

        title = ctk.CTkLabel(
            frame,
            text="Data Management",
            font=ctk.CTkFont(
                size=20,
                weight="bold"
            )
        )

        title.pack(
            anchor="w",
            padx=20,
            pady=(20, 5)
        )

        description = ctk.CTkLabel(
            frame,
            text="Manage your saved financial transactions."
        )

        description.pack(
            anchor="w",
            padx=20,
            pady=(0, 15)
        )

        clear_button = ctk.CTkButton(
            frame,
            text="Clear All Transactions",
            command=self.clear_transactions
        )

        clear_button.pack(
            anchor="w",
            padx=20,
            pady=(0, 20)
        )

    # =========================================================
    # ABOUT
    # =========================================================

    def create_about_section(self):

        frame = ctk.CTkFrame(
            self,
            corner_radius=15
        )

        frame.grid(
            row=3,
            column=0,
            sticky="ew",
            padx=30,
            pady=10
        )

        title = ctk.CTkLabel(
            frame,
            text="About",
            font=ctk.CTkFont(
                size=20,
                weight="bold"
            )
        )

        title.pack(
            anchor="w",
            padx=20,
            pady=(20, 5)
        )

        information = ctk.CTkLabel(
            frame,
            text=(
                "Personal Finance Tracker\n"
                "Version 1.0\n\n"
                "A desktop application for managing "
                "personal income and expenses."
            ),
            justify="left"
        )

        information.pack(
            anchor="w",
            padx=20,
            pady=(0, 20)
        )

    # =========================================================
    # APPEARANCE
    # =========================================================

    def change_appearance(self, mode):

        ctk.set_appearance_mode(
            mode
        )

    # =========================================================
    # CLEAR TRANSACTIONS
    # =========================================================

    def clear_transactions(self):

        confirm = messagebox.askyesno(
            "Clear All Transactions",
            (
                "Are you sure you want to delete "
                "ALL transactions?\n\n"
                "This action cannot be undone."
            )
        )

        if not confirm:
            return

        connection = database.connect_database()
        cursor = connection.cursor()

        cursor.execute(
            "DELETE FROM transactions"
        )

        connection.commit()
        connection.close()

        messagebox.showinfo(
            "Transactions Cleared",
            "All transactions have been deleted."
        )

        if self.refresh_dashboard:
            self.refresh_dashboard()
