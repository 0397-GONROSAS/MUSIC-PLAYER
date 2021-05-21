from tkinter import *
from tkinter import filedialog
from pygame import mixer
from tkinter import messagebox

import random

#Creando pantalla principal y asignando dimensiones
main=Tk()
main.resizable(False,False)
main.geometry('810x510')
main.title("Reproductor de musica")
#Imagenes para boton
playb=PhotoImage(file='play.gif')
playb=playb.subsample(5)

pauseb=PhotoImage(file="pause.gif")
pauseb=pauseb.subsample(19)

ranb=PhotoImage(file="shuffle.gif")
ranb=ranb.subsample(12)

bucleb=PhotoImage(file="loop.gif")
bucleb=bucleb.subsample(6)

netxb=PhotoImage(file="next.gif")
netxb=netxb.subsample(6)

prevb=PhotoImage(file="prev.gif")
prevb=prevb.subsample(11)

#Imagenes para reproducir
imagen1=PhotoImage(file="blind and frozen.gif")
imagen1=imagen1.subsample(5)

imagen2=PhotoImage(file="Carusso.gif")
imagen2=imagen2.subsample(2)  

imagen3=PhotoImage(file="Durch alle gezeiten.gif")
imagen3=imagen3.subsample(2)

imagen4=PhotoImage(file="From Hell.gif")
imagen4=imagen4.subsample(5)

imagen5=PhotoImage(file="Hallelujah.gif")
imagen5=imagen5.zoom(1)

imagen6=PhotoImage(file="Heart of glass.gif")
imagen6=imagen6.subsample(3)

imagen7=PhotoImage(file="I just called.gif")
imagen7=imagen7.zoom(1)

imagen8=PhotoImage(file="Isabel.gif")
imagen8=imagen8.zoom(1)

imagen9=PhotoImage(file="Metal machine.gif")
imagen9=imagen9.subsample(4)
#Variables globales
global archivo2,nc,state,loop,shuffle,archivo,reproducidas
nc=0
state=0
loop=0
shuffle=0
archivo2=[]
reproducidas=[]
archivo=""

#Funciones

#Boton Play
def play():
	global archivo,nc,state
	if len(archivo)==0:
		vacio()
		importc()

	else:
		mixer.init()
		mixer.music.load(archivo[nc])
		mixer.music.set_volume(0.7)
		if state==True:
			mixer.music.pause()
			state=0
		else:
			state=1
			mixer.music.play()

#Función de Advertencia
def vacio():
	messagebox.showinfo("Reproductor","Biblioteca vacia, por favor importe una carpeta")

#Funcion para reproducir cancion
def actual(x):
	mixer.init()
	mixer.music.load(archivo[nc])
	mixer.music.set_volume(0.7)
	mixer.music.play()
	repro()

#Boton Next song
def nsong():
	global nc,loop, shuffle
	if loop==True:
		nc=nc
	elif shuffle==True:
		nc=random.randint(0,len(archivo))
	else:
		nc+=1
	
	if nc>len(archivo):
		nc=0
	actual(nc)


	
#Boton Prev song
def psong():
	global nc, loop, shuffle
	if loop==True:
		nc=nc
	else:
		nc-=1
	if nc<0:
		nc=0
	actual(nc)

#Boton Shuffle
def shuffle():
	global shuffle,loop
	loop=False
	if shuffle==True:
		shuffle=False
	else:
		shuffle=True

#Boton Loop
def loop():
	global loop,shuffle
	shuffle=False
	if loop==True:
		loop=False
	else:
		loop=True



#Boton Biblioteca
def biblioteca():
	global archivo2
	frame4=Frame(frame1,width=600,height=400,background="gray17")
	frame4.grid(row=0,column=1,ipadx=0,ipady=0)
	label=Label(frame4,text="Tu música",bg="gray17",fg="white",font=(30))
	label.place(anchor="nw")

	#Añadiendo ListBox
	myBib=Listbox(frame4,bg="gray17",fg="white",width=80)
	myBib.place(x=50,y=40)
	myBib.insert(0,*archivo2)


