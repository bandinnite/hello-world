import tkinter as tk
import time
root = tk.Tk()
catnip = 0
baby = 0
babyinc = 1
kitten = 0
cat = 0
catlady = 0
bingo = 0
bingofact = 0
china = 0
prestige = 1
cur = 1
can =tk.Canvas(root, width= 100, height = 100)
can.pack()
e = can.create_text(50, 10, text=str(catnip)+' catnip')
def currency():
    global baby
    global babyinc
    global catnip
    global kitten
    global cat
    global catlady
    global bingo
    global bingofact
    global cur
    time.sleep(1)
    baby += (babyinc*prestige)
    catnip += kitten
    kitten += cat
    cat += catlady
    catlady += bingo
    bingo += bingofact
    bingofact += china
    #print baby
    #print catnip
    #print kitten
    #print cat
    cur = 0
#def mother():
    #while (cur == 1):
        #currency()
#mother()
def catnipf():
    global cur
    global catnip
    catnip += 1
    can.itemconfig(e, text=str(catnip)+' catnip')
def kittenf(buyk):
    global catnip
    global kitten
    global baby
    cnnum = catnip/10
    if buyk.get() == 1:
        kitbuy = 1
    elif buyk.get() == 2:
        if cnnum >= baby:
            kitbuy = baby/2
        else:
            kitbuy = cnnum/2
    else :
        if cnnum >= baby:
            kitbuy = baby
        else:
            kitbuy = cnnum
    kitten += 1*kitbuy
    catnip -= 10*kitbuy
    baby -= 1*kitbuy
def catf(buyc):
    global catnip
    global kitten
    global cat
    global baby
    cnnum = catnip/1000
    cnum = kitten/100
    if buyc.get() == 1:
        catbuy = 1
    elif buyc.get() == 2:
        if cnnum >= baby:
            catbuy = baby/2
        else:
            catbuy = cnum/2
    else :
        if cnnum >= baby:
            catbuy = baby
        else:
            catbuy = cnum
    cat += 1*catbuy
    catnip -= 100*catbuy
    kitten -= 10*catbuy
    baby -= 1*catbuy
def catladyf(buyl):
    global cur
    global catnip
    global cat
    global catlady
    global baby
    cnnum = catnip/100000
    cnum = kitten/100
    if buyl.get() == 1:
        catbuy = 1
    elif buyl.get() == 2:
        if cnnum >= baby:
            catbuy = baby/2
        else:
            catbuy = cnum/2
    else :
        if cnnum >= baby:
            catbuy = baby
        else:
            catbuy = cnum
    catlady += 1*catbuy
    catnip -= 100000*catbuy
    cat -= 1000*catbuy
    baby -= 1*catbuy
v = tk.IntVar()
tk.Radiobutton(root, text="buy One", variable=v, value=1).pack(anchor=tk.W)
tk.Radiobutton(root, text="buy Half", variable=v, value=2).pack(anchor=tk.W)
tk.Radiobutton(root, text="buy max", variable=v, value=3).pack(anchor=tk.W)
tk.Button(root, text = 'harvest catnip', command = catnipf).pack()
tk.Button(root, text = 'buy kitten', command = kittenf).pack()
tk.Button(root, text = 'buy cat', command = catf).pack()
tk.Button(root, text = 'buy crazy cat lady', command = catladyf).pack()
root.mainloop()