import enum
import json

class Mode(enum.Enum):
    PAUSE=1
    LETTERS=2
    NUMBERS=2

class _Team():
    def __init__(self, number):
        self.name = "Team{0}".format(number)
        self.score = 0

    def toJSON(self):
        return json.dumps({"Team": {
            "name": self.name,
            "score": self.score
        }})

# TODO read data from saved file
class GameData():
    def __init__(self, fileName=None):
        self.team1 = _Team(1)
        self.team2 = _Team(2)

        self.mode = Mode.PAUSE

    def toJSON(self):
        return json.dumps({"GameData": {
            "team1": json.loads(self.team1.toJSON()),
            "team2": json.loads(self.team2.toJSON()),
            "mode": str(self.mode)
        }})
