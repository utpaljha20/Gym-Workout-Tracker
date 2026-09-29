import csv
import os


# Always use the data folder inside this project
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FOLDER = os.path.join(BASE_DIR, "data")

EXERCISE_FILE = os.path.join(DATA_FOLDER, "exercises.csv")
WORKOUT_FILE = os.path.join(DATA_FOLDER, "workouts.csv")


def initialize_files():
    os.makedirs(DATA_FOLDER, exist_ok=True)

    if not os.path.exists(EXERCISE_FILE):
        with open(EXERCISE_FILE, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Exercise", "Muscle Group"])

    if not os.path.exists(WORKOUT_FILE):
        with open(WORKOUT_FILE, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(
                ["Date", "Exercise", "Muscle Group", "Weight", "Sets", "Reps"]
            )


def save_exercise(exercise, muscle_group):
    initialize_files()

    with open(EXERCISE_FILE, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([exercise, muscle_group])


def get_exercises():
    initialize_files()

    with open(EXERCISE_FILE, "r", newline="") as file:
        reader = csv.DictReader(file)
        return list(reader)


def save_workout(date, exercise, muscle_group, weight, sets, reps):
    initialize_files()

    with open(WORKOUT_FILE, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(
            [date, exercise, muscle_group, weight, sets, reps]
        )


def get_workouts():
    initialize_files()

    with open(WORKOUT_FILE, "r", newline="") as file:
        reader = csv.DictReader(file)
        return list(reader)