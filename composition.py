class InvalidMarksError(ValueError):
    def __init__(self,marks):
        self.marks=marks

class Student:
    def __init__(self,id,name,age):
        self.id=id
        self.name=name
        self.age=age

class Result:
    def __init__(self,marks):
        self.marks=marks
        self._marks=marks

    @property
    def marks(self):
        return self._marks

    @marks.setter
    def marks(self,newmarks):
        if 0<newmarks<=100:
            self._marks=newmarks
        else:
            raise InvalidMarksError(newmarks)

    def is_passed(self):
        return self.marks>=50
        

class StudentRecord:
    def __init__(self,student,result):
        self.student=student
        self.result=result

stu=Student(1,"khushi",19)
res=Result(90)
srecord=StudentRecord(stu,res)
print(srecord.student.name)
print(srecord.result.marks)
print(srecord.result.is_passed())
