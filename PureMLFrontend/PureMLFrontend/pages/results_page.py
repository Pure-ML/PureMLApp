"""The first page."""

import reflex as rx

from ..templates import template

from ..views.data_lists.ml_spec_data_list import ml_spec_data_list
# from ..views.table import main_table


from .. import styles



@template(route="/results", title="Page1")
def results_page() -> rx.Component:
    """The last page.

    Returns:
        The UI for the results page.
    """

    return rx.hstack(

        rx.box(
            rx.vstack(
                rx.heading("Base Dataset"),
                rx.heading("55%"),
                rx.progress(value=55),

                rx.hstack(
                    rx.heading("55%"),
                    rx.heading("55%"),
                    rx.heading("55%"),
                ),
                rx.button(
                    "Download",
                    on_click=rx.download(
                        url="/path/to/your/file.ext",
                    ),
                ),

                ml_spec_data_list(),

                align="center",

            ), 
            background_color=rx.color("gray", 2),
            border_bottom=styles.border,
            border_top=styles.border,
            border_left=styles.border,
            border_right=styles.border,
            border_radius="20px",
            padding="30px",

                
        ),
        rx.box(
            rx.vstack(
                rx.heading("PureML Enriched Dataset"),
                rx.heading("87%"),
                rx.progress(value=87),

                rx.hstack(
                    rx.heading("55%"),
                    rx.heading("55%"),
                    rx.heading("55%"),
                ),
                rx.button(
                    "Download",
                    on_click=rx.download(
                        url="/path/to/your/file.ext",
                    ),
                ),

                ml_spec_data_list(),

                align="center",
            ),
            background_color=rx.color("gray", 2),
            border_bottom=styles.border,
            border_top=styles.border,
            border_left=styles.border,
            border_right=styles.border,
            border_radius="20px",
            padding="30px",

        ),

        justify="center",
        align="center",
        spacing="4",
        #height="100vh",
        width="100%",
    )