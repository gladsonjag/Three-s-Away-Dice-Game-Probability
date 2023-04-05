#------------------------Two's Away probability coding project-----------------
import random
import numpy as np
import matplotlib.pyplot as plt
import time


def getDice(roll):
    indicies3 = np.where(roll == 3)[0]
    if len(indicies3) > 0:
        num_dice = len(roll) - len(indicies3)
    else:
        num_dice = len(roll) - 1
    return num_dice 

def getScore(roll):
    indicies3 = np.where(roll == 3)[0]
    if len(indicies3) > 0:
        rollScore = 0
    else:
        rollScore = np.min(roll)
    return rollScore

def play(num_dice):
    score = 0
    while num_dice > 0:
        roll = np.random.randint(low=1, high=7, size=num_dice)
        score += getScore(roll)
        num_dice = getDice(roll)
    
    return score

def CreateScoreList(sampleSize, die_amount):
    datalist = np.empty(shape=(sampleSize), dtype=int)
    for i in range(sampleSize):
        datalist[i] = play(die_amount)

    return datalist

def CreateDataList(scorelist, limit):
    data = np.empty(shape=(limit), dtype=int)
    for i in range(limit):
        numOfScores = len(np.where(scorelist == i)[0])
        data[i] = numOfScores

    return data

def CreatePlot(datalist, limit):

    #creates the % probabilty for the bar chart
    perc_prob_list = []
    total = np.sum(datalist)
    for data in datalist:
        perc_prob_list.append(round((data/total) * 100, 2))

    #Creating a figure with some fig size
    fig, ax = plt.subplots(figsize = (10,5))
    ax.bar(range(limit), datalist, width=0.8)
    #Now the trick is here.
    #plt.text() , you need to give (x,y) location , where you want to put the numbers,
    #So here index will give you x pos and data+1 will provide a little gap in y axis.
    for index, data in enumerate(datalist):
        plt.text(x=index-0.35 , y=data+1 , s=f"{perc_prob_list[index]}%" , fontdict=dict(fontsize=8))
    plt.tight_layout()
    plt.xticks(range(limit))
    plt.show()

    return






def main():
    start_time = time.time()
    turns = 100000
    dieAmount = 6
    scoreLimit = 25
    #makes a list of scores 1st being the amount of turns you want to test and 2nd value being the amount of die being used per turn
    scoreList = CreateScoreList(turns, dieAmount)
    datalist = CreateDataList(scoreList, scoreLimit)
    CreatePlot(datalist, scoreLimit)
    
    print("--- %s seconds ---" % (time.time() - start_time))
    return

main()