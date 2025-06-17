from players.Athlete import Athlete

"""
Abstract subclass of Athlete for team-based ball sports.

Attributes:
    team_name (str): Name of the athlete's team.
    jersey_number (int): Jersey number.
    endorsement (str, optional): Endorsement brand or sponsor.

Class Attributes:
    ballplayer_count (int): Tracks number of BallPlayer instances.
"""
class BallPlayer(Athlete):
    ballplayer_count = 0

    def __init__(self, name, age, team_name, jersey_number, country=None, salary=None, endorsement=None):
        super().__init__(name, age, country, salary)
        # Add ball-player-specific attributes
        self.team_name = team_name.strip() if team_name else None
        self.jersey_number = int(jersey_number) if jersey_number else None
        self.endorsement = endorsement.strip() if endorsement else None

        BallPlayer.ballplayer_count += 1
        print(f"Ball Player '{self.name}', {self.age} created; total #of ball players {BallPlayer.ballplayer_count}.")

    def printEndorsement(self):
        # All BallPlayers have endorsements
        pass

    def __str__(self):
        return super().__str__() + f"\nTeam: {self.team_name}\nJersey #: {self.jersey_number}\nEndorsement: {self.endorsement}"

"""
Represents a basketball player.

Attributes:
    three_point_pct (float, optional): 3-point shot percentage.
    rebounds (int, optional): Number of rebounds recorded.

Class Attributes:
    basketball_count (int): Tracks number of BasketballPlayer instances.
"""
class BasketballPlayer(BallPlayer):
    basketball_count = 0
    
    def __init__(self, name, age, team_name, jersey_number, country=None, salary=None, endorsement=None,
                 three_point_pct=None, rebounds=None):
        super().__init__(name, age, team_name, jersey_number, country, salary, endorsement)
        # Basketball-specific fields like touchdowns and passing yards
        self.three_point_pct = float(three_point_pct) if three_point_pct else None
        self.rebounds = int(rebounds) if rebounds else None

        BasketballPlayer.basketball_count += 1
        print(f"Basketball Player '{self.name}', {self.age} created; total #of basketball players {BasketballPlayer.basketball_count}.")

    @staticmethod
    def parse(text):
        # Parse from text line to BasketballPlayer object
        parts = [p.strip() for p in text.split(",")]
        return BasketballPlayer(*parts[:9])

    def printStats(self):
        print(f"3PT%: {self.three_point_pct}\nRebounds: {self.rebounds}")

    def printEndorsement(self):
        print(f"Basketball PlayerEndorsement: {self.endorsement}")

    def __repr__(self):
        fields = [
            self.name, self.age, self.team_name, self.jersey_number,
            self.country, self.salary, self.endorsement,
            self.three_point_pct, self.rebounds
        ]
        return f"BasketballPlayer: {','.join('' if f is None else str(f) for f in fields)}"


"""
Represents a football player.

Attributes:
    touchdowns (int, optional): Total number of touchdowns.
    passing_yards (int, optional): Total passing yards.

Class Attributes:
    football_count (int): Tracks number of FootballPlayer instances.
"""
class FootballPlayer(BallPlayer):
    football_count = 0

    def __init__(self, name, age, team_name, jersey_number, country=None, salary=None, endorsement=None,
                 touchdowns=None, passing_yards=None):
        super().__init__(name, age, team_name, jersey_number, country, salary, endorsement)
        # Football-specific fields like touchdowns and passing yards
        self.touchdowns = int(touchdowns) if touchdowns else None
        self.passing_yards = int(passing_yards) if passing_yards else None

        FootballPlayer.football_count += 1
        print(f"Football Player '{self.name}', {self.age} created; total #of football players {FootballPlayer.football_count}.")

    @staticmethod
    def parse(text): 
        # Football-specific fields like touchdowns and passing yards
        parts = [p.strip() for p in text.split(",")]
        return FootballPlayer(*parts[:9])

    def printStats(self):
        print(f"Touchdowns: {self.touchdowns}\nPassing Yards: {self.passing_yards}")

    def printEndorsement(self):
        print(f"Football Player Endorsement: {self.endorsement}")

    def __repr__(self):
        fields = [
            self.name, self.age, self.team_name, self.jersey_number,
            self.country, self.salary, self.endorsement,
            self.touchdowns, self.passing_yards
        ]
        return f"FootballPlayer: {','.join('' if f is None else str(f) for f in fields)}"

