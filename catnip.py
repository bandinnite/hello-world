import time
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
def mother():
    while (cur == 1):
        currency()
mother()
def catnip():
    global cur
    global catnip
    catnip += 1
    cur = 1
def kitten(buyk):
    global catnip
    global kitten
    global baby
    kitten += 1*buyk
    catnip -= 10*buyk
    baby -= 1*buyk
def cat(buyc):
    global catnip
    global kitten
    global cat
    global baby
    cat += 1*buyc
    catnip -= 100*buyc
    kitten -= 10*buyc
    baby -= 1*buyc
def catlady(buyl):
    global cur
    global catnip
    global cat
    global catlady
    global baby
    catlady += 1*buyl
    catnip -= 10000*buyl
    cat -= 100*buyl
    baby -= 1*buyl
