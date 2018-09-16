#Connect 4 Game against Computer
aa = [" "," "," "," "," "," "," "]
bb = [" "," "," "," "," "," "," "]
cc = [" "," "," "," "," "," "," "]
dd = [" "," "," "," "," "," "," "]
ee = [" "," "," "," "," "," "," "]
ff = [" "," "," "," "," "," "," "]

print "Welcome to Connect 4!"
from time import sleep
sleep(0.5)
import random
a = random.randint(1,2)
user =0
comp =0
print "In order to play, you must tell me the column number you want to put your token in."
sleep(0.5)
print "For example, the leftmost column is 1 and the rightmost column is 7"
print""
sleep(0.5)
if a==1:
    user = "X"
    comp = "O"
    print "You are X. You go first."
else:
    user = "O"
    comp = "X"
    print "You are O. You go first."
print ""
spaces = [1,2,3,4,5,6,7]
winvaruser = 0
winvarcomp = 0
import random
import os
import subprocess
########################################## Basic Functions ##################################
def checkSpaces():
    for i in spaces:
        if aa[i-1]!=" " and bb[i-1]!=" " and cc[i-1]!=" " and dd[i-1]!=" " and ee[i-1]!=" " and ff[i-1]!= " ":
            spaces.remove(i)
def some_move(column,user):
    index = column-1
    if ff[index]!=" ":
        if ee[index]!=" ":
            if dd[index]!=" ":
                if cc[index]!=" ":
                    if bb[index]!=" ":
                        aa[index]= user
                    else:
                        bb[index]=user
                else:
                    cc[index]=user
            else:
                dd[index]=user
        else:
            ee[index]=user
    else:
        ff[index]=user
def checkInp1():
	inp1 = str(raw_input("Enter your slot: "))
	try:
		inp1 = int(inp1)
		if inp1 not in spaces:
			print "Please enter correctly."
			inp1 = checkInp1()
	except:
		print "Please enter correctly."
		inp1 = checkInp1()
	finally:
		return inp1
def reset():
    aa = [" "," "," "," "," "," "," "]
    bb = [" "," "," "," "," "," "," "]
    cc = [" "," "," "," "," "," "," "]
    dd = [" "," "," "," "," "," "," "]
    ee = [" "," "," "," "," "," "," "]
    ff = [" "," "," "," "," "," "," "]
    spaces = [1,2,3,4,5,6,7]
    winvaruser = 0
    winvarcomp = 0
########################################## Check For Win ####################################
def checkVert():
    flag = 0
    for i in range(0,7):
        if aa[i]==bb[i]==cc[i]==dd[i]!=" ":
            flag = 1
            break
        elif bb[i]==cc[i]==dd[i]==ee[i]!=" ":
            flag = 1
            break
        elif cc[i]==dd[i]==ee[i]==ff[i]!=" ":
            flag = 1
            break

    return flag
def checkHoriz1(aa):
    flag = 0
    for i in range(0,4):
        if aa[i]==aa[i+1]==aa[i+2]==aa[i+3]!=" ":
            flag = 1
            break
    return flag
def checkHoriz():
    flag = 0
    list1 = [checkHoriz1(aa),checkHoriz1(bb),checkHoriz1(cc),checkHoriz1(dd),checkHoriz1(ee),checkHoriz1(ff)]
    for i in list1:
        if i == 1:
            flag = 1
            break
    return flag

def checkDiag1(aa,bb,cc,dd):
    flag = 0
    var = 6
    for i in range(0,4):
        if aa[i]==bb[i+1]==cc[i+2]==dd[i+3]!=" ":
            flag = 1
            break
    while var>2:
        if aa[var]==bb[var-1]==cc[var-2]==dd[var-3]!=" ":
            flag = 1
            break
        var-=1
    
    return flag
def checkDiag():
    flag = 0
    lista = [checkDiag1(aa,bb,cc,dd),checkDiag1(bb,cc,dd,ee),checkDiag1(cc,dd,ee,ff)]
    for i in lista:
        if i == 1:
            flag = 1
            break
    return flag
def checkWin():
    flag = 0
    lista = [checkDiag(), checkHoriz(), checkVert()]
    for i in lista:
        if i == 1:
            flag =1
            break
    return flag



########################## Artificial Intelligence Part 1: Checking for Block ###################

