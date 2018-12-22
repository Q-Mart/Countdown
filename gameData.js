class Team {
  constructor(name, score) {
    this.name = name;
    this.score = score;
  }
}

class GameData {
  constructor(team1, team2, mode) {
    this.team1 = team1;
    this.team2 = team2;
    this.mode = mode;
  }
}

function stringToGameData(string) {
  ret = JSON.parse(string)["GameData"];
  ret.team1 = ret.team1["Team"];
  ret.team2 = ret.team2["Team"];

  return ret;
}
