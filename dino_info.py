info_list = [
    {'name': 'Plesiosaurio', 'incubation': 5, 'ecosystem': ['jungla', 'hielo'], 'description': 'Acuático. El jugador que juega la carta de Plesiosaurio puede mostrar sus cartas al resto de jugadores.'},
    {'name': 'Plesiosaurio del oasis', 'incubation': 5, 'ecosystem': ['desierto'], 'description': 'Acuático. Elimina la extinción automática en el desierto cada ronda.'},
    {'name': 'Maiasaura', 'incubation': 3, 'ecosystem': ['jungla'], 'description':  'Protege todos los huevos del tablero. Permite eclosionar huevos una ronda antes de tiempo.'},
    {'name': 'Anquilosaurio', 'incubation': 5, 'ecosystem': ['jungla', 'hielo'], 'description': 'Cuando el huevo de Anquilosaurio eclosiona, roba una carta.'},
    {'name': 'Minmi', 'incubation': 1, 'ecosystem': ['desierto'], 'description': 'Al final de la ronda, puede migrar al origen de otra migración ocurrida este turno.'},
    {'name': 'Diplodocus verde', 'incubation': 5, 'ecosystem': ['jungla'], 'description': 'En caso de incendio, sobreviven hasta tres dinosarios distintos al diplodocus verde.'},
    {'name': 'Diplodocus rocoso', 'incubation': 4, 'ecosystem': ['volcán'], 'description': 'En caso de erupción volcánica, sobreviven hasta dos dinosarios distintos al diplodocus rocoso.'},
    {'name': 'Diplodocus blanco', 'incubation': 6, 'ecosystem': ['hielo'], 'description': 'Protege a todos los dinosaurios de la jungla de la edad de hielo.'},
    {'name': 'Pterosaurio', 'incubation': 2, 'ecosystem': ['hielo', 'desierto'], 'description': 'Vuela, migra instantáneamente al hielo o al desierto.'},
    {'name': 'Pterodáctilo', 'incubation': 2, 'ecosystem': ['jungla'], 'description': 'Vuela, migra instantáneamente con la condición de extinguir un dinosaurio en el ecosistema de destino.'},
    {'name': 'Utahraptor', 'incubation': 4, 'ecosystem': ['volcán'], 'description': 'Puede unirse a la migración de otro dinosaurio de su ecosistema.'},
    {'name': 'Estiracosaurio', 'incubation': 3, 'ecosystem': ['jungla'], 'description': 'Puede migrar a cualquier ecosistema vacío al final de la ronda.'},
    {'name': 'Herrerasaurio', 'incubation': 4, 'ecosystem': ['jungla'], 'description': 'Cada turno, otro dinosaurio de su ecosistema migra al volcán huyendo del herrerasaurio.'},
    {'name': 'Edmontosaurio', 'incubation': 5, 'ecosystem': ['hielo'], 'description': 'Puede migrar al final de la ronda, intercambiando su posición con otro dinosaurio.'},
    {'name': 'Tarquia', 'incubation': 7, 'ecosystem': ['volcán'], 'description': 'El huevo de Tarquia protege a todos los huevos de erupciones volcánicas.'},
    {'name': 'Microraptor', 'incubation': 1, 'ecosystem': ['jungla', 'desierto'], 'description': 'Invulnerable a la extinción automática en el desierto (no protege a otros).'},
    {'name': 'Camarasauro', 'incubation': 7, 'ecosystem': ['hielo'], 'description': 'Elimina la extinción automática en el hielo.'},
    {'name': 'Compsognathus', 'incubation': 1, 'ecosystem': ['volcán', 'desierto'], 'description': 'Puede migrar al final de la ronda, si intercambia su posición con un huevo de dinosaurio.'},
    {'name': 'Paquicefalosaurio', 'incubation': 3, 'ecosystem': ['jungla'], 'description': 'Ladrón de huevos. Puede migrar al final de la ronda, si lleva con él al menos dos huevos de su ecosistema al ecosistema de destino.  Su extinción protege a todos los huevos de su ecosistema hasta la siguiente ronda.'},
    {'name': 'Estegosaurio naranja', 'incubation': 5, 'ecosystem': ['jungla', 'volcán'], 'description': 'Permite poner huevos naturales de la jungla en el volcán.'},
    {'name': 'Estegosaurio violeta', 'incubation': 5, 'ecosystem': ['jungla', 'hielo'], 'description': 'Permite poner huevos naturales de la jungla en el hielo.'},
    {'name': 'Iguanodón', 'incubation': 4, 'ecosystem': ['volcán', 'desierto'], 'description': 'Permite poner cualquier huevo en el ecosistema donde está el iguanodón.'},
    {'name': 'Parasaurolophus', 'incubation': 6, 'ecosystem': ['volcán', 'jungla'], 'description': 'Puede migrar al instante al volcán o la jungla, con el coste de devorar un dinosaurio en el nuevo ecosistema.'},
    {'name': 'Velociraptor', 'incubation': 2, 'ecosystem': ['jungla'], 'description': 'Puede migrar instantáneamente, devorando a un dinosaurio fuera de su ecosistema. Vuelve a su ecosistema de origen al final del turno.'},
    {'name': 'Velociraptor mini', 'incubation': 1, 'ecosystem': ['jungla'], 'description': 'Puede migrar instantáneamente, devorando un huevo fuera de su ecosistema. Vuelve a su ecosistema de origen al final del turno.'},
    {'name': 'Saurópodo', 'incubation': 3, 'ecosystem': ['desierto', 'hielo'], 'description': 'Puede migrar a cualquier ecosistema al final de la ronda. Cuando se extingue, el jugador que jugó la carta de Saurópodo roba una carta.'},
    {'name': 'Huayangosaurio', 'incubation': 4, 'ecosystem': ['volcán', 'desierto'], 'description': 'No puede ser devorado por otros dinosaurios. Cuando se extingue, el jugador que jugó la carta de Huayangosaurio roba una carta.'},
    {'name': 'Paquirrinosaurio', 'incubation': 3, 'ecosystem': ['hielo', 'volcán'], 'description': 'Su extinción protege a todos los dinosaurios de su ecosistema hasta la siguiente ronda.'},
    {'name': 'Espinosaurio', 'incubation': 2, 'ecosystem': ['jungla'], 'description': 'Puede devorar instantáneamente a otro dinosaurio. El jugador que jugó el dinosaurio devorado roba una carta.'},
    {'name': 'Protoceratops caramelo', 'incubation': 3, 'ecosystem': ['desierto'], 'description': 'El jugador que juegue la carta de protoceratops caramelo levanta las siguientes cinco cartas del mazo de dinosaurios, y las coloca en la parte superior o inferior del mazo en cualquier orden.'},
    {'name': 'Protoceratops rosita', 'incubation': 3, 'ecosystem': ['volcán'], 'description': 'El jugador que juegue la carta de protoceratops rosita levanta las siguientes cinco cartas del mazo de dinosaurios, y las coloca en la parte superior o inferior del mazo en cualquier orden.'},
    {'name': 'Triceratops', 'incubation': 4, 'ecosystem': ['jungla'], 'description': 'Su extinción protege a otro dinosaurio hasta la siguiente ronda.'},
]