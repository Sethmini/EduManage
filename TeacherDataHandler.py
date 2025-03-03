from TeacherDataCenter import addTeacher, modifyTeacher, deleteTeacher, getTeacherById, deleteTeacherClassRelationByTeacher
from RelationshipDataCenter import getClassRelationshipsByTeacherId
from SubjectDataCenter import getSubjectById
from ClassDataCenter import getClassRoomById


#####format for saving the student
#teacherID teachername subIdlist teacherdob stream


teacherIncrementor = 0
try:
    with open ("TeacherFile.txt","r") as teacherFile:
        data=teacherFile.read()
        teacherIncrementor=int((data.strip("\n").split("\n")[-1].split(" ")[0])[2:])
except (FileNotFoundError,ValueError,IndexError):
    pass
try:    
    with open ("RemovedTeacherIdFile.txt","r") as removedIdFile:
        removedData=removedIdFile.read()
        removedDataList=removedData.strip("\n").split("\n")
        removedMax=max([int(x[2:]) for x in removedDataList])
        teacherIncrementor=max(removedMax,teacherIncrementor)
except (FileNotFoundError,ValueError,IndexError):
    pass






def add_teacher(command):  #[add_teacher, name , subject id list, dob, stream]
    "check input for errors to add a teacher."
    if not(command[1].isalpha()):
        print("Error. Teacher name should not have numbers included.")
        return;
    if not (command[4]=="A/L" or command[4]=="O/L"):
        print("Error. The stream should be either A/L or O/L.")
        return;
    subIdList=command[2].split(",")
    for subId in subIdList:
        if subIdList.count(subId)>1:
            print("Error. The subject IDs are repeated.")
            return;
        if subId[0:2]!="SB" or subId=="SB" or not(subId[2:].isdigit()):
            print("Error. Invalid ID.")
            return;
        subject=getSubjectById(subId)
        if len(subject)==0:
            print("Error.",subId, "is not previously added or removed.")
            return;
        if subject[0][2]!=command[4]:
            print("Error. The subject IDs and the stream do not match.")
            return;
    checkdob=command[3].split("/")
    if len(checkdob)!=3:
        print("Error. DoB should match with DD/MM/YYYY format.")
        return;
    for check in checkdob:
        if not(check.isdigit()):
            print("Invalid syntax. Press 'help' to check valid command list.")
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
    global teacherIncrementor
    teacherIncrementor+=1
    isStored=addTeacher("TC"+str(teacherIncrementor),command[1],subIdList, command[3], command[4])
    if (isStored): 
        print("Teacher added.")
        print("Teacher ID :","TC"+str(teacherIncrementor))
        return;
    else:
        teacherIncrementor-=1
        print ("Error. This teacher already exists.")
        return;








def modify_teacher(command):   #[modify_teacher,id, newname ,newsubjectidlist,newdob,newstream]
    "check input for errors to modify a teacher."
    if command[1][0:2]!="TC" or command[1]=="TC" or not(command[1][2:].isdigit()):
        print("Error. Invalid ID.")
        return;
    teacher=getTeacherById(command[1])#[TeacherId,name,[subjectIdList], dob,stream]
    if teacher==None:
        print("Error. Teacher with this ID does not exist.")
        return;
    if not(command[2].isalpha()):
        print("Error. Teacher name should not have numbers included.")
        return;
    if not(command[5]=="A/L" or command[5]=="O/L"):
        print("Error. The stream should be either A/L or O/L.")
        return;
    subIdList=command[3].split(",")
    for subId in subIdList:
        if subIdList.count(subId)>1:
            print("Error. The subject IDs are repeated.")
            return;
        if subId[0:2]!="SB" or subId=="SB" or not(subId[2:].isdigit()):
            print("Error. Invalid ID.")
            return;
        subject=getSubjectById(subId)  #[[subid,subname,substream]]
        if len(subject)==0:
            print("Error.",subId, "is not previously added.")
            return;
        if subject[0][2]!=command[5]:
            print("Error. The subject IDs and the stream do not match.")
            return;
    checkdob=command[4].split("/")
    if len(checkdob)!=3:
        print("Error. DoB should match with DD/MM/YYYY format.")
        return;
    for check in checkdob:
        if not(check.isdigit()):
            print("Invalid syntax. Press 'help' to check valid command list.")
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
    isModified=modifyTeacher(command[1],command[2],subIdList, command[4], command[5])
    if not(isModified):
        print("Error. The teacher with the new details was previously added.")
        return;
    else:
        print("Teacher modified.")
        return;








def remove_teacher(command):  #[remove_teacher, id]
    "check input for errors to remove a teacher."
    if command[1][0:2]!="TC" or not (command[1][2:].isdigit()):
        print("Error. Invalid ID.")
        return;
    teacher=getTeacherById(command[1]) #[id,name,subidlist,dob,stream]
    if teacher==None:
        print("Error. Teacher with this ID does not exist.")
        return;
    isDeleted=deleteTeacher(command[1])
    if (isDeleted)==False:
        print("Error. This teacher does not exist.")
        return;
    else:
        print("Teacher removed.")
        deleteTeacherClassRelationByTeacher(command[1])
        return;
    






def help_teacher(command):  # [help_teacher, id]
    "show all details of the teacher."
    if command[1][0:2]!="TC" or not (command[1][2:].isdigit()):
        print("Error. Invalid ID.")
        return;
    teacher=getTeacherById(command[1]) #[id,name,subidlist,dob,stream]
    if teacher==None:
        print("Error. Teacher with this ID does not exist.")
        return;

    else:
        print("\n")
        print("Teacher Name".ljust(12),":", teacher[1])
        print("DOB".ljust(12),":", teacher[3])
        print("Stream".ljust(12),":", teacher[4])
        print("IDs-Subjects".ljust(12),":", teacher[2])
        print("\n")
        teaClassRelationList=getClassRelationshipsByTeacherId(command[1]) #[[id,teacherId,ClassId]]
        if len(teaClassRelationList)!=0:
            for relation in teaClassRelationList:
                Class=getClassRoomById(relation[2]) #[[ClassId,ClassName,capacity,location]]
                print("Class".ljust(12),":",Class[0][1])  
            print("\n")
            return;
        return;


 
