from storage import get_workouts


def show_summary():
    workouts = get_workouts()

    print("\n----- WORKOUT SUMMARY -----")

    if not workouts:
        print("No workout data available.")
        return

    total_sessions = len(workouts)

    total_sets = sum(
        int(workout["Sets"])
        for workout in workouts
    )

    total_reps = sum(
        int(workout["Sets"]) * int(workout["Reps"])
        for workout in workouts
    )

    total_volume = sum(
        float(workout["Weight"])
        * int(workout["Sets"])
        * int(workout["Reps"])
        for workout in workouts
    )

    muscle_count = {}

    for workout in workouts:
        muscle = workout["Muscle Group"]

        if muscle in muscle_count:
            muscle_count[muscle] += 1
        else:
            muscle_count[muscle] = 1

    most_trained_muscle = max(
        muscle_count,
        key=muscle_count.get
    )

    print("Total Workout Entries:", total_sessions)
    print("Total Sets:", total_sets)
    print("Total Reps:", total_reps)
    print("Total Volume:", round(total_volume, 2), "kg")
    print("Most Trained Muscle:", most_trained_muscle)