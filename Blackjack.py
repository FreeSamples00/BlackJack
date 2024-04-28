# ------------------------
# goal?
# messages showing what actions were taken (hit, stay, etc.)
# two aces = 22, no bust FIX
# ------------------------

#-----Imports-----
import turtle, os, random

#-----Variables-----

#Row locations for cards
Px = -200
Py = -95
Dx = -200
Dy = -5

done_bet = False
firstbar = False
bet_input = True

fontype = 'dejavusansmono'

font35 = fontype,'35','bold'
font15 = fontype,'15','bold'
font20 = fontype,'20','bold'
font30 = fontype,'30','bold'

#starting money
currentM = 200

started = False

over = False

bet = 10
betchange = 10

centerx = -100
centery = -50

pens = []

#screen
wn = turtle.Screen()
wn.colormode(255)
wn.bgcolor(0,129,2)
wn.mode('world')
wn.setworldcoordinates(-200,-100,0,0)

#lists image filenames
IMAGES = ["IMAGES/" + f for f in os.listdir("IMAGES")]

#fliplist
flipped = []
for i in range(52):
  flipped.append("False")

#------GUI Functions------

def changebetchange(direction):
  global betchange
  if direction == 'up':
    if betchange == 1:
      betchange = 10
    elif betchange == 10:
      betchange = 20
    elif betchange == 20:
      betchange = 50
  if direction == 'down':
    if betchange == 50:
      betchange = 20
    elif betchange == 20:
      betchange = 10
    elif betchange == 10:
      betchange = 1

  
#write stuff
def write(message,x,y,size,alignment,tortle):
  wn.tracer(False)
  pens[tortle].goto(x,y)
  if alignment == 'c':
    pens[tortle].write(message, font=(fontype,size,'bold'), align=('center'))
  elif alignment == 'l':
    pens[tortle].write(message, font=(fontype,size,'bold'), align=('left'))
  elif alignment == 'r':
    pens[tortle].write(message, font=(fontype,size,'bold'), align=('right'))
  wn.tracer(True)

#searches images for the card by number, returns the filename
def search(number):
  if number == 0:
    iter = 0
    suit = "Red"
  if (number >= 1) and (number <= 13):
    suit = "Club"
    iter = 0
  if (number >= 14) and (number <= 26):
    suit = "Spade"
    iter = 1
  if (number >= 27) and (number <= 39):
    suit = "Diamond"
    iter = 2
  if (number >= 40) and (number <= 53):
    suit = "Heart"
    iter = 3
  number = number - 13*iter
  return(search2(suit,number))

def search2(suit,number):
  found = False
  numbed = (" " + str(number) + ".")
  for i in IMAGES:
    if suit in i:
      if numbed in i:
        found = True
        ind = IMAGES.index(i)
        #print(suit + "  " + str(number))
        return(str(i))
  if found == False:
    print('ERROR 404, "' + suit + '" and "' + str(number) + '" not found')
  
#changes the image of a card
def reshape(turtnum,cardind):
  turtle = search(cardind)
  wn.addshape(turtle)
  turtles[turtnum].shape(turtle)

#deals a card to a location
def GUIdeal(cardnum,x,y,fliped):
  global dflipped
  cardnum = int(cardnum) - 1
  wn.tracer(False)
  turtles[cardnum] = turtle.Turtle()
  turtles[cardnum].penup()
  if fliped == "t":
    cardnum2 = cardnum + 1
    flip(cardnum2)
    dflipped = cardnum2
  else:
    reshape(cardnum,cardnum+1)
  turtles[cardnum].speed(3)
  wn.tracer(True)
  turtles[cardnum].goto(x,y)


#fliperoonie
def flip(cardnum):
  num = cardnum - 1
  if flipped[num] == "True":
    reshape(num,cardnum)
    flipped[num] = "False"
  elif flipped[num] == "False":
    turtle = "IMAGES/Back Red 2.gif"
    wn.addshape(turtle)
    turtles[num].shape(turtle)
    flipped[num] = "True"

