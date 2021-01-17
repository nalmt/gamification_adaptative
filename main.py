import pandas as pd
import random
import numpy as np
import operator

avatarPCHexad = pd.read_csv("data/PLS/Hexad/avatarPathCoefs.csv", sep=";")
avatarPVHexad = pd.read_csv("data/PLS/Hexad/avatarpVals.csv", sep=";")
timerPCHexad = pd.read_csv("data/PLS/Hexad/timerpVals.csv", sep=";")
timerPVHexad = pd.read_csv("data/PLS/Hexad/timerPathCoefs.csv", sep=";")
badgesPCHexad = pd.read_csv("data/PLS/Hexad/badgesPathCoefs.csv", sep=";")
badgesPVHexad = pd.read_csv("data/PLS/Hexad/badgespVals.csv", sep=";")
progressPCHexad = pd.read_csv("data/PLS/Hexad/progressPathCoefs.csv", sep=";")
progressPVHexad = pd.read_csv("data/PLS/Hexad/progresspVals.csv", sep=";")
rankingPCHexad = pd.read_csv("data/PLS/Hexad/rankingPathCoefs.csv", sep=";")
rankingPVHexad = pd.read_csv("data/PLS/Hexad/rankingpVals.csv", sep=";")
scorePCHexad = pd.read_csv("data/PLS/Hexad/scorePathCoefs.csv", sep=";")
scorePVHexad = pd.read_csv("data/PLS/Hexad/scorepVals.csv", sep=";")

avatarPCmotiv = pd.read_csv("data/PLS/Motivation/avatarPathCoefs.csv", sep=";")
avatarPVmotiv = pd.read_csv("data/PLS/Motivation/avatarpVals.csv", sep=";")
timerPCmotiv = pd.read_csv("data/PLS/Motivation/timerpVals.csv", sep=";")
timerPVmotiv = pd.read_csv("data/PLS/Motivation/timerPathCoefs.csv", sep=";")
badgesPCmotiv = pd.read_csv("data/PLS/Motivation/badgesPathCoefs.csv", sep=";")
badgesPVmotiv = pd.read_csv("data/PLS/Motivation/badgespVals.csv", sep=";")
progressPCmotiv = pd.read_csv("data/PLS/Motivation/progressPathCoefs.csv", sep=";")
progressPVmotiv = pd.read_csv("data/PLS/Motivation/progresspVals.csv", sep=";")
rankingPCmotiv = pd.read_csv("data/PLS/Motivation/rankingPathCoefs.csv", sep=";")
rankingPVmotiv = pd.read_csv("data/PLS/Motivation/rankingpVals.csv", sep=";")
scorePCmotiv = pd.read_csv("data/PLS/Motivation/scorePathCoefs.csv", sep=";")
scorePVmotiv = pd.read_csv("data/PLS/Motivation/scorepVals.csv", sep=";")

usersData = pd.read_csv("data/userStats.csv", sep=";")
studentsIdsList = usersData["User"]

class Student:

    def __init__(self, id, data, index):
        self.id = id
        self.data = data
        self.index = index

    def getId(self):
        return str(self.id)

    def getAchiver(self):
        return float(self.data["achiever"][self.index])

    def getPlayer(self):
        return float(self.data["player"][self.index])

    def getSocialiser(self):
        return float(self.data["socialiser"][self.index])

    def getFreeSpirit(self):
        return float(self.data["freeSpirit"][self.index])

    def getDisruptor(self):
        return float(self.data["disruptor"][self.index])

    def getPhilanthropist(self):
        return float(self.data["philanthropist"][self.index])

    def printStatistics(self):
        print("Les statistiques pour l'élève " + self.getId() + " :\n Achiver : " + str(self.getAchiver()) +
              "\n Player : " + str(self.getPlayer()) + "\n Player : " + str(self.getPlayer()) +
              "\n Socialiser : " + str(self.getSocialiser()) + "\n FreeSpirit : " + str(self.getFreeSpirit()) +
              "\n Disrupter : ", str(self.getDisruptor()), "\n Philanthropist : " + str(self.getPhilanthropist()))

    def getGameElement(self):
        return str(self.data["GameElement"][self.index])

