from tkinter import *
from tkinter import font
from tkinter import messagebox
from tkinter.filedialog import Open
from tkinter.font import BOLD, Font
import time
import math

Start_id = 0
login_accepted = False

# login ui
login = Tk()

Background = Frame(login, bg="#2e2e2e", height=100)
End = Frame(login, bg="#2e2e2e", height=40)
Statusbar = Frame(login, bg="white", height=10)

login_i = Text(Background, fg="white", bg="#3e3e3e", relief=FLAT, height=1, width=40, insertwidth=3, insertofftime=200)
PassCode = "THup325"

def login_whitelist():
    global Encrypt
    global PassCode
    if (login_i.get("1.0", "end-1c") == PassCode or login_accepted == True):
        login.destroy()
    elif (login_i.get("1.0", "end-1c")) == Encrypt(PassCode):
        print("User is tring to use a encrypted auth token")
    else:
        pass

login_l = Label(Background, fg="white", bg="#2e2e2e", text="Please enter your product code below:", pady=30, font=Font(login, family="Century Gothic", weight=BOLD, size=12))
login_btn = Button(Background, fg="white", bg="#2e2e2e", relief=FLAT, activebackground="#2e2e2e", width=30, height=1, text="Login", pady=10, font=Font(login, family="Century Gothic", size=10), command=login_whitelist)

Background.pack(side=TOP, fill=X)
End.pack(side=TOP, fill=X)
login_l.pack(side=TOP)
login_i.pack(side=TOP)
login_btn.pack(side=TOP)
Statusbar.pack(side=TOP, fill=X)

keywords = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890,.;'!@#$%^&*()[]"

def Decrypt(string):
    global keywords 
    newStr = ""
    for letter in string:
        letterPos = str(keywords).find(letter)
        #print(letterPos)
        newLetter = keywords[len(keywords)-letterPos-1]
        #print(letter)
        #print(newLetter)
        newStr += newLetter
    #print(newStr)
    return newStr

def Encrypt(string):
    global keywords   
    newStr = ""
    for letter in string:
        letterPos = str(keywords).find(letter)
        #print(letterPos)
        newLetter = keywords[len(keywords)-letterPos-1]
        #print(letter)
        #print(newLetter)
        newStr += newLetter
    return newStr

def CheckLogin(event=None):
    global login_accepted
    global PassCode
    PassCodeSaved = ""
    fileExists = None
    try:
        fileExists = open("./auth.ini", "r")
        fileExists.close()
    except Exception as e:
        fileExists = False
    else:
        fileExists = True

    # check for auth file
    if (fileExists):
        exisiting_file = open("./auth.ini", "r")
        PassCodeSaved = exisiting_file.read()
        PassCodeSaved = Decrypt(PassCodeSaved)
        exisiting_file.close()

    # auth file does not exist check product code
    if PassCodeSaved == PassCode:
        Statusbar.config(bg="#1eea4a")
        login_accepted = True
    else:
        # check new product code and encrypt it
        if (login_i.get("1.0", "end-1c") == PassCode):
            Statusbar.config(bg="#1eea4a")
            # save passcode
            newfile = open("./auth.ini", "w")
            # encrypt
            PassCode = Encrypt(PassCode)
            newfile.write(PassCode)
            newfile.close()
            login_accepted = True
        else:
            Statusbar.config(bg="#ea1e1e")

def SaveLastClickPos_log(event):
    global lastClickX, lastClickY
    lastClickX = event.x
    lastClickY = event.y

def Dragging_log(event):
    x, y = event.x - lastClickX + login.winfo_x(), event.y - lastClickY + login.winfo_y()
    login.geometry("+%s+%s" % (x , y))

login_l.bind('<Button-1>', SaveLastClickPos_log)
login_l.bind('<B1-Motion>', Dragging_log)
login.bind('<Button-1>', CheckLogin)
login.geometry("400x200+500+100")
login.overrideredirect(True)
login.mainloop()

# initialization
window = Tk()

Canv = None
def Clear_Canvas():
    global window
    global Canv

    Canv.destroy()    
    Canv = Canvas(window, height=1000, width=1000, bg="#2e2e2e", highlightthickness=0, bd=0, relief=RIDGE)
    Scroll1 = Scrollbar(Canv, orient="vertical", bg="#2e2e2e", width=20, command=Canv.yview)
    
    Canv.config(yscrollcommand=Scroll1.set)
    
    Canv.pack(side=LEFT, fill=BOTH)
    Scroll1.pack(side=RIGHT, fill=Y)
    Canv.pack_propagate(0)

