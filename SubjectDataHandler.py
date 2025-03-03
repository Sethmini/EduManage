from SubjectDataCenter import addSubject,modifySubject,deleteSubject,getSubjectBySubjectName,getSubjectById
from ScoreDataCenter import getRelationshipsBySubjectId



subjectIncrementer=0
try:
    with open("SubjectFile.txt","r") as subjectFile:
        subjectIncrementer = int(subjectFile.readlines()[-1].split(" ")[0][2:])
except (FileNotFoundError,ValueError,IndexError):
    pass
try:
    with open("RemovedSubjectIdFile.txt","r") as removedSubjectIdFile:
        removedData=removedSubjectIdFile.read()
        removedDataList=removedData.strip("\n").split("\n")
        removedMax=max([int(x[2:]) for x in removedDataList])
        subjectIncrementer=max(removedMax,subjectIncrementer)
except (FileNotFoundError,ValueError,IndexError):
    pass






def handleAddSubject(subjectName,stream):
    "Handling add_subject command"
    subjectEntity=getSubjectBySubjectName(subjectName) #[['id','subjectName','stream']]

    if not subjectName.isalpha():
        print("Error. Subject name should only include alphabetical characters.")
    elif not (stream=="A/L" or stream=="O/L"):
        print("Error. Stream should be either A/L or O/L.")
    else:
        global subjectIncrementer
        subjectIncrementer+=1
        isSuccess=addSubject("SB"+str(subjectIncrementer),subjectName,stream)
        if isSuccess:
            print("Subject added.\nSubject Id :"+" "+"SB"+str(subjectIncrementer))
        else:
            subjectIncrementer-=1
            print("Error. The subject you entered is already added.")
   
       



 
  
def handleModifySubject(subjectId,newSubjectName,stream):
    "Handling modify_subject command"
    subjectEntity=getSubjectById(subjectId) #[['id','name','stream']]
    entity=getSubjectBySubjectName(newSubjectName)  #[['id','name','stream']]
    
    if not(subjectId[0:2]=='SB') or (not subjectId[2::].isdigit()):
        print("Error. Invalid subject ID.")
    elif len(subjectEntity)==0:
        print("Error. The subject ID you entered does not exist in the system.")
    elif not newSubjectName.isalpha():
        print("Error. Subject name should only include alphabetical characters.")
    elif not (stream=="A/L" or stream=="O/L"):
        print("Error. The stream should be either A/L or O/L.")
    elif not newSubjectName.isalpha():
        print("Error. Subject name should only include alphabetical characters. To learn more about syntax, press 'help' to check valid command list.")
    else:
        subjectEntity = getSubjectById(subjectId)
        isSuccess = modifySubject(subjectId,newSubjectName,stream)
        if isSuccess==True:
            print("Subject modified.")
        elif isSuccess=='already_exists':
            print("Error. This new entity already exits.")
        elif isSuccess=='same_data':
            print("Error. You have entered the same data. No modification.")
        else:
            print("Error. This subject does not exist.")
                




   

        
def handleRemoveSubject(subjectId):
    "Handling remove_subject command"
    subjectEntity = getSubjectById(subjectId)   #[['id','name','stream']]

    if not(subjectId[0:2]=='SB') or (not subjectId[2::].isdigit()):
        print("Error. Invalid subject ID.")
    elif len(subjectEntity)==0:
        print("Error. The subject you entered does not exist in the system.")  
    elif len(getRelationshipsBySubjectId(subjectId))!=0:
        print("Error. Cannot be removed. Subject you entered already has a score.")
    else:
        isSuccess = deleteSubject(subjectId)
        if isSuccess==True:
            print("Subject removed.")
        else:
            print("Error. This subject does not exist.")





            
      

def handleShowSubject(subjectId):
    "Handling show_subject command"
    subjectEntity=getSubjectById(subjectId)        #[['id','name','stream']]
    
    if not(subjectId[0:2]=='SB') or (not subjectId[2::].isdigit()):
        print("Error. Invalid subject ID.")
    elif len(subjectEntity)==0:
        print("Error. Subject you entered is not in the system.")
    else:
        print("\n")
        print("\t"+"SUBJECTID".center(15)+"|"+"SUBJECT".center(15)+"|"+"STREAM".center(15))
        print("\t"+subjectEntity[0][0].center(15)+"|"+(subjectEntity[0][1]).center(15)+"|"+(subjectEntity[0][2]).center(15))
        print("\n")



            
