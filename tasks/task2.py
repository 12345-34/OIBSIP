def calculate_bmi(weight, height):
    """Calculate BMI and return BMI value and category."""
    bmi = weight / (height ** 2)

    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi < 24.9:
        category = "Normal weight"
    elif 25 <= bmi < 29.9:
        category = "Overweight"
    else:
        category = "Obese"

    return bmi, category


def main():
    """Main function to get user input and display BMI result."""
    try:
        weight = float(input("Enter your weight in kg: "))
        height = float(input("Enter your height in meters: "))

        if weight <= 0 or height <= 0:
            print("❌ Weight and height must be positive numbers!")
            return
        
        bmi, category = calculate_bmi(weight, height)

        print("\n📊 BMI Calculator Result:")
        print(f"🔹 Your BMI: {bmi:.2f}")
        print(f"🔹 Category: {category}")

    except ValueError:
        print("❌ Invalid input! Please enter numbers for weight and height.")


if __name__ == "__main__":
    main()
