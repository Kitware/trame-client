"""
Trame example that uses an UMD module to file the holes of a STL file before visualization.
You need to build the JS project inside geometry-preprocessing folder in order for this to work.
You can download an example file from here: https://kitware.github.io/vtk-js/data/stl/spherewithholes.stl
"""

from pathlib import Path
import tempfile
from typing import Literal

from trame.app import TrameApp
from trame.ui.vuetify3 import SinglePageLayout

from trame.app.file_upload import ClientFile
from trame.widgets import client, vuetify3, vtk as vtk_widgets
from vtkmodules import all as vtk

VTK_UTILS_SCRIPT = (
    Path(__file__).with_name("geometry-preprocessing")
    / "dist"
    / "geometry-preprocessing.umd.js"
)


class PatientNameValidator(TrameApp):
    def __init__(self, server=None):
        super().__init__(server)

        self.state.decimation_factor = 5
        self.state.hole_size = 1000.0

        client.register_external_script(
            name="fill_stl_holes",
            script_file_path=VTK_UTILS_SCRIPT,
            function_names=["fill_stl_holes"],
            umd=True,
            umd_global_var_name="GeometryPreProcessing",
        )

        # If your preprocessing depends on some libs, you can register them using server.enable_module
        # self.server.enable_module(
        #     {"scripts": ["https://unpkg.com/@kitware/vtk-wasm/vtk-umd.js"]}
        # )

        self.setup_vtk()
        self._build_ui()

    def setup_vtk(self):
        renderer = vtk.vtkRenderer()
        render_window = vtk.vtkRenderWindow()
        render_window.AddRenderer(renderer)
        render_window.OffScreenRenderingOn()

        render_window_interactor = vtk.vtkRenderWindowInteractor()
        render_window_interactor.SetRenderWindow(render_window)
        render_window_interactor.GetInteractorStyle().SetCurrentStyleToTrackballCamera()

        self.renderer = renderer
        self.render_window = render_window

    def _build_ui(self):
        with SinglePageLayout(self.server) as self.ui:
            self.ui.title.set_text("Client Preprocessing UMD Modules")

            with self.ui.toolbar:
                with client.Handler(
                    function="fill_stl_holes",
                    inputs=("{ hole_size }",),
                    completed=(
                        self.preprocessing_pipeline_completed,
                        "[$event.type, $event.outputs]",
                    ),
                ) as fill_stl_holes:
                    vuetify3.VNumberInput(
                        v_model="hole_size",
                        label="Input here the hole size used to configure the VTK.js filter.",
                    )

                    vuetify3.VFileInput(
                        v_model=fill_stl_holes.input_data,
                        accept=".stl",
                        label="""
                            Input here an STL file with holes that needs to be filled.
                            It will be processed by VTK.js
                        """,
                    )

            with (
                self.ui.content,
                vuetify3.VContainer(fluid=True, classes="pa-0 fill-height"),
            ):
                view = vtk_widgets.VtkRemoteView(self.render_window)
                self.ctrl.view_update = view.update
                self.ctrl.view_reset_camera = view.reset_camera

    def preprocessing_pipeline_completed(
        self, event_type: Literal["success", "failure"], output
    ) -> None:
        if event_type == "failure":
            print("pipeline failed")
            return

        stl_file = ClientFile(output[0])

        with tempfile.NamedTemporaryFile(mode="wb") as f:
            print(type(stl_file.content))
            f.write(stl_file.content)
            f.flush()

            stl_reader = vtk.vtkSTLReader(file_name=f.name)
            mapper = vtk.vtkPolyDataMapper()

            stl_reader >> mapper

            actor = vtk.vtkActor()
            actor.SetMapper(mapper)
            self.renderer.AddActor(actor)
            self.renderer.ResetCamera()
            self.render_window.Render()

            self.ctrl.view_update()


def main(**kwargs):
    app = PatientNameValidator()
    app.server.start(**kwargs)


if __name__ == "__main__":
    main()