#disp money
def printmoney():
  global currentM
  wn.tracer(False)
  wallet.clear()
  wallet.write("Wallet: $" + str(currentM), font=(font15))
  wn.tracer(True)


#disp bet
def printbet():
  global bet
  wn.tracer(False)
  bett.clear()
  bett.write("Bet: $" + str(bet), font=(font15))
  wn.tracer(True)

#Edit Bet
def changebet(change):
  global bet, bet_input, currentM, betchange
  if bet_input == True:
    modulo = currentM % 10
    if change == 'pos':
      bet += betchange
    else:
      if modulo != 0:
        if bet == currentM:
          bet -= modulo
        else:
          bet -= betchange
      else:
        bet -= betchange
    if bet < 0:
      bet = 0
    elif bet > currentM:
      bet = currentM
    printbet()

#stops bet editing
def donebet():
  global bet_input, can_hit, bet, currentM, done_bet
  if (bet <= currentM) and (bet > 0) and (done_bet == False):
    currentM -= bet
    printmoney()
    bet_input = False
    pen.clear()
    Ddeal('t')
    Ddeal('f')
    write("Dealer's Cards",Dx,Dy + 12,15,'c',0)
    Pdeal()
    Pdeal()
    write("Player's Cards",Px,Py + 12, 15,'c',0)
    can_hit = True
    done_bet = True

#all cards face up
def faceup():
  flip(dflipped)
  global Dsum, Dx, Dy
  wn.tracer(False)
  if Dsum == 0:
    write("BUST!",Dx + 15,Dy - 4,20,'l',0)
  if Dsum == 21:
    write("BLACKJACK!",Dx + 15,Dy - 4,20,'l',0)
  wn.tracer(True)

#-----Game Functions-----

#set deck and variables
def shuffle():

  collectcards()
  #set variables
  global Psum, Dsum, Pjack, Pbust, Phistory, Dhistory, Daceused, Paceused, Paces, Daces, doubled, Pdone, Ddone, can_hit, bet_input, done_bet

  done_bet = False
  bet_input = True
  can_hit = False
  Ddone = False
  doubled = False
  Daces = 0
  Paces = 0
  Daceused = 0
  Paceused = 0
  Pbust = False
  Pjack = False
  Pdone = False
  Psum = 0
  Dsum = 0
  Phistory = []
  Dhistory = []

  #Setup cardlist Numbers (cardsN)
  global cardsN
  with open('CardsNum.txt', 'r') as f:
      cards0 = f.readlines()
  cardsN = []
  for element in cards0:
    cardsN.append(element.strip())

  #Setup cardlist Words (cardsW)
  global cardsW
  with open('CardsWord.txt', 'r') as f:
      cards00 = f.readlines()
  cardsW = []
  for element in cards00:
    cardsW.append(element.strip())

  #Setup Cardlist for tracking (cardsP)
  global cardsP
  with open('1-52.txt', 'r') as f:
    cards000 = f.readlines()
  cardsP = []
  for element in cards000:
    cardsP.append(element.strip())
  

#PLAYER deal
Phistory = []
def Pdeal():
  global cardsP, Phistory, Paces, Psum, Px, Py
  dealt = -2
  while int(dealt) == -2:
    dealt = random.choice(cardsP)
    dealt = int(dealt)
    dealt = dealt - 1
    if (dealt == 0) or (dealt == 13) or (dealt == 26) or (dealt == 39):
      Paces = Paces + 1
    if dealt != -2:
      Phistory.append(dealt)
      GUIdeal(cardsP[dealt],Px,Py,'f')
      Px += 12
      Psum = int(cardsN[dealt]) + Psum
      cardsP[dealt] = -1

