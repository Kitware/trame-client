"""
Trame example that checks an input DICOM file patient tag against a patient name in the trame state.
"""

from pathlib import Path
from typing import Literal

from trame.app import TrameApp
from trame.ui.vuetify3 import SinglePageLayout

from trame.widgets import client, vuetify3, html

# 1 - lookup the path of your JS file that contains your preprocessing logic
DICOM_UTILS_SCRIPT = Path(__file__).with_name("dicom_utils.js")


class PatientNameValidator(TrameApp):
    def __init__(self, server=None):
        super().__init__(server)

        self.state.patient_name = "John Doe"

        # 2 - register your JS file and entrypoint function using trame_client.Handler module API
        client.register_external_script(
            name="validate_dicom_patient_name",
            script_file_path=DICOM_UTILS_SCRIPT,
            function_names=["validateDicomFilePatientName"],
        )

        self._build_ui()

    def _build_ui(self):
        with SinglePageLayout(self.server) as self.ui:
            self.ui.title.set_text("Client Handler Preprocessing Minimal Example")

            with (
                self.ui.content,
                vuetify3.VContainer(fluid=True),
                vuetify3.VRow(),
                vuetify3.VCol(cols=3),
                # 3. Instantiate the PreProcessor widget
                client.Handler(
                    function="validate_dicom_patient_name",
                    # 4. Pass additional inputs to your preprocessing logic
                    # those must match your function signature in the JS logic file
                    # this is a JS expression that will be passed as is to your function
                    inputs=("{ patient_name }",),
                    # 5. Register a callback to be run when your preprocessing is completed
                    completed=(
                        self.preprocessing_pipeline_completed,
                        "[$event.type, $event.outputs]",
                    ),
                ) as client_handler,
            ):
                with html.Div(style="display: flex; flex-direction: column;"):
                    vuetify3.VFileInput(
                        # 6. Use the provided input_data from the widget to trigger the preprocessing on it
                        # preprocessing.input_data is a provided slot scopped reactive value
                        # which is observed by the PreProcessor component
                        # it should be assigned with whatever data your want to run preprocessing on
                        v_model=client_handler.input_data,
                        hint="Input here a DICOM file",
                        label="DICOM file",
                        persistent_hint=True,
                    )

                    vuetify3.VTextField(
                        v_model="patient_name",
                        hint="Input here the patient name that you expect for your DICOM file",
                        label="Expected Patient Name",
                        persistent_hint=True,
                    )

                    vuetify3.VAlert(
                        v_if="alert_title",
                        text=("alert_text", None),
                        title=("alert_title", None),
                        type=("alert_type", None),
                    )

    def preprocessing_pipeline_completed(
        self, type: Literal["success", "failure"], output
    ) -> None:
        print("preprocessing_pipeline_completed")
        print(type)
        print(output)

        self.state.alert_type = type if type == "success" else "error"
        self.state.alert_title = self.state.alert_type

        if type == "failure":
            self.state.alert_text = (
                f"Expected patient {output[0]['expected']}, got {output[0]['got']}"
            )
        else:
            self.state.alert_text = "Patient name matched! We got the file."


def main(**kwargs):
    app = PatientNameValidator()
    app.server.start(**kwargs)


if __name__ == "__main__":
    main()
