from enum import Enum

"""
Base class representing a generic athlete.

Attributes:
    name (str): Athlete's full name.
    age (int): Age of the athlete.
    country (str, optional): Country of origin.
    salary (float, optional): Annual salary in dollars.

Class Attributes:
    athlete_count (int): Tracks number of Athlete instances created.
"""
class Athlete:
    athlete_count = 0 # Class-level counter for total athletes

    def __init__(self, name, age, country=None, salary=None):
        # Initialize base attributes, handling optional values
        self.name = name.strip() if name else None
        self.age = int(age) if age else None
        self.country = country.strip() if country else None
        self.salary = float(salary) if salary else None

        Athlete.athlete_count += 1
        print(f"Athlete '{self.name}', {self.age} created; total #of athletes {Athlete.athlete_count}.")

    def printStats(self):
        # To be overridden by subclasses
        pass

    def printEndorsement(self):
        # Only relevant for BallPlayer subclasses
        pass

    def __str__(self):
        # Generic string representation of any athlete
        return f"Name: {self.name}\nAge: {self.age}\nCountry: {self.country}\nSalary: {self.salary}"