def aicheckVert():
    flag = 0
    for i in range(0,7):
        if ff[i]==ee[i]==dd[i]==user and cc[i]== " ":
            flag = i+1
            break
        elif ee[i]==dd[i]==cc[i]==user and bb[i] == " ":
            flag = i+1
            break
        elif dd[i]==cc[i]==bb[i]==user and aa[i] == " ":
            flag = i+1
            break
    return flag
def aicheckHoriz():
    flag = 0
    for i in range(0,4):
        if ff[i]==ff[i+1]==ff[i+2]==user and ff[i+3]==" ":
            flag = i+4
            break
        elif ff[i]==ff[i+2]==ff[i+3]== user and ff[i+1]==" ":
            flag = i+2
            break
        elif ff[i]==ff[i+1]==ff[i+3]==user and ff[i+2]==" ":
            flag = i+3
            break
        elif ff[i+1]==ff[i+2]==ff[i+3]==user and ff[i]==" ":
            flag = i+1
            break
        elif ee[i]==ee[i+1]==ee[i+2]==user and ee[i+3]==" " and ff[i+3]!=" ":
            flag = i+4
            break
        elif ee[i]==ee[i+2]==ee[i+3]== user and ee[i+1]==" " and ff[i+1]!=" ":
            flag = i+2
            break
        elif ee[i]==ee[i+1]==ee[i+3]==user and ee[i+2]==" " and ff[i+2]!=" ":
            flag = i+3
            break
        elif ee[i+1]==ee[i+2]==ee[i+3]==user and ee[i]==" " and ff[i]!=" ":
            flag = i+1
            break
        elif dd[i]==dd[i+1]==dd[i+2]==user and dd[i+3]==" " and ee[i+3]!=" ":
            flag = i+4
            break
        elif dd[i]==dd[i+2]==dd[i+3]== user and dd[i+1]==" " and ee[i+1]!=" ":
            flag = i+2
            break
        elif dd[i]==dd[i+1]==dd[i+3]==user and dd[i+2]==" " and ee[i+2]!=" ":
            flag = i+3
            break
        elif dd[i+1]==dd[i+2]==dd[i+3]==user and dd[i]==" " and ee[i]!=" ":
            flag = i+1
            break
        elif cc[i]==cc[i+1]==cc[i+2]==user and cc[i+3]==" " and dd[i+3]!=" ":
            flag = i+4
            break
        elif cc[i]==cc[i+2]==cc[i+3]== user and cc[i+1]==" " and dd[i+1]!=" ":
            flag = i+2
            break
        elif cc[i]==cc[i+1]==cc[i+3]==user and cc[i+2]==" " and dd[i+2]!=" ":
            flag = i+3
            break
        elif cc[i+1]==cc[i+2]==cc[i+3]==user and cc[i]==" " and dd[i]!=" ":
            flag = i+1
            break
        elif bb[i]==bb[i+1]==bb[i+2]==user and bb[i+3]==" " and cc[i+3]!=" ":
            flag = i+4
            break
        elif bb[i]==bb[i+2]==bb[i+3]== user and bb[i+1]==" " and cc[i+1]!=" ":
            flag = i+2
            break
        elif bb[i]==bb[i+1]==bb[i+3]==user and bb[i+2]==" " and cc[i+2]!=" ":
            flag = i+3
            break
        elif bb[i+1]==bb[i+2]==bb[i+3]==user and bb[i]==" " and cc[i]!=" ":
            flag = i+1
            break
        elif aa[i]==aa[i+1]==aa[i+2]==user and aa[i+3]==" " and bb[i+3]!=" ":
            flag = i+4
            break
        elif aa[i]==aa[i+2]==aa[i+3]== user and aa[i+1]==" " and bb[i+1]!=" ":
            flag = i+2
            break
        elif aa[i]==aa[i+1]==aa[i+3]==user and aa[i+2]==" " and bb[i+2]!=" ":
            flag = i+3
            break
        elif aa[i+1]==aa[i+2]==aa[i+3]==user and aa[i]==" " and bb[i]!=" ":
            flag = i+1
            break
    return flag
