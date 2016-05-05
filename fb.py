import mechanize
import bs4
import time
import re
import random
import json
import subprocess
import sys

with open("tumblr_links.txt","rb") as f:
	links = f.read().split("\n")


# email="filler@example.com"
# password="password"
# chatName="First Last-Name"
execfile("config")

browser = mechanize.Browser()
browser.set_handle_robots(False)
cookies = mechanize.CookieJar()
browser.set_cookiejar(cookies)
browser.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36')]
browser.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)


url = "https://m.facebook.com/"
browser.open(url)
browser.select_form(nr = 0)
browser.form['email'] = email
browser.form['pass'] = password
response = browser.submit()

m_page = browser.open("https://m.facebook.com/messages")
m_soup = bs4.BeautifulSoup(m_page.read())
tid = m_soup(text=chatName)[0].parent.get('href')
fbmsgurl = "https://m.facebook.com" + tid



def google(search_string):
	brg = mechanize.Browser()
	brg.set_handle_robots( False )
	brg.addheaders = [('User-agent', 'Mozilla/5.0 (Linux; Android 5.0.2; HTC One_M8 Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.48 Mobile Safari/537.36')]
	brg.open( "http://google.com" )
	brg.select_form(nr=0)
	brg["q"]=search_string
	responseg = brg.submit()
	soupg = bs4.BeautifulSoup(responseg.read())
	return [x.text + "\n" + list(x.find("h3",{"class","r"}).children)[0].get("href") for x in soupg.find_all("div",{"class":"g card-section"})]

def google_image(search_string):
	brg = mechanize.Browser()
	brg.set_handle_robots( False )
	brg.addheaders = [('User-agent', 'Mozilla/5.0 (Linux; Android 5.0.2; HTC One_M8 Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.48 Mobile Safari/537.36')]
	brg.open( "http://www.images.google.com" )
	brg.select_form(nr=0)
	brg["q"]=search_string
	responseg = brg.submit()
	soupg = bs4.BeautifulSoup(responseg.read())
	meta_data = [json.loads(x.text) for x in soupg.find_all("div",{"class":"rg_meta"})]
	return [x['ou'] for x in meta_data]


def message(send_string,brf):
	brf.open(fbmsgurl)
	brf.select_form(nr=1)
	brf["body"] = send_string
	browser.submit()

def main():
	r = browser.open(fbmsgurl)
	soup = bs4.BeautifulSoup(r)
	a = list(list(soup.find_all("div",{"id":"messageGroup"})[0].children)[1].children)[-1]
	if "@search" in a.text:
		string = a.find_all("span")[0].text.replace("@search ","")
		print "google search: ", string
		b = google(string)[0:3]
		b.reverse()
		for ss in b:
			ss = ''.join([i if ord(i) < 128 else ' ' for i in ss])
			message(ss,browser)	
	if "@image" in a.text:
		string = a.find_all("span")[0].text.replace("@image ","")
		print "image search: ", string
		b = google_image(string)[0:3]
		for ss in b:
			message(ss,browser)
	if "@science" in a.text:
		print "fake science"
		message(random.choice(links),browser)
	if "@youtube" in a.text:
		string = a.find_all("span")[0].text.replace("@youtube ","").encode('ascii','ignore')
		print "youtube download: ", string
		p = subprocess.Popen(['youtube-dl',"-f", "mp4", string],stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
		print p.stdout.read()
		message("Your video is being downloaded!",browser)
	if "@mp3" in a.text:
		string = a.find_all("span")[0].text.replace("@mp3 ","").encode('ascii','ignore')
		print "mp3 download: ", string
		p = subprocess.Popen(['youtube-dl',"-x", "--audio-format", "mp3", string],stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
		print p.stdout.read()
		message("Your audio is being downloaded!",browser)
	if "@help" in a.text:
		to_send = "Welcome to the Facebook chat companion!  This is the help page.\n" \
					"***To perform a Google search, send `@search <query>` and you'll get the top 3 results \n"\
					"***To perform a Google image search, send `@image <query>` and you'll get the top 3 results\n "\
					"***To get a random science fact, send `@science` \n" \
					"***To download a youtube video, send `@youtube <url>` \n" \
					"***To download an mp3 file from lots of websites (e.g. youtube, soundcloud), "\
					"send `@mp3 <url>` (not guaranteed to work)"
		message(to_send, browser)
		message("----end help----",browser)
		time.sleep(.5)


while True:
	main()
	time.sleep(.5)
