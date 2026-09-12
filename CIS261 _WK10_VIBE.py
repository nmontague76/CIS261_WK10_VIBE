#NICKIE MONTAGUE
#CIS261
#WK10 VIBE CODING

"""Student Grade Calculator.

This program uses Option A: a list of dictionaries for student records.
"""

FILE_NAME = "student_grades.txt"


def calculate_average(test1, test2, test3):
    """Return the average of three test scores."""
    return (test1 + test2 + test3) / 3


def calculate_grade(average):
    """Return a letter grade based on an average score."""
    if average >= 90:
        return "A"
    if average >= 80:
        return "B"
    if average >= 70:
        return "C"
    if average >= 60:
        return "D"
    return "F"


def create_student(name, student_id, test1, test2, test3):
    """Build a student dictionary with calculated values."""
    average = calculate_average(test1, test2, test3)

    return {
        "name": name,
        "id": student_id,
        "test1": test1,
        "test2": test2,
        "test3": test3,
        "average": average,
        "grade": calculate_grade(average),
    }


def get_score(test_number):
    """Prompt until a valid score from 0 through 100 is entered."""
    while True:
        try:
            score = float(input(f"Test {test_number} score (0-100): "))

            if 0 <= score <= 100:
                return score

            print("Please enter a score from 0 through 100.")

        except ValueError:
            print("Please enter a valid number.")


def add_student(students):
    """Prompt for and add one student record."""
    print("\nADD NEW STUDENT")

    name = input("Enter student name: ").strip()

    while not name:
        print("Student name cannot be blank.")
        name = input("Enter student name: ").strip()

    student_id = input("Enter Student ID: ").strip()

    while not student_id:
        print("Student ID cannot be blank.")
        student_id = input("Enter Student ID: ").strip()

    test1 = get_score(1)
    test2 = get_score(2)
    test3 = get_score(3)

    student = create_student(
        name,
        student_id,
        test1,
        test2,
        test3
    )

    students.append(student)

    print(
        f"\nAdded student: {student['name']} "
        f"(ID: {student['id']})"
    )

    print(
        f"Average: {student['average']:.2f} | "
        f"Grade: {student['grade']}"
    )


def display_students(students):
    """Display all student records in a formatted table."""
    if not students:
        print("\nNo student records found.")
        return

    print("\nALL STUDENT RECORDS")

    print("-" * 92)

    print(
        f"{'Name':<22}"
        f"{'ID':<14}"
        f"{'Test 1':>10}"
        f"{'Test 2':>10}"
        f"{'Test 3':>10}"
        f"{'Average':>12}"
        f"{'Grade':>8}"
    )

    print("-" * 92)

    for student in students:
        print(
            f"{student['name']:<22.22}"
            f"{student['id']:<14.14}"
            f"{student['test1']:>10.2f}"
            f"{student['test2']:>10.2f}"
            f"{student['test3']:>10.2f}"
            f"{student['average']:>12.2f}"
            f"{student['grade']:>8}"
        )

    print("-" * 92)

    print(f"Total students: {len(students)}")


def search_student(students):
    """Search for a student by name."""
    if not students:
        print("\nNo student records available.")
        return

    print("\nSEARCH STUDENT")

    search_text = input(
        "Enter student name to search: "
    ).strip().lower()

    matches = [
        student
        for student in students
        if search_text in student["name"].lower()
    ]

    if not matches:
        print(
            f"No student found with name: {search_text}"
        )
        return

    for student in matches:
        print("\nFound student:")

        print(f"Name: {student['name']}")
        print(f"ID: {student['id']}")
        print(f"Test 1: {student['test1']:.2f}")
        print(f"Test 2: {student['test2']:.2f}")
        print(f"Test 3: {student['test3']:.2f}")
        print(f"Average: {student['average']:.2f}")
        print(f"Grade: {student['grade']}")


def display_statistics(students):
    """Display class statistics."""
    if not students:
        print(
            "\nNo student records available for statistics."
        )
        return

    highest = max(
        students,
        key=lambda student: student["average"]
    )

    lowest = min(
        students,
        key=lambda student: student["average"]
    )

    class_average = (
        sum(
            student["average"]
            for student in students
        )
        / len(students)
    )

    print("\nCLASS STATISTICS")

    print(
        f"Class Average: {class_average:.2f}"
    )

    print(
        f"Highest Average: "
        f"{highest['average']:.2f} "
        f"({highest['name']})"
    )

    print(
        f"Lowest Average: "
        f"{lowest['average']:.2f} "
        f"({lowest['name']})"
    )


def save_students(students, file_name=FILE_NAME):
    """Save student records using pipe-delimited format."""
    try:
        with open(
            file_name,
            "w",
            encoding="utf-8"
        ) as file:

            for student in students:
                file.write(
                    f"{student['name']}|"
                    f"{student['id']}|"
                    f"{student['test1']:.2f}|"
                    f"{student['test2']:.2f}|"
                    f"{student['test3']:.2f}|"
                    f"{student['average']:.2f}|"
                    f"{student['grade']}\n"
                )

        print("\nSaving records...")

        print(
            f"Saved {len(students)} student "
            f"record(s) to file."
        )

    except OSError as error:
        print(
            f"Unable to save student records: "
            f"{error}"
        )


def load_students(file_name=FILE_NAME):
    """Load student records from file."""
    students = []

    try:
        with open(
            file_name,
            "r",
            encoding="utf-8"
        ) as file:

            for line_number, line in enumerate(
                file,
                start=1
            ):

                fields = line.rstrip("\n").split("|")

                if len(fields) != 7:
                    print(
                        f"Skipped malformed record "
                        f"on line {line_number}."
                    )
                    continue

                try:
                    test1 = float(fields[2])
                    test2 = float(fields[3])
                    test3 = float(fields[4])

                    student = create_student(
                        fields[0],
                        fields[1],
                        test1,
                        test2,
                        test3
                    )

                    students.append(student)

                except ValueError:
                    print(
                        f"Skipped invalid scores "
                        f"on line {line_number}."
                    )

    except FileNotFoundError:
        print(
            "No existing student file found. "
            "Starting with an empty list."
        )

    except OSError as error:
        print(
            f"Unable to load student records: "
            f"{error}"
        )

    return students


def show_menu():
    """Display the main menu."""
    print("\n" + "=" * 58)

    print("STUDENT GRADE CALCULATOR")

    print("=" * 58)

    print("1. Add New Student")
    print("2. Display All Students")
    print("3. Search Student by Name")
    print("4. View Class Statistics")
    print("5. Save and Exit (or press ESC)")

    print("=" * 58)

    return input(
        "Select an option (1-5) or press ESC to exit: "
    )


def main():
    """Run the Student Grade Calculator."""
    students = load_students()

    while True:

        choice = show_menu()

        if choice == "\x1b":
            save_students(students)

            print(
                "Thank you for using "
                "Student Grade Calculator!"
            )

            break

        elif choice == "1":
            add_student(students)

        elif choice == "2":
            display_students(students)

        elif choice == "3":
            search_student(students)

        elif choice == "4":
            display_statistics(students)

        elif choice == "5":
            save_students(students)

            print(
                "Thank you for using "
                "Student Grade Calculator!"
            )

            break

        else:
            print(
                "Invalid choice. "
                "Select 1-5 or press ESC to exit."
            )


if __name__ == "__main__":
    main()