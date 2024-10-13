"""from fasthtml.common import *

app,rt = fast_app()"""

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
"""
from fasthtml.common import *
css = Style(':root {--pico-font-size:90%,--pico-font-family: Pacifico, cursive;}')
app = FastHTML(hdrs=(picolink, css))

@app.route("/")
def get():
    return (Title("Hello World"), 
            Main(H1('Hello, World'), cls="container"))"""

from fasthtml.common import *

app = FastHTML()
messages = ["This is a message, which will get rendered as a paragraph"]

@app.get("/")
def home():
    return Main(H1('Messages'), 
        *[P(msg) for msg in messages], #i have no idea why but removing the * breaks it
        A("Link to Page 2 (to add messages)", href="/page2"))

@app.get("/page2")
def page2():
    return Main(P("Add a message with the form below:"),
                Form(Input(type="text", name="data"),
                     Button("Submit"),
                     action="/", method="post"))

@app.post("/")
def add_message(data:str):
    messages.append(data)
    return home()