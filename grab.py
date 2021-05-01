from urllib import request
from urllib.parse import urlencode
import re
from os import system
from time import sleep
import concurrent.futures
import socket
system("clear")
la5dhar = '\033[92m'
system("clear")
la7mar  = '\033[91m'
green = '\033[92m'
labyadh = '\033[00m'
green = "\033[0;32m"
auth = """{} MCA-BD New Crew Scanner{}
  ____  _            _      _____  _     _     _     
 |  _ \| |          | |    |  __ \| |   (_)   | |    
 | |_) | | __ _  ___| | __ | |__) | |__  _ ___| |__  
 |  _ <| |/ _` |/ __| |/ / |  ___/| '_ \| / __| '_ \ 
 | |_) | | (_| | (__|   <  | |    | | | | \__ \ | | |
 |____/|_|\__,_|\___|_|\_\ |_|    |_| |_|_|___/_| |_|
                       ______                        
                      |______|                      
        
    		   Version: 1.0.0

   {} We Don’t Responsible For Any illegal Activists {}
    """.format(la7mar,green,la7mar,green)
headers = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}
try:
	domain = open("domain.txt","r").read().splitlines()
except:
	domain = ['co.in','co.uk','in','pk','co.pk','co.org','org','com','uk','bd','net','ac', 'ad', 'ae', 'af', 'ag', 'ai', 'al', 'am', 'an', 'ao',
                        'aq', 'ar', 'as', 'at', 'au', 'aw', 'ax', 'az', 'ba', 'bb',
                        'bd', 'be', 'bf', 'bg', 'bh', 'bi', 'bj', 'bm', 'bn', 'bo',
                        'br', 'bs', 'bt', 'bv', 'bw', 'by', 'bz', 'ca', 'cc', 'cd',
                        'cf', 'cg', 'ch', 'ci', 'ck', 'cl', 'cm', 'cn', 'co', 'cr',
                        'cu', 'cv', 'cx', 'cy', 'cz', 'de', 'dj', 'dk', 'dm', 'do',
                        'dz', 'ec', 'ee', 'eg', 'eh', 'er', 'es', 'et', 'eu', 'fi',
                        'fj', 'fk', 'fm', 'fo', 'fr', 'ga', 'gb', 'gd', 'ge', 'gf',
                        'gg', 'gh', 'gi', 'gl', 'gm', 'gn', 'gp', 'gq', 'gr', 'gs',
                        'gt', 'gu', 'gw', 'gy', 'hk', 'hm', 'hn', 'hr', 'ht', 'hu',
                        'id', 'ie', 'il', 'im', 'in', 'io', 'iq', 'is', 'it',
                        'je', 'jm', 'jo', 'jp', 'ke', 'kg', 'kh', 'ki', 'km', 'kn',
                        'kp', 'kr', 'kw', 'ky', 'kz', 'la', 'lb', 'lc', 'li', 'lk',
                        'lr', 'ls', 'lt', 'lu', 'lv', 'ly', 'ma', 'mc', 'md', 'me',
                        'mg', 'mh', 'mk', 'ml', 'mm', 'mn', 'mo', 'mp', 'mq', 'mr',
                        'ms', 'mt', 'mu', 'mv', 'mw', 'mx', 'my', 'mz', 'na', 'nc',
                        'ne', 'nf', 'ng', 'ni', 'nl', 'no', 'np', 'nr', 'nu', 'nz',
                        'om', 'pa', 'pe', 'pf', 'pg', 'ph', 'pk', 'pl', 'pm', 'pn',
                        'pr', 'ps', 'pt', 'pw', 'py', 'qa', 're', 'ro', 'rs', 'ru',
                        'rw', 'sa', 'sb', 'sc', 'sd', 'se', 'sg', 'sh', 'si', 'sj',
                        'sk', 'sl', 'sm', 'sn', 'so', 'sr', 'st', 'su', 'sv', 'sy',
                        'sz', 'tc', 'td', 'tf', 'tg', 'th', 'tj', 'tk', 'tl', 'tm',
                        'tn', 'to', 'tp', 'tr', 'tt', 'tv', 'tw', 'tz', 'ua', 'ug',
                        'uk', 'um', 'us', 'uy', 'uz', 'va', 'vc', 've', 'vg', 'vi',
                        'vn', 'vu', 'wf', 'ws', 'ye', 'yt', 'za', 'zm', 'zw', 'com',
                        'net', 'org', 'biz', 'gov', 'mil', 'edu', 'info', 'int', 'tel']
