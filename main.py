def for_loop():
    x = int(input("How many times should I run?"))

    for i in range(x):
        print("This loop is running for the "+ str(i+1) +" time.")


print("0. For Loop")
print("1. How are you?")
user_input = int(input("Pick an option"))

if user_input == 0:
    for_loop()
if user_input == 1:
    print("I'm good how are you?")