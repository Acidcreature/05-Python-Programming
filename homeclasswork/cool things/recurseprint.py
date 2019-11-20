# This program demonstrates the recursive printing program

def main():
    num = int(input("Stupid " ))
    start = 1
    stupid(start, num)
def stupid(start, num):
    if start == num +1:
        return 0
    else:
        print(start)
        return stupid(start + 1, num)
main()
    