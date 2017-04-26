#!/usr/bin/env python

#Imports
from HTMLParser import HTMLParser
import urllib

#Internal Imports

global domain_name,db_name,c
domain_name='https://www.ooredoo.qa'
db_name='ooredoo.qa'
c=0
class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        # Only parse the 'anchor' tag.
        if tag == "a":
           # Check the list of defined attributes.
           for name, value in attrs:
               # If href is defined
               if name == "href":
                   str = value
                   global c
                   c = c+1
                   print c
                   


def main():
  parser = MyHTMLParser()
  url = domain_name
  test = urllib.urlopen(url).read()
  parser.feed(test)

def start_talwar():
  global domain_name,db_name
  main()

def config_talwar():
   return {'inputs':{'domain_name'}, 'outputs':{'domain_name'} }

start_talwar()
