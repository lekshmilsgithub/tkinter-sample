import tkinter
import tkinter.messagebox
from PIL import ImageTk,Image



t=tkinter.Tk()
t.title('Profile')
t.geometry('500x500')

p=Image.open( 'C:\Users\vinod\Desktop\tkinter-sample\bhj.jpg')

p=ImageTk.PhotoImage(p)
pic=tkinter.Label(t,image=p)
pic.place(x=0,y=0)





a=tkinter.Label(text="Profile Creation",bg='purple',fg='white',font=('times new roman',35,'bold'))
a.place(x=100,y=0)



b=tkinter.Label(text="First Name",bg='green',fg='black',font=('times new roman',25,'italic'))
b.place(x=50,y=100)

c=tkinter.Entry(width=20)
c.place(x=270,y=120)



d=tkinter.Label(text="Location",bg='green',fg='black',font=('times new roman',25,'italic'))
d.place(x=50,y=170)

e=tkinter.Entry(width=20)
e.place(x=270,y=190)

def fun():

    name=c.get()
    place=e.get()

    if(name=="" or place==""):
        tkinter.messagebox.showerror("error","fill the box")

    else:
        import pymysql
        x=pymysql.connect(host='localhost',user='root',password='gagana',db='lekshmi')
        cur=x.cursor()
        cur.execute('insert into profile values("'+name+'","'+place+'")')
        x.commit()
        x.close()
    
    tkinter.messagebox.showinfo("thank you","thank uu for visiting")

                                
    t.destroy()
    



f=tkinter.Button(text='Submit',bg='red',fg='black',font=('times new roman',25,'bold'),command=fun)
f.place(x=200,y=270)








t.mainloop()
