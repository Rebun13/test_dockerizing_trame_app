import pickle
import pyvista as pv
import tempfile

from pyvista.trame.ui import plotter_ui
from trame.app import get_server
from trame.app.file_upload import ClientFile
from trame.decorators import TrameApp
from trame.ui.vuetify3 import SinglePageWithDrawerLayout
from trame.widgets import vuetify3


# ---------------------------------------------------------
# Engine class
# ---------------------------------------------------------

pv.OFF_SCREEN = True


@TrameApp()
class MyTrameApp:
    def __init__(self, server=None):
        self.server = get_server(server, client_type="vue3")
        self.pl = pv.Plotter()
        if self.server.hot_reload:
            self.server.controller.on_server_reload.add(self._build_ui)
        self.ui = self._build_ui()

        # Set state variable
        self.state.trame__title = "Trame Multi-user"
        # Set state defaults
        self.state.setdefault("mesh", None)
        self.state.setdefault("scalars", [])
        self.state.setdefault("scalars_options", [])
        self.state.setdefault(
            "styles", ["surface", "wireframe", "points", "points_gaussian"]
        )

    @property
    def state(self):
        return self.server.state

    @property
    def ctrl(self):
        return self.server.controller

    @state.change("scalar_selector", "style_selector", "show_edges")
    def changeOptions(self, **kwargs):
        print(f"Volume: {self.state.volume_switch}")
        if self.state.mesh:
            self.pl.clear_actors()
            self.pl.add_mesh(
                pickle.loads(self.state.mesh),
                style=self.state.style_selector,
                scalars=self.state.scalar_selector,
                show_scalar_bar=True,
                show_edges=self.state.show_edges,
            )

    @state.change("file_exchange")
    def handleFile(self, file_exchange, **kwargs):
        self.pl.clear_actors()
        self.state.scalar_selector = None
        self.state.style_selector = None
        self.state.scalars_options = []
        self.state.mesh = None
        if file_exchange and len(file_exchange) > 0:
            file = ClientFile(file_exchange[0])
            print(file.info)
            bytes = file.content
            with tempfile.NamedTemporaryFile(suffix=file.name) as path:
                with open(path.name, "wb") as f:
                    f.write(bytes)
                mesh = pv.read(path.name)
            self.state.mesh = pickle.dumps(mesh)
            self.state.scalars = mesh.array_names
            self.state.scalars_options = [
                {"title": option, "value": option}
                for index, option in enumerate(self.state.scalars)
            ]
            self.pl.add_mesh(mesh, show_scalar_bar=True)
        self.pl.reset_camera()

    def _build_ui(self, *args, **kwargs):
        with SinglePageWithDrawerLayout(self.server) as layout:
            with layout.toolbar:
                vuetify3.VSpacer()
                vuetify3.VFileInput(
                    show_size=True,
                    closable_chips=True,
                    truncate_length=25,
                    v_model=("file_exchange", None),
                    dense=True,
                    hide_details=True,
                    style="max-width: 300px;",
                    multiple=False,
                )
                vuetify3.VProgressLinear(
                    indeterminate=True,
                    absolute=True,
                    bottom=True,
                    active=("trame__busy",),
                )
            with layout.drawer:
                with vuetify3.VRadioGroup(
                    v_model=("style_selector", None), label="Style"
                ):
                    for option in self.state.styles:
                        vuetify3.VRadio(label=option, value=option)
                vuetify3.VSelect(
                    v_model=("scalar_selector", None),
                    label="Scalar",
                    items=("scalars_options",),
                )
                vuetify3.VSwitch(
                    v_model=("show_edges", False),
                    label="Show edges",
                )
            with layout.content:
                with vuetify3.VContainer(
                    fluid=True,
                    classes="pa-0 fill-height",
                    style="position: relative;",
                ):
                    view = plotter_ui(self.pl)
                    self.ctrl.view_update = view.update
            # Footer
            # layout.footer.hide()

            return layout
