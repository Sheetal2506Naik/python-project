import requests
from bs4 import BeautifulSoup
url="http://whatismyip.host/"
get_link=requests.get(url,headers={'User-Agent': "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0"})
#print(get_link.text)
soup=BeautifulSoup(get_link.text,'html.parser')
ip=soup.find(class_="ipaddress").text
#print(ip)



m=str(ip)
fhand=open('s.txt','w')
fhand.write(m)




