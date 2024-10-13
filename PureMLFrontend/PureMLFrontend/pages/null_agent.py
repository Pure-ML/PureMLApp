

from ..templates import template

import reflex as rx
from ..views.color_picker import primary_color_picker, secondary_color_picker
from ..views.radius_picker import radius_picker
from ..views.scaling_picker import scaling_picker
from ..views.csv_upload import csv_upload_view
# from ..views.table import main_table
from ..backend.table_state import TableState
from ..views.csv_table import main_table
from ..views.upload_and_table import editable_text_example
from ..views.input_path import csv_path_input_example
from ..views.upload_csv import upload_csv
from ..views.pdf_upload import index as pdf_upload
from ..views.automl_settings import ml_config_view as automl_settings
from .landing.index import index as hero

from .. import styles

from ..views.button_stuff import default_class_name, variant_styles, get_variant_class
from reflex.components.datadisplay.dataeditor import DataEditorTheme




import pandas as pd

# Read CSV files
csv_data1 = pd.read_csv("base_dataset.csv")
csv_data2 = pd.read_csv("null_agent_output_dataset.csv")


@template(route="/null_agent", title="NullAgent")
def null_agent() -> rx.Component:
    """The null agent page with two static datatables side by side."""
    return rx.flex(
        rx.box(
                rx.heading(
                    "Null/Missing Value Handling Agent - Utilizing Web Search and Document Search RAG", 
                    size="8",
                    margin_left="20px",
                    margin_right="20px",
                ),
                background_color=rx.color("gray", 2),
                border_bottom=styles.border,
                border_top=styles.border,
                border_left=styles.border,
                border_right=styles.border,
                


                width="100%",
                padding_top="30px",
                padding_bottom="30px",
                margin_bottom="50px",
                border_radius="20px"

        ),
        rx.heading(
            ("User Base Dataset - ")
        ), 
        rx.box(
        rx.data_table(
            data=csv_data1,
            pagination=True,
            search=True,
            sort=True,
            width=["100%", "100%", "48%"],
            # background_color="#6439FF",
            # color="#6439FF"
        ),
            border_radius="20px",
            padding="15px",
            #background_color="#6439FF",
        ),
        rx.heading(
            ("Agent Null-Handling Flow Produced Dataset - ")
        ), 
        rx.box(
        rx.data_table(
            data=csv_data2,
            pagination=True,
            search=True,
            sort=True,
            width=["100%", "100%", "48%"],
        ),
            border_radius="20px",
            padding="15px",
            background_color="#0ec789",
        ),
        rx.button(
                "Next Step",
                on_click=rx.redirect("/column_agent"),
                class_name=default_class_name
                    + " "
                    + variant_styles["primary"]["class_name"]
                    + " "
                    + get_variant_class("indigo"),
            ),
        width="100%",
        spacing="4",
        flex_wrap="wrap",
    )
