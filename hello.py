import datetime
import schedule
import time
import subprocess
import os
import sys

username = input("What is your name, oh esteemed user of this script? ")


# Here we have a few types of variables, e.g. strings, integers, booleans and floats.
somestring = "hello" # string (obvs)
someint = 22 # integer (obvs)
somefloat = 22.2 # float (obvs)
someboolean = True # boolean (even more obv)

def run_hello():
    subprocess.run(["python", "hello.py"]) # Function which will run "hello.py" (this file) in a subprocess


def printvars(): # Here we're printing the values of all these different data types into the console (For demonstration I guess? Would be kind of pointless to have variables and not use them)
    print ("Here is the value of a few different variables: ")
    print (somestring)
    print (someint)
    print (somefloat)
    print (someboolean)

def somerandomcalculatororsomethingidek(): # Quite self-explanatory, it just a function which adds the value of our float to the value of our integer
    print("Now we will do some basic maths with the integer and the float! ")
    result = someint + somefloat
    print("The result of 22 + 22.2 is: ")
    print (result)

'''
And this is some kind of multi-line comment.
Hello!!
Still a comment!

def hello():
    print ("Hello!")

HAHA got you, still just a comment :3
'''

def hello():
    print("Hello " + username + "!") # This just says hello to the user ¯\_(ツ)_/¯

def debuglogorsmth(): # Creates an entry into a logfile whenever this script is run, which would make it easier to pinpoint the time of failure
    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
    with open("Logs/logs.txt", "a") as file:
        file.write("hello.py was run at: " + formatted_time + "\n")

if __name__ == '__main__': # Define what functions we wish to call when executing this script. (Mostly made for compilation into an EXE so that the EXE headers don't kill themselves)
    filename = "AGB.txt" # We define the file path of our Terms of Service (AGB) here
    debuglogorsmth() # We call the Debug Function which will create an entry into the logfile
    try: 
        if not os.path.isfile(filename):
            print(f"Error: {filename} WAS DELETED, HOW DARE THOU?? ") # Here we probe to see if our ToS-File is still there
            sys.exit(1) # If if isn't, the script will exit without further ado.
        else: # If the ToS-File is still here, the script continues
            hello() # Calls the function to greet the user
            printvars() # Calls the function which prints the contents of our variables
            somerandomcalculatororsomethingidek() # Calls the "calculating" function
            schedule.every().day.at("03:00").do(run_hello) # Call the run_hello function every night at 3:00
            while True:
                schedule.run_pending() # This is the scheduler which executes this script every night at 3 am
                time.sleep(1)
    except Exception as e: # Catches potential errors and prints them into the console
        print(e)