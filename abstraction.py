from abc import ABC, abstractmethod

class InvalidMarksError(ValueError):
    def __init__(self,marks):
        self.marks=marks


class ResultPolicy(ABC):

    @abstractmethod
    def is_passed(self,marks:int) ->bool:
        pass
        

class UGResultPolicy(ResultPolicy):

    def is_passed(self,marks):
        return marks>=40

class PGResultPolicy(ResultPolicy):

    def is_passed(self,marks):
        return marks>=50
    
class Student:
    def __init__(self,id,name,age):
        self.id=id
        self.name=name
        self.age=age

#composition here because result  has a resultpolicy
class Result:
    def __init__(self,marks:int,policy:ResultPolicy):
        self.marks=marksss        self._marks=marks
        self.policy=policy#Composition happens here

    def is_passed(self):
        return self.policy.is_passed(self.marks)

    @property
    def marks(self):
        return self._marks

    @marks.setter
    def marks(self,newmarks):
        if 0<=newmarks<=100:
            self._marks=newmarks
        else:
            raise InvalidMarksError(newmarks)

ugstudent=Student(1,"aakriti",19)
ugresult=Result(50, UGResultPolicy())
pgstudent=Student(2,"Khushi",18)
pgresult=Result(40,PGResultPolicy())
print(ugstudent.name)
print(ugresult.is_passed())
print()
print(pgstudent.name)
print(pgresult.is_passed())

