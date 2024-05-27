# program.py
def main():
    while True:
        print("\nMain Menu")
        print("1. Greet")
        print("2. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            greet()
        elif choice == '2':
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")

def greet():
    print("Hello, User!")

if __name__ == "__main__":
    main()
