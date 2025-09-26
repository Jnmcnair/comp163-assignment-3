student_name = "Jonathan McNair"
current_gpa = 3.7
study_hours = 7
social_points = 30
stress_level = 30
print("Welcome,", student_name + "!")
print("Here are your starting stats:")
print("GPA:", current_gpa)
print("Study Hours:", study_hours)
print("Social Points:", social_points)
print("Stress Level:", stress_level)

print()
print("Choose your course load:")
print("A) Light (8 credits)")
print("B) Standard (10 credits)")
print("C) Heavy (12 credits)")

user_choice = input("Enter your choice: ")

if user_choice == "A":
    if current_gpa <= 2.5:
        study_hours += 7
        stress_level += 9
    else:
        study_hours += 3
        stress_level += 4
elif user_choice == "B":
    if current_gpa <= 3.0:
        study_hours += 10
        stress_level += 14
    else:
        study_hours += 8
        stress_level += 6
elif user_choice == "C":
    if current_gpa > 3.5:
        study_hours += 12
        stress_level += 20
    else:
        study_hours += 20
        stress_level += 35
else:
    print("Invalid choice. Please select A, B, or C.")
    
study_options = ["Programming", "Math", "English", "History"]
print(f"The study options are: {study_options}")
print("Chose what you want to study: ")
study_choice = input("Study decision: ")

if study_choice in study_options:
    if study_choice == "Programming":
        current_gpa += 0.3
        social_points -= 15
        print("Well done you know what a print statement is")
    elif study_choice == "Math":
        current_gpa += 0.4
        social_points -= 20
        print("congrats you know how to add 2 and 2 together")
    elif study_choice == "English" and current_gpa >= 3.0:
        social_points += 12
        print("congrats you can read this")
    elif study_choice == "History" or (study_choice == "English" and current_gpa < 3.0):
        current_gpa += 0.2
        social_points += 8
        print("congrats you know what happened 5 minutes ago")
    elif study_choice not in study_options:
        print("Invalid")

    
