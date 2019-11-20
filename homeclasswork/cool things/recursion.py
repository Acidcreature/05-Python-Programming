# endless recursion

def forever_recursion(times):
    annoying_message(times)

def annoying_message(times):
    if times > 0:
        print("Test test1 test2")
        annoying_message(times -1)
forever_recursion(5)
