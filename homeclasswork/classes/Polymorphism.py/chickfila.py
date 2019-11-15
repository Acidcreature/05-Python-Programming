# The Chik fil a program

import random
import chikfilaclass as chik
import pprint

def main():
    role = 0
    authority = 100 
    priviledge = 0
    individuals = []
    party = int(input("How many participants? "))
    count = 0
    # Create objects
    while count < party:
        name = input("Enter the name ")
        role = input("Enter 0 for Instructor or 1 for Student ")
        if role == 0:
            instruct = chik.Instructor(name, authority)
            individuals.append(instruct)
        else:
            stud = chik.Student(name, priviledge)
            individuals.append(stud)
        count += 1
    print(individuals)
main()