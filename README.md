# 🏅 Athlete Statistics Manager

A command-line Python application to manage and analyze a database of athletes. Built for a COMP348 assignment, this program allows users to store, display, and compare statistics of athletes across different sports.

---

## 📂 Features

- 📋 Load athletes from a text-based database
- ➕ Add new athletes (Football, Basketball, Hockey, Swimmer)
- 🗑️ Delete existing athletes
- 🔍 Search by athlete name
- 📈 Display sport-specific statistics
- 🏆 Compare players by performance metrics
- 💾 Save changes back to the database file

---

## 🧾 File Format

Athletes are stored in a plain text file using a structured format. Each line represents one athlete and contains their sport, name, and statistics.

Example line:
```
Basketball,LeBron James,28.1,8.0,7.5
```

---

## 🛠️ How to Run

1. Clone this repository:
```bash
git clone https://github.com/YOUR_USERNAME/athlete-stats.git
cd athlete-stats
```

2. Run the program:
```bash
python main.py
```

> Requires Python 3.7 or higher.

---

## 📁 Project Structure

```
athlete-stats/
├── players/
│   ├── Athlete.py
│   ├── FootballPlayer.py
│   ├── BasketballPlayer.py
│   ├── Swimmer.py
│   └── HockeyPlayer.py
├── main.py
├── utils.py
├── database.txt
└── README.md
```

---

## 👩‍💻 Author

Anastasia Bondarenko  
Software Engineering @ Concordia University

---

## 📎 License

This project is for educational use under COMP348-Principles of Programing.
