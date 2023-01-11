from cProfile import label
from decimal import Rounded
from tkinter import *
from tkinter import messagebox
from turtle import color, title
from matplotlib.figure import Figure 
import tkinter.font as tkFont
from tkinter import Tk, Frame,Button
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends._backend_tk import  NavigationToolbar2Tk
import matplotlib.pyplot as plt 
import numpy as np
import  math as m
import  cmath as cm

ventana = Tk()
ventana.title("Calculadora 2.0")
ventana.minsize(width=1300,height=900)
ventana.resizable(width=False, height=False)
ventana.configure(bg='#AAA2A0')



#Variables Dom of time
Vmt=DoubleVar()
Vat=DoubleVar()
Imt=DoubleVar()
Iat=DoubleVar()
f=DoubleVar()


#Variables Dom of frecuency
Vm=DoubleVar()
Va=DoubleVar()
Im=DoubleVar()
Ia=DoubleVar()

Vme=DoubleVar()
Vae=DoubleVar()
Ime=DoubleVar()
Iae=DoubleVar()

Zm=DoubleVar()
Za=DoubleVar()

#Variables Dom of power
P = DoubleVar()
Q = DoubleVar()
S = DoubleVar()
fp = DoubleVar()
f = DoubleVar()

state = 0

def clearData():
        Vmt.set(0)
        Vat.set(0)
        Imt.set(0)
        Iat.set(0)
        f.set(0)

        Vm.set(0)
        Va.set(0)
        Vme.set(0)
        Vae.set(0)

        Im.set(0)
        Ia.set(0)
        Ime.set(0)
        Iae.set(0)

        Zm.set(0)
        Za.set(0)

        P.set(0)
        Q.set(0)
        S.set(0)
        fp.set(0)


def AppController():
        global state
        if (Vm.get()!=0 or Vme !=0):
          if(Im.get()!=0 or Ime!=0):
                caldomF()
          if Zm!=0:
                caldomF
        if (Im.get()!=0 or Ime !=0):
          if(Vm.get()!=0 or Vme!=0):
                caldomF()
          if Zm!=0:
                caldomF()
        
        elif P.get()!=0 and S.get()!=0:
               caldomP()
        elif P.get()!=0 and fp.get()!=0:
                 caldomP()
        elif S.get()!=0 and fp.get()!=0:
                caldomP() 
        elif Vmt.get()!=0 and Imt.get()!=0:
                if f.get()==0:
                       f.set(60)
                caldomT()
        else:
          messagebox.showerror("Error","Porfacor ingresa un valores en al menos un dominio")
        
        
                
##################################################################################################


#                                        CALCULOS                                                #


##################################################################################################


#                            CALCULO DOMINIO DEL TIEMPO                                                #


def caldomT():
   #Calculos de variables del dominio de la frecuencia  V, Vrms, I, Irms, Z
   if Vmt.get()==0: Vmt.set(120)
   else: 
     Vm.set(Vmt.get())              #Magnitud de V en domf simplemente asignar   
     Va.set(Vat.get())              #Angulo de V en domf simplemente asignar  
     Vme.set(Vmt.get() / m.sqrt(2)) #Magnitud de Vrms
     Vae.set(Va.get())              #Angulo de Vrms

     Im.set(Imt.get())              #Magnitud de I en domf simplemente asignar
     Ia.set(Iat.get())              #Angulo de I en domf simplemente asignar 
     Ime.set(Imt.get() / m.sqrt(2)) #Magnitud de Irms
     Iae.set(Ia.get())              #Angulp de Irms
   
     Zm.set(Vme.get()/Ime.get())
     Za.set(Vae.get()-Iae.get())



   #Calculos de variables del dominio de la potencia P, Q, S, fp
   S.set(abs(Vme.get()*Ime.get()))
   P.set(round(S.get()*m.cos(m.radians(Vae.get())-m.radians(Iae.get())),7))
   Q.set(round(S.get()*m.sin(m.radians(Vae.get())-m.radians(Iae.get())),7))
   fp.set(P.get()/S.get())
   
   if f.get()==0:
        f.set(60)
   plotdomT()
   plotdomF()
   plotdomP()
        
   
   

   

##################################################################################################


#                            CALCULO DOMINIO DE LA FRECUENCIA                                    #


