# >> uvicorn main_v0:app

print('------------- Starting server -------------')
from fasthtml.common import *
from fasthtml.svg import *
# from pydantic import BaseModel, ValidationError, Field, EmailStr
from secrets import token_urlsafe
from typing import List
from dino_info import info_list


def emoji_favicon(emoji):
    return Link(rel="icon", href=f"""data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>{emoji}</text></svg>""")

_css = StyleX('card3d.css')#, background_image=f'url({bg_img})', align='left')
_js = ScriptX('card3d.js')

# https://codepen.io/markmiro/pen/wbqMPa


def card_3d(text, bg_img, amt=1):
    return Div(
        text,
        Div(cls='glow'),
        Style(".card {background: url("+bg_img+");}"),
        cls='card',
    )

folder_url = "https://github.com/Santiago-R/extinction_adventure/imgs/"

def make_cards():
    card_div_list = []
    for info in info_list: 
        # card = card_3d(text=info["name"], bg_img=f'imgs/_{info["name"]}.png')
        card = card_3d(text=info["name"], bg_img=f'{folder_url}_{info["name"]}.png')
        card_div_list.append(Div(card, cls="card-container col-12 col-md-6 col-lg-4"))
        # card_div_list.append(card)
    return card_div_list

###########################################################################
# boots_meta = Meta(name="viewport", content="width=device-width, initial-scale=1.0")
boots_link = Link(href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css", rel="stylesheet")
app = FastHTML(live=True, hdrs=[boots_link, emoji_favicon("🦖"), _css])

@app.get("/")
async def show_cards():
    card_div_list = make_cards()
    first_element = Div(H1("🦕", style="font-size: 250px; text-align: center;"), cls="col-12 col-md-6 col-lg-4")
    boots_grid = Div(Div(first_element, *card_div_list, cls="row"), cls="container")
    # header = H1("Dinosaurios!")
    return Title('Dinosaurios'), Main(boots_grid, _js)

serve()
