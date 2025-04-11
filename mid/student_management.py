class StudentDatabase:
    def __init__(self):
        self.student_list = []
    
    def add_student(self, student):
        self.student_list.append(student)


class Student:
    def __init__(self, student_id:str, name, department):
        self.__student_id = student_id.upper()
        self.__name = name
        self.__department = department
        self.__is_enrolled = False
    
    def enroll_student(self):
        if self.__is_enrolled:
            print(f"Student {self.__student_id}:{self.__name} is already enrolled.!!")
            return
        
        self.__is_enrolled = True
        print(f"Student {self.__student_id}:{self.__name} has been enrolled.")
    
    def drop_student(self):
        if not self.__is_enrolled:
            print(f"Student {self.__student_id}:{self.__name} is not yet enrolled.!!")
            return
        
        self.__is_enrolled = False
        print(f"Student {self.__student_id}:{self.__name} has been dropped.")
    
    def view_student_info(self):
        print(f"ID: {self.__student_id}, Name: {self.__name}, Department: {self.__department}, Enrolled: {self.__is_enrolled}")

    @property
    def id(self):
        return self.__student_id


db = StudentDatabase()
db.add_student(Student("S101", "Alice Smith", "Computer Science"))
db.add_student(Student("S102", "Bob Johnson", "Mathematics"))
db.add_student(Student("S103", "Charlie Lee", "Physics"))



while 1:
    print("""
-- Student Management System --
1. View All Student
2. Enroll Student
3. Drop Student
4. Exit
""")
    choise = input("Enter your choise (1-4): ")
    try:
        choise = int(choise)
    except Exception:
        print("Wrong input type")
        continue

    if choise>4 or choise<1:
        print("Invalid option choisen. Choise between (1-4)")
        continue


    if choise==1:
        for i in db.student_list:
            i.view_student_info()
    
    elif choise==2:
        student_id = input("Enter Student Id to Enroll: ").upper()
        
        done = False
        for student in db.student_list:
            if student.id == student_id:
                student.enroll_student()
                done = True
        if not done:
            print("Provided Student id is not found in the database")
    
    elif choise==3:
        student_id = input("Enter Student Id to Drop: ").upper()
        
        done = False
        for student in db.student_list:
            if student.id == student_id:
                student.drop_student()
                done = True
        if not done:
            print("Provided Student id is not found in the database")

    elif choise==4:
        break