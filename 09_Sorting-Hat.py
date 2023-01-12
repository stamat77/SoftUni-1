command = input()
sorting_successful = True

while not command == "Welcome!":
    if command == "Voldemort":
        print("You must not speak of that name!")
        sorting_successful = False
        break

    length = len(command)

    if length < 5:
        print(f"{command} goes to Gryffindor.")
    elif length == 5:
        print(f"{command} goes to Slytherin.")
    elif length == 6:
        print(f"{command} goes to Ravenclaw.")
    elif length > 6:
        print(f"{command} goes to Hufflepuff.")

    command = input()

if sorting_successful:
    print("Welcome to Hogwarts.")
