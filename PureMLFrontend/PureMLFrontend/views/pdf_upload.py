import reflex as rx
from typing import Literal, Callable



LiteralButtonVariant = Literal[
    "primary", "success", "destructive", "secondary", "muted"
]

default_class_name = "font-smbold rounded-xl cursor-pointer inline-flex items-center justify-center px-[0.875rem] py-2 relative transition-bg border-t border-[rgba(255,255,255,0.21)]"

after_class_name = "after:absolute after:inset-[1px] after:border-t after:rounded-[11px] after:border-white after:opacity-[0.22]"


def get_variant_class(variant: str) -> str:
    return (
        f"bg-gradient-to-b from-[--{variant}-9] to-[--{variant}-9] hover:to-[--{variant}-10] text-white"
        + " "
    )


variant_styles = {

    # "primary": {
    #     "class_name": get_variant_class("violet"),
    # },
    "primary": {
        "class_name": get_variant_class("indigo"),
    },
    "success": {
        "class_name": get_variant_class("green"),
    },
    "destructive": {
        "class_name": get_variant_class("red"),
    },
    "muted": {
        "class_name": "bg-slate-3 hover:bg-slate-5 text-slate-9 border-t !border-slate-5",
    },
    "secondary": {
        "class_name": "bg-slate-4 hover:bg-slate-5 text-slate-10 !border-none",
    },
}


class State(rx.State):
    """The app state."""

    # The images to show.
    img: list[str]

    async def handle_upload(
        self, files: list[rx.UploadFile]
    ):
        """Handle the upload of file(s).

        Args:
            files: The uploaded files.
        """
        for file in files:
            upload_data = await file.read()
            outfile = rx.get_upload_dir() / file.filename

            # Save the file.
            with outfile.open("wb") as file_object:
                file_object.write(upload_data)

            # Update the img var.
            self.img.append(file.filename)

# color = "rgb(107,99,246)"
color = "#5271ff"



def index():
    """The main view."""
    return rx.vstack(
        rx.heading(
            "RAG Powering Context Documents"
        ),
        rx.divider(width="100%"),

        rx.upload(
            rx.vstack(
                rx.button(
                    "Select File",
                    color=color,
                    bg="white",
                    border=f"1px solid {color}",
                ),
                rx.text(
                    "Drag and drop files here or click to select files"
                ),
            ),
            id="upload1",
            border=f"1px dotted {color}",
            padding="5em",
        ),
        rx.hstack(
            rx.foreach(
                rx.selected_files("upload1"), rx.text
            )
        ),
        rx.button(
            "Upload",
            on_click=State.handle_upload(
                rx.upload_files(upload_id="upload1")
            ),
     
            class_name=default_class_name
            + " "
            + variant_styles["primary"]["class_name"]
            + " "
            + get_variant_class("indigo"),
        ),
        rx.button(
            "Clear",
            on_click=rx.clear_selected_files("upload1"),
            class_name=default_class_name
            + " "
            + variant_styles["primary"]["class_name"]
            + " "
            + get_variant_class("indigo"),
        ),

        rx.foreach(
            State.img,
            lambda img: rx.image(
                src=rx.get_upload_url(img)
            ),
        ),
        # padding="5em",
        width="100%",
        spacing="4"
    )