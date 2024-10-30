from fasthtml.common import *
import requests
from icecream import ic
import random
from asyncio import sleep
from fasthtml.common import *

hdrs=(Script(src="https://unpkg.com/htmx-ext-sse@2.2.1/sse.js"),)
app = FastHTML(hdrs=hdrs, exts="ws")
@app.get("/w/{loc}")
def home(loc: str):
    page =     Head(Title("Durham Weather")),
    page=           Body(
                        Div(Form(Input(type="text", name="data", placeholder = "Enter location"), Button("Submit"), action = "/", method = "post")),
                        #Div(hx_ext = "sse", sse_connect ="/number-stream", hx_swap = "innerHTML", sse_swap = "message")
                        Div(Div(hx_ext="sse",
                        sse_connect=f"/weather/{loc}",
                        hx_swap="innerHTML",
                        sse_swap="message"), id = "weather")
                        )
    
    return page
                        
@app.post("/")
def form(data:str):
    return home(data)
                        

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
    try:
        loc = (await(anext(getCoords(location))))
        
        return EventStream(((weather(loc))))
    except:return EventStream(sse_message(P("Invalid location")))

#everything south of this point is stolen directly from google
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
        await sleep(10)

@app.get("/number-stream")
async def get(): return EventStream(number_generator())

rt = app.route

def mk_inp(): return Input(id='msg')
nid = 'notifications'

@rt('/test')
async def get():
    cts = Div(
        Div(id=nid),
        Form(mk_inp(), id='form', ws_send=True),
        hx_ext='ws', ws_connect='/ws')
    return Titled('Websocket Test', cts)

async def on_connect(send): await send(Div('Hello, you have connected', id=nid))
async def on_disconnect( ): print('Disconnected!')

@app.ws('/ws', conn=on_connect, disconn=on_disconnect)
async def ws(msg:str, send):
    await send(Div('Hello ' + msg, id=nid))
    await sleep(2)
    return Div('Goodbye ' + msg, id=nid), mk_inp()

serve()#except the serve() function