#DEALER deal
Dhistory = []
def Ddeal(fliped):
  global Ddealt, Dx, Daces, cardsP, Dhistory
  Ddealt = -2
  while int(Ddealt) == -2:
    Ddealt = random.choice(cardsP)
    Ddealt = int(Ddealt)
    Ddealt = Ddealt - 1
    if (Ddealt == 0) or (Ddealt == 13) or (Ddealt == 26) or (Ddealt == 39):
      Daces = Daces + 1
    if Ddealt != -2:
      global Dsum
      Dhistory.append(Ddealt)
      Dsum = int(cardsN[Ddealt]) + Dsum
      GUIdeal(cardsP[Ddealt],Dx,Dy,fliped)
      Dx += 12
      cardsP[Ddealt] = -1

#hit
def hit():
  global Psum, can_hit, Pjack, Pbust, Pdone, Paceused
  if can_hit == True:
    Pdeal()
    can_hit = False
    for i in range(Paces):
      for i in Phistory:
        if (i == 0) or (i == 13) or (i == 26) or (i == 39):
          if Psum > 21:
            if Paceused < Paces:
              Psum = Psum - 10
              Paceused = Paceused + 1
    if Psum == 21:
      Pjack = True
      Pdone = True
      write("BLACKJACK!",Px + 15, Py - 4,20,'l',0)
    if Psum > 21:
      Pbust = True
      Pdone = True
      write("BUST!",Px + 15, Py - 4,20,'l',0)
      Psum = 0
    Ddecision()

#stay
def stay():
  global can_hit, Pdone
  Pdone = True
  can_hit = False
  Ddecision()
      
#double down    
def doubledown():
  global Psum, Phistory, bet, currentM, can_hit, doubled, Pdone
  if len(Phistory) == 2:
    if (Psum > 8) and (Psum < 12):
      if bet <= currentM:
        currentM -= bet
        bet = bet * 2
        Pdeal()
        can_hit = False
        doubled = True
        Pdone = True
        Ddecision()

#dealer makes choices
def Ddecision():
  global Dsum, can_hit, doubled, Ddone, Daceused, Daces, Dx, Dy
  if Dsum < 17:
    if Ddone == False:
      Ddeal(1)
    for i in Dhistory:
      if (i == 0) or (i == 13) or (i == 26) or (i == 39):
        if Dsum > 21:
          if Daces > Daceused:
            Dsum = Dsum - 10
            Daceused = Daceused + 1  
    if Dsum > 21:
      Dsum = 0
      Ddone = True
    if Dsum > 16:
      Ddone = True
  while (Pdone == True) and (Ddone == False):
    if Dsum < 17:
      if Ddone == False:
        Ddeal(1)
    for i in Dhistory:
      if (i == 0) or (i == 13) or (i == 26) or (i == 39):
        if Dsum > 21:
          if Daces > Daceused:
            Dsum = Dsum - 10
            Daceused = Daceused + 1  
    if Dsum > 21:
      Dsum = 0
      Ddone = True
    if Dsum > 16:
      Ddone = True
  if Pdone == False:
    can_hit = True
  if (Ddone == True) and (Pdone == True):
    faceup()
    scoring()

#scores
def scoring():
  global Dsum, Psum, bet, currentM, started, over
  if (Psum == Dsum):
    if Psum > 0:
      write("PUSH!",centerx,centery,35,'c',0)
      currentM += bet
    else:
      write("YOU LOST!",centerx,centery,35,'c',0)
  else:
    if Psum == 21:
      write("BLACKJACK!",centerx,centery,35,'c',0)
      currentM += (bet + (bet * 1.5))
      currentM = int(currentM)
    else:
      if Psum > Dsum:
        write("YOU WON!",centerx,centery,35,'c',0)
        currentM += bet * 2
      if Psum < Dsum:
        write("YOU LOST!",centerx,centery,35,'c',0)
  printmoney()
  print()
  print("Dealer: " + str(Dsum))
  print("Player: " + str(Psum))
  bet = 10
  started = False
  controls('cont')
  if currentM == 0:
    over = True

