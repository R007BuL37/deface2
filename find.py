import requests
from os import system,chdir,mkdir
from time import sleep
import concurrent.futures
la7mar  = '\033[91m'
la5dhar = '\033[92m'
labyadh = '\033[00m'
green = "\033[0;32m"
red = '\033[31m'
r = '\033[31m'
g = '\033[32m'
y = '\033[33m'
b = '\033[34m'
m = '\033[35m'
c = '\033[36m'
w = '\033[37m'
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
print(auth)
try:
	target = open("dashboard.txt","r").readlines()
except:
	print("dashboard.txt missing")
	exit()
site = input(green+" [+] Enter You Site List: "+la7mar)
site = site.replace(site.split("/")[-1],"")
def scan(x):
	try:
		st = x.strip()
		headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
		req = requests.get(site+"/"+st,headers=headers,timeout=10,allow_redirects=False)
		if req.status_code == 200:
			print(g+"[+] "+w+site+"/"+st+g+" |"+r+" "+g+str(req.status_code)+g+" | "+r+"length: "+g+str(len(req.text)))
		elif 200<req.status_code and req.status_code<400:
			print(m+"[+] "+g+site+"/"+st+g+" |"+r+" "+g+str(req.status_code)+g+" | "+r+"length: "+g+str(len(req.text)))
		else:
			print(r+"[+] "+r+site+"/"+st+g+" |"+r+" "+g+str(req.status_code)+g+" | "+r+"length: "+g+str(len(req.text)))
	except Exception as e:
		#print(r+" [+] Failed: "+site)
		print(e)
try:
	with concurrent.futures.ThreadPoolExecutor(10) as executor:
		executor.map(scan,target)
except Exception as e:
	print(e)
print(green+" [+] All Site Scanned Successful [+]")