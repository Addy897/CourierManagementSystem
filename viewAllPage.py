from tkinter import *
from nav import Nav
class ViewAll:
    def __init__(this,context):
        this.ctx=context
        this.ctx.viewAllPage=this.viewAllPage
       
    def viewAllPage(this):
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
        con=this.ctx.getConnector()
        cur=con.cursor()
        query=f"Select count(*) from products where uid=\'{this.ctx.uid}\'"
        cur.execute(query)
        orderCount=cur.fetchone()[0]
        query=f"Select count(*) from products where uid=\'{this.ctx.uid}\' and status='cancled'"
        cur.execute(query)
        cancelCount=cur.fetchone()[0]
        query=f"Select count(*) from reports where uid=\'{this.ctx.uid}\'"
        cur.execute(query)
        reportCount=cur.fetchone()[0]
        con.close()
        orderButton=this.ctx.createRoundedTile(canvas,90,130,200,263)
        canvas.create_text(
            227.0,
            209.0,
            fill="#FFFFFF",
            text="View Your\nOrders",
            font=("Iceland", 38 * -1)
            )
        this.ctx.createRoundedTile(canvas,90,292,38,263,radius=40,fill="#22E27A")
        orders=canvas.create_text(
            217.0,
            309.0,
            fill="#FFFFFF",
            text=orderCount,
            font=("Iceland", 38 * -1)
            )

        placeButton=this.ctx.createRoundedTile(canvas,504,130,200,263)
        placeTxt=canvas.create_text(
            635.0,
            209.0,
            fill="#FFFFFF",
            text="Place Orders",
            font=("Iceland", 38 * -1)
            )
        this.ctx.createRoundedTile(canvas,504,292,38,263,radius=40,fill="#22E27A")
        placed=canvas.create_text(
            635.0,
            309.0,
            fill="#FFFFFF",
            text=orderCount-cancelCount,
            font=("Iceland", 38 * -1)
            )

        cancelButton=this.ctx.createRoundedTile(canvas,918,130,200,263)
        canvas.create_text(
            1045.0,
            209.0,
            fill="#FFFFFF",
            text="Cancel Orders",
            font=("Iceland", 38 * -1)
            )
        this.ctx.createRoundedTile(canvas,918,292,38,263,radius=40,fill="#22E27A")
        cancelled=canvas.create_text(
            1048.0,
            309.0,
            fill="#FFFFFF",
            text=cancelCount,
            font=("Iceland", 38 * -1)
            )
        
        trackButton=this.ctx.createRoundedTile(canvas,288,425,200,263)
        canvas.create_text(
            425.0,
            520.0,
            fill="#FFFFFF",
            text="Track Your\nOrders",
            font=("Iceland", 38 * -1)
            )
        this.ctx.createRoundedTile(canvas,288,597,38,263,radius=40,fill="#22E27A")
        
        reportButton=this.ctx.createRoundedTile(canvas,698,425,200,263)
        canvas.create_text(
            823.0,
            502.0,
            fill="#FFFFFF",
            text="Reports",
            font=("Iceland", 38 * -1)
            )
        this.ctx.createRoundedTile(canvas,698,597,38,263,radius=40,fill="#22E27A")
        reported=canvas.create_text(
            833.0,
            615.0,
            fill="#FFFFFF",
            text=reportCount,
            font=("Iceland", 38 * -1)
            )
        
        def clicked(event):
                    closest = canvas.find_closest(event.x, event.y)
                    n.changeNav(closest=closest)
                    if placeButton in closest or placeTxt in closest:
                        canvas.destroy()
                        this.ctx.placeOrderPage()
                    elif orderButton in closest or orders in closest:
                        canvas.destroy()
                        this.ctx.viewOrderPage()
                    elif cancelButton in closest or cancelled in closest:
                        canvas.destroy()
                        this.ctx.cancelOrderPage()
                    elif(trackButton in closest):
                        canvas.destroy()
                        this.ctx.trackOrderPage()
                    elif(reportButton in closest):
                        canvas.destroy()
                        this.ctx.reportOrderPage()

        canvas.bind('<Button>', clicked)
        n.nav(canvas,258,0)

       