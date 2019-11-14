# Employee and ProductionWorker Classes

class Employee:
    # The __init__ method accepts an argument for
    # the Employee 
    def __init__(self, name, empnum):
        self.__name = name
        self.__empnum = empnum
    
    # The following methods are mutators for the
    # class's data attributes

    def set_name(self, name):
        self.__name = name

    def set_empnum(self, empnum):
        self.__empnum = empnum
    
    # The following methods are the accessors for the
    # class's data attributes

    def get_name(self):
        return self.__name
    
    def get_empnum(self):
        return self.__empnum

class ProWork(Employee):
    # The __init__ method accepts arguments for the 
    # employee's shift number and hourly pay rate
    def __init__(self, name, empnum, shift, payrate):
        # Call the superclass's __init__ and pass the
        # required arguments. Note we also need to pass 'self'
        Employee.__init__(self, name, empnum)

        # Initialize __shift and __payrate attribs
        self.__shift = shift
        self.__payrate = payrate

    # The following methods are mutators for the
    # class's data attributes

    def set_shift(self, shift):
        self.__shift = shift

    def set_payrate(self, payrate):
        self.__payrate = payrate

    # The following methods are the accessors for the
    # class's data attributes

    def get_shift(self):
        return self.__shift
    
    def get_payrate(self):
        return self.__payrate

class ShiftSuper(Employee):
    # The __init__ method accepts arguments for the
    # ShiftSupervisors salary and bonus
    def __init__(self, name, empnum, salary, bonus):
        # Call the superclass's __init__ and pass the
        # required arguments. Note we also need to pass 'self'
        Employee.__init__(self, name, empnum)

        # Initialize __salary and __bonus attribs
        self.__salary = salary
        self.__bonus = bonus

    # The following methods are mutators for the
    # class's data attributes

    def set_salaryt(self, salary):
        self.__salary = salary

    def set_bonus(self, bonus):
        self.__bonus = bonus

    # The following methods are the accessors for the
    # class's data attributes

    def get_salary(self):
        return self.__salary
    
    def get_bonus(self):
        return self.__bonus