#spacebar
def spacebar():
  global bet_input, started, over, currentM, firstbar
  if over == True:
    if firstbar == False:
      wn.tracer(False)
      pen.clear()
      write("GAME OVER!",centerx,centery,35,'c',0)
      write("TRY AGAIN?",centerx,-62,30,'c',0)
      controls('loss')
      wn.tracer(True)
      firstbar = True
    if firstbar == True:
      currentM = 200
      over = False
      firstbar = False
  elif started == False:
    running_the_thing()
    controls('betting')
  elif (started == True) and (bet_input == False):
    hit()
  elif bet_input == True:
    donebet()
    controls('playing')

#escape
def escape():
  exit()

#tooltips
def controls(stage):
  wn.tracer(False)
  tx = -300
  ty = -90
  deltaty = 7
  fsize = 10
  tooltip.clear()
  if stage == 'betting':
    write("Increase Bet: Up Arrow",tx,ty,fsize,'l',1)
    ty -= deltaty
    write("Decrease Bet: Down Arrow",tx,ty,fsize,'l',1)
    ty -= deltaty
    write("Enter Bet: Spacebar",tx,ty,fsize,'l',1)
  if stage == 'playing':
    write("Hit: Spacebar",tx,ty,fsize,'l',1)
    ty -= deltaty
    write("Stay: Alt Key",tx,ty,fsize,'l',1)
    ty -= deltaty
    write("Double Down: Control Key",tx,ty,fsize,'l',1)
  if stage == 'loss':
    write("Exit: Escape",tx,ty,fsize,'l',1)
    ty -= deltaty
    write("Restart: Spacebar",tx,ty,fsize,'l',1)
  if stage == 'cont':
    write("Continue: Spacebar",tx,ty,fsize,'l',1)
  wn.tracer(True)

# ----Setup-----

#one turtle spot per card
turtles = []
for i in range(52):
  turtles.append('0')


def collectcards():
  global turtles, Dx, Px
  Dx = -200
  Px = -200
  for i in range(52):
    if turtles[i] != '0':
      turtles[i].speed(5)
      turtles[i].goto(0,0)
      turtles[i].hideturtle()
      x = turtles[i]
      turtles[i] = '0'
      del x
  

#turtle to represent deck
def deckcover():
  coverim = "IMAGES/Back Red 2.gif"
  wn.addshape(coverim)
  cover = turtle.Turtle(shape=coverim)
  cover.penup()
  cover.showturtle()

#-pens
#bet
bett = turtle.Turtle()
bett.hideturtle()
bett.penup()
bett.speed(0)
bett.goto(-300,-40)


#money
wallet = turtle.Turtle()
wallet.hideturtle()
wallet.penup()
wallet.speed(0)
wallet.goto(-300,-30)

#pen
pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.speed(0)

tooltip = turtle.Turtle()
tooltip.speed(0)
tooltip.hideturtle()
tooltip.penup()
tooltip.goto(-300,-80)

pens.append(pen)
pens.append(tooltip)
pens.append(bett)
pens.append(wallet)

#----Calls----

write("Press Space to Start",centerx,centery,35,'c',0)


def running_the_thing():
  global started
  if started == False:
    started = True
    pen.clear()
    write("BETTING",centerx,centery,35,'c',0)
    deckcover()
    shuffle()
    printmoney()
    printbet()

#----Keypresses----
#controls:
# continue: space
# hit: space
# confirm bet: space
# change bet: up/down arrows
# stay: alt keys
# doubledown: ctrl keys
# escape: exit
# change degree of change bet: left/right arrows


wn.listen()

wn.onkeypress(lambda: changebet('pos'), 'Up')
wn.onkeypress(lambda: changebet('neg'), 'Down')
wn.onkeypress(stay, 'Alt_R')
wn.onkeypress(stay, 'Alt_L')
wn.onkeypress(doubledown, 'Control_L')
wn.onkeypress(doubledown, 'Control_R')
wn.onkeypress(spacebar, 'space')
wn.onkeypress(escape, 'Escape')
wn.onkeypress(lambda: changebetchange('down'), 'Left')
wn.onkeypress(lambda: changebetchange('up'), 'Right')

wn.mainloop()