from dbaseLogic import createTable, addEntry, getEntries


menu = """Please select one of the following options:
1) Add new entry for today.
2) View entries.
3) Exit.

Your Selection: """
welcome = "Welcome to the programming diary!"


def promptNewEntry():
    entry_content = input("What have you learned today? ")
    entry_date = input("Enter the date: ")

    addEntry(entry_content, entry_date)


def viewEntries(entries):
    for entry in entries:
        print(f"{entry['date']}\n{entry['content']}\n\n")


def main():
    print(welcome)
    createTable()

    # menu options
    while (user_input := input(menu)) != "3":  # used := "walrus" operator here
        if user_input == "1":
            promptNewEntry()
        elif user_input == "2":
            viewEntries(getEntries())
        else:
            print("Invalid option, please try again.")


if __name__ == "__main__":
    main()
