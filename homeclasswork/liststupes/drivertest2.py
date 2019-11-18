

def drivetest():

    ANSWERS = ["B","D","A","A","C","A","B","A","C","D","B","C","D","A","D","C","C","B","D","A"]
    finalgrade = get_test()
    correct = 0
    wrong = 0
    for g in range(len(ANSWERS)):
        if finalgrade[g] == ANSWERS[g]:
            correct += 1
        else:
            wrong += 1
    if correct <= 14:
        print(f" You got {wrong} answers wrong. You failed.")
    else:
        print(f"You got {correct}, You Passed!")
    
def get_test():
    grade = []
    file = input("file name? ")
    f = open(file, 'r')
    #read that file 
    line = f.readline()
    linecount = 0
    while line != '' and linecount <= 20:
        grade.append(line.strip('\n'))
        linecount += 1
        line = f.readline()
    #close file
    f.close()
    #print(grade)
    return grade

drivetest()