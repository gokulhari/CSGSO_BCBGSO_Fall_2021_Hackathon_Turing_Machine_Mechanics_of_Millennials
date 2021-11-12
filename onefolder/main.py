import os
import

def correctSentences(parsedSentences):
    print('The parsed sentences is: ')
    print(parsedSentences)

    correct = input("Are the sentences correct? type 1 for yes and 0 for no ")

    while correct != '1' and correct != '0':
        print("invalid argument try again:")
        correct = input("Are the sentences correct? type 1 for yes and 0 for no ")

    if int(correct) == 0:
        osCommandString = "notepad.exe file.txt"
        os.system(osCommandString)
        print("Go ahead and edit this file and save it. Press yes when you're done")
        done = input("Are you done yet? press 1 for yes and 0 for no ")
        while done != '0' and done != '1':
            print("invalid argument try again:")
            done = input("Are you done yet? press 1 for yes and 0 for no ")
    return


correctSentences(output)

def lstm_to_prep(text):
    """Passed text and converts this into prepositional logic"""  

def correctPrepositional():
    correct = input("Is this logic correct? type 1 for yes and 0 for no ")
    #TODO: Print propositional logic that was just converted.

    while correct != '1' and correct != '0':
        print("invalid argument try again:")
        correct = input("Is this logic correct? type 1 for yes and 0 for no ")
    if int(correct) == 0:
        #assuming we are working with windows
        osCommandString = "notepad.exe file.txt"
        os.system(osCommandString)
        print("Go ahead and edit this file and save it. Press yes when you're done")
        done = input("Are you done yet? press 1 for yes and 0 for no ")
        while done != '0' and done != '1':
            print("invalid argument try again:")
            done = input("Are you done yet? press 1 for yes and 0 for no ")


correctPrepositional()
