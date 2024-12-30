from fasthtml.common import *
import random


COLORS = {
    'desierto': '#C29710',
    'hielo': '#FFFFFF',
    'jungla': '#436B24',
    'volcán': '#91191B',
}
URL_IMGS = "https://raw.githubusercontent.com/Santiago-R/extinction_adventure/refs/heads/main/imgs/_{name}.png"

def emoji_favicon(emoji):
    return Link(rel="icon", href=f"""data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>{emoji}</text></svg>""")

def img_prefetch(url): return Link(rel="prefetch", href=url)

def card_3d(info, id):
    # https://codepen.io/markmiro/pen/wbqMPa
    img_url = URL_IMGS.format(name=info["name"].replace(' ', '%20'))
    title = info["name"] + (('  🥚' + str(info["incubation"])) if 'incubation' in info.keys() else '')
    c_left = COLORS[info['ecosystem'][0]] if 'ecosystem' in info.keys() else '#000000'
    c_right = COLORS[info['ecosystem'][-1]] if 'ecosystem' in info.keys() else '#000000'
    return Div(
        Div(
            H4(title),
            P(info["description"]),
            Div(cls='glow'),
            # Style("#"+id+" { background-image: url("+img_url+"); }"),
            Style(f"""#{id} {{
                border: 15px solid transparent;
                border-image: linear-gradient(to right, {c_left}, {c_right}) 1;
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


class Deck:
    def __init__(self, deck_info, shuffle=True):
        self.deck = []
        # self.urls = []
        for i, info in enumerate(deck_info):
            self.deck.append(card_3d(info=info, id=f'card_{i}'))
            # self.urls.append(URL_IMGS.format(name=info["name"].replace(' ', '%20')))

        if shuffle: random.shuffle(self.deck)
        self.stack = []

    def shuffle(self):
        random.shuffle(self.deck)

    def pop(self, i=-1):
        self.stack.append(self.deck.pop(i))

    def stack_reorder(self, idxs):
        self.stack = [self.stack[i] for i in idxs]

    def stack_to_bottom(self):
        self.deck = self.stack + self.deck
        self.stack = []

    def stack_to_front(self):
        self.deck = self.deck + self.stack
        self.stack = []
    
    def __iter__(self): return iter(self.deck)
    def __getitem__(self, idx): return self.deck[idx]
    def __len__(self): return len(self.deck)

    