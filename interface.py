import sys,re
import indexer

db = indexer.indexer()
DEBUG = ("-debug" in sys.argv)
#apps = db.load()
apps = ["1", "apple", "apple-II", "app", "Apple-III", "app4", "app5",
"app6","app7","app8","app9","app10"]

#searches the existing list of items 
def search(s):
	results = [];
	if(DEBUG):
		print ("INFO: searching for \"" + s + "\" in known apps.")
	resultsbox.delete(0, END)
	
	#crappy linear search
	for i in apps:
		#regex match
		result = re.search(r'(.*)'+s.lower()+'(.*?)',i.lower())
		#if result and (hardcoded limit) is <= 5
		if result and len(results) < 10:
			results.append(i)
			resultsbox.insert(END, i)
    
#gui stuff    
from Tkinter import *
master = Tk()
master.title("Legwork Launcher")

#sets geometry of window based on percentage of pixels
w = master.winfo_screenwidth()
h = master.winfo_screenheight()
#width x height + offset + offset
master.geometry(str(int(w * .4)) + "x" + str(int(h * .15)) +
"+"+str(int(w *.3))+"+"+str(int(h * .375)))
del w
del h

#search field
searchInput = Entry(master)
searchInput.pack(fill=BOTH,expand=1)
searchInput.focus_set()

#key up event for search field
def keyUp(key):
	if key.char and key.keycode != 23:
		s = str(searchInput.get() + key.char)
		search(s)

#custom bind event for when a key is pressed
searchInput.bind("<Key>", keyUp)

#resultsbox on select
def resultSelect(key):
	if(DEBUG): print "INFO: resultsbox key pressed " + str(key.keycode)
	if key.keycode == 36 or str(key.keycode) == "??":
		#TODO: launch application here...
		print resultsbox.get(ACTIVE)

#results table
resultsbox = Listbox(master)
resultsbox.pack(fill=BOTH, expand=1)
resultsbox.bind("<Key>", resultSelect)
resultsbox.bind("<Double-Button-1>", resultSelect)

mainloop()
