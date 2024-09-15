import datetime

username = input("What is your name, oh esteemed user of this script? ")

# Here we have a few types of variables, e.g. strings, integers, booleans and floats.
somestring = "hello" # string (obvs)
someint = 22 # integer (obvs)
somefloat = 22.2 # float (obvs)
someboolean = True # boolean (even more obv)


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

HAHA got you, still just a comment :3
'''

def hello():
    print("Hello " + username + "!")

def debuglogorsmth():
    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
    with open("C:/Users/ramon/Documents/GitHub/RandomKackScript/Logs/logs.txt", "a") as file:
        file.write(formatted_time + "\n")

if __name__ == '__main__':
    debuglogorsmth()
    try:
        hello()
        printvars()
        somerandomcalculatororsomethingidek()
    except Exception as e:
        print(e)