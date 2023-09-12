import random

def generateNumber():
    randomNum = random.randint(1,100)

    print("Random Number: ", randomNum)
    return randomNum

def isEven(number):
    #check if the number is even
    return number % 2 == 0

def looping():
    while True:
        userInput = int(input("enter a number"))

def loopCondition(number):
    while True:
        userInput = int(input("enter a number: "))
        if userInput == number:
            print("Exiting loop")
            break 
        else:
            print(f"you typed: {userInput}")




def main():
    #number = generateNumber()
    index = 0

    #if isEven(generateNumber()):
    #    print(f"{generateNumber()} is even")
    #else:
    #    print(f"{generateNumber()} is odd")

    #if isEven(number):
    #    print(f"{number} is even")
    #else:
    #    print(f"{number} is odd")

    while True:
        #generateNumber()
        #number = generateNumber()
        #number = random.randint(1,100)
        #print(number)
        while index != 5:
            number = random.randint(1,100)
            print(number)
            print(index)
            userInput = int(input("Enter a number: "))
            if userInput == number:
                print("congrats!")
                break
            else:
                print("Wrong number")
                if userInput > number:
                    print("guess is greater than the winning number")
                elif userInput < number:
                    print("guess is less then the winning number")
            index = index + 1
            
        if index == 5:
            print("lost the game. Try again?")
    
        word = input("Do you want to try again? Press y/n: ")
        if word == 'n':
            return False
        else:
            index = 0
        





    #loopCondition(12)


if __name__ == "__main__":
    main()