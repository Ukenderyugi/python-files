def check_age_category(age):
    if age < 18:
        return "You are a minor"
    elif age < 65:
        return "You are an adult"
    else:
        return "You are a senior"

# Ask the user to enter their age
age = int(input("Enter your age: "))

# Check the age category and print the corresponding message
category = check_age_category(age)
print(category)
