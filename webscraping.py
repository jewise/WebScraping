#Web scraping tutorial using python
#https://www.youtube.com/watch?v=3xQTJi2tqgk

import reqeusts
from bs4 import Beautifulsoup

f `
url = "http://www.yellowpages.com/los-angeles-ca/coffee?g=los%20angeles%2C%20ca&q=coffee"
r = requests.get(url)

soup = BeautifulSoup(r.content)

links = soup.find_all("a")

for link in links:
	print "<a href'%s'>%s</a>" %(link.get("href"), link.text)


g_data = soup.find_all("div", {"class": "info"})

for item in g_data: 
	print item.text

for item in g_data:
	print item.contents

for item in g_data:
	print item.contents

for item in g_data:
	print item.contents[0]
	print item.contents[1]

for item in g_data:
	print item.contents[0].text
	print item.contents[1].text


for item in g_data:
	print item.contents[0].find_all ("a", {"class": "business-name"})[0].text
	try:
		print item.contents[1].find_all ("span", {"itemprop": "streetAddress"})[0].text
	except:
		print item.contents[1].find_all ("p", {"itemprop": "address"})[0].text 
	#try:
	#	print item.contents[1].find_all ("p", {"itemprop": "address"})[0].text
	#except:
		#pass 
	try:
		print item.contents[1].find_all ("span", {"itemprop": "addressLocality"})[0].text.replace(',','')
	except:
		pass
	try:
		print item.contents[1].find_all ("span", {"itemprop": "addressRegion"})[0].text
	except:
		pass
	try:
		print item.contents[1].find_all ("span", {"itemprop": "postalCode"})[0].text
	except:
		pass  
	try:
		print item.contents[1].find_all ("li", {"class": "primary"})[0].text
	except:
		pass














