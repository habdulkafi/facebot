# facebook-bot

facebook-bot is an easy-to-use companion for your facebook chat bubbles.  The original inspiration came from the `@dailycute` and `@fbchess` bots in the Facebook Messenger app.  I wanted to add more functionality to my facebook conversations and create a companion user that would add to my mobile facebook messenger experience.  

## Usage

Unlike the newly released facebook chatbot stuff, this chat companion is more primitive.  You must run it on a computer of some sort.  We will call this computer the "server" from here on out.  After doing `git clone`, run `python setup.py` to get started.  The bare-minimum requirements for this program is python 2.7 with bs4 and mechanize installed.  pip is the easiest way to get these packages: `pip install bs4` and `pip install mechanize`.  Note: mechanize doesn't work with python 3.x.  To add functionality, you might consider installing [youtube-dl](https://github.com/rg3/youtube-dl/) (`pip install youtube-dl`) and ffmpeg (or avconv).  I tested it with ffmpeg, and found you must have ffmpeg in your path somewhere for some parts to work correctly.  

There are two ways to use this program.  
1) Connect it to your own personal facebook to augment current conversations you have with other people (can be confusing since all the messages will look like they're being sent by your account)
2) Connect it to a fake facebook account and set it up so it's more like a utility to speed things up in a mobile environment. 

If you choose option 1 (and you don't trust your friends), you can set up permissions so that *only you* can start youtube/mp3 downloads.  This will prevent your friends from spamming you and filling up your server.

Here is the current functionality no matter which method you choose.  

- Send `@search <query>`: The server will respond with the top three search results on Google, including the link to the result's page.  It will look like this: 

![search](http://i.imgur.com/D41qMCj.png)
- Send `@image <query>`: The server will respond with links to the top three image results on Google Images. Example:

![image](http://i.imgur.com/FfYKy8V.png)
- Send `@youtube <url>`: The server will download the video found at the youtube link provided.  However, it will not download it to the phone/user.  It will download it to the location the program is running on the server.  This means that if you run this script in a folder that is tracked by a cloud storage service (Dropbox, Onedrive, Mega, etc.), that service will upload the video to the cloud storage and, if you've got your phone connected to that cloud storage, you can watch the video on your phone (either streaming or download).  If you want to allow your friends to start downloads on your server (not recommended), you can answer `yes` when the `setup.py` file asks you.  If you answer `no`, then only you can initiate downloads (may not be the desired functionality when interacting with a fake facebook account).  NOTE: Requires youtube-dl to work!  Example:

![youtube](http://i.imgur.com/v0z3clN.png)
![vid_dl](http://i.imgur.com/WCTVwxw.png)

- Send `@mp3 <url>`:  The server will download the mp3 version of a youtube video, or an mp3 file off of a service like soundcloud.  The same permissions issue applies here as for `@youtube`. NOTE: if you want to get mp3s from youtube videos, you have to have ffmpeg (or avconv) installed and in the path of the server.  Example:
![mp3](http://i.imgur.com/jzx8W3c.png)
![aud_dl](http://i.imgur.com/qHnCyzn.png)

- Send `@joke`: The server will get a random top-25 joke from reddit.com/r/jokes in the past day and send it back.  Example:

![joke](http://i.imgur.com/3hMpG8i.png)

- Bonus:  Send `@science` and the server will respond with a randomly chosen science fact from gathered from tumblr.  Lots of knowledge out there!



