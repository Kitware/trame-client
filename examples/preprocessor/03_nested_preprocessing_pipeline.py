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

        self.patient_name_validator = client.PreProcessor.register_preprocessing_unit(
            name="validate_dicom_patient_name",
            module_script=DICOM_UTILS_SCRIPT,
            function_name="validateDicomFilePatientName",
        )

        self.dcm_to_nifti_convertor = client.PreProcessor.register_preprocessing_unit(
            name="generate_nifti_from_dicom_file_set",
            module_script=DICOM_UTILS_SCRIPT,
            function_name="generateNIFTIFromDicomFileSet",
        )

        self._build_ui()

    def _build_ui(self):
        with SinglePageLayout(self.server) as ui:
            ui.title.set_text("Nested Pipeline")

            with (
                ui.content,
                vuetify3.VContainer(fluid=True, classes="pa-0 fill-height"),
                client.PreProcessor(
                    variable="validated_dicom_file",
                    preprocessor=self.dcm_to_nifti_convertor,
                    inputs=("{ output_file_name: 'my_converted_file.nii' }",),
                    completed=(
                        self.preprocessing_pipeline_completed,
                        "[$event.type, $event.outputs]",
                    ),
                ),
                client.PreProcessor(
                    variable="input_dicom_fileset",
                    preprocessor=self.patient_name_validator,
                    inputs=("{ patient_name }",),
                    success="validated_dicom_file.value = $event",
                    failure="console.log($event)",
                ),
            ):
                vuetify3.VFileInput(
                    v_model="input_dicom_fileset.value",
                )

    def preprocessing_pipeline_completed(
        self, type: Literal["success", "failure"], output
    ) -> None:
        print("preprocessing_pipeline_completed")
        print(type)
        print(output)


def main(**kwargs):
    app = DicomProcessingPipeline()
    app.server.start(**kwargs)


if __name__ == "__main__":
    main()
