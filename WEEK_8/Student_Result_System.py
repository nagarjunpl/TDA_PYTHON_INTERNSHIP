import csv

students = []

def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    else:
        return "Fail"

def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    subjects = ["Math", "Science", "English"]  # you can expand
    
    marks = {}
    total = 0
    for subject in subjects:
        score = int(input(f"Enter marks for {subject}: "))
        marks[subject] = score
        total += score
    
    percentage = total / len(subjects)
    grade = calculate_grade(percentage)
    
    student = {
        "roll": roll,
        "name": name,
        "marks": marks,
        "total": total,
        "percentage": percentage,
        "grade": grade
    }
    
    students.append(student)
    print(f"\n✅ Student {name} added successfully!\n")

def view_student():
    roll = input("Enter Roll Number to search: ")
    for student in students:
        if student["roll"] == roll:
            print("\n📊 Student Result:")
            print(f"Roll: {student['roll']}")
            print(f"Name: {student['name']}")
            print(f"Marks: {student['marks']}")
            print(f"Total: {student['total']}")
            print(f"Percentage: {student['percentage']:.2f}")
            print(f"Grade: {student['grade']}")
            return
    print("❌ Student not found!")

def view_all():
    print("\nAll Students Results:")
    for student in students:
        print(f"{student['roll']} | {student['name']} | Total: {student['total']} | %: {student['percentage']:.2f} | Grade: {student['grade']}")

def save_to_csv():
    with open("students.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Roll", "Name", "Marks", "Total", "Percentage", "Grade"])
        for student in students:
            writer.writerow([student["roll"], student["name"], student["marks"], student["total"], student["percentage"], student["grade"]])
    print("\n💾 Data saved to students.csv")

def load_from_csv():
    try:
        with open("students.csv", "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                students.append({
                    "roll": row["Roll"],
                    "name": row["Name"],
                    "marks": eval(row["Marks"]),  # careful, in real projects use json instead
                    "total": float(row["Total"]),
                    "percentage": float(row["Percentage"]),
                    "grade": row["Grade"]
                })
        print("📂 Data loaded from students.csv")
    except FileNotFoundError:
        print("⚠️ No existing data found. Starting fresh.")

# ---------------- Menu ----------------
def menu():
    load_from_csv()
    while True:
        print("\n===== Student Result System =====")
        print("1. Add Student")
        print("2. View Student by Roll No")
        print("3. View All Students")
        print("4. Save & Exit")
        
        choice = input("Enter choice: ")
        
        if choice == "1":
            add_student()
        elif choice == "2":
            view_student()
        elif choice == "3":
            view_all()
        elif choice == "4":
            save_to_csv()
            print("👋 Exiting... Goodbye!")
            break
        else:
            print("❌ Invalid choice! Try again.")

menu()
