from ScoreDataCenter import addStudentSubjectRelation, modifyStudentSubjectRelation, deleteStudentSubjectRelation, getRelationshipsByStudentId, getRelationshipsBySubjectId 
from StudentDataCenter import getStudentByName, getStudentById
from SubjectDataCenter import getSubjectById, getSubjectBySubjectName






studentSubjectIncrementor = 0
try:
    with open("ScoreFile.txt","r") as scoreFile:
        studentSubjectIncrementor = int(scoreFile.readlines()[-1][0])
except (FileNotFoundError,ValueError,IndexError):
    pass 
try:
    with open("RemovedScoreIdFile.txt","r") as removedScoreIdFile:
        removedData = removedScoreIdFile.read()
        removedDataList = removedData.strip("\n").split("\n")
        removedMax = max([int(x[0]) for x in removedDataList])
        studentSubjectIncrementor = max(removedMax,studentSubjectIncrementor)
except (FileNotFoundError,ValueError,IndexError):
    pass




#FUNCTIONS




def handleAddStudentSubjectRelation(studentId,subjectId,score):
    "Errors for adding the relationship."
    if studentId[:2]!="ST" or studentId=="ST" or not(studentId[2:].isdigit()): 
        print("Error. Invalid student ID.")
    elif len(getStudentById(studentId))==0:
        print("Error. This student does not exist.")
    elif not(subjectId[0:2]=='SB') or (not subjectId[2::].isdigit()):
        print("Error. Invalid subject ID.")
    elif len(getSubjectById(subjectId))==0:
        print("Error. This subject does not exist.")
    elif not score.isdigit():
        print("Error. The student mark must be a positive number.")
    elif int(score)>100 or int(score)<=0:
        print("Error. The student mark must be in between 0 and 100.")
    else:
        global studentSubjectIncrementor
        studentSubjectIncrementor += 1
        isSuccess = addStudentSubjectRelation(studentSubjectIncrementor,studentId,subjectId,score)
        if isSuccess==True:
            print("Mark added.")
        else:
            studentSubjectIncrementor -=1
            print("Error. This student already has a score.")








def handleModifyStudentSubjectRelation(oldId,oldSubjectId,newId,newSubjectId,score):
    "Errors for modifying the realtionship."
    if oldId[:2]!="ST" or oldId=="ST" or not(oldId[2:].isdigit()): 
        print("Error. Invalid old student ID.")
    elif len(getStudentById(oldId))==0:
        print("Error. This student does not exist.")
    elif not(oldSubjectId[0:2]=='SB') or (not oldSubjectId[2::].isdigit()):
        print("Error. Invalid old subject ID.")
    elif len(getSubjectById(oldSubjectId))==0:
        print("Error. The old subject does not exist.")
    elif newId[:2]!="ST" or newId=="ST" or not(newId[2:].isdigit()): 
        print("Error. Invalid new student ID.")
    elif len(getStudentById(newId))==0:
        print("Error. The new student has not been added to the system yet.")
    elif not(newSubjectId[0:2]=='SB') or (not newSubjectId[2::].isdigit()):
        print("Error. Invalid new subject ID.")
    elif len(getSubjectById(newSubjectId))==0:
        print("Error. The new subject has not been added to the system yet.")
    elif not score.isdigit():
        print("Error. The student mark must be a positive number.")
    elif int(score)>100 or int(score)<=0:
        print("Error. The student mark must be in between 0 and 100.")
    else:
        scoreEntityByStudentId = getRelationshipsByStudentId(oldId) #[[id,studentId,subjectId,score]] 
        scoreEntityBySubjectId = getRelationshipsBySubjectId(oldSubjectId) #[[id,studentId,subjectId,score]] 
        if not(len(scoreEntityByStudentId)!=0 and len(scoreEntityBySubjectId)!=0):
            print("Error. A score needs to be added first to modify it.")
            return
        for relationship1 in scoreEntityByStudentId:
            for relationship2 in scoreEntityBySubjectId:
                if relationship1[0]==relationship2[0]:
                    isSuccess = modifyStudentSubjectRelation(relationship1[0],newId,newSubjectId,score)
                    if isSuccess==True:
                        print("Mark modified.")
                    elif isSuccess=='already_exists':
                        print("Error. The new student already has a score for the new subject in another entity.")
                    elif isSuccess=='same_data':
                        print("Error. You have entered the same data. No modification.")
                    else:
                        print("Error. This student does not have a score yet.")
                    return
        else:
            print("Error. This entity does not exist yet.")
                





    
