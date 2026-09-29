from validation import (
    get_non_empty_input,
    get_positive_number,
    get_positive_integer
)

from storage import (
    get_exercises,
    save_workout,
    get_workouts
)


def record_workout():
    print("\n----- RECORD WORKOUT -----")

    exercises = get_exercises()

    if not exercises:
        print("\nNo exercises found.")
        print("Please add an exercise first.")
        return

    print("\nAvailable Exercises:")

    for number, exercise in enumerate(exercises, start=1):
        print(
            f"{number}. {exercise['Exercise']} "
            f"({exercise['Muscle Group']})"
        )

    while True:
        try:
            choice = int(input("\nSelect exercise number: "))

            if 1 <= choice <= len(exercises):
                selected = exercises[choice - 1]
                break

            print("Please select a valid exercise number.")

        except ValueError:
            print("Please enter a valid number.")

    date = get_non_empty_input("Enter date (DD-MM-YYYY): ")
    weight = get_positive_number("Enter weight (kg): ")
    sets = get_positive_integer("Enter number of sets: ")
    reps = get_positive_integer("Enter reps per set: ")

    save_workout(
        date,
        selected["Exercise"],
        selected["Muscle Group"],
        weight,
        sets,
        reps
    )

    print("\nWorkout recorded successfully!")


def show_workout_history():
    workouts = get_workouts()

    print("\n----- WORKOUT HISTORY -----")

    if not workouts:
        print("No workout records found.")
        return

    print(
        f"{'Date':<15}"
        f"{'Exercise':<20}"
        f"{'Muscle':<15}"
        f"{'Weight':<10}"
        f"{'Sets':<8}"
        f"{'Reps':<8}"
    )

    print("-" * 76)

    for workout in workouts:
        print(
            f"{workout['Date']:<15}"
            f"{workout['Exercise']:<20}"
            f"{workout['Muscle Group']:<15}"
            f"{workout['Weight']:<10}"
            f"{workout['Sets']:<8}"
            f"{workout['Reps']:<8}"
        )