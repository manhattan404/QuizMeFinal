from storedata import AskAndStore

type_question = input("Enter a question: ")
type_answer = input("Ennter the answer: ")

trial = AskAndStore(type_question, type_answer)

print(trial.question)

