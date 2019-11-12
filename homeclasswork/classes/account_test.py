# This program demonstrates the BankAccount class
import bankaccountclass

def main():
    # GEt starting balance
    start_bal = float(input('Enter your starting balance: '))

    # Create BankAccount object
    savings = bankaccountclass.BankAccount(start_bal)

    # Deposit the users paycheck
    pay = float(input('How much were you paid this week? '))
    print('I will deposit this into your account. ')
    savings.deposit(pay)

    #Display the balance
    print(f'Your balance is ${savings.get_balance():,.2f}')

    #Get the amount to withdraw
    cash = float(input('How much would you like to withdraw? '))
    savings.withdraw(cash)

    #display the balance
    print(f'Your balance is ${savings.get_balance():,.2f}')

#call the main function
main()