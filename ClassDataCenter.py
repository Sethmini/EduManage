#Here stores all the classrooms



def addClassRoom(id, name, capacity,location):
    "store the class room inside the class room data list. return True if operation is successful"
    try:
        with open("ClassFile.txt","r") as classFile:
            data = classFile.readlines()
            print("data:",data)
            for line in data:
                if str(id) in line.strip("\n"):
                    return False
    except FileNotFoundError:
        pass
    with open("ClassFile.txt","a") as classFile:
        fileLine = str(id) + " " + str(name) + " " + str(capacity) + " " + location
        print("print(fileLine):",fileLine)
        classFile.write(fileLine)
        classFile.write("\n")
        print(fileLine)
    return True




            

def modifyClassRoom(id, className,capacity,location):
    "modify content of an already stored class room. return True if operation is successful"
    try:
        with open("ClassFile.txt","r") as classFile:
            data=classFile.readlines()
        with open("ClassFile.txt","w") as classFile:
            newDataList = []
            for line in data:
                if id == line.strip("\n").split(" ")[0]:
                    if className==line.strip("\n").split(" ")[1] and capacity==line.strip("\n").split(" ")[2] and location==" ".join(line.strip("\n").split(" ")[3:]):
                        classFile.write(''.join(data))
                        return 'same_data'
                    else:
                        fileLine=str(id)+ " "+str(className)+" "+str(capacity)+" "+location+"\n"
                        newDataList.append(fileLine)
                elif className==line.strip("\n").split(" ")[1] and capacity==line.strip("\n").split(" ")[2] and location==" ".join(line.strip("\n").split(" ")[3:]):
                    classFile.write(''.join(data))
                    return 'already_exists'
                else:
                    fileLine = line
                    newDataList.append(fileLine)
            for line in newDataList:
                classFile.write(line)
            return True
    except (FileNotFoundError,IndexError):
        return False



  


def deleteClassRoom(id):
    "delete a class room from the system. return True if operation is successful"
    try:
        with open("ClassFile.txt","r") as classFile:
            data = classFile.readlines()
        with open("ClassFile.txt","w") as classFile:
            for line in data:
                if id!= line.split(" ")[0]:
                    classFile.write(line)
                else:
                    with open("RemovedClassIdFile.txt","a") as removedClassIdFile:
                        removedClassIdFile.write(line.split(" ")[0]+"\n")
            return True
    except FileNotFoundError:
        return False
   





def deleteTeacherClassRelationByClass(classId):
    try:
        with open("TeacherClassFile.txt","r") as teacherClassFile:
            data = teacherClassFile.readlines()
        with open("TeacherClassFile.txt","w") as teacherClassFile:
            for line in data:
                if classId not in line.strip("\n"):
                    teacherClassFile.write(line)
                elif data.index(line)==-1:
                    return False
                else:
                    with open("RemovedTeacherClassIdFile.txt","a") as removedTeacherClassIdFile:
                        removedTeacherClassIdFile.write(line.split(" ")[0]+"\n")
            return True
    except FileNotFoundError:
        return False







def deleteStudentClassRelationByClass(classId):
    try:
        with open("StudentClassFile.txt","r") as studentClassFile:
            data = studentClassFile.readlines()
        with open("StudentClassFile.txt","w") as studentClassFile:
            for line in data:
                if classId not in line.strip("\n"):
                    studentClassFile.write(line)
                elif data.index(line)==-1:
                    return False
                else:
                    with open("RemovedStudentClassIdFile.txt","a") as removedStudentClassIdFile:
                        removedStudentClassIdFile.write(line.split(" ")[0]+"\n")
            return True
    except FileNotFoundError:
        return False



   



def getClassRoomById(id):
    "return the class room that has given id. Otherwise return None"
    classRoomEntityList=[]
    try:
        with open("ClassFile.txt","r") as classFile:
            data = classFile.readlines()
            for line in data:
                if str(id) == line.strip("\n").split(" ")[0]:
                    classRoomEntityList.append(line.strip("\n").split(" ")) #[['id','name','capacity','location']]
    except (FileNotFoundError,IndexError):
        pass
    return classRoomEntityList


   




def getClassRoomByName(name):
    "return the subject that has given id. Otherwise return None"
    classRoomEntityList=[]
    try:
        with open("ClassFile.txt","r") as classFile:
            data = classFile.readlines()
            for line in data:
                if name == line.strip("\n").split(" ")[1]:
                    classRoomEntityList.append(line.strip("\n").split(" ")) #[['id','name','capacity','location']]
    except (FileNotFoundError,IndexError):
        pass
    return classRoomEntityList


    
  
