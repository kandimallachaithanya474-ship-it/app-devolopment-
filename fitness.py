activities = []

while True:
    print("\n1.Add Activity 2.View Activities 3.Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter activity name: ")
        duration = input("Enter duration (minutes): ")
        calories = input("Enter calories burned: ")

        activity = {
            "name": name,
            "duration": duration,
            "calories": calories
        }

        activities.append(activity)
        print("Activity added!")

    elif choice == "2":
        if not activities:
            print("No activities found")
        else:
            for i, a in enumerate(activities):
                print(i+1, a["name"], "-", a["duration"], "mins -", a["calories"], "cal")

    elif choice == "3":
        break

    else:
        print("Invalid choice")