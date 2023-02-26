
import csv
#create data table values for hot or cold. we only need data that is within hot, or within cold. 
#so we have to create the data that corresponds to hot or cold
# we have to convert the times into years. #so we can use the online calculator for that
#after that, we just have to say if it's TG>then we had it to that array

#it's easiest if we split them into hot or cold lists, then we ask if they are true positive or true negative

#we want these for high OR
positiveAndHot=[]
negativeAndCold=[]

#we don't want these cases for OR
positiveAndCold=[]
negativeAndHot=[]

#hot is january 1st 1998 to june 1st 1998, hot is june 1st 2002 to march 1st 2003. july 1st 2004 to march 1st 2005, september 1st of 2006 to february 1st of 2007, july 1st 2009 to april 1st 2010. 
#cold is july 1st 1998 to march 1st 2001, november 1st of 2005 to april 1st of 2006, june 1st 2007 to july 1st 2008, november 1st 2008 to april 1st 2009. june 1st 2010 to june 1st 2011. july 1st 2011 to may 1st 2012. 

#now we must convert these dates to numeric format

# we need to create ranges

#wash does not span any days of hot values
#scrz does not span any days of hot values
#saba doesn't seem statistically significant

#snlo and wash seem fine, snlo might be biased towards hot values
#mont seems good, not too significant
#elks doesnt span any hot values
#bigs is good, not too significant

file = open('mont.csv') #this section of code just inputs our csv data into arrays, which is kinda helpful.
csvreader = csv.reader(file)
header = []
header = next(csvreader)
rows = []
for row in csvreader:
        rows.append(row)

def hotOrColdDeterminer(date):
    #hot below
    if (date>35794 and date <=35945):
        return "hot"
    if (date>37406 and date <=37679):
        return "hot"
    if (date>38167 and date <=38410):
        return "hot"
    if (date>38959 and date <=39112):
        return "hot"
    if (date>39993 and date <=40267):
        return "hot"
    
#these dates below are for values with heat < 0.5 
    if (date>37286 and date <=37406):
        return "hot"
    if (date>37679 and date <=37740):
        return "hot"
    if (date>37801 and date <=38167):
        return "hot"
    if (date>38410 and date <=38532):
        return "hot"
    if (date>38867 and date <=38959):
        return "hot"
    if (date>39112 and date <=39140):
        return "hot"
    if (date>39932 and date <=39993):
        return "hot"
    if (date>40267 and date <=40297):
        return "hot"
    if (date>41059 and date <=41242):
        return "hot"

    
    #cold below
    if (date>35975 and date <=36949):
        return "cold"
    if (date>38655 and date <=38806):
        return "cold"
    if (date>39232 and date <=39628):
        return "cold"
    if (date>39751 and date <=39902):
        return "cold"
    if (date>40328 and date <=40693):
        return "cold"
    if (date>40723 and date <=41028):
        return "cold"

#these dates below are for cold < 0.5
    if (date>35945 and date <=35975):
        return "cold"
    if (date>36949 and date <=37286):
        return "cold"
    if (date>37740 and date <=37801):
        return "cold"
    if (date>38532 and date <=38655):
        return "cold"
    if (date>38806 and date <=38867):
        return "cold"
    if (date>39140 and date <=39232):
        return "cold"
    if (date>39628 and date <=39751):
        return "cold"
    if (date>39902 and date <=39932):
        return "cold"
    if (date>40297 and date <=40328):
        return "cold"
    if (date>40693 and date <=40723):
        return "cold"
    if (date>41028 and date <=41059):
        return "cold"
    if (date>41242 and date <=41637):
        return "cold"


hottdays1=0
colddays1=0

counter=0 # 216 iterations must be completed
while counter<len(rows):
    date1=rows[counter][1]
    date1=int(date1)
    tgstatus=rows[counter][14]
    tgstatus=int(tgstatus)

    string1=hotOrColdDeterminer(date1)
    #print(date1, tgstatus, string1)

    if (string1=='hot' and tgstatus==1):
        positiveAndHot.append(rows[counter][0])
        hottdays1=hottdays1+1


    if (string1=='cold' and tgstatus==1):
        positiveAndCold.append(rows[counter][0])
        colddays1=colddays1+1

    if (string1=='hot' and tgstatus==0):
        negativeAndHot.append(rows[counter][0])
        hottdays1=hottdays1+1

    if (string1=='cold' and tgstatus==0):
        negativeAndCold.append(rows[counter][0])
        colddays1=colddays1+1

    counter=counter+1

print(len(positiveAndHot), "a")
print(len(negativeAndCold), "d")
print(len(positiveAndCold), "c")
print(len(negativeAndHot), "b")
a=len(positiveAndHot)
b=len(negativeAndHot)
c=len(positiveAndCold)
d=len(negativeAndCold)

colddays=2342+1344
hottdays=1094+1063

numerator=len(positiveAndHot)*len(negativeAndCold)
denominator=len(positiveAndCold)*len(negativeAndHot)

#oddsRatio=numerator/denominator
oddsRatio1=numerator/denominator*colddays1/hottdays1

numerator1=a/(a+b)
denominator1=c/(c+d)

relativerisk=numerator1/denominator1*(colddays1/hottdays1)
print(colddays1/hottdays1)


#print(oddsRatio)
print("with temperature scaling factor,", oddsRatio1, relativerisk)
print("without temperature scaling factor," , numerator/denominator,numerator1/denominator1)
print("hot mortality", a+b, (a+b)*colddays1/hottdays1)
print("cold mortality", c+d, (c+d))