#Boton Recientes
def recientes():
	frame4=Frame(frame1,width=600,height=400,background="gray17")
	frame4.grid(row=0,column=1,ipadx=0,ipady=0)
	label=Label(frame4,text="Escuchadas recientemente",bg="gray17",fg="white",font=(30))
	label.place(anchor="nw")

	#Añadiendo List Box
	global nc,archivo,reproducidas
	x=archivo[nc].replace("Music Folder path","")
	if x not in reproducidas:
		var=archivo[nc].replace("Music Folder path","")
		reproducidas.append(var)

	recent=Listbox(frame4,bg="gray17",fg="white",width=80)
	recent.place(x=50,y=40)
	recent.insert(0,*reproducidas)

#Boton Importar Canciones
def importc():
	global archivo2,archivo
	archivo=filedialog.askopenfilenames(title="Añadir a Biblioteca")
	for i in archivo:
		x=i.replace("musics folder path","")
		archivo2.append(x)
	repro()

#Boton reproducción Actual
def repro():
	global nc, archivo

	cancion=archivo[nc].replace("Music Folder path","")
	imagenes=(imagen1,imagen2,imagen3,imagen4,imagen5,imagen6,imagen7,imagen8,imagen9)
	frame4=Frame(frame1,width=600,height=400,background="gray17")
	frame4.grid(row=0,column=1,ipadx=0,ipady=0)
	label=Label(frame4,text="En reproducción",bg="gray17",fg="white",font=(30))
	label.place(anchor="nw")
	Label(frame4,image=imagenes[nc],bg="gray17").place(x=150,y=50)
	Label(frame4,text=cancion,bg="gray17",fg="white",font=(20)).place(x=200,y=360)

#Dividiendo main
frame1=Frame(main,width=800,height=400)
frame1.grid(row=0,column=0,ipadx=0,ipady=0)
frame2=Frame(main,width=800,height=100,background="gray18")
frame2.grid(row=1,column=0,ipadx=0,ipady=0)

#Dividiendo Frame 1
frame3=Frame(frame1,width=200,height=400,background="gray16")
frame3.grid(row=0,column=0,ipadx=0,ipady=0)
frame4=Frame(frame1,width=600,height=400,background="gray17")
frame4.grid(row=0,column=1,ipadx=0,ipady=0)

#Insertando componentes
#Frame 1
label1=Label(frame3,text="Tu Biblioteca ",bg="gray17",fg="white",font=("Arial Baltic",20))
label1.place(anchor="nw")


#Frame 2
#Botones de control
play=Button(frame2,image=playb,borderwidth=0,command=play)
play.place(x=400,y=20)


n_song=Button(frame2,image=netxb,borderwidth=0,command=nsong)
n_song.place(x=500,y=20)

p_song=Button(frame2,image=prevb,borderwidth=0,command=psong)
p_song.place(x=300,y=20)

Shuffle=Button(frame2,image=ranb,borderwidth=0,command=shuffle)
Shuffle.place(x=150,y=20)

Loop=Button(frame2,image=bucleb,borderwidth=0,command=loop)
Loop.place(x=650,y=20)


#Botones
Biblioteca=Button(frame3,text="Biblioteca",borderwidth=0,background="gray16",fg="white",font=(20),command=biblioteca)
Biblioteca.place(x=0,y=100)

Recientes=Button(frame3,text="Recientes",borderwidth=0,background="gray16",fg="white",font=(20),command=recientes)
Recientes.place(x=0,y=130)

importar=Button(frame3,text="Añadir a biblioteca",borderwidth=0,background="gray16",fg="white",font=(20),command=importc)
importar.place(x=0,y=50)

reproduciendo=Button(frame3,text="Escuchando",borderwidth=0,background="gray16",fg="white",font=(20),command=repro)
reproduciendo.place(x=0,y=160)



main.mainloop()


