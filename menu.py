from prettytable import PrettyTable
from storedata import Questions

myTable = PrettyTable(['Reviewer'])

def showMenu():
    myTable.add_rows(
        [
            ["[A] Store questions and answers"],
            ["[B] Edit questions and answers"],
            ["[C] Take the quiz "],
            ["[D] See scores and progress"],
            ["[E] Quit"],
        ]
    )
    print(myTable)

def chooseOption():
    choice = input("Choose an option: ").lower()

    if choice == "a":
        Questions.prompt()
        Questions.enterquestion()
    elif choice == "quit":
        print("Goodbye!")
