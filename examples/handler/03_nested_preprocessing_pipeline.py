"""
Trame example that checks an input DICOM file patient tag against a patient name in the trame state.
"""

from pathlib import Path
from typing import Literal

from trame.app import TrameApp
from trame.ui.vuetify3 import SinglePageLayout

from trame.widgets import client, vuetify3

DICOM_UTILS_SCRIPT = Path(__file__).with_name("dicom_utils.js")


class DicomProcessingPipeline(TrameApp):
    def __init__(self, server=None):
        super().__init__(server)

        self.state.patient_name = "John Doe"

        # Mark your state as client_only!
        self.state.client_only("dicom_file_set")

        self.dicom_utils_preprocessor = client.register_external_script(
            DICOM_UTILS_SCRIPT,
            name="dicom_utils",
            function_names=[
                "validateDicomFilePatientName",
                "generateNIFTIFromDicomFileSet",
            ],
        )

        self._build_ui()

    def _build_ui(self):
        with SinglePageLayout(self.server) as ui:
            ui.title.set_text("Nested Pipeline")

            with (
                ui.content,
                vuetify3.VContainer(fluid=True),
                vuetify3.VRow(),
                vuetify3.VCol(cols=3),
                client.Handler(
                    variable="validated_dicom_file",
                    function=("dicom_utils", "generateNIFTIFromDicomFileSet"),
                    inputs=("{ output_file_name: 'my_converted_file.nii' }",),
                    completed=(
                        self.preprocessing_pipeline_completed,
                        "[$event.type, $event.outputs]",
                    ),
                ),
                client.Handler(
                    variable="input_dicom_fileset",
                    function=self.dicom_utils_preprocessor.function(
                        "validateDicomFilePatientName"
                    ),
                    inputs=("{ patient_name }",),
                    success="validated_dicom_file.value = $event",
                    failure=(self.on_patient_name_failure, "[$event]"),
                ),
            ):
                vuetify3.VFileInput(
                    v_model="input_dicom_fileset.value",
                    label="DICOM files",
                    hint="""
                        Input here a single DICOM file that will be patient name checked
                        and then converted to a single NIFTI file.
                    """,
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

    def on_patient_name_failure(self, output):
        print(output)
        self.state.alert_type = "error"
        self.state.alert_title = self.state.alert_type
        self.state.alert_text = (
            f"Expected patient {output[0]['expected']}, got {output[0]['got']}"
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
            self.state.alert_text = "Failed to convert to NIFTI file."
        else:
            self.state.alert_text = (
                "Patient name matched! We got the converted NIFTI file."
            )


def main(**kwargs):
    app = DicomProcessingPipeline()
    app.server.start(**kwargs)


if __name__ == "__main__":
    main()
