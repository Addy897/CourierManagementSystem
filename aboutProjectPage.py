from threading import Thread
from time import sleep
from tkinter import *
from nav import Nav
class AboutProject:
    def __init__(this,context):
        this.ctx=context
        this.ctx.aboutProjectPage=this.aboutProjectPage
       
    def aboutProjectPage(this):
        n=Nav(this.ctx)
        canvas = Canvas(
            this.ctx.window,
            bg = "#FFFFFF",
            height = 768,
            width = 1366,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )
        canvas.place(x = 0, y = 0)
        canvas.create_text(
            853.0,
            148.0,
            text="We are",
            anchor="nw",
            font=("Vollkorn", 40 * -1)
        )
        canvas.create_text(
            990.0,
            148.0,
            text="C.M.S",
            fill="#03B114",
            anchor="nw",
            font=("Vollkorn", 40 * -1)
        )
        text="The C.M.S(Courier Management System) is a business system that makes it easier to manage and route couriers. This helps business get more customer and be known to more people. C.M.S solution handles the end-to-end process starting from initiating a courier order, driver pickup, and delivery of a courier business. C.M.S covers all the controls and processes involved in national Courier Importation Services and Domestic Pickup & Delivery"
        t=canvas.create_text(
            853.0,
            197.0,
            anchor="nw",
            width=469,
            font=("Vollkorn", 20 * -1)
        )
        this.aimage = PhotoImage(
            file=this.ctx.assets("audacity.png"))
        i=canvas.create_image(
            395,
            390,
            image=this.aimage
        )
        def clicked(event):
            closest = canvas.find_closest(event.x, event.y)
            n.changeNav(closest=closest)
        aThread=Thread(target=this.animateText,args=(canvas,t,text))
        aThread.daemon=True
        aThread.start()
        iThread=Thread(target=this.animateBox,args=(canvas,i))
        iThread.daemon=True
        iThread.start()
        canvas.bind('<Button>', clicked)
        
        n.nav(canvas,258,0)      
    def animateBox(this,canvas:Canvas,item):
        images=["audacity.png","BiasForAction.png","customer.png","integrity.png"]
        try:
            while True:
                for i in images:
                    this.aimage = PhotoImage(file=this.ctx.assets(i))
                    canvas.itemconfig(item,image=this.aimage)
                    canvas.update()
                    sleep(3)
        except Exception as e:
            print("[-] Error In AboutPage animateBox:",e)
            
              
    def  animateText(this,canvas:Canvas,item,texts):
        try:
            while True:
                for text in texts.split(". "):
                    msg=""
                    for i in text:
                        msg+=i
                        canvas.itemconfig(item,text=msg)
                        canvas.update()
                        sleep(0.05)
                    sleep(1)
        except Exception as e:
            print("[-] Error In AboutPage animateText:",e)
        