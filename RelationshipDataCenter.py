#relationships between teacher, student and class






def addTeacherClass(id, teacherId, classId):
    "adds a relationship of teacher and class to the system if it doesnt already exist."
    try:
        with open("TeacherClassFile.txt","r") as teacherClassFile:
            data = teacherClassFile.readlines()
            for line in data:
                if str(id)==line.strip("\n").split(" ")[0]:
                    return False
                elif teacherId==line.strip("\n").split(" ")[1]:
                    return False
                elif classId==line.strip("\n").split(" ")[2]:
                    return False
    except (FileNotFoundError,IndexError):
        pass
    with open("TeacherClassFile.txt","a") as teacherClassFile:              
        fileLine = str(id) + " " + teacherId + " " + classId
        teacherClassFile.write(fileLine)
        teacherClassFile.write("\n") 
    return True





def addStudentClass(id, studentId, classId, capacity):
    "adds a relationship of student and class to the system if it doesnt already exist"
    try:
        with open("StudentClassFile.txt","r") as studentClassFile:
            data = studentClassFile.read()
            dataList = data.split("\n")
            maxCapacity = 0
            for line in dataList:
                if classId in line:
                    maxCapacity += 1
            if maxCapacity>=int(capacity):
                return 'exceeds_capacity'
            else:
                for line in dataList:
                    if str(id)==line.split(" ")[0]:
                        return False
                    elif studentId in line:
                        return False
    except (FileNotFoundError):
        pass
    with open("StudentClassFile.txt","a") as studentClassFile:
        fileLine = str(id) + " " + studentId + " " + classId
        studentClassFile.write(fileLine)
        studentClassFile.write("\n")
    return True






def getClassRelationshipsByTeacherId(teacherId):
    "returns the relationship list which has teacher and the class IDs"
    selectedRelationships=[]
    try:
        with open("TeacherClassFile.txt","r") as teacherClassFile:
            data = teacherClassFile.readlines()
            for line in data:
                if teacherId in line.strip("\n"):
                    selectedRelationships.append(line.strip("\n").split(" ")) #[['id','teacherId','classId']]
    except FileNotFoundError:
        pass
    return selectedRelationships    






def getClassRelationshipsByStudentId(studentId):
    "returns the relationship list which has student and class IDs"
    selectedRelationships=[]
    try:
        with open("StudentClassFile.txt","r") as studentClassFile:
            data = studentClassFile.readlines()
            for line in data:
                if studentId in line.strip("\n"):
                    selectedRelationships.append(line.strip("\n").split(" ")) #[['id','studentId','classId']]
    except FileNotFoundError:
        pass
    return selectedRelationships  






def getStudentRelationshipsByClassId(classId):
    "returns the relationship list with students and class IDs"
    selectedRelationships=[]
    try:
        with open("StudentClassFile.txt","r") as studentClassFile:
            data = studentClassFile.readlines()
            for line in data:
                if classId in line.strip("\n"):
                    selectedRelationships.append(line.strip("\n").split(" ")) #[['id','studentId','classId']]
    except FileNotFoundError:
        pass
    return selectedRelationships






def getTeacherRelationshipsByClassId(classId):
    "returns the relationship list with teacher and class IDs"
    selectedRelationships=[]
    try:
        with open("TeacherClassFile.txt","r") as teacherClassFile:
            data = teacherClassFile.readlines()
            for line in data:
                if classId in line.strip("\n"):
                    selectedRelationships.append(line.strip("\n").split(" ")) #[['id','teacherId','classId']]
    except FileNotFoundError:
        pass
    return selectedRelationships


    
