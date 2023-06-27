from tkinter import *
from tkinter import ttk
import tkinter.messagebox

root=Tk()
style = ttk.Style()
root.title("Tic Tac Toe")
root.resizable(0,0)

player=1
font = ("timesnewroman 19 bold")
b=0
p1Score=0
p2Score=0
style.configure('TButton', foreground='#e0527d', backgroud="green", font=font)






def ButtonClick(id):
    global player,b,c,p1Score,p2Score

    #for player 1 turn
    if id==1 and bu1['text']==' ' and player==1:
        bu1['text']="X"
        player=2
        b+=1
    if id==2 and bu2['text']==' ' and player==1:
        bu2['text']="X"
        player=2
        b+=1
    if id==3 and bu3['text']==' ' and player==1:
        bu3['text']="X"
        player=2
        b+=1
    if id==4 and bu4['text']==' ' and player==1:
        bu4['text']="X"
        player=2
        b+=1
    if id==5 and bu5['text']==' ' and player==1:
        bu5['text']="X"
        player=2
        b+=1
    if id==6 and bu6['text']==' ' and player==1:
        bu6['text']="X"
        player=2
        b+=1
    if id==7 and bu7['text']==' ' and player==1:
        bu7['text']="X"
        player=2
        b+=1
    if id==8 and bu8['text']==' ' and player==1:
        bu8['text']="X"
        player=2
        b+=1
    if id==9 and bu9['text']==' ' and player==1:
        bu9['text']="X"
        player=2
        b+=1
    #for player 2 turn
    if id==1 and bu1['text']==' ' and player==2:
        bu1['text']="O"
        player=1
        b+=1
    if id==2 and bu2['text']==' ' and player==2:
        bu2['text']="O"
        player=1
        b+=1
    if id==3 and bu3['text']==' ' and player==2:
        bu3['text']="O"
        player=1
        b+=1
    if id==4 and bu4['text']==' ' and player==2:
        bu4['text']="O"
        player=1
        b+=1
    if id==5 and bu5['text']==' ' and player==2:
        bu5['text']="O"
        player=1
        b+=1
    if id==6 and bu6['text']==' ' and player==2:
        bu6['text']="O"
        player=1
        b+=1
    if id==7 and bu7['text']==' ' and player==2:
        bu7['text']="O"
        player=1
        b+=1
    if id==8 and bu8['text']==' ' and player==2:
        bu8['text']="O"
        player=1
        b+=1
    if id==9 and bu9['text']==' ' and player==2:
        bu9['text']="O"
        player=1
        b+=1
        
    #checking for winner   
    if( bu1['text']=='X' and bu2['text']=='X' and bu3['text']=='X' or
        bu4['text']=='X' and bu5['text']=='X' and bu6['text']=='X' or
        bu7['text']=='X' and bu8['text']=='X' and bu9['text']=='X' or
        bu1['text']=='X' and bu4['text']=='X' and bu7['text']=='X' or
        bu2['text']=='X' and bu5['text']=='X' and bu8['text']=='X' or
        bu3['text']=='X' and bu6['text']=='X' and bu9['text']=='X' or
        bu1['text']=='X' and bu5['text']=='X' and bu9['text']=='X' or
        bu3['text']=='X' and bu5['text']=='X' and bu7['text']=='X'):
            p1Score+=1
            disableButton()
            playerScore['text']=f"   Player 1 Score:{p1Score}\n   Player 2 Score:{p2Score}  "
            tkinter.messagebox.showinfo("Tic Tac Toe","Winner is player 1")
    elif( bu1['text']=='O' and bu2['text']=='O' and bu3['text']=='O' or
        bu4['text']=='O' and bu5['text']=='O' and bu6['text']=='O' or
        bu7['text']=='O' and bu8['text']=='O' and bu9['text']=='O' or
        bu1['text']=='O' and bu4['text']=='O' and bu7['text']=='O' or
        bu2['text']=='O' and bu5['text']=='O' and bu8['text']=='O' or
        bu3['text']=='O' and bu6['text']=='O' and bu9['text']=='O' or
        bu1['text']=='O' and bu5['text']=='O' and bu9['text']=='O' or
        bu3['text']=='O' and bu5['text']=='O' and bu7['text']=='O'):
            disableButton()
            p2Score+=1
            playerScore['text']=f"   Player 1 Score:{p1Score}\n   Player 2 Score:{p2Score}  "
            tkinter.messagebox.showinfo("Tic Tac Toe","Winner is player 2")
    elif b==9:
            disableButton()
            tkinter.messagebox.showinfo("Tic Tac Toe","Match is Draw.")

    if player==1:
        playerturn['text']="   Player 1 turn!   "
    elif player==2:
        playerturn['text']="   Player 2 turn!   "


