#output to file with export button


#show button
#Put this inside a daily notes, button to add a hd call then do below
#stucks needs
#more func

import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from datetime import datetime 

top = tk.Tk()

top.title("Notes")


currentdate = datetime.now()
cdate = currentdate.strftime("%m/%d/%Y %H:%M")
# top.geometry('500x300')
tk.Label(top,text="Daily Stuff Tracker\n").grid(row=0,column=3)
tk.Label(top,text=":.:.:.:.:.:").grid(row=0,column=5)

#daily stuff area

tk.Label(top,text="Things did").grid(row=1,column=2)
stuffDid = scrolledtext.ScrolledText(top,wrap=tk.WORD,width=20,height=9)
stuffDid.grid(row=2,column=2)


##Needs area

tk.Label(top,text="Stucks/Needs").grid(row=1,column=4)

needs = scrolledtext.ScrolledText(top,wrap=tk.WORD,width=18,height=9)
needs.grid(row=2,column=4)




phoneList = []

#creates the add a call window
def newphoneWindow():
    callbackbox = tk.BooleanVar()
    #gets the entry field information and appends it to the phoneList
    def addtolist():
        global phoneList
          
        name1=nvar.get()
        email1=email.get()
        phoneNumber1=phoneNumber.get()
        website1=website.get()
        callBack1 = callbackbox.get()
        
        notes1=notes.get()
        
        phoneList.append({'name':name1,'email':email1,'phone':phoneNumber1,'website':website1,'callback':callBack1,'notes':notes1,'timestamp': cdate})
        #runs the function to update the table
        insert_table(callTv)

        #closes the window
        phoneWindow.destroy()
    
    phoneWindow = tk.Toplevel(top)
    #Labels
    phoneWindow.title("Add a Call")
    
    
    tk.Label(phoneWindow,text='Name').grid(row=0)
    tk.Label(phoneWindow,text='Email Address').grid(row=1)
    tk.Label(phoneWindow,text="Phone number").grid(row=2)
    tk.Label(phoneWindow,text="WebSite").grid(row=3)
    
   
    
    tk.Label(phoneWindow, text='Notes').grid(row=5)
    
    #checkbox
    callBack = tk.Checkbutton(phoneWindow,text='Call Back?',variable=callbackbox)
    
    
    #Entries
    nvar=tk.StringVar()
    name=tk.Entry(phoneWindow,textvariable=nvar)
    name.grid(row=0,column=1)
    
    email=tk.Entry(phoneWindow)
    email.grid(row=1,column=1)
    
    phoneNumber = tk.Entry(phoneWindow)
    phoneNumber.grid(row=2,column=1)
    
    website = tk.Entry(phoneWindow)
    website.grid(row=3,column=1)
    
    callBack.grid(row=2,column=2)
    
    notes = tk.Entry(phoneWindow)
    notes.grid(row=5,column=1)
    #buttons in the child window and runs the commands on click
    buttonExit= tk.Button(phoneWindow,text="Exit",command=phoneWindow.destroy)
    buttonExit.grid(row=15,column=2)
    
    buttonAdd= tk.Button(phoneWindow,text="Add",command=addtolist)
    buttonAdd.grid(row=15,column=3)
    

#updates the table 
def insert_table(t):
    o = len(phoneList) -1
    t.insert(parent='',index=o,iid=o,values=(phoneList[o]['name'],phoneList[o]['email'],phoneList[o]['phone'],phoneList[o]['website'],phoneList[o]['callback'],phoneList[o]['notes'],phoneList[o]['timestamp']))

#creates the table Need to rename numbers 
callTv= ttk.Treeview(top,column=(1,2,3,4,5,6,7,),show='headings',height=8)
callTv.column(1, anchor='center',width=80)
callTv.column(2, anchor='center',width=100)
callTv.column(3, anchor='center',width=90)
callTv.column(4, anchor='center',width=80)
callTv.column(5, anchor='center',width=55)
callTv.column(6, anchor='center',width=80)
callTv.column(7, anchor='center',width=80)
callTv.grid(row=2,column=6)


#Table headers
callTv.heading(1, text='Name')
callTv.heading(2, text='Email')
callTv.heading(3, text='Phone')
callTv.heading(4, text='WebSite')
callTv.heading(5, text='CallBack')
callTv.heading(6, text='Notes')
callTv.heading(7, text='TimeStamp')


#Above the table
tk.Label(top,text='Calls').grid(row=1,column=6)



#buttons in the main window
addAcallButton= tk.Button(top,text="Add a Call",command=newphoneWindow)
addAcallButton.grid(row=15,column=3)

buttonExit= tk.Button(top,text="Exit",command=top.destroy)
buttonExit.grid(row=15,column=5)



top.mainloop()





















