# The Sandwhich class

class Sandwhich:
    def __init__(self, crisp, flavor, bread, juiciness):
        # The __init__ method accepts arguments for
        # the  Sandwhich.
        self.__crisp = crisp
        self.__flavor = flavor
        self.__bread = bread
        self.__juiciness = juiciness

        # The following methods are mutators for the
        # class's data attributes

        def set_crisp(self, crisp):
            self.__crisp = crisp

        def set_flavor(self, flavor):
            self.__flavor = flavor

        def set_bread(self, bread):
            self.__bread = bread

        def set_juiciness(self, juiciness):
            self.__juiciness = juiciness

        # The following methods are the accessors for the
        # class's data attributes

        def get_crisp(self):
            return self.__crisp

        def get_flavor(self):
            return self.__flavor

        def get_bread(self):
            return self.__bread

        def get_juiciness(self):
            return self.__juiciness


class Person:
    # The __init__ method accepts an argument for the
    # person
    def __init__(self, name):

        # The following method is a mutator for the
        # class's data attribute

        def set_name(self, name):
            self.__name = name
    
        # The following method is the accessor for the
        # class's data attrib
    
        def get_name(self):
            return self.__name

class Instructor(Person):
    # The __init__ method accepts arguments for the
    # instructors authority
    def __init__(self, name, authority):
        # Call superclass __init__ and pass the 
        # required arguments. Note, need to pass self
        Person.__init__(self, name)

        # initialize __authority
        self.__authority = authority

        # The following method is a mutator for the
        # class data attrib
        def set_authority(self, authority):
            self.__authority = authority

        # The following method is the accessor for the
        # class's data attribute
        def get_authority(self):
            return self.__authority

class Student(Person):
    # The __init__ method accepts arguments for the
    # students priviledge.
    def __init__(self, name, priviledge):
        # Call the superclass's __init__ and pass the
        # required arguments. Note, pass self also.
        Person.__init__(self, name)

        # Initialize __priviledge
        self.__priviledge = priviledge

        # The following method is a mutator
        def set_privilede(self, priviledge):
            self.__priviledge = priviledge

        # the following method is an accessor
        def get_priviledge(self):
            return self.__priviledge
