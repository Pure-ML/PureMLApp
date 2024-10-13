import reflex as rx



def ml_spec_data_list() -> rx.Component:
    return(
        rx.card(
            rx.data_list.root(
                rx.data_list.item(
                    rx.data_list.label("ML Problem Type"),
                    rx.data_list.value(
                        rx.badge(
                            "Classification",
                            variant="soft",
                            radius="full",
                        )
                    ),
                    align="center",
                ),
                rx.data_list.item(
                    rx.data_list.label("Prediction Target"),
                    rx.data_list.value(rx.code("price_col")),
                ),
                rx.data_list.item(
                    rx.data_list.label("Evaluation Metric"),
                    rx.data_list.value("Log-loss"),
                    align="center",
                ),
                rx.data_list.item(
                    rx.data_list.label("Training Framework"),
                    rx.data_list.value("XGBoost"),
                ),
                
            ),
        ),
    )