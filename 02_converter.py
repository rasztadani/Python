print("Dear user!")

mile = 0.62
convert = 0
operation = 1

while operation:

    convert = float(raw_input("Enter kilometer: "))
    print convert * mile

    while True:
        operation = str(raw_input("yes/no: "))

        if operation == "yes":
            print("Ok. let's go!")
            break

        elif operation == "no":
            print("Ok. Bye")
            break
        else:
            print("Not yes or no!!!")
    if operation == "no":
        break