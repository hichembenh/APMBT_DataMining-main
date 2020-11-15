'''
Data downloader from http://www.bvmt.com.tn/fr/content/historique-des-donn%C3%A9es
@uthor AzsezA
collecting all links
'''
import requests
from bs4 import BeautifulSoup
import wget
#import re
import csv
with open('linksCmf.csv', 'w', newline='') as csvfile:
    header = ['Dirty link','Clean link','Is it Downloadble']
    writer = csv.DictWriter(csvfile, fieldnames=header)
    writer.writeheader()