def caldomF():
   f.set(60)
   #Calculos de variables del dominio del tiempo  V, Vrms, I, Irms, Z
   if Vme.get()!=0:
        Vm.set(round(Vme.get()*m.sqrt(2),5))
   if Ime.get()!=0:
        Im.set(round(Ime.get()*m.sqrt(2),5))

   if Vm.get()==0:
        if Im.get()!=0 and Zm.get()!=0:
           Vm.set(round(Im.get()*Zm.get(),5))
   else:
        Vme.set(round(Vm.get()/m.sqrt(2),5))
   
   if Im.get==0:
        if Vm.get() != 0 and Zm.get() !=0:
          Im.set(round(Vm.get()/Zm.get(),5))
   else:
          Ime.set(round(Im.get()/m.sqrt(2),5))
   if Zm.get()==0:
          Zm.set(round(Vm.get()/Im.get(),5))


##Angulos
   if Va.get() ==0:
        Va.set(Vae.get())
   else:
        Vae.set(Va.get())
   
   if Ia.get()==0:
        Ia.set(Iae.get())

   else:
        Iae.set(Ia.get())

   if Za.get()==0:
        Za.set(Va.get()-Ia.get())
   else:
      if Va.get()==0:
        Va.set(Ia.get()+Za.get())
        Vae.set(Va.get())
      else:
        Vae.set(Va.get())
      if Ia.get()==0:
         Ia.set(Va.get()-Za.get())
         Iae.set(Ia.get())
      else:
        Iae.set(Ia.get())




   Vmt.set(Vm.get())              #Magnitud de V en domf simplemente asignar   
   Vat.set(Va.get())              #Angulo de V en domf simplemente asignar  

   Imt.set(Im.get())              #Magnitud de I en domf simplemente asignar
   Iat.set(Ia.get())              #Angulo de I en domf simplemente asignar 
   


   #Calculos de variables del dominio de la potencia P, Q, S, fp
   S.set(abs(Vme.get()*Ime.get()))
   P.set(round(S.get()*m.cos(m.radians(Vae.get())-m.radians(Iae.get())),7))
   Q.set(round(S.get()*m.sin(m.radians(Vae.get())-m.radians(Iae.get())),7))
   fp.set(P.get()/S.get())
   plotdomT()
   plotdomF()
   plotdomP()
   
##################################################################################################


#                            CALCULO DOMINIO DE LA POTENCIA                                      #
  #Calculos de variables del dominio del tiempo  V, Vrms, I, Irms, Z 
def caldomP():
 #Asumimos constantes en este caso, Vrms= 120 , Angulo de V=0, Frecuencia=60 

 #Calculos de variables electricas en el dominio de la frecuencia
  #Calculo del voltaje instantaneo y efectivo
  f.set(60)
  if P.get()==0:
        if fp.get()!=0 and S.get()!=0:
         P.set(fp.get()*S.get())
  elif S.get()==0:
        if fp.get()!=0 and P.get()!=0:
          S.set(P.get()/fp.get())
  elif fp.get()==0:
        if P.get()!=0 and S.get()!=0:
          fp.set(P.get()/S.get())

  

  Vme.set(120.0)
  Vae.set(0)
  Vm.set(Vme.get()*m.sqrt(2))
  Va.set(0)

  #Calculo de la corriente instantanea y efectiva
  Ime.set(S.get()/Vme.get())
  Iae.set((m.acos(fp.get()))*180/m.pi)
  Im.set(Ime.get()*m.sqrt(2))
  Ia.set(Iae.get())

  #Calculo de la impedancia
  Zm.set(Vme.get()/Ime.get())
  Za.set(Vae.get()-Iae.get())

 #Calculos de variables electricas en el dominio de la frecuencia
  Vmt.set(Vm.get())
  Vat.set(Va.get())
  Imt.set(Im.get())
  Iat.set(Ia.get())

  plotdomT()
  plotdomF()
  plotdomP()


#INTERFAZ DOMINIO DEL TIEMPO
##################################################################################################
##################################################################################################
##################################################################################################
##################################################################################################
##################################################################################################
##################################################################################################
##################################################################################################
##################################################################################################
fontStyle = tkFont.Font(size=15)

textov = Label(ventana,text="v",  font=fontStyle,bg='#AAA2A0')
textov.place(x=50,y=55)

textoi = Label(ventana, text="i",  font=fontStyle,bg='#AAA2A0')
textoi.place(x=50,y=115)

textof = Label(ventana,text="fz",  font=fontStyle,bg='#AAA2A0')
textof.place(x=50,y=175)


#Caja de texto
cajaVm = Entry(ventana,textvariable=Vmt)
cajaVm.place(x=80,y=55,
        width=100,
        height=30)

cajaVa = Entry(ventana,textvariable=Vat)
cajaVa.place(x=200,y=55,
        width=100,
        height=30)



cajaIm= Entry(ventana, textvariable=Imt)
cajaIm.place(x=80,y=120,width=100,
        height=30)

