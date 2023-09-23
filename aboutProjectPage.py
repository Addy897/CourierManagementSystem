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
            981.0,
            148.0,
            text="C.M.S",
            fill="#03B114",
            anchor="nw",
            font=("Vollkorn", 40 * -1)
        )
        text="India's leading logistics and supply chain arm. We started operations in 2009 as Flipkart’s in-house supply chain arm. Our consistent excellence in consumer experience, with reliable delivery and managing variability at scale, has made us the preferred partner for various businesses. You can utilise our end-to-end fulfilment services to keep your customers happy with on-time deliveries and hassle-free services."
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
        