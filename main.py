from tkinter import *  
import time  
from datetime import datetime  
def time():  
    now = datetime.now()  
    hour= str(now.strftime("%H"))  
    min= str(now.strftime("%M"))  
    sec= str(now.strftime("%S"))  
    a="AM"  
    if int(hour)>12:  
      hour=int(hour)-12  
      a="PM"  
    lable1.config(text=hour)  
    lable2.config(text=min)  
    lable3.config(text=sec)  
    lable4.config(text=a)  
    lable1.after(200,time)  
root=Tk()  
root.title("Digital Clock")  
root.geometry("1350x700+0+0")  
root.config(bg='#081923')  
 #========show time  
lable1=Label(text="12",fg="white",bg="#009ACD",font=("times new roman",40, "bold"),width=5,height=2)  
lable1.place(x=280,y=150)  
lable2=Label(text="12",fg="white",bg="#00BFFF",font=("times new roman",40, "bold"),width=5,height=2)  
lable2.place(x=430,y=150)  
lable3=Label(text="12",fg="white",bg="#EE7600",font=("times new roman",40, "bold"),width=5,height=2)  
lable3.place(x=580,y=150)  
lable4=Label(text="12",fg="white",bg="#FF7F50",font=("times new roman",40, "bold"),width=5,height=2)  
lable4.place(x=730,y=150)  
 #==========hours seconds  
lable5=Label(text="Mins",fg="white",bg="#00BFFF",font=("times new roman",40, "bold"),width=5,height=1)  
lable5.place(x=430,y=290)  
lable6=Label(text="Sec",fg="white",bg="#EE7600",font=("times new roman",40, "bold"),width=5,height=1)  
lable6.place(x=580,y=290)  
lable7=Label(text="Noon",fg="white",bg="#FF7F50",font=("times new roman",40, "bold"),width=5,height=1)  
lable7.place(x=730,y=290)  
lable8=Label(text="Hour",fg="white",bg="#009ACD",font=("times new roman",40, "bold"),width=5,height=1)  
lable8.place(x=280,y=290)  
time()  
root.mainloop()  
