# >> uvicorn main_v0:app

# WIP: Go through shuffled decks, to play the game!

print('------------- Starting server -------------')
from fasthtml.common import *
from components import emoji_favicon, Deck, img_prefetch

_css = StyleX('card3d.css')
_js = ScriptX('card3d.js')

deck = Deck(shuffle=True)
deck.pop()
# prefetch_links = [img_prefetch(url) for url in deck.urls]

boots_link = Link(href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css", rel="stylesheet")
app = FastHTMLWithLiveReload(hdrs=[boots_link, emoji_favicon("🦖"), _css])


@app.get("/")
async def show_stack():
    global deck
    cards = Div(Div(*deck.stack, cls="row"), cls="container", id="target")
    form = Form(Button("Next"), hx_post="/", target_id="target", hx_swap="innerHTML")
    return Title('Dinosaurios'), Main(cards, form, _js)

@app.post("/")
async def next_card():
    global deck
    deck.stack_to_bottom()
    deck.pop()
    return Div(*deck.stack, cls="row")

serve()
º