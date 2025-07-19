task = input("Enter your task: ").strip()
priority = input("Priority (high/medium/low): ").strip().lower()
time_bound = input("Is it time-bound> (yes/no): ").strip().lower()

match priority:
    case "high":
        if priority == "high" and time_bound == "yes":
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        elif time_bound == "no":
            print(f"Note: '{task}' is a high priority task. Consider completing it when you have free time.")
    case "medium":
        if priority == "medium" and time_bound == "yes":
            print(f"Reminder: '{task}' is a medium priority task that requires immediate attention today!")
        elif time_bound == "no":
            print(f"Note: '{task}' is a medium priority task. Consider completing it when you have free time.")
    case "low":
        if priority == "low" and time_bound == "yes":
            print(f"Reminder: '{task}' is a low priority task that requires immediate attention today!")
        elif time_bound == "no":
            print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
    case _:
        print("Invalid priority level. Please enter 'high', 'medium', or 'low'.")