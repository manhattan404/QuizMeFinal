import os
from colorama import Fore, Back, Style
import json

# Trial Except Error if there's no Topic directory

def NavigateDirectory():

    current_directory = os.getcwdb()
    print(current_directory)
    #path = 'C:\\Users\\Gaming\\Desktop\\QuizMe\\QuizMe\\Topics'
    #change_directory = os.chdir(path)
    #print(change_directory)

    

def CreateNewTopic():

    # Create topic in subfolders
    #path = 'QuizMe\Topics'
    #os.chdir(path)
    new_topic_question = Fore.YELLOW + 'What topic would your like to create?: ' + Style.RESET_ALL
    user_named_topic = input(new_topic_question)
    os.makedirs(user_named_topic)
    topic_created_message = 'Topic named "%s" has been created!' % user_named_topic
    success_message_with_greencolor = Fore.GREEN + topic_created_message + Style.RESET_ALL
    print(success_message_with_greencolor)

NavigateDirectory()
CreateNewTopic()

   

    