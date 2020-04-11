import math

# Ask user to choose investment or bond calculator

user_input = input("Which calculation would you like to do? Enter investment or bond: ")
# Change possible inputs ('BOND', 'Bond', 'bond'; 'INVESTMENT', 'Investment', 'investment') to lowercase
calculator = user_input.lower()

#if-elif-else statements: If user inputs "investment", proceed with calculation; else if user inputs "Investment", proceed with calculation; else if user enters "INVESTMENT", proceed with calculation; else print error message

# if-elif-else statements: investment or bond; simple or compound interest

# If user chooses investment,ask user to input the following: P = principal amount or initial investment amount; r = interest rate; t = time period for investment; interest type (simple or compound)

if calculator == "investment":
    P = float(input("Enter the initial investment amount in rands: "))
    IR = float(input("Enter the interest rate %: "))
    t = float(input("Enter the number of years you would like to invest for: "))
    interest = input("Please select simple or compound interest: ")
    r = IR/100
    if interest == "simple":
        A = P*(1+r*t)
        print("The future value of your investment will be" + " " + str(A))
    elif interest == "compound":
            A = P*math.pow(1+r,t)
            print("The future value of your investment will be" + " " + str(A))
            
# Else if user chooses bond, ask user to input the following: P = principal value of the house; n = number of months over which bond will be repaid; R= annual interest rate

elif calculator == "bond":
    P = float(input("What is the present value of the house? (Enter amount in rands): "))
    n = float(input("Over how many months will the bond be repaid?? "))
    R = float(input("What is the annual interest rate? %: "))
    i = R/12
    x = (i*P)/(1-(1+i)**(-n))
    print("The monthly bond repayment will be" + " " + str(x))
# Else statement (If user input is not 'BOND', 'Bond', 'bond'; or 'INVESTMENT', 'Investment', 'investment', print error message)
else:
    print("Error: That is not a valid input. Enter investment or bond.")

