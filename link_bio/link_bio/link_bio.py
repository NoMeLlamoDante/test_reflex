import reflex as rx
from link_bio.componentes.navbar import navbar
from link_bio.views.header.header import header
from link_bio.views.links import links
from link_bio.componentes.footer import footer
import link_bio.styles.styles as styles
class State(rx.State):
    pass

def index() -> rx.Component:
    return rx.flex(
        rx.box(
            navbar(),
            rx.center(
                rx.vstack(
                    header(),
                    rx.divider(),
                    links(),
                    max_width="80%",
                    justify="center",
                    align="center", 
                ),
                padding_y=styles.Size.NORMAL_LARGE.value,
            ),
            footer(),
            width="100%",
            justify="center",
            align="center", 
        ),
    )

app = rx.App(
    style = styles.BASE_STYLE,
)
app.add_page(index)
app._compile()