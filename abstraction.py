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
    

class DiplomaResultPolicy(ResultPolicy):
    def is_passed(self,marks):
        return marks>=35

class PhDResultPolicy(ResultPolicy):
    def is_passed(self,marks):
        return marks>=60

class Student:
    def __init__(self,id,name,age):
        self.id=id
        self.name=name
        self.age=age


#composition here because result  has a resultpolicy
class Result:
    def __init__(self,marks:int,policy:ResultPolicy):
        self.marks=marks
        self._marks=marks
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

stu=Student(1,"aakriti",19)
res=Result(50,UGResultPolicy())
print(res.is_passed())
print()
stu1=Student(2,"khushi",10)
res1=Result(40,PGResultPolicy())
print(res1.is_passed())
print()
diplomastu=Student(3,"richha",11)
res2=Result(35,DiplomaResultPolicy())
print(res2.is_passed())
print()
phdstu=Student(4,"susan",10)
res3=Result(20,PhDResultPolicy())
print(res3.is_passed())





        