def aicheckDiag():
    flag = 0
    var = 6
    for i in range(0,4):
        if aa[i]==bb[i+1]==cc[i+2]==user and dd[i+3]==" " and ee[i+3]!=" ":
            flag = i+4
            break
        elif bb[i+1]==cc[i+2]==dd[i+3]==user and aa[i]==" " and bb[i]!=" ":
            flag = i+1
            break
        elif aa[i]==cc[i+2]==dd[i+3]==user and bb[i+1]==" " and cc[i+1]!=" ":
            flag = i+2
            break
        elif aa[i]==bb[i+1]==dd[i+3]==user and cc[i+2]==" " and dd[i+2]!= " ":
            flag = i+3
            break
        elif bb[i]==cc[i+1]==dd[i+2]==user and ee[i+3]==" " and ff[i+3]!=" ":
            flag = i+4
            break
        elif cc[i+1]==dd[i+2]==ee[i+3]==user and bb[i]==" " and cc[i]!=" ":
            flag = i+1
            break
        elif bb[i]==dd[i+2]==ee[i+3]==user and cc[i+1]==" " and dd[i+1]!=" ":
            flag = i+2
            break
        elif bb[i]==cc[i+1]==ee[i+3]==user and dd[i+2]==" " and ee[i+2]!= " ":
            flag = i+3
            break
        elif cc[i]==dd[i+1]==ee[i+2]==user and ff[i+3]==" ":
            flag = i+4
            break
        elif dd[i+1]==ee[i+2]==ff[i+3]==user and cc[i]==" " and dd[i]!=" ":
            flag = i+1
            break
        elif cc[i]==ee[i+2]==ff[i+3]==user and dd[i+1]==" " and ee[i+1]!=" ":
            flag = i+2
            break
        elif cc[i]==dd[i+1]==ff[i+3]==user and ee[i+2]==" " and ff[i+2]!= " ":
            flag = i+3
            break

    while var>2:
        if aa[var]==bb[var-1]==cc[var-2]==user and dd[var-3]==" " and ee[var-3]!=" ":
            flag = var-2
            break
        elif bb[var-1]==cc[var-2]==dd[var-3]==user and aa[var]==" " and bb[var]!=" ":
            flag = var+1
            break
        elif aa[var]==cc[var-2]==dd[var-3]==user and bb[var-1]==" " and cc[var-1]!=" ":
            flag = var
            break
        elif aa[var]==bb[var-1]==dd[var-3]==user and cc[var-2]==" " and dd[var-2]!= " ":
            flag = var-1
            break
        elif bb[var]==cc[var-1]==dd[var-2]==user and ee[var-3]==" " and ff[var-3]!=" ":
            flag = var-2
            break
        elif cc[var-1]==dd[var-2]==ee[var-3]==user and bb[var]==" " and cc[var]!=" ":
            flag = var+1
            break
        elif bb[var]==dd[var-2]==ee[var-3]==user and cc[var-1]==" " and dd[var-1]!=" ":
            flag = var
            break
        elif bb[i]==cc[var-1]==ee[var-3]==user and dd[var-2]==" " and ee[var-2]!= " ":
            flag = var-1
            break
        elif cc[var]==dd[var-1]==ee[var-2]==user and ff[var-3]==" ":
            flag = var-2
            break
        elif dd[var-1]==ee[var-2]==ff[var-3]==user and cc[var]==" " and dd[var]!=" ":
            flag = var+1
            break
        elif cc[var]==ee[var-2]==ff[var-3]==user and dd[var-1]==" " and ee[var-1]!=" ":
            flag = var
            break
        elif cc[var]==dd[var-1]==ff[var-3]==user and ee[var-2]==" " and ff[var-2]!= " ":
            flag = var-1
            break
        var-=1
    return flag
def aicheckWin():
    flag = 0
    lista = [aicheckHoriz(),aicheckVert(),aicheckDiag()]
    for i in lista:
        if i!=0:
            flag = i
            break
    return flag





########################## Artificial Intelligence Part 2: Checking for win #################

def wincheckVert():
    flag = 0
    for i in range(0,7):
        if ff[i]==ee[i]==dd[i]==comp and cc[i]== " ":
            flag = i+1
            break
        elif ee[i]==dd[i]==cc[i]==comp and bb[i] == " ":
            flag = i+1
            break
        elif dd[i]==cc[i]==bb[i]==comp and aa[i] == " ":
            flag = i+1
            break
    return flag
