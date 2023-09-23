import datetime
import smtplib
from tkinter import *
from tkinter import filedialog
from PIL import Image,ImageTk
from mapBox import MapBox
from nav import Nav


class PlaceOrder:
    def __init__(this, context):
        this.ctx = context
        this.ctx.placeOrderPage = this.placeOrderPage
        

    def placeOrderPage(this):
        n = Nav(this.ctx)
        if(not this.ctx.loggedIn):
            this.ctx.loginPage()
            return
        else:
            con=this.ctx.getConnector()
            cur=con.cursor()
            #query="use users;"
            #cur.execute(query)
            query=f"Select fname,address,email from user_details where uname=\'{this.ctx.user}\'"
            cur.execute(query)
            this.sname,addr,email=cur.fetchone()
            con.close()
            
        canvas = Canvas(
            this.ctx.window,
            bg="#FFFFFF",
            height=768,
            width=1366,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        this.image_image_1 = PhotoImage(
            file=this.ctx.assets("registerBox.png"))
        image_1 = canvas.create_image(
            1080.0-250,
            372.0,
            image=this.image_image_1
        )
        canvas.place(x=0, y=0)
        this.entry_image_1 = PhotoImage(
            file=this.ctx.assets("newUserEntry.png"))
        rphoneEntryBg = canvas.create_image(
            1083.5-250,
            572.0,
            image=this.entry_image_1
        )
        rphone = Entry(
            bd=0,
            bg="#FFFFFF",
            highlightthickness=0
        )
        rphone.place(
            x=881.0-250,
            y=542.0,
            width=405.0,
            height=48.0
        )
        sphoneEntryBg = canvas.create_image(
            1083.5-250,
            472.0,
            image=this.entry_image_1
        )
        sphone = Entry(
            bd=0,
            bg="#FFFFFF",
            text="",
            highlightthickness=0
        )
        sphone.place(
            x=881.0-250,
            y=442.0,
            width=405.0,
            height=48.0
        )

        raddrEntryBg = canvas.create_image(
            1083.5-250,
            378.0,
            image=this.entry_image_1
        )
        raddr = Entry(
            bd=0,
            bg="#FFFFFF",
            highlightthickness=0
        )
        raddr.place(
            x=881.0-250,
            y=348.0,
            width=405.0,
            height=48.0
        )

        saddrEntryBg = canvas.create_image(
            1083.5-250,
            284.0,
            image=this.entry_image_1
        )
        saddr = Entry(
            bd=0,
            bg="#FFFFFF",
            highlightthickness=0
        )

        saddr.place(
            x=881.0-250,
            y=254.0,
            width=405.0,
            height=48.0
        )
        saddr.insert(0, addr)
        rnameEntryBg = canvas.create_image(
            1083.5-250,
            186.0,
            image=this.entry_image_1
        )
        rname = Entry(
            bd=0,
            bg="#FFFFFF",
            
            highlightthickness=0
        )

        rname.place(
            x=881.0-250,
            y=156.0,
            width=405.0,
            height=48.0
        )

        
        placeButton=this.ctx.createRoundedTile(
            canvas,
            x=878.0-250,
            y=649.0,
            width=419.0,
            height=50.0,
            radius=50,
            fill="#2040AF"
        )
        canvas.create_text(
            800.0,
            650.0,
            anchor="nw",
            text="Place",
            fill="#000000",
            font=("Vollkorn", 30 * -1)
        )
        canvas.create_text(
            874.0-250,
            48.0,
            anchor="nw",
            text="Place Order",
            fill="#000000",
            font=("Iceland", 40 * -1)
        )

        canvas.create_text(
            877.0-250,
            133.0,
            anchor="nw",
            text="Reciever's Name",
            fill="#000000",
            font=("Vollkorn", 20 * -1)
        )
        canvas.create_text(
            877.00-250,
            231.0,
            anchor="nw",
            text="Sender's Address",
            fill="#000000",
            font=("Vollkorn", 20 * -1)
        )

        canvas.create_text(
            878.0-250,
            319.0,
            anchor="nw",
            text="Reciever's Address",
            fill="#000000",
            font=("Vollkorn", 20 * -1)
        )

        canvas.create_text(
            877.0-250,
            414.0,
            anchor="nw",
            text="Your Phone No.",
            fill="#000000",
            font=("Vollkorn", 20 * -1)
        )

        canvas.create_text(
            877.0-250,
            516.0,
            anchor="nw",
            text="Reciver's Phone No.",
            fill="#000000",
            font=("Vollkorn", 20 * -1)
        )

        e = canvas.create_text(
            1068.0-170-250,
            612.0,
            anchor="nw",
            text="",
            fill="#000000",
            font=("Vollkorn", 15 * -1)
        )

        this.locButtonImg = PhotoImage(
            file=this.ctx.assets("loc.png"))
        sloc = Button(
            image=this.locButtonImg,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: this.ctx.window.after(0, gmap),
            relief="flat"
        )
        sloc.place(
            x=1040.0-250,
            y=230.0,
            width=18.0,
            height=22.0
        )
        rloc = Button(
            image=this.locButtonImg,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: this.ctx.window.after(0, gmap, "r"),
            relief="flat"
        )
        rloc.place(
            x=1060.0-250,
            y=319.0,
            width=18.0,
            height=22.0
        )
        

        def gmap(f="s"):
            try:
                app = MapBox(this.ctx.window)
                address = app.start()
                if (f == 'r'):
                    raddr.delete(0, END)
                    raddr.insert(0, address.address)
                else:
                    saddr.delete(0, END)
                    saddr.insert(0, address.address)
            except:
                pass
        canvas.create_rectangle(230,133,430,333)
        buttonImage=canvas.create_text(
            330,
            350,
            text="Select Image Of Product",
            font=("Vollkorn", 20 * -1)
        )
        this.imgPath=None
        def clicked(event):
            closest = canvas.find_closest(event.x, event.y)
            n.changeNav(closest=closest)
            bbox=canvas.bbox(placeButton)
            if(buttonImage in closest):
                this.imgPath=filedialog.askopenfilename(initialdir="/", title="Select Product Image",
                    filetypes=(("Image files", "*.png"),("All files", "*.*")))
                this.image = Image.open(this.imgPath)
                this.image=this.image.resize((200,200))
                this.image=ImageTk.PhotoImage(this.image)
                this.imageL=Label(canvas,image=this.image,height=200,width=200)
                this.imageL.place(x=230,y=133)
            elif(event.x>bbox[0] and event.y>bbox[1] and event.x<bbox[2] and event.y<bbox[3]):
                if(this.imgPath is None):
                    this.ctx.show_error(canvas,e,"Please Provide Image of Product")
                    return
                pDate=datetime.datetime.now()
                details={"rname":rname.get(),"saddr":saddr.get(),"raddr":raddr.get(),"sphone":sphone.get(),"rphone":rphone.get(),"pDate":f"{pDate.year}-{pDate.month}-{pDate.day}","rDate":f"{pDate.year}-{pDate.month}-{pDate.day+7}","Image":this.imgPath}
                if(this.verifyDetails(canvas,e,details)):
                    refId=this.place(details)
                    if(refId is not False):
                        this.ctx.show_error(canvas,e,f"Placing Order.Please Wait",fill="#004dcf")
                        canvas.update()
                        raddr.delete(0, END)
                        saddr.delete(0, END)
                       
                        rphone.delete(0, END)
                        sphone.delete(0, END)
                        this.sendRefId(this.sname,email,refId)
                        this.ctx.window.clipboard_clear()
                        this.ctx.window.clipboard_append(refId)

                        this.ctx.show_error(canvas,e,f"Your Product Ref Id is: {refId}",fill="#004dcf")
                    else:
                        this.ctx.show_error(canvas,e,f"Your Product Place Failed!!")
        canvas.bind('<Button>', clicked)

        n.nav(canvas, 258, 0)
        canvas.update()
    def sendRefId(this,name,email,refId):
        try:
            e,p="Project email here ","Your gmail app password here"
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.ehlo()
            server.starttls()
            try:
                server.login(e, p)
            except smtplib.SMTPAuthenticationError:
               return False
            header='To:'+email+'\n'+'From:'+e+'\n'+'subject:Order Placed\n'+"Hey, "+name+"\nYour Order Has been Placed\nYour Refernce Id is: "
            
            msg=header+refId
            server.sendmail(e, email, msg)
            server.close()
        except:
            return False
    def verifyDetails(this,canvas:Canvas,e:int,details:dict):
        for i in details.keys():
            if(not this.ctx.parseChars(details[i])):
                if("rname" in i):
                    this.ctx.show_error(canvas,e,"Enter Valid Name")
                    return False
                elif("saddr"  in i or "raddr" in i ):
                    this.ctx.show_error(canvas,e,"Enter Valid Address")
                    return False
                elif("rphone" in i or "sphone" in i):
                    this.ctx.show_error(canvas,e,"Enter Valid Phone No.")
                    return False
        if(len(details["rphone"])!=10 or len(details["sphone"])!=10):
            this.ctx.show_error(canvas,e,"Enter Valid Phone No.")
            return False
        elif(len(details["rname"])==0):
            this.ctx.show_error(canvas,e,"Enter Valid Name.")
            return False
        elif(len(details["raddr"])==0 or len(details["saddr"])==0):
            this.ctx.show_error(canvas,e,"Enter Valid Address.")
            return False
        elif("India" not in details["raddr"] or "India" not in  details["saddr"]):
            this.ctx.show_error(canvas,e,"Incomplete Address.(House No. Area City State India)")
            return False
        else:
            this.ctx.show_error(canvas,e,"")
            return True
    def place(this,details):
        con=this.ctx.getConnector()
        cur=con.cursor()
        refId=f"U{this.ctx.uid}{datetime.datetime.now().year}{datetime.datetime.now().month}{datetime.datetime.now().day}{datetime.datetime.now().hour}{datetime.datetime.now().minute}{datetime.datetime.now().second}"
        
        try:
            query=f'''insert into products (rname,sname,saddr,raddr,spno,rpno,pDate,rDate,image,status,refId,uid) values("{details['rname']}",
              "{this.sname}",
              "{details['saddr']}" ,
              "{details['raddr']}",
              {details['sphone']},
              {details['rphone']},
              "{details['pDate']}",
              "{details['rDate']}",
              "{details['Image']}",
              "Not Picked Up",
              "{refId}",
              {this.ctx.uid});
              '''
            cur.execute(query)
            con.commit()
            con.close()
        except Exception as e:
            print(e)
            return False
        return refId
       
        
       
       