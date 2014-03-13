from types import MethodType
class Student(object):

    __slots__ = ('name', 'score', 'age', 'hobby')
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print '%s: %s' % (self.name, self.score)

class UniversityStudent(Student):

    __slots__ = ('name', 'sex', 'age', '_age')
    def print_sex(self):
        print '%s: %s' % (self.name, self.sex)
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self, value):
        if not isinstance(value, int):
            raise ValueError('age must be a int value')
        elif value < 0 or value > 100:
            raise ValueError('age must be between 0 and 100')
        else:
            self._age = value

lily = UniversityStudent('Lily', '96')
lily.sex = 'female'
lily.print_sex()
lily.age = 102
lily.hobby = 'basket_ball'
print lily.hobby
print lily.age, lily._age, dir(lily)

jim = Student('Jim', 98)
lucy = Student('Lucy', 99)

jim.print_score()
lucy.print_score()

def set_score(self, score):
    self.score = score

jim.set_score = MethodType(set_score, jim, Student)
jim.set_score(100)
jim.print_score()

lucy.age = 18
lucy.sex = 'female'

