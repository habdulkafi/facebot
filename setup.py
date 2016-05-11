#
# Husam Abdul-Kafi
# 05/11/16
#

import sys
import os
import readline
try:
	import mechanize
	import bs4
except:
	print "mechanize and bs4 must be installed.  \n" \
	"--- pip install mechanize\n" \
	"--- pip install bs4\n" \
	"--- sudo pip install youtube-dl"
	sys.exit()




print "Welcome to the facebot!"
print "To use this program, you will need a Facebook account that does NOT have \n" \
		"two-factor authentication enabled.  \n" \
		"To start out, you will need to enter your exact name on Facebook, the \n" \
		"email address associated with your account, and your password. Don't \n" \
		"worry, I promise there's no way for me to find out your password.  \n" \
		"You'll also need to enter the name of the chat conversation this bot \n" \
		"is going to be connected to.  Basically, if it's a group conversation,\n" \
		"then you gotta put the full name of that conversation that you see on\n" \
		"Facebook. If it's an individual person, then their name (as it appears \n" \
		"on Facebook) is what you need to enter. NOTE: The chat conversation\n" \
		"must first *exist* before setting this up! \n"\
		"Sometimes, you don't want your conversation partner to start downloads \n" \
		"to your server without your permission.  If you don't want this, answer `no` \n"\
		"to the `permission preference` question.  Otherwise, answer `yes`.\n"


name = raw_input("----Enter your Name (exactly): ")
print "\n"
email = raw_input("----Enter your Email Address: ")
print "\n"
password = raw_input("----Enter your password: ")
print "\n"
chatname = raw_input("----Enter the chat name: ")
print "\n"
pref = raw_input("----Enter your permission preference [yes/no]: ")
print "\n"
confirm = raw_input("To confirm, type y if the following is correct: \n"\
		"Name: " + name + "\nEmail: " + email + "\nPassword: " + password + "\nChatname: " \
		+ chatname + "\nPreference: " + pref + "\n[y/n]:")
print "\n"
if confirm != 'y':
	print "Exiting"
	sys.exit()

with open('config','wb') as f:
	f.write('email="' + email + '"\n')
	f.write('password="' + password + '"\n')
	f.write('chatName="' + chatname + '"\n')
	f.write('pref="' + pref + '"\n')
	f.write('name="' + name + '"\n')

status = os.system('which youtube-dl')

if status:
	print "NOTE: the youtube video functionality won't work without youtube-dl.  Install it using `pip install youtube-dl`"

status = os.system('which ffmpeg')
if status:
	print "NOTE: to download mp3s from youtube videos, you need both youtube-dl and ffmpeg (or avconv).  Good luck with that!\n" \
			"(but you can probably download non-youtube mp3s just fine)"

print "you're all set up now!  run `python fb.py` to get started!"


