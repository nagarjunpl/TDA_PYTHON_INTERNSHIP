FILE_NAME = "contacts.txt"

while True:
    print("\n--- Contact Book ---")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Name: ")
        phone = input("Phone: ")
        with open(FILE_NAME, "a") as file:
            file.write(f"{name} - {phone}\n")
        print(" Contact saved!")

    elif choice == "2":
        try:
            with open(FILE_NAME, "r") as file:
                print("\n Contacts:")
                print(file.read())
        except FileNotFoundError:
            print(" No contacts found.")

    elif choice == "3":
        print(" Goodbye!")
        break
    else:
        print(" Invalid choice, try again.")
