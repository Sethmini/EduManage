from ClassDataCenter import addClassRoom, modifyClassRoom, deleteClassRoom, getClassRoomByName, getClassRoomById, deleteTeacherClassRelationByClass, deleteStudentClassRelationByClass






classRoomIncrementer=0
try:
    with open("ClassFile.txt","r") as classFile:
        classRoomIncrementer = int(classFile.readlines()[-1].split(" ")[0][2:])
except (FileNotFoundError,ValueError,IndexError):
    pass
try:
    with open("RemovedClassIdFile.txt","r") as removedClassIdFile:
        removedData=removedClassIdFile.read()
        removedDataList=removedData.strip("\n").split("\n")
        removedMax=max([int(x[2:]) for x in removedDataList])
        classRoomIncrementer=max(removedMax,classRoomIncrementer)
except (FileNotFoundError,ValueError,IndexError):
    pass






def handleAddClassRoom(name,capacity,location):
    "Handling add_class_room command"
    classEntity=getClassRoomByName(name)
    if '-' not in name:
        print("Error. Invalid class name. ex-: 7-B")
        return
    checkName=name.split("-") #[8,C]
    if not(checkName[0].isdigit()):
        print("Error. Grade should be a number.")
        return
    if (int(checkName[0])>13 or int(checkName[0])<1):
        print("Error. Grade should be in the range of 1-13")
        return
    if not(checkName[1].isupper()):
        print("Error. Class should be a capital letter.")
        return
    if not(len(checkName[1])==1): 
        print("Error in class name.")
        return
    if not(capacity.isdigit()):
        print("Error. Capacity should be a number.")
        return
    for classes in classEntity:
        if classes[1]==name:
            print("Error. The class you entered already exists.")
            break
    else:
        global classRoomIncrementer
        classRoomIncrementer+=1
        isSuccess=addClassRoom("CR"+str(classRoomIncrementer),name,capacity,location)
        if isSuccess:
            print("Class room added.\nClass room Id :"+" "+"CR"+str(classRoomIncrementer))
        else:
            classRoomIncrementer-=1
            print("Error. The class room you entered is already added.")
        
            




    

def handleModifyClassRoom(classRoomId,newName,newCapacity,newLocation):
    "Handling modify_class_room command"
    classRoomEntity=getClassRoomById(classRoomId)#[['id','name','capacity','location']]   
    checkNewName=newName.split("-")
    if not(classRoomId[0:2]=='CR') or (not classRoomId[2::].isdigit()):
        print("Error. Invalid class room ID.")
    elif len(classRoomEntity)==0:
        print("Error. Class room ID you entered does not exist in the system.")    
    elif not(checkNewName[0].isdigit()):
        print("Error. Grade should be a number.")
    elif (int(checkNewName[0])>13 or int(checkNewName[0])<1):
        print("Error. Grade should be in the range of 1-13")        
    elif not(checkNewName[1].isupper()):
        print("Error. Class should be a capital letter.")    
    elif not(newCapacity.isdigit()):
        print("Error. Capacity Should be a number.")    
    elif classRoomEntity[0][1]!=newName and len(getClassRoomByName(newName))!=0:
        print("Error. The new class name you entered already exists in the system.")
    else:
        isSuccess = modifyClassRoom(classRoomId,newName,newCapacity,newLocation)
        if isSuccess==True:
            print("Class Room modified.")
        elif isSuccess=='already_exists':
            print("Error. This class already exists.")
        elif isSuccess=='same_data':
            print("Error. You have entered the same data. No modification.")
        else:
            print("Error. This class room does not exist.")
        






        
def handleRemoveClassRoom(classRoomId):
    "Handling remove_class_room command"
    classRoomEntity=getClassRoomById(classRoomId)
    if not(classRoomId[0:2]=='CR') or (not classRoomId[2::].isdigit()):
        print("Error. Invalid class room ID.")
    elif len(classRoomEntity)==0:
        print("Error. The class room you entered does not exist in the system.")
    else:
        classRoomEntity=getClassRoomById(classRoomId)
        isSuccess = deleteClassRoom(classRoomId)
        if isSuccess:
            print("Class room removed.")
            deleteTeacherClassRelationByClass(classRoomId)
            deleteStudentClassRelationByClass(classRoomId)
        else:
            print("Error. This class room does not exist.")
        







def handleHelpClassRoom(classRoomId):
    "Handling show_subject command"
    classRoomEntity=getClassRoomById(classRoomId)    #[id,name,capacity,location]
    if not(classRoomId[0:2]=='CR') or (not classRoomId[2::].isdigit()):
        print("Error. Invalid class room ID.")
    elif len(classRoomEntity)==0:
        print("Error. Class room you entered is not in the system.")
    else:
        classRoomEntity=getClassRoomById(classRoomId)
        print("\n")
        print("\t"+"CLASSID".center(27)+"|"+"CLASSROOM".center(27)+"|"+"CAPACITY".center(27)+"|"+"LOCATION".center(27))
        print("\t"+classRoomEntity[0][0].center(27)+"|"+classRoomEntity[0][1].center(27)+"|"+classRoomEntity[0][2].center(27)+"|"+" ".join(classRoomEntity[0][3:]).center(27))
        print("\n")

    
  
