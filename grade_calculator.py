def calculate_grade(marks):
    """Function to determine grade and message based on marks."""
    if marks >= 90:
        return "A", "Outstanding! You're Gr8! 🌟"
    elif marks >= 80:
        return "B", "Very Good! Keep it up! 👍"
    elif marks >= 70:
        return "C", "Gr8 job! With a bit more effort, you'll reach the top! 📈"
    elif marks >= 60:
        return "D", "You passed! Now work harder for the next one. 📚"
    else:
        return "F", "Never give up! Prepare again and try again. 💪"

def main():
    print("--- 🎯 Student Grade Calculator ---")
    name = input("Enter student name: ")

    # While loop for inp validation
    while True:
        try:
            marks = float(input("Enter marks (0-100): "))
            if 0 <= marks <= 100:
                break # Exit loop if inp is valid
            else:
                print("❌ Invalid input. Please enter a number between 0 and 100.")
        except ValueError:
            print("❌ Invalid input. Please enter a numeric value.")

    # Get results from function
    grade, message = calculate_grade(marks)

    # Final Output
    print(f"\n📊 RESULT FOR {name.upper()}:")
    print(f"Marks: {marks}/100")
    print(f"Grade: {grade}")
    print(f"Message: {message}")

if __name__ == "__main__":
    main()