from urllib import request
from os import system,chdir,mkdir
from time import sleep
import concurrent.futures
la7mar  = '\033[91m'
la5dhar = '\033[92m'
labyadh = '\033[00m'
green = "\033[0;32m"
red = '\033[31m'
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
def saved(x,y):
	i = x
	i = i.replace("http://","")
	i = i.replace("https://","")
	i = i.replace("www.","")
	i = i.split("/")
	i = i[0]
	try:
		m = open(y,"r").read()
	except:
		open(y,"w")
		m = open(y,"r").read()
	if i in m:
		#print(la7mar+" [+] Already Exists: "+x)
		pass
	else:
		open(y,"a").write(x+"\n")
try:
	target = open("dir.txt","r").readlines()
except:
	target = ["upload.php","kcfinder/browse.php","assets/ckeditor/kcfinder/browse.php","assets/libs/kcfinder/browse.php","panel/kcfinder/upload.php","wp-admin/setup-config.php","wp-admin/install.php","admin/index.php","admin/login.php","administrator/index.php","user/login"]
site = input(green+" [+] Enter You Site List: "+la7mar)
th = input(green+" [+] How Many Speed: "+la7mar)
try:
	opn = open(site,"r").readlines()
except:
	print(la7mar+"\n\n [!] Failed To Open List")
	quit()
try:
	chdir("Result/")
except:
	mkdir("Result")
	chdir("Result/")
def scan(x):
	try:
		for dork in target:
			try:
				dork = dork.strip()
				st = x.strip()
				headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
				r = request.Request("http://"+st+"/"+dork,None,headers=headers)
				r = request.urlopen(r,timeout=10)
				ripon = r.read().decode("utf-8")
				meurl = "http://"+st+"/"+dork
				valid = ripon.lower()
				valid = valid.replace('"','\'')
				rip = "<form" in valid
				rip2 = "type='file'" in valid
				bypasss = True
				if "<title>WordPress &rsaquo; Installation</title>" in ripon and rip == True:
					print(g+" - "+w+meurl+c+" ---> "+w+"Wp-Install"+g+" YES!"+w)
					saved(meurl,"wp-install.txt")
					break
				elif 'name="wp-submit"' in ripon:
					bypasss = False
					print(g+" - "+w+meurl+c+" ---> "+w+"Wordpress Site"+g+" YES!"+w)
					saved(st,"Wordpress.txt")
				elif "OpenCart" in ripon and "admin/index.php?route=common/login" in ripon:
					bypasss = False
					print(g+" - "+w+meurl+c+" ---> "+w+"Opencart"+g+" YES!"+w)
					saved(st,"Opencart.txt")
				elif '/sites/default/files' in ripon:
					bypasss = False
					print(g+" - "+w+meurl+c+" ---> "+w+"Drupal"+g+" YES!"+w)
					saved(st,"Durpal.txt")
				elif 'value="com_login"' in ripon and 'Joomla' in ripon:
					bypasss = False
					print(g+" - "+w+meurl+c+" ---> "+w+"Joomla Site"+g+" YES!"+w)
					saved(st,"Joomla.txt")
				elif  "<title>WordPress &rsaquo; Installation</title>" in ripon and rip == False:
					bypasss = False
					print(g+" - "+w+meurl+c+" ---> "+w+"Wordpress Site"+g+" YES!"+w)
					saved(st,"Wordpress.txt")
				elif '<title>WordPress &rsaquo; Setup Configuration File</title>' in ripon:
					print(g+" - "+w+meurl+c+" ---> "+w+"Wp-Setup"+g+" YES!"+w)
					saved(meurl,"wp-setup.txt")
					break
				elif bypasss == True and rip == True and "type='password'" in valid:
					print(g+" - "+w+meurl+c+" ---> "+w+"Admin-Panel"+g+" YES!"+w)
					saved(meurl,"admin-panel.txt")
					break
				elif rip == True and rip2 == True:
					print(g+" - "+w+meurl+c+" ---> "+w+"Uploader"+g+" YES!"+w)
					saved(meurl,"upload.txt")
				elif "<title>KCFinder: /files</title>" in ripon or "kc_CKEditor" in ripon or "kcact:upload" in ripon:
					print(g+" - "+w+meurl+c+" ---> "+w+"Kcfinder"+g+" YES!"+w)
					saved(meurl,"kcfinder.txt")
					break
				else:
					print(red+" - "+w+meurl+c+" ---> "+w+"CMS-Exploit"+red+" NO!"+w)
					#continue
			except Exception as e:
				print(red+" - "+w+x.strip()+c+" ---> "+w+"Exploit Path"+red+" NO!"+w)
	except Exception as e:
		print(e)
		print(red+" - "+w+x.strip()+c+" ---> "+w+"Shell"+red+" NO!"+w)
try:
	with concurrent.futures.ThreadPoolExecutor(int(th)) as executor:
		executor.map(scan,opn)
except Exception as e:
	print(e)
print(green+" [+] All Site Scanned Successful [+]")