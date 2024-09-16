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


def printvars():
    print ("Here is the value of a few different variables: ")
    print (somestring)
    print (someint)
    print (somefloat)
    print (someboolean)

def somerandomcalculatororsomethingidek():
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
    print("Hello " + username + "!")

def debuglogorsmth():
    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
    with open("Logs/logs.txt", "a") as file:
        file.write("hello.py was run at: " + formatted_time + "\n")

if __name__ == '__main__':
    filename = "AGB.txt"
    debuglogorsmth()
    try:
        if not os.path.isfile(filename):
            print(f"Error: {filename} WAS DELETED, HOW DARE THOU?? ")
            sys.exit(1)
        else:
            hello()
            printvars()
            somerandomcalculatororsomethingidek()
            schedule.every().day.at("03:00").do(run_hello) # Call the run_hello function every night at 3:00
            while True:
                schedule.run_pending()
                time.sleep(1)
    except Exception as e:
        print(e)