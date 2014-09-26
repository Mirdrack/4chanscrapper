from bs4 import BeautifulSoup
import requests, shutil, random, string

def randomword(length):
   return ''.join(random.choice(string.lowercase) for i in range(length))

def download_img(url):
	filename = randomword(10)
	response = requests.get(url, stream=True)
	with open(filename + '.png', 'wb') as out_file:
	    shutil.copyfileobj(response.raw, out_file)
	del response
	print(filename + " " + url)
 	pass 

#url = "http://boards.4chan.org/wg/thread/5933467/beautiful-girl-thread"
url = raw_input('Enter your input:')
r = requests.get(url)
data = r.text
soup = BeautifulSoup(data)

links = soup.find_all("a", class_="fileThumb")
for link in links:
	download_img("http:" + link.get('href'))
