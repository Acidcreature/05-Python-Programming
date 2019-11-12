# Def Superhero class

class SuperHero:

    def __init__(self, heroname, realname, powers, color):
        self.__h = heroname
        self.__r = realname
        self.__p = powers
        self.__c = color 

    def set_realname(self, realname):
        self.__r = realname

    def set_powers(self, powers):
        self.__p = powers

    def set_heroname(self, heroname):
        self.__h = heroname

    def set_color(self, color):
        self.__c = color

    def get_heroname(self):
        return self.__h
    
    def get_color(self):
        return self.__c
    
    def get_realname(self):
        return self.__r

    def get_powers(self):
        return self.__p