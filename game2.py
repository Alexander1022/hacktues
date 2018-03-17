#! python
import sys
import time
print("Time Machine 0.0.1 beta")
print("LOADING")
print("")
def progbar(curr, total, full_progbar):
    frac = curr/total
    filled_progbar = round(frac*full_progbar)
    time.sleep(0.1)
    print('\r', '#'*filled_progbar + '-'*(full_progbar-filled_progbar), '[{:>7.2%}]'.format(frac), end='')

for i in range(0, 105, 5):
    progbar(i,100, 20)
print()
print()
name=input("WRITE YOUR NAME:")
print("HI",name)
for i in "-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-":
    print(i,end='')
    time.sleep(0.01)
print()
sex=input("girl or boy : ")
print()
input("press ENTER to continue!")
print("YOU WALK THROUGH THE FOREST AND FIND A TIME MACHINE")
for i in "▀ ▄ ▀ ▄ ▀ ▄ ▀ ▄ ▀ ▄ ▀ ▄ ▀ ▄ ▀ ▄ ▀ ▄ ▀ ▄ ▀ ▄ ▀ ▄ ▀ ▄ ▀ ▄ ▀ ▄ ▀ ▄ ":
    print(i,end='')
    time.sleep(0.02)
print("")
for c in "DO YOU WANT TO ENTER IN IT??!":
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(0.1)

a=input("yes OR no:");
if a == ("yes"):
    print("GREAT!!!")
elif a == ("no"):
    print("GOODBYE my",sex)
    exit()
else:
    print("WHAT ARE YOU GONNA DO THEN?!?")
    print()
    exit()
ww=int(input("WHICH WORLD WAR YOU WANNA GO?!? (1/2) : "));
if ww == 1:
    input("WHAT VEHICLE DO YOU WANT TO USE - CAR or PLANE : ")
    print("ACTUALLY,THERE ARE NOT ANY VEHICLES ON THAT TIME")

elif ww == 2:
    print("WOW.good")
    az=input("Do you want fun fact? (yes/no) : ");
    if az ==("yes"):
        print ("""In 1941, more than 3 million cars were manufactured in the US.
              Only 139 more were made during the entire war.""")
    if az==("no"):
        print("ooh,okey")

else:
    print("What the ......?!?")
    exit()
            
print("")
for i in "UNFORTUNATELY THE TIME MACHINE IS BROKEN":
    print(i,end='')
    time.sleep(0.1)
print()

for c in "NOW,YOU MUST PLAY IT, ":
    sys.stdout.write(c)
    sys.stdout.flush()  
    time.sleep(0.1)
print("THAT IS GOING TO BE INTERESTING!!! :)")

print("YOU HAVE LIFE AND ARMOR")
for c in "YOU MUST CHOOSE ONE ":
    sys.stdout.write(c)
    sys.stdout.flush()  
    time.sleep(0.1)
action=input("shield OR armor:");
if action == ("shield"):
    print("YOOO,YOU HAVE PROTECTION,",sex)
elif action == "armor":
    print("YOUR BODY IS PROTECTED")

else:
    print("YOU ARE DEAD!!!")
    exit()
 
input("PRESS ENTER TO JOIN THE WAR")
print("There are some soldiers,",name)
for c in "THEY ARE GOING TO FIND A GUN FOR YOU,MAYBE A SNIPER RIFLE?!?":
    sys.stdout.write(c)
    sys.stdout.flush()  
    time.sleep(0.1)
print("")  
string = """
⌐╦╦═─   .

⌐╦╦═─        .

⌐╦╦═─             .

⌐╦╦═─                  .

⌐╦╦═─                      .

⌐╦╦═─                          .

⌐╦╦═─                             .

⌐╦╦═─                                .

⌐╦╦═─                                   .
                                                                          
"""



print("")
for line in string.splitlines():
    print(line)
    time.sleep(0.08)
    
print("EXCELLENT,YOU MADE IT")
for c in "YOU ALMOST KILLED THEM ":
    sys.stdout.write(c)
    sys.stdout.flush()  
    time.sleep(0.1)

print()

print("GOOD JOB,",sex)
for c in "BUT THE MACHINE IS FIXED":
    sys.stdout.write(c)
    sys.stdout.flush()  
    time.sleep(0.1)

print()

for c in " FOR NOW ;) ":
    sys.stdout.write(c)
    sys.stdout.flush()  
    time.sleep(0.1)
print("")
b=input("Do you want to meet Napoleon??!? (yes/no)");
if b==("yes"):
    print("YEAH,",sex)
else:
    print("ooh,okey")
    print()

x=input("DO YOU WANT TO GO INTO THE BATTLE IN VATERLO WITH HIM (yes/no)");
if x == ("yes"):
    print("LET'S GO")
