# >> uvicorn main_v0:app

# WIP: Go through shuffled decks, to play the game!

print('------------- Starting server -------------')
from fasthtml.common import *
from components import emoji_favicon, Deck

_css = StyleX('card3d.css')
_js = ScriptX('card3d.js')

boots_link = Link(href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css", rel="stylesheet")
app = FastHTMLWithLiveReload(hdrs=[boots_link, emoji_favicon("🦖"), _css])

@app.get("/")
async def handle_deck():
    deck = Deck(shuffle=True)
    deck.pop()
    boots_grid = Div(Div(*deck.stack, cls="row"), cls="container")
    return Title('Dinosaurios'), Main(boots_grid, _js)

serve()
