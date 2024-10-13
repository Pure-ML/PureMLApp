import reflex as rx
import pandas as pd
import os

class CSVUploadState(rx.State):
    csv_data: list = []
    error_message: str = ""
    df: pd.DataFrame = pd.DataFrame()

    @rx.var
    def df_not_empty(self) -> bool:
        """Return the CSV path to be used by the component."""
        value = self.df.empty
        print("df_not_empty:", value)

        if value == True: 
            return False 
        return True
    
    @rx.var
    def get_df(self) -> pd.DataFrame: 
        return self.df

    async def handle_csv_upload(self, files: list[rx.UploadFile]):
        if not files:
            self.error_message = "No file was uploaded."
            return

        file = files[0]
        try:
            contents = await file.read()
            upload_dir = rx.get_upload_dir()
            file_path = os.path.join(upload_dir, file.filename)
            print("File Path:", file_path)
            
            with open(file_path, "wb") as f:
                f.write(contents)

            self.df = pd.read_csv(file_path)
            self.error_message = ""
        except Exception as e:
            self.error_message = f"Error reading CSV: {str(e)}"

def csv_upload_view():
    return rx.vstack(
        rx.heading("CSV Uploader and Viewer"),
        rx.upload(
            rx.vstack(
                rx.button("Select CSV File"),
                rx.text("Or drag and drop here"),
                padding="2em",
                border="2px dashed",
                border_color="gray.300",
                border_radius="md",
            ),
            multiple=False,
            accept={".csv": ["text/csv"]},
            max_files=1,
        ),
        rx.button(
            "Upload CSV",
            on_click=lambda: CSVUploadState.handle_csv_upload(rx.upload_files()),
        ),
        rx.cond(
            CSVUploadState.error_message != "",
            rx.text(CSVUploadState.error_message, color="blue"),
        ),
        rx.cond(
            CSVUploadState.df_not_empty,
            # rx.data_table(
            #     data=CSVUploadState.df,
            #     pagination=True,
            #     search=True,
            #     sort=True,
            # ),
            rx.data_table(
                data=CSVUploadState.get_df,
                pagination=True,
                search=True,
                sort=True,
            ),
            rx.text("No CSV data loaded yet."),
        ),
        width="100%",
        spacing="4",
    )

def upload_csv():
    return rx.vstack(
        csv_upload_view(),
        width="100%",
        padding="20px",
    )