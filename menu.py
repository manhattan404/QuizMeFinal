from prettytable import PrettyTable

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