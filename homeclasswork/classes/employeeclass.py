#The Employee Class

class Employee:
    # The __init__ method initializes the attributes
    def __init__(self, name, ID, dep, job):
        self.__name = name
        self.__ID = ID
        self.__dep = dep
        self.__job = job

    # The get_name method returns the name
    def get_name(self):
        return self.__name

    # The get_ID method returns the ID
    def get_ID(self):
        return self.__ID

    # The get_dep method returns the dep
    def get_dep(self):
        return self.__dep

    # The get_job method returns the job
    def get_job(self):
        return self.__job