def ipdorker(dork):
	okkk = dork
	first = 0
	try:
		for i in range(int(page2)):
			first = first+50
			url = "http://www.bing.com/search?q=ip%3A%22"+okkk+"%22&count=1000&first="+str(first)
			url = request.Request(url,None,headers=headers)
			result = request.urlopen(url,timeout=10)
			result = result.read().decode('utf-8')
			patern = r'<h2><a href="(.*?)"'
			ok = re.findall(patern,result)
			for i in ok:
				i = i.replace("<strong>","")
				i = i.replace("</strong>","")
				i = i.replace("http://","")
				i = i.replace("https://","")
				i = i.replace("www.","")
				i = i.split("/")
				i = i[0]
				check(i)						
	except Exception as e:
		print(e)
		#print(la7mar+" [!] Connection Failed [!]")
		ipdorker(dork)
def ip(x):
	x = x
	try:
		socket.setdefaulttimeout(2)
		url = socket.gethostbyname(x)
	except socket.herror:
		return 5
	try:
		file = open("all-ip.txt","r").read()
	except:
		open("all-ip.txt","w")
		file = open("all-ip.txt","r").read()
	if url in file:
		print(la7mar+" [+] IP Exists: "+url)
	else:
		file = open("all-ip.txt","a")
		file.write(url+"\n")
		file.close()
		print(green+" [+] IP Added: "+url)
		ipdorker(url)	
def bing(dork):
	for dom in domain:
		okkk = dork.strip()+" site:."+dom
		first = 0
		try:
			for i in range(int(page1)):
				first = first+50
				params = {'q': okkk, 'count': '1000','first':first}
				get = urlencode(params)
				url = "http://www.bing.com/search?"+get
				url = request.Request(url,None,headers=headers)
				result = request.urlopen(url,timeout=10)
				result = result.read().decode('utf-8')
				patern = r'<h2><a href="(.*?)"'
				ok = re.findall(patern,result)
				for i in ok:
					i = i.replace("<strong>","")
					i = i.replace("</strong>","")
					i = i.replace("http://","")
					i = i.replace("https://","")
					i = i.replace("www.","")
					i = i.split("/")
					i = i[0]
					check(i)
					ip(i)						
		except Exception as e:
			print(e)
			bing(dork)
def check(url):
	pdf = ".pdf"
	string = "." in url
	try:
		file = open(filename,"r").read()
	except:
		open(filename,"w")
		file = open(filename,"r").read()
	if url in file or pdf in url or string == False:
			print(la7mar+" [+] Already Exists: "+url+labyadh)
	else:
		file = open(filename,"a")
		file.write(url+"\n")
		file.close()
		print(la5dhar+" [+] Added: "+url+labyadh)
try:
	print(auth)
	dorks = input(green+" [+] Enter Your Dork List: "+la7mar)
	page1 = input(green+" [+] Page For Bing Dork: "+la7mar)
	page2 = input(green+" [+] Page For IP Dork: "+la7mar)
	filename = input(green+" [+] Save Site List: "+la7mar)
	th = input(green+" [+] How Many Process: "+la7mar)
	dork = open(dorks,"r").readlines()
except Exception as e:
	print(e)
	exit()
try:
	with concurrent.futures.ThreadPoolExecutor(int(th)) as executor:
		executor.map(bing,dork)
except Exception as e:
	print(e)