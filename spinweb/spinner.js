let spinning = false;
function spinWheel() {
  if (spinning) return;
  spinning = true;
  let wheel = document.getElementById("spinWheel");
  let deg = (Math.floor(Math.random() * 6) + 6) * 360 + Math.floor(Math.random()*360);
  wheel.style.transition = "transform 2.5s cubic-bezier(.22,.68,.81,.42)";
  wheel.style.transform = `rotate(${deg}deg)`;
  setTimeout(() => {
    spinning = false;
    fetch('/spin', {method:'POST'}).then(r=>r.json()).then(d=>{
      document.getElementById('rupeecoins').textContent = d.coins;
      document.getElementById('result').textContent = d.message;
    });
  }, 2600);
}
function exchangeCoins() {
  alert("Coin exchange coming soon!");
}
