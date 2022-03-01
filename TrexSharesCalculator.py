from tkinter import *
import datetime
import os
import pickle


# ----------------------- Share Class ----------------------- #
class share:
    time = ""
    date = ""


# ----------------------- Rig data ----------------------- #
RigDict = {}


def addrig(rigName):
    RigDict[rigName] = list()


# ----------------------- Initialization ----------------------- #
mainPath = os.getcwd()
configBuffer = list()
if os.path.exists("SharesData.pkl") and os.path.getsize("SharesData.pkl") > 0:
    f = open("SharesData.pkl", "rb")
    RigDict = pickle.load(f)
    f.close()
if os.path.exists("Config.pkl") and os.path.getsize("Config.pkl") > 0:
    fc = open("Config.pkl", "rb")
    configBuffer = pickle.load(fc)
    path = configBuffer[0]
else:
    path = None
# ----------------------- Time Variables ----------------------- #
now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
# ----------------------- Files reading ----------------------- #

isPath = False


def directory(p):
    global path
    global isPath
    try:
        path = p
        os.chdir(path)
        updateConf()
        isPath = True
    except:
        dirErrorprompt()
        isPath = False


# text file extraction
def read_text_file(file_path):
    with open(file_path, 'r') as f:
        line = f.readlines()
        sharesBuffer = list()
        for item in line:
            if "[ OK ]" in item:
                x = share()
                x.date = (str(item)[:8])
                x.time = (str(item)[9:17])
                sharesBuffer.append(x)
        return sharesBuffer


# iterate over directory
def dirRead():
    for file in os.listdir():
        for j in RigDict:
            if file.startswith(j):
                file_path = f"{path}\{file}"
                templist = read_text_file(file_path)
                RigDict[j].extend(templist)


# ----------------------- GUI Methods ----------------------- #
def updatePath():
    directory(E0.get())


def updateConf():
    T0.configure(state='normal')
    T0.insert(INSERT, "\nCurrent Path: " + path)
    T0.configure(state='disabled')


def dirErrorprompt():
    T0.configure(state='normal')
    T0.insert(INSERT, "\nDirectory was not found")
    T0.configure(state='disabled')


def calculateShares():
    directory(path)
    for j in RigDict:
        RigDict[j] = list()
    dirRead()
    T0.configure(state='normal')
    for j in RigDict:
        T0.insert(INSERT, "\n" + j + " Has " + str(len(RigDict[j])) + " Shares")
    T0.configure(state='disabled')


# ----------------------- GUI Initialization ----------------------- #
# add Rig Window
def addRigWindow():
    def updateTempRigDict():
        addrig(AE0.get())

        T0.insert(INSERT, "\nnew rig has been added to the list")

        AddRigWindow.destroy()

    AddRigWindow = Tk()
    AddRigWindow.title('Add new Rig')
    AddRigWindow.geometry('500x150')

    Label(AddRigWindow, text='Rig Name: ').place(x=10, y=23)
    AE0 = Entry(AddRigWindow, width=49, borderwidth=4)
    AE0.place(x=100, y=25)

    ABa = Button(AddRigWindow, text='add', padx=20, command=updateTempRigDict, borderwidth=4)
    ABa.place(x=417, y=13)

    AddRigWindow.resizable(0, 0)
    AddRigWindow.mainloop()


# Main window
MainWindow = Tk()
MainWindow.title('T-rex Shares Calculator')
MainWindow.geometry('500x550')

Frame(MainWindow, bg="blue").grid(row=0, column=0)

E0 = Entry(MainWindow, width=49, borderwidth=4)
E0.place(x=100, y=25)

Label(MainWindow, text='Directory Path: ').place(x=10, y=23)

Bup = Button(MainWindow, text='update Path', padx=40, pady=5, command=updatePath, borderwidth=4)
Bup.place(x=176, y=60)

Bcs = Button(MainWindow, text='Calculate shares', padx=15, pady=5, command=calculateShares, borderwidth=4)
Bcs.place(x=31, y=130)

Bq = Button(MainWindow, text='Quit', padx=15, pady=5, command=MainWindow.destroy, borderwidth=4)
Bq.place(x=407, y=130)

T0 = Text(MainWindow, width=54, height=16, background="black", foreground="white", borderwidth=6)
T0.place(x=31, y=200)

nR = Button(MainWindow, text='Add New Rig', padx=100, pady=5, command=addRigWindow, borderwidth=4)
nR.place(x=115, y=492)

T0.insert(INSERT, "Current Path is: " + str(path))

if len(RigDict) > 0:
    T0.insert(INSERT, "\nCurrent saved Rigs data: ")
    for i in RigDict:
        T0.insert(INSERT, "\n" + i + " has " + str(len(RigDict[i])) + " Shares")

MainWindow.resizable(0, 0)

MainWindow.mainloop()

# ----------------------- File output ----------------------- #
# [Path]
configBuffer.append(path)

# dump config
os.chdir(mainPath)
fc = open("Config.pkl", "wb")
pickle.dump(configBuffer, fc)
fc.close()

# dump data
f = open("SharesData.pkl", "wb")
pickle.dump(RigDict, f)
f.close()
