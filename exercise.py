from validation import get_non_empty_input
from storage import save_exercise, get_exercises


def add_exercise():
    print("\n----- ADD EXERCISE -----")

    exercise_name = get_non_empty_input("Enter exercise name: ")
    muscle_group = get_non_empty_input("Enter muscle group: ")

    exercises = get_exercises()

    for exercise in exercises:
        if exercise["Exercise"].lower() == exercise_name.lower():
            print("This exercise already exists.")
            return

    save_exercise(exercise_name, muscle_group)

    print("\nExercise added successfully!")
    print("Exercise:", exercise_name)
    print("Muscle Group:", muscle_group)


def show_exercises():
    exercises = get_exercises()

    if not exercises:
        print("\nNo exercises available.")
        return

    print("\n----- EXERCISE LIST -----")

    for number, exercise in enumerate(exercises, start=1):
        print(
            f"{number}. {exercise['Exercise']} "
            f"({exercise['Muscle Group']})"
        )