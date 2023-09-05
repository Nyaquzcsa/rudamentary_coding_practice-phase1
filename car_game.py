#car game using while loops
command = ""

game_help = input("Help needed: ")
if game_help == "yes":
    print("start: Start the car;  "
          "stop: stops the car;  "
          "quit: quits the game")



while command != "quit":
    command = input(">")
    if command == "start":
        print("car has started moving")
    if command == "stop":
        print("Car has stopped")
    elif command == "quit":
        print("quitting game")


