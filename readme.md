## ¡¡Salva a los dinosaurios de la extinción!!

> Juego de mesa y de cartas colaborativo

#### Tablero:
> cuatro cuadrantes, cada uno con un ecosistema - Desierto, Jungla, Volcán, Hielo.

![board](board.jpg)

#### Cómo se juega:
Se juega con una baraja de cartas de dinosaurios y una baraja de cartas de eventos.  
  
Es un juego colaborativo, pero no podemos desvelar nuestras cartas al resto de jugadores.  
  
La partida termina cuando los eventos catastróficos extinguen a todas las especies de dinosaurio. El objetivo es salvar a los dinosaurios de la extinción el mayor tiempo posible.  
  
Los jugadores empiezan sin cartas. En su turno, roban una carta y pueden jugar las cartas de dinosaurio que deseen. Al jugar una carta de dinosaurio, se coloca la carta de dinosaurio en la casilla de incubación indicada, como cuenta atrás hasta la eclosión del huevo, y se coloca el huevo de dinosaurio en su ecosistema correspondiente. Si el dinosaurio tiene varios ecosistemas válidos, el jugador elige en cuál de ellos colocar el huevo. Al extinguirse uno o más dinosaurios, y/o perderse uno o más huevos, se colocan las cartas de dinosaurio correspondientes en el orden que los jugadores elijan detrás del mazo de dinosaurios.  

#### Cada ronda:
- Avanzan los contadores de incubación.
- Nacen los dinosaurios que han terminado su incubación.
- Se juega una carta de evento (Los primeros 5 turnos están exentos). Si no quedan eventos, ganamos la partida.
- Si todos los dinosaurios se han extinguido y todos los huevos se han perdido, termina la partida.
- Cada jugador juega su turno

#### Cada turno:
- Se ejecutan acciones disponibles, como las migraciones, en cualquier orden elegido.
- Si hubiera dinosaurios en el desierto, se extingue uno.
- Si hubiera dinosaurios en el hielo, se extingue uno.
- Si hubiera dinosaurios en la jungla, se añade el huevo correspondiente a la siguiente carta de dinosaurio de la baraja.

#### Cartas de evento:
- (x3) Migración masiva: Los jugadores pueden mover cualquier dinosaurio a cualquier ecosistema.
- (x2) Meteorito: Se extinguen todos los dinosaurios excepto los voladores y los acuáticos.
- (x3) Edad de hielo: Se extinguen todos los dinosaurios que no tienen el hielo como ecosistema. Se pierden los huevos con más de dos rondas de incubación pendiente.
- (x3) Sequía: Se extinguen todos los dinosaurios que no tienen el desierto como ecosistema. Se pierden los huevos a punto de eclosionar.
- (x5) Explosión cámbrica: Todos los jugadores roban una carta de dinosaurio.
- (x5) Incendio: Se extinguen todos los dinosaurios de la jungla excepto los acuáticos. Se pierden todos los huevos de la jungla excepto los acuáticos.
- (x5) Erupción volcánica: Se extinguen todos los dinosaurios del volcán excepto los acuáticos. Se pierden todos los huevos del volcán.
- (x3) Sobrepoblación: Se extinguen todos los dinosaurios del ecosistema con más dinosaurios.
- (x3) Se extinguen tres dinosaurios en la jungla.
- (x3) Plaga: Se extinguen todos los dinosaurios acuáticos y voladores. Se extingue al menos un dinosaurio de cada ecosistema.
- (x5) Terremoto: Todos los huevos se pierden. Todos los dinosaurios deben migrar a un ecosistema adyacente.
- (x2) Epigenética: Sin alterar su orden, desvela las tres siguientes cartas de evento. Los jugadores pueden desvelar sus cartas y discutir estrategias.
- (x5) Superviviente: La partida no puede terminar esta ronda. Juega la siguiente carta de evento de la baraja, pero continúa jugando aunque todos los dinosaurios se extingan y todos los huevos se pierdan.

