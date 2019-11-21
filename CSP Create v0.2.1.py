import Tkinter as tk
import time
root = tk.Tk()
root.wm_title('Dungeon Explorer')
editor = tk.Text(root, width=75)
editor.grid(column=0, row=0, columnspan=3)
w = tk.Canvas(root, width=200, height=387, background='#F0F0F0')
w.grid(column=3, row=0, columnspan=1)
healthbar = w.create_polygon(0,0,0,24,200,24,200,0, fill='#00FF00')
ehealthbar = w.create_polygon(0,24,0,48,200,48,200,24, fill='#FF0000')
phb=w.create_text((110,12), text='100/100')
ehb=w.create_text((110,36), text='100/100')
gold = 0
go=w.create_text((110,60), text=str(gold))
pmhp = 100
php = 100
patk = 10
preg = 20
parm = 5
emhp = 100
ehp = 100
eatk = 20
earm = 0 
edead = 0
pdead = 0
turn = 0
lvl = 1
gold = 0
enemy = 'rat'
def status():
    global w
    global php
    blug = int((200*php)/pmhp)
    blag = int((200*ehp)/emhp)
    w.coords(healthbar, (0,0,0,24,blug,24,blug,0))
    w.coords(ehealthbar, (0,24,0,48,blag,48,blag,24))
    w.itemconfig(phb, text = str(php)+'/'+str(pmhp))
    w.itemconfig(ehb, text = str(ehp)+'/'+str(emhp))
def pattack():
    global turn
    if turn == 1:
        global ehp
        ehp -= (patk - earm)
        turn = 0
        status()
        eturn()
def pheal():
    global turn
    if turn == 1:
        global php
        php = php + preg
        if php >= pmhp:
            php = pmhp
        turn = 0
        status()
        eturn()
def eturn():
    time.sleep(1)
    global php
    global edead
    global turn
    global ehp
    global gold
    global lvl
    if ehp <= 0:
        edead = 1
        editor.delete(1.0, tk.END)
        editor.insert(tk.END, 'the enemy has now died\n')
        golde = (lvl*100)
        gold =+ golde
        w.itemconfig(go, text=str(gold))
        editor.insert(tk.END, str(golde)+' gold\n')
        ehp = 0
        turn = 0
        php = pmhp
        status()
    if edead == 0:
        time.sleep(1)
        editor.insert(tk.END,  str(enemy)+' attacks for '+str(eatk)+'\n'+'you blocked '+str(parm)+' damage\n')
        editor.see(tk.END)
        php -= (eatk-parm)
        if php <= 0:
            editor.insert(tk.END, 'YOU DIED!!!!, GAME OVER\n')
            php = 0
            status()
        else:
            turn = 1
            status()       
def buttona():
    if turn == 1:
        editor.insert(tk.END, 'you attack for '+str(patk)+'\n')
        editor.see(tk.END)
        pattack()
def buttonh():
    if turn == 1:
        editor.insert(tk.END, 'you heal for '+str(preg)+'\n')
        editor.see(tk.END)
        pheal()
selnew = 0
selsho = 0
selstat = 0
def buttonn():
    global lvl
    global edead
    if edead == 1 and selnew == 1:
        global emhp
        global selnew
        global ehp 
        global eatk
        global earm
        global turn
        emhp = 100*lvl*.1
        ehp = 100*lvl*.1
        eatk = 20*lvl*.1
        earm = 5*lvl*.1
        edead = 0
        turn = 1
        selnew = 0
        editor.insert(tk.END, '\n')
        status()
    else:
        editor.insert(tk.END, 'please choose the level you would like to play\n using the up/down arrows \n please note that higher levels are significantly harder\n if you are not leveled high enough\n')
        editor.see
        if edead == 1:
            selnew = 1
shosel = 0
def buttons():
    global shosel
    if shosel == 0:
        shosel = 1
    if shosel == 1:
        shosel = 0
        if selstat == 0:
            global pmhp
        selstatus()
def selstatus():
    if selstat == 0:
        editor.insert(tk.END, 'max health')
    if selstat == 1:
        editor.insert(tk.END, 'attack')
    if selstat == 2:
        editor.insert(tk.END, 'armor')
    if selstat == 3:
        editor.insert(tk.END, 'health regen')
    editor.see
def buttonu():
    global selstat
    if selnew ==1:
        global lvl
        lvl += 1
        editor.insert(tk.END, str(lvl)+'  ')
        editor.see
    if shosel ==1 and selstat < 4:
        selstat += 1
        selstatus()
def buttond():
    global selstat
    if selnew ==1:
        global lvl
        lvl -= 1
        editor.insert(tk.END, str(lvl)+'  ')
        editor.see
    if shosel ==1 and selstat > 0:
        selstat -= 1
        selstatus()
def start():
    global selnew
    global edead 
    selnew = 1
    edead = 1
    selnew = 1
    global pmhp
    global php
    global patk
    global preg
    global parm
    global emhp
    global ehp 
    global eatk
    global earm
    global turn
    global lvl
    pmhp = 100
    php = 100
    patk = 100
    preg = 20
    parm = 5
    lvl = 5
    buttonn()
    editor.insert(tk.END, 'your health is '+str(php)+'\n')
    editor.insert(tk.END, 'your maximum health is '+str(pmhp)+'\n')
    editor.insert(tk.END, 'your attack is '+str(patk)+'\n')
    editor.insert(tk.END, 'your health regeneration is '+str(preg)+'\n')
    editor.insert(tk.END, 'your armour is '+str(parm)+'\n')
    editor.insert(tk.END, 'the '+enemy+' health is '+str(ehp)+'\n')
    editor.insert(tk.END, 'the '+enemy+' max health is '+str(emhp)+'\n')
    editor.insert(tk.END, 'the '+enemy+' attack is '+str(eatk)+'\n')
    editor.insert(tk.END, 'the '+enemy+' armour is '+str(earm)+'\n')
    editor.see
    turn = 1
start()
button0 = tk.Button(root, width=15,bg='#FF9090', height=6, text=('attack'), 
                command=buttona)
button0.grid(row=1, column=0)
button1 = tk.Button(root, width=15,bg='#90FF90', height=6, text = ('heal'), 
                command=buttonh)
button1.grid(row=1, column=1)
button2 = tk.Button(root, width=15,bg='#FFFF90', height=6, text=('new enemy'), 
                command=buttonn)
button2.grid(row=1, column=2)
button3 = tk.Button(root, width=15,bg='#9090FF', height=6, text=('store'), 
                command=buttons)
button3.grid(row=1, column=3)
button4 = tk.Button(root, width=5,bg='#909090', height=2, text=('up'), 
                command=buttonu)
button4.grid(row=0, column=4)
button5 = tk.Button(root, width=5,bg='#909090', height=2, text=('down'), 
                command=buttond)
button5.grid(row=1, column=4)
root.mainloop()