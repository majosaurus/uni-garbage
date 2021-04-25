class Robot:
    """Represents a robot, with a name."""

    # A class variable, counting the number of robots
    #
    # There is a leading underscore to mark that the class variable
    # called _population should not be accessed directly from outside this class:
    _population = 0

    def __init__(self, name, languages):
        """Initializes the data."""

        # There are two leading underscores here to mark that the
        # object variable __name should not be accessed directly from
        # outside this object:
        self.__name = name

        if languages < 0:
            self.__languages = 0
        else:
            self.__languages = languages

        print("(Initializing {})".format(self.__name))
        
        # When this person is created, the robot
        # adds to the population
        Robot._population += 1


    def die(self):
        """I am dying."""

        print("{} is being destroyed!".format(self.__name))
        Robot._population -= 1

        if Robot._population == 0:
            print("{} was the last one.".format(self.__name))
        else:
            print("There are still {:d} robots working.".format(Robot._population))


    def say_hi(self):
        """Greeting by the robot.

        Yeah, they can do that."""

        if self.__languages == 0:
            print("Blip, blip, blop, {}".format(self.__name))
        
        else:
            print("Greetings, my masters call me {} and I speak {} languages.".format(self.__name, self.__languages))


    def learn_languages(self, how_many_new):
        """Robots can learn new languages."""

        if how_many_new <= 0 and self.__languages != 0:
            print("I do not know how to learn {} number of languages.".format(how_many_new))
            print("I still speak {} languages.".format(self.__languages))
        
        elif self.__languages == 0:
            print("Blip, blip, blop, {}".format(self.__name))
        
        else:
            self.__languages += how_many_new
            print("Learning {} new languages...".format(how_many_new))
            print("Now I can speak {} languages in total.".format(self.__languages))

    
    def forget_languages(self, how_many_forget):
        """Robots forget languages from time to time"""

        if how_many_forget <= 0 and self.__languages != 0:
            print("I do not know how to learn {} number of languages.".format(how_many_forget))
            print("I still speak {} languages.".format(self.__languages))
        
        elif how_many_forget >= self.__languages or self.__languages == 0:
            print("Blip, blip, blop, {}".format(self.__name))

        else:
            self.__languages -= how_many_forget
            print("Forgetting {} languages...".format(how_many_forget))
            print("Now I can speak {} languages in total.".format(self.__languages))


    @classmethod
    def how_many(cls):
        """Prints the current population."""
        print("We have {:d} robots.".format(cls._population))


def main():
    # Main program that creates and kills robots

    droid1 = Robot("R2-D2", 3)
    droid1.say_hi()
    droid1.learn_languages(4)
    droid1.forget_languages(3)
    Robot.how_many()
    print()

    droid2 = Robot("C-3PO", 5)
    droid2.say_hi()
    droid2.learn_languages(1)
    droid2.forget_languages(6)
    Robot.how_many()
    print()

    droid3 = Robot("Welding", 2)
    droid3.say_hi()
    droid3.learn_languages(-1)
    droid3.forget_languages(5)
    Robot.how_many()
    print()

    droid4 = Robot("Dumb", -7)
    droid4.say_hi()
    droid4.learn_languages(0)
    droid4.forget_languages(0)
    Robot.how_many()

    print("\nRobots can do some work here.\n")

    print("Robots have finished their work. So let's destroy them.")
    droid1.die()
    droid2.die()
    droid3.die()
    droid4.die()
    
    Robot.how_many()


main() # Call main program