def pathCoefsValidation(pCoefs, pValues, validateValue, factor):
    pathCoefs = pCoefs.copy()

    if factor == "Hexad":

        if (pValues["achiever"][0] >= validateValue):
            pathCoefs["achiever", 0] = 0

        if (pValues["achiever"][1] >= validateValue):
            pathCoefs["achiever", 1] = 0

        if (pValues["achiever"][2] >= validateValue):
            pathCoefs["achiever", 2] = 0

        if (pValues["socialiser"][0] >= validateValue):
            pathCoefs["socialiser", 0] = 0

        if (pValues["socialiser"][1] >= validateValue):
            pathCoefs["socialiser", 1] = 0

        if (pValues["socialiser"][2] >= validateValue):
            pathCoefs["socialiser", 2] = 0

        if (pValues["player"][0] >= validateValue):
            pathCoefs["player", 0] = 0

        if (pValues["player"][1] >= validateValue):
            pathCoefs["player", 1] = 0

        if (pValues["player"][2] >= validateValue):
            pathCoefs["player", 2] = 0

        if (pValues["freeSpirit"][0] >= validateValue):
            pathCoefs["freeSpirit", 0] = 0

        if (pValues["freeSpirit"][1] >= validateValue):
            pathCoefs["freeSpirit", 1] = 0

        if (pValues["freeSpirit"][2] >= validateValue):
            pathCoefs["freeSpirit", 2] = 0

        if (pValues["disruptor"][0] >= validateValue):
            pathCoefs["disruptor", 0] = 0

        if (pValues["disruptor"][1] >= validateValue):
            pathCoefs["disruptor", 1] = 0

        if (pValues["disruptor"][2] >= validateValue):
            pathCoefs["disruptor", 2] = 0

        if (pValues["philanthropist"][0] >= validateValue):
            pathCoefs["philanthropist", 0] = 0

        if (pValues["philanthropist"][1] >= validateValue):
            pathCoefs["philanthropist", 1] = 0

        if (pValues["philanthropist"][2] >= validateValue):
            pathCoefs["philanthropist", 2] = 0

    elif(factor == "Motvation"):
        if(pValues["MI"][0] >= validateValue):
            pathCoefs["MI"][0] = 0
        if (pValues["MI"][1] >= validateValue):
            pathCoefs["MI"][1] = 0
        if (pValues["MI"][2] >= validateValue):
            pathCoefs["MI"][2] = 0
        if (pValues["ME"][0] >= validateValue):
            pathCoefs["ME"][0] = 0
        if (pValues["ME"][1] >= validateValue):
            pathCoefs["ME"][1] = 0
        if (pValues["ME"][2] >= validateValue):
            pathCoefs["ME"][2] = 0
        if (pValues["amotI"][0] >= validateValue):
            pathCoefs["amotI"][0] = 0
        if (pValues["amotI"][1] >= validateValue):
            pathCoefs["amotI"][1] = 0
        if (pValues["amotI"][2] >= validateValue):
            pathCoefs["amotI"][2] = 0
    return pathCoefs

def getRandomStudent():
    randomStudentId = random.choice(studentsIdsList)
    randomStudentData = usersData.loc[usersData['User'] == randomStudentId]
    index = randomStudentData.index.values.astype(int)[0]
    s = Student(randomStudentId, randomStudentData, index)
    return s

def gameElementScoreArray(pathCoefs):
    geArray = np.zeros(6)
    geArray[0] = pathCoefs["achiever"][0] + pathCoefs["achiever"][1] - pathCoefs["achiever"][2]
    geArray[1] = pathCoefs["player"][0] + pathCoefs["player"][1] - pathCoefs["player"][2]
    geArray[2] = pathCoefs["socialiser"][0] + pathCoefs["socialiser"][1] - pathCoefs["socialiser"][2]
    geArray[3] = pathCoefs["freeSpirit"][0] + pathCoefs["freeSpirit"][1] - pathCoefs["freeSpirit"][2]
    geArray[4] = pathCoefs["disruptor"][0] + pathCoefs["disruptor"][1] - pathCoefs["disruptor"][2]
    geArray[5] = pathCoefs["philanthropist"][0] + pathCoefs["philanthropist"][1] - pathCoefs["philanthropist"][2]
    return geArray

