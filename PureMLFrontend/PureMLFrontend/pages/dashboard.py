"""The dashboard page."""

from ..templates import template
from ..backend.table_state import TableState
# from ..views.table import main_table
from ..views.csv_table import main_table


import reflex as rx


@template(route="/dashboard", title="Dashboard", on_load=TableState.load_entries)
def dashboard() -> rx.Component:
    """The dashboard page.

    Returns:
        The UI for the dashboard page.
    """
    return rx.vstack(
        rx.heading("CI Job Dashboard", size="5"),
        main_table(),
        spacing="8",
        width="100%",
    )
