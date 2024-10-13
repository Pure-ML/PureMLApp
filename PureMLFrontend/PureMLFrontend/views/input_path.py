import reflex as rx
import pandas as pd
import os
from .button_stuff import default_class_name, variant_styles, get_variant_class





class CSVPathInput(rx.ComponentState):
    path: str = "data.csv"
    csv_data: list = []
    error_message: str = ""
    df: pd.DataFrame

    def load_csv(self):
        if not self.path:
            self.error_message = "Please enter a CSV path."
            return

        try:
            if os.path.exists(self.path):
                print("SELF.PATH:", self.path)
                df = pd.read_csv(self.path)

                self.df = df
                self.error_message = ""
            else:
                self.error_message = f"File not found: {self.path}"
        except Exception as e:
            self.error_message = f"Error reading CSV: {str(e)}"

    @classmethod
    def get_component(cls, **props):
        return rx.vstack(
            rx.hstack(
                rx.input(
                    value=cls.path,
                    on_change=cls.set_path,
                    placeholder="Enter CSV path",
                    width="100%",
                ),
                rx.button(
                    "Load CSV", 
                    on_click=cls.load_csv,
                    class_name=default_class_name
                    + " "
                    + variant_styles["primary"]["class_name"]
                    + " "
                    + get_variant_class("indigo"),

                ),
            ),
            rx.cond(
                cls.error_message != "",
                rx.text(cls.error_message, color="red"),
            ),
            rx.cond(
                cls.csv_data != [],
      
                rx.data_table(
                    data=cls.df,
                    pagination=True,
                    search=True,
                    sort=True,
                ),
             
                rx.text("No CSV data loaded yet.")
            ),
            width="100%",
            spacing="4",
        )

csv_path_input = CSVPathInput.create

def csv_path_input_example():
    return rx.vstack(
        rx.heading("Dataset"),
        rx.divider(width="100%"),

        csv_path_input(),
        width="100%",
        spacing="4",
    )