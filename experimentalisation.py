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
import requests
"""
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
    """
"""
app = FastHTML()

count = 0

@app.get("/")
def home():
    return Title("Count Demo"), Main(
        H1("Count Demo"),
        P(f"Count is set to {count}", id="count"),
        Button("Increment", hx_post="/increment", hx_target="#count", hx_swap="innerHTML")
    )

@app.post("/increment")
def increment():
    print("incrementing")
    global count
    count += 1
    return f"Count is set to {count}"
"""

"""Img(src = f"https://openweathermap.org/img/wn/{response['weather'][0]['icon']}@2x.png", style = "width: 100px"),"""

import json
app = FastHTML()
@app.get("/")
async def home():
    response = requests.get("https://api.openweathermap.org/data/2.5/weather?lat=54.76&lon=-1.58&appid=9044863ea8fb7c4bb152d8b4e14469b0").json()
    url = f"https://openweathermap.org/img/wn/{response['weather'][0]['icon']}@2x.png"
    page = Html(Head(Title("Durham Weather")), 
                Body(P(f"{response['name']}", Br(),Div(
                        Div( style = f"display: flex; width: 100px; height: 100px; background-image: url('{url}'); float: left"),
                        Div( P(f"{response['weather'][0]['main']}", style = "margin:auto"), style = "display: flex; width:100px; height:100px; float: left; text-align: center"), style = f"height: 100px; width:210px"))))
    
    
    return page