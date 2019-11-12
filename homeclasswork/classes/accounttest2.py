# This program demonstrates the BankAccount class
import bankaccountclass

def main():
    # Get starting balance
    start_bal = float(input('Enter your starting balance: '))

    # Create BankAccount object
    savings = bankaccountclass.BankAccount(start_bal)

    # Deposit the users paycheck
    pay = float(input('How much were you paid this week? '))
    print('I will deposit this into your account. ')
    savings.deposit(pay)

    #Display the balance
    print(savings)

    #Get the amount to withdraw
    cash = float(input('How much would you like to withdraw? '))
    savings.withdraw(cash)

    #display the balance
    print(savings)

#call the main function
main()