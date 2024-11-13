import datetime
import time

reminders = {}

def add_reminder(date, time, message):
    reminders[f"{date} {time}"] = message
    print("Reminder added successfully")

def view_reminders():
    for reminder_time, message in reminders.items():
        print(f"{reminder_time}: {message}")

def check_reminders():
    while True:
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        if current_time in reminders:
            print(f"Reminder: {reminders[current_time]}")
            del reminders[current_time]
        time.sleep(60)

while True:
    print("1. Add Reminder")
    print("2. View Reminders")
    print("3. Check Reminders")
    print("4. Quit")
    choice = input("Enter your choice: ")
    if choice == "1":
        date = input("Enter date: ")
        time = input("Enter time: ")
        message = input("Enter message: ")
        add_reminder(date, time, message)
    elif choice == "2":
        view_reminders()
    elif choice == "3":
        check_reminders()
    elif choice == "4":
        break
    else:
        print("Invalid choice")
