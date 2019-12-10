"""
Assistant to draft email
"""

import updater
import pyperclip
import datetime 

firstName=updater.nameArray

myText="Hi mishra,\n\n"+"I hope all is well !\n\n"+"Thanks,\n"+"Prateek"
pyperclip.copy(myText)

#CREATE AND NEW DATE AND TIME
# now = datetime.datetime.now() 

#WRITE DATE AND TIME TO THE LOG
# with open("log.py", "w") as f1:        
    # f1.writelines(now.strftime("%Y-%m-%d %H:%M:%S")