def gameElementMotivationScore(pathcoefs):
    mi = pathcoefs["MI"][0] + pathcoefs["MI"][1] + pathcoefs["MI"][2]
    me = pathcoefs["ME"][0] + pathcoefs["ME"][1] + pathcoefs["ME"][2]
    amot = pathcoefs["amotI"][0] + pathcoefs["amotI"][1] + pathcoefs["amotI"][2]
    score = mi + me + amot
    return score

def generateAffinityArray(factor, student, scoreScoreArray, avatarScoreArray, badgeScoreArray, progressScoreArray, rankingScoreArray, timerScoreArray):
    r = {}
    if factor == "Hexad":
        r["badge"] = student.getAchiver() * badgeScoreArray[0] + student.getPlayer() * badgeScoreArray[1] \
                     + student.getSocialiser() * badgeScoreArray[2] + student.getFreeSpirit() * badgeScoreArray[3] + \
                     student.getDisruptor() * badgeScoreArray[4] + student.getPhilanthropist() * badgeScoreArray[5]

        r["score"] = student.getAchiver() * scoreScoreArray[0] + student.getPlayer() * scoreScoreArray[1] \
                     + student.getSocialiser() * scoreScoreArray[2] + student.getFreeSpirit() * scoreScoreArray[3] + \
                     student.getDisruptor() * scoreScoreArray[4] + student.getPhilanthropist() * scoreScoreArray[5]

        r["avatar"] = student.getAchiver() * avatarScoreArray[0] + student.getPlayer() * avatarScoreArray[1] \
                     + student.getSocialiser() * avatarScoreArray[2] + student.getFreeSpirit() * avatarScoreArray[3] + \
                     student.getDisruptor() * avatarScoreArray[4] + student.getPhilanthropist() * avatarScoreArray[5]

        r["timer"] = student.getAchiver() * timerScoreArray[0] + student.getPlayer() * timerScoreArray[1] \
                     + student.getSocialiser() * timerScoreArray[2] + student.getFreeSpirit() * timerScoreArray[3] + \
                     student.getDisruptor() * timerScoreArray[4] + student.getPhilanthropist() * timerScoreArray[5]

        r["ranking"] = student.getAchiver() * rankingScoreArray[0] + student.getPlayer() * rankingScoreArray[1] \
                     + student.getSocialiser() * rankingScoreArray[2] + student.getFreeSpirit() * rankingScoreArray[3] + \
                     student.getDisruptor() * rankingScoreArray[4] + student.getPhilanthropist() * rankingScoreArray[5]

        r["progress"] = student.getAchiver() * progressScoreArray[0] + student.getPlayer() * progressScoreArray[1] \
                       + student.getSocialiser() * progressScoreArray[2] + student.getFreeSpirit() * progressScoreArray[3] + \
                       student.getDisruptor() * progressScoreArray[4] + student.getPhilanthropist() * progressScoreArray[5]

    elif(factor == "Motivation"):
        r["badge"] = student.getAchiver() * badgeScoreArray

        r["score"] = student.getAchiver() * scoreScoreArray

        r["avatar"] = student.getAchiver() * avatarScoreArray

        r["timer"] = student.getAchiver() * timerScoreArray

        r["ranking"] = student.getAchiver() * rankingScoreArray

        r["progress"] = student.getAchiver() * progressScoreArray

    sortedDict = dict(sorted(r.items(), key=operator.itemgetter(1),reverse=True))

    return sortedDict


def suggestGameElements(affinityArray, studentid, factor):
    print("Les éléments de jeu du plus adapté au moins adapté pour l'élève " + studentid +", selon " + factor + " :")
    n = 1
    for key in affinityArray:
        print(str(n) + "- " + key)
        n = n + 1

student = getRandomStudent()
id = student.getId()

