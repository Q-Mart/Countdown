// class Team() {
//   constructor(name, score) {
//     this.name = name;
//     this.score = score;
//   }
// }

// class GameData() {
//   constructor(team1, team2, mode) {
//     this.team1 = team1;
//     this.team2 = team2;
//     this.mode = mode;
//   }
// }
var ws = new WebSocket("ws://localhost:8888/socControl");
ws.onopen = function() {
   ws.send("Hello, world");
};
ws.onmessage = function (evt) {
   console.log(evt.data);
};
