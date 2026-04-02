from pathlib import Path

from trame.app import TrameApp
from trame.app.file_upload import ClientFile
from trame.ui.vuetify3 import SinglePageLayout

from trame.widgets import client, html, vuetify3

DICOM_UTILS_SCRIPT = Path(__file__).with_name("dicom_utils.js")


class DicomToNiftiConvertor(TrameApp):
    def __init__(self, server=None):
        super().__init__(server)

        self.state.dicom_file_set = None
        self.state.error_message = ""
        self.state.is_error = False

        # Mark your state as client_only!
        self.state.client_only("dicom_file_set")

        client.PreProcessor.register_preprocessing_unit(
            name="generate_nii_from_dcm",
            module_script=DICOM_UTILS_SCRIPT,
            function_name="generateNIFTIFromDicomFileSet",
        )

        self._build_ui()

    def _build_ui(self):
        with SinglePageLayout(self.server) as self.ui:
            self.ui.title.set_text("Explicit Pipeline Trigger")

            with (
                self.ui.content,
                vuetify3.VContainer(fluid=True, classes="pa-0 fill-height"),
            ):
                with vuetify3.VCard():
                    with (
                        vuetify3.VSnackbar(
                            v_model=("is_error",),
                            color="error",
                            location="bottom left",
                            close_on_content_click=True,
                            timeout=6000,
                        ),
                        html.Div(style="align-items: center;"),
                    ):
                        vuetify3.VIcon("mdi-information", style="margin-right: 12px")
                        html.Span("{{ error_message }}")

                    vuetify3.VFileInput(v_model="dicom_file_set", multiple=True)

                    with client.PreProcessor(
                        preprocessor="generate_nii_from_dcm",
                        inputs=("{ output_file_name: 'my_converted_file.nii' }",),
                        # success event for the logic happy path
                        success=(self.save_nifti_file, "[$event]"),
                        # failure event for the logic error path (e.g. invalid data)
                        failure=(self.handle_nifti_convertion_error, "[$event]"),
                        # error event for any exception raised during logic execution
                        error=(self.handle_nifti_convertion_error, "[$event]"),
                    ) as preprocessing:
                        # trigger the preprocessing on our dicom_file_set state key
                        vuetify3.VBtn(
                            "Convert DICOMs to NIFTI file",
                            color="primary",
                            click=preprocessing.trigger_preprocessing("dicom_file_set"),
                        )

    def save_nifti_file(self, raw_nifti_file):
        nifti_file = ClientFile(raw_nifti_file[0])
        print("got a NIFTI file")

        print(nifti_file.info)
        print(nifti_file.name)

        file_path = (Path("outputs") / nifti_file.name).resolve()
        file_path.parent.mkdir(parents=True, exist_ok=True)

        with file_path.open(mode="xb") as file:
            file.write(nifti_file.content)

    def handle_nifti_convertion_error(self, error):
        print(error)
        self.state.error_message = error
        self.state.is_error = True


def main(**kwargs):
    app = DicomToNiftiConvertor()
    app.server.start(**kwargs)


if __name__ == "__main__":
    main()
