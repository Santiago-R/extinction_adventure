# >> uvicorn main_decks:app

print('------------ Starting server ------------')
from fasthtml.common import *
from components import emoji_favicon, Deck, img_prefetch
from card_info import dino_info, event_info


_css = StyleX('card3d.css')
_js = ScriptX('card3d.js')

event_deck = Deck(event_info, shuffle=True)
event_deck.pop()
dino_deck = Deck(dino_info, shuffle=True)
dino_deck.pop()
# prefetch_links = [img_prefetch(url) for url in dino_deck.urls]

boots_link = Link(href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css", rel="stylesheet")
app = FastHTMLWithLiveReload(hdrs=[boots_link, emoji_favicon("🦖"), _css])


@app.get("/")
async def show_stack():
    global deck
    dino_cards = Div(Div(*dino_deck.stack, cls="row"), cls="container", id="dino_deck")
    dino_form = Form(Button("Siguiente Dinosaurio"), hx_post="/next_dino", target_id="dino_deck", hx_swap="innerHTML")
    event_cards = Div(Div(*event_deck.stack, cls="row"), cls="container", id="event_deck")
    event_form = Form(Button("Siguiente Evento"), hx_post="/next_event", target_id="event_deck", hx_swap="innerHTML")
    return Title('Dinosaurios'), Main(
            Div(Div(dino_cards, dino_form, cls="col-6"),
            Div(event_cards, event_form, cls="col-6"),
            cls='row'
        ), _js)


@app.post("/next_dino")
async def next_dino():
    global dino_deck
    dino_deck.stack_to_bottom()
    dino_deck.pop()
    return Div(*dino_deck.stack, cls="row")

@app.post("/next_event")
async def next_event():
    global event_deck
    event_deck.stack_to_bottom()
    event_deck.pop()
    return Div(*event_deck.stack, cls="row")

serve()
