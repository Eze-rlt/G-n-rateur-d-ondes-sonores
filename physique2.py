from time import sleep
from tkinter import*
from threading import Thread
from winsound import Beep

def fermer(event=None):
    root.destroy()

def deplacement(event=None):
    x_souris, y_souris = root.winfo_pointerxy()
    x_souris-=175
    y_souris-=40

    if x_souris > root.winfo_screenwidth()-350:
        x_souris = root.winfo_screenwidth()-350
    elif x_souris < 0:
        x_souris = 0
    
    if y_souris > root.winfo_screenheight()-80:
        y_souris = root.winfo_screenheight()-80
    elif y_souris < 0:
        y_souris = 0
    
    root.geometry(f"350x80+{round(x_souris)}+{round(y_souris)}")

def modify_label(nbe: int) -> None:
    nbe = str(nbe)[::-1]
    nbe2 = str()

    for x in range(len(nbe)):
        
        if x%3 == 0 and x>0:
            nbe2=' '+nbe2
        
        nbe2=nbe[x]+nbe2
        

    var_frequence.set(nbe2+' Hz')

def pause(event):
    global var_pause
    if var_pause:
        var_pause = False
    else:
        var_pause = True

def beep_start():
    global fin, var_pause
    frequence = 100
    duree = 500#int(input('Quel est la durée (en ms) ? '))
    while frequence < 32000:#REPETE JUSQU'A CE QUE LA FReQUENCE ATTEINDE 32000
        if fin:
            break
        elif var_pause:
            sleep(0.5)
            print('pause')
            continue
            
        Beep(frequence, duree)#CREE LE BIP
        frequence+=100#AJOUTE UN CERTAIN NOMBRE à LA FREQUENCE
        try:
            modify_label(frequence)
        except:
            pass

fin=False
var_pause = False
root = Tk()
root.config(bg='blue')
root.overrideredirect(True)
root.attributes("-topmost", True)

var_frequence = StringVar(value='100 Hz')
deplacement()

label_frequence = Label(root, textvariable=var_frequence, bg='blue', fg='white', font=('', 55))
label_frequence.pack(expand=YES)

root.bind('<space>', pause)
root.bind('<B1-Motion>', deplacement)
root.bind('<Escape>', fermer)

Thread(target=beep_start).start()

root.mainloop()
fin = True