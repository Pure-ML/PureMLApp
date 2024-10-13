import reflex as rx
from .. import styles


def footer():
    return rx.box(
        rx.spacer(),
        rx.text("Built by the DataSmiths 0__0"),
        padding="1em",
        background_color=rx.color("gray", 1),
        text_align="center",
        width="100%",
        # position="sticky",
        bottom="0px",
        border_top=styles.border,
        margin_top="20px",


    )