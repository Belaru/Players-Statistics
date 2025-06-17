from Utils import *
from players import *
from players.BallPlayer import BallPlayer, BasketballPlayer, FootballPlayer
from players.Swimmer import Swimmer
from players.HockeyPlayer import HockeyPlayer

import os

def main():
    athletes = []
    filename = ""
    modified = False

    try:
        # Display interactive menu to user
        while True:
            print("\nMenu:\n1. Load File\n2. Print Stats\n3. Delete Athlete\n4. Save File\n5. Athlete Info\n6. Display Chart\n7. Exit")
            choice = input("Enter choice: ").strip()

            # Load athletes from file
            if choice == "1":
                filename = input("Enter filename: ").strip()
                if os.path.exists(filename):
                    with open(filename, encoding="utf-8") as f:
                        for line in f:
                            athlete = parse_line(line.strip())
                            if athlete:
                                athletes.append(athlete)
                    modified = True
                else:
                    print("File not found.")

            # Print stats using print_statistics()
            elif choice == "2":
                print_statistics(athletes)

            # Delete by name, with duplicate warning
            elif choice == "3":
                name = input("Enter athlete name to delete: ").strip()
                matches = [a for a in athletes if a.name == name]
                if not matches:
                    print("Athlete not found.")
                elif len(matches) > 1:
                    print(f"Found {len(matches)} athletes with the name '{name}'.")
                    confirm = input("Delete all of them? (y/n): ").strip().lower()
                    if confirm == "y":
                        athletes = [a for a in athletes if a.name != name]
                        modified = True
                        print("All matching athletes deleted.")
                    else:
                        athletes.remove(matches[0])
                else:
                    athletes.remove(matches[0])
                    modified = True
                    print("Athlete deleted.")

            # Save back to file (with confirmation)
            elif choice == "4":
                if filename:
                    confirm = input("Overwrite file? (y/n): ").strip().lower()
                    if confirm == "y":
                        save_to_file(filename, athletes)
                        modified = False
                        print("File saved.")
                else:
                    print("No file loaded.")

            # Lookup athlete by name and display their info
            elif choice == "5":
                name = input("Enter athlete name: ").strip()
                found = [a for a in athletes if a.name == name]
                if not found:
                    print("Athlete not found.")
                for a in found:
                    print(a)
                    a.printStats()
                    a.printEndorsement()
            # Display pie charts with multiple breakdown options
            elif choice == "6":
                print("Chart Menu:\n1. Number of Athletes (level 1)\n2. Number of Athletes (leaf)\n3. Salaries (level 1)\n4. Salaries (leaf)\n5. Endorsements")
                sub = input("Choose chart: ").strip()

                # Chart 1: Number of athletes (Level 1 inheritance)
                if sub == "1":
                    # Shows distribution of top-level types: HockeyPlayer, BallPlayer, Swimmer
                    labels = ["HockeyPlayer", "BallPlayer", "Swimmer"]
                    values = [HockeyPlayer.hockey_count, BallPlayer.ballplayer_count, Swimmer.swimmer_count]
                    show_pie_chart("Athletes (Level 1)", labels, values)

                # Chart 2: Number of athletes (Leaf classes only)
                elif sub == "2":
                    # Shows how many instances of the most specific subclasses exist
                    labels = ["HockeyPlayer", "BasketballPlayer", "FootballPlayer", "Swimmer"]
                    values = [HockeyPlayer.hockey_count, BasketballPlayer.basketball_count,
                            FootballPlayer.football_count, Swimmer.swimmer_count]
                    show_pie_chart("Athletes (Leaf)", labels, values)

                # Chart 3: Average salary per Level 1 class (HockeyPlayer, BallPlayer, Swimmer)
                elif sub == "3":
                    # Only includes instances with non-null salaries
                    classes = [HockeyPlayer, BallPlayer, Swimmer]
                    labels, values = [], []
                    for cls in classes:
                        group = [a.salary for a in athletes if isinstance(a, cls) and a.salary is not None]
                        if group:
                            labels.append(cls.__name__)
                            values.append(sum(group) / len(group))
                    show_pie_chart("Avg Salaries (Level 1)", labels, values)

                # Chart 4: Average salary per Leaf class (HockeyPlayer, BasketballPlayer, FootballPlayer, Swimmer)
                elif sub == "4":
                    # Ignores athletes without salary values
                    classes = [HockeyPlayer, BasketballPlayer, FootballPlayer, Swimmer]
                    labels, values = [], []
                    for cls in classes:
                        group = [a.salary for a in athletes if isinstance(a, cls) and a.salary is not None]
                        if group:
                            labels.append(cls.__name__)
                            values.append(sum(group) / len(group))
                    show_pie_chart("Avg Salaries (Leaf)", labels, values)

                # Chart 5: Number of BallPlayers per endorsement brand
                elif sub == "5":
                    # Aggregates endorsements sorted alphabetically
                    endorsements = Counter(a.endorsement for a in athletes
                                        if isinstance(a, BallPlayer) and a.endorsement)
                    labels, values = zip(*sorted(endorsements.items()))
                    show_pie_chart("Endorsements", labels, values)

            # Exit safely (with unsaved changes warning)
            elif choice == "7":
                if modified:
                    confirm = input("Unsaved changes detected. Exit anyway? (y/n): ").strip().lower()
                    if confirm != "y":
                        continue
                print("Goodbye!")
                break

            else:
                print("Invalid choice.")

    except KeyboardInterrupt: # Graceful exit on Ctrl+C
        print("\n\nDetected Ctrl+C — exiting program.")
        if modified:
            confirm = input("You have unsaved changes. Exit anyway? (y/n): ").strip().lower()
            if confirm != "y":
                main()  # re-enter main loop
                return
        print("Goodbye!")
if __name__ == "__main__":
    main()
