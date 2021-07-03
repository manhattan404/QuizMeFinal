import os

def NavigateDirectory():

    cwd = os.getcwd()
    print(cwd)
    os.chdir("C:\\Users\\Gaming\\Desktop\\QuizMe\\QuizMe\\Topics")
    new_cwd = os.getcwdb()
    print(new_cwd)
