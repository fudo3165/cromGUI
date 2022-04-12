#-------------------------------
import tkinter as tk
from tkinter import *
import os
#-------------------------------
bashrcc = ('/root/.bashrc')
#bashrcc = ('text.txt')
doptext = ('#CROM COMMAND!')
#-------------------------------
os.system('clear')
#------BACKUP-------------------
folder_dop = os.path.exists('dop')
if(folder_dop == True):
    d4 = True
else:
    os.system('mkdir dop')


file_back = os.path.isfile(f'dop/.bashrc')
if(file_back == True):
    d3 = True
else:
    els = tk.Tk()
    els.title('?')
    els.geometry('300x300')
    els.resizable(width=FALSE,height=FALSE)
    els['bg']='white'

    #=======================================

    def els_yes():
        file_backup = open(bashrcc, 'r')
        backup1 = file_backup.read()
        dop = open(f'dop/.bashrc', 'w')
        dop.write(backup1)
        dop.close()
        file_backup.close()
        els.destroy()

    def els_no():
        els.destroy()

    #=======================================

    text=tk.Label(text='Create return file?', bg='white').place(x=0, y=0, width=300, height=240)

    els_yes_otv = tk.Button(els, text='Yes', bg='white', command=els_yes).place(x=0, y=240, width=150, height=60)
    els_no_otv = tk.Button(els, text='No', bg='white', command=els_no).place(x=150, y=240, width=150, height=60)

    els.mainloop()


#------BACKUP-------------------

main = tk.Tk()
main.geometry("400x500")
main.resizable(width=FALSE, height=FALSE)
main.title('Crom')
main['bg'] = 'white'

#--------------------------------

def getTextInput():
    otv = os.path.isfile(bashrcc)

    if(otv == True):

        result=textExample.get(1.0, tk.END+"-1c")
        res=name.get(1.0, tk.END+"-1c")
        co = (f'alias {res}="{result}" ')

        wr = open(bashrcc, 'a')
        wr.write(f'\n{doptext}\n')
        wr.write(f'{co}')
        wr.write(f'\n{doptext}\n')

        wr.close()
        textExample.delete("1.0","end")
        name.delete("1.0","end")
        ok()

    else:
        er()

def ok():
    ok = tk.Tk()
    ok.title('successfully')
    ok.resizable(width=FALSE, height=FALSE)
    ok.geometry('250x60')

    text = tk.Label(ok, text='The operation was successful', bg='white', fg='green').place(x=0, y=0,width=250, height=35)
    des = tk.Button(ok, text='Ok', bg='white', command=ok.destroy).place(x=0, y=30, width=250, height=30)

    ok.mainloop()


def er():
    er = tk.Tk()
    er.title('Not successful')
    er.resizable(width=FALSE, height=FALSE)
    er.geometry('250x60')

    text = tk.Label(er, text='Error!', bg='white', fg='red').place(x=0, y=0,width=250, height=35)
    des = tk.Button(er, text='Ok', bg='white', command=er.destroy).place(x=0, y=30, width=250, height=30)

    er.mainloop()

def hand():
    os.system('nano ~/.bashrc')

def save():

    save=tk.Tk()
    save.title('?')
    save.resizable(width=FALSE,height=FALSE)
    save.geometry('300x250')
    save['bg']='white'

    def savee():
        os.system('shutdown -r now')

    def savee_destroy():
        save.destroy()

    text = tk.Label(save, text='Your computer will restart. You are sure?', bg='white').place(x=0,y=0,width=300,height=190)
    yes = tk.Button(save, text='Yes', bg='white', command=savee).place(x=0,y=190,width=150, height=60)
    no = tk.Button(save, text='No', bg='white', command=savee_destroy).place(x=150,y=190,width=150, height=60)

    save.mainloop()

def back():

    #===============================================
    def start_backup():
        backk.destroy()
        file_backup = open(bashrcc, 'w')
        dop = open(f'dop/.bashrc', 'r')
        dop_file = dop.read()
        file_backup.write(dop_file)
        dop.close()
        file_backup.close()
        ok()
    #===============================================


    backk = tk.Tk()
    backk.title('Restore?')
    backk.resizable(width=FALSE, height=FALSE)
    backk.geometry('300x150')
    backk['bg'] = 'white'
    text = tk.Label(backk, text='All new commands will be deleted!', bg='white').place(x=0, y=0, width=300, height=40)

    yes = tk.Button(backk, text='yes', bg='white', command=start_backup ).place(x=0,y=100, width=150, height=50)
    no = tk.Button(backk, text='no', bg='white', command=backk.destroy).place(x=150,y=100, width=150, height=50)

    backk.mainloop()

#--------------------------------

text1 = tk.Label(text='New command name', bg='white').place(x=0, y=0, width=400, height=30)
text2 = tk.Label(text='Command', bg='white').place(x=0, y=84, width=400, height=30)

textExample=tk.Text(main, height=10)
name=tk.Text(main, height=10)
btnRead=tk.Button(main, height=1, width=10, text="Add", command=getTextInput, bg='white')

h = tk.Button(main, text='Manually', bg='white', fg='green', command=hand)
b = tk.Button(main, text='Restore', bg='white', fg='green', command=back)
s = tk.Button(main, text='Save', bg='white', fg='green', command=save)



#---------------------------------

textExample.place(x=0, y=116, width=400, height=210)
btnRead.place(x=0,y=450, width=400, height=50)
name.place(x=0,y=32, width=400, height=50)
h.place(x=0, y=408, width=133.33, height=40)
b.place(x=133.33, y=408, width=133.33, height=40)
s.place(x=266.66, y=408, width=133.33, height=40)

#---------------------------------

main.mainloop()

#---------------------------------