def make_draggable(widget):
    widget.bind("<Button-1>", on_drag_start)
    widget.bind("<B1-Motion>", on_drag_motion)

def on_drag_start(event):
    widget = event.widget
    widget._drag_start_x = event.x
    widget._drag_start_y = event.y

def on_drag_motion(event):
    widget = event.widget
    x = widget.winfo_x() - widget._drag_start_x + event.x
    y = widget.winfo_y() - widget._drag_start_y + event.y
    widget.place(x=x, y=y)
    
counter= 1
def Add(whatToAdd):
    global counter
    global Canv
    global Start_id
    if (whatToAdd == "String"):
        Title_Font = Font(Canv, family="Calibri", size=15, weight=BOLD)
        Input_Font = Font(Canv, family="Tahoma", size=10)

        Box = Frame(Canv, height=120, width=200, bg="#1e1e1e")
        Box_Head = Frame(Box, height=30, width=200, bg="#1e1e1e")
        Box_Content = Frame(Box, height=120, width=200, bg="#1e1e1e")
        Title = Label(Box_Head, pady=10, fg="white", bg="#1e1e1e", text=whatToAdd, font=Title_Font, padx=25)
        Close_Button = Button(Box_Head, text="X", takefocus=0, activebackground="#1e1e1e", font=Title_Font, pady=10, fg="red", bg="#1e1e1e", relief=FLAT, command=Box.destroy)
        InputName = Text(Box_Content, fg="white", bg="#3e3e3e", relief=FLAT, font=Input_Font, height=.5, width=15, insertwidth=1, insertofftime=200)
 
        # --- packing --- #
        Box_Head.pack(side=TOP)
        Box_Content.pack(side=TOP)
        Title.pack(side=LEFT)
        Close_Button.pack(side=RIGHT)
        InputName.pack(side=TOP)
        Box.pack(side=LEFT)
        Box.pack_propagate(0)

        make_draggable(Box)
 
# --- Add window --- #
addWindowOpen = False
def OpenBlockWindow():
    global addWindowOpen
    if addWindowOpen == False:
        addWindowOpen = True
        
        addWindow = Tk()

        Title_Font = Font(addWindow, family="Calibri", size=13, weight=BOLD)
        List_Font = Font(addWindow, family="Tahoma", size=11, weight=BOLD)

        def CheckSelected():
            try:
                Selected_Widget = List.get(List.curselection()[0])
            except Exception as e:
                messagebox.showerror("Error", "Please pick a block to be added!")
            else:
                Add(Selected_Widget)

        # --- Window Options --- #
        def destroyWindow():
            global addWindowOpen
            addWindowOpen = False
            addWindow.destroy()

        TitleBar = Frame(addWindow, bg="#3e3e3e", height=50)
        Title_Label = Label(TitleBar, text="Add a Block", fg="white", bg="#3e3e3e", padx=10, font=Title_Font)
        Close = Button(TitleBar, text="x", fg="white", bg="#3e3e3e", relief=FLAT, font=Title_Font, padx=5, command=destroyWindow)
        List = Listbox(addWindow, justify=CENTER, selectmode=SINGLE, width=300, height=10, font=List_Font, fg="white", bg="#3e3e3e", bd=0)
        Insert_Button = Button(addWindow, fg="white", bg="#2e2e2e", text="Insert", relief=FLAT, font=List_Font, command=CheckSelected)

        List.insert(List.size()+1, "String")

        # --- packing --- #
        TitleBar.pack(fill=X)
        Title_Label.pack(side=LEFT)
        Close.pack(side=RIGHT)
        List.pack(side=TOP, fill=X)
        Insert_Button.pack(side=TOP)

        def SaveLastClickPos(event):
            global lastClickX, lastClickY
            lastClickX = event.x
            lastClickY = event.y

        def Dragging(event):
            x, y = event.x - lastClickX + addWindow.winfo_x(), event.y - lastClickY + addWindow.winfo_y()
            addWindow.geometry("+%s+%s" % (x , y))

        addWindow.wm_title("Add Widget")
        addWindow.wm_overrideredirect(True)
        addWindow.config(background="#2e2e2e")
        addWindow.bind('<Button-1>', SaveLastClickPos)
        addWindow.bind('<B1-Motion>', Dragging)
        addWindow.geometry("300x260+"+str(window.winfo_x()+window.winfo_width()+10)+"+"+str(window.winfo_y()))
        addWindow.mainloop()
    else:
        pass

