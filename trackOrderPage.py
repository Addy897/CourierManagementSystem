from tkinter import *
from nav import Nav
from PIL import ImageTk,Image
class TrackOrder:
    def __init__(this,context):
        this.ctx=context
        this.ctx.trackOrderPage=this.trackOrderPage
       
    def trackOrderPage(this):
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
        
        this.entry_image_1 = PhotoImage(
            file=this.ctx.assets("newUserEntry.png"))
        entry_bg_1 = canvas.create_image(
            783.5,
            186.0,
            image=this.entry_image_1
        )
        searchBox = Entry(
            bd=0,
            bg="#FFFFFF",
            highlightthickness=0
        )
        searchBox.place(
            x=581.0,
            y=156.0,
            width=405.0,
            height=48.0
        )
        canvas.create_text(
            431.0,
            185.0,
            text="Enter Product Id",
            font=("Iceland", 40 * -1)
        )
        n.nav(canvas,258,0)
        this.ctx.createRoundedTile(canvas,85,221,440+5,1218+5,radius=32,fill="#696969")
        this.ctx.createRoundedTile(canvas,85,221,440,1218,radius=32,fill="#74BB5B")
        canvas.create_line(300,241,300,241+401,fill="#000000",width=1)


        def clicked(event):
            closest = canvas.find_closest(event.x, event.y)
            n.changeNav(closest=closest)
        labels=[]
        def showOrders(event):
            for i in labels:
                canvas.delete(i)
            labels.clear()
            refId=searchBox.get()
            if(refId ==""):
                return
            con=this.ctx.getConnector()
            cur=con.cursor()
            query=f"select rname,saddr,raddr,spno,rpno,pdate,rdate,image,status,refId from products where refId='{refId}' and status != 'cancled' and uid={this.ctx.uid};"
            cur.execute(query)
            result=cur.fetchone()
            con.close()
            x1,y1=310,245
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
            this.ImageL.place(x=90,y=250)
        canvas.bind('<Button>', clicked)
        searchBox.bind("<Return>",showOrders)
        n.nav(canvas,258,0)
       