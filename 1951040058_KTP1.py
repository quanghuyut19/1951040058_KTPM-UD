import math
import random

class HUMAN(object):

    def __init__(self, age=None , gender=None):
        if age is not None:
            self._age = age
        else: 
            self._age = random.randint(1, 160)
            random.ran
        if gender is not None:
            self._gender = gender
        else:
            self._gender = random.choice(['male', 'female'])

    @property
    def eat(self):
        pass
    
    @property
    def sleep(self):
        pass
    
    @property
    def run(self):
        pass

class STUDENT(HUMAN):

    def __init__(self, age=None , gender=None , id=None , score=None , credit=None):
        super().__init__(age, gender)
        if score is not None:
            self._score = score
        else:
            self._score = round((random.uniform(0, 4)),1)
        if credit is not None:
            self._credit = credit
        else:
            self._credit = random.randint(0, 250)
        if id is not None:
            self._id = id
        else:
            self._id = "SV_{}".format(random.randint(0, 9999))
        if age is not None:
            self._age = age
        else:
            self._age = "Student's age is{}".format(random.randint(18, 28))
        if gender is not None:
            self._gender = gender
        else:
            self._gender = "Student's gender is{}".format(random.choice(['male', 'female']))

    def result(self):
        if self._score >= 3.8 and self._score <= 4:
            return "A+"
        elif self._score >= 3.3 and self._score <= 3.5:
            return "A"
        elif self._score >= 3 and self._score <= 3.2:
            return "B+"
        elif self._score >= 2.6 and self._score <= 2.9:
            return "B"
        elif self._score >= 1.8 and self._score <= 2.5:
            return "C"
        elif self._score < 1.8:
            return "D"
    
    def graduate(result, self):
        if result != 'D' and self._credit == 250:
            return True
        else: False




        



