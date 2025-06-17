command = input("give Command: ")
match command:
    case "Hi":
        print("Hi,Welcome to AIML")
    case "Hello":
        print("Hey,Welcome to AIML")
    case "Bye":
        print("Bye, Thank you for visiting")
    case Default:
        print("Invalid Command")