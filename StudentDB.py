while True:
    name = ["Emma Jones", "Connor Johnson", "Steph Smith", "Robert Brown", "Emanuel Watts"]
    hometown = ["Grand Rapids", "Waterford", "Flint", "Fenton", "Detroit"]
    favorite_food = ["Chocolate", "Pizza", "Tacos", "Salad", "Pasta"]

    num = int(input("Which student would you like to learn about? Enter a number 1-5: "))
    student = num - 1
    if student not in range(0, len(name)):
        print("Sorry, that student does not exist. Please enter a number 1-5")
        continue
    else:
        print(f"Student {student + 1} is {name[student]}. What would you like to know?")
        while True:
            student_info = input("Enter \"hometown\" or \"favorite food\": ")
            if student_info == "hometown":
                print(f"{name[student]} is from {hometown[student]}")
                break
            elif student_info == "favorite food":
                print(f"{name[student]}'s favorite food is {favorite_food[student]}")
                break
            else:
                print("That category doesn't exist. Please enter either \"hometown\" or \"favorite food\": ")

    while True:
        learn_more = input("Would you like to learn about another student? Enter \"y\" or \"n\": ")
        if learn_more == "y":
            continue
        elif learn_more == "n":
            print("Have a nice day!")
            break
        else:
            print("Enter either \"y\" or \"n\"")
