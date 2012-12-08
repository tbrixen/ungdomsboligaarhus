# -*- coding: ISO-8859-1 -*-
import urllib
import urllib2
import re
import sys

#Config
username = 0;

if(username == 0):
        sys.exit('You need to configure the script');

#Send the HTTP request
url = 'http://ungdomsboligaarhus.dk/web/512/Work.nsf/Login?OpenAgent&User=' + str(username) + '&renew'
req = urllib2.Request(url)

#Recive the html
response = urllib2.urlopen(req)
the_page = response.read()

#See if the page contains "Du har nu fornyet din"
regex = re.compile("Du har nu fornyet din")
r = regex.search(the_page)
if r:
  print 'Du har nu genansøgt'
else:
  print 'Der er sket en fejl i genansøgningen'
