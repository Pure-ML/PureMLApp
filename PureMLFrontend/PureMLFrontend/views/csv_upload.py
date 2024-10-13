# import reflex as rx
# from .table import csv_table

# class State(rx.State):
#     """The app state."""

#     # The images to show.
#     csv: list[str]

    

#     async def handle_upload(
#         self, files: list[rx.UploadFile]
#     ):
#         """Handle the upload of file(s).

#         Args:
#             files: The uploaded files.
#         """
#         print("handle_upload()..")
#         for file in files:
#             upload_data = await file.read()
#             outfile = rx.get_upload_dir() / file.filename

#             # Save the file.
#             with outfile.open("wb") as file_object:
#                 file_object.write(upload_data)

#             # Update the file var.
#             self.csv.append(file.filename)


# color = "rgb(107,99,246)"


# def csv_upload_view():
#     """The main view."""
#     return rx.vstack(
#         rx.upload(
#             rx.vstack(
#                 rx.button(
#                     "Select File",
#                     color=color,
#                     bg="white",
#                     border=f"1px solid {color}",
#                 ),
#                 rx.text(
#                     "Drag and drop files here or click to select files"
#                 ),
#             ),
#             id="upload1",
#             border=f"1px dotted {color}",
#             padding="5em",
#         ),
#         rx.hstack(
#             rx.foreach(
#                 rx.selected_files("upload1"), rx.text
#             )
#         ),
#         rx.button(
#             "Upload",
#             on_click=State.handle_upload(
#                 rx.upload_files(upload_id="upload1")
#             ),
           
#         ),
#         rx.button(
#             "Clear",
#             on_click=rx.clear_selected_files("upload1"),
#         ),


#         csv_table("https://media.geeksforgeeks.org/wp-content/uploads/nba.csv"),

#         padding="5em",
#     )




# import reflex as rx
# import pandas as pd
# from typing import List
# # from .table import csv_table

# class State(rx.State):
#     """The csv upload process state."""

#     # The csvs.
#     csv: list[str]
#     csv_path: str = ""  # New state variable to store the CSV file path

#     async def handle_upload(
#         self, files: list[rx.UploadFile]
#     ):
#         """Handle the upload of file(s)."""
#         for file in files:
#             upload_data = await file.read()
#             outfile = rx.get_upload_dir() / file.filename

#             # Save the file.
#             with outfile.open("wb") as file_object:
#                 file_object.write(upload_data)

#             # Update the file var.

#             self.csv.append(file.filename)
#             self.csv_path = str(outfile)  # Store the path of the uploaded CSV

#             print("CSV PATH:", self.csv_path)

#             self.csv_path = 'uploaded_files/sample_submission.csv'
    
#     @rx.var
#     def get_csv_path(self) -> str:
#         print("get_csv_path:", self.csv_path)
#         return self.csv_path
    

#     @classmethod
#     def get_component(cls, **props):
#         print()
    

            

# color = "rgb(107,99,246)"



# def csv_upload_view():
#     """The main view."""
#     return rx.vstack(
#         rx.upload(
#             rx.vstack(
#                 rx.button(
#                     "Select File",
#                     color=color,
#                     bg="white",
#                     border=f"1px solid {color}",
#                 ),
#                 rx.text(
#                     "Drag and drop files here or click to select files"
#                 ),
#             ),
#             id="upload1",
#             border=f"1px dotted {color}",
#             padding="5em",
#         ),
#         rx.hstack(
#             rx.foreach(
#                 rx.selected_files("upload1"), rx.text
#             )
#         ),
#         rx.button(
#             "Upload",
#             on_click=State.handle_upload(
#                 rx.upload_files(upload_id="upload1")
#             ),
            
#         ),
#         rx.button(
#             "Clear",
#             on_click=rx.clear_selected_files("upload1"),
#         ),
#         rx.cond(
#             1==1,
#             csv_table(""),
#             print("Cond Failed...")
#         ),
#         csv_table(State.get_csv_path),
#         padding="5em",
#     )



# def csv_table(data_url):
#     print("DATE URL:", data_url)
#     data_csv = pd.read_csv(
#         "https://media.geeksforgeeks.org/wp-content/uploads/nba.csv"
#         # data_url
#     )

#     return rx.data_table(
#         data=data_csv,
#         pagination=True,
#         search=True,
#         sort=True,
#     )



import reflex as rx
import pandas as pd
from typing import List

class State(rx.State):
    """The CSV upload process state."""

    csv: List[str] = []
    csv_path: str = "https://media.geeksforgeeks.org/wp-content/uploads/nba.csv"  # State variable to store the CSV file path

    async def handle_upload(self, files: List[rx.UploadFile]):
        """Handle the upload of file(s)."""
        for file in files:
            upload_data = await file.read()
            outfile = rx.get_upload_dir() / file.filename

            # Save the file
            with outfile.open("wb") as file_object:
                file_object.write(upload_data)

            # Update the CSV path state
            self.csv.append(file.filename)
            self.csv_path = str(outfile)  # Store the path of the uploaded CSV
            print("CSV Path updated to:", self.csv_path)
    
    @rx.var
    def get_csv_path(self) -> str:
        """Return the CSV path to be used by the component."""
        #:", self.csv_path)
        return self.csv_path


color = "rgb(107,99,246)"


def csv_upload_view():
    """The main view."""
    return rx.vstack(
        # CSV Upload Section
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
            on_click=State.handle_upload(
                rx.upload_files(upload_id="upload1")
            ),
        ),
        # Clear Button
        rx.button(
            "Clear",
            on_click=rx.clear_selected_files("upload1"),
        ),

       
        # Conditionally Render csv_table if csv_path is set
        # rx.cond(
        #     State.csv_path,
        #     lambda: csv_table(State.csv_path),
        #     rx.text("No CSV file uploaded.", color="gray")
        # ),
        csv_table(),
        padding="5em",
    )


def csv_table():
    data_url = State.csv_path
    """Creates a data table from the uploaded CSV file."""
    print("DATA URL:", data_url)
    print("get_csv_path:", State.get_csv_path)
    data_url = "https://media.geeksforgeeks.org/wp-content/uploads/nba.csv"
    # Check if data_url is valid before loading
    if data_url:
        data_csv = pd.read_csv(data_url)
        return rx.data_table(
            data=data_csv,
            pagination=True,
            search=True,
            sort=True,
        )
    else:
        return rx.text("No data available.", color="gray")
