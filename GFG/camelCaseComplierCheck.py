def camelCaseSeparation(words, variableName):
    tempArr = [[variableName[0]]]
    for var in variableName[1:]:
        if((tempArr[-1][-1].islower() and var.isupper()) or (tempArr[-1][-1].isupper() and var.isupper())):
            tempArr.append(list(var))
        else:
            tempArr[-1].append(var)
    newArr = []
    for i in tempArr:
        newArr.append("".join(i))
    
    for i in (newArr):
        if(i in words):
            continue
        elif(i[0].lower()+i[1:] in words):
            continue
        else:
            return False
    return True

words=["is", 
 "valid", 
 "right",
 "not",
 "no"]
variableName= "isNoTValid"


print(camelCaseSeparation(words, variableName)) #False
words=["is", 
 "valid", 
 "right",
 "not",
 "no"]
variableName= "isNotValid"


print(camelCaseSeparation(words, variableName)) #True