elif x == ("no"):
    print("WHY ARE SO FEARFUL")
else:
    print("WHAT?!")

print()

question = input("DO YOU WANT A INTERESTING FACT?!? (yes/no): ");
if question == ("yes"):
    print("NAPOLEON’S ARMY DISCOVERED THE ROSETTA STONE.")
elif question == ("no"):
    print("YOU ARE SO UNLOVING!!!")
else:
    print("Wrong answer,!,",sex)

print()

string = """ :) :) :) :) """
for line in string.splitlines():
    print(line)
    time.sleep(0.5)

op = input("Do you want to go in the Elizabeth 1 time?!? (yes/no) ");
if op == ("yes"):
    print ("SHE IS WAITING YOU!!")
elif op == ("no"):
    print("OH,YOU DONT WANT TO GO ANYWHERE :( ")
else: ("Wrong answer!!!")

print()

string = """ANYWAY!"""
for line in string.splitlines():
    print(line)
    time.sleep(0.4)
print()

zz = input("DO YOU WANT TO HEAR A INTERESTING FACT ABOUT ELIZABETH 1 (ok/no way) ")
if zz == ("ok"):
    print("ACTUALLY,she could speak many languages.")
elif zz == ("no way"):
    print("whyyy??!? you dont want to study!!")
else: ("OK,NEVERMIND.....")

print()

string = """TIME FOR SMALL QUIZ!!!"""
for line in string.splitlines():
    print(line)
    time.sleep(0.8)

print()


print("LOADING...")
def progbar(curr, total, full_progbar):
    frac = curr/total
    filled_progbar = round(frac*full_progbar)
    time.sleep(0.1)
    print('\r', '#'*filled_progbar + '-'*(full_progbar-filled_progbar), '[{:>7.2%}]'.format(frac), end='')

for i in range(0, 105, 5):
    progbar(i,100, 20)

xso = int(input("WHICH YEAR BULGARIA WAS MADE?!? : "));
if xso == 681:
    print("CORRECT!!",name)
else: print("SILLY")

print()

bg = int(input("How many times Bulgaria has lost flag in a battle?!? : "))
if bg == 0:
    print("Bravo!",name)
else:
    print("Wrong. The Bulgarian army has never lost a single flag in battle.")

print()

bg1 = int(input("How many percents of Bulgaria is covered with forests?!? = 33 ,66 or 99 : "))
if bg1 == 33:
    print("Yep")
elif bg1 ==66:
    print("Nope. Nearly one third of Bulgaria is covered with forests.")
elif bg1 == 99:
    print("Nope. Nearly one third of Bulgaria is covered with forests.")
else:
    print("NOT THE RIGHT ANSWER")

print()

input("PRESS ENTER TO CONTINUE")

print()

print("OKEY,AFTER THIS SMALL QUIZ,IT'S TIME FOR THE TIME MACHINE...",name)

print("LOADING OBJECTS")
def progbar(curr, total, full_progbar):
    frac = curr/total
    filled_progbar = round(frac*full_progbar)
    time.sleep(0.1)
    print('\r', '#'*filled_progbar + '-'*(full_progbar-filled_progbar), '[{:>7.2%}]'.format(frac), end='')

for i in range(0, 105, 5):
    progbar(i,100, 20)

print()

print("The machine is fixed and you can travel somewhere.. ")

string = """ But you can return only in Renaissance or in the New Time!"""
for line in string.splitlines():
    print(line)
    time.sleep(0.5)

hey = input("YOU CHOOSE : Renaissance or the New Time (r/nt) :");
if hey == ("r"):
    print("let's go my",sex)
elif hey ==("nt"):
    print("Something went wrong..")
    print("You are going to go to the Renaissance")
else:
    print("NO")
    

print("YOU CAN FLIGHT WITH Leonardo da Vinci WITH HIS PARAGLIDER")
leo=input("Do you want to flight type yes or no (yes/no) : ");
if leo == ("yes"):
    print("MAYBE YOU WILL FALL DOWN AND BREAK A LEG")
    for i in "JUST KIDDING!":
        print(i,end='')
    time.sleep(0.2)
elif leo == ("no"):
    print("you don't want to do anything! :( ")
    for i in "YOU ARE SO LAZY":
        print(i,end='')
    time.sleep(0.2)
else:
    print("bye")
    exit()
print("===================================================")
print("THE MACHINE WAS FIXED")
zd=input("DO YOU WANNA GO TO THE PRESENT?!(yes/no) : ");
if zd == ("yes"):
    print("But first! WE MUST GO OT CREATOR IF ELSYS")
    print("Stela is waiting for you")
elif zd == ("no"):
    print("GAME OVER")
    exit()
else:
    print("YOU WANT!!! X( ")

print("YOU GONNA GO TO THE DATE OF THE CREATION OF ELSYS!")

