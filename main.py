from exercise import add_exercise, show_exercises
from workout import record_workout, show_workout_history
from progress import show_progress
from summary import show_summary
from storage import initialize_files


def show_menu():
    print("\n================================")
    print("       GYM WORKOUT TRACKER")
    print("================================")
    print("1. Add Exercise")
    print("2. Record Workout")
    print("3. View Workout History")
    print("4. View Progress")
    print("5. Workout Summary")
    print("6. View Exercise List")
    print("7. Exit")


def main():
    initialize_files()

    while True:
        show_menu()

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_exercise()

        elif choice == "2":
            record_workout()

        elif choice == "3":
            show_workout_history()

        elif choice == "4":
            show_progress()

        elif choice == "5":
            show_summary()

        elif choice == "6":
            show_exercises()

        elif choice == "7":
            print("\nThank you for using Gym Workout Tracker!")
            break

        else:
            print("\nInvalid choice. Please enter a number from 1 to 7.")


if __name__ == "__main__":
    main() 