def handleDeleteStudentSubjectRelation(studentId,subjectId):
    "Errors for removing the relationship."
    if studentId[:2]!="ST" or studentId=="ST" or not(studentId[2:].isdigit()): 
        print("Error. Invalid student ID.")
    elif len(getStudentById(studentId))==0:
        print("Error. This student does not exist.")
    elif not(subjectId[0:2]=='SB') or (not subjectId[2::].isdigit()):
        print("Error. Invalid subject ID.")
    elif len(getSubjectById(subjectId))==0:
        print("Error. This subject does not exist.")
    else:
        scoreEntityByStudentId = getRelationshipsByStudentId(studentId) #[id,studentId,subjectId,score]
        scoreEntityBySubjectId = getRelationshipsBySubjectId(subjectId) #[id,studentId,subjectId,score]
        if not(len(scoreEntityByStudentId)!=0 and len(scoreEntityBySubjectId)!=0):
            print("Error. This score does not exist yet.")
            return
        for relationship1 in scoreEntityByStudentId:
            for relationship2 in scoreEntityBySubjectId:   
                if not(relationship1==relationship2):
                    continue
                isSuccess = deleteStudentSubjectRelation(relationship1[0])
                if isSuccess:
                    print("Mark removed.")
                else:
                    print("Error. The score does not exist.")
                return
        else:
            print("Error. This entity does not exist.")
                







def handleShowMark(studentId,subjectId):
    "Show details of the score of a student for a subject."
    if studentId[:2]!="ST" or studentId=="ST" or not(studentId[2:].isdigit()): 
        print("Error. Invalid student ID.")
    elif not(subjectId[0:2]=='SB') or (not subjectId[2::].isdigit()):
        print("Error. Invalid subject ID.")
    elif len(getStudentById(studentId))==0:
        print("Error. This student does not exist.")
    elif len(getSubjectById(subjectId))==0:
        print("Error. This subject does not exist.")
    else:
        studentEntity = getStudentById(studentId) #[[studentId,name,dob]]
        subjectEntity = getSubjectById(subjectId) #[[subjetcId,name,stream]]
        scoreEntityByStudentId = getRelationshipsByStudentId(studentId) #[id,studentId,subjectId,score]
        scoreEntityBySubjectId = getRelationshipsBySubjectId(subjectId) #[id,studentId,subjectId,score]
        for relationship1 in scoreEntityByStudentId:
            for relationship2 in scoreEntityBySubjectId:
                if relationship1==relationship2:
                    print("\nStudent name :",studentEntity[0][1])
                    print("Subject name :",subjectEntity[0][1])
                    print("Mark         :",relationship1[3],"\n")
                    break
                else:
                    continue
            else:
                continue
            break
        else:
            print("Error. This entity does not exist.")



        



def handleShowAllMarks(studentId):
    "Show details of all scores of the student."
    if studentId[:2]!="ST" or studentId=="ST" or not(studentId[2:].isdigit()): 
        print("Error. Invalid student ID.")
    elif len(getStudentById(studentId))==0:
        print("Error. This student does not exist.")
    else:
        scoreEntityByStudentId = getRelationshipsByStudentId(studentId) #[id,studentId,subjectId,score]
        if len(scoreEntityByStudentId)==0:
            print("There are no scores for this student yet.")
        else:
            studentEntity = getStudentById(studentId) #[[studentId,name,dob]]
            print("\n",studentEntity[0][1],":")
            print("\t"+"Subject ID".center(13)+"|"+"Subject Name".center(15)+"|"+"Score".center(7))
            for index in range(len(scoreEntityByStudentId)):
                subjectEntity = getSubjectById(scoreEntityByStudentId[index][2]) #[[subjectId,subjectName,stream]]
                print("\t"+subjectEntity[0][0].center(13)+"|"+subjectEntity[0][1].center(15)+"|"+scoreEntityByStudentId[index][3].center(7))
            print("\n")





            

def handleShowAllStudents(subjectId):
    "Show all students related to a subject."
    if not(subjectId[0:2]=='SB') or (not subjectId[2::].isdigit()):
        print("Error. Invalid subject ID.")
    elif len(getSubjectById(subjectId))==0:
        print("Error. This subject does not exist.")
    else:
        scoreEntityBySubjectId = getRelationshipsBySubjectId(subjectId) #[[id,studentId,subjectId,score]
        if len(scoreEntityBySubjectId)==0:
            print("This subject does not have any students yet.")
        else:
            subjectEntity = getSubjectById(subjectId) #[[subjectId,name,stream]]
            print("\n")
            print("Subject Name:",subjectEntity[0][1])
            print("Student Names:")
            for relationship in scoreEntityBySubjectId:
                studentEntity = getStudentById(relationship[1]) #[studentId,name,dob]
                print("\t\t"+studentEntity[0][0].center(7)+" - "+studentEntity[0][1].ljust(7))
            print("\n")
            
            

