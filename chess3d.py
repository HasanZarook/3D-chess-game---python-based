# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 20:38:30 2022

@author: Abraham Oreem and Hasan zarook
"""
import pygame
import tkinter
from tkinter import *
import tkinter.font as font
from PIL import Image
from PIL import ImageTk
from tkinter import ttk
sw=''
n,n1,n2,n3,n4,n5,n6,n7,n8,n9,n10,n11,n12,n13,n14,n15=1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1
check=0
class crd(object):
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __str__(self):
        return (str(self.x)+" "+str(self.y))
    def __eq__(self,other):
        if self.x==other.x and self.y==other.y:
            return True
        else:
            return False

def changer(b):
    global Save,check
    global Bbpawn,Bbpawn2,Bbpawn3,Bbpawn4,Bbpawn5,Bbpawn6,Bbpawn7,Bbpawn8\
        ,Bbking,Bbqueen,Bbnit,Bbnit1,Bbbish,Bbbish1,Bbrook,Bbrook1
    global Wbpawn,Wbpawn1,Wbpawn2,Wbpawn3,Wbpawn4,Wbpawn5,Wbpawn6,Wbpawn7\
        ,Bwking,Bwqueen,Bwnit,Bwnit1,Bwbish,Bwbish1,Bwrook,Bwrook1
    if check==0:
        a=b
    elif check==1:
        a=3
        
    if a==1:
        Save['state']='active'
        for i in (Bbpawn,Bbpawn2,Bbpawn3,Bbpawn4,Bbpawn5,Bbpawn6,Bbpawn7,Bbpawn8,Bbking,Bbqueen,Bbnit,Bbnit1,Bbbish,Bbbish1,Bbrook,Bbrook1):
            i.config(state='active')
        for j in (Wbpawn,Wbpawn1,Wbpawn2,Wbpawn3,Wbpawn4,Wbpawn5,Wbpawn6,Wbpawn7,Bwking,Bwqueen,Bwnit,Bwnit1,Bwbish,Bwbish1,Bwrook,Bwrook1):
            j.config(state='disabled')
    elif a==2:
        Save['state']='active'
        for i in (Bbpawn,Bbpawn2,Bbpawn3,Bbpawn4,Bbpawn5,Bbpawn6,Bbpawn7,Bbpawn8,Bbking,Bbqueen,Bbnit,Bbnit1,Bbbish,Bbbish1,Bbrook,Bbrook1):
            i.config(state='disabled')
        for j in (Wbpawn,Wbpawn1,Wbpawn2,Wbpawn3,Wbpawn4,Wbpawn5,Wbpawn6,Wbpawn7,Bwking,Bwqueen,Bwnit,Bwnit1,Bwbish,Bwbish1,Bwrook,Bwrook1):
            j.config(state='active')
    elif a==3:
        for i in (Bbpawn,Bbpawn2,Bbpawn3,Bbpawn4,Bbpawn5,Bbpawn6,Bbpawn7,Bbpawn8,Bbking,Bbqueen,Bbnit,Bbnit1,Bbbish,Bbbish1,Bbrook,Bbrook1):
            i.config(state='disabled')
        for j in (Wbpawn,Wbpawn1,Wbpawn2,Wbpawn3,Wbpawn4,Wbpawn5,Wbpawn6,Wbpawn7,Bwking,Bwqueen,Bwnit,Bwnit1,Bwbish,Bwbish1,Bwrook,Bwrook1):
            j.config(state='disabled')
        Save['state']='disabled'
        check=1
def destroyer():
    global win
    sw.destroy()
    win.destroy()
    
def loader():
    global Bbpawn,Bbpawn2,Bbpawn3,Bbpawn4,Bbpawn5,Bbpawn6,Bbpawn7,Bbpawn8\
        ,Bbking,Bbqueen,Bbnit,Bbnit1,Bbbish,Bbbish1,Bbrook,Bbrook1
    global Wbpawn,Wbpawn1,Wbpawn2,Wbpawn3,Wbpawn4,Wbpawn5,Wbpawn6,Wbpawn7\
        ,Bwking,Bwqueen,Bwnit,Bwnit1,Bwbish,Bwbish1,Bwrook,Bwrook1
    iq=[Wbpawn,Wbpawn1,Wbpawn2,Wbpawn3,Wbpawn4,Wbpawn5,Wbpawn6,Wbpawn7,Bbpawn,Bbpawn2,Bbpawn3,Bbpawn4,Bbpawn5,Bbpawn6,Bbpawn7,Bbpawn8\
        ,Bbrook,Bbrook1,Bbbish,Bbbish1,Bbnit,Bbnit1,Bbking,Bbqueen,Bwrook,Bwrook1,Bwbish,Bwbish1,Bwnit,Bwnit1,Bwking,Bwqueen]
    with open('Savegame.txt','r+') as sg:
        lg=sg.readlines()
    n=0
    for s in lg:
        if n==32:
            if lg[n]=="disabled":
                changer(1)
                break
            elif lg[n]=="active":
                break
        x=s.split()
        g=iq[n]
        nx=int(x[0])
        ny=int(x[1])
        g.place(x=nx,y=ny)
        n+=1
def restart():
    sw.destroy()
    start()
            
def load():
    start(1)
    
def start(a=0):
    global sw
    sw=Toplevel(win)
    sw.title("Chess")
    sw.geometry("1920x1080")
    sw.iconbitmap("chess icon.ico")
    sc=Canvas(sw, height=1080,width=1920,bg='black')
    img1=(Image.open("chess board.jpg"))
    rimg1=img1.resize((800,800),Image.ANTIALIAS)
    nimg1= ImageTk.PhotoImage(rimg1)
    sc.create_image(380,0,anchor=NW,image=nimg1,tag='board')
    peice1=(Image.open("pawnb.png"))
    rimg2=peice1.resize((50,50),Image.ANTIALIAS)
    nimg2= ImageTk.PhotoImage(rimg2)
    mf=font.Font(size=15,weight='bold')
    Rip=Label(sw,text="RIP DEPT",font=mf,bg='white',bd=10,pady=70,padx=20)
    Rip.place(x=105,y=332)
    Restart=Button(sw,command=restart,text='Restart Game',font=mf,bg='black',fg='white',activebackground='white',bd=10,padx=40,pady=10)
    Restart.place(x=1248,y=158)
    global Save
    Save=Button(sw,command=saver,text='Save Game',state='disabled',font=mf,bg='black',fg='white',activebackground='white',bd=10,padx=40,pady=10)
    Save.place(x=1248,y=358)
    Quit=Button(sw,command=destroyer,text='Quit Game',font=mf,bg='black',fg='white',activebackground='green',bd=10,padx=40,pady=10)
    Quit.place(x=1248,y=558)
    global Bbpawn
    Bbpawn=Button(sw,image=nimg2,state='disabled',command=lambda:[moverBP1(),draggerBP1()])
    Bbpawn.place(x=490,y=202)
# =============================================================================
#     Bbpawn.bind("<Button-1>",dragger)
#     Bbpawn.bind("<B1-Motion>",mover)
# =============================================================================
    global Bbpawn2
    Bbpawn2=Button(sw,image=nimg2,state='disabled',command=lambda:[moverBP2(),draggerBP2()])
    Bbpawn2.place(x=565,y=202)
# =============================================================================
#     Bbpawn2.bind("<Button-1>",dragger)
#     Bbpawn2.bind("<B1-Motion>",mover)
# =============================================================================
    global Bbpawn3
    Bbpawn3=Button(sw,image=nimg2,state='disabled',command=lambda:[moverBP3(),draggerBP3()])
    Bbpawn3.place(x=640,y=202)
# =============================================================================
#     Bbpawn3.bind("<Button-1>",dragger)
#     Bbpawn3.bind("<B1-Motion>",mover)
# =============================================================================
    global Bbpawn4
    Bbpawn4=Button(sw,image=nimg2,state='disabled',command=lambda:[moverBP4(),draggerBP4()])
    Bbpawn4.place(x=715,y=202)
# =============================================================================
#     Bbpawn4.bind("<Button-1>",dragger)
#     Bbpawn4.bind("<B1-Motion>",mover)
# =============================================================================
    global Bbpawn5
    Bbpawn5=Button(sw,image=nimg2,state='disabled',command=lambda:[moverBP5(),draggerBP5()])
    Bbpawn5.place(x=790,y=202)
# =============================================================================
#     Bbpawn5.bind("<Button-1>",dragger)
#     Bbpawn5.bind("<B1-Motion>",mover)
# =============================================================================
    global Bbpawn6
    Bbpawn6=Button(sw,image=nimg2,state='disabled',command=lambda:[moverBP6(),draggerBP6()])
    Bbpawn6.place(x=865,y=202)
# =============================================================================
#     Bbpawn6.bind("<Button-1>",dragger)
#     Bbpawn6.bind("<B1-Motion>",mover)
# =============================================================================
    global Bbpawn7
    Bbpawn7=Button(sw,image=nimg2,state='disabled',command=lambda:[moverBP7(),draggerBP7()])
    Bbpawn7.place(x=940,y=202)
# =============================================================================
#     Bbpawn7.bind("<Button-1>",dragger)
#     Bbpawn7.bind("<B1-Motion>",mover)
# =============================================================================
    global Bbpawn8
    Bbpawn8=Button(sw,image=nimg2,state='disabled',command=lambda:[moverBP8(),draggerBP8()])
    Bbpawn8.place(x=1015,y=202)
# =============================================================================
#     Bbpawn8.bind("<Button-1>",dragger)
#     Bbpawn8.bind("<B1-Motion>",mover)
# =============================================================================
    peicekb=(Image.open("king zrk b.png"))
    rimgkb=peicekb.resize((50,50),Image.ANTIALIAS)
    nimgkb= ImageTk.PhotoImage(rimgkb)
    global Bbking
    Bbking=Button(sw,image=nimgkb,state='disabled',command=lambda:[moverBbking(),draggerBbking()])
    Bbking.place(x=715,y=134)
# =============================================================================
#     Bbking.bind("<Button-1>",dragger)
#     Bbking.bind("<B1-Motion>",mover)
# =============================================================================
    peicekw=(Image.open("king AB w.png"))
    rimgkw=peicekw.resize((50,50),Image.ANTIALIAS)
    nimgkw= ImageTk.PhotoImage(rimgkw)
    global Bwking
    Bwking=Button(sw,image=nimgkw,command=lambda:[moverBwking(),draggerBwking()])
    Bwking.place(x=715,y=610)
# =============================================================================
#     Bwking.bind("<Button-1>",dragger)
#     Bwking.bind("<B1-Motion>",mover)
# =============================================================================
    peicewp=(Image.open("pawnw.png"))
    rimgwp=peicewp.resize((50,50),Image.ANTIALIAS)
    nimgwp= ImageTk.PhotoImage(rimgwp)
    global Wbpawn
    Wbpawn=Button(sw,image=nimgwp,command=lambda:[moverWP1(),draggerWP1()])
    Wbpawn.place(x=490,y=542)
# =============================================================================
#     Wbpawn.bind("<Button-1>",dragger)
#     Wbpawn.bind("<B1-Motion>",mover1)
# =============================================================================
    global Wbpawn1
    Wbpawn1=Button(sw,image=nimgwp,command=lambda:[moverWP2(),draggerWP2()])
    Wbpawn1.place(x=565,y=542)
# =============================================================================
#     Wbpawn1.bind("<Button-1>",dragger)
#     Wbpawn1.bind("<B1-Motion>",mover)
# =============================================================================
    global Wbpawn2
    Wbpawn2=Button(sw,image=nimgwp,command=lambda:[moverWP3(),draggerWP3()])
    Wbpawn2.place(x=640,y=542)
# =============================================================================
#     Wbpawn2.bind("<Button-1>",dragger)
#     Wbpawn2.bind("<B1-Motion>",mover)
# =============================================================================
    global Wbpawn3
    Wbpawn3=Button(sw,image=nimgwp,command=lambda:[moverWP4(),draggerWP4()])
    Wbpawn3.place(x=715,y=542)
# =============================================================================
#     Wbpawn3.bind("<Button-1>",dragger)
#     Wbpawn3.bind("<B1-Motion>",mover)
# =============================================================================
    global Wbpawn4
    Wbpawn4=Button(sw,image=nimgwp,command=lambda:[moverWP5(),draggerWP5()])
    Wbpawn4.place(x=790,y=542)
# =============================================================================
#     Wbpawn4.bind("<Button-1>",dragger)
#     Wbpawn4.bind("<B1-Motion>",mover)
# =============================================================================
    global Wbpawn5
    Wbpawn5=Button(sw,image=nimgwp,command=lambda:[moverWP6(),draggerWP6()])
    Wbpawn5.place(x=865,y=542)
# =============================================================================
#     Wbpawn5.bind("<Button-1>",dragger)
#     Wbpawn5.bind("<B1-Motion>",mover)
# =============================================================================
    global Wbpawn6
    Wbpawn6=Button(sw,image=nimgwp,command=lambda:[moverWP7(),draggerWP7()])
    Wbpawn6.place(x=940,y=542)
# =============================================================================
#     Wbpawn6.bind("<Button-1>",dragger)
#     Wbpawn6.bind("<B1-Motion>",mover)
# =============================================================================
    global Wbpawn7
    Wbpawn7=Button(sw,image=nimgwp,command=lambda:[moverWP8(),draggerWP8()])
    Wbpawn7.place(x=1015,y=542)
# =============================================================================
#     Wbpawn7.bind("<Button-1>",dragger)
#     Wbpawn7.bind("<B1-Motion>",mover)
# =============================================================================
    peiceqw=(Image.open("queenw.png"))
    rimgqw=peiceqw.resize((50,50),Image.ANTIALIAS)
    nimgqw= ImageTk.PhotoImage(rimgqw)
    global Bwqueen
    Bwqueen=Button(sw,image=nimgqw,command=lambda:[moverBwqueen(),draggerBwqueen()])
    Bwqueen.place(x=790,y=610)
# =============================================================================
#     Bwqueen.bind("<Button-1>",dragger)
#     Bwqueen.bind("<B1-Motion>",mover)
# =============================================================================
    peiceqb=(Image.open("queenb.png"))
    rimgqb=peiceqb.resize((50,50),Image.ANTIALIAS)
    nimgqb= ImageTk.PhotoImage(rimgqb)
    global Bbqueen
    Bbqueen=Button(sw,image=nimgqb,state='disabled',command=lambda:[moverBbqueen(),draggerBbqueen()])
    Bbqueen.place(x=790,y=134)
# =============================================================================
#     Bbqueen.bind("<Button-1>",dragger)
#     Bbqueen.bind("<B1-Motion>",mover)
# =============================================================================
    peicerb=(Image.open("rookb.png"))
    rimgrb=peicerb.resize((50,50),Image.ANTIALIAS)
    nimgrb= ImageTk.PhotoImage(rimgrb)
    global Bbrook
    Bbrook=Button(sw,image=nimgrb,state='disabled',command=lambda:[moverBbrook(),draggerBbrook()])
    Bbrook.place(x=490,y=134)
# =============================================================================
#     Bbrook.bind("<Button-1>",dragger)
#     Bbrook.bind("<B1-Motion>",mover)
# =============================================================================
    global Bbrook1
    Bbrook1=Button(sw,image=nimgrb,state='disabled',command=lambda:[moverBbrook1(),draggerBbrook1()])
    Bbrook1.place(x=1015,y=134)
# =============================================================================
#     Bbrook1.bind("<Button-1>",dragger)
#     Bbrook1.bind("<B1-Motion>",mover)
# =============================================================================
    peicerw=(Image.open("rookw.png"))
    rimgrw=peicerw.resize((50,50),Image.ANTIALIAS)
    nimgrw= ImageTk.PhotoImage(rimgrw)
    global Bwrook
    Bwrook=Button(sw,image=nimgrw,command=lambda:[moverBwrook(),draggerBwrook()])
    Bwrook.place(x=490,y=610)
# =============================================================================
#     Bwrook.bind("<Button-1>",dragger)
#     Bwrook.bind("<B1-Motion>",mover)
# =============================================================================
    global Bwrook1
    Bwrook1=Button(sw,image=nimgrw,command=lambda:[moverBwrook1(),draggerBwrook1()])
    Bwrook1.place(x=1015,y=610)
# =============================================================================
#     Bwrook1.bind("<Button-1>",dragger)
#     Bwrook1.bind("<B1-Motion>",mover)
# =============================================================================
    global Bbbish
    peicebb=(Image.open("bishopwb.png"))
    rimgbb=peicebb.resize((50,50),Image.ANTIALIAS)
    nimgbb= ImageTk.PhotoImage(rimgbb)
    Bbbish=Button(sw,image=nimgbb,state='disabled',command=lambda:[moverBbbish(),draggerBbbish()])
    Bbbish.place(x=640,y=134)
# =============================================================================
#     Bbbish.bind("<Button-1>",dragger)
#     Bbbish.bind("<B1-Motion>",mover)
# =============================================================================
    global Bbbish1
    Bbbish1=Button(sw,image=nimgbb,state='disabled',command=lambda:[moverBbbish1(),draggerBbbish1()])
    Bbbish1.place(x=865,y=134)
# =============================================================================
#     Bbbish1.bind("<Button-1>",dragger)
#     Bbbish1.bind("<B1-Motion>",mover)
# =============================================================================
    global Bwbish
    peicewb=(Image.open("bishopw.png"))
    rimgwb=peicewb.resize((50,50),Image.ANTIALIAS)
    nimgwb= ImageTk.PhotoImage(rimgwb)
    Bwbish=Button(sw,image=nimgwb,command=lambda:[moverBwbish(),draggerBwbish()])
    Bwbish.place(x=640,y=610)
# =============================================================================
#     Bwbish.bind("<Button-1>",dragger)
#     Bwbish.bind("<B1-Motion>",mover)
# =============================================================================
    global Bwbish1
    Bwbish1=Button(sw,image=nimgwb,command=lambda:[moverBwbish1(),draggerBwbish1()])
    Bwbish1.place(x=865,y=610)
# =============================================================================
#     Bwbish1.bind("<Button-1>",dragger)
#     Bwbish1.bind("<B1-Motion>",mover)
# =============================================================================
    global Bbnit
    peiceknb=(Image.open("knightb.png"))
    rimgknb=peiceknb.resize((50,50),Image.ANTIALIAS)
    nimgknb= ImageTk.PhotoImage(rimgknb)
    Bbnit=Button(sw,image=nimgknb,state='disabled',command=lambda:[moverBbnit(),draggerBbnit()])
    Bbnit.place(x=565,y=134)
# =============================================================================
#     Bbnit.bind("<Button-1>",dragger)
#     Bbnit.bind("<B1-Motion>",mover)
# =============================================================================
    global Bbnit1
    Bbnit1=Button(sw,image=nimgknb,state='disabled',command=lambda:[moverBbnit1(),draggerBbnit1()])
    Bbnit1.place(x=940,y=134)
# =============================================================================
#     Bbnit1.bind("<Button-1>",dragger)
#     Bbnit1.bind("<B1-Motion>",mover)
# =============================================================================
    global Bwnit
    peiceknw=(Image.open("knightw.png"))
    rimgknw=peiceknw.resize((50,50),Image.ANTIALIAS)
    nimgknw= ImageTk.PhotoImage(rimgknw)
    Bwnit=Button(sw,image=nimgknw,command=lambda:[moverBwnit(),draggerBwnit()])
    Bwnit.place(x=565,y=610)
# =============================================================================
#     Bwnit.bind("<Button-1>",dragger)
#     Bwnit.bind("<B1-Motion>",mover)
# =============================================================================
    global Bwnit1
    Bwnit1=Button(sw,image=nimgknw,command=lambda:[moverBwnit1(),draggerBwnit1()])
    Bwnit1.place(x=940,y=610)
# =============================================================================
#     Bwnit1.bind("<Button-1>",dragger)
#     Bwnit1.bind("<B1-Motion>",mover)
# =============================================================================
    if a==1:
        loader()
    
    sw.bind("<Button-1>",positioner)
    
    sc.pack()
    sw.attributes("-fullscreen",True)
    sw.mainloop()
    
    
    
def terminator(killer):
    global poswp1
    global poswp2
    global poswp3
    global poswp4
    global poswp5
    global poswp6
    global poswp7
    global poswp8
    global posbp1
    global posbp2
    global posbp3
    global posbp4
    global posbp5
    global posbp6
    global posbp7
    global posbp8
    global posbr1
    global posbr2
    global posbbi1
    global posbbi2
    global posbn1
    global posbn2
    global posbk
    global posbq
    global poswr1
    global poswr2
    global poswbi1
    global poswbi2
    global poswn1
    global poswn2
    global poswk
    global poswq
    peicesdict={Bwbish:poswbi1,Bwbish1:poswbi2,Bwrook:poswr1,Bwrook1:poswr2,Bwqueen:poswq,Bwking:poswk,Bwnit:poswn1,Bwnit1:poswn2,Wbpawn:poswp1,Wbpawn1:poswp2,Wbpawn2:poswp3,Wbpawn3:poswp4,Wbpawn4:poswp5,Wbpawn5:poswp6,Wbpawn6:poswp7,Wbpawn7:poswp8\
                ,Bbbish:posbbi1,Bbbish1:posbbi2,Bbrook:posbr1,Bbrook1:posbr2,Bbqueen:posbq,Bbking:posbk,Bbnit:posbn1,Bbnit1:posbn2,Bbpawn:posbp1,Bbpawn2:posbp2,Bbpawn3:posbp3,Bbpawn4:posbp4,Bbpawn5:posbp5,Bbpawn6:posbp6,Bbpawn7:posbp7,Bbpawn8:posbp8}
    pos=peicesdict[killer]
    del peicesdict[killer]
    for victim in peicesdict:
        if pos==peicesdict[victim]:
            victim.place(x=150,y=350)
            victim['state']='disabled'
            if victim==Bbking or victim==Bwking:
                mf=font.Font(size=50,weight='bold',family='Times')
                GO=Label(sw,text="GAME OVER",font=mf,bg='red',bd=10,pady=20,padx=20)
                GO.place(x=533,y=305)
                changer(3)
            
                
    
    
def Peices_info(WP1,WP2,WP3,WP4,WP5,WP6,WP7,WP8,BP1,BP2,BP3,BP4,BP5,BP6,BP7,BP8,BR1,BR2,BBI1,BBI2,BN1,BN2,BK,BQ,WR1,WR2,WBI1,WBI2,WN1,WN2,WK,WQ):
    global poswp1
    global poswp2
    global poswp3
    global poswp4
    global poswp5
    global poswp6
    global poswp7
    global poswp8
    global posbp1
    global posbp2
    global posbp3
    global posbp4
    global posbp5
    global posbp6
    global posbp7
    global posbp8
    global posbr1
    global posbr2
    global posbbi1
    global posbbi2
    global posbn1
    global posbn2
    global posbk
    global posbq
    global poswr1
    global poswr2
    global poswbi1
    global poswbi2
    global poswn1
    global poswn2
    global poswk
    global poswq
    poswp1,poswp2=WP1,WP2
    poswp3=WP3
    poswp4=WP4
    poswp5=WP5
    poswp6=WP6
    poswp7=WP7
    poswp8=WP8
    posbp1=BP1
    posbp2=BP2
    posbp3=BP3
    posbp4=BP4
    posbp5=BP5
    posbp6=BP6
    posbp7=BP7
    posbp8=BP8
    posbr1=BR1
    posbr2=BR2
    posbbi1=BBI1
    posbbi2=BBI2
    posbn1=BN1
    posbn2=BN2
    posbk=BK
    posbq=BQ
    poswr1=WR1
    poswr2=WR2
    poswbi1=WBI1
    poswbi2=WBI2
    poswn1=WN1
    poswn2=WN2
    poswk=WK
    poswq=WQ

def saver():
    global poswp1,poswp2,poswp3,poswp4,poswp5,poswp6,poswp7,poswp8,posbp1,posbp2,posbp3,posbp4,posbp5,posbp6,posbp7\
        ,posbp8,posbr1,posbr2,posbbi1,posbbi2,posbn1,posbn2,posbk,posbq\
            ,poswr1,poswr2,poswbi1,poswbi2,poswn1,poswn2,poswk,poswq
    n=[poswp1,poswp2,poswp3,poswp4,poswp5,poswp6,poswp7,poswp8,posbp1,posbp2,posbp3,posbp4,posbp5,posbp6,posbp7\
        ,posbp8,posbr1,posbr2,posbbi1,posbbi2,posbn1,posbn2,posbk,posbq\
            ,poswr1,poswr2,poswbi1,poswbi2,poswn1,poswn2,poswk,poswq]
    
    with open('Savegame.txt','r+') as sv:
        sv.truncate(0)
        sv.seek(0)
        for i in n:
            c=str(i)+"\n"
            sv.write(c)
        if Wbpawn['state']=='active':
            state="active"
            sv.write(state)
        else:
            state="disabled"
            sv.write(state)            
        
def dragger(event):
    widget=event.widget
    widget.startX=event.x
    widget.startY=event.y

def mover(event):
    widget=event.widget
    x=widget.winfo_x()-widget.startX+event.x
    y=widget.winfo_y()-widget.startY+event.y
    widget.place(x=x,y=y)

def draggerWP1():
     global cx
     global cy
     cx=Wbpawn.winfo_x() 
     cy=Wbpawn.winfo_y()
         
def moverWP1():
    
    global sw
    global cx
    global cy
    def mover2(event):
        global n
        global Wbpawn
        x=event.x
        y=event.y
        smy=cy-136
        smx=cx
        nx=cx
        ny=cy-68
        if (x<(cx+141)and x>(cx+67)) and (y<(cy-8) and y>(cy-76)):
            nx=cx+75
            ny=cy-68
            n=0
        elif (x<(cx-13)and x>(cx-87)) and (y<(cy-8) and y>(cy-76)):
            nx=cx-75
            ny=cy-68
            n=0
        while n==1:
            if y<467:
                nx=smx
                ny=smy
                
            n=0
        Wbpawn.place(x=nx,y=ny)
        print(nx,"  ",ny)
        xi=1
        try:
            Peices_info(WP1=crd(nx,ny),WP2=crd(Wbpawn1.winfo_x(),Wbpawn1.winfo_y()),WP3=crd(Wbpawn2.winfo_x(),Wbpawn2.winfo_y()),WP4=crd(Wbpawn3.winfo_x(),Wbpawn3.winfo_y()),WP5=crd(Wbpawn4.winfo_x(),Wbpawn4.winfo_y()),WP6=crd(Wbpawn5.winfo_x(),Wbpawn5.winfo_y()),WP7=crd(Wbpawn6.winfo_x(),Wbpawn6.winfo_y()),WP8=crd(Wbpawn7.winfo_x(),Wbpawn7.winfo_y()),BP1=crd(Bbpawn.winfo_x(),Bbpawn.winfo_y()),BP2=crd(Bbpawn2.winfo_x(),Bbpawn2.winfo_y()),BP3=crd(Bbpawn3.winfo_x(),Bbpawn3.winfo_y()),BP4=crd(Bbpawn4.winfo_x(),Bbpawn4.winfo_y()),BP5=crd(Bbpawn5.winfo_x(),Bbpawn5.winfo_y()),BP6=crd(Bbpawn6.winfo_x(),Bbpawn6.winfo_y()),BP7=crd(Bbpawn7.winfo_x(),Bbpawn7.winfo_y()),BP8=crd(Bbpawn8.winfo_x(),Bbpawn8.winfo_y()),BR1=crd(Bbrook.winfo_x(),Bbrook.winfo_y()),BR2=crd(Bbrook1.winfo_x(),Bbrook1.winfo_y()),BBI1=crd(Bbbish.winfo_x(),Bbbish.winfo_y()),BBI2=crd(Bbbish1.winfo_x(),Bbbish1.winfo_y()),BN1=crd(Bbnit.winfo_x(),Bbnit.winfo_y()),BN2=crd(Bbnit1.winfo_x(),Bbnit1.winfo_y()),BK=crd(Bbking.winfo_x(),Bbking.winfo_y()),BQ=crd(Bbqueen.winfo_x(),Bbqueen.winfo_y()),WR1=crd(Bwrook.winfo_x(),Bwrook.winfo_y()),WR2=crd(Bwrook1.winfo_x(),Bwrook1.winfo_y()),WBI1=crd(Bwbish.winfo_x(),Bwbish.winfo_y()),WBI2=crd(Bwbish1.winfo_x(),Bwbish1.winfo_y()),WN1=crd(Bwnit.winfo_x(),Bwnit.winfo_y()),WN2=crd(Bwnit1.winfo_x(),Bwnit1.winfo_y()),WK=crd(Bwking.winfo_x(),Bwking.winfo_y()),WQ=crd(Bwqueen.winfo_x(),Bwqueen.winfo_y()))
            terminator(Wbpawn)
            sw.unbind("<Button-1>")
        except :
            print("click in the box not on the button")
            xi=2
        if xi==2:
            pass
        else:
            changer(1)
        
    
    sw.bind("<Button-1>",mover2)

def draggerWP2():
     global cx
     global cy
     cx=Wbpawn1.winfo_x() 
     cy=Wbpawn1.winfo_y()
     print(cx,',',cy)
             
def moverWP2():
    
    global sw
    global cx
    global cy
    def mover2(event):
        global n1
        global Wbpawn1
        x=event.x
        y=event.y
        smy=cy-136
        smx=cx
        nx=cx
        ny=cy-68
        if (x<(cx+141)and x>(cx+67)) and (y<(cy-8) and y>(cy-76)):
            nx=cx+75
            ny=cy-68
            n1=0
        elif (x<(cx-13)and x>(cx-87)) and (y<(cy-8) and y>(cy-76)):
            nx=cx-75
            ny=cy-68
            n1=0
        while n1==1:
            if y<467:
                nx=smx
                ny=smy
                
            n1=0
        Wbpawn1.place(x=nx,y=ny)
        xi=1
        try:
            Peices_info(WP1=crd(Wbpawn.winfo_x(),Wbpawn.winfo_y()),WP2=crd(nx,ny),WP3=crd(Wbpawn2.winfo_x(),Wbpawn2.winfo_y()),WP4=crd(Wbpawn3.winfo_x(),Wbpawn3.winfo_y()),WP5=crd(Wbpawn4.winfo_x(),Wbpawn4.winfo_y()),WP6=crd(Wbpawn5.winfo_x(),Wbpawn5.winfo_y()),WP7=crd(Wbpawn6.winfo_x(),Wbpawn6.winfo_y()),WP8=crd(Wbpawn7.winfo_x(),Wbpawn7.winfo_y()),BP1=crd(Bbpawn.winfo_x(),Bbpawn.winfo_y()),BP2=crd(Bbpawn2.winfo_x(),Bbpawn2.winfo_y()),BP3=crd(Bbpawn3.winfo_x(),Bbpawn3.winfo_y()),BP4=crd(Bbpawn4.winfo_x(),Bbpawn4.winfo_y()),BP5=crd(Bbpawn5.winfo_x(),Bbpawn5.winfo_y()),BP6=crd(Bbpawn6.winfo_x(),Bbpawn6.winfo_y()),BP7=crd(Bbpawn7.winfo_x(),Bbpawn7.winfo_y()),BP8=crd(Bbpawn8.winfo_x(),Bbpawn8.winfo_y()),BR1=crd(Bbrook.winfo_x(),Bbrook.winfo_y()),BR2=crd(Bbrook1.winfo_x(),Bbrook1.winfo_y()),BBI1=crd(Bbbish.winfo_x(),Bbbish.winfo_y()),BBI2=crd(Bbbish1.winfo_x(),Bbbish1.winfo_y()),BN1=crd(Bbnit.winfo_x(),Bbnit.winfo_y()),BN2=crd(Bbnit1.winfo_x(),Bbnit1.winfo_y()),BK=crd(Bbking.winfo_x(),Bbking.winfo_y()),BQ=crd(Bbqueen.winfo_x(),Bbqueen.winfo_y()),WR1=crd(Bwrook.winfo_x(),Bwrook.winfo_y()),WR2=crd(Bwrook1.winfo_x(),Bwrook1.winfo_y()),WBI1=crd(Bwbish.winfo_x(),Bwbish.winfo_y()),WBI2=crd(Bwbish1.winfo_x(),Bwbish1.winfo_y()),WN1=crd(Bwnit.winfo_x(),Bwnit.winfo_y()),WN2=crd(Bwnit1.winfo_x(),Bwnit1.winfo_y()),WK=crd(Bwking.winfo_x(),Bwking.winfo_y()),WQ=crd(Bwqueen.winfo_x(),Bwqueen.winfo_y()))
            terminator(Wbpawn1)
            sw.unbind("<Button-1>")
        except :
            print("click in the box not on the button")
            xi=2
        if xi==2:
            pass
        else:
            changer(1)
    
    sw.bind("<Button-1>",mover2)
    
def draggerWP3():
     global cx
     global cy
     cx=Wbpawn2.winfo_x() 
     cy=Wbpawn2.winfo_y()
     print(cx,',',cy)
        
def moverWP3():
    
    global sw
    global cx
    global cy
    def mover2(event):
        global n2
        global Wbpawn2
        x=event.x
        y=event.y
        smy=cy-136
        smx=cx
        nx=cx
        ny=cy-68
        if (x<(cx+141)and x>(cx+67)) and (y<(cy-8) and y>(cy-76)):
            nx=cx+75
            ny=cy-68
            n2=0
        elif (x<(cx-13)and x>(cx-87)) and (y<(cy-8) and y>(cy-76)):
            nx=cx-75
            ny=cy-68
            n2=0
        while n2==1:
            if y<467:
                nx=smx
                ny=smy
                
            n2=0
        Wbpawn2.place(x=nx,y=ny)
        xi=1
        try:
            Peices_info(WP1=crd(Wbpawn.winfo_x(),Wbpawn.winfo_y()),WP2=crd(Wbpawn1.winfo_x(),Wbpawn1.winfo_y()),WP3=crd(nx,ny),WP4=crd(Wbpawn3.winfo_x(),Wbpawn3.winfo_y()),WP5=crd(Wbpawn4.winfo_x(),Wbpawn4.winfo_y()),WP6=crd(Wbpawn5.winfo_x(),Wbpawn5.winfo_y()),WP7=crd(Wbpawn6.winfo_x(),Wbpawn6.winfo_y()),WP8=crd(Wbpawn7.winfo_x(),Wbpawn7.winfo_y()),BP1=crd(Bbpawn.winfo_x(),Bbpawn.winfo_y()),BP2=crd(Bbpawn2.winfo_x(),Bbpawn2.winfo_y()),BP3=crd(Bbpawn3.winfo_x(),Bbpawn3.winfo_y()),BP4=crd(Bbpawn4.winfo_x(),Bbpawn4.winfo_y()),BP5=crd(Bbpawn5.winfo_x(),Bbpawn5.winfo_y()),BP6=crd(Bbpawn6.winfo_x(),Bbpawn6.winfo_y()),BP7=crd(Bbpawn7.winfo_x(),Bbpawn7.winfo_y()),BP8=crd(Bbpawn8.winfo_x(),Bbpawn8.winfo_y()),BR1=crd(Bbrook.winfo_x(),Bbrook.winfo_y()),BR2=crd(Bbrook1.winfo_x(),Bbrook1.winfo_y()),BBI1=crd(Bbbish.winfo_x(),Bbbish.winfo_y()),BBI2=crd(Bbbish1.winfo_x(),Bbbish1.winfo_y()),BN1=crd(Bbnit.winfo_x(),Bbnit.winfo_y()),BN2=crd(Bbnit1.winfo_x(),Bbnit1.winfo_y()),BK=crd(Bbking.winfo_x(),Bbking.winfo_y()),BQ=crd(Bbqueen.winfo_x(),Bbqueen.winfo_y()),WR1=crd(Bwrook.winfo_x(),Bwrook.winfo_y()),WR2=crd(Bwrook1.winfo_x(),Bwrook1.winfo_y()),WBI1=crd(Bwbish.winfo_x(),Bwbish.winfo_y()),WBI2=crd(Bwbish1.winfo_x(),Bwbish1.winfo_y()),WN1=crd(Bwnit.winfo_x(),Bwnit.winfo_y()),WN2=crd(Bwnit1.winfo_x(),Bwnit1.winfo_y()),WK=crd(Bwking.winfo_x(),Bwking.winfo_y()),WQ=crd(Bwqueen.winfo_x(),Bwqueen.winfo_y()))
            terminator(Wbpawn2)
            sw.unbind("<Button-1>")
        except :
            print("click in the box not on the button")
            xi=2
        if xi==2:
            pass
        else:
            changer(1)
    sw.bind("<Button-1>",mover2)
         
def draggerWP4():
     global cx
     global cy
     cx=Wbpawn3.winfo_x() 
     cy=Wbpawn3.winfo_y()
     print(cx,',',cy)
        
def moverWP4():
    
    global sw
    global cx
    global cy
    def mover2(event):
        global n3
        global Wbpawn3
        x=event.x
        y=event.y
        smy=cy-136
        smx=cx
        nx=cx
        ny=cy-68
        if (x<(cx+141)and x>(cx+67)) and (y<(cy-8) and y>(cy-76)):
            nx=cx+75
            ny=cy-68
            n3=0
        elif (x<(cx-13)and x>(cx-87)) and (y<(cy-8) and y>(cy-76)):
            nx=cx-75
            ny=cy-68
            n3=0
        while n3==1:
            if y<467:
                nx=smx
                ny=smy
                5
            n3=0
        Wbpawn3.place(x=nx,y=ny)
        xi=1
        try:
            Peices_info(WP1=crd(Wbpawn.winfo_x(),Wbpawn.winfo_y()),WP2=crd(Wbpawn1.winfo_x(),Wbpawn1.winfo_y()),WP3=crd(Wbpawn2.winfo_x(),Wbpawn2.winfo_y()),WP4=crd(nx,ny),WP5=crd(Wbpawn4.winfo_x(),Wbpawn4.winfo_y()),WP6=crd(Wbpawn5.winfo_x(),Wbpawn5.winfo_y()),WP7=crd(Wbpawn6.winfo_x(),Wbpawn6.winfo_y()),WP8=crd(Wbpawn7.winfo_x(),Wbpawn7.winfo_y()),BP1=crd(Bbpawn.winfo_x(),Bbpawn.winfo_y()),BP2=crd(Bbpawn2.winfo_x(),Bbpawn2.winfo_y()),BP3=crd(Bbpawn3.winfo_x(),Bbpawn3.winfo_y()),BP4=crd(Bbpawn4.winfo_x(),Bbpawn4.winfo_y()),BP5=crd(Bbpawn5.winfo_x(),Bbpawn5.winfo_y()),BP6=crd(Bbpawn6.winfo_x(),Bbpawn6.winfo_y()),BP7=crd(Bbpawn7.winfo_x(),Bbpawn7.winfo_y()),BP8=crd(Bbpawn8.winfo_x(),Bbpawn8.winfo_y()),BR1=crd(Bbrook.winfo_x(),Bbrook.winfo_y()),BR2=crd(Bbrook1.winfo_x(),Bbrook1.winfo_y()),BBI1=crd(Bbbish.winfo_x(),Bbbish.winfo_y()),BBI2=crd(Bbbish1.winfo_x(),Bbbish1.winfo_y()),BN1=crd(Bbnit.winfo_x(),Bbnit.winfo_y()),BN2=crd(Bbnit1.winfo_x(),Bbnit1.winfo_y()),BK=crd(Bbking.winfo_x(),Bbking.winfo_y()),BQ=crd(Bbqueen.winfo_x(),Bbqueen.winfo_y()),WR1=crd(Bwrook.winfo_x(),Bwrook.winfo_y()),WR2=crd(Bwrook1.winfo_x(),Bwrook1.winfo_y()),WBI1=crd(Bwbish.winfo_x(),Bwbish.winfo_y()),WBI2=crd(Bwbish1.winfo_x(),Bwbish1.winfo_y()),WN1=crd(Bwnit.winfo_x(),Bwnit.winfo_y()),WN2=crd(Bwnit1.winfo_x(),Bwnit1.winfo_y()),WK=crd(Bwking.winfo_x(),Bwking.winfo_y()),WQ=crd(Bwqueen.winfo_x(),Bwqueen.winfo_y()))
            terminator(Wbpawn3)
            sw.unbind("<Button-1>")
        except :
            print("click in the box not on the button")
            xi=2
        if xi==2:
            pass
        else:
            changer(1)
    sw.bind("<Button-1>",mover2)    

def draggerWP5():
     global cx
     global cy
     cx=Wbpawn4.winfo_x() 
     cy=Wbpawn4.winfo_y()
     print(cx,',',cy)
        
def moverWP5():
    
    global sw
    global cx
    global cy
    def mover2(event):
        global n4
        global Wbpawn4
        x=event.x
        y=event.y
        smy=cy-136
        smx=cx
        nx=cx
        ny=cy-68
        if (x<(cx+141)and x>(cx+67)) and (y<(cy-8) and y>(cy-76)):
            nx=cx+75
            ny=cy-68
            n4=0
        elif (x<(cx-13)and x>(cx-87)) and (y<(cy-8) and y>(cy-76)):
            nx=cx-75
            ny=cy-68
            n4=0
        while n4==1:
            if y<467:
                nx=smx
                ny=smy
                
            n4=0
        Wbpawn4.place(x=nx,y=ny)
        xi=1
        try:
            Peices_info(WP1=crd(Wbpawn.winfo_x(),Wbpawn.winfo_y()),WP2=crd(Wbpawn1.winfo_x(),Wbpawn1.winfo_y()),WP3=crd(Wbpawn2.winfo_x(),Wbpawn2.winfo_y()),WP4=crd(Wbpawn3.winfo_x(),Wbpawn3.winfo_y()),WP5=crd(nx,ny),WP6=crd(Wbpawn5.winfo_x(),Wbpawn5.winfo_y()),WP7=crd(Wbpawn6.winfo_x(),Wbpawn6.winfo_y()),WP8=crd(Wbpawn7.winfo_x(),Wbpawn7.winfo_y()),BP1=crd(Bbpawn.winfo_x(),Bbpawn.winfo_y()),BP2=crd(Bbpawn2.winfo_x(),Bbpawn2.winfo_y()),BP3=crd(Bbpawn3.winfo_x(),Bbpawn3.winfo_y()),BP4=crd(Bbpawn4.winfo_x(),Bbpawn4.winfo_y()),BP5=crd(Bbpawn5.winfo_x(),Bbpawn5.winfo_y()),BP6=crd(Bbpawn6.winfo_x(),Bbpawn6.winfo_y()),BP7=crd(Bbpawn7.winfo_x(),Bbpawn7.winfo_y()),BP8=crd(Bbpawn8.winfo_x(),Bbpawn8.winfo_y()),BR1=crd(Bbrook.winfo_x(),Bbrook.winfo_y()),BR2=crd(Bbrook1.winfo_x(),Bbrook1.winfo_y()),BBI1=crd(Bbbish.winfo_x(),Bbbish.winfo_y()),BBI2=crd(Bbbish1.winfo_x(),Bbbish1.winfo_y()),BN1=crd(Bbnit.winfo_x(),Bbnit.winfo_y()),BN2=crd(Bbnit1.winfo_x(),Bbnit1.winfo_y()),BK=crd(Bbking.winfo_x(),Bbking.winfo_y()),BQ=crd(Bbqueen.winfo_x(),Bbqueen.winfo_y()),WR1=crd(Bwrook.winfo_x(),Bwrook.winfo_y()),WR2=crd(Bwrook1.winfo_x(),Bwrook1.winfo_y()),WBI1=crd(Bwbish.winfo_x(),Bwbish.winfo_y()),WBI2=crd(Bwbish1.winfo_x(),Bwbish1.winfo_y()),WN1=crd(Bwnit.winfo_x(),Bwnit.winfo_y()),WN2=crd(Bwnit1.winfo_x(),Bwnit1.winfo_y()),WK=crd(Bwking.winfo_x(),Bwking.winfo_y()),WQ=crd(Bwqueen.winfo_x(),Bwqueen.winfo_y()))
            terminator(Wbpawn4)
            sw.unbind("<Button-1>")
        except :
            print("click in the box not on the button")
            xi=2
        if xi==2:
            pass
        else:
            changer(1)
    sw.bind("<Button-1>",mover2)

def draggerWP6():
     global cx
     global cy
     cx=Wbpawn5.winfo_x() 
     cy=Wbpawn5.winfo_y()
     print(cx,',',cy)
            
def moverWP6():
    
    global sw
    global cx
    global cy
    def mover2(event):
        global n5
        global Wbpawn5
        x=event.x
        y=event.y
        smy=cy-136
        smx=cx
        nx=cx
        ny=cy-68
        if (x<(cx+141)and x>(cx+67)) and (y<(cy-8) and y>(cy-76)):
            nx=cx+75
            ny=cy-68
            n5=0
        elif (x<(cx-13)and x>(cx-87)) and (y<(cy-8) and y>(cy-76)):
            nx=cx-75
            ny=cy-68
            n5=0
        while n5==1:
            if y<467:
                nx=smx
                ny=smy
                
            n5=0
        Wbpawn5.place(x=nx,y=ny)
        xi=1
        try:
            Peices_info(WP1=crd(Wbpawn.winfo_x(),Wbpawn.winfo_y()),WP2=crd(Wbpawn1.winfo_x(),Wbpawn1.winfo_y()),WP3=crd(Wbpawn2.winfo_x(),Wbpawn2.winfo_y()),WP4=crd(Wbpawn3.winfo_x(),Wbpawn3.winfo_y()),WP5=crd(Wbpawn4.winfo_x(),Wbpawn4.winfo_y()),WP6=crd(nx,ny),WP7=crd(Wbpawn6.winfo_x(),Wbpawn6.winfo_y()),WP8=crd(Wbpawn7.winfo_x(),Wbpawn7.winfo_y()),BP1=crd(Bbpawn.winfo_x(),Bbpawn.winfo_y()),BP2=crd(Bbpawn2.winfo_x(),Bbpawn2.winfo_y()),BP3=crd(Bbpawn3.winfo_x(),Bbpawn3.winfo_y()),BP4=crd(Bbpawn4.winfo_x(),Bbpawn4.winfo_y()),BP5=crd(Bbpawn5.winfo_x(),Bbpawn5.winfo_y()),BP6=crd(Bbpawn6.winfo_x(),Bbpawn6.winfo_y()),BP7=crd(Bbpawn7.winfo_x(),Bbpawn7.winfo_y()),BP8=crd(Bbpawn8.winfo_x(),Bbpawn8.winfo_y()),BR1=crd(Bbrook.winfo_x(),Bbrook.winfo_y()),BR2=crd(Bbrook1.winfo_x(),Bbrook1.winfo_y()),BBI1=crd(Bbbish.winfo_x(),Bbbish.winfo_y()),BBI2=crd(Bbbish1.winfo_x(),Bbbish1.winfo_y()),BN1=crd(Bbnit.winfo_x(),Bbnit.winfo_y()),BN2=crd(Bbnit1.winfo_x(),Bbnit1.winfo_y()),BK=crd(Bbking.winfo_x(),Bbking.winfo_y()),BQ=crd(Bbqueen.winfo_x(),Bbqueen.winfo_y()),WR1=crd(Bwrook.winfo_x(),Bwrook.winfo_y()),WR2=crd(Bwrook1.winfo_x(),Bwrook1.winfo_y()),WBI1=crd(Bwbish.winfo_x(),Bwbish.winfo_y()),WBI2=crd(Bwbish1.winfo_x(),Bwbish1.winfo_y()),WN1=crd(Bwnit.winfo_x(),Bwnit.winfo_y()),WN2=crd(Bwnit1.winfo_x(),Bwnit1.winfo_y()),WK=crd(Bwking.winfo_x(),Bwking.winfo_y()),WQ=crd(Bwqueen.winfo_x(),Bwqueen.winfo_y()))
            terminator(Wbpawn5)
            sw.unbind("<Button-1>")
        except :
            print("click in the box not on the button")
            xi=2
        if xi==2:
            pass
        else:
            changer(1)
    sw.bind("<Button-1>",mover2)

def draggerWP7():
     global cx
     global cy
     cx=Wbpawn6.winfo_x() 
     cy=Wbpawn6.winfo_y()
     print(cx,',',cy)
        
def moverWP7():
    
    global sw
    global cx
    global cy
    def mover2(event):
        global n6
        global Wbpawn6
        x=event.x
        y=event.y
        smy=cy-136
        smx=cx
        nx=cx
        ny=cy-68
        if (x<(cx+141)and x>(cx+67)) and (y<(cy-8) and y>(cy-76)):
            nx=cx+75
            ny=cy-68
            n6=0
        elif (x<(cx-13)and x>(cx-87)) and (y<(cy-8) and y>(cy-76)):
            nx=cx-75
            ny=cy-68
            n6=0
        while n6==1:
            if y<467:
                nx=smx
                ny=smy
                
            n6=0
        Wbpawn6.place(x=nx,y=ny)
        xi=1
        try:
            Peices_info(WP1=crd(Wbpawn.winfo_x(),Wbpawn.winfo_y()),WP2=crd(Wbpawn1.winfo_x(),Wbpawn1.winfo_y()),WP3=crd(Wbpawn2.winfo_x(),Wbpawn2.winfo_y()),WP4=crd(Wbpawn3.winfo_x(),Wbpawn3.winfo_y()),WP5=crd(Wbpawn4.winfo_x(),Wbpawn4.winfo_y()),WP6=crd(Wbpawn5.winfo_x(),Wbpawn5.winfo_y()),WP7=crd(nx,ny),WP8=crd(Wbpawn7.winfo_x(),Wbpawn7.winfo_y()),BP1=crd(Bbpawn.winfo_x(),Bbpawn.winfo_y()),BP2=crd(Bbpawn2.winfo_x(),Bbpawn2.winfo_y()),BP3=crd(Bbpawn3.winfo_x(),Bbpawn3.winfo_y()),BP4=crd(Bbpawn4.winfo_x(),Bbpawn4.winfo_y()),BP5=crd(Bbpawn5.winfo_x(),Bbpawn5.winfo_y()),BP6=crd(Bbpawn6.winfo_x(),Bbpawn6.winfo_y()),BP7=crd(Bbpawn7.winfo_x(),Bbpawn7.winfo_y()),BP8=crd(Bbpawn8.winfo_x(),Bbpawn8.winfo_y()),BR1=crd(Bbrook.winfo_x(),Bbrook.winfo_y()),BR2=crd(Bbrook1.winfo_x(),Bbrook1.winfo_y()),BBI1=crd(Bbbish.winfo_x(),Bbbish.winfo_y()),BBI2=crd(Bbbish1.winfo_x(),Bbbish1.winfo_y()),BN1=crd(Bbnit.winfo_x(),Bbnit.winfo_y()),BN2=crd(Bbnit1.winfo_x(),Bbnit1.winfo_y()),BK=crd(Bbking.winfo_x(),Bbking.winfo_y()),BQ=crd(Bbqueen.winfo_x(),Bbqueen.winfo_y()),WR1=crd(Bwrook.winfo_x(),Bwrook.winfo_y()),WR2=crd(Bwrook1.winfo_x(),Bwrook1.winfo_y()),WBI1=crd(Bwbish.winfo_x(),Bwbish.winfo_y()),WBI2=crd(Bwbish1.winfo_x(),Bwbish1.winfo_y()),WN1=crd(Bwnit.winfo_x(),Bwnit.winfo_y()),WN2=crd(Bwnit1.winfo_x(),Bwnit1.winfo_y()),WK=crd(Bwking.winfo_x(),Bwking.winfo_y()),WQ=crd(Bwqueen.winfo_x(),Bwqueen.winfo_y()))
            terminator(Wbpawn6)
            sw.unbind("<Button-1>")
        except :
            print("click in the box not on the button")
            xi=2
        if xi==2:
            pass
        else:
            changer(1)
    sw.bind("<Button-1>",mover2)

def draggerWP8():
     global cx
     global cy
     cx=Wbpawn7.winfo_x() 
     cy=Wbpawn7.winfo_y()
     print(cx,',',cy)
        
def moverWP8():
    
    global sw
    global cx
    global cy
    def mover2(event):
        global n7
        global Wbpawn7
        x=event.x
        y=event.y
        smy=cy-136
        smx=cx
        nx=cx
        ny=cy-68
        if (x<(cx+141)and x>(cx+67)) and (y<(cy-8) and y>(cy-76)):
            nx=cx+75
            ny=cy-68
            n7=0
        elif (x<(cx-13)and x>(cx-87)) and (y<(cy-8) and y>(cy-76)):
            nx=cx-75
            ny=cy-68
            n7=0
        while n7==1:
            if y<467:
                nx=smx
                ny=smy
            n7=0
        Wbpawn7.place(x=nx,y=ny)
        xi=1
        try:
            Peices_info(WP1=crd(Wbpawn.winfo_x(),Wbpawn.winfo_y()),WP2=crd(Wbpawn1.winfo_x(),Wbpawn1.winfo_y()),WP3=crd(Wbpawn2.winfo_x(),Wbpawn2.winfo_y()),WP4=crd(Wbpawn3.winfo_x(),Wbpawn3.winfo_y()),WP5=crd(Wbpawn4.winfo_x(),Wbpawn4.winfo_y()),WP6=crd(Wbpawn5.winfo_x(),Wbpawn5.winfo_y()),WP7=crd(Wbpawn6.winfo_x(),Wbpawn6.winfo_y()),WP8=crd(nx,ny),BP1=crd(Bbpawn.winfo_x(),Bbpawn.winfo_y()),BP2=crd(Bbpawn2.winfo_x(),Bbpawn2.winfo_y()),BP3=crd(Bbpawn3.winfo_x(),Bbpawn3.winfo_y()),BP4=crd(Bbpawn4.winfo_x(),Bbpawn4.winfo_y()),BP5=crd(Bbpawn5.winfo_x(),Bbpawn5.winfo_y()),BP6=crd(Bbpawn6.winfo_x(),Bbpawn6.winfo_y()),BP7=crd(Bbpawn7.winfo_x(),Bbpawn7.winfo_y()),BP8=crd(Bbpawn8.winfo_x(),Bbpawn8.winfo_y()),BR1=crd(Bbrook.winfo_x(),Bbrook.winfo_y()),BR2=crd(Bbrook1.winfo_x(),Bbrook1.winfo_y()),BBI1=crd(Bbbish.winfo_x(),Bbbish.winfo_y()),BBI2=crd(Bbbish1.winfo_x(),Bbbish1.winfo_y()),BN1=crd(Bbnit.winfo_x(),Bbnit.winfo_y()),BN2=crd(Bbnit1.winfo_x(),Bbnit1.winfo_y()),BK=crd(Bbking.winfo_x(),Bbking.winfo_y()),BQ=crd(Bbqueen.winfo_x(),Bbqueen.winfo_y()),WR1=crd(Bwrook.winfo_x(),Bwrook.winfo_y()),WR2=crd(Bwrook1.winfo_x(),Bwrook1.winfo_y()),WBI1=crd(Bwbish.winfo_x(),Bwbish.winfo_y()),WBI2=crd(Bwbish1.winfo_x(),Bwbish1.winfo_y()),WN1=crd(Bwnit.winfo_x(),Bwnit.winfo_y()),WN2=crd(Bwnit1.winfo_x(),Bwnit1.winfo_y()),WK=crd(Bwking.winfo_x(),Bwking.winfo_y()),WQ=crd(Bwqueen.winfo_x(),Bwqueen.winfo_y()))
            terminator(Wbpawn7)
            sw.unbind("<Button-1>")
        except :
            print("click in the box not on the button")
            xi=2
        if xi==2:
            pass
        else:
            changer(1)
    sw.bind("<Button-1>",mover2)
    
def draggerBP1():
     global Bbpawn
     global cx
     global cy
     cx=Bbpawn.winfo_x() 
     cy=Bbpawn.winfo_y()
     print(cx,',',cy)
            
def moverBP1():

    global sw
    global cx
    global cy
    def mover2(event):
        global n8
        global Bbpawn
        x=event.x
        y=event.y
        smy=cy+136
        smx=cx
        nx=cx
        ny=cy+68
        if (x<(cx+141)and x>(cx+67)) and (y<(cy+128) and y>(cy+60)):
            nx=cx+75
            ny=cy+68
            n8=0
        elif (x<(cx-13)and x>(cx-87)) and (y<(cy+128) and y>(cy+60)):
            nx=cx-75
            ny=cy+68
            n8=0            
        while n8==1:
            if y>330 or y<263:
                nx=smx
                ny=smy
                
            n8=0
        Bbpawn.place(x=nx,y=ny)
        xi=1
        try:
            Peices_info(WP1=crd(Wbpawn.winfo_x(),Wbpawn.winfo_y()),WP2=crd(Wbpawn1.winfo_x(),Wbpawn1.winfo_y()),WP3=crd(Wbpawn2.winfo_x(),Wbpawn2.winfo_y()),WP4=crd(Wbpawn3.winfo_x(),Wbpawn3.winfo_y()),WP5=crd(Wbpawn4.winfo_x(),Wbpawn4.winfo_y()),WP6=crd(Wbpawn5.winfo_x(),Wbpawn5.winfo_y()),WP7=crd(Wbpawn6.winfo_x(),Wbpawn6.winfo_y()),WP8=crd(Wbpawn7.winfo_x(),Wbpawn7.winfo_y()),BP1=crd(nx,ny),BP2=crd(Bbpawn2.winfo_x(),Bbpawn2.winfo_y()),BP3=crd(Bbpawn3.winfo_x(),Bbpawn3.winfo_y()),BP4=crd(Bbpawn4.winfo_x(),Bbpawn4.winfo_y()),BP5=crd(Bbpawn5.winfo_x(),Bbpawn5.winfo_y()),BP6=crd(Bbpawn6.winfo_x(),Bbpawn6.winfo_y()),BP7=crd(Bbpawn7.winfo_x(),Bbpawn7.winfo_y()),BP8=crd(Bbpawn8.winfo_x(),Bbpawn8.winfo_y()),BR1=crd(Bbrook.winfo_x(),Bbrook.winfo_y()),BR2=crd(Bbrook1.winfo_x(),Bbrook1.winfo_y()),BBI1=crd(Bbbish.winfo_x(),Bbbish.winfo_y()),BBI2=crd(Bbbish1.winfo_x(),Bbbish1.winfo_y()),BN1=crd(Bbnit.winfo_x(),Bbnit.winfo_y()),BN2=crd(Bbnit1.winfo_x(),Bbnit1.winfo_y()),BK=crd(Bbking.winfo_x(),Bbking.winfo_y()),BQ=crd(Bbqueen.winfo_x(),Bbqueen.winfo_y()),WR1=crd(Bwrook.winfo_x(),Bwrook.winfo_y()),WR2=crd(Bwrook1.winfo_x(),Bwrook1.winfo_y()),WBI1=crd(Bwbish.winfo_x(),Bwbish.winfo_y()),WBI2=crd(Bwbish1.winfo_x(),Bwbish1.winfo_y()),WN1=crd(Bwnit.winfo_x(),Bwnit.winfo_y()),WN2=crd(Bwnit1.winfo_x(),Bwnit1.winfo_y()),WK=crd(Bwking.winfo_x(),Bwking.winfo_y()),WQ=crd(Bwqueen.winfo_x(),Bwqueen.winfo_y()))
            terminator(Bbpawn)
            sw.unbind("<Button-1>")
        except :
            print("click in the box not on the button")
            xi=2
        if xi==2:
            pass
        else:
            changer(2)
    sw.bind("<Button-1>",mover2)    

def draggerBP2():
     global Bbpawn2
     global cx
     global cy
     cx=Bbpawn2.winfo_x() 
     cy=Bbpawn2.winfo_y()
     print(cx,',',cy)
    
def moverBP2():
    
    global sw
    global cx
    global cy
    def mover2(event):
        global n9
        global Bbpawn2
        x=event.x
        y=event.y
        smy=cy+136
        smx=cx
        nx=cx
        ny=cy+68
        if (x<(cx+141)and x>(cx+67)) and (y<(cy+128) and y>(cy+60)):
            nx=cx+75
            ny=cy+68
            n9=0
        elif (x<(cx-13)and x>(cx-87)) and (y<(cy+128) and y>(cy+60)):
            nx=cx-75
            ny=cy+68
            n9=0
        while n9==1:
            if y>330 or y<263:
                nx=smx
                ny=smy
                
            n9=0
        Bbpawn2.place(x=nx,y=ny)
        xi=1
        try:
            Peices_info(WP1=crd(Wbpawn.winfo_x(),Wbpawn.winfo_y()),WP2=crd(Wbpawn1.winfo_x(),Wbpawn1.winfo_y()),WP3=crd(Wbpawn2.winfo_x(),Wbpawn2.winfo_y()),WP4=crd(Wbpawn3.winfo_x(),Wbpawn3.winfo_y()),WP5=crd(Wbpawn4.winfo_x(),Wbpawn4.winfo_y()),WP6=crd(Wbpawn5.winfo_x(),Wbpawn5.winfo_y()),WP7=crd(Wbpawn6.winfo_x(),Wbpawn6.winfo_y()),WP8=crd(Wbpawn7.winfo_x(),Wbpawn7.winfo_y()),BP1=crd(Bbpawn.winfo_x(),Bbpawn.winfo_y()),BP2=crd(nx,ny),BP3=crd(Bbpawn3.winfo_x(),Bbpawn3.winfo_y()),BP4=crd(Bbpawn4.winfo_x(),Bbpawn4.winfo_y()),BP5=crd(Bbpawn5.winfo_x(),Bbpawn5.winfo_y()),BP6=crd(Bbpawn6.winfo_x(),Bbpawn6.winfo_y()),BP7=crd(Bbpawn7.winfo_x(),Bbpawn7.winfo_y()),BP8=crd(Bbpawn8.winfo_x(),Bbpawn8.winfo_y()),BR1=crd(Bbrook.winfo_x(),Bbrook.winfo_y()),BR2=crd(Bbrook1.winfo_x(),Bbrook1.winfo_y()),BBI1=crd(Bbbish.winfo_x(),Bbbish.winfo_y()),BBI2=crd(Bbbish1.winfo_x(),Bbbish1.winfo_y()),BN1=crd(Bbnit.winfo_x(),Bbnit.winfo_y()),BN2=crd(Bbnit1.winfo_x(),Bbnit1.winfo_y()),BK=crd(Bbking.winfo_x(),Bbking.winfo_y()),BQ=crd(Bbqueen.winfo_x(),Bbqueen.winfo_y()),WR1=crd(Bwrook.winfo_x(),Bwrook.winfo_y()),WR2=crd(Bwrook1.winfo_x(),Bwrook1.winfo_y()),WBI1=crd(Bwbish.winfo_x(),Bwbish.winfo_y()),WBI2=crd(Bwbish1.winfo_x(),Bwbish1.winfo_y()),WN1=crd(Bwnit.winfo_x(),Bwnit.winfo_y()),WN2=crd(Bwnit1.winfo_x(),Bwnit1.winfo_y()),WK=crd(Bwking.winfo_x(),Bwking.winfo_y()),WQ=crd(Bwqueen.winfo_x(),Bwqueen.winfo_y()))
            terminator(Bbpawn2)
            sw.unbind("<Button-1>")
        except :
            print("click in the box not on the button")
            xi=2
        if xi==2:
            pass
        else:
            changer(2)
    sw.bind("<Button-1>",mover2)
    
def draggerBP3():
     global Bbpawn3
     global cx
     global cy
     cx=Bbpawn3.winfo_x() 
     cy=Bbpawn3.winfo_y()
     print(cx,',',cy)
           
def moverBP3():
    
    global sw
    global cx
    global cy
    def mover2(event):
        global n10
        global Bbpawn3
        x=event.x
        y=event.y
        smy=cy+136
        smx=cx
        nx=cx
        ny=cy+68
        if (x<(cx+141)and x>(cx+67)) and (y<(cy+128) and y>(cy+60)):
            nx=cx+75
            ny=cy+68
            n10=0
        elif (x<(cx-13)and x>(cx-87)) and (y<(cy+128) and y>(cy+60)):
            nx=cx-75
            ny=cy+68
            n10=0
        while n10==1:
            if y>330 or y<263:
                nx=smx
                ny=smy
                
            n10=0
        Bbpawn3.place(x=nx,y=ny)
        xi=1
        try:
            Peices_info(WP1=crd(Wbpawn.winfo_x(),Wbpawn.winfo_y()),WP2=crd(Wbpawn1.winfo_x(),Wbpawn1.winfo_y()),WP3=crd(Wbpawn2.winfo_x(),Wbpawn2.winfo_y()),WP4=crd(Wbpawn3.winfo_x(),Wbpawn3.winfo_y()),WP5=crd(Wbpawn4.winfo_x(),Wbpawn4.winfo_y()),WP6=crd(Wbpawn5.winfo_x(),Wbpawn5.winfo_y()),WP7=crd(Wbpawn6.winfo_x(),Wbpawn6.winfo_y()),WP8=crd(Wbpawn7.winfo_x(),Wbpawn7.winfo_y()),BP1=crd(Bbpawn.winfo_x(),Bbpawn.winfo_y()),BP2=crd(Bbpawn2.winfo_x(),Bbpawn2.winfo_y()),BP3=crd(nx,ny),BP4=crd(Bbpawn4.winfo_x(),Bbpawn4.winfo_y()),BP5=crd(Bbpawn5.winfo_x(),Bbpawn5.winfo_y()),BP6=crd(Bbpawn6.winfo_x(),Bbpawn6.winfo_y()),BP7=crd(Bbpawn7.winfo_x(),Bbpawn7.winfo_y()),BP8=crd(Bbpawn8.winfo_x(),Bbpawn8.winfo_y()),BR1=crd(Bbrook.winfo_x(),Bbrook.winfo_y()),BR2=crd(Bbrook1.winfo_x(),Bbrook1.winfo_y()),BBI1=crd(Bbbish.winfo_x(),Bbbish.winfo_y()),BBI2=crd(Bbbish1.winfo_x(),Bbbish1.winfo_y()),BN1=crd(Bbnit.winfo_x(),Bbnit.winfo_y()),BN2=crd(Bbnit1.winfo_x(),Bbnit1.winfo_y()),BK=crd(Bbking.winfo_x(),Bbking.winfo_y()),BQ=crd(Bbqueen.winfo_x(),Bbqueen.winfo_y()),WR1=crd(Bwrook.winfo_x(),Bwrook.winfo_y()),WR2=crd(Bwrook1.winfo_x(),Bwrook1.winfo_y()),WBI1=crd(Bwbish.winfo_x(),Bwbish.winfo_y()),WBI2=crd(Bwbish1.winfo_x(),Bwbish1.winfo_y()),WN1=crd(Bwnit.winfo_x(),Bwnit.winfo_y()),WN2=crd(Bwnit1.winfo_x(),Bwnit1.winfo_y()),WK=crd(Bwking.winfo_x(),Bwking.winfo_y()),WQ=crd(Bwqueen.winfo_x(),Bwqueen.winfo_y()))
            terminator(Bbpawn3)
            sw.unbind("<Button-1>")
        except :
            print("click in the box not on the button")
            xi=2
        if xi==2:
            pass
        else:
            changer(2)
    sw.bind("<Button-1>",mover2)
    
def draggerBP4():
     global Bbpawn4
     global cx
     global cy
     cx=Bbpawn4.winfo_x() 
     cy=Bbpawn4.winfo_y()
     print(cx,',',cy)
        
def moverBP4():
    
    global sw
    global cx
    global cy
    def mover2(event):
        global n11
        global Bbpawn4
        x=event.x
        y=event.y
        smy=cy+136
        smx=cx
        nx=cx
        ny=cy+68
        if (x<(cx+141)and x>(cx+67)) and (y<(cy+128) and y>(cy+60)):
            nx=cx+75
            ny=cy+68
            n11=0
        elif (x<(cx-13)and x>(cx-87)) and (y<(cy+128) and y>(cy+60)):
            nx=cx-75
            ny=cy+68
            n11=0
        while n11==1:
            if y>330 or y<263:
                nx=smx
                ny=smy
                
            n11=0
        Bbpawn4.place(x=nx,y=ny)
        xi=1
        try:
            Peices_info(WP1=crd(Wbpawn.winfo_x(),Wbpawn.winfo_y()),WP2=crd(Wbpawn1.winfo_x(),Wbpawn1.winfo_y()),WP3=crd(Wbpawn2.winfo_x(),Wbpawn2.winfo_y()),WP4=crd(Wbpawn3.winfo_x(),Wbpawn3.winfo_y()),WP5=crd(Wbpawn4.winfo_x(),Wbpawn4.winfo_y()),WP6=crd(Wbpawn5.winfo_x(),Wbpawn5.winfo_y()),WP7=crd(Wbpawn6.winfo_x(),Wbpawn6.winfo_y()),WP8=crd(Wbpawn7.winfo_x(),Wbpawn7.winfo_y()),BP1=crd(Bbpawn.winfo_x(),Bbpawn.winfo_y()),BP2=crd(Bbpawn2.winfo_x(),Bbpawn2.winfo_y()),BP3=crd(Bbpawn3.winfo_x(),Bbpawn3.winfo_y()),BP4=crd(nx,ny),BP5=crd(Bbpawn5.winfo_x(),Bbpawn5.winfo_y()),BP6=crd(Bbpawn6.winfo_x(),Bbpawn6.winfo_y()),BP7=crd(Bbpawn7.winfo_x(),Bbpawn7.winfo_y()),BP8=crd(Bbpawn8.winfo_x(),Bbpawn8.winfo_y()),BR1=crd(Bbrook.winfo_x(),Bbrook.winfo_y()),BR2=crd(Bbrook1.winfo_x(),Bbrook1.winfo_y()),BBI1=crd(Bbbish.winfo_x(),Bbbish.winfo_y()),BBI2=crd(Bbbish1.winfo_x(),Bbbish1.winfo_y()),BN1=crd(Bbnit.winfo_x(),Bbnit.winfo_y()),BN2=crd(Bbnit1.winfo_x(),Bbnit1.winfo_y()),BK=crd(Bbking.winfo_x(),Bbking.winfo_y()),BQ=crd(Bbqueen.winfo_x(),Bbqueen.winfo_y()),WR1=crd(Bwrook.winfo_x(),Bwrook.winfo_y()),WR2=crd(Bwrook1.winfo_x(),Bwrook1.winfo_y()),WBI1=crd(Bwbish.winfo_x(),Bwbish.winfo_y()),WBI2=crd(Bwbish1.winfo_x(),Bwbish1.winfo_y()),WN1=crd(Bwnit.winfo_x(),Bwnit.winfo_y()),WN2=crd(Bwnit1.winfo_x(),Bwnit1.winfo_y()),WK=crd(Bwking.winfo_x(),Bwking.winfo_y()),WQ=crd(Bwqueen.winfo_x(),Bwqueen.winfo_y()))
            terminator(Bbpawn4)
            sw.unbind("<Button-1>")
        except :
            print("click in the box not on the button")
            xi=2
        if xi==2:
            pass
        else:
            changer(2)
    sw.bind("<Button-1>",mover2) 
    
def draggerBP5():
     global Bbpawn5
     global cx
     global cy
     cx=Bbpawn5.winfo_x() 
     cy=Bbpawn5.winfo_y()
     print(cx,',',cy)
        
def moverBP5():
    
    global sw
    global cx
    global cy
    def mover2(event):
        global n12
        global Bbpawn5
        x=event.x
        y=event.y
        smy=cy+136
        smx=cx
        nx=cx
        ny=cy+68
        if (x<(cx+141)and x>(cx+67)) and (y<(cy+128) and y>(cy+60)):
            nx=cx+75
            ny=cy+68
            n12=0
        elif (x<(cx-13)and x>(cx-87)) and (y<(cy+128) and y>(cy+60)):
            nx=cx-75
            ny=cy+68
            n12=0
        while n12==1:
            if y>330 or y<263:
                nx=smx
                ny=smy
                
            n12=0
        Bbpawn5.place(x=nx,y=ny)
        xi=1
        try:
            Peices_info(WP1=crd(Wbpawn.winfo_x(),Wbpawn.winfo_y()),WP2=crd(Wbpawn1.winfo_x(),Wbpawn1.winfo_y()),WP3=crd(Wbpawn2.winfo_x(),Wbpawn2.winfo_y()),WP4=crd(Wbpawn3.winfo_x(),Wbpawn3.winfo_y()),WP5=crd(Wbpawn4.winfo_x(),Wbpawn4.winfo_y()),WP6=crd(Wbpawn5.winfo_x(),Wbpawn5.winfo_y()),WP7=crd(Wbpawn6.winfo_x(),Wbpawn6.winfo_y()),WP8=crd(Wbpawn7.winfo_x(),Wbpawn7.winfo_y()),BP1=crd(Bbpawn.winfo_x(),Bbpawn.winfo_y()),BP2=crd(Bbpawn2.winfo_x(),Bbpawn2.winfo_y()),BP3=crd(Bbpawn3.winfo_x(),Bbpawn3.winfo_y()),BP4=crd(Bbpawn4.winfo_x(),Bbpawn4.winfo_y()),BP5=crd(nx,ny),BP6=crd(Bbpawn6.winfo_x(),Bbpawn6.winfo_y()),BP7=crd(Bbpawn7.winfo_x(),Bbpawn7.winfo_y()),BP8=crd(Bbpawn8.winfo_x(),Bbpawn8.winfo_y()),BR1=crd(Bbrook.winfo_x(),Bbrook.winfo_y()),BR2=crd(Bbrook1.winfo_x(),Bbrook1.winfo_y()),BBI1=crd(Bbbish.winfo_x(),Bbbish.winfo_y()),BBI2=crd(Bbbish1.winfo_x(),Bbbish1.winfo_y()),BN1=crd(Bbnit.winfo_x(),Bbnit.winfo_y()),BN2=crd(Bbnit1.winfo_x(),Bbnit1.winfo_y()),BK=crd(Bbking.winfo_x(),Bbking.winfo_y()),BQ=crd(Bbqueen.winfo_x(),Bbqueen.winfo_y()),WR1=crd(Bwrook.winfo_x(),Bwrook.winfo_y()),WR2=crd(Bwrook1.winfo_x(),Bwrook1.winfo_y()),WBI1=crd(Bwbish.winfo_x(),Bwbish.winfo_y()),WBI2=crd(Bwbish1.winfo_x(),Bwbish1.winfo_y()),WN1=crd(Bwnit.winfo_x(),Bwnit.winfo_y()),WN2=crd(Bwnit1.winfo_x(),Bwnit1.winfo_y()),WK=crd(Bwking.winfo_x(),Bwking.winfo_y()),WQ=crd(Bwqueen.winfo_x(),Bwqueen.winfo_y()))
            terminator(Bbpawn5)
            sw.unbind("<Button-1>")
        except :
            print("click in the box not on the button")
            xi=2
        if xi==2:
            pass
        else:
            changer(2)
    sw.bind("<Button-1>",mover2)

def draggerBP6():
     global Bbpawn6
     global cx
     global cy
     cx=Bbpawn6.winfo_x() 
     cy=Bbpawn6.winfo_y()
     print(cx,',',cy)
        
def moverBP6():
    
    global sw
    global cx
    global cy
    def mover2(event):
        global n13
        global Bbpawn6
        x=event.x
        y=event.y
        smy=cy+136
        smx=cx
        nx=cx
        ny=cy+68
        if (x<(cx+141)and x>(cx+67)) and (y<(cy+128) and y>(cy+60)):
            nx=cx+75
            ny=cy+68
            n13=0
        elif (x<(cx-13)and x>(cx-87)) and (y<(cy+128) and y>(cy+60)):
            nx=cx-75
            ny=cy+68
            n13=0
        while n13==1:
            if y>330 or y<263:
                nx=smx
                ny=smy
                
            n13=0
        Bbpawn6.place(x=nx,y=ny)
        xi=1
        try:
            Peices_info(WP1=crd(Wbpawn.winfo_x(),Wbpawn.winfo_y()),WP2=crd(Wbpawn1.winfo_x(),Wbpawn1.winfo_y()),WP3=crd(Wbpawn2.winfo_x(),Wbpawn2.winfo_y()),WP4=crd(Wbpawn3.winfo_x(),Wbpawn3.winfo_y()),WP5=crd(Wbpawn4.winfo_x(),Wbpawn4.winfo_y()),WP6=crd(Wbpawn5.winfo_x(),Wbpawn5.winfo_y()),WP7=crd(Wbpawn6.winfo_x(),Wbpawn6.winfo_y()),WP8=crd(Wbpawn7.winfo_x(),Wbpawn7.winfo_y()),BP1=crd(Bbpawn.winfo_x(),Bbpawn.winfo_y()),BP2=crd(Bbpawn2.winfo_x(),Bbpawn2.winfo_y()),BP3=crd(Bbpawn3.winfo_x(),Bbpawn3.winfo_y()),BP4=crd(Bbpawn4.winfo_x(),Bbpawn4.winfo_y()),BP5=crd(Bbpawn5.winfo_x(),Bbpawn5.winfo_y()),BP6=crd(nx,ny),BP7=crd(Bbpawn7.winfo_x(),Bbpawn7.winfo_y()),BP8=crd(Bbpawn8.winfo_x(),Bbpawn8.winfo_y()),BR1=crd(Bbrook.winfo_x(),Bbrook.winfo_y()),BR2=crd(Bbrook1.winfo_x(),Bbrook1.winfo_y()),BBI1=crd(Bbbish.winfo_x(),Bbbish.winfo_y()),BBI2=crd(Bbbish1.winfo_x(),Bbbish1.winfo_y()),BN1=crd(Bbnit.winfo_x(),Bbnit.winfo_y()),BN2=crd(Bbnit1.winfo_x(),Bbnit1.winfo_y()),BK=crd(Bbking.winfo_x(),Bbking.winfo_y()),BQ=crd(Bbqueen.winfo_x(),Bbqueen.winfo_y()),WR1=crd(Bwrook.winfo_x(),Bwrook.winfo_y()),WR2=crd(Bwrook1.winfo_x(),Bwrook1.winfo_y()),WBI1=crd(Bwbish.winfo_x(),Bwbish.winfo_y()),WBI2=crd(Bwbish1.winfo_x(),Bwbish1.winfo_y()),WN1=crd(Bwnit.winfo_x(),Bwnit.winfo_y()),WN2=crd(Bwnit1.winfo_x(),Bwnit1.winfo_y()),WK=crd(Bwking.winfo_x(),Bwking.winfo_y()),WQ=crd(Bwqueen.winfo_x(),Bwqueen.winfo_y()))
            terminator(Bbpawn6)
            sw.unbind("<Button-1>")
        except :
            print("click in the box not on the button")
            xi=2
        if xi==2:
            pass
        else:
            changer(2)
    sw.bind("<Button-1>",mover2)

def draggerBP7():
     global Bbpawn7
     global cx
     global cy
     cx=Bbpawn7.winfo_x() 
     cy=Bbpawn7.winfo_y()
     print(cx,',',cy)
        
def moverBP7():
    
    global sw
    global cx
    global cy
    def mover2(event):
        global n14
        global Bbpawn7
        x=event.x
        y=event.y
        smy=cy+136
        smx=cx
        nx=cx
        ny=cy+68
        if (x<(cx+141)and x>(cx+67)) and (y<(cy+128) and y>(cy+60)):
            nx=cx+75
            ny=cy+68
            n14=0
        elif (x<(cx-13)and x>(cx-87)) and (y<(cy+128) and y>(cy+60)):
            nx=cx-75
            ny=cy+68
            n14=0
        while n14==1:
            if y>330 or y<263:
                nx=smx
                ny=smy
                
            n14=0
        Bbpawn7.place(x=nx,y=ny)
        xi=1
        try:
            Peices_info(WP1=crd(Wbpawn.winfo_x(),Wbpawn.winfo_y()),WP2=crd(Wbpawn1.winfo_x(),Wbpawn1.winfo_y()),WP3=crd(Wbpawn2.winfo_x(),Wbpawn2.winfo_y()),WP4=crd(Wbpawn3.winfo_x(),Wbpawn3.winfo_y()),WP5=crd(Wbpawn4.winfo_x(),Wbpawn4.winfo_y()),WP6=crd(Wbpawn5.winfo_x(),Wbpawn5.winfo_y()),WP7=crd(Wbpawn6.winfo_x(),Wbpawn6.winfo_y()),WP8=crd(Wbpawn7.winfo_x(),Wbpawn7.winfo_y()),BP1=crd(Bbpawn.winfo_x(),Bbpawn.winfo_y()),BP2=crd(Bbpawn2.winfo_x(),Bbpawn2.winfo_y()),BP3=crd(Bbpawn3.winfo_x(),Bbpawn3.winfo_y()),BP4=crd(Bbpawn4.winfo_x(),Bbpawn4.winfo_y()),BP5=crd(Bbpawn5.winfo_x(),Bbpawn5.winfo_y()),BP6=crd(Bbpawn6.winfo_x(),Bbpawn6.winfo_y()),BP7=crd(nx,ny),BP8=crd(Bbpawn8.winfo_x(),Bbpawn8.winfo_y()),BR1=crd(Bbrook.winfo_x(),Bbrook.winfo_y()),BR2=crd(Bbrook1.winfo_x(),Bbrook1.winfo_y()),BBI1=crd(Bbbish.winfo_x(),Bbbish.winfo_y()),BBI2=crd(Bbbish1.winfo_x(),Bbbish1.winfo_y()),BN1=crd(Bbnit.winfo_x(),Bbnit.winfo_y()),BN2=crd(Bbnit1.winfo_x(),Bbnit1.winfo_y()),BK=crd(Bbking.winfo_x(),Bbking.winfo_y()),BQ=crd(Bbqueen.winfo_x(),Bbqueen.winfo_y()),WR1=crd(Bwrook.winfo_x(),Bwrook.winfo_y()),WR2=crd(Bwrook1.winfo_x(),Bwrook1.winfo_y()),WBI1=crd(Bwbish.winfo_x(),Bwbish.winfo_y()),WBI2=crd(Bwbish1.winfo_x(),Bwbish1.winfo_y()),WN1=crd(Bwnit.winfo_x(),Bwnit.winfo_y()),WN2=crd(Bwnit1.winfo_x(),Bwnit1.winfo_y()),WK=crd(Bwking.winfo_x(),Bwking.winfo_y()),WQ=crd(Bwqueen.winfo_x(),Bwqueen.winfo_y()))
            terminator(Bbpawn7)
            sw.unbind("<Button-1>")
        except :
            print("click in the box not on the button")
            xi=2
        if xi==2:
            pass
        else:
            changer(2)
    sw.bind("<Button-1>",mover2)

def draggerBP8():
     global Bbpawn8
     global cx
     global cy
     cx=Bbpawn8.winfo_x() 
     cy=Bbpawn8.winfo_y()
     print(cx,',',cy)
        
def moverBP8():
    global sw
    global cx
    global cy
    def mover2(event):
        global n15
        global Bbpawn8
        x=event.x
        y=event.y
        smy=cy+136
        smx=cx
        nx=cx
        ny=cy+68
        if (x<(cx+141)and x>(cx+67)) and (y<(cy+128) and y>(cy+60)):
            nx=cx+75
            ny=cy+68
            n15=0
        elif (x<(cx-13)and x>(cx-87)) and (y<(cy+128) and y>(cy+60)):
            nx=cx-75
            ny=cy+68
            n15=0
        while n15==1:
            if y>330 or y<263:
                nx=smx
                ny=smy
                
            n15=0
        Bbpawn8.place(x=nx,y=ny)
        xi=1
        try:
            Peices_info(WP1=crd(Wbpawn.winfo_x(),Wbpawn.winfo_y()),WP2=crd(Wbpawn1.winfo_x(),Wbpawn1.winfo_y()),WP3=crd(Wbpawn2.winfo_x(),Wbpawn2.winfo_y()),WP4=crd(Wbpawn3.winfo_x(),Wbpawn3.winfo_y()),WP5=crd(Wbpawn4.winfo_x(),Wbpawn4.winfo_y()),WP6=crd(Wbpawn5.winfo_x(),Wbpawn5.winfo_y()),WP7=crd(Wbpawn6.winfo_x(),Wbpawn6.winfo_y()),WP8=crd(Wbpawn7.winfo_x(),Wbpawn7.winfo_y()),BP1=crd(Bbpawn.winfo_x(),Bbpawn.winfo_y()),BP2=crd(Bbpawn2.winfo_x(),Bbpawn2.winfo_y()),BP3=crd(Bbpawn3.winfo_x(),Bbpawn3.winfo_y()),BP4=crd(Bbpawn4.winfo_x(),Bbpawn4.winfo_y()),BP5=crd(Bbpawn5.winfo_x(),Bbpawn5.winfo_y()),BP6=crd(Bbpawn6.winfo_x(),Bbpawn6.winfo_y()),BP7=crd(Bbpawn7.winfo_x(),Bbpawn7.winfo_y()),BP8=crd(nx,ny),BR1=crd(Bbrook.winfo_x(),Bbrook.winfo_y()),BR2=crd(Bbrook1.winfo_x(),Bbrook1.winfo_y()),BBI1=crd(Bbbish.winfo_x(),Bbbish.winfo_y()),BBI2=crd(Bbbish1.winfo_x(),Bbbish1.winfo_y()),BN1=crd(Bbnit.winfo_x(),Bbnit.winfo_y()),BN2=crd(Bbnit1.winfo_x(),Bbnit1.winfo_y()),BK=crd(Bbking.winfo_x(),Bbking.winfo_y()),BQ=crd(Bbqueen.winfo_x(),Bbqueen.winfo_y()),WR1=crd(Bwrook.winfo_x(),Bwrook.winfo_y()),WR2=crd(Bwrook1.winfo_x(),Bwrook1.winfo_y()),WBI1=crd(Bwbish.winfo_x(),Bwbish.winfo_y()),WBI2=crd(Bwbish1.winfo_x(),Bwbish1.winfo_y()),WN1=crd(Bwnit.winfo_x(),Bwnit.winfo_y()),WN2=crd(Bwnit1.winfo_x(),Bwnit1.winfo_y()),WK=crd(Bwking.winfo_x(),Bwking.winfo_y()),WQ=crd(Bwqueen.winfo_x(),Bwqueen.winfo_y()))
            terminator(Bbpawn8)
            sw.unbind("<Button-1>")
        except :
            print("click in the box not on the button")
            xi=2
        if xi==2:
            pass
        else:
            changer(2)
    sw.bind("<Button-1>",mover2)    

def draggerBwnit():
     global Bwnit
     global cx
     global cy
     cx=Bwnit.winfo_x() 
     cy=Bwnit.winfo_y()
     print(cx,',s',cy)

def moverBwnit():
    global sw
    global cx
    global cy
    def mover2(event):
        global Bwnit
        x=event.x
        y=event.y
        if (x<(cx+145)and x>(cx+66)) and (y<(cy-76) and y>(cy-144)):
            nx=cx+75
            ny=cy-136
            Bwnit.place(x=nx,y=ny)
        elif (x<(cx-8)and x>(cx-82)) and (y<(cy-76) and y>(cy-144)):
            nx=cx-75
            ny=cy-136
            Bwnit.place(x=nx,y=ny)
        elif (x<(cx-83)and x>(cx-157)) and (y<(cy-8) and y>(cy-76)):
            nx=cx-150
            ny=cy-68
            Bwnit.place(x=nx,y=ny)
        elif (x<(cx-83)and x>(cx-157)) and (y<(cy+128) and y>(cy+60)):
            nx=cx-150
            ny=cy+68
            Bwnit.place(x=nx,y=ny)
        elif (x<(cx+213)and x>(cx+139)) and (y<(cy-8) and y>(cy-76)):
            nx=cx+150
            ny=cy-68
            Bwnit.place(x=nx,y=ny)
        elif (x<(cx+213)and x>(cx+139)) and (y<(cy+128) and y>(cy+60)):
            nx=cx+150
            ny=cy+68
            Bwnit.place(x=nx,y=ny)
        elif (x<(cx-8)and x>(cx-82)) and (y<(cy+196) and y>(cy+128)):
            nx=cx-75
            ny=cy+136
            Bwnit.place(x=nx,y=ny)
        elif (x<(cx+145)and x>(cx+66)) and (y<(cy+196) and y>(cy+128)):
            nx=cx+75
            ny=cy+136
            Bwnit.place(x=nx,y=ny)
        xi=1
        try:
            Peices_info(WP1=crd(Wbpawn.winfo_x(),Wbpawn.winfo_y()),WP2=crd(Wbpawn1.winfo_x(),Wbpawn1.winfo_y()),WP3=crd(Wbpawn2.winfo_x(),Wbpawn2.winfo_y()),WP4=crd(Wbpawn3.winfo_x(),Wbpawn3.winfo_y()),WP5=crd(Wbpawn4.winfo_x(),Wbpawn4.winfo_y()),WP6=crd(Wbpawn5.winfo_x(),Wbpawn5.winfo_y()),WP7=crd(Wbpawn6.winfo_x(),Wbpawn6.winfo_y()),WP8=crd(Wbpawn7.winfo_x(),Wbpawn7.winfo_y()),BP1=crd(Bbpawn.winfo_x(),Bbpawn.winfo_y()),BP2=crd(Bbpawn2.winfo_x(),Bbpawn2.winfo_y()),BP3=crd(Bbpawn3.winfo_x(),Bbpawn3.winfo_y()),BP4=crd(Bbpawn4.winfo_x(),Bbpawn4.winfo_y()),BP5=crd(Bbpawn5.winfo_x(),Bbpawn5.winfo_y()),BP6=crd(Bbpawn6.winfo_x(),Bbpawn6.winfo_y()),BP7=crd(Bbpawn7.winfo_x(),Bbpawn7.winfo_y()),BP8=crd(Bbpawn8.winfo_x(),Bbpawn8.winfo_y()),BR1=crd(Bbrook.winfo_x(),Bbrook.winfo_y()),BR2=crd(Bbrook1.winfo_x(),Bbrook1.winfo_y()),BBI1=crd(Bbbish.winfo_x(),Bbbish.winfo_y()),BBI2=crd(Bbbish1.winfo_x(),Bbbish1.winfo_y()),BN1=crd(Bbnit.winfo_x(),Bbnit.winfo_y()),BN2=crd(Bbnit1.winfo_x(),Bbnit1.winfo_y()),BK=crd(Bbking.winfo_x(),Bbking.winfo_y()),BQ=crd(Bbqueen.winfo_x(),Bbqueen.winfo_y()),WR1=crd(Bwrook.winfo_x(),Bwrook.winfo_y()),WR2=crd(Bwrook1.winfo_x(),Bwrook1.winfo_y()),WBI1=crd(Bwbish.winfo_x(),Bwbish.winfo_y()),WBI2=crd(Bwbish1.winfo_x(),Bwbish1.winfo_y()),WN1=crd(nx,ny),WN2=crd(Bwnit1.winfo_x(),Bwnit1.winfo_y()),WK=crd(Bwking.winfo_x(),Bwking.winfo_y()),WQ=crd(Bwqueen.winfo_x(),Bwqueen.winfo_y()))
            terminator(Bwnit)
            sw.unbind("<Button-1>")
        except :
            print("click in the box not on the button")
            xi=2
        if xi==2:
            pass
        else:
            changer(1)
    sw.bind("<Button-1>",mover2)    

def draggerBwnit1():
     global Bwnit1
     global cx
     global cy
     cx=Bwnit1.winfo_x() 
     cy=Bwnit1.winfo_y()
     print(cx,',s',cy)

def moverBwnit1():
    
    global sw
    global cx
    global cy
    def mover2(event):
        global Bwnit1
        x=event.x
        y=event.y
        if (x<(cx+145)and x>(cx+66)) and (y<(cy-76) and y>(cy-144)):
            nx=cx+75
            ny=cy-136
            Bwnit1.place(x=nx,y=ny)
        elif (x<(cx-8)and x>(cx-82)) and (y<(cy-76) and y>(cy-144)):
            nx=cx-75
            ny=cy-136
            Bwnit1.place(x=nx,y=ny)
        elif (x<(cx-83)and x>(cx-157)) and (y<(cy-8) and y>(cy-76)):
            nx=cx-150
            ny=cy-68
            Bwnit1.place(x=nx,y=ny)
        elif (x<(cx-83)and x>(cx-157)) and (y<(cy+128) and y>(cy+60)):
            nx=cx-150
            ny=cy+68
            Bwnit1.place(x=nx,y=ny)
        elif (x<(cx+213)and x>(cx+139)) and (y<(cy-8) and y>(cy-76)):
            nx=cx+150
            ny=cy-68
            Bwnit1.place(x=nx,y=ny)
        elif (x<(cx+213)and x>(cx+139)) and (y<(cy+128) and y>(cy+60)):
            nx=cx+150
            ny=cy+68
            Bwnit1.place(x=nx,y=ny)
        elif (x<(cx-8)and x>(cx-82)) and (y<(cy+196) and y>(cy+128)):
            nx=cx-75
            ny=cy+136
            Bwnit1.place(x=nx,y=ny)
        elif (x<(cx+145)and x>(cx+66)) and (y<(cy+196) and y>(cy+128)):
            nx=cx+75
            ny=cy+136
            Bwnit1.place(x=nx,y=ny)
        xi=1
        try:
            Peices_info(WP1=crd(Wbpawn.winfo_x(),Wbpawn.winfo_y()),WP2=crd(Wbpawn1.winfo_x(),Wbpawn1.winfo_y()),WP3=crd(Wbpawn2.winfo_x(),Wbpawn2.winfo_y()),WP4=crd(Wbpawn3.winfo_x(),Wbpawn3.winfo_y()),WP5=crd(Wbpawn4.winfo_x(),Wbpawn4.winfo_y()),WP6=crd(Wbpawn5.winfo_x(),Wbpawn5.winfo_y()),WP7=crd(Wbpawn6.winfo_x(),Wbpawn6.winfo_y()),WP8=crd(Wbpawn7.winfo_x(),Wbpawn7.winfo_y()),BP1=crd(Bbpawn.winfo_x(),Bbpawn.winfo_y()),BP2=crd(Bbpawn2.winfo_x(),Bbpawn2.winfo_y()),BP3=crd(Bbpawn3.winfo_x(),Bbpawn3.winfo_y()),BP4=crd(Bbpawn4.winfo_x(),Bbpawn4.winfo_y()),BP5=crd(Bbpawn5.winfo_x(),Bbpawn5.winfo_y()),BP6=crd(Bbpawn6.winfo_x(),Bbpawn6.winfo_y()),BP7=crd(Bbpawn7.winfo_x(),Bbpawn7.winfo_y()),BP8=crd(Bbpawn8.winfo_x(),Bbpawn8.winfo_y()),BR1=crd(Bbrook.winfo_x(),Bbrook.winfo_y()),BR2=crd(Bbrook1.winfo_x(),Bbrook1.winfo_y()),BBI1=crd(Bbbish.winfo_x(),Bbbish.winfo_y()),BBI2=crd(Bbbish1.winfo_x(),Bbbish1.winfo_y()),BN1=crd(Bbnit.winfo_x(),Bbnit.winfo_y()),BN2=crd(Bbnit1.winfo_x(),Bbnit1.winfo_y()),BK=crd(Bbking.winfo_x(),Bbking.winfo_y()),BQ=crd(Bbqueen.winfo_x(),Bbqueen.winfo_y()),WR1=crd(Bwrook.winfo_x(),Bwrook.winfo_y()),WR2=crd(Bwrook1.winfo_x(),Bwrook1.winfo_y()),WBI1=crd(Bwbish.winfo_x(),Bwbish.winfo_y()),WBI2=crd(Bwbish1.winfo_x(),Bwbish1.winfo_y()),WN1=crd(Bwnit.winfo_x(),Bwnit.winfo_y()),WN2=crd(nx,ny),WK=crd(Bwking.winfo_x(),Bwking.winfo_y()),WQ=crd(Bwqueen.winfo_x(),Bwqueen.winfo_y()))
            terminator(Bwnit1)
            sw.unbind("<Button-1>")
        except :
            print("click in the box not on the button")
            xi=2
        if xi==2:
            pass
        else:
            changer(1)
    
    sw.bind("<Button-1>",mover2)

def draggerBbnit():
     global Bbnit
     global cx
     global cy
     cx=Bbnit.winfo_x() 
     cy=Bbnit.winfo_y()
     print(cx,',s',cy)

def moverBbnit():
    
    global sw
    global cx
    global cy
    def mover2(event):
        global Bbnit
        x=event.x
        y=event.y
        
        if (x<(cx+145)and x>(cx+66)) and (y<(cy-76) and y>(cy-144)):
            nx=cx+75
            ny=cy-136
            Bbnit.place(x=nx,y=ny)
        elif (x<(cx-8)and x>(cx-82)) and (y<(cy-76) and y>(cy-144)):
            nx=cx-75
            ny=cy-136
            Bbnit.place(x=nx,y=ny)
        elif (x<(cx-83)and x>(cx-157)) and (y<(cy-8) and y>(cy-76)):
            nx=cx-150
            ny=cy-68
            Bbnit.place(x=nx,y=ny)
        elif (x<(cx-83)and x>(cx-157)) and (y<(cy+128) and y>(cy+60)):
            nx=cx-150
            ny=cy+68
            Bbnit.place(x=nx,y=ny)
        elif (x<(cx+213)and x>(cx+139)) and (y<(cy-8) and y>(cy-76)):
            nx=cx+150
            ny=cy-68
            Bbnit.place(x=nx,y=ny)
        elif (x<(cx+213)and x>(cx+139)) and (y<(cy+128) and y>(cy+60)):
            nx=cx+150
            ny=cy+68
            Bbnit.place(x=nx,y=ny)
        elif (x<(cx-8)and x>(cx-82)) and (y<(cy+196) and y>(cy+128)):
            nx=cx-75
            ny=cy+136
            Bbnit.place(x=nx,y=ny)
        elif (x<(cx+145)and x>(cx+66)) and (y<(cy+196) and y>(cy+128)):
            nx=cx+75
            ny=cy+136
            Bbnit.place(x=nx,y=ny)
        xi=1
        try:
            Peices_info(WP1=crd(Wbpawn.winfo_x(),Wbpawn.winfo_y()),WP2=crd(Wbpawn1.winfo_x(),Wbpawn1.winfo_y()),WP3=crd(Wbpawn2.winfo_x(),Wbpawn2.winfo_y()),WP4=crd(Wbpawn3.winfo_x(),Wbpawn3.winfo_y()),WP5=crd(Wbpawn4.winfo_x(),Wbpawn4.winfo_y()),WP6=crd(Wbpawn5.winfo_x(),Wbpawn5.winfo_y()),WP7=crd(Wbpawn6.winfo_x(),Wbpawn6.winfo_y()),WP8=crd(Wbpawn7.winfo_x(),Wbpawn7.winfo_y()),BP1=crd(Bbpawn.winfo_x(),Bbpawn.winfo_y()),BP2=crd(Bbpawn2.winfo_x(),Bbpawn2.winfo_y()),BP3=crd(Bbpawn3.winfo_x(),Bbpawn3.winfo_y()),BP4=crd(Bbpawn4.winfo_x(),Bbpawn4.winfo_y()),BP5=crd(Bbpawn5.winfo_x(),Bbpawn5.winfo_y()),BP6=crd(Bbpawn6.winfo_x(),Bbpawn6.winfo_y()),BP7=crd(Bbpawn7.winfo_x(),Bbpawn7.winfo_y()),BP8=crd(Bbpawn8.winfo_x(),Bbpawn8.winfo_y()),BR1=crd(Bbrook.winfo_x(),Bbrook.winfo_y()),BR2=crd(Bbrook1.winfo_x(),Bbrook1.winfo_y()),BBI1=crd(Bbbish.winfo_x(),Bbbish.winfo_y()),BBI2=crd(Bbbish1.winfo_x(),Bbbish1.winfo_y()),BN1=crd(nx,ny),BN2=crd(Bbnit1.winfo_x(),Bbnit1.winfo_y()),BK=crd(Bbking.winfo_x(),Bbking.winfo_y()),BQ=crd(Bbqueen.winfo_x(),Bbqueen.winfo_y()),WR1=crd(Bwrook.winfo_x(),Bwrook.winfo_y()),WR2=crd(Bwrook1.winfo_x(),Bwrook1.winfo_y()),WBI1=crd(Bwbish.winfo_x(),Bwbish.winfo_y()),WBI2=crd(Bwbish1.winfo_x(),Bwbish1.winfo_y()),WN1=crd(Bwnit.winfo_x(),Bwnit.winfo_y()),WN2=crd(Bwnit1.winfo_x(),Bwnit1.winfo_y()),WK=crd(Bwking.winfo_x(),Bwking.winfo_y()),WQ=crd(Bwqueen.winfo_x(),Bwqueen.winfo_y()))
            terminator(Bbnit)
            sw.unbind("<Button-1>")
        
        except :
            print("click in the box not on the button")
            xi=2
        if xi==2:
            pass
        else:
            changer(2)
    
    sw.bind("<Button-1>",mover2)    

def draggerBbnit1():
     global Bbnit1
     global cx
     global cy
     cx=Bbnit1.winfo_x() 
     cy=Bbnit1.winfo_y()
     print(cx,',s',cy)

def moverBbnit1():
    
    global sw
    global cx
    global cy
    def mover2(event):
        global Bbnit1
        x=event.x
        y=event.y
        if (x<(cx+145)and x>(cx+66)) and (y<(cy-76) and y>(cy-144)):
            nx=cx+75
            ny=cy-136
            Bbnit1.place(x=nx,y=ny)
        elif (x<(cx-8)and x>(cx-82)) and (y<(cy-76) and y>(cy-144)):
            nx=cx-75
            ny=cy-136
            Bbnit1.place(x=nx,y=ny)
        elif (x<(cx-83)and x>(cx-157)) and (y<(cy-8) and y>(cy-76)):
            nx=cx-150
            ny=cy-68
            Bbnit1.place(x=nx,y=ny)
        elif (x<(cx-83)and x>(cx-157)) and (y<(cy+128) and y>(cy+60)):
            nx=cx-150
            ny=cy+68
            Bbnit1.place(x=nx,y=ny)
        elif (x<(cx+213)and x>(cx+139)) and (y<(cy-8) and y>(cy-76)):
            nx=cx+150
            ny=cy-68
            Bbnit1.place(x=nx,y=ny)
        elif (x<(cx+213)and x>(cx+139)) and (y<(cy+128) and y>(cy+60)):
            nx=cx+150
            ny=cy+68
            Bbnit1.place(x=nx,y=ny)
        elif (x<(cx-8)and x>(cx-82)) and (y<(cy+196) and y>(cy+128)):
            nx=cx-75
            ny=cy+136
            Bbnit1.place(x=nx,y=ny)
        elif (x<(cx+145)and x>(cx+66)) and (y<(cy+196) and y>(cy+128)):
            nx=cx+75
            ny=cy+136
            Bbnit1.place(x=nx,y=ny)
        xi=1
        try:
            Peices_info(WP1=crd(Wbpawn.winfo_x(),Wbpawn.winfo_y()),WP2=crd(Wbpawn1.winfo_x(),Wbpawn1.winfo_y()),WP3=crd(Wbpawn2.winfo_x(),Wbpawn2.winfo_y()),WP4=crd(Wbpawn3.winfo_x(),Wbpawn3.winfo_y()),WP5=crd(Wbpawn4.winfo_x(),Wbpawn4.winfo_y()),WP6=crd(Wbpawn5.winfo_x(),Wbpawn5.winfo_y()),WP7=crd(Wbpawn6.winfo_x(),Wbpawn6.winfo_y()),WP8=crd(Wbpawn7.winfo_x(),Wbpawn7.winfo_y()),BP1=crd(Bbpawn.winfo_x(),Bbpawn.winfo_y()),BP2=crd(Bbpawn2.winfo_x(),Bbpawn2.winfo_y()),BP3=crd(Bbpawn3.winfo_x(),Bbpawn3.winfo_y()),BP4=crd(Bbpawn4.winfo_x(),Bbpawn4.winfo_y()),BP5=crd(Bbpawn5.winfo_x(),Bbpawn5.winfo_y()),BP6=crd(Bbpawn6.winfo_x(),Bbpawn6.winfo_y()),BP7=crd(Bbpawn7.winfo_x(),Bbpawn7.winfo_y()),BP8=crd(Bbpawn8.winfo_x(),Bbpawn8.winfo_y()),BR1=crd(Bbrook.winfo_x(),Bbrook.winfo_y()),BR2=crd(Bbrook1.winfo_x(),Bbrook1.winfo_y()),BBI1=crd(Bbbish.winfo_x(),Bbbish.winfo_y()),BBI2=crd(Bbbish1.winfo_x(),Bbbish1.winfo_y()),BN1=crd(Bbnit.winfo_x(),Bbnit.winfo_y()),BN2=crd(nx,ny),BK=crd(Bbking.winfo_x(),Bbking.winfo_y()),BQ=crd(Bbqueen.winfo_x(),Bbqueen.winfo_y()),WR1=crd(Bwrook.winfo_x(),Bwrook.winfo_y()),WR2=crd(Bwrook1.winfo_x(),Bwrook1.winfo_y()),WBI1=crd(Bwbish.winfo_x(),Bwbish.winfo_y()),WBI2=crd(Bwbish1.winfo_x(),Bwbish1.winfo_y()),WN1=crd(Bwnit.winfo_x(),Bwnit.winfo_y()),WN2=crd(Bwnit1.winfo_x(),Bwnit1.winfo_y()),WK=crd(Bwking.winfo_x(),Bwking.winfo_y()),WQ=crd(Bwqueen.winfo_x(),Bwqueen.winfo_y()))
            terminator(Bbnit1)
            sw.unbind("<Button-1>")
        except :
            print("click in the box not on the button")
            xi=2
        if xi==2:
            pass
        else:
            changer(2)
    sw.bind("<Button-1>",mover2)

def draggerBwrook():
     global Bwrook
     global cx
     global cy
     cx=Bwrook.winfo_x() 
     cy=Bwrook.winfo_y()
     
def moverBwrook():
    
    global sw
    global cx
    global cy
    def mover2(event):
        global Bwrook
        x=event.x
        y=event.y
        if (x<(cx+67)and x>(cx-7)) and (y<(cy-8) and y>(cy-76)):
            nx=cx
            ny=cy-68
            Bwrook.place(x=nx,y=ny)
        elif (x<(cx+67)and x>(cx-7)) and (y<(cy-76) and y>(cy-144)):
            nx=cx
            ny=cy-136
            Bwrook.place(x=nx,y=ny)
        elif (x<(cx+67)and x>(cx-7)) and (y<(cy-144) and y>(cy-212)):
            nx=cx
            ny=cy-204
            Bwrook.place(x=nx,y=ny)
        elif (x<(cx+67)and x>(cx-7)) and (y<(cy-212) and y>(cy-280)):
            nx=cx
            ny=cy-272
            Bwrook.place(x=nx,y=ny)
        elif (x<(cx+67)and x>(cx-7)) and (y<(cy-280) and y>(cy-348)):
            nx=cx
            ny=cy-340
            Bwrook.place(x=nx,y=ny)
        elif (x<(cx+67)and x>(cx-7)) and (y<(cy-348) and y>(cy-416)):
            nx=cx
            ny=cy-408
            Bwrook.place(x=nx,y=ny)
        elif (x<(cx+67)and x>(cx-7)) and (y<(cy-416) and y>(cy-484)):
            nx=cx
            ny=cy-476
            Bwrook.place(x=nx,y=ny)
        elif (x<(cx+67)and x>(cx-7)) and (y<(cy+128) and y>(cy+60)):
            nx=cx
            ny=cy+68
            Bwrook.place(x=nx,y=ny)
        elif (x<(cx+67)and x>(cx-7)) and (y<(cy+196) and y>(cy+128)):
            nx=cx
            ny=cy+136
            Bwrook.place(x=nx,y=ny)
        elif (x<(cx+67)and x>(cx-7)) and (y<(cy+264) and y>(cy+196)):
            nx=cx
            ny=cy+204
            Bwrook.place(x=nx,y=ny)
        elif (x<(cx+67)and x>(cx-7)) and (y<(cy+332) and y>(cy+264)):
            nx=cx
            ny=cy+272
            Bwrook.place(x=nx,y=ny)
        elif (x<(cx+67)and x>(cx-7)) and (y<(cy+400) and y>(cy+332)):
            nx=cx
            ny=cy+340
            Bwrook.place(x=nx,y=ny)
        elif (x<(cx+67)and x>(cx-7)) and (y<(cy+468) and y>(cy+400)):
            nx=cx
            ny=cy+408
            Bwrook.place(x=nx,y=ny)
        elif (x<(cx+67)and x>(cx-7)) and (y<(cy+536) and y>(cy+468)):
            nx=cx
            ny=cy+476
            Bwrook.place(x=nx,y=ny)
        elif (x<(cx+141)and x>(cx+67)) and (y<(cy+60) and y>(cy-8)):
            nx=cx+75
            ny=cy
            Bwrook.place(x=nx,y=ny)
        elif (x<(cx+215)and x>(cx+141)) and (y<(cy+60) and y>(cy-8)):
            nx=cx+150
            ny=cy
            Bwrook.place(x=nx,y=ny)
        elif (x<(cx+289)and x>(cx+215)) and (y<(cy+60) and y>(cy-8)):
            nx=cx+225
            ny=cy
            Bwrook.place(x=nx,y=ny)
        elif (x<(cx+363)and x>(cx+289)) and (y<(cy+60) and y>(cy-8)):
            nx=cx+300
            ny=cy
            Bwrook.place(x=nx,y=ny)
        elif (x<(cx+437)and x>(cx+363)) and (y<(cy+60) and y>(cy-8)):
            nx=cx+375
            ny=cy
            Bwrook.place(x=nx,y=ny)
        elif (x<(cx+511)and x>(cx+437)) and (y<(cy+60) and y>(cy-8)):
            nx=cx+450
            ny=cy
            Bwrook.place(x=nx,y=ny)
        elif (x<(cx+585)and x>(cx+511)) and (y<(cy+60) and y>(cy-8)):
            nx=cx+526
            ny=cy
            Bwrook.place(x=nx,y=ny)
        elif (x<(cx-13)and x>(cx-87)) and (y<(cy+60) and y>(cy-8)):
            nx=cx-75
            ny=cy
            Bwrook.place(x=nx,y=ny)
        elif (x<(cx-87)and x>(cx-161)) and (y<(cy+60) and y>(cy-8)):
            nx=cx-150
            ny=cy
            Bwrook.place(x=nx,y=ny)
        elif (x<(cx-161)and x>(cx-235)) and (y<(cy+60) and y>(cy-8)):
            nx=cx-225
            ny=cy
            Bwrook.place(x=nx,y=ny)
        elif (x<(cx-235)and x>(cx-309)) and (y<(cy+60) and y>(cy-8)):
            nx=cx-300
            ny=cy
            Bwrook.place(x=nx,y=ny)
        elif (x<(cx-309)and x>(cx-383)) and (y<(cy+60) and y>(cy-8)):
            nx=cx-375
            ny=cy
            Bwrook.place(x=nx,y=ny)
        elif (x<(cx-383)and x>(cx-457)) and (y<(cy+60) and y>(cy-8)):
            nx=cx-450
            ny=cy
            Bwrook.place(x=nx,y=ny)
        elif (x<(cx-457)and x>(cx-531)) and (y<(cy+60) and y>(cy-8)):
            nx=cx-526
            ny=cy
            Bwrook.place(x=nx,y=ny)
        xi=1
        try:
            Peices_info(WP1=crd(Wbpawn.winfo_x(),Wbpawn.winfo_y()),WP2=crd(Wbpawn1.winfo_x(),Wbpawn1.winfo_y()),WP3=crd(Wbpawn2.winfo_x(),Wbpawn2.winfo_y()),WP4=crd(Wbpawn3.winfo_x(),Wbpawn3.winfo_y()),WP5=crd(Wbpawn4.winfo_x(),Wbpawn4.winfo_y()),WP6=crd(Wbpawn5.winfo_x(),Wbpawn5.winfo_y()),WP7=crd(Wbpawn6.winfo_x(),Wbpawn6.winfo_y()),WP8=crd(Wbpawn7.winfo_x(),Wbpawn7.winfo_y()),BP1=crd(Bbpawn.winfo_x(),Bbpawn.winfo_y()),BP2=crd(Bbpawn2.winfo_x(),Bbpawn2.winfo_y()),BP3=crd(Bbpawn3.winfo_x(),Bbpawn3.winfo_y()),BP4=crd(Bbpawn4.winfo_x(),Bbpawn4.winfo_y()),BP5=crd(Bbpawn5.winfo_x(),Bbpawn5.winfo_y()),BP6=crd(Bbpawn6.winfo_x(),Bbpawn6.winfo_y()),BP7=crd(Bbpawn7.winfo_x(),Bbpawn7.winfo_y()),BP8=crd(Bbpawn8.winfo_x(),Bbpawn8.winfo_y()),BR1=crd(Bbrook.winfo_x(),Bbrook.winfo_y()),BR2=crd(Bbrook1.winfo_x(),Bbrook1.winfo_y()),BBI1=crd(Bbbish.winfo_x(),Bbbish.winfo_y()),BBI2=crd(Bbbish1.winfo_x(),Bbbish1.winfo_y()),BN1=crd(Bbnit.winfo_x(),Bbnit.winfo_y()),BN2=crd(Bbnit1.winfo_x(),Bbnit1.winfo_y()),BK=crd(Bbking.winfo_x(),Bbking.winfo_y()),BQ=crd(Bbqueen.winfo_x(),Bbqueen.winfo_y()),WR1=crd(nx,ny),WR2=crd(Bwrook1.winfo_x(),Bwrook1.winfo_y()),WBI1=crd(Bwbish.winfo_x(),Bwbish.winfo_y()),WBI2=crd(Bwbish1.winfo_x(),Bwbish1.winfo_y()),WN1=crd(nx,ny),WN2=crd(Bwnit1.winfo_x(),Bwnit1.winfo_y()),WK=crd(Bwking.winfo_x(),Bwking.winfo_y()),WQ=crd(Bwqueen.winfo_x(),Bwqueen.winfo_y()))
            terminator(Bwrook)
            sw.unbind("<Button-1>")
        except :
            print("click in the box not on the button")
            xi=2
        if xi==2:
            pass
        else:
            changer(1)
    
    sw.bind("<Button-1>",mover2)

def draggerBwrook1():
     global Bwrook1
     global cx
     global cy
     cx=Bwrook1.winfo_x() 
     cy=Bwrook1.winfo_y()
     
def moverBwrook1():
    
    global sw
    global cx
    global cy
    def mover2(event):
        global Bwrook1
        x=event.x
        y=event.y
        if (x<(cx+67)and x>(cx-7)) and (y<(cy-8) and y>(cy-76)):
            nx=cx
            ny=cy-68
            Bwrook1.place(x=nx,y=ny)
        elif (x<(cx+67)and x>(cx-7)) and (y<(cy-76) and y>(cy-144)):
            nx=cx
            ny=cy-136
            Bwrook1.place(x=nx,y=ny)
        elif (x<(cx+67)and x>(cx-7)) and (y<(cy-144) and y>(cy-212)):
            nx=cx
            ny=cy-204
            Bwrook1.place(x=nx,y=ny)
        elif (x<(cx+67)and x>(cx-7)) and (y<(cy-212) and y>(cy-280)):
            nx=cx
            ny=cy-272
            Bwrook1.place(x=nx,y=ny)
        elif (x<(cx+67)and x>(cx-7)) and (y<(cy-280) and y>(cy-348)):
            nx=cx
            ny=cy-340
            Bwrook1.place(x=nx,y=ny)
        elif (x<(cx+67)and x>(cx-7)) and (y<(cy-348) and y>(cy-416)):
            nx=cx
            ny=cy-408
            Bwrook1.place(x=nx,y=ny)
        elif (x<(cx+67)and x>(cx-7)) and (y<(cy-416) and y>(cy-484)):
            nx=cx
            ny=cy-476
            Bwrook1.place(x=nx,y=ny)
        elif (x<(cx+67)and x>(cx-7)) and (y<(cy+128) and y>(cy+60)):
            nx=cx
            ny=cy+68
            Bwrook1.place(x=nx,y=ny)
        elif (x<(cx+67)and x>(cx-7)) and (y<(cy+196) and y>(cy+128)):
            nx=cx
            ny=cy+136
            Bwrook1.place(x=nx,y=ny)
        elif (x<(cx+67)and x>(cx-7)) and (y<(cy+264) and y>(cy+196)):
            nx=cx
            ny=cy+204
            Bwrook1.place(x=nx,y=ny)
        elif (x<(cx+67)and x>(cx-7)) and (y<(cy+332) and y>(cy+264)):
            nx=cx
            ny=cy+272
            Bwrook1.place(x=nx,y=ny)
        elif (x<(cx+67)and x>(cx-7)) and (y<(cy+400) and y>(cy+332)):
            nx=cx
            ny=cy+340
            Bwrook1.place(x=nx,y=ny)
        elif (x<(cx+67)and x>(cx-7)) and (y<(cy+468) and y>(cy+400)):
            nx=cx
            ny=cy+408
            Bwrook1.place(x=nx,y=ny)
        elif (x<(cx+67)and x>(cx-7)) and (y<(cy+536) and y>(cy+468)):
            nx=cx
            ny=cy+476
            Bwrook1.place(x=nx,y=ny)
        elif (x<(cx+141)and x>(cx+67)) and (y<(cy+60) and y>(cy-8)):
            nx=cx+75
            ny=cy
            Bwrook1.place(x=nx,y=ny)
        elif (x<(cx+215)and x>(cx+141)) and (y<(cy+60) and y>(cy-8)):
            nx=cx+150
            ny=cy
            Bwrook1.place(x=nx,y=ny)
        elif (x<(cx+289)and x>(cx+215)) and (y<(cy+60) and y>(cy-8)):
            nx=cx+225
            ny=cy
            Bwrook1.place(x=nx,y=ny)
        elif (x<(cx+363)and x>(cx+289)) and (y<(cy+60) and y>(cy-8)):
            nx=cx+300
            ny=cy
            Bwrook1.place(x=nx,y=ny)
        elif (x<(cx+437)and x>(cx+363)) and (y<(cy+60) and y>(cy-8)):
            nx=cx+375
            ny=cy
            Bwrook1.place(x=nx,y=ny)
        elif (x<(cx+511)and x>(cx+437)) and (y<(cy+60) and y>(cy-8)):
            nx=cx+450
            ny=cy
            Bwrook1.place(x=nx,y=ny)
        elif (x<(cx+585)and x>(cx+511)) and (y<(cy+60) and y>(cy-8)):
            nx=cx+526
            ny=cy
            Bwrook1.place(x=nx,y=ny)
        elif (x<(cx-13)and x>(cx-87)) and (y<(cy+60) and y>(cy-8)):
            nx=cx-75
            ny=cy
            Bwrook1.place(x=nx,y=ny)
        elif (x<(cx-87)and x>(cx-161)) and (y<(cy+60) and y>(cy-8)):
            nx=cx-150
            ny=cy
            Bwrook1.place(x=nx,y=ny)
        elif (x<(cx-161)and x>(cx-235)) and (y<(cy+60) and y>(cy-8)):
            nx=cx-225
            ny=cy
            Bwrook1.place(x=nx,y=ny)
        elif (x<(cx-235)and x>(cx-309)) and (y<(cy+60) and y>(cy-8)):
            nx=cx-300
            ny=cy
            Bwrook1.place(x=nx,y=ny)
        elif (x<(cx-309)and x>(cx-383)) and (y<(cy+60) and y>(cy-8)):
            nx=cx-375
            ny=cy
            Bwrook1.place(x=nx,y=ny)
        elif (x<(cx-383)and x>(cx-457)) and (y<(cy+60) and y>(cy-8)):
            nx=cx-450
            ny=cy
            Bwrook1.place(x=nx,y=ny)
        elif (x<(cx-457)and x>(cx-531)) and (y<(cy+60) and y>(cy-8)):
            nx=cx-526
            ny=cy
            Bwrook1.place(x=nx,y=ny)
        xi=1
        try:
            Peices_info(WP1=crd(Wbpawn.winfo_x(),Wbpawn.winfo_y()),WP2=crd(Wbpawn1.winfo_x(),Wbpawn1.winfo_y()),WP3=crd(Wbpawn2.winfo_x(),Wbpawn2.winfo_y()),WP4=crd(Wbpawn3.winfo_x(),Wbpawn3.winfo_y()),WP5=crd(Wbpawn4.winfo_x(),Wbpawn4.winfo_y()),WP6=crd(Wbpawn5.winfo_x(),Wbpawn5.winfo_y()),WP7=crd(Wbpawn6.winfo_x(),Wbpawn6.winfo_y()),WP8=crd(Wbpawn7.winfo_x(),Wbpawn7.winfo_y()),BP1=crd(Bbpawn.winfo_x(),Bbpawn.winfo_y()),BP2=crd(Bbpawn2.winfo_x(),Bbpawn2.winfo_y()),BP3=crd(Bbpawn3.winfo_x(),Bbpawn3.winfo_y()),BP4=crd(Bbpawn4.winfo_x(),Bbpawn4.winfo_y()),BP5=crd(Bbpawn5.winfo_x(),Bbpawn5.winfo_y()),BP6=crd(Bbpawn6.winfo_x(),Bbpawn6.winfo_y()),BP7=crd(Bbpawn7.winfo_x(),Bbpawn7.winfo_y()),BP8=crd(Bbpawn8.winfo_x(),Bbpawn8.winfo_y()),BR1=crd(Bbrook.winfo_x(),Bbrook.winfo_y()),BR2=crd(Bbrook1.winfo_x(),Bbrook1.winfo_y()),BBI1=crd(Bbbish.winfo_x(),Bbbish.winfo_y()),BBI2=crd(Bbbish1.winfo_x(),Bbbish1.winfo_y()),BN1=crd(Bbnit.winfo_x(),Bbnit.winfo_y()),BN2=crd(Bbnit1.winfo_x(),Bbnit1.winfo_y()),BK=crd(Bbking.winfo_x(),Bbking.winfo_y()),BQ=crd(Bbqueen.winfo_x(),Bbqueen.winfo_y()),WR1=crd(Bwrook.winfo_x(),Bwrook.winfo_y()),WR2=crd(nx,ny),WBI1=crd(Bwbish.winfo_x(),Bwbish.winfo_y()),WBI2=crd(Bwbish1.winfo_x(),Bwbish1.winfo_y()),WN1=crd(nx,ny),WN2=crd(Bwnit1.winfo_x(),Bwnit1.winfo_y()),WK=crd(Bwking.winfo_x(),Bwking.winfo_y()),WQ=crd(Bwqueen.winfo_x(),Bwqueen.winfo_y()))
            terminator(Bwrook1)
            sw.unbind("<Button-1>")
        except :
            print("click in the box not on the button")
            xi=2
        if xi==2:
            pass
        else:
            changer(1)
    
    sw.bind("<Button-1>",mover2)

def draggerBbrook():
     global Bbrook
     global cx
     global cy
     cx=Bbrook.winfo_x() 
     cy=Bbrook.winfo_y()
     
def moverBbrook():
    
    global sw
    global cx
    global cy
    def mover2(event):
        global Bbrook
        x=event.x
        y=event.y
        if (x<(cx+67)and x>(cx-7)) and (y<(cy-8) and y>(cy-76)):
            nx=cx
            ny=cy-68
            Bbrook.place(x=nx,y=ny)
        elif (x<(cx+67)and x>(cx-7)) and (y<(cy-76) and y>(cy-144)):
            nx=cx
            ny=cy-136
            Bbrook.place(x=nx,y=ny)
        elif (x<(cx+67)and x>(cx-7)) and (y<(cy-144) and y>(cy-212)):
            nx=cx
            ny=cy-204
            Bbrook.place(x=nx,y=ny)
        elif (x<(cx+67)and x>(cx-7)) and (y<(cy-212) and y>(cy-280)):
            nx=cx
            ny=cy-272
            Bbrook.place(x=nx,y=ny)
        elif (x<(cx+67)and x>(cx-7)) and (y<(cy-280) and y>(cy-348)):
            nx=cx
            ny=cy-340
            Bbrook.place(x=nx,y=ny)
        elif (x<(cx+67)and x>(cx-7)) and (y<(cy-348) and y>(cy-416)):
            nx=cx
            ny=cy-408
            Bbrook.place(x=nx,y=ny)
        elif (x<(cx+67)and x>(cx-7)) and (y<(cy-416) and y>(cy-484)):
            nx=cx
            ny=cy-476
            Bbrook.place(x=nx,y=ny)
        elif (x<(cx+67)and x>(cx-7)) and (y<(cy+128) and y>(cy+60)):
            nx=cx
            ny=cy+68
            Bbrook.place(x=nx,y=ny)
        elif (x<(cx+67)and x>(cx-7)) and (y<(cy+196) and y>(cy+128)):
            nx=cx
            ny=cy+136
            Bbrook.place(x=nx,y=ny)
        elif (x<(cx+67)and x>(cx-7)) and (y<(cy+264) and y>(cy+196)):
            nx=cx
            ny=cy+204
            Bbrook.place(x=nx,y=ny)
        elif (x<(cx+67)and x>(cx-7)) and (y<(cy+332) and y>(cy+264)):
            nx=cx
            ny=cy+272
            Bbrook.place(x=nx,y=ny)
        elif (x<(cx+67)and x>(cx-7)) and (y<(cy+400) and y>(cy+332)):
            nx=cx
            ny=cy+340
            Bbrook.place(x=nx,y=ny)
        elif (x<(cx+67)and x>(cx-7)) and (y<(cy+468) and y>(cy+400)):
            nx=cx
            ny=cy+408
            Bbrook.place(x=nx,y=ny)
        elif (x<(cx+67)and x>(cx-7)) and (y<(cy+536) and y>(cy+468)):
            nx=cx
            ny=cy+476
            Bbrook.place(x=nx,y=ny)
        elif (x<(cx+141)and x>(cx+67)) and (y<(cy+60) and y>(cy-8)):
            nx=cx+75
            ny=cy
            Bbrook.place(x=nx,y=ny)
        elif (x<(cx+215)and x>(cx+141)) and (y<(cy+60) and y>(cy-8)):
            nx=cx+150
            ny=cy
            Bbrook.place(x=nx,y=ny)
        elif (x<(cx+289)and x>(cx+215)) and (y<(cy+60) and y>(cy-8)):
            nx=cx+225
            ny=cy
            Bbrook.place(x=nx,y=ny)
        elif (x<(cx+363)and x>(cx+289)) and (y<(cy+60) and y>(cy-8)):
            nx=cx+300
            ny=cy
            Bbrook.place(x=nx,y=ny)
        elif (x<(cx+437)and x>(cx+363)) and (y<(cy+60) and y>(cy-8)):
            nx=cx+375
            ny=cy
            Bbrook.place(x=nx,y=ny)
        elif (x<(cx+511)and x>(cx+437)) and (y<(cy+60) and y>(cy-8)):
            nx=cx+450
            ny=cy
            Bbrook.place(x=nx,y=ny)
        elif (x<(cx+585)and x>(cx+511)) and (y<(cy+60) and y>(cy-8)):
            nx=cx+526
            ny=cy
            Bbrook.place(x=nx,y=ny)
        elif (x<(cx-13)and x>(cx-87)) and (y<(cy+60) and y>(cy-8)):
            nx=cx-75
            ny=cy
            Bbrook.place(x=nx,y=ny)
        elif (x<(cx-87)and x>(cx-161)) and (y<(cy+60) and y>(cy-8)):
            nx=cx-150
            ny=cy
            Bbrook.place(x=nx,y=ny)
        elif (x<(cx-161)and x>(cx-235)) and (y<(cy+60) and y>(cy-8)):
            nx=cx-225
            ny=cy
            Bbrook.place(x=nx,y=ny)
        elif (x<(cx-235)and x>(cx-309)) and (y<(cy+60) and y>(cy-8)):
            nx=cx-300
            ny=cy
            Bbrook.place(x=nx,y=ny)
        elif (x<(cx-309)and x>(cx-383)) and (y<(cy+60) and y>(cy-8)):
            nx=cx-375
            ny=cy
            Bbrook.place(x=nx,y=ny)
        elif (x<(cx-383)and x>(cx-457)) and (y<(cy+60) and y>(cy-8)):
            nx=cx-450
            ny=cy
            Bbrook.place(x=nx,y=ny)
        elif (x<(cx-457)and x>(cx-531)) and (y<(cy+60) and y>(cy-8)):
            nx=cx-526
            ny=cy
            Bbrook.place(x=nx,y=ny)
        xi=1
        try:
            Peices_info(WP1=crd(Wbpawn.winfo_x(),Wbpawn.winfo_y()),WP2=crd(Wbpawn1.winfo_x(),Wbpawn1.winfo_y()),WP3=crd(Wbpawn2.winfo_x(),Wbpawn2.winfo_y()),WP4=crd(Wbpawn3.winfo_x(),Wbpawn3.winfo_y()),WP5=crd(Wbpawn4.winfo_x(),Wbpawn4.winfo_y()),WP6=crd(Wbpawn5.winfo_x(),Wbpawn5.winfo_y()),WP7=crd(Wbpawn6.winfo_x(),Wbpawn6.winfo_y()),WP8=crd(Wbpawn7.winfo_x(),Wbpawn7.winfo_y()),BP1=crd(Bbpawn.winfo_x(),Bbpawn.winfo_y()),BP2=crd(Bbpawn2.winfo_x(),Bbpawn2.winfo_y()),BP3=crd(Bbpawn3.winfo_x(),Bbpawn3.winfo_y()),BP4=crd(Bbpawn4.winfo_x(),Bbpawn4.winfo_y()),BP5=crd(Bbpawn5.winfo_x(),Bbpawn5.winfo_y()),BP6=crd(Bbpawn6.winfo_x(),Bbpawn6.winfo_y()),BP7=crd(Bbpawn7.winfo_x(),Bbpawn7.winfo_y()),BP8=crd(Bbpawn8.winfo_x(),Bbpawn8.winfo_y()),BR1=crd(nx,ny),BR2=crd(Bbrook1.winfo_x(),Bbrook1.winfo_y()),BBI1=crd(Bbbish.winfo_x(),Bbbish.winfo_y()),BBI2=crd(Bbbish1.winfo_x(),Bbbish1.winfo_y()),BN1=crd(Bbnit.winfo_x(),Bbnit.winfo_y()),BN2=crd(Bbnit1.winfo_x(),Bbnit1.winfo_y()),BK=crd(Bbking.winfo_x(),Bbking.winfo_y()),BQ=crd(Bbqueen.winfo_x(),Bbqueen.winfo_y()),WR1=crd(Bwrook.winfo_x(),Bwrook.winfo_y()),WR2=crd(Bwrook1.winfo_x(),Bwrook1.winfo_y()),WBI1=crd(Bwbish.winfo_x(),Bwbish.winfo_y()),WBI2=crd(Bwbish1.winfo_x(),Bwbish1.winfo_y()),WN1=crd(Bwnit.winfo_x(),Bwnit.winfo_y()),WN2=crd(Bwnit1.winfo_x(),Bwnit1.winfo_y()),WK=crd(Bwking.winfo_x(),Bwking.winfo_y()),WQ=crd(Bwqueen.winfo_x(),Bwqueen.winfo_y()))
            terminator(Bbrook)
            sw.unbind("<Button-1>")
        except :
            print("click in the box not on the button")
            xi=2
        if xi==2:
            pass
        else:
            changer(2)
    sw.bind("<Button-1>",mover2)

def draggerBbrook1():
     global Bbrook1
     global cx
     global cy
     cx=Bbrook1.winfo_x() 
     cy=Bbrook1.winfo_y()
     
def moverBbrook1():
    
    global sw
    global cx
    global cy
    def mover2(event):
        global Bbrook1
        x=event.x
        y=event.y
        if (x<(cx+67)and x>(cx-7)) and (y<(cy-8) and y>(cy-76)):
            nx=cx
            ny=cy-68
            Bbrook1.place(x=nx,y=ny)
        elif (x<(cx+67)and x>(cx-7)) and (y<(cy-76) and y>(cy-144)):
            nx=cx
            ny=cy-136
            Bbrook1.place(x=nx,y=ny)
        elif (x<(cx+67)and x>(cx-7)) and (y<(cy-144) and y>(cy-212)):
            nx=cx
            ny=cy-204
            Bbrook1.place(x=nx,y=ny)
        elif (x<(cx+67)and x>(cx-7)) and (y<(cy-212) and y>(cy-280)):
            nx=cx
            ny=cy-272
            Bbrook1.place(x=nx,y=ny)
        elif (x<(cx+67)and x>(cx-7)) and (y<(cy-280) and y>(cy-348)):
            nx=cx
            ny=cy-340
            Bbrook1.place(x=nx,y=ny)
        elif (x<(cx+67)and x>(cx-7)) and (y<(cy-348) and y>(cy-416)):
            nx=cx
            ny=cy-408
            Bbrook1.place(x=nx,y=ny)
        elif (x<(cx+67)and x>(cx-7)) and (y<(cy-416) and y>(cy-484)):
            nx=cx
            ny=cy-476
            Bbrook1.place(x=nx,y=ny)
        elif (x<(cx+67)and x>(cx-7)) and (y<(cy+128) and y>(cy+60)):
            nx=cx
            ny=cy+68
            Bbrook1.place(x=nx,y=ny)
        elif (x<(cx+67)and x>(cx-7)) and (y<(cy+196) and y>(cy+128)):
            nx=cx
            ny=cy+136
            Bbrook1.place(x=nx,y=ny)
        elif (x<(cx+67)and x>(cx-7)) and (y<(cy+264) and y>(cy+196)):
            nx=cx
            ny=cy+204
            Bbrook1.place(x=nx,y=ny)
        elif (x<(cx+67)and x>(cx-7)) and (y<(cy+332) and y>(cy+264)):
            nx=cx
            ny=cy+272
            Bbrook1.place(x=nx,y=ny)
        elif (x<(cx+67)and x>(cx-7)) and (y<(cy+400) and y>(cy+332)):
            nx=cx
            ny=cy+340
            Bbrook1.place(x=nx,y=ny)
        elif (x<(cx+67)and x>(cx-7)) and (y<(cy+468) and y>(cy+400)):
            nx=cx
            ny=cy+408
            Bbrook1.place(x=nx,y=ny)
        elif (x<(cx+67)and x>(cx-7)) and (y<(cy+536) and y>(cy+468)):
            nx=cx
            ny=cy+476
            Bbrook1.place(x=nx,y=ny)
        elif (x<(cx+141)and x>(cx+67)) and (y<(cy+60) and y>(cy-8)):
            nx=cx+75
            ny=cy
            Bbrook1.place(x=nx,y=ny)
        elif (x<(cx+215)and x>(cx+141)) and (y<(cy+60) and y>(cy-8)):
            nx=cx+150
            ny=cy
            Bbrook1.place(x=nx,y=ny)
        elif (x<(cx+289)and x>(cx+215)) and (y<(cy+60) and y>(cy-8)):
            nx=cx+225
            ny=cy
            Bbrook1.place(x=nx,y=ny)
        elif (x<(cx+363)and x>(cx+289)) and (y<(cy+60) and y>(cy-8)):
            nx=cx+300
            ny=cy
            Bbrook1.place(x=nx,y=ny)
        elif (x<(cx+437)and x>(cx+363)) and (y<(cy+60) and y>(cy-8)):
            nx=cx+375
            ny=cy
            Bbrook1.place(x=nx,y=ny)
        elif (x<(cx+511)and x>(cx+437)) and (y<(cy+60) and y>(cy-8)):
            nx=cx+450
            ny=cy
            Bbrook1.place(x=nx,y=ny)
        elif (x<(cx+585)and x>(cx+511)) and (y<(cy+60) and y>(cy-8)):
            nx=cx+526
            ny=cy
            Bbrook1.place(x=nx,y=ny)
        elif (x<(cx-13)and x>(cx-87)) and (y<(cy+60) and y>(cy-8)):
            nx=cx-75
            ny=cy
            Bbrook1.place(x=nx,y=ny)
        elif (x<(cx-87)and x>(cx-161)) and (y<(cy+60) and y>(cy-8)):
            nx=cx-150
            ny=cy
            Bbrook1.place(x=nx,y=ny)
        elif (x<(cx-161)and x>(cx-235)) and (y<(cy+60) and y>(cy-8)):
            nx=cx-225
            ny=cy
            Bbrook1.place(x=nx,y=ny)
        elif (x<(cx-235)and x>(cx-309)) and (y<(cy+60) and y>(cy-8)):
            nx=cx-300
            ny=cy
            Bbrook1.place(x=nx,y=ny)
        elif (x<(cx-309)and x>(cx-383)) and (y<(cy+60) and y>(cy-8)):
            nx=cx-375
            ny=cy
            Bbrook1.place(x=nx,y=ny)
        elif (x<(cx-383)and x>(cx-457)) and (y<(cy+60) and y>(cy-8)):
            nx=cx-450
            ny=cy
            Bbrook1.place(x=nx,y=ny)
        elif (x<(cx-457)and x>(cx-531)) and (y<(cy+60) and y>(cy-8)):
            nx=cx-526
            ny=cy
            Bbrook1.place(x=nx,y=ny)
        xi=1
        try:
            Peices_info(WP1=crd(Wbpawn.winfo_x(),Wbpawn.winfo_y()),WP2=crd(Wbpawn1.winfo_x(),Wbpawn1.winfo_y()),WP3=crd(Wbpawn2.winfo_x(),Wbpawn2.winfo_y()),WP4=crd(Wbpawn3.winfo_x(),Wbpawn3.winfo_y()),WP5=crd(Wbpawn4.winfo_x(),Wbpawn4.winfo_y()),WP6=crd(Wbpawn5.winfo_x(),Wbpawn5.winfo_y()),WP7=crd(Wbpawn6.winfo_x(),Wbpawn6.winfo_y()),WP8=crd(Wbpawn7.winfo_x(),Wbpawn7.winfo_y()),BP1=crd(Bbpawn.winfo_x(),Bbpawn.winfo_y()),BP2=crd(Bbpawn2.winfo_x(),Bbpawn2.winfo_y()),BP3=crd(Bbpawn3.winfo_x(),Bbpawn3.winfo_y()),BP4=crd(Bbpawn4.winfo_x(),Bbpawn4.winfo_y()),BP5=crd(Bbpawn5.winfo_x(),Bbpawn5.winfo_y()),BP6=crd(Bbpawn6.winfo_x(),Bbpawn6.winfo_y()),BP7=crd(Bbpawn7.winfo_x(),Bbpawn7.winfo_y()),BP8=crd(Bbpawn8.winfo_x(),Bbpawn8.winfo_y()),BR1=crd(Bbrook.winfo_x(),Bbrook.winfo_y()),BR2=crd(nx,ny),BBI1=crd(Bbbish.winfo_x(),Bbbish.winfo_y()),BBI2=crd(Bbbish1.winfo_x(),Bbbish1.winfo_y()),BN1=crd(Bbnit.winfo_x(),Bbnit.winfo_y()),BN2=crd(Bbnit1.winfo_x(),Bbnit1.winfo_y()),BK=crd(Bbking.winfo_x(),Bbking.winfo_y()),BQ=crd(Bbqueen.winfo_x(),Bbqueen.winfo_y()),WR1=crd(Bwrook.winfo_x(),Bwrook.winfo_y()),WR2=crd(Bwrook1.winfo_x(),Bwrook1.winfo_y()),WBI1=crd(Bwbish.winfo_x(),Bwbish.winfo_y()),WBI2=crd(Bwbish1.winfo_x(),Bwbish1.winfo_y()),WN1=crd(nx,ny),WN2=crd(Bwnit1.winfo_x(),Bwnit1.winfo_y()),WK=crd(Bwking.winfo_x(),Bwking.winfo_y()),WQ=crd(Bwqueen.winfo_x(),Bwqueen.winfo_y()))
            terminator(Bwrook1)
            sw.unbind("<Button-1>")
        except :
            print("click in the box not on the button")
            xi=2
        if xi==2:
            pass
        else:
            changer(2)
    
    sw.bind("<Button-1>",mover2)

def draggerBwbish():
     global cx
     global cy
     cx=Bwbish.winfo_x() 
     cy=Bwbish.winfo_y()

def moverBwbish():
    global sw
    global cx
    global cy
    def mover2(event):
        global n
        global Bwbish
        x=event.x
        y=event.y
        if (x<(cx+141)and x>(cx+67)) and (y<(cy-8) and y>(cy-76)):
            nx=cx+75
            ny=cy-68
            Bwbish.place(x=nx,y=ny)
        elif (x<(cx+215)and x>(cx+141)) and (y<(cy-76) and y>(cy-144)):
            nx=cx+150
            ny=cy-136
            Bwbish.place(x=nx,y=ny)
        elif (x<(cx+289)and x>(cx+215)) and (y<(cy-144) and y>(cy-212)):
            nx=cx+225
            ny=cy-204
            Bwbish.place(x=nx,y=ny)
        elif (x<(cx+363)and x>(cx+289)) and (y<(cy-212) and y>(cy-280)):
            nx=cx+300
            ny=cy-272
            Bwbish.place(x=nx,y=ny)
        elif (x<(cx+437)and x>(cx+363)) and (y<(cy-280) and y>(cy-348)):
            nx=cx+375
            ny=cy-340
            Bwbish.place(x=nx,y=ny)
        elif (x<(cx+511)and x>(cx+437)) and (y<(cy-348) and y>(cy-416)):
            nx=cx+450
            ny=cy-408
            Bwbish.place(x=nx,y=ny)
        elif (x<(cx+585)and x>(cx+511)) and (y<(cy-416) and y>(cy-484)):
            nx=cx+526
            ny=cy-476
            Bwbish.place(x=nx,y=ny)
        elif (x<(cx+141)and x>(cx+67)) and (y<(cy+128) and y>(cy+60)):
            nx=cx+75
            ny=cy+68
            Bwbish.place(x=nx,y=ny)
        elif (x<(cx+215)and x>(cx+141)) and (y<(cy+196) and y>(cy+128)):
            nx=cx+150
            ny=cy+136
            Bwbish.place(x=nx,y=ny)
        elif (x<(cx+289)and x>(cx+215)) and (y<(cy+264) and y>(cy+196)):
            nx=cx+225
            ny=cy+204
            Bwbish.place(x=nx,y=ny)
        elif (x<(cx+363)and x>(cx+289)) and (y<(cy+332) and y>(cy+264)):
            nx=cx+300
            ny=cy+272
            Bwbish.place(x=nx,y=ny)
        elif (x<(cx+437)and x>(cx+363)) and (y<(cy+400) and y>(cy+332)):
            nx=cx+375
            ny=cy+340
            Bwbish.place(x=nx,y=ny)
        elif (x<(cx+511)and x>(cx+437)) and (y<(cy+468) and y>(cy+400)):
            nx=cx+450
            ny=cy+408
            Bwbish.place(x=nx,y=ny)
        elif (x<(cx+585)and x>(cx+511)) and (y<(cy+536) and y>(cy+468)):
            nx=cx+526
            ny=cy+476
            Bwbish.place(x=nx,y=ny)
        elif (x<(cx-13)and x>(cx-87)) and (y<(cy-8) and y>(cy-76)):
            nx=cx-75
            ny=cy-68
            Bwbish.place(x=nx,y=ny)
        elif (x<(cx-87)and x>(cx-161)) and (y<(cy-76) and y>(cy-144)):
            nx=cx-150
            ny=cy-136
            Bwbish.place(x=nx,y=ny)
        elif (x<(cx-161)and x>(cx-235)) and (y<(cy-144) and y>(cy-212)):
            nx=cx-225
            ny=cy-204
            Bwbish.place(x=nx,y=ny)
        elif (x<(cx-235)and x>(cx-309)) and (y<(cy-212) and y>(cy-280)):
            nx=cx-300
            ny=cy-272
            Bwbish.place(x=nx,y=ny)
        elif (x<(cx-309)and x>(cx-383)) and (y<(cy-280) and y>(cy-348)):
            nx=cx-375
            ny=cy-340
            Bwbish.place(x=nx,y=ny)
        elif (x<(cx-383)and x>(cx-457)) and (y<(cy-348) and y>(cy-416)):
            nx=cx-450
            ny=cy-408
            Bwbish.place(x=nx,y=ny)
        elif (x<(cx-457)and x>(cx+531)) and (y<(cy-416) and y>(cy-484)):
            nx=cx-526
            ny=cy-476
            Bwbish.place(x=nx,y=ny)
        elif (x<(cx-13)and x>(cx-87)) and (y<(cy+128) and y>(cy+60)):
            nx=cx-75
            ny=cy+68
            Bwbish.place(x=nx,y=ny)
        elif (x<(cx-87)and x>(cx-161)) and (y<(cy+196) and y>(cy+128)):
            nx=cx-150
            ny=cy+136
            Bwbish.place(x=nx,y=ny)
        elif (x<(cx-161)and x>(cx-235)) and (y<(cy+264) and y>(cy+196)):
            nx=cx-225
            ny=cy+204
            Bwbish.place(x=nx,y=ny)
        elif (x<(cx-235)and x>(cx-309)) and (y<(cy+332) and y>(cy+264)):
            nx=cx-300
            ny=cy+272
            Bwbish.place(x=nx,y=ny)
        elif (x<(cx-309)and x>(cx-383)) and (y<(cy+400) and y>(cy+332)):
            nx=cx-375
            ny=cy+340
            Bwbish.place(x=nx,y=ny)
        elif (x<(cx-383)and x>(cx-457)) and (y<(cy+468) and y>(cy+400)):
            nx=cx-450
            ny=cy+408
            Bwbish.place(x=nx,y=ny)
        elif (x<(cx-457)and x>(cx+531)) and (y<(cy+536) and y>(cy+468)):
            nx=cx-526
            ny=cy+476
            Bwbish.place(x=nx,y=ny)
        print(nx,"  ",ny)
        xi=1
        try:
           Peices_info(WP1=crd(Wbpawn.winfo_x(),Wbpawn.winfo_y()),WP2=crd(Wbpawn1.winfo_x(),Wbpawn1.winfo_y()),WP3=crd(Wbpawn2.winfo_x(),Wbpawn2.winfo_y()),WP4=crd(Wbpawn3.winfo_x(),Wbpawn3.winfo_y()),WP5=crd(Wbpawn4.winfo_x(),Wbpawn4.winfo_y()),WP6=crd(Wbpawn5.winfo_x(),Wbpawn5.winfo_y()),WP7=crd(Wbpawn6.winfo_x(),Wbpawn6.winfo_y()),WP8=crd(Wbpawn7.winfo_x(),Wbpawn7.winfo_y()),BP1=crd(Bbpawn.winfo_x(),Bbpawn.winfo_y()),BP2=crd(Bbpawn2.winfo_x(),Bbpawn2.winfo_y()),BP3=crd(Bbpawn3.winfo_x(),Bbpawn3.winfo_y()),BP4=crd(Bbpawn4.winfo_x(),Bbpawn4.winfo_y()),BP5=crd(Bbpawn5.winfo_x(),Bbpawn5.winfo_y()),BP6=crd(Bbpawn6.winfo_x(),Bbpawn6.winfo_y()),BP7=crd(Bbpawn7.winfo_x(),Bbpawn7.winfo_y()),BP8=crd(Bbpawn8.winfo_x(),Bbpawn8.winfo_y()),BR1=crd(Bbrook.winfo_x(),Bbrook.winfo_y()),BR2=crd(Bbrook1.winfo_x(),Bbrook1.winfo_y()),BBI1=crd(Bbbish.winfo_x(),Bbbish.winfo_y()),BBI2=crd(Bbbish1.winfo_x(),Bbbish1.winfo_y()),BN1=crd(Bbnit.winfo_x(),Bbnit.winfo_y()),BN2=crd(Bbnit1.winfo_x(),Bbnit1.winfo_y()),BK=crd(Bbking.winfo_x(),Bbking.winfo_y()),BQ=crd(Bbqueen.winfo_x(),Bbqueen.winfo_y()),WR1=crd(Bwrook.winfo_x(),Bwrook.winfo_y()),WR2=crd(Bwrook1.winfo_x(),Bwrook1.winfo_y()),WBI1=crd(nx,ny),WBI2=crd(Bwbish1.winfo_x(),Bwbish1.winfo_y()),WN1=crd(Bwnit.winfo_x(),Bwnit.winfo_y()),WN2=crd(Bwnit1.winfo_x(),Bwnit1.winfo_y()),WK=crd(Bwking.winfo_x(),Bwking.winfo_y()),WQ=crd(Bwqueen.winfo_x(),Bwqueen.winfo_y()))
           terminator(Bwbish)
           sw.unbind("<Button-1>")
        except:
            print("CLick in the box not on the button")
            xi=2
        if xi==2:
            pass
        else:
            changer(1)
    sw.bind("<Button-1>",mover2)

def draggerBwbish1():
     global cx
     global cy
     cx=Bwbish1.winfo_x() 
     cy=Bwbish1.winfo_y()

def moverBwbish1():
    global sw
    global cx
    global cy
    def mover2(event):
        global n
        global Bwbish1
        x=event.x
        y=event.y
        if (x<(cx+141)and x>(cx+67)) and (y<(cy-8) and y>(cy-76)):
            nx=cx+75
            ny=cy-68
            Bwbish1.place(x=nx,y=ny)
        elif (x<(cx+215)and x>(cx+141)) and (y<(cy-76) and y>(cy-144)):
            nx=cx+150
            ny=cy-136
            Bwbish1.place(x=nx,y=ny)
        elif (x<(cx+289)and x>(cx+215)) and (y<(cy-144) and y>(cy-212)):
            nx=cx+225
            ny=cy-204
            Bwbish1.place(x=nx,y=ny)
        elif (x<(cx+363)and x>(cx+289)) and (y<(cy-212) and y>(cy-280)):
            nx=cx+300
            ny=cy-272
            Bwbish1.place(x=nx,y=ny)
        elif (x<(cx+437)and x>(cx+363)) and (y<(cy-280) and y>(cy-348)):
            nx=cx+375
            ny=cy-340
            Bwbish1.place(x=nx,y=ny)
        elif (x<(cx+511)and x>(cx+437)) and (y<(cy-348) and y>(cy-416)):
            nx=cx+450
            ny=cy-408
            Bwbish1.place(x=nx,y=ny)
        elif (x<(cx+585)and x>(cx+511)) and (y<(cy-416) and y>(cy-484)):
            nx=cx+526
            ny=cy-476
            Bwbish1.place(x=nx,y=ny)
        elif (x<(cx+141)and x>(cx+67)) and (y<(cy+128) and y>(cy+60)):
            nx=cx+75
            ny=cy+68
            Bwbish1.place(x=nx,y=ny)
        elif (x<(cx+215)and x>(cx+141)) and (y<(cy+196) and y>(cy+128)):
            nx=cx+150
            ny=cy+136
            Bwbish1.place(x=nx,y=ny)
        elif (x<(cx+289)and x>(cx+215)) and (y<(cy+264) and y>(cy+196)):
            nx=cx+225
            ny=cy+204
            Bwbish1.place(x=nx,y=ny)
        elif (x<(cx+363)and x>(cx+289)) and (y<(cy+332) and y>(cy+264)):
            nx=cx+300
            ny=cy+272
            Bwbish1.place(x=nx,y=ny)
        elif (x<(cx+437)and x>(cx+363)) and (y<(cy+400) and y>(cy+332)):
            nx=cx+375
            ny=cy+340
            Bwbish1.place(x=nx,y=ny)
        elif (x<(cx+511)and x>(cx+437)) and (y<(cy+468) and y>(cy+400)):
            nx=cx+450
            ny=cy+408
            Bwbish1.place(x=nx,y=ny)
        elif (x<(cx+585)and x>(cx+511)) and (y<(cy+536) and y>(cy+468)):
            nx=cx+526
            ny=cy+476
            Bwbish1.place(x=nx,y=ny)
        elif (x<(cx-13)and x>(cx-87)) and (y<(cy-8) and y>(cy-76)):
            nx=cx-75
            ny=cy-68
            Bwbish1.place(x=nx,y=ny)
        elif (x<(cx-87)and x>(cx-161)) and (y<(cy-76) and y>(cy-144)):
            nx=cx-150
            ny=cy-136
            Bwbish1.place(x=nx,y=ny)
        elif (x<(cx-161)and x>(cx-235)) and (y<(cy-144) and y>(cy-212)):
            nx=cx-225
            ny=cy-204
            Bwbish1.place(x=nx,y=ny)
        elif (x<(cx-235)and x>(cx-309)) and (y<(cy-212) and y>(cy-280)):
            nx=cx-300
            ny=cy-272
            Bwbish1.place(x=nx,y=ny)
        elif (x<(cx-309)and x>(cx-383)) and (y<(cy-280) and y>(cy-348)):
            nx=cx-375
            ny=cy-340
            Bwbish1.place(x=nx,y=ny)
        elif (x<(cx-383)and x>(cx-457)) and (y<(cy-348) and y>(cy-416)):
            nx=cx-450
            ny=cy-408
            Bwbish1.place(x=nx,y=ny)
        elif (x<(cx-457)and x>(cx+531)) and (y<(cy-416) and y>(cy-484)):
            nx=cx-526
            ny=cy-476
            Bwbish1.place(x=nx,y=ny)
        elif (x<(cx-13)and x>(cx-87)) and (y<(cy+128) and y>(cy+60)):
            nx=cx-75
            ny=cy+68
            Bwbish1.place(x=nx,y=ny)
        elif (x<(cx-87)and x>(cx-161)) and (y<(cy+196) and y>(cy+128)):
            nx=cx-150
            ny=cy+136
            Bwbish1.place(x=nx,y=ny)
        elif (x<(cx-161)and x>(cx-235)) and (y<(cy+264) and y>(cy+196)):
            nx=cx-225
            ny=cy+204
            Bwbish1.place(x=nx,y=ny)
        elif (x<(cx-235)and x>(cx-309)) and (y<(cy+332) and y>(cy+264)):
            nx=cx-300
            ny=cy+272
            Bwbish1.place(x=nx,y=ny)
        elif (x<(cx-309)and x>(cx-383)) and (y<(cy+400) and y>(cy+332)):
            nx=cx-375
            ny=cy+340
            Bwbish1.place(x=nx,y=ny)
        elif (x<(cx-383)and x>(cx-457)) and (y<(cy+468) and y>(cy+400)):
            nx=cx-450
            ny=cy+408
            Bwbish1.place(x=nx,y=ny)
        elif (x<(cx-457)and x>(cx+531)) and (y<(cy+536) and y>(cy+468)):
            nx=cx-526
            ny=cy+476
            Bwbish1.place(x=nx,y=ny)
        print(nx,"  ",ny)
        xi=1
        try:
            Peices_info(WP1=crd(Wbpawn.winfo_x(),Wbpawn.winfo_y()),WP2=crd(Wbpawn1.winfo_x(),Wbpawn1.winfo_y()),WP3=crd(Wbpawn2.winfo_x(),Wbpawn2.winfo_y()),WP4=crd(Wbpawn3.winfo_x(),Wbpawn3.winfo_y()),WP5=crd(Wbpawn4.winfo_x(),Wbpawn4.winfo_y()),WP6=crd(Wbpawn5.winfo_x(),Wbpawn5.winfo_y()),WP7=crd(Wbpawn6.winfo_x(),Wbpawn6.winfo_y()),WP8=crd(Wbpawn7.winfo_x(),Wbpawn7.winfo_y()),BP1=crd(Bbpawn.winfo_x(),Bbpawn.winfo_y()),BP2=crd(Bbpawn2.winfo_x(),Bbpawn2.winfo_y()),BP3=crd(Bbpawn3.winfo_x(),Bbpawn3.winfo_y()),BP4=crd(Bbpawn4.winfo_x(),Bbpawn4.winfo_y()),BP5=crd(Bbpawn5.winfo_x(),Bbpawn5.winfo_y()),BP6=crd(Bbpawn6.winfo_x(),Bbpawn6.winfo_y()),BP7=crd(Bbpawn7.winfo_x(),Bbpawn7.winfo_y()),BP8=crd(Bbpawn8.winfo_x(),Bbpawn8.winfo_y()),BR1=crd(Bbrook.winfo_x(),Bbrook.winfo_y()),BR2=crd(Bbrook1.winfo_x(),Bbrook1.winfo_y()),BBI1=crd(Bbbish.winfo_x(),Bbbish.winfo_y()),BBI2=crd(Bbbish1.winfo_x(),Bbbish1.winfo_y()),BN1=crd(Bbnit.winfo_x(),Bbnit.winfo_y()),BN2=crd(Bbnit1.winfo_x(),Bbnit1.winfo_y()),BK=crd(Bbking.winfo_x(),Bbking.winfo_y()),BQ=crd(Bbqueen.winfo_x(),Bbqueen.winfo_y()),WR1=crd(Bwrook.winfo_x(),Bwrook.winfo_y()),WR2=crd(Bwrook1.winfo_x(),Bwrook1.winfo_y()),WBI1=crd(Bwbish.winfo_x(),Bwbish.winfo_y()),WBI2=crd(nx,ny),WN1=crd(Bwnit.winfo_x(),Bwnit.winfo_y()),WN2=crd(Bwnit1.winfo_x(),Bwnit1.winfo_y()),WK=crd(Bwking.winfo_x(),Bwking.winfo_y()),WQ=crd(Bwqueen.winfo_x(),Bwqueen.winfo_y()))
            terminator(Bwbish1)
            sw.unbind("<Button-1>")
        except:
            print("Click in the box not on the button")
            xi=2
        if xi==2:
            pass
        else:
            changer(1)
            
    sw.bind("<Button-1>",mover2)

def draggerBbbish():
     global cx
     global cy
     cx=Bbbish.winfo_x() 
     cy=Bbbish.winfo_y()

def moverBbbish():
    global sw
    global cx
    global cy
    def mover2(event):
        global n
        global Bbbish
        x=event.x
        y=event.y
        if (x<(cx+141)and x>(cx+67)) and (y<(cy-8) and y>(cy-76)):
            nx=cx+75
            ny=cy-68
            Bbbish.place(x=nx,y=ny)
        elif (x<(cx+215)and x>(cx+141)) and (y<(cy-76) and y>(cy-144)):
            nx=cx+150
            ny=cy-136
            Bbbish.place(x=nx,y=ny)
        elif (x<(cx+289)and x>(cx+215)) and (y<(cy-144) and y>(cy-212)):
            nx=cx+225
            ny=cy-204
            Bbbish.place(x=nx,y=ny)
        elif (x<(cx+363)and x>(cx+289)) and (y<(cy-212) and y>(cy-280)):
            nx=cx+300
            ny=cy-272
            Bbbish.place(x=nx,y=ny)
        elif (x<(cx+437)and x>(cx+363)) and (y<(cy-280) and y>(cy-348)):
            nx=cx+375
            ny=cy-340
            Bbbish.place(x=nx,y=ny)
        elif (x<(cx+511)and x>(cx+437)) and (y<(cy-348) and y>(cy-416)):
            nx=cx+450
            ny=cy-408
            Bbbish.place(x=nx,y=ny)
        elif (x<(cx+585)and x>(cx+511)) and (y<(cy-416) and y>(cy-484)):
            nx=cx+526
            ny=cy-476
            Bbbish.place(x=nx,y=ny)
        elif (x<(cx+141)and x>(cx+67)) and (y<(cy+128) and y>(cy+60)):
            nx=cx+75
            ny=cy+68
            Bbbish.place(x=nx,y=ny)
        elif (x<(cx+215)and x>(cx+141)) and (y<(cy+196) and y>(cy+128)):
            nx=cx+150
            ny=cy+136
            Bbbish.place(x=nx,y=ny)
        elif (x<(cx+289)and x>(cx+215)) and (y<(cy+264) and y>(cy+196)):
            nx=cx+225
            ny=cy+204
            Bbbish.place(x=nx,y=ny)
        elif (x<(cx+363)and x>(cx+289)) and (y<(cy+332) and y>(cy+264)):
            nx=cx+300
            ny=cy+272
            Bbbish.place(x=nx,y=ny)
        elif (x<(cx+437)and x>(cx+363)) and (y<(cy+400) and y>(cy+332)):
            nx=cx+375
            ny=cy+340
            Bbbish.place(x=nx,y=ny)
        elif (x<(cx+511)and x>(cx+437)) and (y<(cy+468) and y>(cy+400)):
            nx=cx+450
            ny=cy+408
            Bbbish.place(x=nx,y=ny)
        elif (x<(cx+585)and x>(cx+511)) and (y<(cy+536) and y>(cy+468)):
            nx=cx+526
            ny=cy+476
            Bbbish.place(x=nx,y=ny)
        elif (x<(cx-13)and x>(cx-87)) and (y<(cy-8) and y>(cy-76)):
            nx=cx-75
            ny=cy-68
            Bbbish.place(x=nx,y=ny)
        elif (x<(cx-87)and x>(cx-161)) and (y<(cy-76) and y>(cy-144)):
            nx=cx-150
            ny=cy-136
            Bbbish.place(x=nx,y=ny)
        elif (x<(cx-161)and x>(cx-235)) and (y<(cy-144) and y>(cy-212)):
            nx=cx-225
            ny=cy-204
            Bbbish.place(x=nx,y=ny)
        elif (x<(cx-235)and x>(cx-309)) and (y<(cy-212) and y>(cy-280)):
            nx=cx-300
            ny=cy-272
            Bbbish.place(x=nx,y=ny)
        elif (x<(cx-309)and x>(cx-383)) and (y<(cy-280) and y>(cy-348)):
            nx=cx-375
            ny=cy-340
            Bbbish.place(x=nx,y=ny)
        elif (x<(cx-383)and x>(cx-457)) and (y<(cy-348) and y>(cy-416)):
            nx=cx-450
            ny=cy-408
            Bbbish.place(x=nx,y=ny)
        elif (x<(cx-457)and x>(cx+531)) and (y<(cy-416) and y>(cy-484)):
            nx=cx-526
            ny=cy-476
            Bbbish.place(x=nx,y=ny)
        elif (x<(cx-13)and x>(cx-87)) and (y<(cy+128) and y>(cy+60)):
            nx=cx-75
            ny=cy+68
            Bbbish.place(x=nx,y=ny)
        elif (x<(cx-87)and x>(cx-161)) and (y<(cy+196) and y>(cy+128)):
            nx=cx-150
            ny=cy+136
            Bbbish.place(x=nx,y=ny)
        elif (x<(cx-161)and x>(cx-235)) and (y<(cy+264) and y>(cy+196)):
            nx=cx-225
            ny=cy+204
            Bbbish.place(x=nx,y=ny)
        elif (x<(cx-235)and x>(cx-309)) and (y<(cy+332) and y>(cy+264)):
            nx=cx-300
            ny=cy+272
            Bbbish.place(x=nx,y=ny)
        elif (x<(cx-309)and x>(cx-383)) and (y<(cy+400) and y>(cy+332)):
            nx=cx-375
            ny=cy+340
            Bbbish.place(x=nx,y=ny)
        elif (x<(cx-383)and x>(cx-457)) and (y<(cy+468) and y>(cy+400)):
            nx=cx-450
            ny=cy+408
            Bbbish.place(x=nx,y=ny)
        elif (x<(cx-457)and x>(cx+531)) and (y<(cy+536) and y>(cy+468)):
            nx=cx-526
            ny=cy+476
            Bbbish.place(x=nx,y=ny)
        print(nx,"  ",ny)
        xi=1
        try:
            Peices_info(WP1=crd(Wbpawn.winfo_x(),Wbpawn.winfo_y()),WP2=crd(Wbpawn1.winfo_x(),Wbpawn1.winfo_y()),WP3=crd(Wbpawn2.winfo_x(),Wbpawn2.winfo_y()),WP4=crd(Wbpawn3.winfo_x(),Wbpawn3.winfo_y()),WP5=crd(Wbpawn4.winfo_x(),Wbpawn4.winfo_y()),WP6=crd(Wbpawn5.winfo_x(),Wbpawn5.winfo_y()),WP7=crd(Wbpawn6.winfo_x(),Wbpawn6.winfo_y()),WP8=crd(Wbpawn7.winfo_x(),Wbpawn7.winfo_y()),BP1=crd(Bbpawn.winfo_x(),Bbpawn.winfo_y()),BP2=crd(Bbpawn2.winfo_x(),Bbpawn2.winfo_y()),BP3=crd(Bbpawn3.winfo_x(),Bbpawn3.winfo_y()),BP4=crd(Bbpawn4.winfo_x(),Bbpawn4.winfo_y()),BP5=crd(Bbpawn5.winfo_x(),Bbpawn5.winfo_y()),BP6=crd(Bbpawn6.winfo_x(),Bbpawn6.winfo_y()),BP7=crd(Bbpawn7.winfo_x(),Bbpawn7.winfo_y()),BP8=crd(Bbpawn8.winfo_x(),Bbpawn8.winfo_y()),BR1=crd(Bbrook.winfo_x(),Bbrook.winfo_y()),BR2=crd(Bbrook1.winfo_x(),Bbrook1.winfo_y()),BBI1=crd(nx,ny),BBI2=crd(Bbbish1.winfo_x(),Bbbish1.winfo_y()),BN1=crd(Bbnit.winfo_x(),Bbnit.winfo_y()),BN2=crd(Bbnit1.winfo_x(),Bbnit1.winfo_y()),BK=crd(Bbking.winfo_x(),Bbking.winfo_y()),BQ=crd(Bbqueen.winfo_x(),Bbqueen.winfo_y()),WR1=crd(Bwrook.winfo_x(),Bwrook.winfo_y()),WR2=crd(Bwrook1.winfo_x(),Bwrook1.winfo_y()),WBI1=crd(Bwbish.winfo_x(),Bwbish.winfo_y()),WBI2=crd(Bwbish1.winfo_x(),Bwbish1.winfo_y()),WN1=crd(Bwnit.winfo_x(),Bwnit.winfo_y()),WN2=crd(Bwnit1.winfo_x(),Bwnit1.winfo_y()),WK=crd(Bwking.winfo_x(),Bwking.winfo_y()),WQ=crd(Bwqueen.winfo_x(),Bwqueen.winfo_y()))
            terminator(Bbbish)
            sw.unbind("<Button-1>")
        except:
            print("Click in the box not inside the button")
            xi=2
        if xi==2:
            pass
        else:
            changer(2)
    sw.bind("<Button-1>",mover2)

def draggerBbbish1():
     global cx
     global cy
     cx=Bbbish1.winfo_x() 
     cy=Bbbish1.winfo_y()

def moverBbbish1():
    global sw
    global cx
    global cy
    def mover2(event):
        global n
        global Bbbish1
        x=event.x
        y=event.y
        if (x<(cx+141)and x>(cx+67)) and (y<(cy-8) and y>(cy-76)):
            nx=cx+75
            ny=cy-68
            Bbbish1.place(x=nx,y=ny)
        elif (x<(cx+215)and x>(cx+141)) and (y<(cy-76) and y>(cy-144)):
            nx=cx+150
            ny=cy-136
            Bbbish1.place(x=nx,y=ny)
        elif (x<(cx+289)and x>(cx+215)) and (y<(cy-144) and y>(cy-212)):
            nx=cx+225
            ny=cy-204
            Bbbish1.place(x=nx,y=ny)
        elif (x<(cx+363)and x>(cx+289)) and (y<(cy-212) and y>(cy-280)):
            nx=cx+300
            ny=cy-272
            Bbbish1.place(x=nx,y=ny)
        elif (x<(cx+437)and x>(cx+363)) and (y<(cy-280) and y>(cy-348)):
            nx=cx+375
            ny=cy-340
            Bbbish1.place(x=nx,y=ny)
        elif (x<(cx+511)and x>(cx+437)) and (y<(cy-348) and y>(cy-416)):
            nx=cx+450
            ny=cy-408
            Bbbish1.place(x=nx,y=ny)
        elif (x<(cx+585)and x>(cx+511)) and (y<(cy-416) and y>(cy-484)):
            nx=cx+526
            ny=cy-476
            Bbbish1.place(x=nx,y=ny)
        elif (x<(cx+141)and x>(cx+67)) and (y<(cy+128) and y>(cy+60)):
            nx=cx+75
            ny=cy+68
            Bbbish1.place(x=nx,y=ny)
        elif (x<(cx+215)and x>(cx+141)) and (y<(cy+196) and y>(cy+128)):
            nx=cx+150
            ny=cy+136
            Bbbish1.place(x=nx,y=ny)
        elif (x<(cx+289)and x>(cx+215)) and (y<(cy+264) and y>(cy+196)):
            nx=cx+225
            ny=cy+204
            Bbbish1.place(x=nx,y=ny)
        elif (x<(cx+363)and x>(cx+289)) and (y<(cy+332) and y>(cy+264)):
            nx=cx+300
            ny=cy+272
            Bbbish1.place(x=nx,y=ny)
        elif (x<(cx+437)and x>(cx+363)) and (y<(cy+400) and y>(cy+332)):
            nx=cx+375
            ny=cy+340
            Bbbish1.place(x=nx,y=ny)
        elif (x<(cx+511)and x>(cx+437)) and (y<(cy+468) and y>(cy+400)):
            nx=cx+450
            ny=cy+408
            Bbbish1.place(x=nx,y=ny)
        elif (x<(cx+585)and x>(cx+511)) and (y<(cy+536) and y>(cy+468)):
            nx=cx+526
            ny=cy+476
            Bbbish1.place(x=nx,y=ny)
        elif (x<(cx-13)and x>(cx-87)) and (y<(cy-8) and y>(cy-76)):
            nx=cx-75
            ny=cy-68
            Bbbish1.place(x=nx,y=ny)
        elif (x<(cx-87)and x>(cx-161)) and (y<(cy-76) and y>(cy-144)):
            nx=cx-150
            ny=cy-136
            Bbbish1.place(x=nx,y=ny)
        elif (x<(cx-161)and x>(cx-235)) and (y<(cy-144) and y>(cy-212)):
            nx=cx-225
            ny=cy-204
            Bbbish1.place(x=nx,y=ny)
        elif (x<(cx-235)and x>(cx-309)) and (y<(cy-212) and y>(cy-280)):
            nx=cx-300
            ny=cy-272
            Bbbish1.place(x=nx,y=ny)
        elif (x<(cx-309)and x>(cx-383)) and (y<(cy-280) and y>(cy-348)):
            nx=cx-375
            ny=cy-340
            Bbbish1.place(x=nx,y=ny)
        elif (x<(cx-383)and x>(cx-457)) and (y<(cy-348) and y>(cy-416)):
            nx=cx-450
            ny=cy-408
            Bbbish1.place(x=nx,y=ny)
        elif (x<(cx-457)and x>(cx+531)) and (y<(cy-416) and y>(cy-484)):
            nx=cx-526
            ny=cy-476
            Bbbish1.place(x=nx,y=ny)
        elif (x<(cx-13)and x>(cx-87)) and (y<(cy+128) and y>(cy+60)):
            nx=cx-75
            ny=cy+68
            Bbbish1.place(x=nx,y=ny)
        elif (x<(cx-87)and x>(cx-161)) and (y<(cy+196) and y>(cy+128)):
            nx=cx-150
            ny=cy+136
            Bbbish1.place(x=nx,y=ny)
        elif (x<(cx-161)and x>(cx-235)) and (y<(cy+264) and y>(cy+196)):
            nx=cx-225
            ny=cy+204
            Bbbish1.place(x=nx,y=ny)
        elif (x<(cx-235)and x>(cx-309)) and (y<(cy+332) and y>(cy+264)):
            nx=cx-300
            ny=cy+272
            Bbbish1.place(x=nx,y=ny)
        elif (x<(cx-309)and x>(cx-383)) and (y<(cy+400) and y>(cy+332)):
            nx=cx-375
            ny=cy+340
            Bbbish1.place(x=nx,y=ny)
        elif (x<(cx-383)and x>(cx-457)) and (y<(cy+468) and y>(cy+400)):
            nx=cx-450
            ny=cy+408
            Bbbish1.place(x=nx,y=ny)
        elif (x<(cx-457)and x>(cx+531)) and (y<(cy+536) and y>(cy+468)):
            nx=cx-526
            ny=cy+476
            Bbbish1.place(x=nx,y=ny)
        print(nx,"  ",ny)
        xi=1
        try:
            Peices_info(WP1=crd(Wbpawn.winfo_x(),Wbpawn.winfo_y()),WP2=crd(Wbpawn1.winfo_x(),Wbpawn1.winfo_y()),WP3=crd(Wbpawn2.winfo_x(),Wbpawn2.winfo_y()),WP4=crd(Wbpawn3.winfo_x(),Wbpawn3.winfo_y()),WP5=crd(Wbpawn4.winfo_x(),Wbpawn4.winfo_y()),WP6=crd(Wbpawn5.winfo_x(),Wbpawn5.winfo_y()),WP7=crd(Wbpawn6.winfo_x(),Wbpawn6.winfo_y()),WP8=crd(Wbpawn7.winfo_x(),Wbpawn7.winfo_y()),BP1=crd(Bbpawn.winfo_x(),Bbpawn.winfo_y()),BP2=crd(Bbpawn2.winfo_x(),Bbpawn2.winfo_y()),BP3=crd(Bbpawn3.winfo_x(),Bbpawn3.winfo_y()),BP4=crd(Bbpawn4.winfo_x(),Bbpawn4.winfo_y()),BP5=crd(Bbpawn5.winfo_x(),Bbpawn5.winfo_y()),BP6=crd(Bbpawn6.winfo_x(),Bbpawn6.winfo_y()),BP7=crd(Bbpawn7.winfo_x(),Bbpawn7.winfo_y()),BP8=crd(Bbpawn8.winfo_x(),Bbpawn8.winfo_y()),BR1=crd(Bbrook.winfo_x(),Bbrook.winfo_y()),BR2=crd(Bbrook1.winfo_x(),Bbrook1.winfo_y()),BBI1=crd(Bbbish.winfo_x(),Bbbish.winfo_y()),BBI2=crd(nx,ny),BN1=crd(Bbnit.winfo_x(),Bbnit.winfo_y()),BN2=crd(Bbnit1.winfo_x(),Bbnit1.winfo_y()),BK=crd(Bbking.winfo_x(),Bbking.winfo_y()),BQ=crd(Bbqueen.winfo_x(),Bbqueen.winfo_y()),WR1=crd(Bwrook.winfo_x(),Bwrook.winfo_y()),WR2=crd(Bwrook1.winfo_x(),Bwrook1.winfo_y()),WBI1=crd(Bwbish.winfo_x(),Bwbish.winfo_y()),WBI2=crd(Bwbish1.winfo_x(),Bwbish1.winfo_y()),WN1=crd(Bwnit.winfo_x(),Bwnit.winfo_y()),WN2=crd(Bwnit1.winfo_x(),Bwnit1.winfo_y()),WK=crd(Bwking.winfo_x(),Bwking.winfo_y()),WQ=crd(Bwqueen.winfo_x(),Bwqueen.winfo_y()))
            terminator(Bbbish1)
            sw.unbind("<Button-1>")
        except:
            print("Click in the box not on the button")
            xi=2
        if xi==2:
            pass
        else:
            changer(2)
    sw.bind("<Button-1>",mover2)

def draggerBwqueen():
     global cx
     global cy
     cx=Bwqueen.winfo_x() 
     cy=Bwqueen.winfo_y()

def moverBwqueen():
    global sw
    global cx
    global cy
    def mover2(event):
        global n
        global Bwqueen
        x=event.x
        y=event.y
        if (x<(cx+141)and x>(cx+67)) and (y<(cy-8) and y>(cy-76)):
            nx=cx+75
            ny=cy-68
            Bwqueen.place(x=nx,y=ny)
        elif (x<(cx+215)and x>(cx+141)) and (y<(cy-76) and y>(cy-144)):
            nx=cx+150
            ny=cy-136
            Bwqueen.place(x=nx,y=ny)
        elif (x<(cx+289)and x>(cx+215)) and (y<(cy-144) and y>(cy-212)):
            nx=cx+225
            ny=cy-204
            Bwqueen.place(x=nx,y=ny)
        elif (x<(cx+363)and x>(cx+289)) and (y<(cy-212) and y>(cy-280)):
            nx=cx+300
            ny=cy-272
            Bwqueen.place(x=nx,y=ny)
        elif (x<(cx+437)and x>(cx+363)) and (y<(cy-280) and y>(cy-348)):
            nx=cx+375
            ny=cy-340
            Bwqueen.place(x=nx,y=ny)
        elif (x<(cx+511)and x>(cx+437)) and (y<(cy-348) and y>(cy-416)):
            nx=cx+450
            ny=cy-408
            Bwqueen.place(x=nx,y=ny)
        elif (x<(cx+585)and x>(cx+511)) and (y<(cy-416) and y>(cy-484)):
            nx=cx+526
            ny=cy-476
            Bwqueen.place(x=nx,y=ny)
        elif (x<(cx+141)and x>(cx+67)) and (y<(cy+128) and y>(cy+60)):
            nx=cx+75
            ny=cy+68
            Bwqueen.place(x=nx,y=ny)
        elif (x<(cx+215)and x>(cx+141)) and (y<(cy+196) and y>(cy+128)):
            nx=cx+150
            ny=cy+136
            Bwqueen.place(x=nx,y=ny)
        elif (x<(cx+289)and x>(cx+215)) and (y<(cy+264) and y>(cy+196)):
            nx=cx+225
            ny=cy+204
            Bwqueen.place(x=nx,y=ny)
        elif (x<(cx+363)and x>(cx+289)) and (y<(cy+332) and y>(cy+264)):
            nx=cx+300
            ny=cy+272
            Bwqueen.place(x=nx,y=ny)
        elif (x<(cx+437)and x>(cx+363)) and (y<(cy+400) and y>(cy+332)):
            nx=cx+375
            ny=cy+340
            Bwqueen.place(x=nx,y=ny)
        elif (x<(cx+511)and x>(cx+437)) and (y<(cy+468) and y>(cy+400)):
            nx=cx+450
            ny=cy+408
            Bwqueen.place(x=nx,y=ny)
        elif (x<(cx+585)and x>(cx+511)) and (y<(cy+536) and y>(cy+468)):
            nx=cx+526
            ny=cy+476
            Bwqueen.place(x=nx,y=ny)
        elif (x<(cx-13)and x>(cx-87)) and (y<(cy-8) and y>(cy-76)):
            nx=cx-75
            ny=cy-68
            Bwqueen.place(x=nx,y=ny)
        elif (x<(cx-87)and x>(cx-161)) and (y<(cy-76) and y>(cy-144)):
            nx=cx-150
            ny=cy-136
            Bwqueen.place(x=nx,y=ny)
        elif (x<(cx-161)and x>(cx-235)) and (y<(cy-144) and y>(cy-212)):
            nx=cx-225
            ny=cy-204
            Bwqueen.place(x=nx,y=ny)
        elif (x<(cx-235)and x>(cx-309)) and (y<(cy-212) and y>(cy-280)):
            nx=cx-300
            ny=cy-272
            Bwqueen.place(x=nx,y=ny)
        elif (x<(cx-309)and x>(cx-383)) and (y<(cy-280) and y>(cy-348)):
            nx=cx-375
            ny=cy-340
            Bwqueen.place(x=nx,y=ny)
        elif (x<(cx-383)and x>(cx-457)) and (y<(cy-348) and y>(cy-416)):
            nx=cx-450
            ny=cy-408
            Bwqueen.place(x=nx,y=ny)
        elif (x<(cx-457)and x>(cx+531)) and (y<(cy-416) and y>(cy-484)):
            nx=cx-526
            ny=cy-476
            Bwqueen.place(x=nx,y=ny)
        elif (x<(cx-13)and x>(cx-87)) and (y<(cy+128) and y>(cy+60)):
            nx=cx-75
            ny=cy+68
            Bwqueen.place(x=nx,y=ny)
        elif (x<(cx-87)and x>(cx-161)) and (y<(cy+196) and y>(cy+128)):
            nx=cx-150
            ny=cy+136
            Bwqueen.place(x=nx,y=ny)
        elif (x<(cx-161)and x>(cx-235)) and (y<(cy+264) and y>(cy+196)):
            nx=cx-225
            ny=cy+204
            Bwqueen.place(x=nx,y=ny)
        elif (x<(cx-235)and x>(cx-309)) and (y<(cy+332) and y>(cy+264)):
            nx=cx-300
            ny=cy+272
            Bwqueen.place(x=nx,y=ny)
        elif (x<(cx-309)and x>(cx-383)) and (y<(cy+400) and y>(cy+332)):
            nx=cx-375
            ny=cy+340
            Bwqueen.place(x=nx,y=ny)
        elif (x<(cx-383)and x>(cx-457)) and (y<(cy+468) and y>(cy+400)):
            nx=cx-450
            ny=cy+408
            Bwqueen.place(x=nx,y=ny)
        elif (x<(cx-457)and x>(cx+531)) and (y<(cy+536) and y>(cy+468)):
            nx=cx-526
            ny=cy+476
            Bwqueen.place(x=nx,y=ny)
        elif (x<(cx+67)and x>(cx-7)) and (y<(cy-8) and y>(cy-76)):
            nx=cx
            ny=cy-68
            Bwqueen.place(x=nx,y=ny)
        elif (x<(cx+67)and x>(cx-7)) and (y<(cy-76) and y>(cy-144)):
            nx=cx
            ny=cy-136
            Bwqueen.place(x=nx,y=ny)
        elif (x<(cx+67)and x>(cx-7)) and (y<(cy-144) and y>(cy-212)):
            nx=cx
            ny=cy-204
            Bwqueen.place(x=nx,y=ny)
        elif (x<(cx+67)and x>(cx-7)) and (y<(cy-212) and y>(cy-280)):
            nx=cx
            ny=cy-272
            Bwqueen.place(x=nx,y=ny)
        elif (x<(cx+67)and x>(cx-7)) and (y<(cy-280) and y>(cy-348)):
            nx=cx
            ny=cy-340
            Bwqueen.place(x=nx,y=ny)
        elif (x<(cx+67)and x>(cx-7)) and (y<(cy-348) and y>(cy-416)):
            nx=cx
            ny=cy-408
            Bwqueen.place(x=nx,y=ny)
        elif (x<(cx+67)and x>(cx-7)) and (y<(cy-416) and y>(cy-484)):
            nx=cx
            ny=cy-476
            Bwqueen.place(x=nx,y=ny)
        elif (x<(cx+67)and x>(cx-7)) and (y<(cy+128) and y>(cy+60)):
            nx=cx
            ny=cy+68
            Bwqueen.place(x=nx,y=ny)
        elif (x<(cx+67)and x>(cx-7)) and (y<(cy+196) and y>(cy+128)):
            nx=cx
            ny=cy+136
            Bwqueen.place(x=nx,y=ny)
        elif (x<(cx+67)and x>(cx-7)) and (y<(cy+264) and y>(cy+196)):
            nx=cx
            ny=cy+204
            Bwqueen.place(x=nx,y=ny)
        elif (x<(cx+67)and x>(cx-7)) and (y<(cy+332) and y>(cy+264)):
            nx=cx
            ny=cy+272
            Bwqueen.place(x=nx,y=ny)
        elif (x<(cx+67)and x>(cx-7)) and (y<(cy+400) and y>(cy+332)):
            nx=cx
            ny=cy+340
            Bwqueen.place(x=nx,y=ny)
        elif (x<(cx+67)and x>(cx-7)) and (y<(cy+468) and y>(cy+400)):
            nx=cx
            ny=cy+408
            Bwqueen.place(x=nx,y=ny)
        elif (x<(cx+67)and x>(cx-7)) and (y<(cy+536) and y>(cy+468)):
            nx=cx
            ny=cy+476
            Bwqueen.place(x=nx,y=ny)
        elif (x<(cx+141)and x>(cx+67)) and (y<(cy+60) and y>(cy-8)):
            nx=cx+75
            ny=cy
            Bwqueen.place(x=nx,y=ny)
        elif (x<(cx+215)and x>(cx+141)) and (y<(cy+60) and y>(cy-8)):
            nx=cx+150
            ny=cy
            Bwqueen.place(x=nx,y=ny)
        elif (x<(cx+289)and x>(cx+215)) and (y<(cy+60) and y>(cy-8)):
            nx=cx+225
            ny=cy
            Bwqueen.place(x=nx,y=ny)
        elif (x<(cx+363)and x>(cx+289)) and (y<(cy+60) and y>(cy-8)):
            nx=cx+300
            ny=cy
            Bwqueen.place(x=nx,y=ny)
        elif (x<(cx+437)and x>(cx+363)) and (y<(cy+60) and y>(cy-8)):
            nx=cx+375
            ny=cy
            Bwqueen.place(x=nx,y=ny)
        elif (x<(cx+511)and x>(cx+437)) and (y<(cy+60) and y>(cy-8)):
            nx=cx+450
            ny=cy
            Bwqueen.place(x=nx,y=ny)
        elif (x<(cx+585)and x>(cx+511)) and (y<(cy+60) and y>(cy-8)):
            nx=cx+526
            ny=cy
            Bwqueen.place(x=nx,y=ny)
        elif (x<(cx-13)and x>(cx-87)) and (y<(cy+60) and y>(cy-8)):
            nx=cx-75
            ny=cy
            Bwqueen.place(x=nx,y=ny)
        elif (x<(cx-87)and x>(cx-161)) and (y<(cy+60) and y>(cy-8)):
            nx=cx-150
            ny=cy
            Bwqueen.place(x=nx,y=ny)
        elif (x<(cx-161)and x>(cx-235)) and (y<(cy+60) and y>(cy-8)):
            nx=cx-225
            ny=cy
            Bwqueen.place(x=nx,y=ny)
        elif (x<(cx-235)and x>(cx-309)) and (y<(cy+60) and y>(cy-8)):
            nx=cx-300
            ny=cy
            Bwqueen.place(x=nx,y=ny)
        elif (x<(cx-309)and x>(cx-383)) and (y<(cy+60) and y>(cy-8)):
            nx=cx-375
            ny=cy
            Bwqueen.place(x=nx,y=ny)
        elif (x<(cx-383)and x>(cx-457)) and (y<(cy+60) and y>(cy-8)):
            nx=cx-450
            ny=cy
            Bwqueen.place(x=nx,y=ny)
        elif (x<(cx-457)and x>(cx-531)) and (y<(cy+60) and y>(cy-8)):
            nx=cx-526
            ny=cy
            Bwqueen.place(x=nx,y=ny)
        xi=1
        try:
            Peices_info(WP1=crd(Wbpawn.winfo_x(),Wbpawn.winfo_y()),WP2=crd(Wbpawn1.winfo_x(),Wbpawn1.winfo_y()),WP3=crd(Wbpawn2.winfo_x(),Wbpawn2.winfo_y()),WP4=crd(Wbpawn3.winfo_x(),Wbpawn3.winfo_y()),WP5=crd(Wbpawn4.winfo_x(),Wbpawn4.winfo_y()),WP6=crd(Wbpawn5.winfo_x(),Wbpawn5.winfo_y()),WP7=crd(Wbpawn6.winfo_x(),Wbpawn6.winfo_y()),WP8=crd(Wbpawn7.winfo_x(),Wbpawn7.winfo_y()),BP1=crd(Bbpawn.winfo_x(),Bbpawn.winfo_y()),BP2=crd(Bbpawn2.winfo_x(),Bbpawn2.winfo_y()),BP3=crd(Bbpawn3.winfo_x(),Bbpawn3.winfo_y()),BP4=crd(Bbpawn4.winfo_x(),Bbpawn4.winfo_y()),BP5=crd(Bbpawn5.winfo_x(),Bbpawn5.winfo_y()),BP6=crd(Bbpawn6.winfo_x(),Bbpawn6.winfo_y()),BP7=crd(Bbpawn7.winfo_x(),Bbpawn7.winfo_y()),BP8=crd(Bbpawn8.winfo_x(),Bbpawn8.winfo_y()),BR1=crd(Bbrook.winfo_x(),Bbrook.winfo_y()),BR2=crd(Bbrook1.winfo_x(),Bbrook1.winfo_y()),BBI1=crd(Bbbish.winfo_x(),Bbbish.winfo_y()),BBI2=crd(Bbbish1.winfo_x(),Bbbish1.winfo_y()),BN1=crd(Bbnit.winfo_x(),Bbnit.winfo_y()),BN2=crd(Bbnit1.winfo_x(),Bbnit1.winfo_y()),BK=crd(Bbking.winfo_x(),Bbking.winfo_y()),BQ=crd(Bbqueen.winfo_x(),Bbqueen.winfo_y()),WR1=crd(Bwrook.winfo_x(),Bwrook.winfo_y()),WR2=crd(Bwrook1.winfo_x(),Bwrook1.winfo_y()),WBI1=crd(Bwbish.winfo_x(),Bwbish.winfo_y()),WBI2=crd(Bwbish1.winfo_x(),Bwbish1.winfo_y()),WN1=crd(Bwnit.winfo_x(),Bwnit.winfo_y()),WN2=crd(Bwnit1.winfo_x(),Bwnit1.winfo_y()),WK=crd(Bwking.winfo_x(),Bwking.winfo_y()),WQ=crd(nx,ny))
            terminator(Bwqueen)
            sw.unbind("<Button-1>")
        except:
            print("Click on the button not on the box")
            xi=2
        if xi==2:
            pass
        else:
            changer(1)
    sw.bind("<Button-1>",mover2)

def draggerBbqueen():
     global cx
     global cy
     cx=Bbqueen.winfo_x() 
     cy=Bbqueen.winfo_y()

def moverBbqueen():
    global sw
    global cx
    global cy
    def mover2(event):
        global n
        global Bbqueen
        x=event.x
        y=event.y
        if (x<(cx+141)and x>(cx+67)) and (y<(cy-8) and y>(cy-76)):
            nx=cx+75
            ny=cy-68
            Bbqueen.place(x=nx,y=ny)
        elif (x<(cx+215)and x>(cx+141)) and (y<(cy-76) and y>(cy-144)):
            nx=cx+150
            ny=cy-136
            Bbqueen.place(x=nx,y=ny)
        elif (x<(cx+289)and x>(cx+215)) and (y<(cy-144) and y>(cy-212)):
            nx=cx+225
            ny=cy-204
            Bbqueen.place(x=nx,y=ny)
        elif (x<(cx+363)and x>(cx+289)) and (y<(cy-212) and y>(cy-280)):
            nx=cx+300
            ny=cy-272
            Bbqueen.place(x=nx,y=ny)
        elif (x<(cx+437)and x>(cx+363)) and (y<(cy-280) and y>(cy-348)):
            nx=cx+375
            ny=cy-340
            Bbqueen.place(x=nx,y=ny)
        elif (x<(cx+511)and x>(cx+437)) and (y<(cy-348) and y>(cy-416)):
            nx=cx+450
            ny=cy-408
            Bbqueen.place(x=nx,y=ny)
        elif (x<(cx+585)and x>(cx+511)) and (y<(cy-416) and y>(cy-484)):
            nx=cx+526
            ny=cy-476
            Bbqueen.place(x=nx,y=ny)
        elif (x<(cx+141)and x>(cx+67)) and (y<(cy+128) and y>(cy+60)):
            nx=cx+75
            ny=cy+68
            Bbqueen.place(x=nx,y=ny)
        elif (x<(cx+215)and x>(cx+141)) and (y<(cy+196) and y>(cy+128)):
            nx=cx+150
            ny=cy+136
            Bbqueen.place(x=nx,y=ny)
        elif (x<(cx+289)and x>(cx+215)) and (y<(cy+264) and y>(cy+196)):
            nx=cx+225
            ny=cy+204
            Bbqueen.place(x=nx,y=ny)
        elif (x<(cx+363)and x>(cx+289)) and (y<(cy+332) and y>(cy+264)):
            nx=cx+300
            ny=cy+272
            Bbqueen.place(x=nx,y=ny)
        elif (x<(cx+437)and x>(cx+363)) and (y<(cy+400) and y>(cy+332)):
            nx=cx+375
            ny=cy+340
            Bbqueen.place(x=nx,y=ny)
        elif (x<(cx+511)and x>(cx+437)) and (y<(cy+468) and y>(cy+400)):
            nx=cx+450
            ny=cy+408
            Bbqueen.place(x=nx,y=ny)
        elif (x<(cx+585)and x>(cx+511)) and (y<(cy+536) and y>(cy+468)):
            nx=cx+526
            ny=cy+476
            Bbqueen.place(x=nx,y=ny)
        elif (x<(cx-13)and x>(cx-87)) and (y<(cy-8) and y>(cy-76)):
            nx=cx-75
            ny=cy-68
            Bbqueen.place(x=nx,y=ny)
        elif (x<(cx-87)and x>(cx-161)) and (y<(cy-76) and y>(cy-144)):
            nx=cx-150
            ny=cy-136
            Bbqueen.place(x=nx,y=ny)
        elif (x<(cx-161)and x>(cx-235)) and (y<(cy-144) and y>(cy-212)):
            nx=cx-225
            ny=cy-204
            Bbqueen.place(x=nx,y=ny)
        elif (x<(cx-235)and x>(cx-309)) and (y<(cy-212) and y>(cy-280)):
            nx=cx-300
            ny=cy-272
            Bbqueen.place(x=nx,y=ny)
        elif (x<(cx-309)and x>(cx-383)) and (y<(cy-280) and y>(cy-348)):
            nx=cx-375
            ny=cy-340
            Bbqueen.place(x=nx,y=ny)
        elif (x<(cx-383)and x>(cx-457)) and (y<(cy-348) and y>(cy-416)):
            nx=cx-450
            ny=cy-408
            Bbqueen.place(x=nx,y=ny)
        elif (x<(cx-457)and x>(cx+531)) and (y<(cy-416) and y>(cy-484)):
            nx=cx-526
            ny=cy-476
            Bbqueen.place(x=nx,y=ny)
        elif (x<(cx-13)and x>(cx-87)) and (y<(cy+128) and y>(cy+60)):
            nx=cx-75
            ny=cy+68
            Bbqueen.place(x=nx,y=ny)
        elif (x<(cx-87)and x>(cx-161)) and (y<(cy+196) and y>(cy+128)):
            nx=cx-150
            ny=cy+136
            Bbqueen.place(x=nx,y=ny)
        elif (x<(cx-161)and x>(cx-235)) and (y<(cy+264) and y>(cy+196)):
            nx=cx-225
            ny=cy+204
            Bbqueen.place(x=nx,y=ny)
        elif (x<(cx-235)and x>(cx-309)) and (y<(cy+332) and y>(cy+264)):
            nx=cx-300
            ny=cy+272
            Bbqueen.place(x=nx,y=ny)
        elif (x<(cx-309)and x>(cx-383)) and (y<(cy+400) and y>(cy+332)):
            nx=cx-375
            ny=cy+340
            Bbqueen.place(x=nx,y=ny)
        elif (x<(cx-383)and x>(cx-457)) and (y<(cy+468) and y>(cy+400)):
            nx=cx-450
            ny=cy+408
            Bbqueen.place(x=nx,y=ny)
        elif (x<(cx-457)and x>(cx+531)) and (y<(cy+536) and y>(cy+468)):
            nx=cx-526
            ny=cy+476
            Bbqueen.place(x=nx,y=ny)
        elif (x<(cx+67)and x>(cx-7)) and (y<(cy-8) and y>(cy-76)):
            nx=cx
            ny=cy-68
            Bbqueen.place(x=nx,y=ny)
        elif (x<(cx+67)and x>(cx-7)) and (y<(cy-76) and y>(cy-144)):
            nx=cx
            ny=cy-136
            Bbqueen.place(x=nx,y=ny)
        elif (x<(cx+67)and x>(cx-7)) and (y<(cy-144) and y>(cy-212)):
            nx=cx
            ny=cy-204
            Bbqueen.place(x=nx,y=ny)
        elif (x<(cx+67)and x>(cx-7)) and (y<(cy-212) and y>(cy-280)):
            nx=cx
            ny=cy-272
            Bbqueen.place(x=nx,y=ny)
        elif (x<(cx+67)and x>(cx-7)) and (y<(cy-280) and y>(cy-348)):
            nx=cx
            ny=cy-340
            Bbqueen.place(x=nx,y=ny)
        elif (x<(cx+67)and x>(cx-7)) and (y<(cy-348) and y>(cy-416)):
            nx=cx
            ny=cy-408
            Bbqueen.place(x=nx,y=ny)
        elif (x<(cx+67)and x>(cx-7)) and (y<(cy-416) and y>(cy-484)):
            nx=cx
            ny=cy-476
            Bbqueen.place(x=nx,y=ny)
        elif (x<(cx+67)and x>(cx-7)) and (y<(cy+128) and y>(cy+60)):
            nx=cx
            ny=cy+68
            Bbqueen.place(x=nx,y=ny)
        elif (x<(cx+67)and x>(cx-7)) and (y<(cy+196) and y>(cy+128)):
            nx=cx
            ny=cy+136
            Bbqueen.place(x=nx,y=ny)
        elif (x<(cx+67)and x>(cx-7)) and (y<(cy+264) and y>(cy+196)):
            nx=cx
            ny=cy+204
            Bbqueen.place(x=nx,y=ny)
        elif (x<(cx+67)and x>(cx-7)) and (y<(cy+332) and y>(cy+264)):
            nx=cx
            ny=cy+272
            Bbqueen.place(x=nx,y=ny)
        elif (x<(cx+67)and x>(cx-7)) and (y<(cy+400) and y>(cy+332)):
            nx=cx
            ny=cy+340
            Bbqueen.place(x=nx,y=ny)
        elif (x<(cx+67)and x>(cx-7)) and (y<(cy+468) and y>(cy+400)):
            nx=cx
            ny=cy+408
            Bbqueen.place(x=nx,y=ny)
        elif (x<(cx+67)and x>(cx-7)) and (y<(cy+536) and y>(cy+468)):
            nx=cx
            ny=cy+476
            Bbqueen.place(x=nx,y=ny)
        elif (x<(cx+141)and x>(cx+67)) and (y<(cy+60) and y>(cy-8)):
            nx=cx+75
            ny=cy
            Bbqueen.place(x=nx,y=ny)
        elif (x<(cx+215)and x>(cx+141)) and (y<(cy+60) and y>(cy-8)):
            nx=cx+150
            ny=cy
            Bbqueen.place(x=nx,y=ny)
        elif (x<(cx+289)and x>(cx+215)) and (y<(cy+60) and y>(cy-8)):
            nx=cx+225
            ny=cy
            Bbqueen.place(x=nx,y=ny)
        elif (x<(cx+363)and x>(cx+289)) and (y<(cy+60) and y>(cy-8)):
            nx=cx+300
            ny=cy
            Bbqueen.place(x=nx,y=ny)
        elif (x<(cx+437)and x>(cx+363)) and (y<(cy+60) and y>(cy-8)):
            nx=cx+375
            ny=cy
            Bbqueen.place(x=nx,y=ny)
        elif (x<(cx+511)and x>(cx+437)) and (y<(cy+60) and y>(cy-8)):
            nx=cx+450
            ny=cy
            Bbqueen.place(x=nx,y=ny)
        elif (x<(cx+585)and x>(cx+511)) and (y<(cy+60) and y>(cy-8)):
            nx=cx+526
            ny=cy
            Bbqueen.place(x=nx,y=ny)
        elif (x<(cx-13)and x>(cx-87)) and (y<(cy+60) and y>(cy-8)):
            nx=cx-75
            ny=cy
            Bbqueen.place(x=nx,y=ny)
        elif (x<(cx-87)and x>(cx-161)) and (y<(cy+60) and y>(cy-8)):
            nx=cx-150
            ny=cy
            Bbqueen.place(x=nx,y=ny)
        elif (x<(cx-161)and x>(cx-235)) and (y<(cy+60) and y>(cy-8)):
            nx=cx-225
            ny=cy
            Bbqueen.place(x=nx,y=ny)
        elif (x<(cx-235)and x>(cx-309)) and (y<(cy+60) and y>(cy-8)):
            nx=cx-300
            ny=cy
            Bbqueen.place(x=nx,y=ny)
        elif (x<(cx-309)and x>(cx-383)) and (y<(cy+60) and y>(cy-8)):
            nx=cx-375
            ny=cy
            Bbqueen.place(x=nx,y=ny)
        elif (x<(cx-383)and x>(cx-457)) and (y<(cy+60) and y>(cy-8)):
            nx=cx-450
            ny=cy
            Bbqueen.place(x=nx,y=ny)
        elif (x<(cx-457)and x>(cx-531)) and (y<(cy+60) and y>(cy-8)):
            nx=cx-526
            ny=cy
            Bbqueen.place(x=nx,y=ny)
        print(nx,"  ",ny)
        xi=1
        try:
            Peices_info(WP1=crd(Wbpawn.winfo_x(),Wbpawn.winfo_y()),WP2=crd(Wbpawn1.winfo_x(),Wbpawn1.winfo_y()),WP3=crd(Wbpawn2.winfo_x(),Wbpawn2.winfo_y()),WP4=crd(Wbpawn3.winfo_x(),Wbpawn3.winfo_y()),WP5=crd(Wbpawn4.winfo_x(),Wbpawn4.winfo_y()),WP6=crd(Wbpawn5.winfo_x(),Wbpawn5.winfo_y()),WP7=crd(Wbpawn6.winfo_x(),Wbpawn6.winfo_y()),WP8=crd(Wbpawn7.winfo_x(),Wbpawn7.winfo_y()),BP1=crd(Bbpawn.winfo_x(),Bbpawn.winfo_y()),BP2=crd(Bbpawn2.winfo_x(),Bbpawn2.winfo_y()),BP3=crd(Bbpawn3.winfo_x(),Bbpawn3.winfo_y()),BP4=crd(Bbpawn4.winfo_x(),Bbpawn4.winfo_y()),BP5=crd(Bbpawn5.winfo_x(),Bbpawn5.winfo_y()),BP6=crd(Bbpawn6.winfo_x(),Bbpawn6.winfo_y()),BP7=crd(Bbpawn7.winfo_x(),Bbpawn7.winfo_y()),BP8=crd(Bbpawn8.winfo_x(),Bbpawn8.winfo_y()),BR1=crd(Bbrook.winfo_x(),Bbrook.winfo_y()),BR2=crd(Bbrook1.winfo_x(),Bbrook1.winfo_y()),BBI1=crd(Bbbish.winfo_x(),Bbbish.winfo_y()),BBI2=crd(Bbbish1.winfo_x(),Bbbish1.winfo_y()),BN1=crd(Bbnit.winfo_x(),Bbnit.winfo_y()),BN2=crd(Bbnit1.winfo_x(),Bbnit1.winfo_y()),BK=crd(Bbking.winfo_x(),Bbking.winfo_y()),BQ=crd(nx,ny),WR1=crd(Bwrook.winfo_x(),Bwrook.winfo_y()),WR2=crd(Bwrook1.winfo_x(),Bwrook1.winfo_y()),WBI1=crd(Bwbish.winfo_x(),Bwbish.winfo_y()),WBI2=crd(Bwbish1.winfo_x(),Bwbish1.winfo_y()),WN1=crd(Bwnit.winfo_x(),Bwnit.winfo_y()),WN2=crd(Bwnit1.winfo_x(),Bwnit1.winfo_y()),WK=crd(Bwking.winfo_x(),Bwking.winfo_y()),WQ=crd(Bwqueen.winfo_x(),Bwqueen.winfo_y()))
            terminator(Bbqueen)
            sw.unbind("<Button-1>")
        except:
            print("Click in the box not on the button")
            xi=2
        if xi==2:
            pass
        else:
            changer(2)
    sw.bind("<Button-1>",mover2)

def draggerBwking():
     global cx
     global cy
     cx=Bwking.winfo_x() 
     cy=Bwking.winfo_y()

def moverBwking():
    global sw
    global cx
    global cy
    def mover2(event):
        global n
        global Bwking
        x=event.x
        y=event.y
        if (x<(cx+141)and x>(cx+67)) and (y<(cy-8) and y>(cy-76)):
            nx=cx+75
            ny=cy-68
            Bwking.place(x=nx,y=ny)
        
        
        elif (x<(cx+141)and x>(cx+67)) and (y<(cy+128) and y>(cy+60)):
            nx=cx+75
            ny=cy+68
            Bwking.place(x=nx,y=ny)
        
        elif (x<(cx-13)and x>(cx-87)) and (y<(cy-8) and y>(cy-76)):
            nx=cx-75
            ny=cy-68
            Bwking.place(x=nx,y=ny)
        
        elif (x<(cx-13)and x>(cx-87)) and (y<(cy+128) and y>(cy+60)):
            nx=cx-75
            ny=cy+68
            Bwking.place(x=nx,y=ny)
        
        elif (x<(cx+67)and x>(cx-7)) and (y<(cy-8) and y>(cy-76)):
            nx=cx
            ny=cy-68
            Bwking.place(x=nx,y=ny)
        
        elif (x<(cx+67)and x>(cx-7)) and (y<(cy+128) and y>(cy+60)):
            nx=cx
            ny=cy+68
            Bwking.place(x=nx,y=ny)
        
        elif (x<(cx+141)and x>(cx+67)) and (y<(cy+60) and y>(cy-8)):
            nx=cx+75
            ny=cy
            Bwking.place(x=nx,y=ny)
        
        elif (x<(cx-13)and x>(cx-87)) and (y<(cy+60) and y>(cy-8)):
            nx=cx-75
            ny=cy
            Bwking.place(x=nx,y=ny)
        
        print(nx,"  ",ny)
        xi=1
        try:
            Peices_info(WP1=crd(Wbpawn.winfo_x(),Wbpawn.winfo_y()),WP2=crd(Wbpawn1.winfo_x(),Wbpawn1.winfo_y()),WP3=crd(Wbpawn2.winfo_x(),Wbpawn2.winfo_y()),WP4=crd(Wbpawn3.winfo_x(),Wbpawn3.winfo_y()),WP5=crd(Wbpawn4.winfo_x(),Wbpawn4.winfo_y()),WP6=crd(Wbpawn5.winfo_x(),Wbpawn5.winfo_y()),WP7=crd(Wbpawn6.winfo_x(),Wbpawn6.winfo_y()),WP8=crd(Wbpawn7.winfo_x(),Wbpawn7.winfo_y()),BP1=crd(Bbpawn.winfo_x(),Bbpawn.winfo_y()),BP2=crd(Bbpawn2.winfo_x(),Bbpawn2.winfo_y()),BP3=crd(Bbpawn3.winfo_x(),Bbpawn3.winfo_y()),BP4=crd(Bbpawn4.winfo_x(),Bbpawn4.winfo_y()),BP5=crd(Bbpawn5.winfo_x(),Bbpawn5.winfo_y()),BP6=crd(Bbpawn6.winfo_x(),Bbpawn6.winfo_y()),BP7=crd(Bbpawn7.winfo_x(),Bbpawn7.winfo_y()),BP8=crd(Bbpawn8.winfo_x(),Bbpawn8.winfo_y()),BR1=crd(Bbrook.winfo_x(),Bbrook.winfo_y()),BR2=crd(Bbrook1.winfo_x(),Bbrook1.winfo_y()),BBI1=crd(Bbbish.winfo_x(),Bbbish.winfo_y()),BBI2=crd(Bbbish1.winfo_x(),Bbbish1.winfo_y()),BN1=crd(Bbnit.winfo_x(),Bbnit.winfo_y()),BN2=crd(Bbnit1.winfo_x(),Bbnit1.winfo_y()),BK=crd(Bbking.winfo_x(),Bbking.winfo_y()),BQ=crd(Bbqueen.winfo_x(),Bbqueen.winfo_y()),WR1=crd(Bwrook.winfo_x(),Bwrook.winfo_y()),WR2=crd(Bwrook1.winfo_x(),Bwrook1.winfo_y()),WBI1=crd(Bwbish.winfo_x(),Bwbish.winfo_y()),WBI2=crd(Bwbish1.winfo_x(),Bwbish1.winfo_y()),WN1=crd(Bwnit.winfo_x(),Bwnit.winfo_y()),WN2=crd(Bwnit1.winfo_x(),Bwnit1.winfo_y()),WK=crd(nx,ny),WQ=crd(Bwqueen.winfo_x(),Bwqueen.winfo_y()))
            terminator(Bwking)
            sw.unbind("<Button-1>")
        except:
            print("Click in the box not on the button")
            xi=2
        if xi==2:
            pass
        else:
            changer(1)
        
    sw.bind("<Button-1>",mover2)

def draggerBbking():
     global cx
     global cy
     cx=Bbking.winfo_x() 
     cy=Bbking.winfo_y()

def moverBbking():
    global sw
    global cx
    global cy
    def mover2(event):
        global n
        global Bbking
        x=event.x
        y=event.y
        if (x<(cx+141)and x>(cx+67)) and (y<(cy-8) and y>(cy-76)):
            nx=cx+75
            ny=cy-68
            Bbking.place(x=nx,y=ny)
        
        
        elif (x<(cx+141)and x>(cx+67)) and (y<(cy+128) and y>(cy+60)):
            nx=cx+75
            ny=cy+68
            Bbking.place(x=nx,y=ny)
        
        elif (x<(cx-13)and x>(cx-87)) and (y<(cy-8) and y>(cy-76)):
            nx=cx-75
            ny=cy-68
            Bbking.place(x=nx,y=ny)
        
        elif (x<(cx-13)and x>(cx-87)) and (y<(cy+128) and y>(cy+60)):
            nx=cx-75
            ny=cy+68
            Bbking.place(x=nx,y=ny)
        
        elif (x<(cx+67)and x>(cx-7)) and (y<(cy-8) and y>(cy-76)):
            nx=cx
            ny=cy-68
            Bbking.place(x=nx,y=ny)
        
        elif (x<(cx+67)and x>(cx-7)) and (y<(cy+128) and y>(cy+60)):
            nx=cx
            ny=cy+68
            Bbking.place(x=nx,y=ny)
        
        elif (x<(cx+141)and x>(cx+67)) and (y<(cy+60) and y>(cy-8)):
            nx=cx+75
            ny=cy
            Bbking.place(x=nx,y=ny)
        
        elif (x<(cx-13)and x>(cx-87)) and (y<(cy+60) and y>(cy-8)):
            nx=cx-75
            ny=cy
            Bbking.place(x=nx,y=ny)
        
        print(nx,"  ",ny)
        xi=1
        try:
            Peices_info(WP1=crd(Wbpawn.winfo_x(),Wbpawn.winfo_y()),WP2=crd(Wbpawn1.winfo_x(),Wbpawn1.winfo_y()),WP3=crd(Wbpawn2.winfo_x(),Wbpawn2.winfo_y()),WP4=crd(Wbpawn3.winfo_x(),Wbpawn3.winfo_y()),WP5=crd(Wbpawn4.winfo_x(),Wbpawn4.winfo_y()),WP6=crd(Wbpawn5.winfo_x(),Wbpawn5.winfo_y()),WP7=crd(Wbpawn6.winfo_x(),Wbpawn6.winfo_y()),WP8=crd(Wbpawn7.winfo_x(),Wbpawn7.winfo_y()),BP1=crd(Bbpawn.winfo_x(),Bbpawn.winfo_y()),BP2=crd(Bbpawn2.winfo_x(),Bbpawn2.winfo_y()),BP3=crd(Bbpawn3.winfo_x(),Bbpawn3.winfo_y()),BP4=crd(Bbpawn4.winfo_x(),Bbpawn4.winfo_y()),BP5=crd(Bbpawn5.winfo_x(),Bbpawn5.winfo_y()),BP6=crd(Bbpawn6.winfo_x(),Bbpawn6.winfo_y()),BP7=crd(Bbpawn7.winfo_x(),Bbpawn7.winfo_y()),BP8=crd(Bbpawn8.winfo_x(),Bbpawn8.winfo_y()),BR1=crd(Bbrook.winfo_x(),Bbrook.winfo_y()),BR2=crd(Bbrook1.winfo_x(),Bbrook1.winfo_y()),BBI1=crd(Bbbish.winfo_x(),Bbbish.winfo_y()),BBI2=crd(Bbbish1.winfo_x(),Bbbish1.winfo_y()),BN1=crd(Bbnit.winfo_x(),Bbnit.winfo_y()),BN2=crd(Bbnit1.winfo_x(),Bbnit1.winfo_y()),BK=crd(nx,ny),BQ=crd(Bbqueen.winfo_x(),Bbqueen.winfo_y()),WR1=crd(Bwrook.winfo_x(),Bwrook.winfo_y()),WR2=crd(Bwrook1.winfo_x(),Bwrook1.winfo_y()),WBI1=crd(Bwbish.winfo_x(),Bwbish.winfo_y()),WBI2=crd(Bwbish1.winfo_x(),Bwbish1.winfo_y()),WN1=crd(Bwnit.winfo_x(),Bwnit.winfo_y()),WN2=crd(Bwnit1.winfo_x(),Bwnit1.winfo_y()),WK=crd(Bwking.winfo_x(),Bwking.winfo_y()),WQ=crd(Bwqueen.winfo_x(),Bwqueen.winfo_y()))
            terminator(Bbking)
            sw.unbind("<Button-1>")
        except:
            print("Click in the box not on the button")
            xi=2
        if xi==2:
            pass
        else:
            changer(2)
    sw.bind("<Button-1>",mover2)

def positioner(event):
    x=event.x
    y=event.y
    print(x,' it ',y)
def main():
    global win
    global c
    global b
    global b1
    win=Tk()
    win.title('CHESS')
    win.geometry("1920x1080")
    win.iconbitmap("chess icon.ico")
    c=Canvas(win, height=1080,width=1920,bg='black')
    img=(Image.open("bggg.jpg"))
    rimg=img.resize((1600,900),Image.ANTIALIAS)
    nimg= ImageTk.PhotoImage(rimg)
    c.create_image(0,0,anchor=NW,image=nimg,tag='cover')
    mf=font.Font(size=20,weight='bold')
    b=Button(win,text='Start Game',command=start,font=mf,bg='black',fg='white',activebackground='green',bd=10,padx=40,pady=10)
    b.place(x=669,y=550)
# =============================================================================
#     b.bind("<Button-1>",dragger)
#     b.bind("<B1-Motion>",mover)
# =============================================================================
    b1=Button(win, text='Load game',command=load,font=mf,bg='black',fg='white',activebackground='green',bd=10,padx=38,pady=10)
    b1.place(x=669,y=650)
# =============================================================================
#     b1.bind("<Button-1>",dragger)
#     b1.bind("<B1-Motion>",mover)
# =============================================================================
    c.pack()
    win.attributes("-fullscreen",True)
    win.mainloop()

main()