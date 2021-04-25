CURRENT_YEAR = 2020

class SchoolMember:
    '''Represents any school member.'''

    def __init__(self, name, year_of_birth):
        ''' Create a new school member '''

        # Double underscore in self.__name and self.__age means that these variables
        # are unaccessible outside this object, even in the subclasses Teacher and Student:
        self.__name = name
        self.__year_of_birth = year_of_birth
        print('(Initialized SchoolMember: {})'.format(self.__name))

    def get_name(self):
        ''' This getter method makes it possible to ask for the name of this
        object from outside. This is needed since the variable __name itself is unaccessible. '''
        return self.__name

    def get_year_of_birth(self):
        return self.__year_of_birth

    def get_age(self):
        return (CURRENT_YEAR - self.get_year_of_birth())

    def tell(self):
        '''Tell my details.'''
        print('Name:"{}" Age:"{}"'.format(self.__name, self.get_age()), end=" ")
        
        
class Teacher(SchoolMember):
    ''' Represents a teacher. '''

    def __init__(self, name, year_of_birth, salary):
        SchoolMember.__init__(self, name, year_of_birth)
        self.__salary = salary
        print('(Initialized Teacher: {})'.format(self.get_name()))
    
    def get_year_of_retirement(self):
        if self.get_year_of_birth() < 1965:
            return self.get_year_of_birth() + 65
        else:
            return self.get_year_of_birth() + 68

    def tell(self):
        SchoolMember.tell(self)
        print('Year of Retirement: "{:d}" Salary: "{:d}"'.format(self.get_year_of_retirement(), self.__salary), end=" ")


class ClassTeacher(Teacher):
    """Represents a teacher teaching a class"""

    def __init__(self, name, year_of_birth, salary, which_class):
        Teacher.__init__(self, name, year_of_birth, salary)
        self.__which_class = which_class
    
    def tell(self):
        Teacher.tell(self)
        print('Class: "{}"'.format(self.__which_class))


class SubTeacher(Teacher):
    """Represents a teacher teaching a subject"""

    def __init__(self, name, year_of_birth, salary, subject):
        Teacher.__init__(self, name, year_of_birth, salary)
        self.__subject = subject

    def tell(self):
        Teacher.tell(self)
        print('Subject: "{}"'.format(self.__subject))


class Student(SchoolMember):
    ''' Represents a student. '''

    def __init__(self, name, year_of_birth, marks):
        SchoolMember.__init__(self, name, year_of_birth)
        self.__marks = marks
        print('(Initialized Student: {})'.format(self.get_name()))
        
    def get_year_of_graduation(self):
        return self.get_year_of_birth() + 19

    def tell(self):
        SchoolMember.tell(self)
        print('Marks: "{:d}", Year of Graduation: "{:d}"'.format(self.__marks, self.get_year_of_graduation()))
        

def main():

    t = ClassTeacher('Mrs. Shrividya', 1968, 30000, '3A')
    t1 = SubTeacher('Mr. Watercress', 1964, 2000, 'English')
    s = Student('Swaroop', 1725, 75)
        
    # prints a blank line
    print()

    members = [t, t1, s]
    for member in members:
        # Works for both Teachers and Students
        member.tell()

main() # Call main program
