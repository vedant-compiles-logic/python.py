subjects = {}

def subject_manager():
    while True:
        print("\nSubject manager")
        print("1. Add Subject")
        print("2. View Subjects")
        print("3. Go back")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter subject name: ")
            if name in subjects:
                print("Subject already exists.")
            else:
                marks = float(input("Enter marks out of 100: "))
                if 0 <= marks <= 100:
                    subjects[name] = marks
                    print("Subject added successfully!")
                else:
                    print("Marks must be between 0 and 100.")

        elif choice == "2":
            if not subjects:
                print("No subjects added yet.")
            else:
                print("\nSubjects:")
                for name, marks in subjects.items():
                    print(f"{name}: {marks}")

        elif choice == "3":
            print("Returning to main menu.")
            break

        else:
            print("Invalid choice. Try again. ")

study_records = []

def study_tracker():
    while True:
        print("\nStudy tracker")
        print("1. Record study session ")
        print("2. View study Records ")
        print("3. Go back ")

        choice = input("Enter your choice: ")

        if choice == "1":
            topic = input("Enter the topic studied: ")
            hours = float(input("Enter study hours: "))

            if hours > 0:
                record = {
                    "topic": topic,
                    "hours": hours,
                }

                study_records.append(record)
                print("Study session recorded successfully! ")
            else:
                print("Study hours must be greater than zero ")

        elif choice == "2":
            if not study_records:
                print("No study records available. ")
            else:
                total_hours = 0
                for record in study_records:
                    print(record["topic"], "", record["hours"], "hours")
                    total_hours += record["hours"]

                print("Total study hours:", total_hours)

        elif choice == "3":
            break

        else:
            print("Invalid choice. Try again. ")

def performance_analyzer():
    print("\nPerformance Analyzer")

    if not subjects:
        print("Please add subjects and marks first. ")
        return

    total_marks = 0
    weak_subjects = []

    for name, marks in subjects.items():
        total_marks += marks

        if marks < 40:
            weak_subjects.append(name)

    average = total_marks / len(subjects)

    print("Total subjects:", len(subjects))
    print("Average marks:", round(average, 2))

    if weak_subjects:
        print("Subjects needing improvement: ")
        for name in weak_subjects:
            print("", name)
    else:
        print("No subjects below 40 marks. ")


tasks = []


def task_manager():
    while True:
        print("\nTask manager")
        print("1. Add task ")
        print("2. View tasks ")
        print("3. Mark Task as completed ")
        print("4. Go back ")

        choice = input("Enter your choice: ")
        if choice == "1":
            task_name = input("Enter task description: ")
            task = {
                "task": task_name,
                "status": "pending",
            }
            tasks.append(task)
            print("Task added successfully! ")
        
        elif choice == "2":
            if not tasks:
                print("No tasks available.")
            else:
                print("\nTasks: ")
                for t in tasks:
                    print(t["task"], "",t["status"])

        elif choice == "3":
            if not tasks:
                print("No tasks available.")
            else:
                task_name = input("Enter the task name to mark as completed: ")
                found = False
                for t in tasks:
                        if t["task"] == task_name:
                            t["status"] = "Completed"
                            print("Task marked as completed! ")
                            found = True 
                            break
                if not found:
                    print("Task not found. ")

        elif choice == "4":
            break
        else:
            print("Invalid choice. Try again.")

def generate_report():
    print("nPerformance and Progress Report")

    print("\nSubjects: ")
    if not subjects:
        print("No subjects added. ")
    else:
        total_marks = 0
        for name, marks in subjects.items():
            print(name, ":", marks)
            total_marks += marks
        print("Average marks:", round(total_marks / len(subjects), 2))
    print("\nStudy Log: ")
    if not study_records:
        print("No study records. ")
    else:
        total_hours = 0
        for record in study_records:
            total_hours += record["hours"]
        print("Total study hours: ", total_hours)
    print("\nTasks: ")
    if not tasks:
        print("No tasks. ")
    else:
        for t in tasks:
            print(t["task"], "", t["status"])

def main():
    while True:
        print("Student study and performance tracker ")

        print("1. Subject manager ")
        print("2. Study tracker ")
        print("3. Performance Analyzer ")
        print("4. Task manager ")
        print("5. Generate report ")
        print("6. Exit ")

        choice = input("Enter your choice: ")

        if choice == "1":
            subject_manager()
        elif choice == "2":
            study_tracker()
        elif choice == "3":
            performance_analyzer()
        elif choice == "4":
            task_manager()
        elif choice == "5":
            generate_report()
        elif choice == "6":
            print("Thank you for using the tracker! ")
            break
        else:
            print("Invlaid choice. Enter a number from 1 to 6 ")

main()
    


