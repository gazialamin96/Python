
help = '''
    Start - To start the car
    Stop - To Stop the car
    quit - To exit the Game
'''

command = "";
started = False
stopped = False
while True:
    command = input('> ').lower()
    if command == "help":
        print(help)
    elif command == "start":
        if started:
            print("car is already started")
        else:
            started = True
            print("car started!")
    elif command == "stop":
        if stopped:
            print('car is already stopped!')
            break
        else:
            stopped = True
            print("Car Stopped!")
            break
    elif command == "quit":
        break
    else:
        print("Input is not valid! Please input the valid one")