cajaIa= Entry(ventana, textvariable=Iat)
cajaIa.place(x=200,y=120,width=100,
        height=30)

cajaf = Entry(ventana,textvariable=f)
cajaf.place(x=80,y=180,width=100,
        height=30)





#INTERFAZ DOMINIO DE LA FRECUENCIA
##################################################################################################
##################################################################################################
##################################################################################################
##################################################################################################
##################################################################################################
##################################################################################################
##################################################################################################
##################################################################################################

textov = Label(ventana,text="V",  font=fontStyle,bg='#AAA2A0')
textov.place(x=500,y=55)

textoi = Label(ventana, text="I",  font=fontStyle,bg='#AAA2A0')
textoi.place(x=500,y=115)

textov = Label(ventana,text="Vrms",  font=fontStyle,bg='#AAA2A0')
textov.place(x=470,y=175)

textoi = Label(ventana, text="Irms",  font=fontStyle,bg='#AAA2A0')
textoi.place(x=470,y=235)

textov = Label(ventana,text="Z",  font=fontStyle,bg='#AAA2A0')
textov.place(x=500,y=295)




#Caja de texto
cajaVm = Entry(ventana,textvariable=Vm)
cajaVm.place(x=530,y=55,
        width=100,
        height=30)

cajaVa = Entry(ventana,textvariable=Va)
cajaVa.place(x=650,y=55,
        width=100,
        height=30)

cajaVrms_m = Entry(ventana,textvariable=Vme)
cajaVrms_m.place(x=530,y=175,
        width=100,
        height=30)

cajaVrms_a = Entry(ventana,textvariable=Vae)
cajaVrms_a.place(x=650,y=175,
        width=100,
        height=30)


cajaIm= Entry(ventana, textvariable=Im)
cajaIm.place(x=530,y=120,width=100,
        height=30)

cajaIa= Entry(ventana, textvariable=Ia)
cajaIa.place(x=650,y=120,width=100,
        height=30)

cajaIrms_m = Entry(ventana,textvariable=Ime)
cajaIrms_m.place(x=530,y=235,
        width=100,
        height=30)

cajaIrms_a = Entry(ventana,textvariable=Iae)
cajaIrms_a.place(x=650,y=235,
        width=100,
        height=30)

cajaZm = Entry(ventana,textvariable=Zm)
cajaZm.place(x=530,y=295,
        width=100,
        height=30)

        
cajaZa = Entry(ventana,textvariable=Za)
cajaZa.place(x=650,y=295,
        width=100,
        height=30)

#Botones
calcula = Button(ventana,text="Calcular",command=AppController)
calcula.place(x=620,y=800)

clear = Button(ventana,text="Borrar datos",command=clearData)
clear.place(x=700,y=800)




#INTERFAZ POWER
##################################################################################################
##################################################################################################
##################################################################################################
##################################################################################################
##################################################################################################
##################################################################################################
##################################################################################################
##################################################################################################

textoP = Label(ventana,text="P",  font=fontStyle,bg='#AAA2A0')
textoP.place(x=940,y=55)

textoQ = Label(ventana, text="Q",  font=fontStyle,bg='#AAA2A0')
textoQ.place(x=940,y=115)

textoS = Label(ventana,text="S",  font=fontStyle,bg='#AAA2A0')
textoS.place(x=940,y=175)

textofP = Label(ventana, text="fp",  font=fontStyle,bg='#AAA2A0')
textofP.place(x=940,y=235)

#Caja de texto
cajaP = Entry(ventana,textvariable=P)
cajaP.place(x=970,y=55,
        width=150,
        height=30)

cajaQ= Entry(ventana, textvariable=Q)
cajaQ.place(x=970,y=120,width=150,
        height=30)

cajaS = Entry(ventana,textvariable=S)
cajaS.place(x=970,y=180,width=150,
        height=30)

cajafp= Entry(ventana, textvariable=fp)
cajafp.place(x=970,y=240,width=150,
        height=30)





##################################################################################################


#                                        GRAFICAS                                                #


##################################################################################################



