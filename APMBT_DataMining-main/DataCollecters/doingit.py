'''
After exctracting all file links in a csv file
we download them-extract them in a directory /DataInit
@uthor: AzsezA
'''
import sys
import csv
import urllib.request
import requests
import os
#import canvas

print("opening CSV file")
#opening links.csv to extract the good links
i=0
with open('links.csv','r') as csvfile:
    reader = csv.DictReader(csvfile)
    print("done opening the file")
    for row in reader :
        if row['Is it Downloadble'] == 'True' :
            print("downloading file  "+str(i)+" : "+row['Dirty link'])
            urllib.request.urlretrieve(row['Clean link'])
            #req = requests.get(row['Clean link'])
            #type (req)
            #file = canvas.Canvas(req)
            #file.save()
            urllib.request.urlretrieve(row['Clean link'],'file'+str(i))
            print("Done !! ")
            i+=1
            #f= open(os.getcwd() + '\\' + 'file'+str(i) + '.txt').read()
#extracting them in the same directory
