# QUESTION 3: Use structure to display student details and also search any student details; {std_names, std_roll, std_branch}

class Student:
    def __init__(self, std_name: str, std_roll: int, std_branch: str) -> None:
        self.name = std_name
        self.roll = std_roll
        self.branch = std_branch

    def __str__(self) -> str:
        return f"Name: {self.name}, Roll Number: {self.roll}, Branch: {self.branch}"


class StudentDatabase:
    def __init__(self) -> None:
        self.student_data = list()

    @staticmethod
    def choose_branch() -> int:
        branches = [
            "Computer Science",
            "Mechanical Engineering",
            "Electrical Engineering",
            "Civil Engineering",
            "Chemical Engineering"
        ]

        print("\nChoose any branch from the following options:")
        for index, branch in enumerate(branches):
            print(f"{index+1}. {branch}")

        # while loop lets user make correct choice, if invalid number (not corresponding to any branch) is entered
        while True:
            try:
                selected_branch_num = int(input("Enter the number corresponding to the branch: "))
                if 1 <= selected_branch_num <= len(branches):
                    return branches[selected_branch_num - 1]
                else:
                    print("Invalid choice. \nSelect the number corresponding to the branch")
            except ValueError:
                print("Invalid input. Please enter a number.")

    # This function adds one student at a time
    def add_one_student(self) -> None:
        name = input("Enter student's name: ")
        roll = input("Enter student's roll number: ")
        branch = self.choose_branch()
        student = Student(name, roll, branch)
        self.student_data.append(student)
        print("Student added successfully!")

    # Function to add multiple student records at a time.
    def add_multiple_students(self) -> None:
        num_students = int(input("Enter the number of students: "))
        for _ in range(num_students):
            name = input("Enter student's name: ")
            roll = input("Enter student's roll number: ")
            branch = self.choose_branch()
            student = Student(name, roll, branch)
            self.student_data.append(student)

    # This function searches for any student record using roll number.
    def search_by_roll(self) -> None:
        try:
            roll_to_search = input("Enter roll number to search for: ")
            for stud in self.student_data:
                if stud.roll == roll_to_search:
                    print("\nStudent record found:")
                    print(stud)
                    return
            print(f"No student record found with roll number: {roll_to_search}.")
        except ValueError:
            print("Invalid input! Please enter a number")

    # This function displays all student records.
    def display_all_students(self) -> None:
        if not self.student_data:
            print("No student records are found.")
        else:
            print("\nAll Students:")
            for stud in self.student_data:
                print(stud)

    # This function shows main menu of the program
    def menu(self) -> None:
        while True:
            print("\nMenu:")
            print("1. Enter one student record")
            print("2. Enter multiple student records")
            print("3. Search student via roll number")
            print("4. Display all student records")
            print("5. Exit")
            choice = input("Enter your choice (1-5): ")

            if choice == '1':
                self.add_one_student()
            elif choice == '2':
                self.add_multiple_students()
            elif choice == '3':
                self.search_by_roll()
            elif choice == '4':
                self.display_all_students()
            elif choice == '5':
                print("Exiting the program...")
                break
            else:
                print("Invalid choice. Please select a valid option.")
                continue

            # Asking if the user wants to continue
            continue_choice = input("<Press 'y' to continue & 'n' to exit> :").strip().lower()
            if continue_choice not in ('yes', 'y'):
                print("Exiting the program...")
                break


if __name__ == "__main__":
    db = StudentDatabase()
    db.menu()
