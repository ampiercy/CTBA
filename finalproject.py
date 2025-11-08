import dash
from dash import Dash, dcc, html
import dash_bootstrap_components as dbc

app = Dash(
    __name__,
    use_pages=True,
    suppress_callback_exceptions=True,
    title="Andrew Piercy Makeup Final Dashboard",
)
server = app.server

app.layout = html.Div(
    className="page-wrapper",
    children=[
        # Navbar
        dbc.Navbar(
            dbc.Container([
                dbc.NavbarBrand("Andrew Piercy Makeup Final Dashboard", className="brand-text"),

                # Centered nav links
                dbc.Nav(
                    [
                        dbc.NavLink("Home", href="/", active="exact"),
                        dbc.NavLink("Interactive Beef Trading Map", href="/pageone", active="exact"),
                        dbc.NavLink("Beef Trade Time Series", href="/pagetwo", active="exact"),
                    ],
                    className="nav-links"
                ),
            ], fluid=True),
            className="custom-navbar",
            dark=True
        ),

        # Page content container
        html.Div(dash.page_container, className="page-content"),

        # Footer
        html.Footer(
            "Andrew Piercy | Data from USDA Economic Research Service",
            className="footer"
        )
    ]
)

if __name__ == "__main__":
    app.run(debug=True) 
