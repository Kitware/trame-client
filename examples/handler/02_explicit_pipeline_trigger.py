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
        self.state.feedback_message = ""
        self.state.is_error = False
        self.state.is_success = False

        # Mark your state as client_only!
        self.state.client_only("dicom_file_set")

        client.register_external_script(
            name="generate_nii_from_dcm",
            script_file_path=DICOM_UTILS_SCRIPT,
            function_names=["generateNIFTIFromDicomFileSet"],
        )

        self._build_ui()

    def _build_ui(self):
        with SinglePageLayout(self.server) as self.ui:
            self.ui.title.set_text("Explicit Pipeline Trigger")

            with (
                self.ui.content,
                vuetify3.VContainer(fluid=True),
                vuetify3.VRow(),
                vuetify3.VCol(cols=3),
            ):
                with vuetify3.VCard(flat=True):
                    with (
                        vuetify3.VSnackbar(
                            model_value=("is_error || is_success",),
                            color=("is_error ? 'error' : 'success'",),
                            location="top left",
                            close_on_content_click=True,
                            timeout=6000,
                            update_modelValue="is_error = $event; is_success = $event;",
                        ),
                        html.Div(style="align-items: center;"),
                    ):
                        vuetify3.VIcon("mdi-information", style="margin-right: 12px")
                        html.Span("{{ feedback_message }}")

                    vuetify3.VFileInput(
                        v_model="dicom_file_set",
                        multiple=True,
                        label="DICOM files",
                        hint="Input here a set of DICOM files that will be converted to a single .nii file",
                        persistent_hint=True,
                    )

                    with client.Handler(
                        function="generate_nii_from_dcm",
                        inputs=("{ output_file_name: 'my_converted_file.nii' }",),
                        # success event for the logic happy path
                        success=(self.save_nifti_file, "[$event]"),
                        # failure event for the logic error path (e.g. invalid data)
                        failure=(self.handle_nifti_convertion_error, "[$event]"),
                        # error event for any exception raised during logic execution
                        error=(self.handle_nifti_convertion_error, "[$event]"),
                    ) as client_handler:
                        # trigger the preprocessing on our dicom_file_set state key
                        vuetify3.VBtn(
                            "Convert DICOMs to NIFTI file",
                            color="primary",
                            click=client_handler.run("dicom_file_set"),
                        )

    def save_nifti_file(self, raw_nifti_file):
        nifti_file = ClientFile(raw_nifti_file[0])
        print("got a NIFTI file")

        print(nifti_file.info)
        print(nifti_file.name)

        self.state.feedback_message = "NIFTI file successfully generated"
        self.state.is_success = True
        self.state.is_error = False

        file_path = (Path("outputs") / nifti_file.name).resolve()
        file_path.parent.mkdir(parents=True, exist_ok=True)

        if file_path.exists():
            file_path.unlink()

        with file_path.open(mode="xb") as file:
            file.write(nifti_file.content)

    def handle_nifti_convertion_error(self, error):
        print(error)
        self.state.feedback_message = error
        self.state.is_error = True


def main(**kwargs):
    app = DicomToNiftiConvertor()
    app.server.start(**kwargs)


if __name__ == "__main__":
    main()
