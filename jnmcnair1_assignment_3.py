#Ai was used in line 61 and 64 to help with the logical and membership operators and making sure the elif statements made sense but rest of logic is developed inderpendently
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
        
graduation = input("Do you want to graduate? (yes/no): ")
#AI was used here to help with understanding is and is not statements and used for minor debugging help with nested if/else statements      
if type(graduation) is str and graduation is not None:
    if current_gpa >= 3.5:
        if stress_level < 40:
            ending = "You graduate with honors and a little bit of stress"
        else:
            ending = "You graduate with honors, but you need therapy"
    elif current_gpa >= 2.0:
        if social_points >= 50 and study_hours > 20:
            ending = "You graduate successfully with some good time management skills"
        elif social_points < 20 or stress_level > 70:
            ending = "You barely graduate and I dont blame you, take some time off champ"
        else:
            ending = "You graduate now have fun"
    else:
        if stress_level > 80:
            ending = "You get so cooked by stress you drop out"
        else:
            ending = "Your GPA was too low you couldnt graduate"
    
    print("End of the game")
    print(ending)
    print()
    print("Final Stats:")
    print("Student Name:", student_name)
    print("GPA:", current_gpa)
    print("Study Hours:", study_hours)
    print("Social Points:", social_points)
    print("Stress Level:", stress_level)

else:
    print("Invalid input for graduation decision.")