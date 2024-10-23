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

import random
from asyncio import sleep
from fasthtml.common import *

hdrs=(Script(src="https://unpkg.com/htmx-ext-sse@2.2.1/sse.js"),)
app = FastHTML(hdrs=hdrs)
@app.get("/")
def home():
    response = requests.get("https://api.openweathermap.org/data/2.5/weather?lat=54.76&lon=-1.58&appid=9044863ea8fb7c4bb152d8b4e14469b0").json()
    url = f"https://openweathermap.org/img/wn/{response['weather'][0]['icon']}@2x.png"
    #print(response)
    response2 = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q=Durham,GB&limit=1&appid=9044863ea8fb7c4bb152d8b4e14469b0").json()
    #print(response2)
    page = Head(Title("Durham Weather")), 
    page =           Body(Div(P(f"{response['name']}", Br(),Div(
                        Div( style = f"display: flex; width: 100px; height: 100px; background-image: url('{url}'); float: left"),
                        Div( P(f"{response['weather'][0]['main']}", style = "margin:auto"), style = "display: flex; width:100px; height:100px; float: left; text-align: center"), style = f"height: 100px; width:210px")),
                        H2("Temperature:"),
                        Div( Table(Tr(Th("Temperature"), Th("Feels Like"), Th("Minimum"), Th("Maximum")),
                                   Tr(Td(round((float(response["main"]["temp"]))-273.15,2), "°C"), Td(round((float(response["main"]["feels_like"]))-273.15,2), "°C"), Td(round((float(response["main"]["temp_min"]))-273.15,2), "°C"), Td(round((float(response["main"]["temp_max"]))-273.15,2), "°C")    ) ) , cls="table" )
                        ),
                        
                        #Div(hx_ext = "sse", sse_connect ="/number-stream", hx_swap = "innerHTML", sse_swap = "message")
                        Div(Div(hx_ext="sse",
                        sse_connect="/weather/Nottingham",
                        hx_swap="innerHTML",
                        sse_swap="message"))
                        )
    
    page2 = Body(Div(Div(hx_ext="sse",
                        sse_connect="/number-stream",
                        hx_swap="beforeend show:bottom",
                        sse_swap="message")))
    return page
                        

shutdown_event = signal_shutdown()

async def getCoords(loc):
    while not shutdown_event.is_set():
        response = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={loc},GB&limit=1&appid=9044863ea8fb7c4bb152d8b4e14469b0").json()
        coords = [response[0]["lat"], response[0]["lon"]]

        yield (await (location(coords)))
        await sleep(90) # every 90 seconds


async def location(coords):

        response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={coords[0]}&lon={coords[1]}&appid=9044863ea8fb7c4bb152d8b4e14469b0").json()
        return response
      

async def weather(response):
    while not shutdown_event.is_set():
        print(response)

        url = f"https://openweathermap.org/img/wn/{response['weather'][0]['icon']}@2x.png"

        data = Div(P(f"{response['name']}", Br(),Div(
                            Div( style = f"display: flex; width: 100px; height: 100px; background-image: url('{url}'); float: left"),
                            Div( P(f"{response['weather'][0]['main']}", style = "margin:auto"), style = "display: flex; width:100px; height:100px; float: left; text-align: center"), style = f"height: 100px; width:210px")),
                            H2("Temperature:"),
                            Div( Table(Tr(Th("Temperature"), Th("Feels Like"), Th("Minimum"), Th("Maximum")),
                                    Tr(Td(round((float(response["main"]["temp"]))-273.15,2), "°C"), Td(round((float(response["main"]["feels_like"]))-273.15,2), "°C"), Td(round((float(response["main"]["temp_min"]))-273.15,2), "°C"), Td(round((float(response["main"]["temp_max"]))-273.15,2), "°C")    ) ) , cls="table" ))
        yield sse_message(data)
        await sleep(90)

@app.get("/weather/{location}")
async def get(location : str):
    print("hi")
    loc = (await(anext(getCoords(location))))
    
    return EventStream((await anext(weather(loc))))
"""
@app.get("/weather/Nottingham")
async def get():
    location = "Nottingham"
    print("hi")
    loc = await getCoords(location)
    
    return EventStream(weather(loc))
    """


@app.get("/dingus")
def index():
    #print("hi")
    return Titled("SSE Random Number Generator",
        P("Generate pairs of random numbers, as the list grows scroll downwards."),
        Div(hx_ext="sse",
            sse_connect="/number-stream",
            hx_swap="beforeend show:bottom",
            sse_swap="message"))

#shutdown_event = signal_shutdown()

async def number_generator():
    while not shutdown_event.is_set():
        data = Article(random.randint(1, 100))
        yield sse_message(data)
        await sleep(1)

@app.get("/number-stream")
async def get(): return EventStream(number_generator())

serve()