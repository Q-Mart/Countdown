try {
  var data = new GameData();
} catch(err) {
  console.error("gameData.js not included! Make sure you have <script src=\"resources/gameData.js\"></script> included above the inclusion of this script in your HTML!");
}

function updatePageAccordingToData() {
  radioButtonIdString = "";
  switch (data.mode) {
    case "Mode.PAUSE":
      radioButtonIdString = "radioPause";
      break;

    case "Mode.LETTERS":
      radioButtonIdString = "radioLetters";
      break;

    case "Mode.NUMBERS":
      radioButtonIdString = "radioNumbers";
      break;
  }
  document.getElementById(radioButtonIdString).checked = true;

  document.getElementById("team1Name").innerHTML = data.team1.name;
  document.getElementById("team2Name").innerHTML = data.team2.name;
  document.getElementById("team1Score").innerHTML = data.team1.score;
  document.getElementById("team2Score").innerHTML = data.team2.score;
}

var ws = new WebSocket("ws://localhost:8888/socControl");
ws.onopen = function() {
   // ws.send("Hello, world");
};

ws.onmessage = function (evt) {
  console.debug("Recieved:" + evt.data);
  data = stringToGameData(evt.data);

  console.debug("Parsed into:");
  console.debug(data);

  updatePageAccordingToData();
};
