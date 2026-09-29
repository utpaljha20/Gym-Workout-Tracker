from storage import get_workouts


def show_progress():
    workouts = get_workouts()

    print("\n----- PROGRESS TRACKER -----")

    if not workouts:
        print("No workout data available.")
        return

    exercise_name = input(
        "Enter exercise name to check progress: "
    ).strip()

    selected_workouts = []

    for workout in workouts:
        if workout["Exercise"].lower() == exercise_name.lower():
            selected_workouts.append(workout)

    if not selected_workouts:
        print("No records found for this exercise.")
        return

    highest_weight = max(
        float(workout["Weight"])
        for workout in selected_workouts
    )

    total_sets = sum(
        int(workout["Sets"])
        for workout in selected_workouts
    )

    total_reps = sum(
        int(workout["Reps"]) * int(workout["Sets"])
        for workout in selected_workouts
    )

    print("\nExercise:", selected_workouts[0]["Exercise"])
    print("Muscle Group:", selected_workouts[0]["Muscle Group"])
    print("Highest Weight:", highest_weight, "kg")
    print("Total Sets:", total_sets)
    print("Total Reps:", total_reps)
    print("Number of Sessions:", len(selected_workouts))