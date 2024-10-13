# import reflex as rx

# class MLConfigState(rx.State):
#     problem_type: str = "Classification"
#     evaluation_metric: str = "Accuracy"
#     training_framework: str = "XGBoost"

#     def set_problem_type(self, value: str):
#         self.problem_type = value

#     def set_evaluation_metric(self, value: str):
#         self.evaluation_metric = value

#     def set_training_framework(self, value: str):
#         self.training_framework = value

# def ml_config_inputs():
#     return rx.vstack(
#         rx.heading("Machine Learning Configuration"),
#         rx.form(
#             rx.vstack(
#                 rx.form_control(
#                     rx.form_label("ML Problem Type"),
#                     rx.select(
#                         ["Classification", "Regression"],
#                         placeholder="Select problem type",
#                         on_change=MLConfigState.set_problem_type,
#                         value=MLConfigState.problem_type,
#                     ),
#                 ),
#                 rx.form_control(
#                     rx.form_label("Evaluation Metric"),
#                     rx.select(
#                         ["Accuracy", "F1 Score", "Log Loss", "Precision", "ROC/AUC"],
#                         placeholder="Select evaluation metric",
#                         on_change=MLConfigState.set_evaluation_metric,
#                         value=MLConfigState.evaluation_metric,
#                     ),
#                 ),
#                 rx.form_control(
#                     rx.form_label("Training Framework"),
#                     rx.select(
#                         ["XGBoost", "LightGBM", "Scikit-learn", "Random Forest"],
#                         placeholder="Select training framework",
#                         on_change=MLConfigState.set_training_framework,
#                         value=MLConfigState.training_framework,
#                     ),
#                 ),
#                 rx.button("Submit", type_="submit"),
#             ),
#             on_submit=rx.window_alert(f"Submitted: {MLConfigState.problem_type}, {MLConfigState.evaluation_metric}, {MLConfigState.training_framework}"),
#         ),
#         rx.divider(),
#         rx.heading("Current Configuration"),
#         rx.text(f"Problem Type: {MLConfigState.problem_type}"),
#         rx.text(f"Evaluation Metric: {MLConfigState.evaluation_metric}"),
#         rx.text(f"Training Framework: {MLConfigState.training_framework}"),
#         width="100%",
#         max_width="400px",
#         spacing="4",
#     )

# def index():
#     return rx.center(
#         ml_config_inputs(),
#         padding="20px",
#     )


import reflex as rx

class MLConfigState(rx.State):
    problem_type: str = "Classification"
    prediction_target: str = "brand"
    evaluation_metric: str = "R-Squared"
    training_framework: str = "XGBoost"

 

def ml_config_view() -> rx.Component:
    return rx.vstack(
        rx.heading("ML Configuration"),
        rx.divider(width="100%"),

        rx.vstack(
            rx.hstack(
                rx.icon("codesandbox", color="#6439FF"),
                rx.heading("ML Problem Type", size="5"),
                align="center",
            ),
            rx.select(
                ["Classification", "Regression"],
                placeholder="ML Problem Type",
                label="ML Problem Type",
                value=MLConfigState.problem_type,
                on_change=MLConfigState.set_problem_type,
                color="#6439FF",
                radius="full",
                width="50%",
                # variant="soft",

            ),
            width="100%",
            margin_bottom="30px"
        ),
        rx.vstack(
            rx.hstack(
                rx.icon("crosshair",  color="#6439FF"),
                rx.heading("Prediction Target", size="5"),
                align="center",
            ),
            rx.select(
                ["brand", "model", "model_year", "milage", "fuel_type", "engine", "transmission", "price"],
                #milage	fuel_type	engine	transmission	price
                placeholder="Prediction Target",
                label="Prediction Target",
                value=MLConfigState.prediction_target,
                on_change=MLConfigState.set_prediction_target,
                default_value="brand",
                color="#6439FF",
                radius="full",
                width="50%",
            ),
            width="100%",
            margin_bottom="30px"
        ),
        rx.vstack(
            rx.hstack(
                rx.icon("chevrons-right-left",  color="#6439FF"),
                rx.heading("Evaluation Metric", size="5"),
                align="center",
            ),
            rx.select(
                ["Accuracy", "F1 Score", "Log Loss", "Precision", "ROC/AUC", "MSE", "MAE"],
                placeholder="Evaluation Metric",
                label="Evaluation Metric",
                value=MLConfigState.evaluation_metric,
                on_change=MLConfigState.set_evaluation_metric,
                color="#6439FF",
                radius="full",
                width="50%",
            ),
            width="100%",
            margin_bottom="30px"
        ),
        rx.vstack(
            
            rx.hstack(
                rx.icon("cpu", color="#6439FF"),
                rx.heading("Training Framework", size="5"),
                align="center",
            ),
            rx.select(
                ["XGBoost", "LightGBM", "Scikit-learn", "Random Forest"],
                placeholder="Training Framework",
                label="Training Framework",
                value=MLConfigState.training_framework,
                on_change=MLConfigState.set_training_framework,
                color="#6439FF",
                radius="full",
                width="50%",
            ),
            width="100%",
            margin_bottom="30px"

        ),
        spacing="4",
        width="100%",

    )

