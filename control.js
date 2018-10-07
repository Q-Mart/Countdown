var ws = new WebSocket("ws://localhost:8888/socControl");

try {
  var data = new GameData();
} catch(err) {
  console.error("gameData.js not included! Make sure you have <script src=\"resources/gameData.js\"></script> included above the inclusion of this script in your HTML!");
}

ws.onopen = function() {
   // ws.send("Hello, world");
};
ws.onmessage = function (evt) {
  console.debug("Recieved:" + evt.data);
  data = stringToGameData(evt.data);

  console.debug("Parsed into:");
  console.debug(data);
};