#GRAFICA DOMINIO DEL TIEMPO
##################################################################################################
##################################################################################################
##################################################################################################
##################################################################################################
##################################################################################################
##################################################################################################
##################################################################################################
##################################################################################################
def plotdomT():
        frame = Frame(ventana, bg='#AAA2A0')
        frame.grid(column=0,row=0, sticky='nsew')

        frame.place(x=42,y=250)
        Fs = 8000
      
        sample = 4000
        x = np.arange(sample)
        v = Vmt.get()*np.cos((f.get()* x/Fs)+Vat.get())
        i = Imt.get()*np.cos((f.get()* x/Fs)+Iat.get())
        p = 1/2*(Vmt.get()*Imt.get())*np.cos(Vat.get()-Iat.get())+1/2*(Vmt.get()*Imt.get())*np.cos(2*f.get()*x/Fs+Vat.get()+Iat.get())

        #Voltaje
        fig, axs = plt.subplots(3,1 , dpi=80, figsize=(5, 7), sharex=True,
                facecolor='#AAA2A0')
        
        axs[0].set_ylabel('Voltios(V)', fontsize=10, loc='center')
        axs[0].plot(x,v,color="blue",lw=1)
        axs[0].set_title('v(t)')
        axs[0].grid()
        axs[0].set_xlabel('t', fontsize=12)
        


        axs[1].plot(x,i,color="red",lw=1)
        axs[1].set_title('i(t)')
        axs[1].grid()
        axs[1].set_ylabel('Amperios(A)')
        axs[1].set_xlabel('t', fontsize=12)

        axs[2].plot(x,p,color="green",lw=1)
        axs[2].set_title('p(t)')
        axs[2].grid()
        axs[2].set_xlabel('t', fontsize=12)
        axs[2].set_ylabel('Watt(W)')

        canvas = FigureCanvasTkAgg(fig, master = frame)  # Crea el area de dibujo en Tkinter
        canvas.draw()
        canvas.get_tk_widget().grid(column=0, row=0)



#GRAFICA DOMINIO DE LA FRECUENCIA
##################################################################################################
##################################################################################################
##################################################################################################
##################################################################################################
##################################################################################################
##################################################################################################
##################################################################################################
##################################################################################################
def plotdomF(): 
    def toRect(r,angulo):

        
        angulo = (float(angulo)*cm.pi)/180
        z = cm.rect(float(r),angulo)
        real = round(z.real,2)
        imag = round(z.imag,2)* 1j
        complejo = complex(real+imag)
        
        return complejo
        
    Ver =  toRect(Vme.get(),Vae.get())
    Ier =  toRect(Ime.get(),Iae.get())

    frameF = Frame(ventana, bg='#AAA2A0')
    frameF.grid(column=0,row=0, sticky='nsew')
    
    frameF.place(x=470,y=340)
    fig = Figure(figsize = (5, 5.5), 
                 dpi = 80,facecolor='#AAA2A0') 

    plot1 = fig.add_subplot(111) 

    plot1.plot([Ver.real,0],[Ver.imag,0],color="blue",lw=1, label="Vrms") 
    plot1.plot([Ier.real,0],[Ier.imag,0],color="red", lw=1, label="Irms")
    plot1.grid()
    plot1.set_xlabel('Re', fontsize=12)
    plot1.set_ylabel('Im')
    plot1.legend(loc="upper left", fontsize=12)

    canvas = FigureCanvasTkAgg(fig, master = frameF)   
    canvas.draw() 
    canvas.get_tk_widget().pack() 
#     toolbar = NavigationToolbar2Tk(canvas,frameF) 
#     toolbar.update() 
    canvas.get_tk_widget().pack() 



 #GRAFICA DOMINIO DE LA POTENCIA
##################################################################################################
##################################################################################################
##################################################################################################
##################################################################################################
##################################################################################################
##################################################################################################
##################################################################################################
##################################################################################################
def plotdomP(): 
    frameP = Frame(ventana, bg='#AAA2A0')
    frameP.grid(column=0,row=0, sticky='nsew')
    
    frameP.place(x=870,y=340)
    fig = Figure(figsize = (5, 5.5), 
                 dpi = 80,facecolor='#AAA2A0') 
    plot2 = fig.add_subplot(111) 
    plot2.plot([P.get(),0],[Q.get(),0],color="orange",lw=1) 
    plot2.grid()
    plot2.set_xlabel('P', fontsize=12)
    plot2.set_ylabel('Q')
    canvas = FigureCanvasTkAgg(fig, master = frameP)   
    canvas.draw() 
    canvas.get_tk_widget().pack() 
#     toolbar = NavigationToolbar2Tk(canvas,frameF) 
#     toolbar.update() 
    canvas.get_tk_widget().pack() 



##################################################################################################


#                                        CALCULOS                                                #


##################################################################################################

#CALCULOS DOMINIO DEL TIEMPO
##################################################################################################
##################################################################################################
##################################################################################################
##################################################################################################
##################################################################################################
##################################################################################################
##################################################################################################
##################################################################################################

plotdomT()
plotdomF()
plotdomP()
ventana.mainloop()

  