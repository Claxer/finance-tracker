# savings.py

import customtkinter as ctk

from database import (
    add_savings_goal,
    get_savings_goals
)

from theme import COLORS, FONTS


class SavingsPage(ctk.CTkFrame):

    def __init__(self, parent, app):

        super().__init__(
            parent,
            fg_color="transparent"
        )

        self.app = app

        self.grid_columnconfigure(
            0,
            weight=1
        )

        self.grid_rowconfigure(
            3,
            weight=1
        )

        self.create_header()
        self.create_form()
        self.create_goal_list()

        self.refresh()

    # =====================================================
    # HEADER
    # =====================================================

    def create_header(self):

        ctk.CTkLabel(
            self,
            text="Savings Goals",
            font=FONTS["title"],
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
            text="Track the progress of the things you are saving for.",
            font=FONTS["body"],
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

    # =====================================================
    # FORM
    # =====================================================

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
            text="New Savings Goal",
            font=FONTS["subheading"]
        ).pack(
            anchor="w",
            padx=20,
            pady=(20, 15)
        )

        self.name = ctk.CTkEntry(
            form,
            width=200,
            height=38,
            corner_radius=10,
            placeholder_text="Goal name"
        )

        self.name.pack(
            side="left",
            padx=(20, 8),
            pady=(0, 20)
        )

        self.target = ctk.CTkEntry(
            form,
            width=150,
            height=38,
            corner_radius=10,
            placeholder_text="Target amount"
        )

        self.target.pack(
            side="left",
            padx=8,
            pady=(0, 20)
        )

        self.saved = ctk.CTkEntry(
            form,
            width=150,
            height=38,
            corner_radius=10,
            placeholder_text="Already saved"
        )

        self.saved.pack(
            side="left",
            padx=8,
            pady=(0, 20)
        )

        self.target_date = ctk.CTkEntry(
            form,
            width=150,
            height=38,
            corner_radius=10,
            placeholder_text="Target date"
        )

        self.target_date.pack(
            side="left",
            padx=8,
            pady=(0, 20)
        )

        ctk.CTkButton(
            form,
            text="Add Goal",
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

    # =====================================================
    # GOAL LIST
    # =====================================================

    def create_goal_list(self):

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

    # =====================================================
    # ADD GOAL
    # =====================================================

    def add(self):

        name = self.name.get().strip()

        if not name:

            self.message(
                "Please enter a goal name."
            )

            return

        try:

            target = float(
                self.target.get()
            )

            saved = float(
                self.saved.get() or 0
            )

            if target <= 0:
                raise ValueError

            if saved < 0:
                raise ValueError

        except ValueError:

            self.message(
                "Please enter valid amounts."
            )

            return

        add_savings_goal(
            name,
            target,
            saved,
            self.target_date.get().strip()
        )

        self.name.delete(
            0,
            "end"
        )

        self.target.delete(
            0,
            "end"
        )

        self.saved.delete(
            0,
            "end"
        )

        self.target_date.delete(
            0,
            "end"
        )

        self.refresh()

    # =====================================================
    # REFRESH
    # =====================================================

    def refresh(self):

        for widget in self.list_frame.winfo_children():
            widget.destroy()

        goals = get_savings_goals()

        if not goals:

            ctk.CTkLabel(
                self.list_frame,
                text="No savings goals created yet.",
                font=FONTS["body"],
                text_color=(
                    COLORS["secondary_text"],
                    COLORS["dark_secondary"]
                )
            ).pack(
                pady=30
            )

            return

        for (
            goal_id,
            name,
            target,
            saved,
            target_date
        ) in goals:

            self.create_goal_card(
                name,
                target,
                saved,
                target_date
            )

    # =====================================================
    # GOAL CARD
    # =====================================================

    def create_goal_card(
        self,
        name,
        target,
        saved,
        target_date
    ):

        card = ctk.CTkFrame(
            self.list_frame,
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

        card.pack(
            fill="x",
            pady=6
        )

        top = ctk.CTkFrame(
            card,
            fg_color="transparent"
        )

        top.pack(
            fill="x",
            padx=20,
            pady=(18, 8)
        )

        ctk.CTkLabel(
            top,
            text=name,
            font=FONTS["subheading"]
        ).pack(
            side="left"
        )

        percentage = min(
            saved / target * 100,
            100
        )

        ctk.CTkLabel(
            top,
            text=f"{percentage:.0f}%",
            font=FONTS["button"],
            text_color=COLORS["success"]
        ).pack(
            side="right"
        )

        progress = ctk.CTkProgressBar(
            card,
            height=10,
            corner_radius=5,
            progress_color=COLORS["success"]
        )

        progress.pack(
            fill="x",
            padx=20,
            pady=5
        )

        progress.set(
            min(saved / target, 1)
        )

        bottom = ctk.CTkFrame(
            card,
            fg_color="transparent"
        )

        bottom.pack(
            fill="x",
            padx=20,
            pady=(8, 18)
        )

        ctk.CTkLabel(
            bottom,
            text=(
                f"₱{saved:,.2f} saved "
                f"of ₱{target:,.2f}"
            ),
            font=FONTS["small"],
            text_color=(
                COLORS["secondary_text"],
                COLORS["dark_secondary"]
            )
        ).pack(
            side="left"
        )

        if target_date:

            ctk.CTkLabel(
                bottom,
                text=f"Target: {target_date}",
                font=FONTS["small"],
                text_color=(
                    COLORS["secondary_text"],
                    COLORS["dark_secondary"]
                )
            ).pack(
                side="right"
            )

    # =====================================================
    # MESSAGE
    # =====================================================

    def message(self, text):

        dialog = ctk.CTkToplevel(self)

        dialog.title("Finance")

        dialog.geometry(
            "350x160"
        )

        dialog.resizable(
            False,
            False
        )

        dialog.transient(
            self.winfo_toplevel()
        )

        ctk.CTkLabel(
            dialog,
            text=text,
            wraplength=300,
            font=FONTS["body"]
        ).pack(
            pady=30
        )

        ctk.CTkButton(
            dialog,
            text="OK",
            width=100,
            command=dialog.destroy
        ).pack()
