#from urllib.request import urlopen
from lxml import etree
from lxml import html
import requests
from io import StringIO

response = requests.get('https://www.insidearbitrage.com/insider-buying/')

parser = etree.HTMLParser()
tree = etree.parse(StringIO(response.text), parser)
root = tree.getroot()
etree.tostring(response, method="text")

#path=f""//*[@id="sortTableM"]/div[2]/table[2]/tbody/tr[2]/td[2]""
#path="//*[@id="sortTableM"]/div[2]/table[2]/tbody/tr[2]/td[2]/a"
#first=tree.xpath(path)
path='//*[@id="sortTableM"]/div[2]/table[2]/tbody/tr[2]/td[2]'
print("this is the value of root:", root)
print(response.xpath(path)
#print(first)