def restartbutton():
    global a,b,c
    player=1
    b=0
    playerturn['text']="   Player 1 turn!   "
    bu1['text']=' '
    bu2['text']=' '
    bu3['text']=' '
    bu4['text']=' '
    bu5['text']=' '
    bu6['text']=' '
    bu7['text']=' '
    bu8['text']=' '
    bu9['text']=' '
    bu1.state(['!disabled'])
    bu2.state(['!disabled'])
    bu3.state(['!disabled'])
    bu4.state(['!disabled'])
    bu5.state(['!disabled'])
    bu6.state(['!disabled'])
    bu7.state(['!disabled'])
    bu8.state(['!disabled'])
    bu9.state(['!disabled'])
    
def disableButton():
    bu1.state(['disabled'])
    bu2.state(['disabled'])
    bu3.state(['disabled'])
    bu4.state(['disabled'])
    bu5.state(['disabled'])
    bu6.state(['disabled'])
    bu7.state(['disabled'])
    bu8.state(['disabled'])
    bu9.state(['disabled'])

def resetScore():
    global p1Score,p2Score
    restartbutton()
    p1Score = 0
    p2Score = 0
    playerScore['text']=f"   Player 1 Score:{p1Score}\n   Player 2 Score:{p2Score}  "
#add Buttons

mainHeading = Label(root,text="Tic Tac Toe", font=("timesnewroman", 40,"bold italic"))
mainHeading.grid(row=0,column=0,columnspan=5)

bu1=ttk.Button(root,text=' ',command=lambda: ButtonClick(1))
bu1.grid(row=1,column=0,ipadx=40,ipady=40)


bu2=ttk.Button(root,text=' ',command=lambda: ButtonClick(2))
bu2.grid(row=1,column=1,ipadx=40,ipady=40)


bu3=ttk.Button(root,text=' ',command=lambda: ButtonClick(3))
bu3.grid(row=1,column=2,ipadx=40,ipady=40)


bu4=ttk.Button(root,text=' ',command=lambda: ButtonClick(4))
bu4.grid(row=2,column=0,ipadx=40,ipady=40)


bu5=ttk.Button(root,text=' ',command=lambda: ButtonClick(5))
bu5.grid(row=2,column=1,ipadx=40,ipady=40)


bu6=ttk.Button(root,text=' ',command=lambda: ButtonClick(6))
bu6.grid(row=2,column=2,ipadx=40,ipady=40)


bu7=ttk.Button(root,text=' ',command=lambda: ButtonClick(7))
bu7.grid(row=3,column=0,ipadx=40,ipady=40)


bu8=ttk.Button(root,text=' ',command=lambda: ButtonClick(8))
bu8.grid(row=3,column=1,ipadx=40,ipady=40)


bu9=ttk.Button(root,text=' ',command=lambda: ButtonClick(9))
bu9.grid(row=3,column=2,ipadx=40,ipady=40)


playerturn=ttk.Label(root,text="   Player 1 turn!  ", font=font)
playerturn.grid(row=4,column=0,ipadx=20,ipady=20)

playerScore=ttk.Label(root,text=f"   Player 1 Score:{p1Score}\n   Player 2 Score:{p2Score}  ", font=font)
playerScore.grid(row=5,column=0,ipadx=20,ipady=20)

playerdetails=ttk.Label(root,text="    Player 1 is X\n    Player 2 is O", font=font)
playerdetails.grid(row=4,column=2,ipadx=40,ipady=40,rowspan=2)

res=ttk.Button(root,text='Restart',command=lambda: restartbutton())
res.grid(row=4,column=1,ipadx=20,ipady=20)

res=ttk.Button(root,text='Reset Score',command=lambda: resetScore())
res.grid(row=5,column=1,ipadx=20,ipady=20)


            
root.mainloop()

