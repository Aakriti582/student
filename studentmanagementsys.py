class InvalidAgeError(ValueError):
    def __init__(self,age):
        self.age=age
        super().__init__(age)

class InvalidMarksError(ValueError):
    def __init__(self,marks):
        self.marks=marks
        super().__init__(marks)  

class InvalidContactError(ValueError):
    def __init__(self,contact):
        self.contact=contact
        super().__init__(contact)

class Student:
    college_name="LBEF-APU"
    block_name="D-Block"

    def __init__(self,sid,sname,address,age,marks,contact):
        self.sid=sid
        self.sname=sname
        self.address=address
        self._age=None
        self._marks=None
        self._contact=None

        self.marks=marks
        self.contact=contact
        self.age=age

    @property
    def marks(self):
        return self._marks

    @marks.setter
    def marks(self,newmarks):
        if 0<=newmarks<=100:
            self._marks=newmarks

        else:
            raise InvalidMarksError(newmarks)

    @property
    def contact(self):
        return self._contact

    @contact.setter
    def contact(self,newcontact):
            newcontact=str(newcontact)
            if len(newcontact)==10 and newcontact.isdigit():
                self._contact=newcontact
            else:
                raise InvalidContactError(newcontact)

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self,newage):
        if 10<=newage <=60:
            self._age=newage
        else:
            raise InvalidAgeError(newage)
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


    #STRETCH TASK of day 6

    def get_summary(self):
        return{
            "name":self.sname,
            "type":self.__class__.__name__,
            "passed":self.is_passed()
        }
 
    def is_passed(self):
       return self.marks >=40

try:
    stu=Student(1,"aakriti","maitidevi",111,80,9807657654)
   
except InvalidAgeError as e:
    print("Invalid age:",e)

try:
    stu=Student(2,"Khushi","ratopul",19,800,9807657654)
except InvalidMarksError as a:
    print("Invalid marks:",a)

try:
    stu=Student(2,"Khushi","ratopul",19,80,980764)
except InvalidContactError as k:
    print("Invalid contact:",k)

