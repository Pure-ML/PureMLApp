
import reflex as rx
import pandas as pd
from typing import List


class EditableText(rx.ComponentState):
    text: str = "Click to edit"
    original_text: str
    editing: bool = False

    def start_editing(self, original_text: str):
        self.original_text = original_text
        self.editing = True

    def stop_editing(self):
        self.editing = False
        self.original_text = ""

    @classmethod
    def get_component(cls, **props):
        # Pop component-specific props with defaults before passing **props
        value = props.pop("value", cls.text)
        on_change = props.pop("on_change", cls.set_text)
        cursor = props.pop("cursor", "pointer")

        # Set the initial value of the State var.
        initial_value = props.pop("initial_value", None)
        if initial_value is not None:
            # Update the pydantic model to use the initial value as default.
            cls.__fields__["text"].default = initial_value

        # Form elements for editing, saving and reverting the text.
        edit_controls = rx.hstack(
            rx.input(
                value=value,
                on_change=on_change,
                **props,
            ),
            rx.icon_button(
                rx.icon("x"),
                on_click=[
                    on_change(cls.original_text),
                    cls.stop_editing,
                ],
                type="button",
                color_scheme="red",
            ),
            rx.icon_button(rx.icon("check")),
            align="center",
            width="100%",
        )

        # Return the text or the form based on the editing Var.
        return rx.cond(
            cls.editing,
            rx.form(
                edit_controls,
                on_submit=lambda _: cls.stop_editing(),
            ),
            rx.text(
                value,
                on_click=cls.start_editing(value),
                cursor=cursor,
                **props,
            ),
        )









class CsvTable(rx.ComponentState):
    text: str = "Click to edit"
    original_text: str
    editing: bool = False

    csv_uploaded: bool = False

    csv: List[str] = []
    csv_path: str = "https://media.geeksforgeeks.org/wp-content/uploads/nba.csv"  # State variable to store the CSV file path

    
    def change_csv_path(self, new_path : str):
        print("New Path:", new_path)
        self.csv_path = new_path
        self.csv_uploaded = True 

    async def handle_upload(self, files: List[rx.UploadFile]):
        """Handle the upload of file(s)."""
        for file in files:
            upload_data = await file.read()
            outfile = rx.get_upload_dir() / file.filename

            # Save the file
            with outfile.open("wb") as file_object:
                file_object.write(upload_data)

            # Update the CSV path state


            #self.csv.append(file.filename)
            self.change_csv_path(str(outfile))
            #self.csv_path = str(outfile)  # Store the path of the uploaded CSV

            print("CSV Path updated to:", self.csv_path)

    def start_editing(self, original_text: str):
        self.original_text = original_text
        self.editing = True

    def stop_editing(self):
        self.editing = False
        self.original_text = ""

    @rx.var
    def get_text(self) -> str:
        """A computed var that returns the current color."""
        # Computed vars update automatically when the state changes.
        return self.text
    
    @rx.var 
    def get_csv_path(self) -> str: 
        return self.csv_path

    @classmethod
    def get_component(cls, **props):
        # Pop component-specific props with defaults before passing **props
        value = props.pop("value", cls.text)
        print("Cls text:", cls.get_text)
        on_change = props.pop("on_change", cls.set_text)
        cursor = props.pop("cursor", "pointer")

        # Set the initial value of the State var.
        initial_value = props.pop("initial_value", None)
        if initial_value is not None:
            # Update the pydantic model to use the initial value as default.
            cls.__fields__["text"].default = initial_value

        # Form elements for editing, saving and reverting the text.
        edit_controls = rx.hstack(
            rx.input(
                value=value,
                on_change=on_change,
                **props,
            ),
            rx.icon_button(
                rx.icon("x"),
                on_click=[
                    on_change(cls.original_text),
                    cls.stop_editing,
                ],
                type="button",
                color_scheme="red",
            ),
            rx.icon_button(rx.icon("check")),
            align="center",
            width="100%",
        )


        upload_controls = rx.vstack(
            rx.upload(
            rx.vstack(
                rx.button(
                    "Select File",
                    color=color,
                    bg="white",
                    border=f"1px solid {color}",
                ),
                rx.text("Drag and drop files here or click to select files"),
            ),
            id="upload1",
            border=f"1px dotted {color}",
            padding="5em",
            ),
            # Display selected files
            rx.hstack(
                rx.foreach(
                    rx.selected_files("upload1"), rx.text
                )
            ),
            # Upload Button
            rx.button(
                "Upload",
                on_click= cls.handle_upload(
                    rx.upload_files(upload_id="upload1")
                ),
            ),
        )

        # csv_table = rx.vstack(
        #     rx.data_table(
        #         data=pd.read_csv(cls.text),
        #         pagination=True,
        #         search=True,
        #         sort=True,
        #     )
        # )

        # Return the text or the form based on the editing Var.
        # return rx.cond(
        #     cls.editing,
        #     rx.form(
        #         edit_controls,
        #         on_submit=lambda _: cls.stop_editing(),
        #     ),
        #     rx.text(
        #         value,
        #         on_click=cls.start_editing(value),
        #         cursor=cursor,
        #         **props,
        #     ),
        # )

        return rx.cond(
            cls.csv_uploaded, 
            upload_controls, 
            upload_controls
            # csv_table

        )


editable_text = EditableText.create
csv_table = CsvTable.create


color = "rgb(107,99,246)"


def editable_text_example():
    return rx.vstack(
        
        editable_text(),
        editable_text(
            initial_value="Edit me!", color="blue"
        ),
        editable_text(
            initial_value="Reflex is fun",
            font_family="monospace",
            width="100%",
        ),

        csv_table()
    )