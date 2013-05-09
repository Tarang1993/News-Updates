# Author: Tarang Patel
# Email : tarangrockr@gmail.com,

#!/usr/bin/python

import urllib
import urllib2
import xml.dom.minidom
from Tkinter import *
from xml.dom import minidom
from ScrolledText import ScrolledText

def ShowNews():
	url = "http://news.prlog.org/in/rss.xml"
        u = urllib2.urlopen(url)
        xml = minidom.parse(u)
        title= []
	description=[]
        for element in xml.getElementsByTagName('title'):
		title.append(element.firstChild.nodeValue)
        for element in xml.getElementsByTagName('description'):
 		description.append(element.firstChild.nodeValue)
		val = ''
        for i in range(len(title)):
		val = val + '========  ' + title[i] + '  ========'
                val = val + '\n'
                val = val + '\n'
                val = val + 'Details: ' + description[i]
                val = val + '\n'
                val = val + '\n'
        return val

news = ShowNews()       
root = Tk()
root.title("Latest News update!")
News = ScrolledText(root, height = 50 , width = 190)

News.insert(INSERT,news)
News.pack()
root.mainloop()
