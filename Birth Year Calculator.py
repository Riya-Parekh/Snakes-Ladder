def calculate_birth_year():
    while True:
        try:
            current_year = int(input("Enter the current year (e.g., 2023): "))
            age = int(input("Enter your age: "))
            
            if age < 0:
                print("Age cannot be negative. Please enter a valid age.")
                continue
            
            # Calculate the birth year
            birth_year = current_year - age
            
            if birth_year > current_year:
                print("It seems you've entered an age that results in a future birth year. Please check your inputs.")
            else:
                print(f"You were born in the year: {birth_year}")
            break  # Exit the loop if everything is valid
        except ValueError:
            print("Invalid input. Please enter numeric values.")

# Run the function
calculate_birth_year()
