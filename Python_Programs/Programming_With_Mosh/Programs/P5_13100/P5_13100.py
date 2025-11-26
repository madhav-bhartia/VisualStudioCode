def car():
    print('Type "help" to get started!')
    while True:
        cmd = input("-> ").lower()
        started = False

        if cmd == "help":
            print("Here are the accepted commands and what they do")
            print("Start - Start the car!")
            print("Stop - Stop the car!")
            print("Quit - To exit")
        elif cmd == "start":
            if started:
                print("A ghost!: U good bro? Need some help! (XD)")
                print("Progarm: <-> Get Uno reverse card! Idiot.")
                print("Thought i was dum but as it turns out u are!")
            else:
                print("Car started...")
                print("Ready to go!")
                started = True
        elif cmd == "stop":
            if not started:
                print("A ghost!: U good bro? Need some help! (XD)")
                print("Progarm: <-> Get Uno reverse card! Idiot.")
                print("Thought i was dum but as it turns out u are!")
            else:
                print("Car stopped.")
                started = False
        elif cmd == "quit":
            break
        else:
            print("I don't understand that!")
            print('Type "help" to get started')


car()

# YEESSSSSS!!! Did everything correctly on the first try!
# In the solution found out about a improved way to use
# ".lower()" command.
# Found out how to use "while loops without using any conditions!"
