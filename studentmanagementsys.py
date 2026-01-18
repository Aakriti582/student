class Student:
    college_name="LBEF-APU"
    block_name="D-Block"

    total_students=0
    def __init__(self,sid,sname,address,marks,age,contact):
        self.sid=sid
        self.sname=sname
        self.address=address
        self.marks=marks
        self.age=age
        self.contact=contact

        Student.total_students+=1

    #to display object clearly 
    def __str__(self):
        return(
            
        f"the student name is {self.sname}\n"
        f"the rollno is {self.sid}\n"
        f"and the address is {self.address}\n"
        f"the marks obatined is {self.marks}\n"
        f"the age of{self.sname} is {self.age}\n"
        f"and her contact is {self.contact}\n"
        f"and the college she studies is {Student.college_name}\n"
        f"her class is in {Student.block_name}"
        )
    
    def __repr__(self):
        return  ("Student '{}' , '{}', '{}', '{}' ").format(self.sname,self.address,self.age,self.marks)

    def display(self):
        print(f"the student name is {self.sname}")
        print(f"the rollno is {self.sid}")
        print(f"and the address is {self.address}")
        print(f"the marks obatined is {self.marks}")
        print(f"the age of{self.sname} is {self.age}")
        print(f"and her contact is {self.contact}")
        print(f"and the college she studies is {Student.college_name}")
        print(f"her class is in {Student.block_name}")

    #noramal classethod
    @classmethod
    def set_block_name(cls,newname):
        cls.block_name=newname

    #classmethod as alternative constructor
    @classmethod
    def from_string(cls,data_str):
        sid,sname,address,marks,age,contact=data_str.split(",")
        return cls (int(sid),sname,address,int(marks),int(age),int(contact))
    #static method to validate the contact n of student
    @staticmethod
    def valid_contact(contact):
        try:
            contact_int=int(contact)

            contact_str=str(contact)
            if len(contact_str)<=10:
                return True
            else:
                return False
        except(ValueError,TypeError):
            return False
            
   
    def is_passed(self):
        if  0<self.marks<=100:
            return f"{self.sname} you have PASSED!!"

class UGStudent(Student):
    def __init__(self,sid,sname,address,marks,age,contact,semester,course):
        super().__init__(sid,sname,address,marks,age,contact)
        self.semester=semester
        self.course=course

#method overriding
    def is_passed(self):
        if self.marks >=40:
            return f"{self.sname} you have PASSED!!!!!!"
        else:
            return f"{self.sname} you have FAILED!!! Try harder "

class PGStudent(Student):
    def __init__(self,sid,sname,address,marks,age,contact,thesis_tittle,supervisor):
        super().__init__(sid,sname,address,marks,age,contact)
        self.thesis_tittle=thesis_tittle
        self.supervisor=supervisor

#method overriding
    def is_passed(self):
        if self.marks >=40:
            return f"{self.sname} you have PASSED!!!!!!"
        else:
            return f"{self.sname} you have FAILED!!! Try harder "

#UGStudent details
ugstu=UGStudent(12,"susan","ilam",14,16,9807563421,"first-sem","Bsc-IT(cloud)")
print(ugstu.semester)
print(ugstu.course)
print()

#PGStudentdetails
pgstu=PGStudent(11,"khushi","kalanki",90,12,980765432,"history of nepal","Dr.RN Thakur")
print(pgstu.supervisor)
print(pgstu.thesis_tittle)

#normal base class student instance
s1=Student(1,"aaakriti","maitidevi", 50,19,9808754)

#creating a single  list of each 3 categories student
student_list=[s1,ugstu,pgstu]
print(student_list)
for stulist in student_list:
    print(stulist.is_passed())




s2=Student(2,"salina","ratopul",80,20,980764532)
s1.display()
Student.set_block_name("E-block")#changes the class variable block name of only salina fron D to E block
print()
s2.display()
Student.set_block_name("E-block")
print(f"the total no of students in {Student.college_name} is {Student.total_students}")
s3_str="3,Monika,baneshwor,80,31,980765432"
print()
S3=Student.from_string(s3_str)
print(S3)
s4=Student.valid_contact(98076534361)#returns False here
print(s4)