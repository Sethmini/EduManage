#here stores all the teachers


def addTeacher(id, name, subjectIdList,dob,stream):
    "store the teacher inside the student data list. return True if operation is successful"
    try:
        with open ("TeacherFile.txt","r") as teacherFile:
            data=teacherFile.read()
            for line in data.strip("\n").split("\n"):
                if id==line.split(" ")[0]:
                    return False;
                if name==line.split(" ")[1] and len(subjectIdList)==len(line.split(" ")[2].split(",")) and dob==line.split(" ")[3]:
                    for subject in subjectIdList:
                        if subject in line.split(" ")[2].split(","):
                            return False;
    except (FileNotFoundError,IndexError):
        pass
    with open("TeacherFile.txt","a") as teacherFile:
        teacherFile.write(id + " " + name +" "+ ",".join(subjectIdList)+" " + dob +" "+stream+ "\n")
    return True;




    

def modifyTeacher(id, name,subjectIdList, dob, stream):
    "modify content of a already stored teacher. return True if operation is successful"
    data = []
    try:
        with open ("TeacherFile.txt","r") as teacherFile:
            data=teacherFile.read()
        for line in data.strip("\n").split("\n"):
            if name==line.split(" ")[1] and len(subjectIdList)==len(line.split(" ")[2].split(",")) and dob==line.split(" ")[3]:
                for subject in subjectIdList:
                    if subject in line.split(" ")[2].split(","):
                        return False;
        with open ("TeacherFile.txt","w") as teacherFile:
             for line in data.strip("\n").split("\n"):
                if id==line.split(" ")[0]:
                    teacherFile.write(id + " " + name +" "+ ",".join(subjectIdList)+" " + dob +" "+stream+ "\n")
                else:
                    teacherFile.write(line+"\n")
        return True
    except FileNotFoundError:
        return False;






def deleteTeacher(id):
    "delete a teacher from the system. return True if operation is successful"
    try:
        with open("TeacherFile.txt","r") as teacherFile:
            data=teacherFile.read()
        with open ("TeacherFile.txt","w") as teacherFile:
            for line in data.strip("\n").split("\n"):
                if id!=line.split(" ")[0]:
                    teacherFile.write(line+"\n")
                else:
                    with open ("RemovedTeacherIdFile.txt","a") as removedIdFile:
                        removedIdFile.write(line.split(" ")[0]+"\n")
            return True
    except FileNotFoundError:
        return False;






def deleteTeacherClassRelationByTeacher(teacherId):
    try:
        with open("TeacherClassFile.txt","r") as teacherClassFile:
            data = teacherClassFile.readlines()
        with open("TeacherClassFile.txt","w") as teacherClassFile:
            for line in data:
                if teacherId not in line.strip("\n"):
                    teacherClassFile.write(line)
                elif data.index(line)==-1:
                    return False
                else:
                    with open("RemovedTeacherClassIdFile.txt","a") as removedTeacherClassIdFile:
                        removedTeacherClassIdFile.write(line.split(" ")[0]+"\n")
            return True
    except FileNotFoundError:
        return False






def getTeacherById(id):
    "return the teacher that has given id. Otherwise return None"
    try:
        with open ("TeacherFile.txt","r") as teacherFile:
            data=teacherFile.read()
            for line in data.strip("\n").split("\n"):
                if id==line.split(" ")[0]:
                    stepOne=line.split(" ")
                    stepTwo=stepOne[2].split(",")
                    returnLine=[]
                    returnLine.extend(stepOne[0:2])
                    returnLine.append(stepTwo)
                    returnLine.extend(stepOne[3:])
                    return returnLine;
            return None;
    except (FileNotFoundError,IndexError):
        return None;



