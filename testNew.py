# Thank God for His Faithfullness
# this is my coding
class Person(object):

    def __init__(self,name):
        self.name = name
        #print name

    def __str__(self):
        return self.name

class UniMember(Person):
    def __init__(self,name):
        super(UniMember,self).__init__(name)
        self.borrowedList = []
    
    def borrow(self,book):
        self.borrowedList.append(book)

class UniStaff(UniMember):
    def __init__(self,job,name):
        super(UniStaff,self).__init__(name)
        self.job  = job
        self.taughtcourses = []


    def teaches(self,course):
        self.taughtcourses.append(course)

    def isTeaching(self,student):
        if student.__class__.__name__ != 'Student':
            return False
        
        for i in range(len(self.taughtcourses)):
            for j in range(len(student.attendedCourses)):
                if self.taughtcourses[i] == student.attendedCourses[j]:
                    return True
        return False
    
class Student(UniMember):
    def __init__(self,name,numBooks=2):
        super(Student,self).__init__(name)
        self.attendedCourses = []
        self.numBooks = numBooks

    def attends(self,course):
        self.attendedCourses.append(course)

    def borrow(self,book):
        if self.numBooks > len(self.borrowedList):
            super(Student,self).borrow(book)
        else:
            print 'error'
        """
        if len(self.borrowedList) >= self.numBooks:
            print 'error'
        else:
            super(Student,self).borrow(book)
        """    
    
thor = UniStaff("Reader","Thorsten")
pete = Student("Peter")
st   = Student("st")
pete.borrow("Python book")
pete.borrow("Java book")
pete.borrow("Logic book")
thor.teaches("g54prg")
thor.teaches("g52ifr")
pete.attends("g54prg")
pete.attends("g54swe")
st.attends("g54swe")

print str(thor)
print str(pete)
print thor.isTeaching(pete)
print thor.isTeaching(thor)