def wincheckHoriz():
    flag = 0
    for i in range(0,4):
        if ff[i]==ff[i+1]==ff[i+2]==comp and ff[i+3]==" ":
            flag = i+4
            break
        elif ff[i]==ff[i+2]==ff[i+3]== comp and ff[i+1]==" ":
            flag = i+2
            break
        elif ff[i]==ff[i+1]==ff[i+3]==comp and ff[i+2]==" ":
            flag = i+3
            break
        elif ff[i+1]==ff[i+2]==ff[i+3]==comp and ff[i]==" ":
            flag = i+1
            break
        elif ee[i]==ee[i+1]==ee[i+2]==comp and ee[i+3]==" " and ff[i+3]!=" ":
            flag = i+4
            break
        elif ee[i]==ee[i+2]==ee[i+3]== comp and ee[i+1]==" " and ff[i+1]!=" ":
            flag = i+2
            break
        elif ee[i]==ee[i+1]==ee[i+3]==comp and ee[i+2]==" " and ff[i+2]!=" ":
            flag = i+3
            break
        elif ee[i+1]==ee[i+2]==ee[i+3]==comp and ee[i]==" " and ff[i]!=" ":
            flag = i+1
            break
        elif dd[i]==dd[i+1]==dd[i+2]==comp and dd[i+3]==" " and ee[i+3]!=" ":
            flag = i+4
            break
        elif dd[i]==dd[i+2]==dd[i+3]== comp and dd[i+1]==" " and ee[i+1]!=" ":
            flag = i+2
            break
        elif dd[i]==dd[i+1]==dd[i+3]==comp and dd[i+2]==" " and ee[i+2]!=" ":
            flag = i+3
            break
        elif dd[i+1]==dd[i+2]==dd[i+3]==comp and dd[i]==" " and ee[i]!=" ":
            flag = i+1
            break
        elif cc[i]==cc[i+1]==cc[i+2]==comp and cc[i+3]==" " and dd[i+3]!=" ":
            flag = i+4
            break
        elif cc[i]==cc[i+2]==cc[i+3]== comp and cc[i+1]==" " and dd[i+1]!=" ":
            flag = i+2
            break
        elif cc[i]==cc[i+1]==cc[i+3]==comp and cc[i+2]==" " and dd[i+2]!=" ":
            flag = i+3
            break
        elif cc[i+1]==cc[i+2]==cc[i+3]==comp and cc[i]==" " and dd[i]!=" ":
            flag = i+1
            break
        elif bb[i]==bb[i+1]==bb[i+2]==comp and bb[i+3]==" " and cc[i+3]!=" ":
            flag = i+4
            break
        elif bb[i]==bb[i+2]==bb[i+3]== comp and bb[i+1]==" " and cc[i+1]!=" ":
            flag = i+2
            break
        elif bb[i]==bb[i+1]==bb[i+3]==comp and bb[i+2]==" " and cc[i+2]!=" ":
            flag = i+3
            break
        elif bb[i+1]==bb[i+2]==bb[i+3]==comp and bb[i]==" " and cc[i]!=" ":
            flag = i+1
            break
        elif aa[i]==aa[i+1]==aa[i+2]==comp and aa[i+3]==" " and bb[i+3]!=" ":
            flag = i+4
            break
        elif aa[i]==aa[i+2]==aa[i+3]== comp and aa[i+1]==" " and bb[i+1]!=" ":
            flag = i+2
            break
        elif aa[i]==aa[i+1]==aa[i+3]==comp and aa[i+2]==" " and bb[i+2]!=" ":
            flag = i+3
            break
        elif aa[i+1]==aa[i+2]==aa[i+3]==comp and aa[i]==" " and bb[i]!=" ":
            flag = i+1
            break
    return flag
