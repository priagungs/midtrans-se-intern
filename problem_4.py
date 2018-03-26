import itertools

def sortKey(l):
    return l[2]

def bruteforce(dictPeople):
    namePeople = [x for x in dictPeople]
    listEmbark = list(itertools.permutations(namePeople))
    listDisembark = list(itertools.permutations(namePeople))
    listCartesianProd = []
    for embark in listEmbark:
        for disembark in listDisembark:
            listCartesianProd.append((embark, disembark, evaluate(dictPeople, embark, disembark)))
    listCartesianProd.sort(key=sortKey)
    return listCartesianProd[0][0], listCartesianProd[0][1]
    
def evaluate(dictPeople, embark, disembark):
    currPos = 1
    cost = 0
    elevator = []
    idxEmbark, idxDisembark = 0, 0
    stop = False
    while not stop:
        if idxEmbark == len(embark) and idxDisembark == len(disembark):
            stop = True
        else:
            if(disembark[idxDisembark] in elevator):
                if(idxDisembark < len(disembark)):
                    if currPos != dictPeople[disembark[idxDisembark]][1]:
                        cost += 2+1*abs(currPos-dictPeople[disembark[idxDisembark]][1])
                    currPos = dictPeople[disembark[idxDisembark]][1]
                    idxDisembark += 1
            else:
                if idxEmbark < len(embark):
                    if currPos != dictPeople[embark[idxEmbark]][0]:
                        cost += 2+1*abs(currPos-dictPeople[embark[idxEmbark]][0])
                    currPos = dictPeople[embark[idxEmbark]][0]
                    idxEmbark += 1
    return cost





dictPeople = {
    'p1':(1, 5),
    'p2':(2, 3),
    'p3':(2, 4),
    'p4':(3, 4),
    'p5':(3, 1),
    'p6':(5, 1)
}

embark, disembark = bruteforce(dictPeople)
print(embark)
print(disembark)