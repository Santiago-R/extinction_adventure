const cards = document.querySelectorAll('.card');
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
}