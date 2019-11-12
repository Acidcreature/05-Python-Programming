import superhero as s

def main():
    color = input("Please enter a color. ")
    heroname = input("Please choose your hero name: ")
    powers = input('test')
    realname = input('test1')
    
    #print(f"""You are the {color} {heroname}. Your super power 
#is {powers} and {realname} is your secret identity.""")
    hero = s.SuperHero(color, heroname, powers, realname)

    print(hero.get_color())
    print(hero.get_heroname())
    print(hero.get_realname())
    print(hero.get_powers())
main()