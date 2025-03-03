#here stores all the students




def addStudent(id, name, dob):
    "store the student inside the student data list. return True if operation is successful"
    try:
        with open ("StudentFile.txt","r") as studentFile:
            data=studentFile.read()
            for line in data.strip("\n").split("\n"):
                if id==line.split(" ")[0]:
                    print("ID is in the system")
                    print("id",id)
                    print("line.split(" ")[0]",line.split(" ")[0])
                    return False;
                elif name==line.split(" ")[1] and dob==line.split(" ")[2]:
                    return False;
    except (FileNotFoundError,IndexError):
        pass
    with open("StudentFile.txt","a") as studentFile:
        studentFile.write(id + " " + name + " " + dob + "\n")
    return True;








def modifyStudent(id,name,dob):                 
    "modify content of a already stored Student. return True if operation is successful"
    data = []
    try:
        with open ("StudentFile.txt","r") as studentFile:
            data=studentFile.readlines()
        with open ("StudentFile.txt","w") as studentFile:
            for line in data:
                if id in line.strip("\n"):
                    fileLine=str(id)+" "+name+" "+str(dob)
                    studentFile.write(fileLine)
                    studentFile.write("\n")
                else:
                    studentFile.write(line)
            return True
    except FileNotFoundError:
        return False
    




    
    


def deleteStudent(id):                   
    "delete a Student from the system. return True if operation is successful"
    try:
        with open("StudentFile.txt","r") as studentFile:
            data=studentFile.readlines()
        with open ("StudentFile.txt","w") as studentFile:
            for line in data:
                if str(id) not in line.strip("\n"):
                    studentFile.write(line)
                elif data.index(line)==-1:
                    return False
                else:
                    with open("RemovedStudentIdFile.txt","a") as removedIdFile:
                        removedIdFile.write(line.split(" ")[0]+"\n")                            
            return True
    except FileNotFoundError:
        return False
         







def deleteStudentClassRelationByStudent(studentId):
    try:
        with open("StudentClassFile.txt","r") as studentClassFile:
            data = studentClassFile.readlines()
        with open("StudentClassFile.txt","w") as studentClassFile:
            for line in data:
                if studentId not in line.strip("\n"):
                    studentClassFile.write(line)
                elif data.index(line)==-1:
                    return False
                else:
                    with open("RemovedStudentClassIdFile.txt","a") as removedStudentClassIdFile:
                        removedStudentClassIdFile.write(line.split(" ")[0]+"\n")
            return True
    except FileNotFoundError:
        return False



    



def getStudentById(id):
    "return the student that has given id. Otherwise return None"
    studentEntityList=[]
    try:
        with open ("StudentFile.txt","r") as studentFile:
            data=studentFile.readlines()
            for line in data:
                if str(id) in line.strip("\n"):
                    studentEntityList.append(line.strip("\n").split(" "))
    except FileNotFoundError:
        pass
    return studentEntityList
    
        





def getStudentByName(name):
    "return the student that has given name. Otherwise return None"
    studentEntityList=[]
    try:
        with open ("StudentFile.txt","r") as studentFile:
            data=studentFile.read()
            for line in data.strip("\n").split("\n"):
                if name==line.split(" ")[1]:
                    studentEntityList.append(line.split(" "));
    except (FileNotFoundError,IndexError):
        pass
    return studentEntityList;






