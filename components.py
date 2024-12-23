from fasthtml.common import *
from dino_info import info_list
import random


COLORS = {
    'desierto': '#C29710',
    'hielo': '#FFFFFF',
    'jungla': '#436B24',
    'volcán': '#91191B'
}
URL_IMGS = "https://raw.githubusercontent.com/Santiago-R/extinction_adventure/refs/heads/main/imgs/_{name}.png"

def emoji_favicon(emoji):
    return Link(rel="icon", href=f"""data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>{emoji}</text></svg>""")

def card_3d(info, id):
    # https://codepen.io/markmiro/pen/wbqMPa
    img_url = URL_IMGS.format(name=info["name"].replace(' ', '%20'))
    return Div(
        Div(
            H4(info["name"] + '  🥚' + str(info["incubation"])),
            P(info["description"]),
            Div(cls='glow'),
            # Style("#"+id+" { background-image: url("+img_url+"); }"),
            Style(f"""#{id} {{
                border: 15px solid transparent;
                border-image: linear-gradient(to right, {COLORS[info['ecosystem'][0]]}, {COLORS[info['ecosystem'][-1]]}) 1;
                background: url('{img_url}') top center no-repeat, #FFFFFF;
                background-size: 320px 320px;
                padding: 330px 15px 15px 15px;
            }}"""),
                # box-sizing: border-box;
            cls='card',
            id=id,
        ),
        cls="card-container col-12 col-md-6 col-lg-4"
    )

# def make_deck():
#     deck = []
#     for i, info in enumerate(info_list):
#         card = card_3d(info=info, id=f'card_{i}')
#         # deck.append(Div(card, cls="card-container col-12 col-md-6 col-lg-4"))
#         # card_div_list.append(card)
#     return deck

class Deck:
    "Replaces make_deck, adds shuffle functionality"
    def __init__(self, shuffle=True):
        self.deck = []
        for i, info in enumerate(info_list):
            self.deck.append(card_3d(info=info, id=f'card_{i}'))
        if shuffle: random.shuffle(self.deck)
        self.stack = []
    def shuffle(self):
        random.shuffle(self.deck)
    def pop(self, n=1):
        for _ in range(n): self.stack.append(self.deck.pop())
        return self.stack
    def reorder_stack(self, idxs):
        self.stack = [self.stack[i] for i in idxs]
    def push(self):
        self.deck = self.stack + self.deck
        self.stack = []
    
    def __iter__(self): return iter(self.deck)
    def __getitem__(self, idx): return self.deck[idx]
    def __len__(self): return len(self.deck)

    