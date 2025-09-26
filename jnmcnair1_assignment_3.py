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
    

