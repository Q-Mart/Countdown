function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

function randomBetween(a,b) {
  diff = b-a
  return Math.floor((Math.random() * diff) + a);
}

function randomlyChangeNumber() {
  document.getElementById('randomNumber').innerHTML = randomBetween(100, 999);
}

window.onload = async function () {
  await sleep(500);

  var interval = setInterval(randomlyChangeNumber, 50);
  setTimeout(function() {clearInterval(interval)}, 1500);
}
