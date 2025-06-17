from players.Athlete import Athlete

from enum import Enum

"""
Enum representing valid hockey positions.

Values:
    - Forward
    - Defenseman
    - Goalie
"""
class HockeyPosition(Enum):
    Forward = "Forward"
    Defenseman = "Defenseman"
    Goalie = "Goalie"

"""
Represents a hockey player.

Attributes:
    position (HockeyPosition): Player's position on the team.
    goals_scored (int): Number of goals scored.
    stick_brand (str, optional): Brand of hockey stick used.
    skates_size (int, optional): Skate size.

Class Attributes:
    hockey_count (int): Tracks number of HockeyPlayer instances.
"""
class HockeyPlayer(Athlete):
    hockey_count = 0

    def __init__(self, name, age, country=None, salary=None, position=None,
                 goals_scored=None, stick_brand=None, skates_size=None):
        super().__init__(name, age, country, salary)
        # Hockey-specific fields + enum for position
        self.position = HockeyPosition[position] if position else None
        self.goals_scored = int(goals_scored) if goals_scored else 0
        self.stick_brand = stick_brand.strip() if stick_brand else None
        self.skates_size = int(skates_size) if skates_size else None

        HockeyPlayer.hockey_count += 1
        print(f"Hockey Player '{self.name}', {self.age} created; total #of hockey players {HockeyPlayer.hockey_count}.")

    @staticmethod
    def parse(text):
        parts = [p.strip() for p in text.split(",")]
        return HockeyPlayer(*parts[:8])

    def printStats(self):
        print(f"Position: {self.position.name if self.position else 'Unknown'}\nGoals Scored: {self.goals_scored}")

    def __repr__(self):
        fields = [
            self.name, self.age, self.country, self.salary,
            self.position.name if self.position else None,
            self.goals_scored, self.stick_brand, self.skates_size
        ]
        return f"HockeyPlayer: {','.join('' if f is None else str(f) for f in fields)}"
