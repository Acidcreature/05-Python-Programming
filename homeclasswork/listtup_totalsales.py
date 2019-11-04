"""1. Total Sales
Design a program that asks the user to enter a store’s sales for each day of the week. The
amounts should be stored in a list. Use a loop to calculate the total sales for the week and
display the result."""

def totsales():
    sales = []

    for d in range(7):
        salesin = float(input("Please enter your daily sales. "))
        sales.append(salesin)
    print(sales)
    salestotal = 0
    for s in sales:
        salestotal += float(s)
    print(salestotal)
totsales()