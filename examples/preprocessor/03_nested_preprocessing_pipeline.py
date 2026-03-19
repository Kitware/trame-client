"""
Trame example that checks an input DICOM file patient tag against a patient name in the trame state.
"""

from pathlib import Path
from typing import Literal

from trame.app import get_server
from trame.ui.vuetify3 import SinglePageLayout

from trame.widgets import client, vuetify3

server = get_server()

server.state.patient_name = "John Doe"


def preprocessing_pipeline_completed(
    type: Literal["success", "failure"], output
) -> None:
    print("preprocessing_pipeline_completed")
    print(type)
    print(output)


DICOM_UTILS_SCRIPT = Path(__file__).with_name("dicom_utils.js")

patient_name_validator = client.PreProcessor.register_preprocessing_unit(
    name="validate_dicom_patient_name",
    module_script=DICOM_UTILS_SCRIPT,
    function_name="validateDicomFilePatientName",
)

dcm_to_nifti_convertor = client.PreProcessor.register_preprocessing_unit(
    name="generate_nifti_from_dicom_file_set",
    module_script=DICOM_UTILS_SCRIPT,
    function_name="generateNIFTIFromDicomFileSet",
)


with SinglePageLayout(server) as ui:
    ui.title.set_text("Nested Pipeline")

    with (
        ui.content,
        vuetify3.VContainer(fluid=True, classes="pa-0 fill-height"),
        client.PreProcessor(
            variable="validated_dicom_file",
            preprocessor=dcm_to_nifti_convertor,
            inputs=("{ output_file_name: 'my_converted_file.nii' }",),
            completed=(
                preprocessing_pipeline_completed,
                "[$event.type, $event.outputs]",
            ),
        ),
        client.PreProcessor(
            variable="input_dicom_fileset",
            preprocessor=patient_name_validator,
            inputs=("{ patient_name }",),
            success="validated_dicom_file.value = $event",
            failure="console.log($event)",
        ),
    ):
        vuetify3.VFileInput(
            v_model="input_dicom_fileset.value",
        )

server.start()
