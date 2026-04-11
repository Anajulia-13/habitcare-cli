import json
from datetime import date

FILE = "data.json"


def load_data():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def save_data(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=2)


def add_habit(name):
    if not name:
        raise ValueError("Nome inválido")

    data = load_data()
    habit = {
        "name": name,
        "date": str(date.today()),
        "done": False
    }
    data.append(habit)
    save_data(data)


def list_habits():
    return load_data()


def complete_habit(index):
    data = load_data()
    if index < 0 or index >= len(data):
        raise IndexError("Índice inválido")

    data[index]["done"] = True
    save_data(data)
