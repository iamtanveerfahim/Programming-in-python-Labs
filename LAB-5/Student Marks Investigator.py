students = [
    [201, "Amina", [78, 85, 90]],
    [202, "Rahim", [65, 70, 68]],
    [203, "Nadia", [92, 88, 95]],
    [204, "Hasan", [55, 60, 65]],
    [205, "Tania", [80, 80, 80]]
]


# Task 1: Calculate average marks
def calculate_average(marks):
    if len(marks) == 0:
        return 0

    total = 0

    for mark in marks:
        if mark < 0 or mark > 100:
            print("Invalid mark:", mark)
            return None

        total = total + mark

    average = total / len(marks)
    return average


# Task 2: Classify performance
def classify_performance(average):
    if average is None:
        return "Invalid Marks"
    elif average >= 80:
        return "Excellent"
    elif average >= 70:
        return "Good"
    elif average >= 60:
        return "Satisfactory"
    else:
        return "Needs Improvement"


# Task 3: Display student report
def display_report(students):
    if len(students) == 0:
        print("No student records available.")
        return

    print("\nStudent Performance Report")
    print("-----------------------------------------------")

    for student in students:
        student_id = student[0]
        name = student[1]
        marks = student[2]

        average = calculate_average(marks)
        performance = classify_performance(average)

        if average is not None:
            print("ID:", student_id)
            print("Name:", name)
            print("Average:", round(average, 2))
            print("Performance:", performance)
            print("-----------------------------------------------")
        else:
            print("ID:", student_id)
            print("Name:", name)
            print("Performance:", performance)
            print("-----------------------------------------------")


# Function call
display_report(students)