# --- Export it all --- #
def Export():
    file = open("./Exported_Script.lua", "w+")
    Exported_String = "-- This file was created using RVS ---\n\n"
    
    # add all items in a flow method

    """  # get all variables
    loop_counter = 0
    new_counter = 1
    for i in list_widgets["Variables"]:
        loop_counter += 1
        if (loop_counter == 2):
            loop_counter = 0
            continue
        VarName = list_widgets["Variables"]["Variable Name"+str(new_counter)].get("1.0", "end-1c")
        new_counter += 1
        VarValue = list_widgets["Variables"]["Variable Value"+str(new_counter)].get("1.0", "end-1c")
        
        # if not emptystring
        if len(VarName) > 0 and len(VarValue) > 0:
            Exported_String += "local " + VarName + " = " + VarValue + "\n"
        
        new_counter += 1 """

    file.write(Exported_String)
    file.close()

# --- Fonts --- #
Title_Icon_Font = Font(window, family="Calibri", size=13, weight=BOLD)
Title_Font = Font(window, family="Century Gothic", size=15, weight=BOLD)

# --- Main Stuff --- #
def DestroyAllWindows():
    exit(1)

Main_Window = Frame(master=window, height="30", bg="#2e2e2e")
Title_Label = Label(Main_Window, text="RVS - Roblox Visual Scripting", fg="white", bg="#2e2e2e", font=Title_Font, padx=15)
Close_Button = Button(Main_Window, text="x", fg="white", padx=10, bg="#2e2e2e", relief=FLAT, font=Title_Icon_Font, command=DestroyAllWindows)

Middle_Window = Frame(window, bg="#393938", height="30")

Export_Button = Button(Middle_Window, text="Export to Lua", fg="white", bg="#393938", padx=10, relief=FLAT, font=Title_Icon_Font, command=Export)

Add_Widget = Button(Middle_Window, text="Add Block", padx=10, fg="white", bg="#393938", relief=FLAT, font=Title_Icon_Font, command=OpenBlockWindow)

ClearCanvas = Button(Middle_Window, text="Clear Canvas", padx=10, fg="white", bg="#393938", relief=FLAT, font=Title_Icon_Font, command=Clear_Canvas)

Add_Event = Button(Middle_Window, text="Add Event", padx=10, fg="white", bg="#393938", relief=FLAT, font=Title_Icon_Font)

Add_Function = Button(Middle_Window, text="Add Function", padx=10, fg="white", bg="#393938", relief=FLAT, font=Title_Icon_Font)

Canv = Canvas(window, height=1000, bd=0, highlightthickness=0, relief=RIDGE, width=1000, bg="#2e2e2e")

Scroll1 = Scrollbar(Canv, orient="vertical", bg="#2e2e2e", width=20, command=Canv.yview)

Canv.config(yscrollcommand=Scroll1.set)

# --- UI Packing --- #
Main_Window.pack(fill=BOTH)
Close_Button.pack(side=RIGHT)
Title_Label.pack(side=LEFT)

Middle_Window.pack(fill=X)
ClearCanvas.pack(side=LEFT)
Export_Button.pack(side=RIGHT)
Add_Widget.pack(side=LEFT)
Add_Event.pack(side=LEFT)
Add_Function.pack(side=LEFT)
Canv.pack(side=LEFT, fill=BOTH)
Scroll1.pack(side=RIGHT, fill=Y)

Canv.pack_propagate(0)

# --- Window Specs --- #
def SaveLastClickPos(event):
    global lastClickX, lastClickY
    lastClickX = event.x
    lastClickY = event.y

def Dragging(event):
    x, y = event.x - lastClickX + window.winfo_x(), event.y - lastClickY + window.winfo_y()
    window.geometry("+%s+%s" % (x , y))

window.wm_overrideredirect(True)
window.geometry("1000x600+50+100")
window.config(background="#2e2e2e")
Main_Window.bind('<Button-1>', SaveLastClickPos)
Main_Window.bind('<B1-Motion>', Dragging)

# Run it all
window.mainloop()
