import reflex as rx
from ..backend.csv_table_state import TableState


def _header_cell(text: str) -> rx.Component:
    """Creates a table header cell for a given column name."""
    return rx.table.column_header_cell(
        rx.text(text, font_weight="bold"),
        align="center"
    )


def _show_item(item: dict) -> rx.Component:
    """Creates a table row with cells for each value in the item dictionary."""
    return rx.table.row(
        rx.foreach(
            item.values(),
            lambda value: rx.table.cell(rx.text(str(value))),
        ),
        align="center",
    )


def _pagination_view() -> rx.Component:
    """Creates pagination controls."""
    return rx.hstack(
        rx.text(
            "Page ",
            rx.code(TableState.page_number),
            f" of {TableState.total_pages}",
            justify="end",
        ),
        rx.icon_button(
            rx.icon("chevrons-left", size=18),
            on_click=TableState.first_page,
            opacity=rx.cond(TableState.page_number == 1, 0.6, 1),
            color_scheme=rx.cond(TableState.page_number == 1, "gray", "accent"),
            variant="soft",
        ),
        rx.icon_button(
            rx.icon("chevron-left", size=18),
            on_click=TableState.prev_page,
            opacity=rx.cond(TableState.page_number == 1, 0.6, 1),
            color_scheme=rx.cond(TableState.page_number == 1, "gray", "accent"),
            variant="soft",
        ),
        rx.icon_button(
            rx.icon("chevron-right", size=18),
            on_click=TableState.next_page,
            opacity=rx.cond(TableState.page_number == TableState.total_pages, 0.6, 1),
            color_scheme=rx.cond(TableState.page_number == TableState.total_pages, "gray", "accent"),
            variant="soft",
        ),
        rx.icon_button(
            rx.icon("chevrons-right", size=18),
            on_click=TableState.last_page,
            opacity=rx.cond(TableState.page_number == TableState.total_pages, 0.6, 1),
            color_scheme=rx.cond(TableState.page_number == TableState.total_pages, "gray", "accent"),
            variant="soft",
        ),
        spacing="5",
        margin_top="1em",
        align="center",
        width="100%",
        justify="end",
    )


def main_table() -> rx.Component:
    """Main function to render the table with dynamic columns and pagination."""
    return rx.box(
        rx.table.root(
            rx.table.header(
                rx.table.row(
                    rx.foreach(
                        TableState.columns,
                        lambda col: _header_cell(col),
                    )
                ),
            ),
            rx.table.body(
                rx.foreach(
                    TableState.get_current_page,
                    lambda item: _show_item(item),
                )
            ),
            variant="surface",
            size="3",
            width="100%",
        ),
        _pagination_view(),
        width="100%",
    )
