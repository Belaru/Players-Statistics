from players.Athlete import Athlete

"""
Represents a swimmer.

Attributes:
    stroke_style (str): Primary swimming stroke.
    personal_best_time (float, optional): Personal best swim time (in seconds).

Class Attributes:
    swimmer_count (int): Tracks number of Swimmer instances.
"""
class Swimmer(Athlete):
    swimmer_count = 0

    def __init__(self, name, age, stroke_style, country=None, salary=None, personal_best_time=None):
        super().__init__(name, age, country, salary)
        # Swimmer-specific fields like stroke style and best time
        self.stroke_style = stroke_style.strip() if stroke_style else None
        self.personal_best_time = float(personal_best_time) if personal_best_time else None

        Swimmer.swimmer_count += 1
        print(f"Swimmer '{self.name}', {self.age} created; total #of swimmers {Swimmer.swimmer_count}.")

    @staticmethod
    def parse(text):
        # Parse a line of text into a Swimmer object
        parts = [p.strip() for p in text.split(",")]
        return Swimmer(*parts[:6])

    def printStats(self):
        print(f"Stroke Style: {self.stroke_style}\nBest Time: {self.personal_best_time}")

    def __repr__(self):
        fields = [
            self.name, self.age, self.stroke_style,
            self.country, self.salary, self.personal_best_time
        ]
        return f"Swimmer: {','.join('' if f is None else str(f) for f in fields)}"

