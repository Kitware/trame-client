from typing import Literal

from trame.app import TrameApp
from trame.ui.vuetify3 import SinglePageLayout

from trame.widgets import client, vuetify3


class ItkWasmPreprocessor(TrameApp):
    def __init__(self, server=None):
        super().__init__(server)

        client.PreProcessor.register_preprocessing_unit(
            name="read_dicom_tags",
            module_script="https://cdn.jsdelivr.net/npm/@itk-wasm/dicom@7.6.4/dist/bundle/index-worker-embedded.min.js",
            function_name="readDicomTags",
        )

        self._build_ui()

    def _build_ui(self):
        with SinglePageLayout(self.server) as ui:
            ui.title.set_text("Client Preprocessing Minimal Example")

            with (
                ui.content,
                vuetify3.VContainer(fluid=True, classes="pa-0 fill-height"),
                client.PreProcessor(
                    variable="dicom_file",
                    preprocessor="read_dicom_tags",
                    inputs=("{ tagsToRead: { tags: ['0008|103e'] } }",),
                    completed=(
                        self.preprocessing_pipeline_completed,
                        "[$event.type, $event.outputs.tags]",
                    ),
                ),
            ):
                vuetify3.VFileInput(
                    v_model="dicom_file.value",
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
