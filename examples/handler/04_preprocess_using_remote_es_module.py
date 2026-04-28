from typing import Literal

from trame.app import TrameApp
from trame.ui.vuetify3 import SinglePageLayout

from trame.widgets import client, vuetify3


class ItkWasmPreprocessor(TrameApp):
    def __init__(self, server=None):
        super().__init__(server)

        self.read_dicom_tags_preprocessor_logic = client.register_external_script(
            name="read_dicom_tags",
            script_file_path="https://cdn.jsdelivr.net/npm/@itk-wasm/dicom@7.6.4/dist/bundle/index-worker-embedded.min.js",
            function_names=["readDicomTags"],
        )

        self._build_ui()

    def _build_ui(self):
        with SinglePageLayout(self.server) as ui:
            ui.title.set_text("Client Preprocessing Minimal Example")

            with (
                ui.content,
                vuetify3.VContainer(fluid=True),
                vuetify3.VRow(),
                vuetify3.VCol(cols=3),
                client.Handler(
                    variable="dicom_file",
                    function=self.read_dicom_tags_preprocessor_logic,
                    inputs=("{ tagsToRead: { tags: ['0008|103e'] } }",),
                    completed=(
                        self.preprocessing_pipeline_completed,
                        "[$event.type, $event.outputs.tags]",
                    ),
                ),
            ):
                vuetify3.VFileInput(
                    v_model="dicom_file.value",
                    label="DICOM file",
                    hint="Select a DICOM file to extract tags from",
                    persistent_hint=True,
                )

    def preprocessing_pipeline_completed(
        self, type: Literal["success", "failure"], output
    ) -> None:
        print("preprocessing_pipeline_completed")
        print(type)
        print(output)


def main(**kwargs):
    app = ItkWasmPreprocessor()
    app.server.start(**kwargs)


if __name__ == "__main__":
    main()
