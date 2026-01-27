class InvalidMarksError(ValueError):
    def __init__(self,marks):
        self.marks=marks

class UGResultPolicy:
    def is_passed(self,marks):
        return marks>=50

class PGResultPolicy:
    def is_passed(self,marks):
        return marks>=40

class Student:
    def __init__(self,id,name,age):
        self.id=id
        self.name=name
        self.age=age

   
class Result:
    def __init__(self,marks,policy):
        self._marks=marks
        self.policy=policy

    @property
    def marks(self):
        return self._marks

    @marks.setter
    def marks(self,newmarks):
        if 0<self.newmarks<100:
            self._marks=newmarks
        else:
            raise InvalidMarksError(newmarks)

    def is_passed(self):
        result= self.policy.is_passed(self.marks)
        if not isinstance(result,bool):
            raise TypeError("Result Policy must return Boolean")
        return result

    # def check_result(self):
    #     return self.is_passed()



ugres=Result(50,UGResultPolicy())
print(ugres.is_passed())
print()
pgres=Result(30,PGResultPolicy())
print(pgres.is_passed())