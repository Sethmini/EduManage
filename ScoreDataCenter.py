#here stores all the relationships between student, subject and score






def addStudentSubjectRelation(id, studentId, subjectId, score):
    "adds relationship to the system if the id doesn't already exist."
    try:
        with open("ScoreFile.txt","r") as scoreFile:
            data = scoreFile.readlines()
            for line in data:
                if str(id) == line.strip("\n").split(" ")[0]:
                    return False
                elif studentId==line.strip("\n").split(" ")[1] and subjectId==line.strip("\n").split(" ")[2]:
                    return False
    except (FileNotFoundError,IndexError):
        pass
    with open("ScoreFile.txt","a") as scoreFile:
        fileLine = str(id) + " " + studentId + " " + subjectId + " " + str(score)
        scoreFile.write(fileLine)
        scoreFile.write("\n")
    return True;









def modifyStudentSubjectRelation(id, studentId, subjectId, score):
    "modifies the relationship from the system if id exists."
    try:
        with open("ScoreFile.txt","r") as scoreFile:
            data = scoreFile.readlines()
        with open("ScoreFile.txt","w") as scoreFile:
            newDataList = []
            for line in data:
                if str(id) == line.strip("\n").split(" ")[0]:
                    if studentId==line.strip("\n").split(" ")[1] and subjectId==line.strip("\n").split(" ")[2] and score==line.strip("\n").split(" ")[3]:
                        scoreFile.write(''.join(data))
                        return 'same_data'
                    else:
                        fileLine = str(id) + " " + studentId + " " + subjectId + " " + str(score) + "\n"
                        newDataList.append(fileLine)
                else:
                    if studentId==line.strip("\n").split(" ")[1] and subjectId==line.strip("\n").split(" ")[2]:
                        scoreFile.write(''.join(data))
                        return 'already_exists'
                    else:
                        fileLine = line
                        newDataList.append(fileLine)
            for line in newDataList:
                scoreFile.write(line)
            return True
    except (FileNotFoundError,IndexError):
        return False








def deleteStudentSubjectRelation(id):
    "delete a Relationship from the system. return True if operation is successful"
    try:
        with open("ScoreFile.txt","r") as scoreFile:
            data = scoreFile.readlines()
        with open("ScoreFile.txt","w") as scoreFile:
            for line in data:
                if str(id) != line.strip("\n").split(" ")[0]:
                    scoreFile.write(line)
                else:
                    with open("RemovedScoreIdFile.txt","a") as removedScoreFile:
                        removedScoreFile.write(line.split(" ")[0]+"\n")
            return True
    except (FileNotFoundError,IndexError):
        return False




    



def getRelationshipsBySubjectId(subjectId):
    "return the relationship list which has mentioned subjectId"
    selectedRelationships=[]
    try:
        with open("ScoreFile.txt","r") as scoreFile:
            data = scoreFile.readlines()
            for line in data:
                if subjectId == line.strip("\n").split(" ")[2]:
                    selectedRelationships.append(line.strip("\n").split(" ")) #[[id,studentId,subjectId,score]]
    except (FileNotFoundError,IndexError):
        pass
    return selectedRelationships







def getRelationshipsByStudentId(studentId):
    "return the relationship list which has mentioned studentId"
    selectedRelationships=[]
    try:
        with open("ScoreFile.txt","r") as scoreFile:
            data = scoreFile.readlines()
            for line in data:
                if studentId == line.strip("\n").split(" ")[1]:
                    selectedRelationships.append(line.strip("\n").split(" ")) #[[id,studentId,subjectId,score]]
    except (FileNotFoundError,IndexError):
        pass
    return selectedRelationships





