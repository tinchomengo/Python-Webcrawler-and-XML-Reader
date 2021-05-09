'''
XML parser reads web XML file and adds integer tag content and prints its sum
'''


import xml.etree.ElementTree as ET
import urllib.request
finalcount = 0

url = urllib.request.urlopen("") #  url has to be added
r_url = url.read().decode("utf-8")
par = ET.fromstring(r_url)
stuff = par.findall('') #  Add path for tags you look for on XSD eg: ('person/name')
for tag in stuff:
    count = tag.find('count').text #  'count' tag name may vary, but content must be an integer
    finalcount += int(count)
print(finalcount)
