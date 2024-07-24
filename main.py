class WorkoutManager:
    def __init__(self):
        self.workouts = []

    def add_workout(self, name, date, duration, calories):
        workout = {
            'name': name,
            'date': date,
            'duration': duration,
            'calories': calories
        }
        self.workouts.append(workout)
        print(f"Added workout: {name} on {date} for {duration} minutes, burning {calories} calories.")

    def view_workouts(self):
        if not self.workouts:
            print("No workouts to display.")
            return

        for i, workout in enumerate(self.workouts, 1):
            print(f"{i}. {workout['name']} on {workout['date']} for {workout['duration']} minutes, burning {workout['calories']} calories.")

    def delete_workout(self, index):
        try:
            removed_workout = self.workouts.pop(index - 1)
            print(f"Deleted workout: {removed_workout['name']} on {removed_workout['date']}.")
        except IndexError:
            print("Invalid workout number.")

def main():
    manager = WorkoutManager()

    while True:
        print("\nWorkout Manager")
        print("1. Add workout")
        print("2. View workouts")
        print("3. Delete workout")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter workout name: ")
            date = input("Enter workout date (YYYY-MM-DD): ")
            duration = input("Enter workout duration (in minutes): ")
            calories = input("Enter calories burned: ")
            manager.add_workout(name, date, duration, calories)
        elif choice == '2':
            manager.view_workouts()
        elif choice == '3':
            manager.view_workouts()
            index = int(input("Enter the workout number to delete: "))
            manager.delete_workout(index)
        elif choice == '4':
            print("Exiting the Workout Manager.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
