from typing import Literal

from trame.app import get_server
from trame.ui.vuetify3 import SinglePageLayout

from trame.widgets import client, vuetify3

server = get_server()


def preprocessing_pipeline_completed(
    type: Literal["success", "failure"], output
) -> None:
    print("preprocessing_pipeline_completed")
    print(type)
    print(output)


client.PreProcessor.register_preprocessing_unit(
    name="read_dicom_tags",
    module_script="https://cdn.jsdelivr.net/npm/@itk-wasm/dicom@7.6.4/dist/bundle/index-worker-embedded.min.js",
    function_name="readDicomTags",
)


with SinglePageLayout(server) as ui:
    ui.title.set_text("Client Preprocessing Minimal Example")

    with (
        ui.content,
        vuetify3.VContainer(fluid=True, classes="pa-0 fill-height"),
        client.PreProcessor(
            variable="dicom_file",
            preprocessor="read_dicom_tags",
            inputs=("{ tagsToRead: { tags: ['0008|103e'] } }",),
            completed=(
                preprocessing_pipeline_completed,
                "[$event.type, $event.outputs.tags]",
            ),
        ) as preprocessing,
    ):
        vuetify3.VFileInput(
            v_model="dicom_file.value",
        )

server.start()
