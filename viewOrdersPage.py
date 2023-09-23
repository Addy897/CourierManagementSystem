from tkinter import *
from PIL import Image,ImageTk
from nav import Nav 

class ViewOrders:
    def __init__(this,ctx):
        this.ctx = ctx
        this.ctx.viewOrderPage = this.viewOrderPage
    def viewOrderPage(this):
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
        n.nav(canvas,258,0)
        this.ctx.createRoundedTile(canvas,85,100,500+5,1200+5,radius=32,fill="#696969")
        this.ctx.createRoundedTile(canvas,85,100,500,1200,radius=32,fill="#74BB5B")
        canvas.create_line(300,121,300,121+401,fill="#000000",width=1)

        this.nextimage = Image.open(this.ctx.assets("next.png"))
        this.nextimage=this.nextimage.resize((50,50))
        this.nextimage=ImageTk.PhotoImage(this.nextimage)
        this.nextButton=Label(canvas,image=this.nextimage,height=50,width=50)
        this.nextButton.place(x=600,y=620)

        this.previousimage = Image.open(this.ctx.assets("previous.png"))
        this.previousimage=this.previousimage.resize((50,50))
        this.previousimage=ImageTk.PhotoImage(this.previousimage)
        this.previousButton=Label(canvas,image=this.previousimage,height=50,width=50)
        this.previousButton.place(x=420,y=620)
        con=this.ctx.getConnector()
        cur=con.cursor()
        query=f"select rname,saddr,raddr,spno,rpno,pdate,rdate,image,status,refId from products where uid={this.ctx.uid};"
        cur.execute(query)
        listR=cur.fetchall()
        con.close()
        this.count=0
        
        def clicked(event):
            closest = canvas.find_closest(event.x, event.y)
            n.changeNav(closest=closest)
            
                
        labels=[]
        this.ImageL=None
        def showOrders(count):
            try:
                this.ImageL.destroy()
            except:
                pass
            for i in labels:
                canvas.delete(i)
            labels.clear()
            if(len(listR)==0):
                return
            result=listR[count]
            x1,y1=310,145
            d=40
            fontSize=20
            labels.append(canvas.create_text(
            x1,
            y1,
            anchor="nw",
            text="Reciver's Name: "+result[0],
            font=("Vollkorn", fontSize * -1)
            ))
            labels.append(canvas.create_text(
            x1,
            y1+(d),
            anchor="nw",
            text="Sender's Address: "+result[1],
            font=("Vollkorn", fontSize * -1)
            ))
            labels.append(canvas.create_text(
            x1,
            y1+(2*d),
            anchor="nw",
            text="Reciever's Address: "+result[2],
            font=("Vollkorn", fontSize * -1)
            ))
            labels.append(canvas.create_text(
            x1,
            y1+(3*d),
            anchor="nw",
            text="Sender's Phone No.: "+str(result[3]),
            font=("Volkorn", fontSize * -1)
            ))
            labels.append(canvas.create_text(
            x1,
            y1+(4*d),
            anchor="nw",
            text="Reciever's Phone No.: "+str(result[4]),
            font=("Volkorn", fontSize * -1)
            ))
            labels.append(canvas.create_text(
            x1,
            y1+(5*d),
            anchor="nw",
            text="Order Placed On: "+str(result[5]),
            font=("Volkorn", fontSize * -1)
            ))
            labels.append(canvas.create_text(
            x1,
            y1+(6*d),
            anchor="nw",
            text="Delivery On: "+str(result[6]),
            font=("Volkorn", fontSize * -1)
            ))
            labels.append(canvas.create_text(
            x1,
            y1+(7*d),
            anchor="nw",
            text="Current Status: "+str(result[8]),
            font=("Volkorn", fontSize * -1)
            ))
            labels.append(canvas.create_text(
            x1,
            y1+(8*d),
            anchor="nw",
            text="RefId: "+result[9],
            font=("Volkorn", fontSize * -1)
            ))
            this.currentImage = Image.open(result[7])
            this.currentImage=this.currentImage.resize((200,200))
            this.currentImage=ImageTk.PhotoImage(this.currentImage)
            this.ImageL=Label(canvas,image=this.currentImage,height=200,width=200)
            this.ImageL.place(x=90,y=150)
        def showNext(event):
             if(this.count<len(listR)-1):
                    this.count+=1
                    showOrders(this.count)
        def showPrevious(event):
            if(this.count>0):
                    this.count-=1
                    showOrders(this.count)
        showOrders(this.count)

        canvas.bind('<Button>', clicked)
        this.nextButton.bind("<Button>",showNext)
        this.previousButton.bind("<Button>",showPrevious)
        n.nav(canvas,258,0)