#### Cartas de dinosaurio:

<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet">

<style>* {
    box-sizing: border-box;
}

html,
body {
    width: 100%;
    height: 100%;
    background-color: rgb(50, 57, 37);
}

body {
    font-family: system-ui, sans-serif;
    perspective: 1500px;
}

.card-container {
    perspective: 1200px;
}

.card {
    font-weight: bold;
    padding: 1em;
    text-align: left;
    text-shadow: 0 0 4px #000;
    color: #ddd;

    width: 350px;
    height: 350px;
    -webkit-text-stroke: 1px black;
    margin: 1em;
    font-size: 1.25em;
    box-shadow: 0 1px 5px #00000099;
    border-radius: 10px;
    background-size: cover;

    position: relative;

    transition-duration: 300ms;
    transition-property: transform, box-shadow;
    transition-timing-function: ease-out;
    transform: rotate3d(0);
}

.card:hover {
    transition-duration: 150ms;
    box-shadow: 0 5px 20px 5px #00000044;
}

.card .glow {
    position: absolute;
    width: 100%;
    height: 100%;
    left: 0;
    top: 0;
    background-image: radial-gradient(circle at 50% -20%, #ffffff22, #0000000f);
}</style>

<div class="container">
         <div class="row">
           <div class="col-12 col-md-6 col-lg-4">
             <h1 style="font-size: 250px; text-align: center;">🦕</h1>
           </div>
           <div class="card-container col-12 col-md-6 col-lg-4">
             <div id="card_0" class="card me__1" style="">
Plesiosaurio               <div class="glow" style="background-image: radial-gradient(circle at 313.159px -22.736px, rgba(255, 255, 255, 0.267), rgba(0, 0, 0, 0.06));"></div>
               <style ready="">#card_0 { background-image: url(https://raw.githubusercontent.com/Santiago-R/extinction_adventure/refs/heads/main/imgs/_Plesiosaurio.png); }</style>
             </div>
           </div>
           <div class="card-container col-12 col-md-6 col-lg-4">
             <div id="card_1" class="card me__2" style="">
Plesiosaurio del oasis               <div class="glow" style="background-image: radial-gradient(circle at 391.341px -141.726px, rgba(255, 255, 255, 0.267), rgba(0, 0, 0, 0.06));"></div>
               <style ready="">#card_1 { background-image: url(https://raw.githubusercontent.com/Santiago-R/extinction_adventure/refs/heads/main/imgs/_Plesiosaurio%20del%20oasis.png); }</style>
             </div>
           </div>
           <div class="card-container col-12 col-md-6 col-lg-4">
             <div id="card_2" class="card me__3" style="">
Maiasaura               <div class="glow" style="background-image: radial-gradient(circle at 120.881px -86.9539px, rgba(255, 255, 255, 0.267), rgba(0, 0, 0, 0.06));"></div>
               <style ready="">#card_2 { background-image: url(https://raw.githubusercontent.com/Santiago-R/extinction_adventure/refs/heads/main/imgs/_Maiasaura.png); }</style>
             </div>
           </div>
           <div class="card-container col-12 col-md-6 col-lg-4">
             <div id="card_3" class="card me__4" style="">
Anquilosaurio               <div class="glow" style="background-image: radial-gradient(circle at -139.088px 27.0461px, rgba(255, 255, 255, 0.267), rgba(0, 0, 0, 0.06));"></div>
               <style ready="">#card_3 { background-image: url(https://raw.githubusercontent.com/Santiago-R/extinction_adventure/refs/heads/main/imgs/_Anquilosaurio.png); }</style>
             </div>
           </div>
           <div class="card-container col-12 col-md-6 col-lg-4">
             <div id="card_4" class="card me__5" style="">
Minmi               <div class="glow" style="background-image: radial-gradient(circle at -97.0574px 448.685px, rgba(255, 255, 255, 0.267), rgba(0, 0, 0, 0.06));"></div>
               <style ready="">#card_4 { background-image: url(https://raw.githubusercontent.com/Santiago-R/extinction_adventure/refs/heads/main/imgs/_Minmi.png); }</style>
             </div>
           </div>
           <div class="card-container col-12 col-md-6 col-lg-4">
             <div id="card_5" class="card me__6" style="">
Diplodocus verde               <div class="glow" style="background-image: radial-gradient(circle at 244.881px -191.284px, rgba(255, 255, 255, 0.267), rgba(0, 0, 0, 0.06));"></div>
               <style ready="">#card_5 { background-image: url(https://raw.githubusercontent.com/Santiago-R/extinction_adventure/refs/heads/main/imgs/_Diplodocus%20verde.png); }</style>
             </div>
           </div>
           <div class="card-container col-12 col-md-6 col-lg-4">
             <div id="card_6" class="card me__7" style="">
Diplodocus rocoso               <div class="glow" style="background-image: radial-gradient(circle at 268.912px 490.257px, rgba(255, 255, 255, 0.267), rgba(0, 0, 0, 0.06));"></div>
               <style ready="">#card_6 { background-image: url(https://raw.githubusercontent.com/Santiago-R/extinction_adventure/refs/heads/main/imgs/_Diplodocus%20rocoso.png); }</style>
             </div>
           </div>
           <div class="card-container col-12 col-md-6 col-lg-4">
             <div id="card_7" class="card me__8" style="">
Diplodocus blanco               <div class="glow" style="background-image: radial-gradient(circle at 504.943px 176.716px, rgba(255, 255, 255, 0.267), rgba(0, 0, 0, 0.06));"></div>
               <style ready="">#card_7 { background-image: url(https://raw.githubusercontent.com/Santiago-R/extinction_adventure/refs/heads/main/imgs/_Diplodocus%20blanco.png); }</style>
             </div>
           </div>
           <div class="card-container col-12 col-md-6 col-lg-4">
             <div id="card_8" class="card me__9" style="">
Pterosaurio               <div class="glow" style="background-image: radial-gradient(circle at 228.881px 308.386px, rgba(255, 255, 255, 0.267), rgba(0, 0, 0, 0.06));"></div>
               <style ready="">#card_8 { background-image: url(https://raw.githubusercontent.com/Santiago-R/extinction_adventure/refs/heads/main/imgs/_Pterosaurio.png); }</style>
             </div>
           </div>
           <div class="card-container col-12 col-md-6 col-lg-4">
             <div id="card_9" class="card me__10" style="">
Pterodáctilo               <div class="glow" style="background-image: radial-gradient(circle at 334.912px 352.747px, rgba(255, 255, 255, 0.267), rgba(0, 0, 0, 0.06));"></div>
               <style ready="">#card_9 { background-image: url(https://raw.githubusercontent.com/Santiago-R/extinction_adventure/refs/heads/main/imgs/_Pterodáctilo.png); }</style>
             </div>
           </div>
           <div class="card-container col-12 col-md-6 col-lg-4">
             <div id="card_10" class="card me__11" style="">
Utahraptor               <div class="glow" style="background-image: radial-gradient(circle at 302.943px -239.253px, rgba(255, 255, 255, 0.267), rgba(0, 0, 0, 0.06));"></div>
               <style ready="">#card_10 { background-image: url(https://raw.githubusercontent.com/Santiago-R/extinction_adventure/refs/heads/main/imgs/_Utahraptor.png); }</style>
             </div>
           </div>
           <div class="card-container col-12 col-md-6 col-lg-4">
             <div id="card_11" class="card me__12" style="">
Estiracosaurio               <div class="glow" style="background-image: radial-gradient(circle at 58.8811px 364.778px, rgba(255, 255, 255, 0.267), rgba(0, 0, 0, 0.06));"></div>
               <style ready="">#card_11 { background-image: url(https://raw.githubusercontent.com/Santiago-R/extinction_adventure/refs/heads/main/imgs/_Estiracosaurio.png); }</style>
             </div>
           </div>
           <div class="card-container col-12 col-md-6 col-lg-4">
             <div id="card_12" class="card me__13" style="">
Herrerasaurio               <div class="glow" style="background-image: radial-gradient(circle at 272.912px 394.384px, rgba(255, 255, 255, 0.267), rgba(0, 0, 0, 0.06));"></div>
               <style ready="">#card_12 { background-image: url(https://raw.githubusercontent.com/Santiago-R/extinction_adventure/refs/heads/main/imgs/_Herrerasaurio.png); }</style>
             </div>
           </div>
           <div class="card-container col-12 col-md-6 col-lg-4">
             <div id="card_13" class="card me__14" style="">
Edmontosaurio               <div class="glow" style="background-image: radial-gradient(circle at -207.057px 480.778px, rgba(255, 255, 255, 0.267), rgba(0, 0, 0, 0.06));"></div>
               <style ready="">#card_13 { background-image: url(https://raw.githubusercontent.com/Santiago-R/extinction_adventure/refs/heads/main/imgs/_Edmontosaurio.png); }</style>
             </div>
           </div>
           <div class="card-container col-12 col-md-6 col-lg-4">
             <div id="card_14" class="card me__15" style="">
Tarquia               <div class="glow" style="background-image: radial-gradient(circle at 446.881px 400.907px, rgba(255, 255, 255, 0.267), rgba(0, 0, 0, 0.06));"></div>
               <style ready="">#card_14 { background-image: url(https://raw.githubusercontent.com/Santiago-R/extinction_adventure/refs/heads/main/imgs/_Tarquia.png); }</style>
             </div>
           </div>
           <div class="card-container col-12 col-md-6 col-lg-4">
             <div id="card_15" class="card me__16" style="">
Microraptor               <div class="glow" style="background-image: radial-gradient(circle at 272.912px 354.251px, rgba(255, 255, 255, 0.267), rgba(0, 0, 0, 0.06));"></div>
               <style ready="">#card_15 { background-image: url(https://raw.githubusercontent.com/Santiago-R/extinction_adventure/refs/heads/main/imgs/_Microraptor.png); }</style>
             </div>
           </div>
           <div class="card-container col-12 col-md-6 col-lg-4">
             <div id="card_16" class="card me__17" style="">
Camarasauro               <div class="glow" style="background-image: radial-gradient(circle at -121.057px -173.192px, rgba(255, 255, 255, 0.267), rgba(0, 0, 0, 0.06));"></div>
               <style ready="">#card_16 { background-image: url(https://raw.githubusercontent.com/Santiago-R/extinction_adventure/refs/heads/main/imgs/_Camarasauro.png); }</style>
             </div>
           </div>
           <div class="card-container col-12 col-md-6 col-lg-4">
             <div id="card_17" class="card me__18">
Compsognathus               <div class="glow"></div>
               <style ready="">#card_17 { background-image: url(https://raw.githubusercontent.com/Santiago-R/extinction_adventure/refs/heads/main/imgs/_Compsognathus.png); }</style>
             </div>
           </div>
           <div class="card-container col-12 col-md-6 col-lg-4">
             <div id="card_18" class="card me__19" style="">
Paquicefalosaurio               <div class="glow" style="background-image: radial-gradient(circle at 274.912px 431.757px, rgba(255, 255, 255, 0.267), rgba(0, 0, 0, 0.06));"></div>
               <style ready="">#card_18 { background-image: url(https://raw.githubusercontent.com/Santiago-R/extinction_adventure/refs/heads/main/imgs/_Paquicefalosaurio.png); }</style>
             </div>
           </div>
           <div class="card-container col-12 col-md-6 col-lg-4">
             <div id="card_19" class="card me__20" style="">
Estegosaurio naranja               <div class="glow" style="background-image: radial-gradient(circle at 184.943px -193.161px, rgba(255, 255, 255, 0.267), rgba(0, 0, 0, 0.06));"></div>
               <style ready="">#card_19 { background-image: url(https://raw.githubusercontent.com/Santiago-R/extinction_adventure/refs/heads/main/imgs/_Estegosaurio%20naranja.png); }</style>
             </div>
           </div>
           <div class="card-container col-12 col-md-6 col-lg-4">
             <div id="card_20" class="card me__21">
Estegosaurio violeta               <div class="glow"></div>
               <style ready="">#card_20 { background-image: url(https://raw.githubusercontent.com/Santiago-R/extinction_adventure/refs/heads/main/imgs/_Estegosaurio%20violeta.png); }</style>
             </div>
           </div>
           <div class="card-container col-12 col-md-6 col-lg-4">
             <div id="card_21" class="card me__22" style="">
Iguanodón               <div class="glow" style="background-image: radial-gradient(circle at 276.912px 443.394px, rgba(255, 255, 255, 0.267), rgba(0, 0, 0, 0.06));"></div>
               <style ready="">#card_21 { background-image: url(https://raw.githubusercontent.com/Santiago-R/extinction_adventure/refs/heads/main/imgs/_Iguanodón.png); }</style>
             </div>
           </div>
           <div class="card-container col-12 col-md-6 col-lg-4">
             <div id="card_22" class="card me__23" style="">
Parasaurolophus               <div class="glow" style="background-image: radial-gradient(circle at 366.943px 327.231px, rgba(255, 255, 255, 0.267), rgba(0, 0, 0, 0.06));"></div>
               <style ready="">#card_22 { background-image: url(https://raw.githubusercontent.com/Santiago-R/extinction_adventure/refs/heads/main/imgs/_Parasaurolophus.png); }</style>
             </div>
           </div>
           <div class="card-container col-12 col-md-6 col-lg-4">
             <div id="card_23" class="card me__24">
Velociraptor               <div class="glow"></div>
               <style ready="">#card_23 { background-image: url(https://raw.githubusercontent.com/Santiago-R/extinction_adventure/refs/heads/main/imgs/_Velociraptor.png); }</style>
             </div>
           </div>
           <div class="card-container col-12 col-md-6 col-lg-4">
             <div id="card_24" class="card me__25" style="">
Velociraptor mini               <div class="glow" style="background-image: radial-gradient(circle at 296.912px -120.837px, rgba(255, 255, 255, 0.267), rgba(0, 0, 0, 0.06));"></div>
               <style ready="">#card_24 { background-image: url(https://raw.githubusercontent.com/Santiago-R/extinction_adventure/refs/heads/main/imgs/_Velociraptor%20mini.png); }</style>
             </div>
           </div>
           <div class="card-container col-12 col-md-6 col-lg-4">
             <div id="card_25" class="card me__26">
Saurópodo               <div class="glow"></div>
               <style ready="">#card_25 { background-image: url(https://raw.githubusercontent.com/Santiago-R/extinction_adventure/refs/heads/main/imgs/_Saurópodo.png); }</style>
             </div>
           </div>
           <div class="card-container col-12 col-md-6 col-lg-4">
             <div id="card_26" class="card me__27" style="">
Huayangosaurio               <div class="glow" style="background-image: radial-gradient(circle at 342.881px 204.112px, rgba(255, 255, 255, 0.267), rgba(0, 0, 0, 0.06));"></div>
               <style ready="">#card_26 { background-image: url(https://raw.githubusercontent.com/Santiago-R/extinction_adventure/refs/heads/main/imgs/_Huayangosaurio.png); }</style>
             </div>
           </div>
           <div class="card-container col-12 col-md-6 col-lg-4">
             <div id="card_27" class="card me__28" style="">
Paquirrinosaurio               <div class="glow" style="background-image: radial-gradient(circle at 306.912px 228.833px, rgba(255, 255, 255, 0.267), rgba(0, 0, 0, 0.06));"></div>
               <style ready="">#card_27 { background-image: url(https://raw.githubusercontent.com/Santiago-R/extinction_adventure/refs/heads/main/imgs/_Paquirrinosaurio.png); }</style>
             </div>
           </div>
           <div class="card-container col-12 col-md-6 col-lg-4">
             <div id="card_28" class="card me__29" style="">
Espinosaurio               <div class="glow" style="background-image: radial-gradient(circle at -97.4719px 495.393px, rgba(255, 255, 255, 0.267), rgba(0, 0, 0, 0.06));"></div>
               <style ready="">#card_28 { background-image: url(https://raw.githubusercontent.com/Santiago-R/extinction_adventure/refs/heads/main/imgs/_Espinosaurio.png); }</style>
             </div>
           </div>
           <div class="card-container col-12 col-md-6 col-lg-4">
             <div id="card_29" class="card me__30" style="">
Protoceratops caramelo               <div class="glow" style="background-image: radial-gradient(circle at 552.881px 336.405px, rgba(255, 255, 255, 0.267), rgba(0, 0, 0, 0.06));"></div>
               <style ready="">#card_29 { background-image: url(https://raw.githubusercontent.com/Santiago-R/extinction_adventure/refs/heads/main/imgs/_Protoceratops%20caramelo.png); }</style>
             </div>
           </div>
           <div class="card-container col-12 col-md-6 col-lg-4">
             <div id="card_30" class="card me__31" style="">
Protoceratops rosita               <div class="glow" style="background-image: radial-gradient(circle at 357.525px 151.747px, rgba(255, 255, 255, 0.267), rgba(0, 0, 0, 0.06));"></div>
               <style ready="">#card_30 { background-image: url(https://raw.githubusercontent.com/Santiago-R/extinction_adventure/refs/heads/main/imgs/_Protoceratops%20rosita.png); }</style>
             </div>
           </div>
           <div class="card-container col-12 col-md-6 col-lg-4">
             <div id="card_31" class="card me__32" style="">
Triceratops               <div class="glow" style="background-image: radial-gradient(circle at 498.943px -17.5953px, rgba(255, 255, 255, 0.267), rgba(0, 0, 0, 0.06));"></div>
               <style ready="">#card_31 { background-image: url(https://raw.githubusercontent.com/Santiago-R/extinction_adventure/refs/heads/main/imgs/_Triceratops.png); }</style>
             </div>
           </div>
         </div>
       </div>


<script>const cards = document.querySelectorAll('.card');
let bounds;
let card;

function rotateToMouse(e) {
  const mouseX = e.clientX;
  const mouseY = e.clientY;
  const leftX = mouseX - bounds.x;
  const topY = mouseY - bounds.y;
  const center = {
    x: leftX - bounds.width / 2,
    y: topY - bounds.height / 2
  }
  const distance = Math.hypot(center.x, center.y)
  const amt = 1.3

  card.style.transform = `
    scale3d(${1 + 0.07 * amt}, ${1 + 0.07 * amt}, 1.0)
    rotate3d(
      ${center.y / 100 * amt},
      ${-center.x / 100 * amt},
      0,
      ${Math.sqrt(distance) * amt}deg
    )
    `;

  card.querySelector('.glow').style.backgroundImage = `
    radial-gradient(
      circle at
      ${center.x * 2 + bounds.width / 2}px
      ${center.y * 2 + bounds.height / 2}px,
      #ffffff44,
      #0000000f
    )
  `;
}

for (let i = 0; i < cards.length; i++) {
  cards[i].addEventListener('mouseenter', () => {
    card = cards[i]
    bounds = card.getBoundingClientRect();
    document.addEventListener('mousemove', rotateToMouse);
  });
  cards[i].addEventListener('mouseleave', () => {
    card = null
    document.removeEventListener('mousemove', rotateToMouse);
    cards[i].style.transform = '';
    cards[i].style.background = '';
  });
}</script>