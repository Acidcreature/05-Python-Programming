# recursive multiply
def main():
    num1 = int(input("Number 1: "))
    num2 = int(input("Number 2: "))
    total = 0
    count = 1
    calcd(count, num1, num2, total)
    
def calcd(count, num1, num2, total):
    if count > num1:
        return 0
    else:
        total += num2 
        print(total)
        return calcd(count +1 , num1, num2, total)

    
main()


