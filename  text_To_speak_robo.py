import os
if __name__ == '__main__':
    print ("Welcome to Robo Speaskes ")
    while True:
        message = input ("Enter what you want to speak : ")
        if message == "q":
            os.system ("Say 'Bye Bye friend '")
            break
        command = f"say {message}"
        os.system(command)