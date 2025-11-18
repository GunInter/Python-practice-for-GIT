promtp = ""
start = False
stop = False

while True:

    promtp = input("> ").lower()

    if promtp == "help":

        print("start - to start the car")
        print("stop - to stop the car")
        print("quit - to exit")

    elif promtp == "start":

        if start:
            print("Car is already started!")
        else:
            start = True
            print("Car started ready to go...")

    elif promtp == "stop":
        if not start:
            print("Car is already stopped!!")
        else:
            start = False
            print("Car stopped.......not movingggg")

    elif promtp == "quit":
        break

    else:
        print("Sorry,I dont understabd this")
