import random

#This is a simplified version of my take on the guessing game
#everything is done within the main section of the code
#in this version I make use of a nested while loop to keep the game 
#running after the initial game is over

#The first while loop will keep going until the loop returns 
#a value of False to end the loop
#The second loop will go until the index variable reaches the value
# of five

#For testing purposes, the game will print out the winning number
#generated by randint
#You can turn off this feature by commenting out print(number)
#on line 25
def main():
    index = 0

    while True:
        number = random.randint(1,100)

        while index != 5:
            #number = random.randint(1,100)
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
                    print("guess is less than the winning number")
            index = index + 1

        if index == 5:
            print("lost the game. Try again?")

        word = input("Do you want to try again? Press y/n: ")
        if word == 'n':
            return False
        else:
            index = 0

if __name__ == "__main__":
    main()