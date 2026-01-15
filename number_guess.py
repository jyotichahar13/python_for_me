def get_input (n:int):
    try:
        user_input=int(input(f"Guess a number from 1 to {n} "))
    except ValueError:
        print("Please enter a number")
    else:
        if user_input <1 or user_input >10:
            print("Please enter correct number")
        else:
            return user_input


def main ():
    user_input= get_input(100) 
    upper=100
    lower=0

    guessed_num : int =int(upper/2)
    while True:
        
        if guessed_num==user_input:
            print(f"Your number is {guessed_num}")
            break
        print (f"Upper: {upper} Lower: {lower}, guess: {guessed_num}")

        result=input(f"Is your number greater than {guessed_num} y/n")
        
        if result=='y':
            lower=guessed_num
            guessed_num=int((lower+upper)/2)
        else:
            upper=guessed_num
            guessed_num=int((lower+upper)/2)

main()