#pathCoefs du profil hexad pour chaque element jeu après validation
pcoefBadges = pathCoefsValidation(badgesPCHexad, badgesPVHexad, 0.05, "Hexad")
pcoefAvatar = pathCoefsValidation(avatarPCHexad, avatarPVHexad, 0.05, "Hexad")
pcoefTimer = pathCoefsValidation(timerPCHexad, timerPVHexad, 0.05, "Hexad")
pcoefProgress = pathCoefsValidation(progressPCHexad, progressPVHexad, 0.05, "Hexad")
pcoefRanking = pathCoefsValidation(rankingPCHexad, rankingPVHexad, 0.05, "Hexad")
pcoefScore = pathCoefsValidation(scorePCHexad, scorePVHexad, 0.05, "Hexad")

#pathCoefs de la motivation pour chaque element jeu après validation
pcoefBadgesmotiv = pathCoefsValidation(badgesPCmotiv, badgesPVmotiv, 0.05, "Motivation")
pcoefAvatarmotiv = pathCoefsValidation(avatarPCmotiv, avatarPVmotiv, 0.05, "Motivation")
pcoefTimermotiv = pathCoefsValidation(timerPCmotiv, timerPVmotiv, 0.05, "Motivation")
pcoefProgressmotiv = pathCoefsValidation(progressPCmotiv, progressPVmotiv, 0.05, "Motivation")
pcoefRankingmotiv = pathCoefsValidation(rankingPCmotiv, rankingPVmotiv, 0.05, "Motivation")
pcoefScoremotiv = pathCoefsValidation(scorePCmotiv, scorePVmotiv, 0.05, "Motivation")

#vecteur de score pour chaque element jeu selon hexad
scoreScoreArray = gameElementScoreArray(pcoefScore)
avatarScoreArray = gameElementScoreArray(pcoefAvatar)
badgeScoreArray = gameElementScoreArray(pcoefBadges)
progressScoreArray = gameElementScoreArray(pcoefProgress)
rankingScoreArray = gameElementScoreArray(pcoefRanking)
timerScoreArray = gameElementScoreArray(pcoefTimer)

#score motivation pour chaque element jeu
scoreScoreMotiv = gameElementMotivationScore(pcoefScoremotiv)
avatarScoreMotiv= gameElementMotivationScore(pcoefAvatarmotiv)
badgeScoreMotiv = gameElementMotivationScore(pcoefBadgesmotiv)
progressScoreMotiv = gameElementMotivationScore(pcoefProgressmotiv)
rankingScoreMotiv = gameElementMotivationScore(pcoefRankingmotiv)
timerScoreMotiv = gameElementMotivationScore(pcoefTimermotiv)

#vecteur d'affinité selon hexad
vectHexad = generateAffinityArray("Hexad", student, scoreScoreArray, avatarScoreArray, badgeScoreArray, progressScoreArray, rankingScoreArray, timerScoreArray)

#vecteur d'affinité selon motivation
vectMotiv = generateAffinityArray("Motivation", student, scoreScoreMotiv, avatarScoreMotiv, badgeScoreMotiv, progressScoreMotiv, rankingScoreMotiv, timerScoreMotiv)

suggestGameElements(vectHexad, id,"son profil Hexad")
print('=================================================================================================================================')
suggestGameElements(vectMotiv, id, "sa motivation")



"""
if student.getGameElement() == "avatar":
    print(pathCoefsValidation(avatarPCHexad, avatarPVHexad, 0.05))
if student.getGameElement() == "timer":
    print(pathCoefsValidation(timerPCHexad, timerPVHexad, 0.05))
if student.getGameElement() == "progress":
    print(pathCoefsValidation(progressPCHexad, progressPVHexad, 0.05))
if student.getGameElement() == "ranking":
    print(pathCoefsValidation(rankingPCHexad, rankingPVHexad, 0.05))
if student.getGameElement() == "score":
    print(pathCoefsValidation(scorePCHexad, scorePVHexad, 0.05))
if student.getGameElement() == "badges":
    print(pathCoefsValidation(badgesPCHexad, badgesPVHexad, 0.05))
"""


