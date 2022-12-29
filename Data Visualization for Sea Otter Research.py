#Aryan Gupta, December 29th, 2022. aryan2026gupta@gmail.com
import matplotlib as plt
import matplotlib.pyplot as plt 
import numpy as np
plt.rcParams.update({'font.size': 22})
#the main dataset is below
#these are the values for capture per year: values = [10, 31, 9, 10, 11, 22, 6, 3, 20, 16, 10, 17, 15, 17, 15, 4] we have done this graph, good!
#these are the values for hot and positive: [4, 0, 0, 0, 3, 7, 3, 0, 1, 0, 0, 2, 0, 0, 3, 0]
#these are the values for cold and positive: [0, 6, 3, 3, 0, 1, 0, 0, 1, 4, 2, 1, 2, 7, 2, 0] - we just did this graph
#these are the values for infected with toxoplasmosis: [4, 6, 3, 3, 3, 8, 3, 0, 2, 4, 2, 3, 2, 7, 5, 0] we have done this graph, good!
#these are the values for exposed to hot: [10, 0, 0, 0, 11, 18, 6, 0, 16, 0, 0, 14, 2, 0, 4, 0] - we have done this graph
#these are the values for exposed to cold: [0, 31, 9, 10, 0, 4, 0, 3, 4, 16, 10, 3, 13, 17, 11, 4] - we have done this graph\

#the below value comparisons compare infected sea otters over all sea otters
values1 = [10, 31, 9, 10, 11, 22, 6, 3, 20, 16, 10, 17, 15, 17, 15, 4]
values2 = [4, 6, 3, 3, 3, 8, 3, 0, 2, 4, 2, 3, 2, 7, 5, 0]

#the below value comparisons compare infected sea otters in hot water over all sea otters captured in hot water
values1 = [4, 0, 0, 0, 3, 7, 3, 0, 1, 0, 0, 2, 0, 0, 3, 0] # hot and positive
values2 = [10, 0, 0, 0, 11, 18, 6, 0, 16, 0, 0, 14, 2, 0, 4, 0] #just hot

values1 = [0, 6, 3, 3, 0, 1, 0, 0, 1, 4, 2, 1, 2, 7, 2, 0] # cold and positive
values2 = [0, 31, 9, 10, 0, 4, 0, 3, 4, 16, 10, 3, 13, 17, 11, 4]# just cold 
#the below value comparisons handle infected sea otters in cold water over all sea otters captured in cold water
def insertzeros(array):
    for x in range(len(array)):
        if array[x]==0:
            array[x]=1

#insertzeros(values1)
#insertzeros(values2)
values = np.divide(values1,values2)
print(values)
dates = ['1998', '1999', '2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013']

#the graph below handles the prevalence of toxoplasmosis per year for all water temperatures
# plt.bar(dates,values, color="orange")
# plt.title('Prevalence of Toxoplasmosis amongst Captured Sea Otters from 1998 to 2013', fontsize=19)
# plt.xlabel('Year', fontsize=17)
# plt.ylabel("Prevalence of Toxoplasmosis", fontsize=17)
# plt.show()
#above is good

#below is the graph that handles the prevalence of toxoplasmosis amongst warm sea otter captures
plt.bar(dates,values, color="crimson")
plt.title('Prevalence of Toxoplasmosis amongst Warm Captures from 1998 to 2013', fontsize=19)
plt.xlabel('Year', fontsize=17)
plt.ylabel("Prevalence of Toxoplasmosis", fontsize=17)
plt.ylim(top=1)
plt.show()
#above is good

#below is the graph that handles the prevalence of toxoplasmosis amongst cold sea otter captures
plt.bar(dates,values, color="deepskyblue")
plt.title('Prevalence of Toxoplasmosis amongst Cold Captures from 1998 to 2013', fontsize=19)
plt.xlabel('Year', fontsize=17)
plt.ylabel("Prevalence of Toxoplasmosis", fontsize=17)
plt.ylim(top=1)
plt.show()
#above is good









#BELOW IS GOOD - all otters captured 
# values = [10, 31, 9, 10, 11, 22, 6, 3, 20, 16, 10, 17, 15, 17, 15, 4]
# dates = ['1998', '1999', '2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013']
# plt.bar(dates,values, color="orange")
# plt.title('Epidemic Curve of Sea Otter Captures from 1998 to 2013',fontsize=19)
# plt.xlabel('Year', fontsize=17)
# plt.ylabel("Number of Sea Otters Captured", fontsize=17)
# plt.rcParams.update({'font.size': 22})
# plt.legend(["216 Total Sea Otters"])
# plt.show()


#BELOW IS GOOD! - infected otters captured 
# values = [4, 6, 3, 3, 3, 8, 3, 0, 2, 4, 2, 3, 2, 7, 5, 0]
# dates = ['1998', '1999', '2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013']
# print(np.sum(values))
# plt.bar(dates,values, color="green")
# plt.title('Epidemic Curve of Toxoplasmosis Sea Otter Captures from 1998 to 2013', fontsize=19)
# plt.xlabel('Year', fontsize=17)
# plt.ylabel("Number of Infected Otters Captured", fontsize=17)
# plt.legend(["55 Total Sea Otters"])
# plt.show()
#stops being good

#below is good - cold otters captured
# values = [0, 31, 9, 10, 0, 4, 0, 3, 4, 16, 10, 3, 13, 17, 11, 4]
# dates = ['1998', '1999', '2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013']
# plt.bar(dates,values, color="deepskyblue")
# plt.title('Epidemic Curve of Cold Seawater Captures from 1998 to 2013', fontsize=19)
# plt.xlabel('Year', fontsize=17)
# plt.ylabel("Number of Cold Seawater Captures", fontsize=17)
# plt.legend(["135 Total Sea Otters"])
# plt.show()
#stop being good

#below is good - hot otters captured 
# values = [10, 0, 0, 0, 11, 18, 6, 0, 16, 0, 0, 14, 2, 0, 4, 0]
# dates = ['1998', '1999', '2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013']
# plt.bar(dates,values, color="crimson")
# plt.title('Epidemic Curve of Warm Seawater Captures from 1998 to 2013', fontsize=19)
# plt.xlabel('Year', fontsize=17)
# plt.ylabel("Number of Warm Seawater Captures", fontsize=17)
# plt.legend(["81 Total Sea Otters"])
# plt.show()
#above is good

#below is good - cold and positive sea otters
# values = [0, 6, 3, 3, 0, 1, 0, 0, 1, 4, 2, 1, 2, 7, 2, 0]
# dates = ['1998', '1999', '2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013']
# plt.bar(dates,values, color="deepskyblue")
# plt.title('Epidemic Curve of Cold, Infected Captures from 1998 to 2013', fontsize=19)
# plt.xlabel('Year', fontsize=17)
# plt.ylabel("Number of Cold, Infected Captures", fontsize=17)
# plt.legend(["32 Total Sea Otters"], loc='upper right')
# plt.show()
#above is good 

#below is good - warm and positive sea otters
# values = [4, 0, 0, 0, 3, 7, 3, 0, 1, 0, 0, 2, 0, 0, 3, 0]
# dates = ['1998', '1999', '2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013']
# plt.bar(dates,values, color="crimson")
# plt.title('Epidemic Curve of Warm, Infected Captures from 1998 to 2013', fontsize=19)
# plt.xlabel('Year', fontsize=17)
# plt.ylabel("Number of Warm, Infected Captures", fontsize=17)
# plt.legend(["23 Total Sea Otters"], loc='upper right')
# plt.show()
#above is good 

