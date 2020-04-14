# L1-Capstone1-Finance_Calculators

**The financial calculator enables a user to do 2 types of calculations:**
- Calculate the final value of their investment based on the deposit amount, investement period and preferred interest rate and type.
- Calculate monthly bond repayments based on present value of the property, payment period and interest rate.

**How the code works**
- The user is prompted to enter the type of calculation they would like to do (investment or bond).
- The code makes use of an If-elif-else statement.
- The user input to select the type of calculation is changed to lowercase so that the inpur workes in the If statement regardless of how it was typed by the user.
*The first condition:* If the user chooses "investment" they are prompted for the following in order to do the calculation: initial investment amount, interest rate, number of years to invest and interest type (compund or simple)
- If the interest type is compound and all user input has been received, the function for compund interest from the Python math module is called.
- Else if the interest type is simple and all user input has been received, the function for simple interest from the Python math module is called.
*The second condition:* If the user selects "bond" they are prompted for the for the following in order to do the calculation: present value of the house, repayment period, annual interest rate.
- Once all the user input has been received, the function for bond calculation from Python Math module is called.

