from abc import   abstractstaticmethod

class Iperson:

    def __init__(self) -> None:
        pass


    @abstractstaticmethod
    def person_method():
        """ Interface method """


class Student(Iperson):

    def __init__(self) -> None:
        self.name = "Basic student name"

    def person_method(self):
        print("I am a studnet")

class Teacher(Iperson):

    def __init__(self) -> None:
        self.name = 'Basic Teacher name'

    def person_method(self):
        print('I am a Teacher')          


class PersonFactory:
    @staticmethod
    def build_person(person_type):
        if person_type == "student":
            Student()
        if person_type == 'teacher':
            return Teacher()
        print("Invalid Type")
        return -1 


if __name__ ==  "__main__":
    
    choice = input('what type of person do you want to create?\n')
    person = PersonFactory.build_person(choice)
    person.person_method()

    # s1 = Student()
    # s1.person_method()

    # t1 = Teacher()
    # t1.person_method()