# >> uvicorn main_v0:app

print('------------- Starting server -------------')
from fasthtml.common import *
from fasthtml.svg import *
# from pydantic import BaseModel, ValidationError, Field, EmailStr
from secrets import token_urlsafe
from typing import List
from dino_info import info_list

colors = {
    'desierto': '#C29710',
    'hielo': '#FFFFFF',
    'jungla': '#436B24',
    'volcán': '#91191B'
}

def emoji_favicon(emoji):
    return Link(rel="icon", href=f"""data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>{emoji}</text></svg>""")

_css = StyleX('card3d.css')#, background_image=f'url({bg_img})', align='left')
_js = ScriptX('card3d.js')

img_urls = "https://raw.githubusercontent.com/Santiago-R/extinction_adventure/refs/heads/main/imgs/_{name}.png"

def card_3d(info, id):
    # https://codepen.io/markmiro/pen/wbqMPa
    img_url = img_urls.format(name=info["name"].replace(' ', '%20'))
    return Div(
        H4(info["name"] + '  🥚' + str(info["incubation"])),
        P(info["description"]),
        Div(cls='glow'),
        # Style("#"+id+" { background-image: url("+img_url+"); }"),
        Style(f"""#{id} {{
            border: 15px solid transparent;
            border-image: linear-gradient(to right, {colors[info['ecosystem'][0]]}, {colors[info['ecosystem'][-1]]}) 1;
            background: 
                url('{img_url}') top center no-repeat,
                #FFFFFF;
            background-size: 320px 320px;
            padding: 330px 15px 15px 15px;
        }}"""),
            # box-sizing: border-box;

        cls='card',
        id=id
    )


def make_cards():
    card_div_list = []
    for i, info in enumerate(info_list):
        card = card_3d(info=info, id=f'card_{i}')
        card_div_list.append(Div(card, cls="card-container col-12 col-md-6 col-lg-4"))
        # card_div_list.append(card)
    return card_div_list

###########################################################################
# boots_meta = Meta(name="viewport", content="width=device-width, initial-scale=1.0")
boots_link = Link(href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css", rel="stylesheet")
app = FastHTMLWithLiveReload(hdrs=[boots_link, emoji_favicon("🦖"), _css])

@app.get("/")
async def show_cards():
    card_div_list = make_cards()
    first_element = Div(H1("🦕", style="font-size: 250px; text-align: center;"), cls="col-12 col-md-6 col-lg-4")
    boots_grid = Div(Div(first_element, *card_div_list, cls="row"), cls="container")
    # header = H1("Dinosaurios!")
    return Title('Dinosaurios'), Main(boots_grid, _js)

serve()
