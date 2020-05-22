import requests
from lxml import html

pageContent = requests.get('https://www.insidearbitrage.com/insider-buying/')
tree = html.fromstring(pageContent.text)
first_item=tree.xpath('/html/body/div[1]/div[5]/div[1]/article/div[2]/div[1]/div[2]/table[2]/tbody/tr[2]/td[3]/a')

print(first_item)
#print(pageContent.text)

