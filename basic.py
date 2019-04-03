




'''

WebCrawler:

Search querry: url changed when search querry, error handler, try except
Cheat webiste (user agent)
Fill form
Fill form, multiple pages form, Gmail email
Search through the website, e.g. first list the buttons on the website
'''






import urllib.request
import urllib.parse

url = 'https://www.cosmopolitan.com/search/'
#url3 = 
url2 = 'https://www.cosmopolitan.com/search/?q=car'

#values = {'q':'car','submit':'search'}
values = {'q':'car'}

data = urllib.parse.urlencode(values)
data = data.encode('utf-8')


header = {}
header['User-Agent'] = 'Mozilla/5.0'
req = urllib.request.Request(url = url,data= data, headers = header)

response = urllib.request.urlopen(req)
#response = urllib.request.urlopen(url2)

webpage = response.read().decode('utf-8')


file = open('file.txt','w')

file.write(webpage)

file.close()
