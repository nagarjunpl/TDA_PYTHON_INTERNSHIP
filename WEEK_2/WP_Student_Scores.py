class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def display(self):
        print(f"{self.name}: {self.score}")


class StudentManager:
    def __init__(self):
        self.students = []   # list to store Student objects

    def add_student(self, name, score):
        student = Student(name, score)
        self.students.append(student)
        print(f"Added {name} with score {score}")

    def display_all(self):
        print("\n--- Student Scores ---")
        for student in self.students:
            student.display()


# Main program
def main():
    manager = StudentManager()

    # Adding students
    manager.add_student("Alice", 85)
    manager.add_student("Bob", 92)
    manager.add_student("Charlie", 78)

    # Display all students
    manager.display_all()


# Run the program
main()
