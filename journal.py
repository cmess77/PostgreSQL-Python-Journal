menu = """Please select one of the following options:
1) Add new entry for today.
2) View entries.
3) Exit.

Your Selection: """
welcome = "Welcome to the programming diary!"

print(welcome)

while (user_input := input(menu)) != "3":  # used := "walrus" operator here
    # deal with user input here

    if user_input == "1":
        print("Adding...")
    elif user_input == "2":
        print("Viewing")
    else:
        print("Invalid option, please try again.")
