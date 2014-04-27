import csv
from functools import partial
				# Finding States' Laziness Rankings: #
dataDict = {}

with open('data.csv', 'rU') as csvfile:
	dataReader = csv.reader(csvfile, delimiter=',')
	for row in dataReader:
		state = row[0]
		row.pop(0)
		dataDict[state] = row

projectedmeans = []
with open('rafadata.csv', 'rb') as csvfile: 
	dataReader = csv.reader(csvfile, delimiter=',')
	for row in dataReader:
		projectedmeans.append(row[0])

gdps = []
with open('gdp data.csv', 'rb') as csvfile: 
    dataReader = csv.reader(csvfile, delimiter=',')
    for row in dataReader:
        for letter in row[1]:
            if letter == ',':
                row[1].remove(letter)
        gdps.append((row[0], float(row[1])))
gdps.sort(key=lambda x: x[0])

obesitylevels = []
with open('Obesity data.csv', 'rb') as csvfile:
    dataReader = csv.reader(csvfile, delimiter=',')
    for row in dataReader:
        for letter in row[1]:
            if letter == ',':
                row[1].remove(letter)
        obesitylevels.append((row[0], float(row[1])))

educationlevels = []
with open('education data.csv', 'rb') as csvfile:
    dataReader = csv.reader(csvfile, delimiter=',')
    for row in dataReader:
        for letter in row[1]:
            if letter == ',':
                row[1].remove(letter)
        educationlevels.append((row[0], float(row[1])))
educationlevels.sort(key=lambda x: x[0])


projectedmeans = map(float, projectedmeans)

meanlist = []
for i in dataDict:
	i = [i]
	meanlist.append(i)

index = 0
while index < 50:
	meanlist[index].append(projectedmeans[index])
	index +=1

    # Add relevant information #
meanlist.sort(key=lambda x: x[0])
index = 0
while index<50:
    meanlist[index].append(gdps[index][1])
    meanlist[index].append(obesitylevels[index][1])
    meanlist[index].append(educationlevels[index][1])
    index +=1

meanlist.sort(key=lambda x: x[1], reverse= True)

	# Adding rank to each state#

index = 0
rank = 10
n = 0
go = True
while go:
    for i in range(0,5):
		meanlist[index].insert(0, rank)
		index +=1
    rank -=1
    if rank ==0:
        go = False

def score(inputlist):
    total = 0
    for i in inputlist:
        if i=='a':
            total += 4
        elif i =='b':
            total += 3
        elif i =='c':
            total += 2
        elif i =='d':   
            total += 1
    return total



        # Fix this algorithm before my eyes go blind please #
def state_rank(score):
    if score<=13:
        return 10
    elif score>13 and score<=16:
        return 9
    elif score>16 and score<=19:
        return 8
    elif score>19 and score<=22:
        return 7
    elif score>22 and score<=25:
        return 6
    elif score>25 and score<=28:
        return 5
    elif score>28 and score<=31:
        return 4
    elif score>31 and score<=34:
        return 3
    elif score>34 and score<=37:
        return 2
    elif score>37:
        return 1

def get_rank(scorelist):
    return state_rank(score(scorelist))

def correctstate(somelist, rank):
    if somelist[0]==rank:
        return True
    else:
        return False

def returnresult(rank, somelist):
    yourstates1 = filter(partial(correctstate, rank=get_rank(somelist)), meanlist)
    yourstates = []
    index = 0
    while index<len(yourstates1):
        yourstates.append(yourstates1[index])
        index +=1
    return yourstates


