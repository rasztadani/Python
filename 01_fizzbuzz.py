print("Welcome to the FizzBuzz!")

while True:
    end = int(raw_input("Please give a number betwen 1 and 100: "))
    print(end)

    if end < 100:
        for num in range(1, end+1):
            if num % 3 == 0 and num % 5 == 0:
                print("FizzBuzz")
            elif num % 3 == 0:
                print("Fizz")
            elif num % 5 == 0:
                print("Buzz")
            else:
                print num
        break
    else:
        print ("The number is incorrect!")