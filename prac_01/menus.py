name = input("Enter your name:")
print("(H)ello"
      "(G)oodbye"
      "(Q)uit")
choice = input("Please enter your choice(H,G or Q?)")
while choice != "Q":
    if choice == "H":
        message = "Hello,", name
    elif choice == "G":
        message = "Goodbye,", name
    else:
        message = "Invalid message"
    print(message)
    print("(H)ello"
          "(G)oodbye"
          "(Q)uit")
    choice = input("Please enter your choice again (H,G or Q?)")

print("finished message")
