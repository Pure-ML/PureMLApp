import reflex as rx
from typing import List, Dict
import csv

class TableState(rx.State):
    """The state class."""

    items: List[Dict[str, str]] = []  # Each item is now a dictionary
    columns: List[str] = []  # Store the column names dynamically

    search_value: str = ""
    sort_value: str = ""
    sort_reverse: bool = False

    total_items: int = 0
    offset: int = 0
    limit: int = 12  # Number of rows per page

    @rx.var(cache=True)
    def filtered_sorted_items(self) -> List[Dict[str, str]]:
        items = self.items

        # Sort items dynamically based on selected column
        if self.sort_value:
            items = sorted(
                items,
                key=lambda item: str(item.get(self.sort_value, "")).lower(),
                reverse=self.sort_reverse,
            )

        # Filter items based on search value
        if self.search_value:
            search_value = self.search_value.lower()
            items = [
                item
                for item in items
                if any(
                    search_value in str(value).lower()
                    for value in item.values()
                )
            ]

        return items

    @rx.var(cache=True)
    def page_number(self) -> int:
        return (self.offset // self.limit) + 1

    @rx.var(cache=True)
    def total_pages(self) -> int:
        return (self.total_items // self.limit) + (
            1 if self.total_items % self.limit else 0
        )

    @rx.var(cache=True, initial_value=[])
    def get_current_page(self) -> List[Dict[str, str]]:
        start_index = self.offset
        end_index = start_index + self.limit
        return self.filtered_sorted_items[start_index:end_index]

    def prev_page(self):
        if self.page_number > 1:
            self.offset -= self.limit

    def next_page(self):
        if self.page_number < self.total_pages:
            self.offset += self.limit

    def first_page(self):
        self.offset = 0

    def last_page(self):
        self.offset = (self.total_pages - 1) * self.limit

    def load_entries(self):
        with open("data.csv", mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            self.items = [row for row in reader]
            self.columns = reader.fieldnames if reader.fieldnames else []
            self.total_items = len(self.items)
            print("Total items:",self.total_items)

    def toggle_sort(self, column: str = None):
        if column:
            if self.sort_value == column:
                self.sort_reverse = not self.sort_reverse
            else:
                self.sort_value = column
                self.sort_reverse = False

