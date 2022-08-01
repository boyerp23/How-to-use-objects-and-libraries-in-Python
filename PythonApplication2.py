#File creator: Paul Boyer
#pauboyer@uat.edu
#CSC235 Python Programming 1
#WK 2 assignment 1

#pip installed library
import pyjokes

libs = [pyjokes]
class Program():
    #defining an intializer
    def __init__(self):
        #print statement
        print("*** WELCOME TO MY JOKE TELLING MACHINE ***\n" ,\
            "The jokes are related to programming ",\
            "and can be humorous to those that understand.\n" ,\
            "Feel free to engage in some good fun!")
        # list of program libraries
        self.program_libs = []
        #initialize the object
        for l in libs:
            #print string l in libs where it is installed and located on the system
            print(str(l))
            #print statement
            print("Do you want to hear a joke?")
            #ask for user input
            print("Enter \'y\' for yes")
            #get user input
            usr_in = input()
            #if user input equals yes program will execute and display a joke, otherwise program will end.
            #Upper is added so that upper and lower case is used 
            if str(usr_in).upper() == "y".upper():
                #append method is used to add items to collection types
                self.program_libs.append(l)
    #getter method - keyy needs two whys because it needs to be explicite
    def get_lib(self, keyy:int):
        return self.program_libs[keyy]

myNewProgram = Program()
joke_list = pyjokes.get_joke()
#dictionary
myDict ={}
i = 0
for jokeI in joke_list:
    myDict[i] = jokeI
    i += 1
print(pyjokes.get_joke())
#commented out code - was causing program to print each character to a new line 
'''for k, v in myDict.items():
    print(k, v)'''
#loop in order to play more jokes up tp 100 before exiting program
for i in range(100):
        #ask for user input
        print("Would you like to hear another joke?" ,\
            "Enter \'y\' to continue",\
            "Enter \'n\' to exit\n")
        #get user input
        usr_in = input()
        if str(usr_in).upper() == 'y'.upper():
                print(pyjokes.get_joke())
        #if user is finished they may select no to exit and loop breaks
        if str(usr_in).upper() == 'n'.upper():
            print("Thanks for playing!")
            break
#print statement of location of library on system
print(myNewProgram.get_lib(0))
 
    