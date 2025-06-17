import matplotlib.pyplot as plt
from collections import Counter
from players import *
from players.HockeyPlayer import HockeyPlayer
from players.BallPlayer import BallPlayer, BasketballPlayer, FootballPlayer
from players.Swimmer import Swimmer

# Generic parser based on type prefix
def parse_line(line): 
    if ":" not in line:
        return None
    type_, rest = line.split(":", 1)
    type_ = type_.strip().lower()
    try:
        if type_ == "hockeyplayer":
            return HockeyPlayer.parse(rest)
        elif type_ == "swimmer":
            return Swimmer.parse(rest)
        elif type_ == "basketballplayer":
            return BasketballPlayer.parse(rest)
        elif type_ == "footballplayer":
            return FootballPlayer.parse(rest)
    except Exception as e:
        print(f"Error parsing line: {line}\n{e}")
        return None

# Compute and print summary stats: type counts, endorsements, etc.
def print_statistics(athletes):
    print("Statistics:\n-------------------")
    print(f"{len(athletes)} athletes")
    print(f"{HockeyPlayer.hockey_count} Hockey Players")
    ball_count = BallPlayer.ballplayer_count
    print(f"{ball_count} Ball Players ({BasketballPlayer.basketball_count} Basketball and {FootballPlayer.football_count} Football Players)")
    print(f"{Swimmer.swimmer_count} Swimmers\n")

    endorsements = Counter()
    for a in athletes:
        if isinstance(a, BallPlayer) and a.endorsement:
            endorsements[a.endorsement] += 1

    print("Endorsements:\n-------------------")
    for brand, count in sorted(endorsements.items()):
        print(f"{brand} ({count})")
    print()

    print("Goals Scored:\n-------------------")
    goal_players = sorted([a for a in athletes if isinstance(a, HockeyPlayer)],
                          key=lambda p: (-p.goals_scored, p.name))
    for p in goal_players:
        print(f"{p.goals_scored} {p.name}")
    print()

    print("Touchdowns:\n-------------------")
    touchdown_players = sorted([a for a in athletes if isinstance(a, FootballPlayer) and a.touchdowns is not None],
                                key=lambda p: (-p.touchdowns, p.name))
    for p in touchdown_players:
        print(f"{p.touchdowns} {p.name}")
    print()

# Save athlete list to file using repr()
def save_to_file(filename, athletes):
    with open(filename, 'w', encoding="utf-8") as f:
        for a in athletes:
            f.write(repr(a) + '\n')

# Render a pie chart only if values are present and valid
def show_pie_chart(title, labels, values):
    # print("DEBUG:", list(zip(labels, values)))
    if not values or not any(values):
        print(f"[!] Not enough data to generate chart: {title}")
        return
    plt.figure(figsize=(6, 6))
    plt.pie(values, labels=labels, autopct='%1.1f%%')
    plt.title(title)
    plt.show()
