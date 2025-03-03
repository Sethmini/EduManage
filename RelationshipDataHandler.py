from RelationshipDataCenter import addTeacherClass, addStudentClass, getClassRelationshipsByTeacherId, getClassRelationshipsByStudentId, getStudentRelationshipsByClassId
from TeacherDataCenter import getTeacherById
from ClassDataCenter import getClassRoomById
from StudentDataCenter import getStudentById



teacherClassIncrementor = 0
try:
    with open("TeacherClassFile.txt","r") as teacherClassFile:
        teacherClassIncrementor = int(teacherClassFile.readlines()[-1][0])
except (FileNotFoundError,ValueError,IndexError):
    pass 
try:
    with open("RemovedTeacherClassIdFile.txt","r") as removedTeacherClassIdFile:
        removedData = removedTeacherClassIdFile.read()
        removedDataList = removedData.strip("\n").split("\n")
        removedMax = max([int(x[0]) for x in removedDataList])
        teacherClassIncrementor = max(removedMax,teacherClassIncrementor)
except (FileNotFoundError,ValueError,IndexError):
    pass




studentClassIncrementor = 0
try:
    with open("StudentClassFile.txt","r") as studentClassFile:
        studentClassIncrementor = int(studentClassFile.readlines()[-1][0])
except (FileNotFoundError,ValueError,IndexError):
    pass 
try:
    with open("RemovedStudentClassIdFile.txt","r") as removedStudentClassIdFile:
        removedData = removedStudentClassIdFile.read()
        removedDataList = removedData.strip("\n").split("\n")
        removedMax = max([int(x[0]) for x in removedDataList])
        studentClassIncrementor = max(removedMax,studentClassIncrementor)
except (FileNotFoundError,ValueError,IndexError):
    pass




#FUNCTIONS




def handleAddTeacherClass(teacherId, classId):
    "Errors."
    if (teacherId[0:2]!='TC') or (not teacherId[2::].isdigit()):
        print("Error. The teacher ID that you have entered is invalid.")
    elif (classId[0:2]!='CR') or (not classId[2::].isdigit()): 
        print("Error. The class ID that you have entered is invalid.")
    elif getTeacherById(teacherId)==None:
        print("Error. This teacher does not exist.")
    elif len(getClassRoomById(classId))==0:
        print("Error. This class does not exist.")
    else:
        global teacherClassIncrementor
        teacherClassIncrementor += 1
        isSuccess = addTeacherClass(teacherClassIncrementor, teacherId, classId)
        if isSuccess:
            print("The teacher has been assigned to the class.")
        else:
            teacherClassIncrementor -=1
            print("Error. A relationship with this teacher or class already exists.")






def handleAddStudentClass(studentId, classId):
    "Errors."
    if (studentId[0:2]!='ST') or (not studentId[2::].isdigit()):
        print("Error. The student ID that you have entered is invalid.")
    elif (classId[0:2]!='CR') or (not classId[2::].isdigit()): 
        print("Error. The class ID that you have entered is invalid.")
    elif len(getStudentById(studentId))==0:
        print("Error. This student does not exist.")
    elif len(getClassRoomById(classId))==0:
        print("Error. This class does not exist.")
    else:
        global studentClassIncrementor
        studentClassIncrementor += 1
        classEntity = getClassRoomById(classId) #[[classId,className,capacity,location]]
        isSuccess = addStudentClass(studentClassIncrementor, studentId, classId, classEntity[0][2])
        if isSuccess==True:
            print("The student has been assigned to the class.")
        elif isSuccess=='exceeds_capacity':
            print("Error. The maximum number of students that can be assigned to this class room is reached.")
        else:
            studentClassIncrementor -= 1
            print("Error. This student already has a class.")




            
            

def handleShowTeacherStudents(teacherId):
    "show the students assigned to the teacher."
    teacherEntity = getTeacherById(teacherId)
    teacherClassEntity = getClassRelationshipsByTeacherId(teacherId) #[['id','teacherId','classId']]  
    if (teacherId[0:2]!='TC') or (not teacherId[2::].isdigit()):
        print("Error. The teacher ID that you have entered is invalid.")
    elif teacherEntity==None:
        print("Error. This teacher does not exist.")
    elif len(teacherClassEntity)==0:
        print("Error. This teacher has not been assigned to a class yet.")
    elif len(getStudentRelationshipsByClassId(teacherClassEntity[0][2]))==0:
        print("Error. Students have not been assigned to this teacher yet.")
    else:
        studentClassEntities = getStudentRelationshipsByClassId(teacherClassEntity[0][2])
        print("\nTeacher: "+teacherEntity[1]+"\nStudents: ")
        for relationship in studentClassEntities:
            studentEntity = getStudentById(relationship[1]) #[studentId,name,DoB] 
            print("\t"+(studentEntity[0][0]).ljust(7)+" - "+(studentEntity[0][1]).ljust(15))
        print("\n")




        



def handleShowClassStudents(classId):
    "show the student in the class"
    if (classId[0:2]!='CR') or (not classId[2::].isdigit()):
        print("Error. The class ID that you have entered is invalid.")
    elif len(getClassRoomById(classId))==0:
        print("Error. This class does not exist.")
    elif len(getStudentRelationshipsByClassId(classId))==0:
        print("Error. Students have not been assigned to this class yet.")
    else:
        classEntity = getClassRoomById(classId) #[id,name,capacity,location]
        studentClassEntities = getStudentRelationshipsByClassId(classId) #[['id','studentId','classId']] 
        print("\nClass: "+classEntity[0][1]+"\nStudents: ")
        for relationship in studentClassEntities:
            studentEntity = getStudentById(relationship[1]) #[studentId,name,DoB] 
            print("\t"+(studentEntity[0][0]).ljust(7)+" - "+(studentEntity[0][1]).ljust(15))
        print("\n")



        
