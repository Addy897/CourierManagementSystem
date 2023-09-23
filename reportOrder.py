from tkinter import *
from nav import Nav
from PIL import ImageTk,Image
class ReportOrder:
    def __init__(this,context):
        this.ctx=context
        this.ctx.reportOrderPage=this.reportOrderPage
       
    def reportOrderPage(this):
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
        canvas.create_image(
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
        canvas.create_text(
            520.0,
           300.0,
            text="Reason",
            font=("Iceland", 40 * -1)
        )
        this.searchBoxImage = PhotoImage(
            file=this.ctx.assets("ReasonBox.png"))
        canvas.create_image(
            720.0,
            365.0,
            image=this.searchBoxImage
        )
        reasonBox=Text(this.ctx.window, 
                width=30, 
                height=8,
                highlightthickness=0,
                borderwidth=0)
        reasonBox.place(x=600,y=300)
        submitButton=this.ctx.createRoundedTile(canvas,500,500,40,150,radius=40,fill="#74BB5B")
        submitTxt=canvas.create_text(
            570.0,
           520.0,
            text="Submit",
            
            font=("Vollkorn", 20 * -1)
        )
        e=canvas.create_text(
            520.0,
           470.0,
            text="",
            anchor="nw",
            font=("Vollkorn", 20 * -1)
        )
        def clicked(event):
            closest = canvas.find_closest(event.x, event.y)
            n.changeNav(closest=closest)
            bbox=canvas.bbox(submitTxt)
            if((event.x>bbox[0] and event.y>bbox[1] and event.x<bbox[2] and event.y<bbox[3]) or submitButton in closest):
                refId=searchBox.get()
                reason=reasonBox.get(1.0, "end")
                if(refId==""):
                    this.ctx.show_error(canvas,e,"Enter Product RefId")
                elif(reason == ""):
                    this.ctx.show_error(canvas,e,"Enter Reason For Report")
                else:
                    con=this.ctx.getConnector()
                    cur=con.cursor()
                    query=f"select count(uid) from products where refId='{refId}' and status != 'cancled' and uid = {this.ctx.uid};"
                    cur.execute(query)
                    exist=cur.fetchone()
                    query=f"select fname from  user_details where eid='{this.ctx.uid}';"
                    cur.execute(query)
                    fname=cur.fetchone()
                    if(exist == None):
                        this.ctx.show_error(canvas,e,"Invalid Product RefId")
                        con.close()
                    else:
                        query=f'''insert into reports set (refId,uid,rname,reason) values("{refId}",
                            {this.ctx.uid} ,
                            "{fname[0]}",
                            "{reason}");
                            '''
                        cur.execute(query)
                        con.commit()
                        con.close()
                        this.ctx.show_error(canvas,e,f"Successfully Reported Product {refId}","#004dcf")
                    
        canvas.bind('<Button>', clicked)
        
        n.nav(canvas,258,0)
       