for i in "✖✖✖✖✖✖✖✖✖✖✖✖✖✖✖✖✖✖✖✖✖✖✖✖✖✖✖✖✖✖✖✖":
    print(i,end='')
    time.sleep(0.001)
print("soon will be the end of this game")
for i in "( ͡ಥ ͜ʖ ͡ಥ) ":
    print(i,end='')
    time.sleep(0.07)

print()

print("YOU ARE IN FRONT OF ELSYS")

print()

print("NOW STELA IS WAVING AT YOU")

print()

for i in "WE ARE BACK IN 1988":
    print(i,end='')
    time.sleep(0.001)

print()

print("Here it is an interesting fact:")

for i in "THAT SCHOOL IS PART FROM Cisco Systems Bulgaria":
    print(i,end='')
    time.sleep(0.001)

print()

for i in "THIS SMALL PYTHON GAME WAS MADE BY STUDENTS FROM ELSYS TEAM SYSTEM BUG":
    print(i,end='')
    time.sleep(0.001)

print()

for i in "AND BECAUSE THE SUBJECT WHICH WE CHOOSE IS Digital past,WE ARE GOING TO DO A REAL HISTORY TEST":
    print(i,end='')
    time.sleep(0.001)

print()

for i in "✖✖✖✖✖✖✖✖✖✖✖✖✖✖✖✖✖✖✖✖✖✖✖✖✖✖✖✖✖✖✖✖✖✖✖✖✖✖✖✖✖✖✖✖✖✖✖✖✖":
    print(i,end='')
    time.sleep(0.02)

print()

csar = input("In the time of which king Bulgaria was on three seas?: (a) Khan Krum /b) Khan Kubrat /c) Tsar Simeon The Great : ");
if csar == ("a"):
    print("Wrong! The correct answer is c)")
elif csar == ("b"):
    print("Wrong!The correct answer is c)")
elif csar == ("c"):
    print("Right,you know it!")
else:
    print("NO")

print()

bul = input("Which lord managed Bulgaria for the longest period of time?!? : a) Tsar Simeon /b) Tsar Peter /c) Knyaz Boris : ");
if bul == ("a"):
    print("Wrong! The correct answer is b)")
elif bul == ("b"):
    print("Correct!")
elif bul == ("c"):
    print("Wrong! The correct answer is b)")
else:
    print("NO")

print()

turnovo = input("When was the First Turnovo Uprising??! /a) 1598 /b) 1689 /c) 1988 : ");
if turnovo == ("a"):
    print("Correct!")
elif turnovo == ("b"):
    print("Wrong! The correct answer is a)")
elif turnovo == ("c"):
    print("Wrong! The correct answer is a)")
else:
    print("NO")

print()

bukvar = input("When was the Fish Primer written?!? /a) 1824 /b) 1789 /c) 1834 : ");
if bukvar == ("a"):
    print("Right!")
elif bukvar == ("b"):
    print("Wrong! The correct answer is a)")
elif bukvar == ("c"):
    print("Wrong! The correct answer is a)")
else:
    print("NO")

print()

istoria = input("Who was the first human who has rewritten the Slav-Bulgarian History for the first time!?? /a) Paisii Hilendarski /b) Ivan Vazov /c) Sofroniy Vrachanksi :");
if istoria == ("a"):
    print("Wrong! The correct answer is c)")
elif istoria == ("b"):
    print("Wrong! The correct answer is c)")
elif istoria == ("c"):
    print("Correct!")
else:
    print("NO")

print()

newhistory = input("Which event in the new Bulgarian history connects the date 22 September 1908?!? /a) the beggining of the Balkan War /b)the proclamation of the independence of Bulgaria /c) unification of Eastern Rumelia with the Principality of Bulgaria : ");
if newhistory == ("a"):
    print("Wrong! The correct answer is b)")
elif newhistory == ("b"):
    print("Correct!")
elif newhistory == ("c"):
    print("Wrong! The correct answer is b)")
else:
    print("NO")

print("✖✖✖✖✖✖✖✖✖✖✖✖✖✖✖✖✖✖✖✖✖✖✖✖✖✖✖✖✖✖✖✖✖✖✖✖✖✖")


from tkinter import *
from random import *

def do_event(event):
    print("{},{}".format(event.x,event.y))

def jump(event):
    app.hello_b.place(relx=random(),rely=random())

class App:
    def __init__(self,master):
        frame = Frame(master)
        master.geometry("1280x720")
        master.title("My first program!")
        master.bind("<Button-1>",do_event)
        master.bind("<Button-1>",do_event)
        frame.pack()

        self.hello_b = Button(master,text="thank you!",command=sys.exit)
        self.hello_b.bind("<Enter>",jump)
        self.hello_b.pack()




root = Tk()

app = App(root)

root.mainloop()