def wincheckDiag():
    flag = 0
    var = 6
    for i in range(0,4):
        if aa[i]==bb[i+1]==cc[i+2]==comp and dd[i+3]==" " and ee[i+3]!=" ":
            flag = i+4
            break
        elif bb[i+1]==cc[i+2]==dd[i+3]==comp and aa[i]==" " and bb[i]!=" ":
            flag = i+1
            break
        elif aa[i]==cc[i+2]==dd[i+3]==comp and bb[i+1]==" " and cc[i+1]!=" ":
            flag = i+2
            break
        elif aa[i]==bb[i+1]==dd[i+3]==comp and cc[i+2]==" " and dd[i+2]!= " ":
            flag = i+3
            break
        elif bb[i]==cc[i+1]==dd[i+2]==comp and ee[i+3]==" " and ff[i+3]!=" ":
            flag = i+4
            break
        elif cc[i+1]==dd[i+2]==ee[i+3]==comp and bb[i]==" " and cc[i]!=" ":
            flag = i+1
            break
        elif bb[i]==dd[i+2]==ee[i+3]==comp and cc[i+1]==" " and dd[i+1]!=" ":
            flag = i+2
            break
        elif bb[i]==cc[i+1]==ee[i+3]==comp and dd[i+2]==" " and ee[i+2]!= " ":
            flag = i+3
            break
        elif cc[i]==dd[i+1]==ee[i+2]==comp and ff[i+3]==" ":
            flag = i+4
            break
        elif dd[i+1]==ee[i+2]==ff[i+3]==comp and cc[i]==" " and dd[i]!=" ":
            flag = i+1
            break
        elif cc[i]==ee[i+2]==ff[i+3]==comp and dd[i+1]==" " and ee[i+1]!=" ":
            flag = i+2
            break
        elif cc[i]==dd[i+1]==ff[i+3]==comp and ee[i+2]==" " and ff[i+2]!= " ":
            flag = i+3
            break

    while var>2:
        if aa[var]==bb[var-1]==cc[var-2]==comp and dd[var-3]==" " and ee[var-3]!=" ":
            flag = var-2
            break
        elif bb[var-1]==cc[var-2]==dd[var-3]==comp and aa[var]==" " and bb[var]!=" ":
            flag = var+1
            break
        elif aa[var]==cc[var-2]==dd[var-3]==comp and bb[var-1]==" " and cc[var-1]!=" ":
            flag = var
            break
        elif aa[var]==bb[var-1]==dd[var-3]==comp and cc[var-2]==" " and dd[var-2]!= " ":
            flag = var-1
            break
        elif bb[var]==cc[var-1]==dd[var-2]==comp and ee[var-3]==" " and ff[var-3]!=" ":
            flag = var-2
            break
        elif cc[var-1]==dd[var-2]==ee[var-3]==comp and bb[var]==" " and cc[var]!=" ":
            flag = var+1
            break
        elif bb[var]==dd[var-2]==ee[var-3]==comp and cc[var-1]==" " and dd[var-1]!=" ":
            flag = var
            break
        elif bb[i]==cc[var-1]==ee[var-3]==comp and dd[var-2]==" " and ee[var-2]!= " ":
            flag = var-1
            break
        elif cc[var]==dd[var-1]==ee[var-2]==comp and ff[var-3]==" ":
            flag = var-2
            break
        elif dd[var-1]==ee[var-2]==ff[var-3]==comp and cc[var]==" " and dd[var]!=" ":
            flag = var+1
            break
        elif cc[var]==ee[var-2]==ff[var-3]==comp and dd[var-1]==" " and ee[var-1]!=" ":
            flag = var
            break
        elif cc[var]==dd[var-1]==ff[var-3]==comp and ee[var-2]==" " and ff[var-2]!= " ":
            flag = var-1
            break
        var-=1
    return flag
def wincheckWin():
    flag = 0
    lista = [wincheckHoriz(),wincheckVert(),wincheckDiag()]
    for i in lista:
        if i!=0:
            flag = i
            break
    return flag



########################################## Main Program #####################################
def play():
    winvaruser = 0
    winvarcomp = 0
    while True:
        print "Available columns left: "
        print spaces
        print ""
        inp = checkInp1()
        some_move(inp,user)
        checkSpaces()
        print "\n\n"
        print aa
        print bb
        print cc
        print dd
        print ee
        print ff
        if checkWin() == 1:
            winvaruser = 1
            break
        if wincheckWin()!=0:
            u = wincheckWin()
            some_move(u,comp)
        elif aicheckWin()!=0:
            u = aicheckWin()
            some_move(u,comp)
        elif aicheckWin()==0 and wincheckWin()==0:
            comprand = random.choice(spaces)
            some_move(comprand,comp)
        print "\n\n"
        print "My move!"
        print "\n\n"
        print aa
        print bb
        print cc
        print dd
        print ee
        print ff
        if checkWin() != 1 and spaces == []:
            print "\n\n\nIt's a tie!"
            break
        if checkWin() == 1:
            winvarcomp = 1
            break
        checkSpaces()
        print ""
    
    print "\n\n\n"
    if winvaruser == 1:
        print "You win! Congratulations!"
    elif winvarcomp==1:
        print "Too bad! I won! Better luck next time!"


play()
sleep(2)
print "\n\n\n"
while True:
    s=str(raw_input("Do you want to play again? "))
    s = s.lower()
    if 'yes' in s or 'ye' in s or 'y' in s:
        print "\n\n\n"
        play()
    elif 'no' in s or 'n' in s:
        print ""
        break
    else:
        print "Please try again."
        print ""

