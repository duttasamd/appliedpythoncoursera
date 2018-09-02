import csv
import os.path

with open(os.path.expanduser('~/dev/python/coursera/introdatasciencepython/res/course1_downloads/mpg.csv')) as csvfile :
    mpg = list(csv.DictReader(csvfile))

# print(mpg[:3])
# print(len(mpg))
# mpg[0].keys()
# round(sum(float(d['cty']) for d in mpg)/len(mpg), 2)

cylmpg = dict()
cylcount = dict()
cylmpg

for row in mpg :
    if(row['cyl'] in cylmpg) :
        cylmpg[row['cyl']] += float(row['cty'])
        cylcount[row['cyl']] += 1
    else :
        cylmpg[row['cyl']] = float(row['cty'])
        cylcount[row['cyl']] = 1

for key in cylcount :
    cylmpg[key] /= cylcount[key]

print(cylmpg)
