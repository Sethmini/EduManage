#here stores all the subjects
#CRUD Create Read Update Delete





def addSubject(id, subjectName, stream):
    "store the subject inside the subject data list. return True if operation is successful"
    try:
        with open("SubjectFile.txt","r") as subjectFile:
            data = subjectFile.read()
            for line in data.strip("\n").split("\n"):
                if str(id)==line.split(" ")[0]:
                    return False;
                elif subjectName == line.strip("\n").split(" ")[1] and stream == line.strip("\n").split(" ")[2]:
                    return False;
    except (FileNotFoundError,IndexError):
        pass
    with open("SubjectFile.txt","a") as subjectFile:
        subjectFile.write(str(id)+" "+subjectName+" "+str(stream)+ "\n")
    return True




            
            

def modifySubject(id, subjectName, stream):
    "modify content of an already stored subject. return True if operation is successful"
    data=[]
    try:
        with open("SubjectFile.txt","r") as subjectFile:
            data=subjectFile.readlines()
        with open("SubjectFile.txt","w") as subjectFile:
            newDataList = []
            for line in data:
                if id == line.strip("\n").split(" ")[0]:
                    if subjectName == line.strip("\n").split(" ")[1] and stream == line.strip("\n").split(" ")[2]:
                        subjectFile.write(''.join(data))
                        return 'same_data'
                    else: 
                        fileLine=str(id)+" "+subjectName+" "+str(stream)+"\n"
                        newDataList.append(fileLine)
                elif subjectName == line.strip("\n").split(" ")[1] and stream == line.strip("\n").split(" ")[2]:
                    subjectFile.write(''.join(data))
                    return 'already_exists'
                else:
                    fileLine = line
                    newDataList.append(fileLine)
            for line in newDataList:
                subjectFile.write(line)
            return True
    except (FileNotFoundError,IndexError):
        return False







def deleteSubject(id):
    "delete a subject from the system. return Tue if operation is successful"
    try:
        with open("SubjectFile.txt","r") as subjectFile:
            data=subjectFile.readlines()
        with open("SubjectFile.txt","w") as subjectFile:
            for line in data:
                if id not in line.strip("\n"):
                    subjectFile.write(line)
                elif data.index(line)==-1:
                    return False
                else:
                    with open("RemovedSubjectIdFile.txt","a") as removedSubjectIdFile:
                        removedSubjectIdFile.write(line.split(" ")[0]+"\n")
            return True
    except FileNotFoundError:
        return False
    
                    
                    



      
def getSubjectById(id):
    "return the subject that has given id. Otherwise return None"
    subjectEntityList=[]
    try:
        with open("SubjectFile.txt","r") as subjectFile:
            data=subjectFile.readlines()
            for line in data:
                if str(id) in line.strip("\n"):
                    subjectEntityList.append(line.strip("\n").split(" "))   #[id,name,stream]
    except FileNotFoundError:
        pass
    return subjectEntityList

        

    
    



def getSubjectBySubjectName(subjectName):
    "return the subject that has given id. Otherwise return None"
    subjectEntityList=[]
    try:
        with open("SubjectFile.txt","r") as subjectFile:
            data=subjectFile.readlines()
            for line in data:
                if subjectName in line.strip("\n"):
                    subjectEntityList.append(line.strip("\n").split(" "))  #[id,name,stream]
    except FileNotFoundError:
        pass
    return subjectEntityList



    

