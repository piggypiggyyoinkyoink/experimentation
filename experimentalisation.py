from fasthtml.common import *

app,rt = fast_app()

"""
@rt('/')
def get(): return Div(P('Hello World!'), hx_get="/change")

serve()
"""
@app.get("/")
def home():
    page = Html(Head(Title("Title")), Body(H1("This page is very nice"), Br(),P("Yes it is")))
    return page