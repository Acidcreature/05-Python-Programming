# recursive lines
def main():
    num = int(input("Enter number: "))
    asterisk = '*'
    prast = ''
    count = 1
    printer(count, num, asterisk, prast)

def printer(count, num, asterisk, prast):
    if count > num:
        return 0
    else:
        prast += asterisk
        print(prast)
        return printer(count + 1, num, asterisk, prast)

main()