import datetime

username = input("What is your name, oh esteemed user of this script? ")

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
    except Exception as e:
        print(e)