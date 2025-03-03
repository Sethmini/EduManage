from StudentDataCenter import addStudent, modifyStudent, deleteStudent, getStudentById, getStudentByName, deleteStudentClassRelationByStudent
from ScoreDataCenter import getRelationshipsByStudentId
from SubjectDataCenter import getSubjectById
from RelationshipDataCenter import getClassRelationshipsByStudentId
from ClassDataCenter import getClassRoomById



#####format for saving the student
#studentID studentname studentdob





studentIncrementor = 0
try:
    with open ("StudentFile.txt","r") as studentFile:
        data=studentFile.read()
        studentIncrementor=int((data.strip("\n").split("\n")[-1].split(" ")[0])[2:])
except (FileNotFoundError,ValueError,IndexError):
    pass
try:
    with open("RemovedStudentIdFile.txt","r") as removedIdFile:
        removedData=removedIdFile.read()
        removedDataList=removedData.strip("\n").split("\n")
        removedMax=max([int(x[2:]) for x in removedDataList])
        studentIncrementor=max(removedMax,studentIncrementor)
except (FileNotFoundError,ValueError,IndexError):
    pass






     
def add_student(command):  #[add_student, name, dob]
    "check input for errors to add a student."
    if not(command[1].isalpha()):
        print("Error. Student name should not have numbers included.")
        return;
    checkdob=command[2].split("/")
    if len(checkdob)!=3:             
        print("Error. DoB should match with DD/MM/YYYY format.")
        return;
    for check in checkdob:
        if not(check.isdigit()):
            print("Invalid syntax. Press 'help' to check the valid command list.")
            return;
    if len(checkdob[0])!=2 or len(checkdob[1])!=2 or len(checkdob[2])!=4:
        print("Error. DoB should match with DD/MM/YYYY format.")
        return;
    month=int(checkdob[1])
    day=int(checkdob[0])
    year=int(checkdob[2])
    if (month>12 or month<1):
        print("Error. Invalid DoB.")
        return;
    elif month==2:
        if year%400==0 or (year%4==0 and year%100!=0):
            if (day>29 or day<1):
                print("Error. Invalid DoB.")
                return;
        else:
            if (day>28 or day<1):
                print("Error. Invalid DoB.")
                return;
    elif month==4 or month==6 or month==9 or month==11:
        if (day>30 or day<1):
            print("Error. Invalid DoB.")
            return;
    else:
        if (day>31 or day<1):
            print("Error. Invalid DoB.")
            return;    
    global studentIncrementor
    studentIncrementor+=1
    isStored=addStudent("ST"+str(studentIncrementor),command[1],command[2]) 
    if not(isStored):
        studentIncrementor-=1
        print ("Error. This student is already in the system.")
        return;
    else:
        print("Student added.")
        print("Student ID :", "ST"+str(studentIncrementor))
        return;









def modify_student(command):   #[modify_student,id, newname, newdob]
    "check input for errors to modify a student."
    studentEntity=getStudentById(command[1]) ##[['id','name','DOB']]
    entity=getStudentByName(command[2])     ##[['id','name','DOB']]
    if command[1][0:2]!="ST" or command[1]=="ST" or not(command[1][2:].isdigit()): 
        print("Error. Invalid ID.")
        return;
    if len(studentEntity)==0:
        print("Error. The student ID does not exist in the system.")
        return;
    if not(command[2].isalpha()):
        print("Error. Student name should not have numbers included.")
        return;
    checkdob=command[3].split("/")
    if len(checkdob)!=3:             
        print("Error. DoB should match with DD/MM/YYYY format.")
        return;
    for check in checkdob:
        if not(check.isdigit()):
            print("Invalid syntax. Press 'help' to check the valid command list.")
            return;
    if len(checkdob[0])!=2 or len(checkdob[1])!=2 or len(checkdob[2])!=4:
        print("Error. DoB should match with DD/MM/YYYY format.")
        return;
    month=int(checkdob[1])
    day=int(checkdob[0])
    year=int(checkdob[2])
    if (month>12 or month<1):
        print("Error. Invalid DoB.")
        return;
    elif month==2:
        if year%400==0 or (year%4==0 and year%100!=0):
            if (day>29 or day<1):
                print("Error. Invalid DoB.")
                return;
        else:
            if (day>28 or day<1):
                print("Error. Invalid DoB.")
                return;
    elif month==4 or month==6 or month==9 or month==11:
        if (day>30 or day<1):
            print("Error. Invalid DoB.")
            return;
    else:
        if (day>31 or day<1):
            print("Error. Invalid DoB.")
            return;
    if studentEntity[0][1]==command[2] and studentEntity[0][2]==command[3]:
        print("Error. The entity you entered is already in the system.")
        return;
    if len(entity)!=0:
        for student in entity:
            if student[2]==command[3]:
                print("Error. The entity you entered already exists.")
                return; 
    isModified=modifyStudent(command[1],command[2],command[3])
    if isModified:
        print("Student modified.")
        return;
    else:
        print("Error. This student does not exist in the system yet.")







def remove_student(command):  #[remove_student, id]
    "check input for errors to remove a student."
    studentEntity=getStudentById(command[1])
    
    if command[1][0:2]!="ST" or command[1]=="ST" or not(command[1][2:].isdigit()): 
        print("Error. Invalid ID.")
        return;
    if len(studentEntity)==0: 
        print("Error. Student with this ID does not exist in the system.")
        return;
    if len(getRelationshipsByStudentId(command[1]))!=0:
        print("Cannot be deleted. Student has scores stored in the system.")
        return;
    isDeleted=deleteStudent(command[1])
    if isDeleted==True:
        print("Student removed.")
        deleteStudentClassRelationByStudent(command[1])
        return;
    else:
        print("Error. This student does not exist in the system.")









def help_student(command):  # [help_student, id]
    "show all details of the student."
    if command[1][0:2]!="ST" or command[1]=="ST" or not(command[1][2:].isdigit()): 
        print("Error. Invalid ID.")
        return;
    student=getStudentById(command[1]) #[ID NAME DOB]
    if len(student)==0:     
        print("Error. Student with this ID does not exist.")
        return;
    else:                              
        print("\n")
        print("Student ID".ljust(12)+":"+student[0][0])
        print("Student Name".ljust(12)+":"+ student[0][1])
        print("DOB".ljust(12)+":"+ student[0][2])
        print("\n")
        stuClassRelation=getClassRelationshipsByStudentId(command[1]) #[['id','studentId','classId']] 
        if len(stuClassRelation)!=0:
            Class=getClassRoomById(stuClassRelation[0][2]) #[['id','name','capacity','location']]
            print("Class".ljust(12)+":"+Class[0][1])     
        stuSubRelationList=getRelationshipsByStudentId(command[1]) #[['id','studentId','subjectId','score']]
        if len(stuSubRelationList)!=0:
            for relation in stuSubRelationList:
                subject=getSubjectById(relation[2]) #[['id','subjectName','stream']]
                print("Subject".ljust(12)+":"+subject[0][1])
                print("Score".ljust(12)+":"+relation[3])
            print("\n")
            return;
        else:
            return;


    
