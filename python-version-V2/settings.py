# settings.py

import customtkinter as ctk

from theme import COLORS


class SettingsPage(ctk.CTkFrame):

    def __init__(self, parent, app):

        super().__init__(
            parent,
            fg_color="transparent"
        )

        self.app = app

        self.create_header()
        self.create_settings()

    def create_header(self):

        ctk.CTkLabel(
            self,
            text="Settings",
            font=("Arial", 30, "bold"),
            text_color=(
                COLORS["text"],
                COLORS["dark_text"]
            )
        ).pack(
            anchor="w"
        )

        ctk.CTkLabel(
            self,
            text="Customize how Finance looks and behaves.",
            font=("Arial", 13),
            text_color=(
                COLORS["secondary_text"],
                COLORS["dark_secondary"]
            )
        ).pack(
            anchor="w",
            pady=(3, 20)
        )

    def create_settings(self):

        appearance_card = ctk.CTkFrame(
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

        appearance_card.pack(
            fill="x",
            pady=5
        )

        ctk.CTkLabel(
            appearance_card,
            text="Appearance",
            font=("Arial", 18, "bold")
        ).pack(
            anchor="w",
            padx=20,
            pady=(20, 4)
        )

        ctk.CTkLabel(
            appearance_card,
            text="Choose how the application should look.",
            font=("Arial", 12),
            text_color=(
                COLORS["secondary_text"],
                COLORS["dark_secondary"]
            )
        ).pack(
            anchor="w",
            padx=20,
            pady=(0, 15)
        )

        self.appearance = ctk.CTkOptionMenu(
            appearance_card,
            values=[
                "System",
                "Light",
                "Dark"
            ],
            width=180,
            height=40,
            corner_radius=10,
            command=self.change_appearance
        )

        self.appearance.pack(
            anchor="w",
            padx=20,
            pady=(0, 20)
        )

        # Application information
        info_card = ctk.CTkFrame(
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

        info_card.pack(
            fill="x",
            pady=(15, 5)
        )

        ctk.CTkLabel(
            info_card,
            text="About Finance",
            font=("Arial", 18, "bold")
        ).pack(
            anchor="w",
            padx=20,
            pady=(20, 5)
        )

        ctk.CTkLabel(
            info_card,
            text=(
                "Personal Finance Manager\n"
                "Version 2.1\n\n"
                "Built with Python, CustomTkinter and SQLite."
            ),
            font=("Arial", 13),
            justify="left",
            text_color=(
                COLORS["secondary_text"],
                COLORS["dark_secondary"]
            )
        ).pack(
            anchor="w",
            padx=20,
            pady=(0, 20)
        )

    def change_appearance(self, value):

        ctk.set_appearance_mode(
            value
        )
