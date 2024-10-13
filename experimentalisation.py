from fasthtml.common import *

app,rt = fast_app()

""" basic helo world
@rt('/')
def get(): return Div(P('Hello World!'), hx_get="/change")

serve()
"""

""" some html elements
@app.get("/")
def home():
    page = Html(Head(Title("Title")), Body(H1("This page is very nice"), Br(),P("Yes it is")))
    return page
"""
"""defining routes
@app.get("/")
def home():
    return H1('Hello, World')

@app.route("/", methods=['post', 'put'])
def post_or_put():
    return "got a POST or PUT request"
@rt("/")
def get():
    pass
"""