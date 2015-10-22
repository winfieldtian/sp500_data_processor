import urllib2
import string
import sys
import datetime

TICKERS = []

TICKERS = [line.rstrip('\n') for line in open('sp500.txt')]

for TICKER in TICKERS:
	print "DOWNLOADING " + TICKER
	response = urllib2.urlopen('http://www.google.com/finance/getprices?i=60&p=10d&f=d,o,h,l,c,v&df=cpct&q='+TICKER)
	html = response.read()

	sansHeader = '\n'.join(html.split('\n')[7:]) 

	with open(TICKER+".txt", "a") as myfile:
		myfile.write(sansHeader + '\n')


today = datetime.date.today()
todaysDate = []
todaysDate.append(today)
stringDate = str(todaysDate[0])

with open("metadata.txt", "a") as readme:
    	readme.write('Updated minute resolution data as of ' + stringDate + '\n')
