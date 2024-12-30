# >> uvicorn main_display:app

print('------------ Starting server ------------')
from fasthtml.common import *
from components import emoji_favicon, Deck
from card_info import event_info, dino_info

_css = StyleX('card3d.css')
_js = ScriptX('card3d.js')

boots_link = Link(href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css", rel="stylesheet")
app = FastHTMLWithLiveReload(hdrs=[boots_link, emoji_favicon("🦖"), _css])

@app.get("/")
async def show_cards():
    deck = Deck(dino_info, shuffle=False)
    first_element = Div(H1("🦕", style="font-size: 250px; text-align: center;"), cls="col-12 col-md-6 col-lg-4")
    boots_grid = Div(Div(first_element, *deck, cls="row"), cls="container")
    # header = H1("Dinosaurios!")
    return Title('Dinosaurios'), Main(boots_grid, _js)

serve()
